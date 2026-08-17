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

    # ---- TOC
    n_toc = len(re.findall(r'TOC \\\\o', doc)) + len(re.findall(r'TOC \\o', doc))
    say(n_toc >= 1, "TOC field present", f"{n_toc} found")
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
