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
                     part_banner, chapter_head, sub_head, mini_head, box,
                     two_col, cell_para, cell_mini_head, cell_bullet,
                     cell_box, figure, instrument_table, simple_table,
                     para, bullet, numbered, rule, page_break,
                     update_fields_on_open, spacing, indent, keep_together,
                     BODY_W, G_BOX, G_BOX2, FONT_HEAD, _rich)
from registry import plate as make_plate, detail_plate as make_detail
from diagrams import DIAGRAMS

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
def render_tray(doc, tray, part_no):
    """Render one tray/chapter."""
    if tray.get("newpage"):
        page_break(doc)

    chapter_head(doc, tray["no"], tray["title"], aka=tray.get("aka"),
                 bm=f"tray_{tray['no'].replace('.', '_')}")

    # ---- lead paragraph + side figure ------------------------------------
    plate_spec = tray.get("plate")
    side_box = tray.get("side_box")
    side_figs = [f for f in tray.get("figs", []) if f.get("side")]
    has_side = bool(plate_spec or side_box or side_figs)

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
        if side_box:
            cell_box(right, side_box.get("title"), side_box["lines"])

    # ---- instrument table ------------------------------------------------
    if tray.get("groups"):
        is_foundation = part_no == "0"
        gt = tray.get("groups_title") or (
            "Detailed notes" if is_foundation else "Contents of the tray")
        sub_head(doc, gt)
        head = (("", "Item", "Explanation") if is_foundation
                else ("Qty", "Instrument", "Notes / rationale"))
        instrument_table(doc, tray["groups"], head=head,
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
    if tray.get("qa"):
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
    for tray in part["trays"]:
        render_tray(doc, tray, part["number"])


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
    # Levels 1–2 only: the eleven Parts and the fifty-eight chapters.
    # Deeper headings ("Contents of the tray", "Likely examination
    # questions") repeat in every chapter and would only clutter the list.
    toc(doc, levels="1-2",
        note="To fill in the page numbers: click anywhere in the list "
             "below, press Ctrl+A then F9, and choose "
             "“Update entire table”.")

    for part in parts:
        render_part(doc, part)

    update_fields_on_open(doc)
    doc.save(out_path)
    return out_path


def load_parts():
    parts = []
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
    argv = sys.argv[1:]
    split = "--split" in argv
    argv = [a for a in argv if not a.startswith("--")]
    out = argv[0] if argv else os.path.join(
        ROOT, "Surgical_Instrument_Trays_Notes.docx")

    parts = load_parts()

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
    return path


if __name__ == "__main__":
    main()
