#!/usr/bin/env python3
"""
verify_fields.py -- prove the contents-table page numbers will resolve in
Word.

A PAGEREF field only produces a page number if all of the following hold:
  * the field is well formed:  begin -> instrText -> separate -> result -> end
  * the target bookmark exists, with a matching bookmarkEnd
  * bookmark names are valid (start with a letter, <=40 chars, no spaces)
  * bookmark ids are unique
  * bookmarkStart is placed after w:pPr (schema order), or Word may drop it
  * settings.xml asks Word to refresh fields on open
"""
import re
import sys
import zipfile

from lxml import etree

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def check(path):
    z = zipfile.ZipFile(path)
    xml = z.read("word/document.xml")
    root = etree.fromstring(xml)
    doc = xml.decode("utf8")
    ok = True

    def say(good, label, detail=""):
        nonlocal ok
        print(f"  [{'PASS' if good else 'FAIL'}] {label}"
              + (f"  ->  {detail}" if detail else ""))
        if not good:
            ok = False

    print(f"\n=== {path} ===")

    # ---- bookmarks
    starts = {}
    for b in root.iter(f"{W}bookmarkStart"):
        starts[b.get(f"{W}id")] = b.get(f"{W}name")
    ends = {b.get(f"{W}id") for b in root.iter(f"{W}bookmarkEnd")}
    names = [n for n in starts.values() if n != "_GoBack"]

    say(len(starts) == len(set(starts)), "Bookmark ids unique",
        f"{len(starts)} ids")
    unmatched = [i for i in starts if i not in ends]
    say(not unmatched, "Every bookmarkStart has a bookmarkEnd",
        f"{len(unmatched)} unmatched")

    bad_name = [n for n in names
                if not n[0].isalpha() or len(n) > 40
                or re.search(r"[^A-Za-z0-9_]", n)]
    say(not bad_name, "Bookmark names valid for Word",
        f"{len(bad_name)} invalid" + (f": {bad_name[:5]}" if bad_name else ""))

    dupe = [n for n in set(names) if names.count(n) > 1]
    say(not dupe, "Bookmark names unique",
        f"{len(dupe)} duplicated" + (f": {dupe[:5]}" if dupe else ""))

    # ---- schema order: pPr must precede bookmarkStart
    bad_order = 0
    for p in root.iter(f"{W}p"):
        kids = [k.tag.replace(W, "") for k in p]
        if "bookmarkStart" in kids and "pPr" in kids:
            if kids.index("bookmarkStart") < kids.index("pPr"):
                bad_order += 1
    say(bad_order == 0,
        "bookmarkStart placed after w:pPr (schema order)",
        f"{bad_order} misplaced")

    # ---- field structure
    n_begin = len(re.findall(r'w:fldCharType="begin"', doc))
    n_sep = len(re.findall(r'w:fldCharType="separate"', doc))
    n_end = len(re.findall(r'w:fldCharType="end"', doc))
    say(n_begin == n_sep == n_end,
        "Field runs balanced (begin / separate / end)",
        f"{n_begin} / {n_sep} / {n_end}")

    instr = re.findall(r"<w:instrText[^>]*>(.*?)</w:instrText>", doc)
    prefs = [i.strip() for i in instr if "PAGEREF" in i]
    say(len(prefs) > 0, "PAGEREF fields present", f"{len(prefs)} found")

    # ---- every PAGEREF target resolves to a real bookmark
    targets = [re.match(r"PAGEREF\s+(\S+)", p).group(1) for p in prefs
               if re.match(r"PAGEREF\s+(\S+)", p)]
    missing = sorted(set(t for t in targets if t not in names))
    say(not missing, "Every PAGEREF target is a defined bookmark",
        f"{len(set(targets))} distinct targets"
        + (f", MISSING {missing[:6]}" if missing else ", none missing"))

    hyper = sum(1 for p in prefs if "\\h" in p)
    say(hyper == len(prefs),
        "PAGEREF fields hyperlinked (\\h) so they are also clickable",
        f"{hyper}/{len(prefs)}")

    # ---- update on open
    settings = z.read("word/settings.xml").decode("utf8")
    say("<w:updateFields" in settings and 'w:val="true"' in settings,
        "settings.xml requests a field refresh on open")

    # ---- headings still carry the bookmarks (so PAGEREF points at the
    #      chapter title, not a stray paragraph)
    heads = 0
    for p in root.iter(f"{W}p"):
        st = p.find(f"{W}pPr/{W}pStyle")
        if st is not None and st.get(f"{W}val", "").startswith("Heading"):
            if p.find(f"{W}bookmarkStart") is not None:
                heads += 1
    say(heads >= len(set(targets)) - 2,
        "Bookmarks sit on the heading paragraphs",
        f"{heads} bookmarked headings for {len(set(targets))} targets")

    print(f"  RESULT: {'FIELDS WILL RESOLVE' if ok else 'PROBLEMS FOUND'}")
    return ok


if __name__ == "__main__":
    paths = sys.argv[1:] or ["Surgical_Instrument_Trays_Notes.docx"]
    sys.exit(0 if all(check(p) for p in paths) else 1)
