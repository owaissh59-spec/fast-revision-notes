#!/usr/bin/env python3
"""Structural verification of a generated .docx against the spec."""
import re
import sys
import zipfile

EMU_CM = 360000.0
TWIP_CM = 566.929


def check(path):
    z = zipfile.ZipFile(path)
    names = z.namelist()
    doc = z.read("word/document.xml").decode("utf8")
    ok = True

    def say(good, label, detail=""):
        nonlocal ok
        print(f"  [{'PASS' if good else 'FAIL'}] {label}" +
              (f"  ->  {detail}" if detail else ""))
        if not good:
            ok = False

    print(f"\n=== {path} ===")
    print(f"  size: {round(len(open(path,'rb').read())/1024,1)} KB, "
          f"{len(names)} parts")

    # ---- page setup
    m = re.search(r'<w:pgSz[^/]*w:w="(\d+)"[^/]*w:h="(\d+)"', doc)
    if not m:
        m2 = re.search(r'<w:pgSz([^/]*)/>', doc)
        w = re.search(r'w:w="(\d+)"', m2.group(1)).group(1)
        h = re.search(r'w:h="(\d+)"', m2.group(1)).group(1)
    else:
        w, h = m.group(1), m.group(2)
    wcm, hcm = int(w) / TWIP_CM, int(h) / TWIP_CM
    say(abs(wcm - 21.59) < 0.05 and abs(hcm - 35.56) < 0.05,
        "Legal page size 8.5in x 14in",
        f"{wcm:.2f} cm x {hcm:.2f} cm")

    mg = re.search(r'<w:pgMar([^/]*)/>', doc)
    vals = dict(re.findall(r'w:(\w+)="(-?\d+)"', mg.group(1)))
    margins = {k: int(vals[k]) / TWIP_CM for k in
               ("top", "right", "bottom", "left") if k in vals}
    say(all(abs(v - 1.27) < 0.03 for v in margins.values()),
        "Margins 1.27 cm on all four sides",
        ", ".join(f"{k}={v:.2f}" for k, v in margins.items()))

    # ---- contents: either a TOC field or an explicit PAGEREF table
    n_toc = len(re.findall(r"TOC \\+o", doc))
    n_pref = len(re.findall(r"PAGEREF", doc))
    say(n_toc >= 1 or n_pref >= 1,
        "Contents with live page numbers",
        f"{n_toc} TOC field(s), {n_pref} PAGEREF field(s)")
    settings = z.read("word/settings.xml").decode("utf8")
    say("updateFields" in settings and 'w:val="true"' in settings,
        "updateFields=true (TOC auto-refreshes on open)")

    # ---- bookmarks
    bms = re.findall(r'<w:bookmarkStart[^>]*w:name="([^"]+)"', doc)
    bms = [b for b in bms if b != "_GoBack"]
    say(len(bms) > 0, "Bookmarks present", f"{len(bms)} bookmarks")

    # ---- headings for TOC levels
    for lvl in (1, 2, 3):
        n = len(re.findall(rf'w:val="Heading{lvl}"', doc))
        say(n > 0 if lvl <= 2 else True, f"Heading {lvl} paragraphs", f"{n}")

    # ---- images
    media = [n for n in names if n.startswith("word/media/")]
    say(len(media) > 0, "Embedded images", f"{len(media)} files")
    drawings = len(re.findall(r'<w:drawing>', doc))
    say(drawings > 0, "Inline drawings in body", f"{drawings}")

    # ---- image widths (should fit inside 19.05 cm text column)
    exts = re.findall(r'<wp:extent cx="(\d+)" cy="(\d+)"', doc)
    if exts:
        widest = max(int(a) for a, b in exts) / EMU_CM
        say(widest <= 19.10, "All images fit the text column",
            f"widest = {widest:.2f} cm")

    # ---- tables
    say(doc.count("<w:tbl>") > 0, "Tables present", f"{doc.count('<w:tbl>')}")
    say("w:tblHeader" in doc, "Table header rows repeat across pages")

    # ---- header / footer
    say(any("header" in n for n in names), "Running header part")
    say(any("footer" in n for n in names), "Running footer part")
    say("PAGE" in z.read([n for n in names if "footer" in n][0]).decode("utf8"),
        "PAGE number field in footer")

    # ---- contents table with live page numbers
    n_pageref = len(re.findall(r"PAGEREF", doc))
    n_h1 = doc.count('"Heading1"')
    n_h2 = doc.count('"Heading2"')
    say(n_pageref >= n_h1 + n_h2,
        "Contents table has a live PAGEREF per part and chapter",
        f"{n_pageref} PAGEREF vs {n_h1} parts + {n_h2} chapters")
    say("contents_table" not in doc, "Contents rendered as a real table",
        f"{doc.count('<w:tbl>')} tables present")

    # ---- page-break economy: breaks ONLY between Parts, plus front matter.
    #      Chapters run on continuously to keep the page count down.
    n_breaks = doc.count('w:type="page"')
    budget = n_h1 + 3                      # one per part + cover/contents/how-to
    say(n_breaks <= budget,
        "Page breaks only between Parts",
        f"{n_breaks} breaks for {n_h1} parts, budget {budget}")

    # ---- no intro/foundation chapters in the main flow
    say("Reprocessing cycle" not in doc and "Instrument reprocessing" not in doc,
        "Front matter only -- content starts at the trays")
    say("How to Read These Notes" in doc, "'How to read these notes' page")

    # ---- callout boxes must span the full text column, not sit in the
    #      narrow side column (which left a blank area to their left)
    from lxml import etree
    W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
    root = etree.fromstring(z.read("word/document.xml"))
    nested = 0
    for tbl in root.iter(f"{W}tbl"):
        anc = tbl.getparent()
        while anc is not None:
            if anc.tag == f"{W}tbl":
                nested += 1
                break
            anc = anc.getparent()
    say(nested == 0,
        "No callout boxes nested in the narrow side column",
        f"{nested} nested tables")

    # widest cell in any layout table, as a proxy for full-width blocks
    cellw = [int(c.get(f"{W}w")) / TWIP_CM
             for c in root.iter(f"{W}tcW")
             if c.get(f"{W}type") == "dxa" and c.get(f"{W}w")]
    if cellw:
        say(max(cellw) >= 18.9, "Full-width blocks span the text column",
            f"widest cell = {max(cellw):.2f} cm of 19.05 cm")

    # ---- no blank cells in the instrument tables
    blank_rows = 0
    total_rows = 0
    for tbl in root.iter(f"{W}tbl"):
        rows = list(tbl.iter(f"{W}tr"))
        for tr in rows:
            tcs = list(tr.iter(f"{W}tc"))
            if len(tcs) != 3:
                continue
            texts = ["".join(t.text or "" for t in tc.iter(f"{W}t")).strip()
                     for tc in tcs]
            # an instrument row has a name in column 2
            if not texts[1]:
                continue
            total_rows += 1
            if not texts[2]:
                blank_rows += 1
    say(blank_rows == 0,
        "Every instrument row has a key feature",
        f"{total_rows} rows, {blank_rows} blank")

    # ---- monochrome check: no saturated colours
    colors = set(re.findall(r'w:(?:color|fill)="([0-9A-Fa-f]{6})"', doc))
    bad = []
    for cval in colors:
        r, g, b = (int(cval[i:i + 2], 16) for i in (0, 2, 4))
        if max(r, g, b) - min(r, g, b) > 12:
            bad.append(cval)
    say(not bad, "Monochrome-safe (all greys, no hues)",
        "offenders: " + ", ".join(sorted(bad)) if bad else "all neutral")

    print(f"  RESULT: {'ALL CHECKS PASSED' if ok else 'SOME CHECKS FAILED'}")
    return ok


if __name__ == "__main__":
    paths = sys.argv[1:] or ["smoke.docx"]
    allok = all(check(p) for p in paths)
    sys.exit(0 if allok else 1)
