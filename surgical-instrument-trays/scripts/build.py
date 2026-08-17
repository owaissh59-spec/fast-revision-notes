#!/usr/bin/env python3
"""
build.py -- renders the content modules into the final .docx.

Usage:  python3 scripts/build.py [output.docx]
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Cm, Pt, RGBColor

from docxkit import (new_document, set_header_footer, cover_page, toc,
                     contents_table, how_to_read,
                     part_banner, chapter_head, sub_head, mini_head, box,
                     two_col, cell_para, cell_mini_head, cell_bullet,
                     cell_box, figure, instrument_table, simple_table,
                     para, bullet, numbered, rule, chapter_rule, page_break,
                     update_fields_on_open, spacing, indent, keep_together,
                     BODY_W, G_BOX, G_BOX2, FONT_HEAD, _rich)
from registry import plate as make_plate, detail_plate as make_detail
from diagrams import DIAGRAMS
from features import feature_for

_missing_features = []

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
IMG = os.path.join(ROOT, "images")
os.makedirs(IMG, exist_ok=True)

SIDE_W = 6.5          # cm -- width of the side figure column
FULL_W = 13.4         # cm -- default width for a full-width figure

# Figures must be rendered with enough pixels for their PRINTED size, not
# their logical size. A 470-unit figure placed 13.4 cm wide is only ~90 dpi
# if saved 1:1, which prints soft. Choose the output scale from the target
# width so every figure lands at roughly TARGET_DPI.
TARGET_DPI = 200      # ample for pure line art on a laser printer
GREY_LEVELS = 8       # line art needs very few; halves the file size

# The long-answer "Likely examination questions" sections are excluded by
# default -- the target exam is MCQ based. Pass --with-qa to include them.
INCLUDE_QA = False


HOW_TO_READ_ROWS = [
    ("Lead paragraph",
     "What the tray is for and the single idea that shapes it. If you "
     "remember nothing else from a chapter, remember this."),
    ("Used for / includes",
     "The procedures the tray serves — useful for 'name three indications' "
     "questions."),
    ("Figure",
     "An original line diagram of the tray's **signature instruments** — "
     "the items that identify it. Diagrams are schematic: they show the "
     "identifying feature (jaw pattern, bevel direction, footplate, "
     "curve) rather than a photographic likeness."),
    ("Callout box",
     "The one concept, distinction or safety rule that examiners return to "
     "for that tray."),
    ("Contents of the tray",
     "The full instrument list, grouped by **function** — cutting, "
     "grasping, clamping, retracting, suturing, suctioning — with "
     "quantities and the reason each item is present. Answer 'enumerate "
     "the contents' questions using these groups as headings."),
    ("Additional supplies",
     "Position, draping, structures at risk and procedure-specific notes."),
    ("Comparison table",
     "Where two trays or two instruments are easily confused, they are set "
     "side by side."),
    ("Examination pointers",
     "The single most useful section for an MCQ paper: the specific, "
     "testable facts — named instruments, numbers, temperatures, sizes and "
     "the distinctions between similar items. Revise from these."),
    ("Common mistakes",
     "Errors that lose marks, marked with ✗ — most of them are the "
     "distractors an MCQ will offer you."),
    ("A note on quantities",
     "Instrument **names, functions and groupings** are standard. The "
     "**numbers** (\"6 Allis clamps\") vary between institutions — please "
     "cross-check them against your prescribed textbook."),
    ("Printing",
     "Legal paper (8.5 × 14 in), 1.27 cm margins, monochrome throughout. "
     "No information depends on colour, so a black-and-white printer loses "
     "nothing."),
]


def scale_for(logical_w, cm_w):
    """Output pixels per logical unit needed to hit TARGET_DPI on paper."""
    want_px = (cm_w / 2.54) * TARGET_DPI
    return max(1.0, min(3.0, want_px / float(logical_w)))

_fig_counter = {}
_rendered = set()


# --------------------------------------------------------------- figure cache
def render_plate(spec, key, cm_w):
    """Render a plate/detail/diagram spec to PNG (cached) -> path.

    `cm_w` is the width the figure will occupy on the page; it sets the
    output resolution so the figure prints at ~TARGET_DPI.
    """
    if spec["kind"] == "diagram":
        key = spec["name"]
    path = os.path.join(IMG, f"{key}.png")
    if key in _rendered and os.path.exists(path):
        return path

    if spec["kind"] == "plate":
        a = make_plate(spec["rows"], title=spec.get("title"),
                       width=spec.get("width") or 470, L=spec.get("L"),
                       foot=spec.get("foot"))
    elif spec["kind"] == "detail":
        a = make_detail(spec["items"], title=spec.get("title"),
                        width=spec.get("width") or 470,
                        cols=spec.get("cols", 3), r=spec.get("r", 30))
    elif spec["kind"] == "diagram":
        a = DIAGRAMS[spec["name"]]()
    else:
        raise ValueError(spec["kind"])

    a.save(path, scale=scale_for(a.w, cm_w), colors=GREY_LEVELS)
    _rendered.add(key)
    return path


# ------------------------------------------------------------------- renderers
def fill_features(tray):
    """
    Return the tray's instrument groups with every blank note filled in
    from features.py. A blank third column reads as an omission in a
    printed table, so no row is allowed to ship empty.
    """
    out = []
    for g in tray.get("groups", []):
        items = []
        for it in g["items"]:
            qty, name, note = (list(it) + ["", "", ""])[:3]
            if not str(note).strip():
                note = feature_for(name, tray["no"])
                if not note:
                    _missing_features.append((tray["no"], name))
                    note = ""
            items.append((qty, name, note))
        out.append({"group": g.get("group"), "items": items})
    return out


def render_tray(doc, tray, part_no, first_in_part=False):
    """Render one tray/chapter."""
    # Page breaks occur ONLY between Parts. Chapters run on continuously to
    # keep the page count (and the print bill) down, separated instead by a
    # heavy rule and generous space above the chapter heading.
    if not first_in_part:
        chapter_rule(doc)

    chapter_head(doc, tray["no"], tray["title"], aka=tray.get("aka"),
                 bm=f"tray_{tray['no'].replace('.', '_')}")

    # ---- lead paragraph + side figure ------------------------------------
    plate_spec = tray.get("plate")
    # The conceptual callout is rendered FULL WIDTH below the two-column
    # block. Putting it in the narrow side column used to leave a large
    # blank area to its left whenever the left-hand text ran short.
    side_box = tray.get("side_box")
    side_figs = [f for f in tray.get("figs", []) if f.get("side")]
    has_side = bool(plate_spec or side_figs)

    if has_side:
        left, right = two_col(doc, right_w=Cm(SIDE_W))
        target = left
    else:
        target = doc

    def emit_para(txt, style="TrayLead"):
        if target is doc:
            para(doc, txt, style=style)
        else:
            cell_para(target, txt, style=style)

    def emit_mini(txt):
        if target is doc:
            mini_head(doc, txt)
        else:
            cell_mini_head(target, txt)

    def emit_bullet(txt):
        if target is doc:
            bullet(doc, txt)
        else:
            cell_bullet(target, txt)

    if tray.get("lead"):
        emit_para(tray["lead"])

    if tray.get("uses"):
        emit_mini("Used for / includes")
        for u in tray["uses"]:
            emit_bullet(u)

    if tray.get("draping"):
        emit_mini("Draping & position")
        emit_para(tray["draping"], style="BoxBody")

    # ---- side column contents
    if has_side:
        n = 0
        if plate_spec:
            key = f"plate_{tray['no'].replace('.', '_')}"
            w = SIDE_W - 0.15
            p = render_plate(plate_spec, key, w)
            figure(right, p, w, caption=plate_spec.get("cap"))
            n += 1
        for i, f in enumerate(side_figs):
            w = f.get("w") or (SIDE_W - 0.15)
            p = render_plate(f, f.get("name") or
                             f"sfig_{tray['no'].replace('.', '_')}_{i}", w)
            figure(right, p, w, caption=f.get("cap"))
            n += 1

    # ---- conceptual callout, full width ----------------------------------
    if side_box:
        box(doc, side_box.get("title"), side_box["lines"], fill=G_BOX2)

    # ---- instrument table ------------------------------------------------
    if tray.get("groups"):
        is_foundation = part_no == "0"
        gt = tray.get("groups_title") or (
            "Detailed notes" if is_foundation else "Contents of the tray")
        sub_head(doc, gt)
        head = (("", "Item", "Explanation") if is_foundation
                else ("Qty", "Instrument", "Key feature / rationale"))
        instrument_table(doc, fill_features(tray), head=head,
                         name_w=Cm(8.0) if is_foundation else None,
                         qty_w=Cm(0.9) if is_foundation else Cm(1.5))

    # ---- extras ----------------------------------------------------------
    if tray.get("extras"):
        sub_head(doc, "Additional supplies and accessories", level=4)
        for label, txt in tray["extras"]:
            p = para(doc, f"**{label}** — {txt}", style="BoxBody")
            indent(p, left=0.3)

    # ---- non-side figures ------------------------------------------------
    for i, f in enumerate([f for f in tray.get("figs", [])
                           if not f.get("side")]):
        w = f.get("w") or FULL_W
        p = render_plate(f, f.get("name") or
                         f"fig_{tray['no'].replace('.', '_')}_{i}", w)
        figure(doc, p, w, caption=f.get("cap"))

    # ---- comparison table ------------------------------------------------
    if tray.get("compare"):
        c = tray["compare"]
        sub_head(doc, c.get("cap_head", "Comparison"), level=4) \
            if c.get("cap_head") else None
        simple_table(doc, c["head"], c["rows"], widths=c.get("widths"),
                     font_size=c.get("font_size", 9.2))
        if c.get("cap"):
            p = para(doc, c["cap"], style="FigCaption")
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # ---- mnemonic --------------------------------------------------------
    if tray.get("mnemonic"):
        m = tray["mnemonic"]
        box(doc, m.get("title", "Mnemonic"), m["lines"], fill=G_BOX2)

    # ---- exam pointers ---------------------------------------------------
    if tray.get("points"):
        box(doc, "Examination pointers", tray["points"], fill=G_BOX)

    # ---- pitfalls --------------------------------------------------------
    if tray.get("pitfalls"):
        box(doc, "Common mistakes to avoid", tray["pitfalls"], fill=G_BOX2,
            marker="✗")

    # ---- Q&A -------------------------------------------------------------
    # Omitted by default: the target exam (JKSSB Junior Pharmacist) is MCQ
    # based, so long-answer model answers are not useful. The content is
    # kept in the modules and can be restored with --with-qa.
    if INCLUDE_QA and tray.get("qa"):
        sub_head(doc, "Likely examination questions", level=4)
        for i, (q, ans) in enumerate(tray["qa"], 1):
            p = para(doc, "")
            spacing(p, before=4, after=1)
            indent(p, left=0.55, hanging=0.55)
            keep_together(p)
            r = p.add_run(f"Q{i}.  ")
            r.font.name = FONT_HEAD
            r.bold = True
            r.font.size = Pt(9.6)
            _rich(p, f"**{q}**")
            for rr in p.runs[1:]:
                rr.font.size = Pt(9.8)
            pa = para(doc, "", style="QBank")
            spacing(pa, before=0, after=5)
            indent(pa, left=1.05, hanging=0.5)
            ra = pa.add_run("A.  ")
            ra.font.name = FONT_HEAD
            ra.bold = True
            _rich(pa, ans)


def render_part(doc, part):
    page_break(doc)
    part_banner(doc, part["number"], part["title"], part.get("subtitle"))
    if part.get("intro"):
        p = para(doc, part["intro"], style="TrayLead")
        spacing(p, before=2, after=8)
    for i, tray in enumerate(part["trays"]):
        render_tray(doc, tray, part["number"], first_in_part=(i == 0))


# ------------------------------------------------------------------ front page
def build(parts, out_path, title="SURGICAL INSTRUMENT TRAYS",
          subtitle="Preparation of Instruments Tray"):
    doc = new_document()
    set_header_footer(doc, "Preparation of Instrument Trays",
                      "Complete Examination Notes")

    cover_page(
        doc, title, subtitle,
        ["Complete, illustrated examination notes",
         "General · Gynaecologic & Obstetric · Genitourinary · Thoracic",
         "Cardiovascular · Orthopaedic · Neurologic · ENT · Ophthalmic · "
         "Paediatric"],
        ["Legal (8.5 × 14 in) · 1.27 cm margins · monochrome print-ready",
         "Every figure is an original line diagram, drawn for clarity in "
         "black and white"])

    page_break(doc)
    # An explicit two-column contents TABLE. Each page number is a live
    # PAGEREF field aimed at that chapter's bookmark, so Ctrl+A then F9
    # fills every one of them in.
    entries = []
    for p in parts:
        entries.append((1, p["title"], f"part_{p['number']}"))
        for t in p["trays"]:
            entries.append(
                (2, f"{t['no']}   {t['title']}",
                 f"tray_{t['no'].replace('.', '_')}"))
    contents_table(
        doc, entries,
        note="The page numbers are live fields, shown as “—” until they are "
             "filled in.  **To update them: press Ctrl+A then F9** "
             "(on a Mac, Cmd+A then Fn+F9) — or right-click any number and "
             "choose “Update Field”. Word normally offers to do this when "
             "the file opens. Once updated, each number is also a link: "
             "Ctrl+click it to jump to that tray.")

    page_break(doc)
    how_to_read(
        doc, HOW_TO_READ_ROWS,
        note="Every tray chapter is built to the same pattern, so you can "
             "find the same kind of information in the same place each "
             "time. Read the //lead paragraph// and the //figure// first to "
             "fix the idea, then work through the contents table.")

    for part in parts:
        render_part(doc, part)

    update_fields_on_open(doc)
    doc.save(out_path)
    return out_path


def load_parts(include_foundations=False):
    """
    The main document starts directly at the trays. The Foundations part
    (classification, tray-preparation principles, reprocessing, counting,
    instrument care) is still built as a standalone file by --split, so
    nothing is lost.
    """
    parts = []
    if include_foundations:
        from content_foundations import FOUNDATIONS
        parts.append(FOUNDATIONS)

    for modname, attr in [
        ("content_general", "GENERAL"),
        ("content_gyn", "GYN"),
        ("content_gu", "GU"),
        ("content_thoracic", "THORACIC"),
        ("content_cardio", "CARDIO"),
        ("content_ortho", "ORTHO"),
        ("content_neuro", "NEURO"),
        ("content_ent", "ENT"),
        ("content_eye", "EYE"),
        ("content_peds", "PEDS"),
    ]:
        try:
            mod = __import__(modname)
            parts.append(getattr(mod, attr))
        except (ImportError, AttributeError) as e:
            print(f"  .. skipping {modname} ({e})")
    return parts


def _report(path, parts):
    n = sum(len(p["trays"]) for p in parts)
    print(f"  {os.path.basename(path):<52} "
          f"{n:>3} ch  {os.path.getsize(path)/1024:>7.0f} KB")


def main():
    global INCLUDE_QA
    argv = sys.argv[1:]
    split = "--split" in argv
    INCLUDE_QA = "--with-qa" in argv
    argv = [a for a in argv if not a.startswith("--")]
    out = argv[0] if argv else os.path.join(
        ROOT, "Surgical_Instrument_Trays_Notes.docx")

    parts = load_parts(include_foundations=split)

    if split:
        # One file per Part, for when a single large file is awkward to
        # download. Each is self-contained with its own cover and TOC.
        outdir = os.path.join(ROOT, "notes_by_part")
        os.makedirs(outdir, exist_ok=True)
        print("\nPer-part documents:")
        made = []
        for i, p in enumerate(parts):
            safe = re.sub(r"[^A-Za-z0-9]+", "_", p["title"]).strip("_")
            fn = os.path.join(outdir, f"{i:02d}_{safe}.docx")
            build([p], fn, title=p["title"].upper(),
                  subtitle=f"Part {p['number']} — Instrument Trays")
            _report(fn, [p])
            made.append(fn)
        print(f"\n{len(made)} files in {outdir}/")
        return made

    path = build(parts, out)
    print(f"\nWrote:")
    _report(path, parts)
    if _missing_features:
        print(f"\n  !! {len(_missing_features)} rows still have a blank "
              f"key feature:")
        for no, name in _missing_features[:40]:
            print(f"     {no}  {name}")
    else:
        print("  every instrument row has a key feature")
    return path


if __name__ == "__main__":
    main()
