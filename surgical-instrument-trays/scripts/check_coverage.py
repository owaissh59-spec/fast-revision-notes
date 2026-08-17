#!/usr/bin/env python3
"""Verify every tray in the user's syllabus is present, and every chapter
has at least one figure."""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

SYLLABUS = """
Major Procedures Tray
Basic / Minor procedures tray
Limited procedures tray
Thyroid Tray
Long Instruments tray
Biliary Tract Procedures tray
Choledochoscopy tray
Basic rigid Sigmoidoscopy tray
Gastrointestinal procedures tray
Rectal Procedures tray
Dilatation of the Cervix and Curettage of the Uterus (D&C) tray
Cervical Cone Tray
Laparoscopy tray
Abdominal Hysterectomy tray
Caesarian Section tray
Vaginal Hysterectomy tray
Vasectomy tray
Open Prostatectomy tray
Kidney tray
Mediastinoscopy tray
Thoracotomy tray
Pacemaker tray
Vascular procedures tray
Vascular shunt tray
Cardiac procedures tray
Basic Orthopaedic procedure tray
Minor Orthopaedic procedures tray
Hip replacement tray
Knee or Ankle Arthroscopy tray
Craniotomy tray
Laminectomy tray
Basic Ear procedures tray
Nasal procedures tray
Myringotomy tray
Tonsillectomy and Adenoidectomy Tray
Tracheostomy tray
Antral Puncture tray
Basic eye procedures tray
Eyelid and Conjunctional procedures tray
Basic Eye Muscle procedures tray
Dacryocystorhinostomy tray
Corneal Procedures tray
Cataract Extraction and Lens procedures tray
Glaucoma procedure tray
Basic Eye procedures Microscope tray
Retinal procedures tray
Pediatric major procedures trays
Pediatric minor procedures trays
Pediatric Gastrointestinal procedure trays
""".strip().splitlines()

MODULES = [
    ("content_foundations", "FOUNDATIONS"),
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
]

STOP = {"tray", "trays", "the", "of", "and", "a"}

# normalise British/American and syllabus spelling variants
SPELL = {
    "pediatric": "paediatric", "cesarian": "caesarean",
    "caesarian": "caesarean", "cesarean": "caesarean",
    "conjunctional": "conjunctival", "orthopedic": "orthopaedic",
    "esophageal": "oesophageal", "procedure": "procedures",
}


def toks(s):
    s = s.lower().replace("&", " ")
    s = re.sub(r"[^a-z0-9 ]", " ", s)
    out = set()
    for w in s.split():
        if not w or w in STOP:
            continue
        out.add(SPELL.get(w, w))
    return out


def main():
    chapters = []
    for modname, attr in MODULES:
        mod = __import__(modname)
        part = getattr(mod, attr)
        for t in part["trays"]:
            chapters.append((part["number"], t))

    print(f"Parts: {len(MODULES)}   Chapters: {len(chapters)}\n")

    # ---- syllabus coverage
    print("SYLLABUS COVERAGE")
    missing = []
    for item in SYLLABUS:
        want = toks(item)
        best, score = None, 0.0
        for pno, t in chapters:
            have = toks(t["title"]) | toks(t.get("aka") or "")
            if not want:
                continue
            s = len(want & have) / len(want)
            if s > score:
                best, score = (pno, t), s
        if score >= 0.5:
            pno, t = best
            print(f"  OK   {item:<58} -> {t['no']} {t['title']}")
        else:
            print(f"  MISS {item}")
            missing.append(item)

    # ---- figures per chapter
    print("\nFIGURES PER CHAPTER")
    nofig = []
    total_fig = 0
    for pno, t in chapters:
        n = (1 if t.get("plate") else 0) + len(t.get("figs", []))
        total_fig += n
        flag = "" if n else "   <-- NO FIGURE"
        if not n:
            nofig.append(t["no"])
        print(f"  {t['no']:<6} {n} fig  {t['title'][:52]}{flag}")

    # ---- richness
    print("\nCONTENT COMPLETENESS")
    rows = 0
    for pno, t in chapters:
        rows += sum(len(g["items"]) for g in t.get("groups", []))
    n_pts = sum(len(t.get("points", [])) for _, t in chapters)
    n_qa = sum(len(t.get("qa", [])) for _, t in chapters)
    n_cmp = sum(1 for _, t in chapters if t.get("compare"))
    n_box = sum(1 for _, t in chapters if t.get("side_box"))
    n_pit = sum(1 for _, t in chapters if t.get("pitfalls"))
    n_mn = sum(1 for _, t in chapters if t.get("mnemonic"))
    print(f"  instrument/table rows : {rows}")
    print(f"  figures               : {total_fig}")
    print(f"  exam pointers         : {n_pts}")
    print(f"  Q&A pairs             : {n_qa}")
    print(f"  comparison tables     : {n_cmp}")
    print(f"  side callout boxes    : {n_box}")
    print(f"  'common mistakes' box : {n_pit}")
    print(f"  mnemonic boxes        : {n_mn}")

    print("\nRESULT")
    ok = not missing and not nofig
    if missing:
        print(f"  {len(missing)} syllabus items unmatched: {missing}")
    if nofig:
        print(f"  chapters without a figure: {nofig}")
    if ok:
        print("  All 49 syllabus trays covered; every chapter has a figure.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
