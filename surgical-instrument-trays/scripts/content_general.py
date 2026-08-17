#!/usr/bin/env python3
"""Part I -- General Surgery Trays."""
from schema import T, P, PL, DP, FIG, G, CMP

GENERAL = P(
    "I", "General Surgery Trays",
    "Major · Basic/Minor · Limited · Thyroid · Long instruments · Biliary · "
    "Choledochoscopy · Sigmoidoscopy · Gastrointestinal · Rectal",
    intro="Part I contains the three **reference trays** of the whole "
          "syllabus — limited, basic/minor and major — followed by seven "
          "general-surgical trays built upon them. Master these ten and the "
          "remaining forty become a matter of noting the speciality "
          "additions.",
    trays=[

        # ============================================================ 1.1
        T("1.1", "Major Procedures Tray",
          aka="Laparotomy tray · basic major tray · general exploratory tray",
          lead="The **major procedures tray** is the largest and most "
               "complete general set. It is designed for entry into a deep "
               "body cavity — usually the peritoneal cavity — and must "
               "provide instruments in every functional group, in both "
               "short and medium lengths, sufficient to open, explore, "
               "resect, repair and close without opening a second tray. "
               "Every other abdominal tray in this syllabus is this tray "
               "plus specific additions.",
          uses=["Exploratory laparotomy and trauma laparotomy",
                "Bowel resection and anastomosis",
                "Splenectomy, cholecystectomy, gastrectomy",
                "Appendicectomy (difficult or perforated)",
                "Abdominal hernia repair, incisional and recurrent",
                "As the base tray for biliary, GI, gynaecologic and "
                "urologic abdominal procedures"],
          plate=PL("Signature instruments",
                   [("scalpel_20", "No.4 handle + No.20 blade"),
                    ("mayo_curved", "Mayo scissors, curved"),
                    ("metzenbaum", "Metzenbaum scissors"),
                    ("kocher", "Kocher clamp — 1×2 teeth"),
                    ("richardson", "Richardson retractor"),
                    ("poole", "Poole suction tip")],
                   cap="Fig 1.1 — Instruments that define the major tray"),
          groups=[
              G("Cutting and dissecting", [
                  ("2", "Knife handle No.3", "for No.10 / No.15 blades"),
                  ("1", "Knife handle No.4", "for No.20 blade — skin "
                   "incision"),
                  ("1", "Knife handle No.7", "long, fine — deep dissection"),
                  ("1", "Mayo scissors, straight", "cutting suture"),
                  ("2", "Mayo scissors, curved", "heavy tissue, fascia"),
                  ("2", "Metzenbaum scissors, curved", "17 cm and 23 cm — "
                   "delicate dissection"),
                  ("1", "Wire / suture scissors", "protects fine scissors"),
              ]),
              G("Grasping and holding", [
                  ("2", "Tissue forceps, 1×2 teeth, 15 cm", "skin, fascia"),
                  ("2", "Tissue forceps, 1×2 teeth, 20 cm", "deeper layers"),
                  ("2", "Dressing (thumb) forceps, serrated, 15 cm",
                   "general handling"),
                  ("2", "DeBakey forceps, 20 cm & 24 cm",
                   "atraumatic — bowel, vessels"),
                  ("2", "Adson forceps, 1×2 teeth", "skin closure"),
                  ("6", "Allis tissue forceps", "tough tissue, wound edges"),
                  ("4", "Babcock forceps", "atraumatic — bowel, appendix"),
                  ("8", "Towel clips (Backhaus)", "securing drapes"),
                  ("4", "Sponge-holding forceps", "prep, swabbing, retraction"),
              ]),
              G("Clamping and occluding", [
                  ("12", "Mosquito (Halsted) forceps, curved",
                   "fine bleeding points"),
                  ("12", "Crile forceps, 14 cm, straight & curved",
                   "general haemostasis"),
                  ("8", "Kelly forceps, 16 cm, curved", "deeper vessels"),
                  ("6", "Rochester-Péan forceps, 20 cm",
                   "large pedicles and omentum"),
                  ("6", "Kocher (Ochsner) clamps",
                   "crushing — fascia, tissue to be excised"),
                  ("4", "Right-angled (Mixter) forceps",
                   "passing ligatures behind a pedicle"),
                  ("2", "Tonsil (Schnidt) forceps", "deep ligature work"),
              ]),
              G("Exposing and retracting", [
                  ("2", "Army-Navy retractors", "superficial layers"),
                  ("2", "Richardson retractors, medium & large",
                   "abdominal wall"),
                  ("2", "Deaver retractors", "deep, narrow exposure"),
                  ("2", "Malleable (ribbon) retractors, 2.5 & 5 cm",
                   "shaped to need; protects viscera"),
                  ("1", "Balfour self-retaining retractor",
                   "with bladder blade — maintains laparotomy exposure"),
                  ("2", "Weitlaner retractor", "self-retaining, superficial"),
                  ("4", "Skin hooks / Senn retractors", "fine exposure"),
              ]),
              G("Suturing and stapling", [
                  ("4", "Needle holders, Mayo-Hegar, 15 cm & 20 cm",
                   "tungsten-carbide inserts preferred"),
                  ("1", "Needle holder, long 25 cm", "deep pelvic suturing"),
                  ("—", "Suture and needles",
                   "absorbable for viscera and fascia; non-absorbable for "
                   "skin; taper for bowel, cutting for skin"),
                  ("1", "Ligature carrier (Deschamps)", "deep pedicles"),
                  ("—", "Linear and linear-cutting staplers",
                   "available for bowel work"),
              ]),
              G("Suctioning, accessory and measuring", [
                  ("1", "Poole suction tip", "free peritoneal fluid"),
                  ("1", "Yankauer suction tip", "localised suction"),
                  ("2", "Suction tubing", ""),
                  ("1", "Electrosurgical pencil with holster and tip cleaner",
                   ""),
                  ("2", "Probe and grooved director", "tracts and sinuses"),
                  ("2", "Kidney dish / gallipot", "specimens, irrigation"),
                  ("1", "Ruler / measuring tape", "specimen and defect size"),
                  ("—", "Laparotomy pads, radio-opaque", "counted in fives"),
              ]),
          ],
          extras=[("Position", "Supine, arms as required; table may be "
                   "tilted for exposure."),
                  ("Draping", "Four-towel square around the incision, then "
                   "a laparotomy sheet."),
                  ("Add-on packs kept ready",
                   "Bowel/GI stapler set, biliary set, vascular clamps, "
                   "self-retaining ring retractor, retrieval bags.")],
          side_box={"title": "Why it is 'major'",
                    "lines": ["Not because of the number of pieces but "
                              "because it provides **depth** — long "
                              "instruments, deep retractors and a "
                              "self-retaining retractor.",
                              "It carries **atraumatic** clamps (DeBakey, "
                              "Babcock) as well as crushing clamps, because "
                              "bowel and vessels must survive."]},
          compare=CMP(
              ["Haemostat", "Length", "Jaw serration", "Typical use"],
              [["Mosquito (Halsted)", "12–13 cm", "Fine, full length",
                "Small subcutaneous bleeders"],
               ["Crile", "14 cm", "Full length, transverse",
                "General haemostasis"],
               ["Kelly", "16 cm", "Distal half only", "Deeper vessels"],
               ["Rochester-Péan", "20 cm", "Full length, heavy",
                "Large pedicles, omentum"],
               ["Kocher (Ochsner)", "16–20 cm", "Full length **+ 1×2 teeth**",
                "Fascia; tissue to be excised"]],
              cap="Table 1.1 — The haemostat family in the major tray, in "
                  "increasing order of size"),
          mnemonic={"title": "Mnemonic — building the major tray",
                    "lines": ["**\"3-4-7\"** knife handles: No.3 (small "
                              "blades), No.4 (No.20 blade), No.7 (long "
                              "fine).",
                              "**\"M-M-M\"** scissors: **M**ayo straight "
                              "(suture), **M**ayo curved (tissue), "
                              "**M**etzenbaum (delicate).",
                              "**\"Mo-Cr-Ke-Ro-Ko\"** clamps in increasing "
                              "size: **Mo**squito → **Cr**ile → **Ke**lly → "
                              "**Ro**chester → **Ko**cher (toothed)."]},
          points=[
              "State clearly that the major tray must satisfy **all six "
              "functional groups in two or more lengths**.",
              "The **Balfour self-retaining retractor with bladder blade** "
              "is the item that marks a tray as a true laparotomy set.",
              "**Poole** suction (not Yankauer) is the answer for free fluid "
              "in the peritoneal cavity.",
              "Include **radio-opaque laparotomy pads** and the "
              "**four-point count** in any answer about a major tray.",
              "Long (25 cm) needle holder and No.7 handle are the "
              "instruments that give **depth**; mention them to distinguish "
              "major from basic.",
          ],
          pitfalls=["Listing only clamps and forceps and forgetting "
                    "retractors and suction.",
                    "Saying 'Yankauer' for free peritoneal fluid.",
                    "Omitting the self-retaining retractor.",
                    "Forgetting accessory items (electrosurgical pencil, "
                    "pads, kidney dish) which carry easy marks."],
          qa=[("Enumerate the contents of a major procedures tray.",
               "Answer under the six functional groups: cutting (No.3/4/7 "
               "handles, Mayo straight and curved, Metzenbaum, suture "
               "scissors); grasping (toothed and plain thumb forceps, "
               "DeBakey, Adson, Allis, Babcock, towel clips, sponge "
               "holders); clamping (mosquito, Crile, Kelly, "
               "Rochester-Péan, Kocher, right-angled, tonsil); retracting "
               "(Army-Navy, Richardson, Deaver, malleable, Balfour "
               "self-retaining, Weitlaner, Senn); suturing (Mayo-Hegar "
               "needle holders in three lengths, suture, ligature carrier, "
               "staplers); suction and accessory (Poole, Yankauer, "
               "electrosurgical pencil, probe, grooved director, kidney "
               "dish, radio-opaque pads)."),
              ("How does a major tray differ from a basic tray?",
               "By depth and range: the major tray adds long instruments "
               "(No.7 handle, 20–25 cm clamps and needle holders), deep "
               "retractors (Deaver, malleable), a self-retaining retractor "
               "(Balfour with bladder blade), atraumatic bowel and vascular "
               "clamps, and Poole suction for free cavity fluid.")]),

        # ============================================================ 1.2
        T("1.2", "Basic / Minor Procedures Tray",
          aka="Minor set · general minor tray · basic soft-tissue tray",
          lead="The **basic (minor) procedures tray** is the "
               "general-purpose small set and the single most widely used "
               "tray in any hospital. It covers clean, superficial, "
               "short-duration procedures that do not enter a major body "
               "cavity. It is the reference set from which most speciality "
               "trays are constructed, so its contents must be known "
               "exactly.",
          uses=["Excision of superficial lumps, cysts and lipomata",
                "Incision and drainage of abscesses",
                "Wound debridement and secondary suturing",
                "Lymph node and soft-tissue biopsy",
                "Simple hernia repair in a thin patient",
                "Insertion of central venous access devices and ports",
                "Base tray for minor ENT, ophthalmic, orthopaedic and "
                "gynaecologic procedures"],
          plate=PL("Signature instruments",
                   [("scalpel_15", "No.3 handle + No.15 blade"),
                    ("mayo_straight", "Mayo scissors, straight"),
                    ("metzenbaum", "Metzenbaum scissors"),
                    ("adson", "Adson forceps, 1×2 teeth"),
                    ("senn", "Senn retractor"),
                    ("needle_holder", "Needle holder, 15 cm")],
                   cap="Fig 1.2 — The core of the basic/minor tray"),
          groups=[
              G("Cutting and dissecting", [
                  ("2", "Knife handle No.3", "with No.10 and No.15 blades"),
                  ("1", "Mayo scissors, straight", "suture cutting"),
                  ("1", "Mayo scissors, curved", "tissue"),
                  ("1", "Metzenbaum scissors, 14 cm", "fine dissection"),
                  ("1", "Iris scissors", "very fine trimming"),
              ]),
              G("Grasping and holding", [
                  ("2", "Adson forceps, 1×2 teeth", "skin"),
                  ("2", "Tissue forceps, 1×2 teeth, 13 cm", "fascia"),
                  ("2", "Dressing forceps, serrated, 13 cm",
                   "general handling"),
                  ("4", "Allis tissue forceps", "wound edges, specimens"),
                  ("4", "Towel clips", "drapes"),
                  ("2", "Sponge-holding forceps", "prep and swabbing"),
              ]),
              G("Clamping and occluding", [
                  ("6", "Mosquito forceps, curved", "fine bleeders"),
                  ("6", "Crile forceps, 14 cm", "haemostasis"),
                  ("2", "Kelly forceps, curved", "slightly deeper vessels"),
                  ("2", "Kocher clamps", "tough fascia"),
              ]),
              G("Exposing and retracting", [
                  ("2", "Senn (double-ended) retractors",
                   "blade one end, rake the other"),
                  ("2", "Army-Navy retractors", "small wounds"),
                  ("1", "Weitlaner self-retaining retractor",
                   "frees an assistant's hands"),
                  ("2", "Skin hooks", "delicate skin edges"),
              ]),
              G("Suturing", [
                  ("2", "Needle holders, Mayo-Hegar 15 cm", ""),
                  ("—", "Suture with needles",
                   "absorbable subcutaneous; non-absorbable or staples to "
                   "skin"),
              ]),
              G("Suctioning and accessory", [
                  ("1", "Yankauer or Frazier suction tip",
                   "Frazier if the field is small and fine"),
                  ("1", "Electrosurgical pencil", ""),
                  ("1", "Probe and grooved director",
                   "sinus and fistula tracts"),
                  ("1", "Curette, small", "abscess cavity, granulation"),
                  ("1", "Kidney dish and gallipot", ""),
                  ("—", "Gauze swabs, radio-opaque", "counted"),
              ]),
          ],
          side_box={"title": "Why this tray matters most",
                    "lines": ["It is the **commonest tray in the "
                              "hospital**, and the **reference set** for "
                              "the majority of speciality trays.",
                              "Examiners often ask you to //convert// it: "
                              "'what would you add to a minor tray for a "
                              "thyroidectomy / a D&C / a tracheostomy?'"]},
          compare=CMP(
              ["", "Limited tray", "Basic / minor tray", "Major tray"],
              [["Depth of field", "Skin and subcutaneous only",
                "Superficial + small cavity", "Deep body cavity"],
               ["Longest instrument", "≈ 14 cm", "≈ 16 cm", "≈ 25 cm"],
               ["Retractors", "Skin hooks, Senn",
                "Senn, Army-Navy, Weitlaner",
                "Richardson, Deaver, malleable, Balfour"],
               ["Suction", "Often none", "Yankauer / Frazier",
                "Poole + Yankauer"],
               ["Approx. item count", "15–25", "40–60", "80–120"]],
              cap="Table 1.2 — Where the basic tray sits between limited "
                  "and major"),
          points=[
              "Learn this tray **item by item** — it is the commonest "
              "single-tray question and the base for conversions.",
              "The basic tray does **not** contain a self-retaining "
              "abdominal retractor, long instruments or Poole suction — "
              "these mark the major tray.",
              "**Senn retractor** is double-ended: a flat blade at one end "
              "and three sharp prongs at the other.",
              "Always mention **counted radio-opaque swabs** even in a "
              "minor tray.",
          ],
          qa=[("List the contents of a basic minor procedures tray.",
               "No.3 knife handles with No.10/15 blades; Mayo straight and "
               "curved, Metzenbaum and iris scissors; Adson, toothed and "
               "plain thumb forceps; Allis forceps; towel clips; sponge "
               "holders; mosquito, Crile, Kelly and Kocher clamps; Senn, "
               "Army-Navy and Weitlaner retractors with skin hooks; "
               "Mayo-Hegar needle holders with suture; Yankauer or Frazier "
               "suction; electrosurgical pencil; probe, grooved director, "
               "small curette, kidney dish and counted radio-opaque "
               "swabs."),
              ("Give three procedures for which a minor tray is "
               "appropriate.",
               "Excision of a sebaceous cyst or lipoma; incision and "
               "drainage of an abscess; lymph-node biopsy (also central "
               "line insertion, wound debridement, simple hernia "
               "repair).")]),

        # ============================================================ 1.3
        T("1.3", "Limited Procedures Tray",
          aka="Minimal set · local procedures tray · 'cut-down' tray",
          lead="The **limited procedures tray** is the smallest standard "
               "set. It carries only what is needed for a very "
               "superficial, brief procedure performed under local "
               "anaesthesia, usually outside the main theatre — in a "
               "treatment room, day-case unit or emergency department. Its "
               "purpose is economy: processing a full minor tray for a "
               "two-minute procedure wastes instruments and money.",
          uses=["Excision or shave biopsy of a small skin lesion",
                "Punch biopsy and simple skin suturing",
                "Removal of a foreign body from soft tissue",
                "Toenail avulsion; simple nail-bed procedures",
                "Venous cut-down; removal of a tunnelled line",
                "Suture removal and minor wound care"],
          plate=PL("Signature instruments",
                   [("scalpel_15", "No.3 handle + No.15 blade"),
                    ("iris_scissors", "Iris scissors"),
                    ("adson", "Adson forceps, 1×2 teeth"),
                    ("mosquito", "Mosquito forceps, curved"),
                    ("needle_holder", "Needle holder, 13 cm")],
                   cap="Fig 1.3 — Everything the limited tray really needs"),
          groups=[
              G("Cutting and dissecting", [
                  ("1", "Knife handle No.3", "with No.15 blade"),
                  ("1", "Iris scissors, curved", "fine tissue and trimming"),
                  ("1", "Suture / Mayo scissors, straight",
                   "cutting suture only"),
              ]),
              G("Grasping and holding", [
                  ("1", "Adson forceps, 1×2 teeth", "skin edges"),
                  ("1", "Adson forceps, serrated", "atraumatic handling"),
                  ("2", "Allis forceps, small",
                   "holding the specimen (optional)"),
                  ("2", "Towel clips, small", "securing a small drape"),
              ]),
              G("Clamping", [
                  ("4", "Mosquito forceps, curved",
                   "the only haemostats required"),
                  ("2", "Crile forceps, small", "if slightly deeper"),
              ]),
              G("Retracting", [
                  ("2", "Skin hooks, single or double",
                   "gentle skin-edge retraction"),
                  ("1", "Senn retractor", "if any depth is anticipated"),
              ]),
              G("Suturing", [
                  ("1", "Needle holder, 13 cm", ""),
                  ("—", "Suture with swaged cutting needle",
                   "monofilament to skin"),
              ]),
              G("Accessory", [
                  ("1", "Gallipot", "antiseptic solution"),
                  ("1", "Kidney dish", "specimen and used items"),
                  ("1", "Small curette", "curetting a lesion base"),
                  ("—", "Gauze swabs, counted", ""),
                  ("—", "Local anaesthetic, syringe and needle",
                   "kept off the sterile field until required"),
              ]),
          ],
          side_box={"title": "Defining feature",
                    "lines": ["**No cavity is entered.** The tray has no "
                              "deep retractor, no long instrument and "
                              "usually no suction.",
                              "If suction, self-retaining retraction or "
                              "instruments longer than ≈14 cm are needed, "
                              "the correct choice is a **minor tray**, not "
                              "a limited tray."]},
          points=[
              "Define it by **what it lacks**: no deep retractors, no long "
              "instruments, typically no suction.",
              "Its justification is **economy and turnaround**, not "
              "clinical limitation.",
              "Even here the **count applies** — swabs and the blade must "
              "be accounted for.",
              "Commonly used **outside the main theatre**, so the tray "
              "must be self-sufficient (gallipot, kidney dish, swabs).",
          ],
          qa=[("What is a limited procedures tray and when is it used?",
               "The smallest standard set, containing only a No.3 handle "
               "with No.15 blade, iris and suture scissors, Adson forceps, "
               "a few mosquito forceps, skin hooks, a needle holder and "
               "basic accessories. It is used for very superficial, brief "
               "procedures under local anaesthesia — small skin lesion "
               "excision, punch biopsy, foreign-body removal, nail "
               "avulsion, venous cut-down — where no cavity is entered.")]),

        # ============================================================ 1.4
        T("1.4", "Thyroid Tray",
          aka="Thyroidectomy tray · neck exploration tray",
          lead="The thyroid gland is superficial but extremely vascular and "
               "lies among structures that must not be injured — the "
               "recurrent laryngeal nerve, the parathyroid glands, the "
               "trachea and the great vessels. The **thyroid tray** is "
               "therefore a basic tray upgraded for **meticulous "
               "haemostasis in a shallow but crowded field**: many fine "
               "haemostats, special gland-holding forceps and small "
               "right-angled retractors.",
          uses=["Total, subtotal and hemi-thyroidectomy",
                "Isthmusectomy and excision of a thyroid nodule",
                "Parathyroidectomy and parathyroid exploration",
                "Excision of a thyroglossal cyst",
                "Neck node biopsy and branchial cyst excision",
                "Retrosternal goitre (with a sternal saw available)"],
          plate=PL("Signature instruments",
                   [("lahey_clamp", "Lahey (goitre) vulsellum"),
                    ("mosquito", "Mosquito forceps — many"),
                    ("metzenbaum", "Metzenbaum scissors"),
                    ("right_angle", "Right-angled (Mixter) forceps"),
                    ("weitlaner", "Self-retaining retractor"),
                    ("frazier", "Frazier suction tip")],
                   cap="Fig 1.4 — Fine haemostasis and gland traction "
                       "define this tray"),
          groups=[
              G("Cutting and dissecting", [
                  ("2", "Knife handle No.3", "No.10 for skin, No.15 for fine "
                   "work"),
                  ("1", "Mayo scissors, straight", "suture"),
                  ("2", "Metzenbaum scissors, curved 14 & 18 cm",
                   "the principal dissecting instrument"),
                  ("1", "Fine dissecting scissors",
                   "close to the recurrent laryngeal nerve"),
                  ("1", "Sternal saw / Gigli saw",
                   "kept available for retrosternal extension"),
              ]),
              G("Grasping and holding", [
                  ("4", "Lahey goitre (vulsellum) forceps",
                   "**signature item** — traction on the gland"),
                  ("2", "Adson forceps, 1×2 teeth", "skin"),
                  ("2", "DeBakey forceps", "vessels, trachea, atraumatic"),
                  ("2", "Dressing forceps, fine", ""),
                  ("4", "Allis forceps", "strap muscles, specimen"),
                  ("6", "Towel clips", ""),
                  ("2", "Sponge-holding forceps", ""),
              ]),
              G("Clamping and occluding", [
                  ("20", "Mosquito forceps, curved",
                   "**large numbers** — the gland bleeds from many small "
                   "vessels"),
                  ("8", "Crile forceps, fine", "haemostasis"),
                  ("4", "Right-angled (Mixter) forceps",
                   "superior and inferior thyroid pedicles"),
                  ("2", "Kocher clamps", "strap muscle and fascia"),
                  ("—", "Ligating clips and applier",
                   "increasingly replace ties on small vessels"),
              ]),
              G("Exposing and retracting", [
                  ("2", "Green (thyroid) retractors",
                   "small right-angled blades, hand-held"),
                  ("2", "Army-Navy retractors", "skin flaps"),
                  ("1", "Weitlaner or mastoid self-retaining retractor",
                   "holds the strap muscles apart"),
                  ("2", "Skin hooks / Senn retractors", "flap elevation"),
                  ("2", "Malleable retractor, narrow",
                   "protects the trachea and oesophagus"),
              ]),
              G("Suturing", [
                  ("2", "Needle holders, 15 cm", ""),
                  ("1", "Needle holder, fine 13 cm",
                   "vessel and capsule suturing"),
                  ("—", "Suture", "absorbable to strap muscles and "
                   "platysma; fine monofilament or subcuticular to skin"),
              ]),
              G("Suctioning and accessory", [
                  ("1", "Frazier suction tip, fine",
                   "keeps the small field dry without soft-tissue trauma"),
                  ("1", "Yankauer suction tip", ""),
                  ("1", "Electrosurgical pencil, fine tip",
                   "used cautiously near the nerve"),
                  ("—", "Nerve monitor / stimulator",
                   "identifies the recurrent laryngeal nerve"),
                  ("—", "Closed suction drain", "haematoma is the feared "
                   "early complication"),
                  ("—", "Tracheostomy set", "**must be immediately "
                   "available** in the recovery area"),
              ]),
          ],
          extras=[("Position", "Supine, neck extended over a sandbag or "
                   "head-ring, 15–20° head-up to reduce venous "
                   "engorgement."),
                  ("Incision", "Transverse collar (Kocher) incision, two "
                   "finger-breadths above the sternal notch."),
                  ("Structures at risk",
                   "Recurrent laryngeal nerve, external branch of the "
                   "superior laryngeal nerve, parathyroid glands, trachea, "
                   "oesophagus, carotid sheath.")],
          side_box={"title": "Bedside emergency set",
                    "lines": ["Post-thyroidectomy **haematoma** causes "
                              "rapid airway obstruction.",
                              "A **clip/suture removal set and a "
                              "tracheostomy set** must stay at the "
                              "bedside — a very commonly examined point."]},
          points=[
              "The **signature instrument is the Lahey goitre vulsellum**; "
              "name it first.",
              "Emphasise the **large number of mosquito forceps** — the "
              "quantity itself is characteristic.",
              "**Frazier** suction, not Poole, because the field is small "
              "and delicate.",
              "Always mention the **tracheostomy set at the bedside** and "
              "the risk of **haematoma → airway obstruction**.",
              "Name the structures at risk; marks are given for the "
              "**recurrent laryngeal nerve and parathyroids**.",
          ],
          qa=[("What additions convert a basic tray into a thyroid tray?",
               "Lahey goitre vulsellum forceps for gland traction; a much "
               "larger number of fine mosquito and Crile haemostats; "
               "right-angled Mixter forceps for the thyroid pedicles; "
               "Green (thyroid) right-angled retractors and a "
               "self-retaining retractor; fine Metzenbaum and nerve "
               "scissors; Frazier fine suction; ligating clips; a nerve "
               "stimulator; a closed drain; and a sternal saw plus "
               "tracheostomy set held available."),
              ("Why are so many small haemostats needed?",
               "The thyroid is exceptionally vascular with numerous small "
               "vessels in a shallow crowded field; each must be "
               "individually secured, and diathermy is restricted near the "
               "recurrent laryngeal nerve.")]),

        # ============================================================ 1.5
        T("1.5", "Long Instruments Tray",
          aka="Deep instruments tray · bariatric or deep-cavity supplement",
          lead="The **long instruments tray** is not a stand-alone set: it "
               "is a **supplementary tray of extended-length patterns** "
               "opened in addition to a major tray whenever the operative "
               "field is unusually deep. Standard 14–20 cm instruments "
               "cannot reach, and forcing them causes poor control, tissue "
               "trauma and loss of haemostasis.",
          uses=["Obese or muscular patients (high BMI, thick abdominal wall)",
                "Deep pelvic surgery — low rectal, radical hysterectomy",
                "Retroperitoneal and para-aortic dissection",
                "High subphrenic and hiatal work; deep splenic hilum",
                "Deep thoracic and mediastinal exposure",
                "Any procedure where a standard instrument 'bottoms out'"],
          plate=PL("Extended-length patterns",
                   [("needle_holder_long", "Needle holder, 25–30 cm"),
                    ("right_angle", "Right-angled forceps, long"),
                    ("metzenbaum", "Metzenbaum scissors, 23–28 cm"),
                    ("debakey_forceps", "DeBakey forceps, 24–30 cm"),
                    ("deaver", "Deaver retractor, deep"),
                    ("poole", "Poole suction, long")],
                   cap="Fig 1.5 — The same instruments, in longer patterns"),
          groups=[
              G("Cutting and dissecting — long patterns", [
                  ("1", "Knife handle No.7, long", "fine deep incision"),
                  ("2", "Metzenbaum scissors, 23 cm & 28 cm",
                   "deep delicate dissection"),
                  ("1", "Mayo scissors, curved 23 cm", "deep heavy tissue"),
                  ("1", "Long dissecting scissors, right-angled",
                   "pelvic side-wall"),
              ]),
              G("Grasping and holding — long patterns", [
                  ("2", "DeBakey forceps, 24 cm & 30 cm",
                   "atraumatic at depth"),
                  ("2", "Dressing forceps, 25 cm", ""),
                  ("2", "Tissue forceps, 25 cm, 1×2 teeth", ""),
                  ("4", "Allis forceps, long", ""),
                  ("4", "Babcock forceps, long", "deep bowel handling"),
                  ("2", "Sponge-holding forceps, 25 cm",
                   "swab-on-a-stick at depth"),
              ]),
              G("Clamping — long patterns", [
                  ("8", "Crile / Kelly forceps, 20–24 cm", ""),
                  ("6", "Right-angled (Mixter) forceps, 22–26 cm",
                   "deep pedicles — the key item"),
                  ("4", "Tonsil (Schnidt) forceps, long",
                   "passing deep ligatures"),
                  ("4", "Rochester-Péan forceps, 24 cm", "large pedicles"),
                  ("2", "Kocher clamps, long", ""),
              ]),
              G("Exposing and retracting — deep patterns", [
                  ("2", "Deaver retractors, deep and extra-deep", ""),
                  ("2", "Richardson retractors, large", ""),
                  ("2", "Malleable retractors, wide and long",
                   "shaped to the cavity"),
                  ("1", "Self-retaining ring retractor system",
                   "Balfour, Bookwalter or O'Sullivan-O'Connor"),
                  ("2", "Lighted / fibre-optic retractor",
                   "illumination at depth is as important as reach"),
              ]),
              G("Suturing — long patterns", [
                  ("2", "Needle holders, 25 cm & 30 cm", ""),
                  ("1", "Ligature carrier (Deschamps), long", ""),
                  ("1", "Knot pusher", "tying at depth"),
                  ("—", "Long staplers and clip appliers", ""),
              ]),
              G("Suction and accessory", [
                  ("1", "Poole suction tip, long", ""),
                  ("1", "Yankauer suction tip, long", ""),
                  ("1", "Electrosurgical pencil with extended tip", ""),
                  ("—", "Head-light and long light cord", ""),
              ]),
          ],
          side_box={"title": "The rule of reach",
                    "lines": ["An instrument must be long enough that the "
                              "**operator's hand stays outside the wound**.",
                              "Working with a short instrument at depth "
                              "obstructs the view, tires the hand and "
                              "causes tissue injury.",
                              "**Illumination** must be extended with the "
                              "instruments — a lighted retractor or "
                              "head-light."]},
          points=[
              "State explicitly that this is a **supplementary tray used "
              "with a major tray**, not an independent set.",
              "The instruments are the **same patterns in longer lengths** "
              "— you need only add the word 'long'.",
              "**Long right-angled (Mixter) forceps** and a **long needle "
              "holder** are the two most valuable additions.",
              "Mention **illumination at depth** (lighted retractor or "
              "head-light) — an easily earned mark others forget.",
          ],
          qa=[("What is a long instruments tray and when is it required?",
               "A supplementary tray of extended-length instruments — long "
               "No.7 handle, 23–28 cm Metzenbaum and Mayo scissors, 24–30 cm "
               "DeBakey and dressing forceps, 20–26 cm Crile, Kelly, Mixter "
               "and tonsil clamps, deep Deaver, Richardson and malleable "
               "retractors, a self-retaining ring retractor, 25–30 cm needle "
               "holders, a ligature carrier and long suction — opened "
               "alongside a major tray whenever the field is deep: obesity, "
               "deep pelvic or retroperitoneal surgery, or deep thoracic "
               "exposure.")]),

        # ============================================================ 1.6
        T("1.6", "Biliary Tract Procedures Tray",
          aka="Cholecystectomy tray · common bile duct exploration (CBDE) "
              "tray · gallbladder tray",
          lead="The biliary tree lies deep beneath the right costal margin "
               "and consists of thin-walled ducts that must be handled "
               "without injury. The **biliary tract tray** is a major tray "
               "with three specific additions: instruments to **grasp and "
               "extract stones**, instruments to **calibrate and dilate "
               "the common bile duct**, and equipment for "
               "**intra-operative cholangiography**.",
          uses=["Open cholecystectomy; conversion from laparoscopic",
                "Common bile duct exploration for choledocholithiasis",
                "Operative cholangiography",
                "Choledochoduodenostomy and biliary-enteric bypass",
                "Repair of bile-duct injury; hepaticojejunostomy",
                "Excision of a choledochal cyst"],
          plate=PL("Signature instruments",
                   [("stone_forceps", "Randall stone forceps"),
                    ("bakes_set", "Bakes common-duct dilators"),
                    ("right_angle", "Right-angled forceps — cystic duct"),
                    ("deaver", "Deaver retractor — liver edge"),
                    ("probe", "Biliary probe / duct sound")],
                   cap="Fig 1.6 — Stone extraction and duct calibration"),
          groups=[
              G("Base set", [
                  ("1", "Complete major procedures tray",
                   "see 1.1 — the entire set is required"),
                  ("1", "Long instruments tray",
                   "if the patient is obese or the field is deep"),
              ]),
              G("Stone extraction and duct instruments", [
                  ("4", "Randall stone (gallstone) forceps",
                   "**signature item** — curved sets in graded angles for "
                   "grasping calculi"),
                  ("1", "Set of Bakes common-duct dilators, 3–10 mm",
                   "**signature item** — malleable, olive-tipped; calibrate "
                   "and gently dilate the duct"),
                  ("2", "Biliary probes / duct sounds", "explore the duct"),
                  ("1", "Desjardins gallstone forceps", "long, fine, curved"),
                  ("1", "Biliary Fogarty / balloon catheter",
                   "sweeps stones distally"),
                  ("1", "Scoop / stone spoon", "retrieves fragments"),
                  ("2", "Gallbladder trocar", "decompresses a tense "
                   "gallbladder"),
                  ("1", "Cholangiogram catheter and clamp",
                   "with three-way tap and contrast"),
                  ("1", "Choledochoscope",
                   "available — see 1.7 if planned"),
              ]),
              G("Clamping and dissecting additions", [
                  ("4", "Right-angled (Mixter) forceps, fine and long",
                   "dissecting and encircling the cystic duct and artery"),
                  ("2", "Fine Metzenbaum / duct scissors",
                   "choledochotomy"),
                  ("2", "DeBakey forceps, long", "atraumatic duct handling"),
                  ("—", "Ligating clips and appliers",
                   "cystic artery and duct"),
                  ("2", "Fine mosquito forceps, extra",
                   "Calot's triangle haemostasis"),
              ]),
              G("Retraction additions", [
                  ("2", "Deaver retractors", "retract the liver edge"),
                  ("1", "Upper-hand / Harrington 'sweetheart' retractor",
                   "liver retraction"),
                  ("1", "Self-retaining costal-margin retractor",
                   "elevates the right costal margin"),
                  ("2", "Malleable retractors", "protects the duodenum"),
              ]),
              G("Drainage and closure", [
                  ("—", "T-tube (Kehr), various sizes",
                   "drains the duct after exploration"),
                  ("—", "Fine absorbable suture, 4-0/5-0",
                   "duct closure over the T-tube"),
                  ("—", "Closed suction drain", "subhepatic space"),
                  ("—", "Specimen container", "gallbladder and calculi"),
              ]),
          ],
          extras=[("Position", "Supine, slight left tilt; a radiolucent "
                   "table section is required for cholangiography."),
                  ("Radiography", "Image intensifier or C-arm, lead "
                   "protection for all staff, contrast medium diluted and "
                   "checked."),
                  ("Structures at risk",
                   "Right hepatic artery, common hepatic duct, portal vein, "
                   "duodenum; the classical injury is misidentification of "
                   "the CBD as the cystic duct.")],
          side_box={"title": "Two names to never confuse",
                    "lines": ["**Randall forceps** = curved forceps to "
                              "**grasp stones**.",
                              "**Bakes dilators** = graduated olive-tipped "
                              "rods to **calibrate and dilate the duct**.",
                              "Both are 'biliary', but one grasps and one "
                              "dilates."]},
          points=[
              "The three defining additions are **stone forceps, Bakes "
              "dilators and cholangiography equipment** — say all three.",
              "Mention the **T-tube** and fine duct suture; T-tube "
              "drainage after CBD exploration is a standard exam point.",
              "**Deaver / Harrington retractors** for the liver edge are "
              "characteristic.",
              "Note that **radiolucent table and lead protection** are "
              "part of the preparation, not just instruments.",
          ],
          qa=[("What are the specific additions to a major tray for biliary "
               "surgery?",
               "Randall (and Desjardins) stone forceps and a stone scoop; a "
               "graded set of Bakes common-duct dilators with biliary "
               "probes; a biliary balloon catheter; a cholangiogram "
               "catheter with clamp, contrast and image intensifier; fine "
               "long right-angled Mixter forceps and duct scissors; "
               "Deaver/Harrington liver retractors; T-tubes with fine "
               "absorbable suture; and a choledochoscope if duct "
               "exploration is planned."),
              ("Why is a T-tube used and how is the tray prepared for it?",
               "After choledochotomy a T-tube decompresses the duct, "
               "prevents a bile leak from the suture line and provides "
               "access for post-operative cholangiography. The tray must "
               "carry assorted T-tube sizes, fine 4-0/5-0 absorbable "
               "suture for closure around it and a closed subhepatic "
               "drain.")]),

        # ============================================================ 1.7
        T("1.7", "Choledochoscopy Tray",
          aka="Common bile duct endoscopy tray",
          lead="**Choledochoscopy** is direct visual inspection of the "
               "interior of the bile ducts with a fine rigid or flexible "
               "endoscope, performed through a choledochotomy (or through "
               "the cystic duct) to confirm complete stone clearance. The "
               "tray is a **biliary tray plus a complete endoscopic "
               "system** with continuous irrigation, and it must remain "
               "capable of open surgery throughout.",
          uses=["Confirming duct clearance during CBD exploration",
                "Retrieval of retained or impacted calculi under vision",
                "Biopsy of an intraductal lesion or stricture",
                "Post-operative choledochoscopy through the T-tube tract",
                "Assessment of a biliary anastomosis"],
          plate=PL("Signature instruments",
                   [("choledochoscope", "Choledochoscope"),
                    ("stone_forceps", "Stone-grasping forceps"),
                    ("bakes_set", "Bakes dilators — prepare the duct"),
                    ("debakey_forceps", "DeBakey forceps — duct edges")],
                   cap="Fig 1.7 — Endoscopic vision added to the biliary set"),
          groups=[
              G("Base set", [
                  ("1", "Complete biliary tract procedures tray",
                   "see 1.6 — open capability must be retained throughout"),
              ]),
              G("The endoscopic system", [
                  ("1", "Choledochoscope, rigid or flexible",
                   "**signature item** — fine calibre (3–5 mm) with a "
                   "working channel"),
                  ("1", "Fibre-optic light cable and light source",
                   "high-intensity, cold light"),
                  ("1", "Camera head, coupler and monitor",
                   "with recorder for documentation"),
                  ("1", "Irrigation set — warm saline under pressure",
                   "**essential**: the duct must be distended with fluid "
                   "to be seen"),
                  ("1", "Three-way tap and pressure tubing",
                   "controls irrigation flow"),
                  ("—", "Sterile drapes for the camera and cable", ""),
              ]),
              G("Instruments passed through the scope", [
                  ("1", "Flexible stone-grasping (basket) forceps",
                   "Dormia basket — retrieves calculi under vision"),
                  ("1", "Flexible biopsy forceps",
                   "intraductal lesions and strictures"),
                  ("1", "Balloon extraction catheter",
                   "sweeps stones toward the choledochotomy"),
                  ("1", "Electrohydraulic or laser lithotripsy probe",
                   "fragments an impacted stone (where available)"),
                  ("—", "Guidewire", "maintains access across a stricture"),
              ]),
              G("Duct access and closure", [
                  ("1", "Set of Bakes dilators",
                   "gently calibrate the duct to admit the scope"),
                  ("2", "Fine DeBakey / duct forceps",
                   "hold the choledochotomy edges open"),
                  ("2", "Stay sutures, 4-0/5-0",
                   "hold the duct edges apart — a practical necessity"),
                  ("—", "T-tube and fine absorbable suture",
                   "closure after inspection"),
                  ("—", "Closed suction drain", "subhepatic"),
              ]),
          ],
          extras=[("Critical practical point",
                   "The scope is delicate and expensive. It is passed and "
                   "received by hand, never left on the tray where an "
                   "instrument may be placed on it, and it is "
                   "sterilised by a low-temperature method (EO, plasma) or "
                   "high-level chemical disinfection — **never by "
                   "steam**, unless the manufacturer specifies "
                   "autoclavability."),
                  ("Fluid management",
                   "Irrigation volume in and out should be monitored; "
                   "over-pressurisation can cause bacteraemia and "
                   "cholangitis.")],
          side_box={"title": "Why irrigation is 'signature'",
                    "lines": ["A bile duct is a **collapsed tube**. "
                              "Without continuous saline distension there "
                              "is nothing to see.",
                              "So the irrigation set is as much a defining "
                              "part of this tray as the scope itself."]},
          points=[
              "Name the **choledochoscope + light source + camera + "
              "irrigation** as one integrated system.",
              "The **Dormia basket** and flexible biopsy forceps are the "
              "working instruments passed through the channel.",
              "Emphasise **low-temperature sterilisation** of the scope — "
              "a very common question.",
              "Stress that the **open biliary tray remains open** — "
              "conversion to open exploration must be immediate.",
              "**Stay sutures** on the choledochotomy are a small but "
              "frequently rewarded detail.",
          ],
          qa=[("What does a choledochoscopy tray contain in addition to a "
               "biliary tray?",
               "A fine rigid or flexible choledochoscope with fibre-optic "
               "light cable, source, camera and monitor; a pressurised warm "
               "saline irrigation set with three-way tap; flexible "
               "stone-grasping (Dormia) baskets, biopsy forceps, balloon "
               "extraction catheter and lithotripsy probe; Bakes dilators "
               "and fine duct forceps with stay sutures for access; and a "
               "T-tube with fine absorbable suture for closure."),
              ("How is a choledochoscope sterilised?",
               "By a low-temperature method — ethylene oxide or hydrogen "
               "peroxide gas plasma — or by high-level chemical "
               "disinfection with glutaraldehyde or peracetic acid "
               "followed by a sterile-water rinse. Steam is used only if "
               "the manufacturer states the instrument is autoclavable.")]),

        # ============================================================ 1.8
        T("1.8", "Basic Rigid Sigmoidoscopy Tray",
          aka="Rigid sigmoidoscopy and proctoscopy tray",
          lead="**Rigid sigmoidoscopy** inspects the rectum and distal "
               "sigmoid (to about 25 cm) with a straight illuminated tube. "
               "The tray is small, self-contained and centred on the "
               "instrument itself: a rigid sigmoidoscope with an "
               "**obturator, light carrier and insufflation bulb**, plus "
               "long instruments to reach down the tube for suction, "
               "swabbing and biopsy.",
          uses=["Diagnostic inspection of rectum and distal sigmoid colon",
                "Biopsy of a rectal lesion or suspicious mucosa",
                "Investigation of rectal bleeding, tenesmus, discharge",
                "Removal of a small foreign body or polyp",
                "Assessment before and after anorectal surgery",
                "Decompression / detorsion of a sigmoid volvulus (with a "
                "flatus tube)"],
          plate=PL("Signature instruments",
                   [("sigmoidoscope", "Rigid sigmoidoscope with obturator"),
                    ("proctoscope", "Proctoscope, shorter and wider"),
                    ("probe", "Long biopsy / swab carrier")],
                   cap="Fig 1.8 — The scope, obturator, light and "
                       "insufflator form one unit"),
          groups=[
              G("The scope assembly — the core of the tray", [
                  ("1", "Rigid sigmoidoscope, 25 cm",
                   "**signature item** — adult and paediatric calibres"),
                  ("1", "Obturator for the sigmoidoscope",
                   "blunt introducer; **removed once past the anal canal**"),
                  ("1", "Proctoscope, short and wider",
                   "for the anal canal and lower rectum"),
                  ("1", "Fibre-optic light carrier with cable and source",
                   "or an integral bulb"),
                  ("1", "Insufflation bulb with tubing",
                   "gently distends the lumen to open it"),
                  ("1", "Eyepiece / viewing window with bellows seal",
                   "maintains distension while viewing"),
              ]),
              G("Long instruments passed down the scope", [
                  ("2", "Rectal biopsy forceps, long",
                   "cup or punch pattern"),
                  ("1", "Long suction tube / rectal sucker",
                   "clears liquid faeces and blood"),
                  ("2", "Long swab (cotton-wool) carriers",
                   "cleans the mucosa for a clear view"),
                  ("1", "Long dissecting forceps",
                   "retrieves small foreign bodies"),
                  ("1", "Snare and cautery lead",
                   "small polypectomy where available"),
                  ("1", "Silver nitrate stick / cautery",
                   "haemostasis at a biopsy site"),
              ]),
              G("Accessory and preparation items", [
                  ("—", "Water-soluble lubricant jelly",
                   "generously applied to scope and anus"),
                  ("—", "Disposable gloves and apron", ""),
                  ("—", "Gauze swabs and receiver", ""),
                  ("1", "Kidney dish", "specimens"),
                  ("—", "Specimen containers with fixative",
                   "labelled with the level of the biopsy"),
                  ("—", "Flatus tube", "sigmoid volvulus decompression"),
                  ("—", "Enema / rectal washout equipment",
                   "bowel preparation before the procedure"),
              ]),
          ],
          extras=[("Position", "Left lateral (Sims) with knees drawn up is "
                   "usual; the knee-elbow or lithotomy position may be "
                   "used."),
                  ("Sequence of use",
                   "Digital rectal examination first → insert the scope "
                   "with the obturator in place, directed toward the "
                   "umbilicus → remove the obturator at about 5 cm → "
                   "advance **under direct vision only**, insufflating "
                   "gently → withdraw slowly, inspecting circumferentially."),
                  ("Safety", "Never advance blindly or against resistance "
                   "— perforation is the principal hazard. Minimal "
                   "insufflation reduces discomfort and vagal response.")],
          side_box={"title": "Obturator rule",
                    "lines": ["The **obturator is used only to pass the "
                              "anal canal**.",
                              "It is removed at about 5 cm, after which "
                              "the scope is advanced **only under direct "
                              "vision**.",
                              "Advancing with the obturator in place risks "
                              "perforation."]},
          points=[
              "The tray is defined by the **scope + obturator + light "
              "carrier + insufflation bulb** — list all four as one unit.",
              "**Digital rectal examination always precedes "
              "instrumentation** — a reliable mark.",
              "Rigid sigmoidoscope reaches about **25 cm**; a proctoscope "
              "is **shorter and wider** for the anal canal.",
              "The complications to quote are **perforation and "
              "bleeding**; the safeguard is advancing only under vision.",
              "All accessory instruments are **long**, because they must "
              "work down a 25 cm tube.",
          ],
          qa=[("List the contents of a basic rigid sigmoidoscopy tray.",
               "A 25 cm rigid sigmoidoscope with its obturator, a "
               "proctoscope, fibre-optic light carrier with cable and "
               "source, insufflation bulb and eyepiece; long rectal biopsy "
               "forceps, long suction tube, long swab carriers and long "
               "dissecting forceps, with a snare and cautery for small "
               "polyps; plus lubricant, gloves, swabs, kidney dish, "
               "labelled specimen containers with fixative and a flatus "
               "tube."),
              ("Describe the safe technique of rigid sigmoidoscopy.",
               "Perform a digital rectal examination first. Insert the "
               "well-lubricated scope with the obturator in place aiming "
               "toward the umbilicus, then remove the obturator at about "
               "5 cm and advance only under direct vision with gentle "
               "insufflation, never against resistance. Withdraw slowly, "
               "inspecting the whole circumference. Perforation and "
               "bleeding are the main complications.")]),

        # ============================================================ 1.9
        T("1.9", "Gastrointestinal Procedures Tray",
          aka="Bowel tray · GI resection and anastomosis tray",
          lead="The **gastrointestinal tray** is a major tray plus the "
               "instruments needed to **divide the gut, control its "
               "contents and rejoin it**. Its logic rests on one "
               "principle: the bowel end that will be **kept** is held "
               "only with **non-crushing (atraumatic)** clamps, while the "
               "end that will be **removed** may be held with **crushing** "
               "clamps. Contamination control and stapling devices "
               "complete the set.",
          uses=["Small and large bowel resection with anastomosis",
                "Gastrectomy, gastrojejunostomy, pyloroplasty",
                "Formation and closure of ileostomy or colostomy",
                "Right, left and sigmoid colectomy; Hartmann's procedure",
                "Repair of perforated peptic ulcer or bowel injury",
                "Adhesiolysis for obstruction"],
          plate=PL("Signature instruments",
                   [("intestinal_clamp", "Doyen non-crushing bowel clamp"),
                    ("babcock", "Babcock forceps — atraumatic"),
                    ("kocher", "Kocher — crushing, specimen side"),
                    ("gi_stapler", "Linear cutting stapler (GIA)"),
                    ("debakey_forceps", "DeBakey forceps")],
                   cap="Fig 1.9 — Crushing versus non-crushing is the "
                       "central idea"),
          groups=[
              G("Base set", [
                  ("1", "Complete major procedures tray", "see 1.1"),
                  ("1", "Long instruments tray",
                   "for deep pelvic or obese cases"),
              ]),
              G("Bowel clamps — the defining group", [
                  ("6", "Doyen intestinal clamps, straight & curved",
                   "**non-crushing** — occlude the bowel to be preserved"),
                  ("4", "Rubber-shod clamps / clamp guards",
                   "further softens the grip on retained bowel"),
                  ("4", "Payr or Kocher crushing clamps",
                   "applied to the **specimen side** only"),
                  ("4", "Babcock forceps",
                   "atraumatic handling and gentle traction"),
                  ("2", "Right-angled forceps", "mesenteric vessels"),
                  ("2", "Allen / Lang-Stevenson anastomosis clamp",
                   "where used, holds the ends in apposition"),
              ]),
              G("Stapling and anastomosis devices", [
                  ("1", "Linear cutter (GIA-type) with reloads",
                   "divides and staples simultaneously"),
                  ("1", "Transverse linear stapler (TA-type) with reloads",
                   "closes a stump or enterotomy"),
                  ("1", "Circular stapler (EEA-type), sized set",
                   "end-to-end colorectal anastomosis"),
                  ("1", "Purse-string clamp with straight needle",
                   "prepares the bowel end for a circular stapler"),
                  ("1", "Anvil grasper / sizers", "for the circular stapler"),
                  ("—", "Ligating clips and appliers", "mesenteric vessels"),
              ]),
              G("Contamination control", [
                  ("—", "Bowel-technique ('dirty') set",
                   "a separate small set of instruments used only after the "
                   "bowel is opened, then discarded from the field"),
                  ("—", "Extra towels and drapes to isolate the bowel",
                   "packing off protects the peritoneal cavity"),
                  ("—", "Suction with a dedicated tip",
                   "for enteric content"),
                  ("—", "Antiseptic-soaked swabs",
                   "cleansing the divided ends"),
                  ("—", "Separate specimen and 'dirty' receivers", ""),
                  ("—", "Change of gloves after the enteric stage", ""),
              ]),
              G("Suturing and closure", [
                  ("2", "Needle holders, standard and long", ""),
                  ("—", "Absorbable suture 3-0/4-0 on a round-bodied "
                   "needle", "seromuscular anastomotic layers"),
                  ("—", "Non-absorbable seromuscular suture",
                   "where a two-layer technique is used"),
                  ("—", "Stay sutures", "hold the bowel ends in apposition"),
                  ("—", "Closed suction drain", ""),
                  ("—", "Stoma appliance and marking pen",
                   "if a stoma is planned"),
              ]),
          ],
          extras=[("Position", "Supine; lithotomy or Lloyd-Davies for "
                   "rectal and low colonic work with stapled anastomosis."),
                  ("Preparation", "Nasogastric tube, urinary catheter, "
                   "mechanical or antibiotic bowel preparation per protocol, "
                   "prophylactic antibiotics, thromboprophylaxis."),
                  ("Anastomotic principles",
                   "Adequate blood supply, tension-free apposition, "
                   "accurate serosa-to-serosa contact, no distal "
                   "obstruction, no faecal loading, no tissue crushing on "
                   "the retained side.")],
          side_box={"title": "Crushing or not?",
                    "lines": ["**Retained bowel** → non-crushing "
                              "(Doyen, rubber-shod, Babcock).",
                              "**Specimen side** → crushing (Payr, "
                              "Kocher).",
                              "Reversing this causes necrosis and "
                              "anastomotic leak — the classic examination "
                              "trap."]},
          mnemonic={"title": "Mnemonic — the anastomosis checklist",
                    "lines": ["**\"BATS-N\"** — **B**lood supply, "
                              "**A**pposition without tension, **T**echnique "
                              "accurate (serosa to serosa), **S**epsis "
                              "controlled, **N**o distal obstruction."]},
          points=[
              "Open with the **crushing vs non-crushing** distinction; it "
              "is the core of the answer.",
              "**Doyen** is the name to give for a non-crushing bowel "
              "clamp; **Payr / Kocher** for crushing.",
              "Name the **three stapler families** — linear cutter (GIA), "
              "transverse linear (TA), circular (EEA).",
              "Describe the **'dirty' bowel-technique set** and glove "
              "change — marks are specifically allotted to contamination "
              "control.",
              "Mention the **purse-string clamp** for circular stapling; "
              "candidates rarely do.",
          ],
          pitfalls=["Applying a crushing clamp to the bowel that will be "
                    "kept.",
                    "Forgetting contamination-control measures entirely.",
                    "Listing staplers without naming their function.",
                    "Omitting stay sutures and drains."],
          qa=[("What are the additions to a major tray for gastrointestinal "
               "surgery?",
               "Non-crushing bowel clamps (Doyen, rubber-shod) and crushing "
               "clamps (Payr, Kocher) with Babcock forceps; stapling "
               "devices — linear cutter, transverse linear and circular "
               "staplers with reloads, purse-string clamp and sizers; "
               "ligating clips; a separate 'dirty' bowel-technique set with "
               "isolation drapes, dedicated suction and separate receivers; "
               "and absorbable round-bodied suture, stay sutures, drains "
               "and stoma appliances."),
              ("Differentiate crushing and non-crushing bowel clamps with "
               "examples.",
               "Non-crushing (atraumatic) clamps such as Doyen or "
               "rubber-shod clamps have smooth or finely ridged jaws that "
               "occlude the lumen without devitalising the wall; they are "
               "applied to bowel that will be retained. Crushing clamps "
               "such as Payr or Kocher have heavy interlocking teeth that "
               "deliberately crush the wall and are applied only to the "
               "specimen side, sealing it and preventing spillage.")]),

        # ============================================================ 1.10
        T("1.10", "Rectal Procedures Tray",
          aka="Anorectal tray · haemorrhoidectomy and fistula tray",
          lead="The anorectal region is a **short, narrow, highly "
               "sensitive and heavily contaminated field**. The rectal tray "
               "is therefore built on a minor tray with three specific "
               "needs: **specialised retractors and specula** to open the "
               "anal canal, **probes and directors** to trace fistula "
               "tracts, and **generous haemostasis** in a very vascular "
               "area.",
          uses=["Haemorrhoidectomy; banding and stapled haemorrhoidopexy",
                "Lateral internal sphincterotomy for anal fissure",
                "Fistula-in-ano — fistulotomy, fistulectomy, seton "
                "insertion",
                "Incision and drainage of perianal and ischiorectal abscess",
                "Excision of anal tags, warts, polyps and fibro-epithelial "
                "papillae",
                "Excision of a pilonidal sinus (an adjacent procedure using "
                "the same set)"],
          plate=PL("Signature instruments",
                   [("proctoscope", "Proctoscope / anal speculum"),
                    ("grooved_director", "Grooved director — fistula tract"),
                    ("probe", "Malleable probe — traces the tract"),
                    ("allis", "Allis forceps — pile mass traction"),
                    ("frazier", "Fine suction")],
                   cap="Fig 1.10 — Exposure of the canal and tracing of "
                       "tracts"),
          groups=[
              G("Base set", [
                  ("1", "Basic / minor procedures tray", "see 1.2"),
              ]),
              G("Anal exposure — retractors and specula", [
                  ("2", "Proctoscope / anal speculum",
                   "**signature item** — Kelly, Sims or bivalve pattern"),
                  ("1", "Eisenhammer or Parks self-retaining anal retractor",
                   "opens the canal and holds itself"),
                  ("2", "Hill-Ferguson retractor",
                   "the standard haemorrhoidectomy retractor"),
                  ("1", "Rigid sigmoidoscope",
                   "proctosigmoidoscopy always precedes anorectal surgery"),
                  ("2", "Small Langenbeck / Army-Navy retractors",
                   "perianal tissue"),
              ]),
              G("Fistula and tract instruments", [
                  ("2", "Malleable fistula probes, fine and stout",
                   "**signature item** — trace the tract from external to "
                   "internal opening"),
                  ("1", "Grooved director",
                   "guides the knife safely along the tract"),
                  ("1", "Lockhart-Mummery fistula probe",
                   "curved, for high tracts"),
                  ("—", "Seton material",
                   "silk, nylon or a soft silicone loop for a high tract"),
                  ("—", "Hydrogen peroxide / methylene blue with syringe",
                   "delineates a tract that cannot be probed"),
                  ("1", "Small curette / spoon", "curettes granulation "
                   "tissue"),
              ]),
              G("Grasping, clamping and cutting", [
                  ("6", "Allis forceps",
                   "traction on the pile mass and skin tags"),
                  ("4", "Artery forceps, fine curved", "pedicle haemostasis"),
                  ("2", "Kocher clamps", ""),
                  ("1", "Knife handle No.3 with No.11 and No.15 blades",
                   "abscess incision and precise cuts"),
                  ("1", "Fine dissecting scissors", ""),
                  ("1", "Diathermy pencil with fine and needle tips",
                   "the principal haemostatic and cutting tool"),
                  ("1", "Anal dilator set",
                   "graded, for controlled dilatation"),
                  ("—", "Haemorrhoid banding applicator with bands",
                   "if banding is planned"),
                  ("—", "Circular stapling device for haemorrhoidopexy",
                   "if stapled technique is planned"),
              ]),
              G("Suturing, packing and accessory", [
                  ("2", "Needle holders, short",
                   "the field is shallow and narrow"),
                  ("—", "Absorbable suture 2-0/3-0 on a round needle",
                   "transfixion of the pile pedicle"),
                  ("1", "Fine suction tip (Frazier)", ""),
                  ("—", "Anal pack / dressing with lubricant",
                   "haemostasis after haemorrhoidectomy"),
                  ("—", "Local anaesthetic with adrenaline and syringe",
                   "infiltration reduces bleeding and gives analgesia"),
                  ("—", "Specimen containers", "separate and labelled"),
                  ("—", "Culture swabs", "pus from an abscess"),
              ]),
          ],
          extras=[("Position", "Lithotomy is usual; prone jack-knife is "
                   "preferred for posterior lesions and pilonidal sinus; "
                   "left lateral for simple procedures."),
                  ("Preparation", "Rectal washout or enema; hair removal as "
                   "required; prophylactic antibiotics for abscess and "
                   "fistula work."),
                  ("Contamination status",
                   "This is a **contaminated field**. Instruments used in "
                   "the anal canal are kept separate from any clean part "
                   "of the procedure, and the tray is handled as "
                   "contaminated at the end.")],
          side_box={"title": "Goodsall's rule",
                    "lines": ["Predicts the course of a fistula tract:",
                              "**Anterior** external opening → tract runs "
                              "**radially (straight)** to the canal.",
                              "**Posterior** external opening → tract "
                              "curves to the **posterior midline**.",
                              "Guides how the probe is directed — commonly "
                              "asked alongside this tray."]},
          points=[
              "Name the exposure instruments precisely: **proctoscope, "
              "Eisenhammer/Parks self-retaining retractor, "
              "Hill-Ferguson retractor**.",
              "The **fistula probe and grooved director** are the "
              "signature pair for fistula work.",
              "State that **proctosigmoidoscopy precedes** any anorectal "
              "operation, to exclude proximal disease.",
              "Quote **Goodsall's rule** — it is frequently paired with "
              "this tray.",
              "Emphasise that this is a **contaminated field** and the "
              "positioning options (lithotomy / prone jack-knife).",
          ],
          qa=[("List the contents of a rectal procedures tray.",
               "A minor tray plus: proctoscope/anal speculum, "
               "Eisenhammer or Parks self-retaining anal retractor, "
               "Hill-Ferguson retractor and a rigid sigmoidoscope; "
               "malleable fistula probes, a grooved director, "
               "Lockhart-Mummery probe, seton material and hydrogen "
               "peroxide or methylene blue; Allis forceps, fine artery "
               "forceps, No.11/15 blades, fine scissors, diathermy with "
               "fine tips and an anal dilator set; short needle holders "
               "with absorbable transfixion suture, fine suction, an anal "
               "pack, local anaesthetic with adrenaline, specimen "
               "containers and culture swabs."),
              ("State Goodsall's rule.",
               "A fistula with an external opening anterior to the "
               "transverse anal line usually runs radially and directly "
               "into the anal canal; one with a posterior external opening "
               "usually curves to open in the posterior midline.")]),
    ])
