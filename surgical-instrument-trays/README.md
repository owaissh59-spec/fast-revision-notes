# Surgical Instrument Trays — Examination Notes

**Deliverable:** `Surgical_Instrument_Trays_Notes.docx` (700 KB) — cover,
contents, "how to read", then straight into the 49 trays.

**If that file will not download**, an identical split set is in
`notes_by_part/` — eleven smaller files of 72–276 KB, one per Part, each
self-contained with its own cover page and table of contents. Same content,
same formatting; all eleven pass the same verification checks.

Complete illustrated notes covering all 49 trays in the *Preparation of
Instruments Tray* syllabus, plus a foundation section on the principles the
whole topic rests on.

## Document specification

| Requirement | Delivered |
|---|---|
| Page size | US Legal — 8.5 × 14 in (21.59 × 35.56 cm) |
| Margins | 1.27 cm on all four sides |
| Table of contents | Two-column **table** — tray name + live page number |
| Page numbers | `PAGEREF` field per row (59), refreshed with Ctrl+A then F9 |
| Bookmarks | 61 — one on every Part and every chapter heading |
| Field refresh | `updateFields=true`, so Word offers to update on open |
| Page breaks | 12 total — **only between Parts**; chapters run on continuously |
| Instrument tables | No blank cells: every one of 1,748 rows has a key feature |
| Colour | Fully monochrome — greys, rules, borders and weight only |
| Figures | 63, embedded; tray plates sit in a **side column** beside the text |
| Figure resolution | ~200 dpi at printed size (600–1040 px wide), 8 grey levels |
| Running head/foot | Topic name in the header, page number in the footer |
| Tables | Header rows repeat automatically across page breaks |

### Updating the table of contents
Open in Word, click in the contents list, press **Ctrl+A** then **F9**, and
choose *Update entire table*. Page numbers fill in from the bookmarks.

## Contents

The main document opens with the cover, the contents table and a one-page
"How to read these notes", then goes directly into the trays.

- **Part I — General Surgery** (10): major, basic/minor, limited, thyroid,
  long instruments, biliary, choledochoscopy, sigmoidoscopy,
  gastrointestinal, rectal.
- **Part II — Gynaecologic & Obstetric** (6): D&C, cervical cone,
  laparoscopy, abdominal hysterectomy, caesarean section, vaginal
  hysterectomy.
- **Part III — Genitourinary** (3): vasectomy, open prostatectomy, kidney.
- **Part IV — Thoracic** (3): mediastinoscopy, thoracotomy, pacemaker.
- **Part V — Cardiovascular** (3): vascular, vascular shunt, cardiac.
- **Part VI — Orthopaedic** (4): basic, minor, hip replacement,
  knee/ankle arthroscopy.
- **Part VII — Neurologic** (2): craniotomy, laminectomy.
- **Part VIII — ENT** (6): basic ear, nasal, myringotomy, T&A,
  tracheostomy, antral puncture.
- **Part IX — Ophthalmic** (9): basic eye, eyelid and conjunctiva, eye
  muscle, dacryocystorhinostomy, cornea, cataract and lens, glaucoma,
  microscope, retina.
- **Part X — Paediatric** (3): major, minor, gastrointestinal.

### Foundations (kept separate)

The groundwork chapters — classification into the six functional groups,
instrument anatomy and grips, principles of tray preparation, reprocessing
and sterilisation, back-table and Mayo-stand set-up, the surgical count, and
care of instruments — are **not** in the main document, which starts at the
trays. They are kept as a standalone file:

`notes_by_part/00_Foundations_of_Instrument_Tray_Preparation.docx`

Worth keeping to hand: "Preparation of Instruments Tray" as a syllabus
heading usually expects the principles as well as the lists.

Every tray chapter follows the same structure: lead paragraph → indications
→ side figure → grouped instrument table with quantities and rationale →
comparison table where useful → memory hook → examination pointers →
common mistakes → likely examination questions with model answers.

## About the figures

All 63 figures are **original line diagrams generated for this document**.
Wikimedia Commons was tried first but rate-limited requests and returned
poor matches for specific instrument names, so a small vector-style drawing
engine was written instead. This gives correct, correctly-labelled,
pure-black-and-white diagrams that print cleanly on a monochrome printer and
carry no licensing restrictions.

They are **schematic study diagrams, not photographs** — drawn to show the
feature that identifies each instrument (jaw pattern, bevel, curve,
footplate) rather than to be photorealistic.

## Rebuilding

```bash
pip install python-docx Pillow
python3 scripts/build.py Surgical_Instrument_Trays_Notes.docx   # single file
python3 scripts/build.py --split                                # 11 per-part files
```

### Checks
```bash
python3 scripts/verify_docx.py Surgical_Instrument_Trays_Notes.docx  # page setup, TOC, bookmarks, monochrome
python3 scripts/validate_keys.py                                     # every figure reference resolves
python3 scripts/check_coverage.py                                    # all 49 syllabus trays present
```

### Source layout

| File | Purpose |
|---|---|
| `scripts/artlib.py` | Drawing engine — canvas, strokes, textures, and the core instrument builders |
| `scripts/artlib2.py` | Specialty builders — specula, dilators, endoscopes, bone, vascular, ENT, thoracic |
| `scripts/registry.py` | 112 named instruments + the plate renderer (auto-measures each row) |
| `scripts/diagrams.py` | 10 conceptual figures — classification chart, back table, count sequence, etc. |
| `scripts/docxkit.py` | Word building blocks — page setup, styles, TOC, bookmarks, tables, side-column layout |
| `scripts/schema.py` | Content constructors |
| `scripts/features.py` | Key-feature text for rows that would otherwise have a blank notes cell, with tray-specific overrides where the rationale differs by site |
| `scripts/content_*.py` | The notes themselves, one module per Part |
| `scripts/build.py` | Renders content modules into the final `.docx` |

## Caveat

Pagination could not be verified in this environment (no Word or
LibreOffice available), so the exact page count is unknown until you open
the file and update the table of contents. Everything else in the table
above was verified programmatically against the document XML.
