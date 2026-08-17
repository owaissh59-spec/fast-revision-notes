#!/usr/bin/env python3
"""Part III -- Genitourinary Trays."""
from schema import T, P, PL, DP, FIG, G, CMP

GU = P(
    "III", "Genitourinary Trays",
    "Vasectomy · Open prostatectomy · Kidney",
    intro="Urological trays span the extremes of scale. **Vasectomy** is one "
          "of the smallest sets in surgery; **open prostatectomy** works in "
          "the deepest, least accessible part of the pelvis; the **kidney "
          "tray** must handle a retroperitoneal organ approached through the "
          "flank, often requiring rib resection. All three share one need — "
          "the ability to control **urine and blood** and to leave "
          "**drainage** behind.",
    trays=[

        # ============================================================ 3.1
        T("3.1", "Vasectomy Tray",
          aka="Male sterilisation set · no-scalpel vasectomy tray",
          lead="**Vasectomy** divides and occludes the vas deferens on each "
               "side to produce permanent male sterilisation. It is a "
               "**limited tray** procedure performed under local "
               "anaesthesia through a tiny scrotal opening. The tray's only "
               "special requirement is a means to **isolate and hold the "
               "vas** without damaging the surrounding vessels.",
          uses=["Elective permanent male sterilisation",
                "Conventional (incisional) vasectomy",
                "No-scalpel vasectomy (NSV) technique",
                "Vasectomy with fascial interposition or cautery occlusion",
                "Occasionally: vasectomy before prostatectomy to prevent "
                "epididymo-orchitis"],
          plate=PL("Signature instruments",
                   [("scalpel_11", "No.11 blade — small stab incision"),
                    ("mosquito", "Mosquito forceps, curved"),
                    ("adson", "Fine toothed forceps"),
                    ("iris_scissors", "Fine scissors"),
                    ("needle_holder", "Needle holder, small")],
                   cap="Fig 3.1 — A limited tray plus vas-specific forceps"),
          groups=[
              G("Base set", [
                  ("1", "Limited procedures tray", "see 1.3"),
              ]),
              G("Vas-specific instruments", [
                  ("1", "Vas deferens fixation (ring) clamp",
                   "**signature item** — an extracutaneous ringed clamp "
                   "that traps and holds the vas against the scrotal skin"),
                  ("1", "Vas dissecting forceps, sharp-pointed curved",
                   "**signature item** of the no-scalpel technique — "
                   "punctures the skin and spreads the tissues, avoiding a "
                   "scalpel entirely"),
                  ("2", "Fine mosquito artery forceps, curved",
                   "isolating and occluding the divided ends"),
                  ("1", "Small Allis forceps", "holds the vas sheath"),
                  ("2", "Fine toothed and non-toothed forceps",
                   "skin and sheath handling"),
              ]),
              G("Cutting and occlusion", [
                  ("1", "Knife handle No.3 with No.11 or No.15 blade",
                   "conventional technique only"),
                  ("1", "Fine iris / tenotomy scissors",
                   "excising a segment of vas"),
                  ("1", "Fine needle-point cautery",
                   "intraluminal (mucosal) cautery occlusion"),
                  ("—", "Ligating clips or fine non-absorbable ties",
                   "occluding the cut ends"),
                  ("—", "Suture for fascial interposition",
                   "interposes the sheath between the ends — reduces "
                   "recanalisation"),
              ]),
              G("Anaesthesia and accessory", [
                  ("—", "Local anaesthetic (lignocaine 1–2 %) with syringe "
                   "and fine needle",
                   "skin weal and vasal nerve block"),
                  ("1", "Gallipot with antiseptic", ""),
                  ("—", "Small drape with a central aperture", ""),
                  ("—", "Gauze swabs, counted", ""),
                  ("—", "Two labelled specimen containers",
                   "**separate left and right vas segments** for "
                   "histological confirmation"),
                  ("—", "Scrotal support and dressing", ""),
                  ("1", "Needle holder with fine absorbable suture",
                   "skin closure — often not required in NSV"),
              ]),
          ],
          extras=[("Position", "Supine, legs slightly apart; the scrotum "
                   "shaved, prepared and supported on a towel."),
                  ("Counselling", "The procedure must be regarded as "
                   "**permanent and irreversible**; informed written "
                   "consent, discussion of failure rate (≈1 in 2000) and "
                   "the need for **post-operative semen analysis** are "
                   "part of preparation."),
                  ("Post-operative", "Contraception must continue until "
                   "azoospermia is confirmed, usually at 12 weeks or after "
                   "about 20 ejaculations."),
                  ("Complications", "Haematoma, infection, sperm granuloma, "
                   "chronic post-vasectomy pain, and recanalisation "
                   "causing failure.")],
          side_box={"title": "No-scalpel vasectomy",
                    "lines": ["Uses only **two special instruments**:",
                              "the **ringed vas fixation clamp**, and",
                              "the **sharp-pointed curved dissecting "
                              "forceps** that puncture and spread instead "
                              "of cutting.",
                              "Result: less bleeding, less haematoma, no "
                              "sutures, faster recovery."]},
          points=[
              "This is a **limited tray plus two instruments** — the "
              "**ring clamp** and the **sharp dissecting forceps**.",
              "Know the **no-scalpel technique** by name and its two "
              "instruments; it is the commonly examined modern method.",
              "**Two separate labelled specimen pots** — left and right — "
              "for histological confirmation of vas.",
              "**Fascial interposition** and **mucosal cautery** reduce "
              "recanalisation — name at least one.",
              "**Semen analysis at ~12 weeks** before relying on the "
              "procedure is a standard mark.",
          ],
          qa=[("Describe the vasectomy tray.",
               "A limited procedures tray plus vas-specific items: a ringed "
               "vas fixation clamp and sharp-pointed curved vas dissecting "
               "forceps (the two no-scalpel instruments); fine curved "
               "mosquito forceps and a small Allis clamp; a No.11 blade and "
               "fine iris scissors; needle-point cautery, clips or fine ties "
               "and suture for fascial interposition; local anaesthetic with "
               "syringe and fine needle; and two separately labelled "
               "specimen containers for the left and right vas segments."),
              ("What advice regarding contraception follows vasectomy?",
               "Contraception must be continued until azoospermia is "
               "confirmed by semen analysis, usually at about 12 weeks or "
               "after roughly 20 ejaculations, because sperm persist in the "
               "distal vas.")]),

        # ============================================================ 3.2
        T("3.2", "Open Prostatectomy Tray",
          aka="Retropubic / suprapubic (transvesical) prostatectomy tray",
          lead="Open prostatectomy enucleates the benign prostatic adenoma "
               "either **through the bladder** (suprapubic/transvesical) or "
               "**through the prostatic capsule** (retropubic, Millin). The "
               "field is the **deepest and narrowest in general surgery**, "
               "surrounded by a rich venous plexus. The tray is a major "
               "tray built for **depth, illumination, enucleation and "
               "control of venous bleeding**.",
          uses=["Benign prostatic hyperplasia with a very large gland "
                "(>80–100 g)",
                "BPH with a large bladder stone or diverticulum requiring "
                "open removal",
                "When TURP is unsuitable — urethral stricture, inability to "
                "position, ankylosis of hips",
                "Failed endoscopic surgery",
                "Simple prostatectomy for chronic retention with "
                "obstructive renal impairment"],
          plate=PL("Signature instruments",
                   [("deaver", "Deaver / deep pelvic retractor"),
                    ("right_angle", "Long right-angled forceps"),
                    ("needle_holder_long", "Needle holder, 25–30 cm"),
                    ("stone_forceps", "Stone / clot forceps"),
                    ("poole", "Suction — heavy bleeding")],
                   cap="Fig 3.2 — Depth, retraction and venous control"),
          groups=[
              G("Base set", [
                  ("1", "Complete major procedures tray", "see 1.1"),
                  ("1", "Complete long instruments tray",
                   "**mandatory** — the retropubic space is very deep"),
              ]),
              G("Exposure of the retropubic space", [
                  ("1", "Self-retaining retractor — Millin, Balfour or "
                   "Bookwalter ring system",
                   "**signature item** — holds the deep pelvic exposure"),
                  ("2", "Deaver retractors, extra-deep", ""),
                  ("2", "Malleable retractors",
                   "protect the bladder and rectum"),
                  ("1", "Bladder (Judd-Mason) retractor",
                   "purpose-made prostatectomy retractor"),
                  ("1", "Head-light or fibre-optic lighted retractor",
                   "**illumination is essential at this depth**"),
                  ("—", "Long moist packs", "pack the space and tamponade"),
              ]),
              G("Enucleation and gland handling", [
                  ("1", "Prostatic enucleator / adenoma spoon",
                   "**signature item** — develops the plane between "
                   "adenoma and capsule"),
                  ("2", "Long Allis / Babcock forceps",
                   "traction on the adenoma"),
                  ("1", "Millin capsule-incising scalpel with long handle",
                   "retropubic capsulotomy"),
                  ("1", "Boomerang / capsule needle",
                   "haemostatic capsular sutures"),
                  ("2", "Long curved Metzenbaum scissors",
                   "urethral division"),
                  ("1", "Stone / clot forceps",
                   "bladder calculi and organised clot"),
                  ("1", "Bladder neck (Denis Browne) retractor", ""),
              ]),
              G("Venous haemostasis — the central problem", [
                  ("6", "Long right-angled (Mixter) forceps",
                   "under-running the dorsal venous complex"),
                  ("4", "Long Rochester-Péan clamps", ""),
                  ("2", "Needle holders, 25 cm and 30 cm",
                   "deep suture ligation"),
                  ("—", "Absorbable suture 0/1 on a large half-circle needle",
                   "capsular and bladder-neck haemostatic sutures"),
                  ("—", "Ligature carrier and knot pusher",
                   "tying at depth"),
                  ("—", "Haemostatic agents — cellulose, gelatin sponge, "
                   "fibrin sealant", "adjuncts for capsular ooze"),
                  ("—", "Diathermy with long extension tip", ""),
                  ("—", "**Cross-matched blood, at least 2 units**",
                   "blood loss can be substantial and rapid"),
              ]),
              G("Drainage and catheters — always required", [
                  ("—", "Three-way irrigating Foley catheter, 22–24 Fr, "
                   "30 mL balloon",
                   "**signature requirement** — allows continuous bladder "
                   "irrigation to prevent clot retention"),
                  ("—", "Continuous bladder irrigation set with warm normal "
                   "saline", ""),
                  ("—", "Suprapubic (Malecot) catheter",
                   "in the transvesical approach"),
                  ("—", "Closed suction drain",
                   "retropubic space (prevents urinoma)"),
                  ("—", "Catheter introducer / stylet and lubricant", ""),
                  ("—", "Bladder syringe", "clot evacuation"),
                  ("—", "Urine drainage bags", ""),
                  ("1", "Specimen container", "adenoma weighed and sent"),
              ]),
              G("Endoscopic capability kept available", [
                  ("1", "Cystoscope with light source",
                   "assessing the bladder and urethra"),
                  ("1", "Resectoscope",
                   "if the plan may change to TURP"),
                  ("—", "Irrigation fluid on a stand", ""),
              ]),
          ],
          extras=[("Position", "Supine with slight Trendelenburg; legs "
                   "slightly apart. A sandbag under the sacrum improves "
                   "retropubic access."),
                  ("Approaches",
                   "**Retropubic (Millin)** — through the prostatic capsule, "
                   "better visualisation of the prostatic bed and bladder "
                   "neck. **Suprapubic (transvesical, Freyer)** — through "
                   "the bladder, preferred when there is a large bladder "
                   "stone or diverticulum to deal with."),
                  ("Complications",
                   "Haemorrhage and clot retention (commonest early), "
                   "urinary infection, incontinence, retrograde "
                   "ejaculation, bladder-neck stenosis, urethral stricture, "
                   "impotence, and osteitis pubis.")],
          side_box={"title": "Three-way catheter",
                    "lines": ["Its three channels are: **balloon "
                              "inflation**, **irrigation inflow** and "
                              "**drainage outflow**.",
                              "**Continuous bladder irrigation** through it "
                              "prevents clot retention — the commonest "
                              "early post-operative emergency.",
                              "Always name it as a **22–24 Fr with a 30 mL "
                              "balloon**."]},
          compare=CMP(
              ["", "Retropubic (Millin)", "Suprapubic (transvesical, Freyer)"],
              [["Route", "Through the prostatic capsule",
                "Through the bladder wall"],
               ["Bladder opened?", "No", "Yes"],
               ["Best when", "Pure prostatic enlargement",
                "Large bladder stone or diverticulum"],
               ["View of prostatic bed", "Excellent — direct",
                "Limited — from above"],
               ["Extra catheter", "Urethral only",
                "Urethral **plus** suprapubic"],
               ["Key retractor", "Millin self-retaining retractor",
                "Bladder (Judd-Mason) retractor"]],
              cap="Table 3.1 — The two open approaches compared"),
          points=[
              "State the **two approaches by name** — retropubic (Millin) "
              "and suprapubic/transvesical (Freyer) — and one indication "
              "for each.",
              "The **long instruments tray is mandatory**, not optional.",
              "**Venous haemostasis** dominates: long right-angled forceps, "
              "long needle holders, capsular sutures, haemostatic agents "
              "and cross-matched blood.",
              "The **three-way irrigating catheter with continuous bladder "
              "irrigation** is the most reliably examined item.",
              "**Illumination (head-light)** and a **retropubic drain** are "
              "easily earned marks.",
              "Name the **prostatic enucleator** as the gland-specific "
              "instrument.",
          ],
          qa=[("Describe the open prostatectomy tray.",
               "A major tray plus a complete long instruments tray; a "
               "Millin, Balfour or Bookwalter self-retaining retractor with "
               "extra-deep Deaver, malleable and Judd-Mason bladder "
               "retractors and a head-light; a prostatic enucleator with "
               "long Allis/Babcock forceps, Millin capsule scalpel, "
               "boomerang needle and stone/clot forceps; long right-angled "
               "Mixter forceps, 25–30 cm needle holders, heavy absorbable "
               "suture, ligature carrier, knot pusher and haemostatic "
               "agents with cross-matched blood; a 22–24 Fr three-way "
               "irrigating Foley with continuous irrigation, a suprapubic "
               "catheter for the transvesical route, a retropubic drain and "
               "a bladder syringe; plus a cystoscope kept available."),
              ("Why is a three-way catheter essential after prostatectomy?",
               "The prostatic bed bleeds freely and clot retention is the "
               "commonest early complication. A three-way catheter allows "
               "continuous bladder irrigation — separate inflow and outflow "
               "channels plus a balloon channel — which washes blood out "
               "before it clots and obstructs the bladder.")]),

        # ============================================================ 3.3
        T("3.3", "Kidney Tray",
          aka="Nephrectomy tray · renal / flank exploration set",
          lead="The kidney lies **retroperitoneally, high under the "
               "diaphragm and behind the ribs**. The standard flank "
               "approach frequently requires **removal or division of the "
               "12th (or 11th) rib**, so the kidney tray is unique among "
               "abdominal trays in carrying **bone and rib instruments** "
               "alongside major and vascular instruments — and it must "
               "handle the short, high-pressure renal pedicle.",
          uses=["Simple and radical nephrectomy for tumour or non-function",
                "Partial nephrectomy; nephron-sparing surgery",
                "Pyelolithotomy and nephrolithotomy for renal calculi",
                "Pyeloplasty for pelviureteric junction obstruction",
                "Nephroureterectomy; donor and transplant nephrectomy",
                "Drainage of a perinephric abscess; renal trauma "
                "exploration"],
          plate=PL("Signature instruments",
                   [("rib_shears", "Rib shears / rib cutter"),
                    ("rib_raspatory", "Doyen periosteal elevator"),
                    ("kidney_clamp", "Kidney pedicle clamp"),
                    ("stone_forceps", "Renal stone forceps"),
                    ("satinsky", "Satinsky vascular clamp"),
                    ("deaver", "Deep retractor")],
                   cap="Fig 3.3 — Bone, vascular and stone instruments "
                       "together"),
          groups=[
              G("Base set", [
                  ("1", "Complete major procedures tray", "see 1.1"),
                  ("1", "Long instruments tray",
                   "the renal pedicle is deep and high"),
              ]),
              G("Rib and bone instruments — unique to this tray", [
                  ("1", "Rib shears / rib cutter",
                   "**signature item** — divides the 12th or 11th rib"),
                  ("1", "Periosteal elevator (Doyen rib raspatory)",
                   "**signature item** — strips periosteum from the rib "
                   "before division"),
                  ("1", "Rib rongeur / bone nibbler",
                   "trims the cut rib end smooth"),
                  ("1", "Bone rasp / file", "smooths a sharp rib edge"),
                  ("1", "Rib spreader (Finochietto), small",
                   "if the pleura is entered or the space widened"),
                  ("1", "Gigli saw with handles", "alternative rib division"),
                  ("1", "Bone wax", "haemostasis of the cut rib"),
              ]),
              G("Vascular control of the renal pedicle", [
                  ("2", "Satinsky (side-biting) vascular clamps",
                   "**signature item** — partial occlusion of the renal "
                   "vein or vena cava"),
                  ("4", "Kidney pedicle clamps (Herrick / Guyon)",
                   "**signature item** — heavy clamps for the pedicle"),
                  ("4", "Bulldog clamps", "temporary small-vessel occlusion"),
                  ("4", "DeBakey vascular forceps, long",
                   "atraumatic vessel handling"),
                  ("2", "Potts-Smith angled vascular scissors",
                   "arteriotomy or venotomy"),
                  ("6", "Long right-angled (Mixter) forceps",
                   "encircling the artery and vein separately"),
                  ("—", "Vessel loops and umbilical tapes",
                   "slinging the pedicle and ureter"),
                  ("—", "Vascular suture 4-0/5-0 on a double-armed needle",
                   ""),
                  ("—", "Vascular staplers / clip appliers",
                   "pedicle control"),
                  ("—", "**Cross-matched blood**",
                   "renal haemorrhage is rapid and heavy"),
              ]),
              G("Stone and collecting-system instruments", [
                  ("4", "Randall renal stone forceps, graded angles",
                   "**signature item** — extracting calculi from the pelvis "
                   "and calyces"),
                  ("1", "Stone scoop and stone spoon", ""),
                  ("1", "Nephroscope with light source",
                   "intra-renal inspection for residual stones"),
                  ("1", "Ureteric catheters / stents (JJ)",
                   "splint the repair or the ureter"),
                  ("1", "Bougies and probes", "calibrate the pelvis and "
                   "ureter"),
                  ("—", "Fine absorbable suture 4-0/5-0",
                   "pelvis and ureteric closure — watertight"),
                  ("—", "Intra-operative ultrasound / radiography",
                   "locates residual calculi"),
              ]),
              G("Retraction and exposure", [
                  ("2", "Deaver retractors, deep", ""),
                  ("2", "Richardson retractors, large",
                   "flank muscle layers"),
                  ("2", "Malleable retractors",
                   "protects liver, spleen, colon and duodenum"),
                  ("1", "Self-retaining ring / Bookwalter retractor", ""),
                  ("1", "Kidney (Gil-Vernet) retractor",
                   "elevates the kidney"),
                  ("—", "Head-light", ""),
              ]),
              G("Drainage and closure", [
                  ("—", "Closed suction drain",
                   "**always** — retroperitoneal collections and urine "
                   "leak"),
                  ("—", "Chest drain with underwater seal",
                   "**kept ready** — the pleura is commonly opened during "
                   "rib resection"),
                  ("—", "Nephrostomy tube",
                   "where the collecting system is drained"),
                  ("—", "Urinary catheter", ""),
                  ("—", "Specimen container",
                   "kidney orientated and labelled; calculi sent separately "
                   "for analysis"),
              ]),
          ],
          extras=[("Position", "**Lateral decubitus (flank) position** with "
                   "the affected side up, the table broken to open the "
                   "space between the 12th rib and the iliac crest, a "
                   "kidney rest or bolster beneath the flank, the lower leg "
                   "flexed and the upper leg straight, with an axillary "
                   "roll. Anterior transperitoneal or thoraco-abdominal "
                   "approaches are used for large tumours."),
                  ("Structures at risk",
                   "**Pleura and diaphragm** superiorly (pneumothorax), "
                   "colon and duodenum medially, spleen on the left, liver "
                   "and vena cava on the right, and the ureter inferiorly."),
                  ("Order of pedicle ligation",
                   "In radical nephrectomy the **renal artery is ligated "
                   "before the vein**, to prevent venous engorgement of the "
                   "kidney.")],
          side_box={"title": "Why bone instruments are on a kidney tray",
                    "lines": ["The kidney lies **behind the 11th and 12th "
                              "ribs**.",
                              "The standard flank approach resects or "
                              "divides the **12th rib** for adequate "
                              "exposure.",
                              "Hence rib shears, periosteal elevator, "
                              "rongeur, rasp and bone wax — and a **chest "
                              "drain kept ready** because the pleura is "
                              "often opened."]},
          points=[
              "The kidney tray is the **only abdominal tray carrying rib "
              "instruments** — explain why (retroperitoneal position behind "
              "the 12th rib).",
              "Name the three signature groups: **rib instruments, pedicle/"
              "vascular clamps, Randall stone forceps**.",
              "**Artery before vein** in radical nephrectomy — a classic "
              "one-liner.",
              "A **chest drain must be immediately available** because the "
              "pleura is frequently breached.",
              "Describe the **lateral flank position with the table broken "
              "and a kidney rest** — positioning marks are commonly given.",
              "A **retroperitoneal drain is always left**, and calculi go "
              "for **stone analysis**.",
          ],
          qa=[("What is special about a kidney tray compared with other "
               "abdominal trays?",
               "It uniquely carries rib and bone instruments — rib shears, "
               "Doyen periosteal elevator, rib rongeur, rasp, Gigli saw, "
               "small rib spreader and bone wax — because the flank approach "
               "resects the 12th rib; it carries heavy renal pedicle clamps "
               "and Satinsky side-biting vascular clamps with vascular "
               "suture for the short high-pressure pedicle; it carries "
               "Randall stone forceps, scoops and a nephroscope for calculi; "
               "and a chest drain is kept ready because the pleura is "
               "frequently opened."),
              ("In radical nephrectomy, is the artery or the vein ligated "
               "first, and why?",
               "The renal artery is ligated first. Ligating the vein first "
               "would leave arterial inflow continuing into an obstructed "
               "venous outflow, causing engorgement, swelling and increased "
               "bleeding.")]),
    ])
