#!/usr/bin/env python3
"""Part 0 -- Foundations of instrument-tray preparation."""
from schema import T, P, PL, DP, FIG, G, CMP

FOUNDATIONS = P(
    "0", "Foundations of Instrument Tray Preparation",
    "Terminology · classification · reprocessing · set-up · counting · care",
    intro="Before any individual tray can be memorised, the //logic// behind "
          "every tray must be clear. A tray is never a random collection of "
          "steel: it is a **planned, reproducible set** that guarantees the "
          "surgeon an instrument for every action the operation may demand, "
          "in a state that is sterile, functional and accounted for. "
          "Part 0 establishes that logic; Parts I–X then apply it "
          "speciality by speciality.",
    trays=[

        # ================================================== 0.1
        T("0.1", "Introduction, Definitions and Terminology",
          aka="Basic vocabulary of instrumentation",
          lead="An **instrument tray** (also //set//, //pack// or //setup//) "
               "is a standardised, pre-assembled and sterilised collection "
               "of surgical instruments and accessories, listed on a "
               "**count sheet**, that provides everything routinely required "
               "for a defined operation or class of operations. "
               "Standardisation is what makes the theatre safe and fast: the "
               "scrub person knows exactly what is present, the sterile "
               "services department knows exactly what to reassemble, and "
               "any missing item is immediately obvious.",
          uses=["Guarantees **availability** — no instrument hunting mid-case",
                "Guarantees **sterility** — one validated cycle for the "
                "whole set",
                "Guarantees **accountability** — a fixed count sheet makes "
                "retained items detectable",
                "Guarantees **economy** — only instruments actually needed "
                "are processed",
                "Guarantees **speed** — a predictable layout allows "
                "instruments to be passed without looking"],
          plate=PL("Key terms made visual",
                   [("scalpel_10", "Instrument — a single item"),
                    ("crile", "Set / tray — many items, one count sheet"),
                    ("sponge_stick", "Accessory — completes the set")],
                   cap="Fig 0.1 — From single instrument to complete set"),
          groups=[
              G("Core vocabulary you must be able to define", [
                  ("—", "Instrument set / tray",
                   "The complete, counted, sterilised collection for a "
                   "defined procedure."),
                  ("—", "Count sheet (tray list)",
                   "The master inventory document packed with the set; the "
                   "legal record of contents."),
                  ("—", "Basic / standard set",
                   "The core group of instruments common to most operations "
                   "of a speciality."),
                  ("—", "Add-on / speciality items",
                   "Instruments opened separately and added to a basic set "
                   "for a particular step."),
                  ("—", "Back table",
                   "The large sterile table holding the bulk of the set, "
                   "supplies and drapes."),
                  ("—", "Mayo stand",
                   "The small movable stand carrying only the instruments "
                   "needed for the current step."),
                  ("—", "Sterile field",
                   "The area around the incision kept free of "
                   "micro-organisms; includes draped tables and gowned "
                   "personnel."),
                  ("—", "Stringer / rack",
                   "A pin or rack threading ring-handled instruments so they "
                   "stay open and ordered."),
                  ("—", "Tip guard / protector",
                   "A latex or silicone sleeve shielding delicate or sharp "
                   "tips during processing."),
                  ("—", "Peel pouch",
                   "A paper–plastic sealed package used for single or few "
                   "small items."),
                  ("—", "Rigid container",
                   "A reusable perforated metal box with filters, replacing "
                   "textile wrapping."),
                  ("—", "Event-related sterility",
                   "The modern concept that a pack stays sterile until an "
                   "//event// (wet, torn, dropped) compromises it — not "
                   "until a fixed date."),
              ]),
          ],
          points=[
              "A tray is defined by **function, not by number of pieces** — "
              "the same operation may be covered by a 40-piece or a "
              "90-piece set depending on the hospital's standardisation.",
              "The count sheet is a **legal document**. It travels with the "
              "set and is signed.",
              "Names are often **eponymous** (Kelly, Kocher, Allis) and vary "
              "regionally; always learn the **descriptive** name too "
              "(e.g. Kocher = //toothed artery forceps//).",
              "//Sterile// (free of all microbial life) is not the same as "
              "//disinfected// (free of most pathogens) or //clean// (free "
              "of visible soil).",
          ],
          qa=[
              ("Define an instrument tray.",
               "A standardised, pre-assembled, sterilised and counted "
               "collection of instruments and accessories, documented on a "
               "count sheet, sufficient for a defined operation."),
              ("Why is standardisation of trays essential?",
               "It ensures availability, sterility, accountability, economy "
               "and speed, and it makes any missing or retained item "
               "immediately detectable."),
          ]),

        # ================================================== 0.2
        T("0.2", "Classification of Surgical Instruments",
          aka="The six functional groups",
          lead="Every instrument in every tray in this syllabus belongs to "
               "one of **six functional groups**. This single framework is "
               "the most valuable thing in the whole topic: if you can place "
               "an unfamiliar instrument into its group, you can deduce its "
               "purpose, how it is passed, how it is cleaned, and why it is "
               "in that particular tray. Examiners frequently ask you to "
               "//classify// rather than merely list.",
          uses=["Group 1 — **Cutting and dissecting**",
                "Group 2 — **Grasping and holding**",
                "Group 3 — **Clamping and occluding**",
                "Group 4 — **Exposing and retracting**",
                "Group 5 — **Suturing and stapling**",
                "Group 6 — **Suctioning and accessory / viewing**"],
          figs=[FIG("fig_classification",
                    "Fig 0.2 — The six functional groups with examples",
                    w=13.2)],
          plate=PL("One representative of each group",
                   [("scalpel_10", "1 · Cutting — scalpel"),
                    ("tissue_forceps", "2 · Grasping — tissue forceps"),
                    ("crile", "3 · Clamping — haemostat"),
                    ("army_navy", "4 · Retracting — Army-Navy"),
                    ("needle_holder", "5 · Suturing — needle holder"),
                    ("yankauer", "6 · Suctioning — Yankauer")],
                   cap="Fig 0.3 — A complete tray must satisfy all six groups"),
          groups=[
              G("Group 1 — Cutting and dissecting", [
                  ("—", "Scalpels (knife handle + blade)",
                   "No.3 handle takes blades 10, 11, 12, 15; No.4 handle "
                   "takes 20–25; No.7 is the long fine handle."),
                  ("—", "Scissors",
                   "Mayo (heavy tissue/suture), Metzenbaum (delicate "
                   "dissection), iris/tenotomy (fine), Potts (vascular), "
                   "wire and bandage scissors."),
                  ("—", "Bone cutters",
                   "Osteotome, chisel, gouge, rongeur, saw, rasp, curette."),
                  ("—", "Others",
                   "Curettes, biopsy punches, dermatome, snares, "
                   "electrosurgical pencil, laser and ultrasonic devices."),
              ]),
              G("Group 2 — Grasping and holding", [
                  ("—", "Thumb (spring) forceps",
                   "Toothed = grips tough tissue; smooth/serrated = delicate "
                   "tissue; Adson for skin; DeBakey atraumatic for vessels "
                   "and bowel."),
                  ("—", "Ring-handled tissue clamps",
                   "Allis (sharp interlocking teeth, tough tissue), Babcock "
                   "(fenestrated atraumatic loop, bowel/tube), Kocher "
                   "(1×2 teeth, fascia), tenaculum (single sharp hook)."),
                  ("—", "Bone and organ holders",
                   "Bone-holding forceps, Lahey (thyroid), stone forceps, "
                   "lung/kidney clamps."),
                  ("—", "Accessory holders",
                   "Sponge-holding forceps (fenestrated jaws), towel clips, "
                   "needle books."),
              ]),
              G("Group 3 — Clamping and occluding", [
                  ("—", "Haemostats (artery forceps)",
                   "Mosquito/Halsted (finest), Crile (fully serrated, "
                   "straight or curved), Kelly (serrations only over the "
                   "distal half), Rochester-Péan (largest)."),
                  ("—", "Right-angled and tonsil clamps",
                   "Mixter, Lahey and tonsil (Schnidt) for passing ligatures "
                   "behind a pedicle."),
                  ("—", "Crushing vs non-crushing",
                   "Crushing (Kocher, Payr) on tissue to be removed; "
                   "non-crushing/atraumatic (Doyen, DeBakey, bulldog, "
                   "Satinsky) on tissue that must survive."),
                  ("—", "Vascular occluders",
                   "Bulldog, Satinsky (side-biting), aortic cross-clamps, "
                   "Fogarty inserts, vessel loops."),
              ]),
              G("Group 4 — Exposing and retracting", [
                  ("—", "Hand-held retractors",
                   "Army-Navy, Richardson, Deaver, malleable/ribbon, Senn, "
                   "rake, Volkmann, skin hooks — held by an assistant."),
                  ("—", "Self-retaining retractors",
                   "Weitlaner, mastoid, cerebellar, Balfour, Finochietto, "
                   "Gelpi — hold themselves open by ratchet or rack."),
                  ("—", "Specula",
                   "Graves/Cusco bivalve, Sims, nasal, aural, eyelid — "
                   "hold a natural orifice open."),
                  ("—", "Accessory exposure",
                   "Malleable ribbon, laparotomy pads, vein retractors, "
                   "fibre-optic lighted retractors."),
              ]),
              G("Group 5 — Suturing and stapling", [
                  ("—", "Needle holders",
                   "Mayo-Hegar and Crile-Wood (ring-handled), Castroviejo "
                   "(spring, microsurgery), Heaney (angled, gynaecology). "
                   "Tungsten-carbide inserts give the longest life."),
                  ("—", "Needles and suture",
                   "Cutting/reverse-cutting for skin and fascia, taper for "
                   "viscera and vessels, blunt for friable liver/kidney."),
                  ("—", "Staplers and clips",
                   "Linear, linear cutter (GIA), circular (EEA), skin "
                   "stapler; ligating clips and appliers."),
                  ("—", "Accessory",
                   "Ligature carrier (Deschamps), suture boots, knot "
                   "pushers."),
              ]),
              G("Group 6 — Suctioning, viewing and accessory", [
                  ("—", "Suction tips",
                   "Yankauer (oral/general, bulbous fenestrated tip), Poole "
                   "(perforated shield, free fluid in a cavity), Frazier "
                   "(fine, angled, thumb vent — neuro/ENT/plastics)."),
                  ("—", "Viewing / endoscopic",
                   "Sigmoidoscope, proctoscope, laparoscope, arthroscope, "
                   "bronchoscope, mediastinoscope, choledochoscope, "
                   "cystoscope, operating microscope."),
                  ("—", "Dilating and probing",
                   "Hegar and Bakes dilators, uterine sound, probes, "
                   "grooved director, lacrimal probes."),
                  ("—", "Measuring and accessory",
                   "Rulers, calipers, kidney dish, gallipot, medicine cup, "
                   "magnets, light cords, irrigation sets."),
              ]),
          ],
          compare=CMP(
              ["Feature", "Crushing clamp", "Non-crushing (atraumatic) clamp"],
              [["Jaw serration", "Deep transverse teeth, may have 1×2 tooth",
                "Fine longitudinal rows, or smooth"],
               ["Effect on tissue", "Deliberately crushes and devitalises",
                "Preserves wall viability and blood supply"],
               ["Typical examples", "Kocher, Payr, Rochester-Péan",
                "Doyen, DeBakey, bulldog, Satinsky"],
               ["Applied to", "Tissue that will be excised or ligated",
                "Bowel, vessel or duct that must survive"],
               ["Consequence of error",
                "Necrosis, leak, anastomotic breakdown",
                "Slippage and haemorrhage if too gentle"]],
              cap="Table 0.1 — Crushing versus non-crushing clamps: the "
                  "single most examined distinction in Group 3"),
          side_box={"title": "Memory hook",
                    "lines": ["**C-G-C-E-S-S** — //Cut, Grasp, Clamp, "
                              "Expose, Stitch, Suck//.",
                              "Check any tray against these six letters; a "
                              "gap means the tray is incomplete."]},
          points=[
              "Learn the **six groups** as your default answer skeleton for "
              "'describe the contents of X tray'.",
              "**Handle–blade pairing** is a favourite one-mark question: "
              "No.3 handle → blades 10/11/12/15; No.4 handle → blades 20–25.",
              "Distinguish **Crile** (serrations along the //whole// jaw) "
              "from **Kelly** (serrations over the //distal half// only).",
              "**Allis vs Babcock**: Allis has sharp interlocking teeth for "
              "tough tissue; Babcock has a smooth fenestrated loop for "
              "delicate hollow structures.",
              "Suction choice follows the site: **Yankauer** oral/general, "
              "**Poole** free peritoneal fluid, **Frazier** fine and "
              "vented for neuro/ENT.",
          ],
          qa=[
              ("Classify surgical instruments functionally.",
               "Cutting and dissecting; grasping and holding; clamping and "
               "occluding; exposing and retracting; suturing and stapling; "
               "suctioning, viewing and accessory."),
              ("Differentiate Allis from Babcock forceps.",
               "Allis has short sharp interlocking teeth and is traumatic — "
               "used on fascia, skin edges and tissue to be excised. "
               "Babcock has a broad fenestrated atraumatic loop — used on "
               "bowel, appendix, ureter and fallopian tube."),
              ("Which suction tip is used for free fluid in the peritoneal "
               "cavity, and why?",
               "Poole suction — its perforated outer shield distributes "
               "suction over many holes so omentum and bowel are not drawn "
               "into and occluded by the tip."),
          ]),

        # ================================================== 0.3
        T("0.3", "Parts of an Instrument and How It Is Handled",
          aka="Instrument anatomy · grips · passing technique",
          lead="Naming the **parts** of an instrument lets you describe "
               "faults precisely (a sprung box lock, a worn ratchet, "
               "misaligned tips) and is regularly asked as a labelled "
               "diagram. The ring-handled (haemostatic) pattern is the "
               "reference design from which most clamps, scissors and "
               "needle holders are derived.",
          figs=[FIG("fig_hemostat_anatomy",
                    "Fig 0.4 — Named parts of a ring-handled instrument",
                    w=13.2),
                FIG("fig_grip",
                    "Fig 0.5 — The three standard grips", w=13.2)],
          plate=PL("Jaw patterns decide the job",
                   [("crile", "Crile — fully serrated"),
                    ("kocher", "Kocher — 1×2 teeth"),
                    ("allis", "Allis — interlocking teeth"),
                    ("babcock", "Babcock — fenestrated loop")],
                   cap="Fig 0.6 — The jaw, not the handle, defines the use"),
          groups=[
              G("Parts of a ring-handled instrument", [
                  ("1", "Ring / bow (finger ring)",
                   "Takes thumb and ring finger; size must suit the "
                   "operator's hand."),
                  ("2", "Ratchet (lock)",
                   "Interlocking teeth on the shanks that hold the jaws "
                   "closed at graded tension. Usually 3–4 teeth."),
                  ("3", "Shank",
                   "The arm between ring and joint. Its length determines "
                   "the working depth of the instrument."),
                  ("4", "Box lock (joint)",
                   "The hinge. A //box// lock (one shank passing through "
                   "the other) is stronger than a screw or pin joint and is "
                   "the commonest wear point."),
                  ("5", "Jaw / blade",
                   "The working end. Serration pattern, curvature, teeth and "
                   "fenestration define the instrument's identity."),
                  ("6", "Tip",
                   "The extreme end; must be in perfect apposition. Tip "
                   "alignment is the key functional test."),
              ]),
              G("Standard grips", [
                  ("—", "Pencil grip",
                   "Scalpel with No.15/No.11 blade, fine dissection, "
                   "electrosurgical pencil. Maximum control, short cuts."),
                  ("—", "Palmar (table-knife) grip",
                   "Scalpel with No.20/No.10 blade for long skin incisions; "
                   "power and a single smooth stroke."),
                  ("—", "Tripod / ring grip",
                   "Thumb and ring finger in the bows, index finger along "
                   "the shank to steady; used for all ring-handled "
                   "instruments."),
                  ("—", "Thumb-forceps grip",
                   "Held like a pen between thumb and index; the "
                   "non-dominant hand's default instrument."),
              ]),
              G("Passing instruments (the scrub person's craft)", [
                  ("—", "Pass decisively",
                   "A firm slap into the palm tells the surgeon the "
                   "instrument has arrived without them looking away from "
                   "the field."),
                  ("—", "Pass ready to use",
                   "Curved jaws point in the direction of use; the handle "
                   "meets the palm; the surgeon should not have to reorient "
                   "it."),
                  ("—", "Pass sharps safely",
                   "Use a **neutral / hands-free zone** (magnetic pad or "
                   "kidney dish) for blades and needles — never hand to "
                   "hand."),
                  ("—", "Anticipate",
                   "Watch the field, not the tray; the next instrument "
                   "should already be in your hand."),
                  ("—", "Keep it clean",
                   "Wipe blood from jaws with a damp sponge as soon as an "
                   "instrument returns; dried blood is the hardest soil to "
                   "remove."),
              ]),
          ],
          side_box={"title": "Functional tests before packing",
                    "lines": ["**Tips** must meet exactly with no light gap.",
                              "**Ratchet** must hold on the first tooth when "
                              "tapped on a hard surface.",
                              "**Box lock** must have no side-to-side play.",
                              "**Scissors** must cut cleanly to the very tip "
                              "(test on gauze, not paper).",
                              "**Needle holder** must grip a needle without "
                              "the needle rotating."]},
          points=[
              "The **box lock** is the commonest site of wear and of "
              "retained soil — it must be cleaned open and lubricated.",
              "A ratchet that springs open when tapped is **condemned**, not "
              "repaired at ward level.",
              "Instruments are sterilised with jaws **open** (unlocked) — a "
              "locked ratchet prevents steam reaching the joint surfaces.",
              "Curved instruments are passed with the **curve pointing the "
              "way the surgeon will work**.",
          ],
          qa=[
              ("Draw and label the parts of an artery forceps.",
               "Ring/bow, ratchet, shank, box lock (joint), jaw, tip — see "
               "Fig 0.4."),
              ("Why are ring-handled instruments sterilised in the open "
               "position?",
               "A closed ratchet shields the box-lock and jaw surfaces from "
               "steam contact, so sterilisation cannot be assured; it also "
               "stresses the joint."),
          ]),

        # ================================================== 0.4
        T("0.4", "Principles of Tray Preparation",
          aka="Rules that govern the assembly of every set",
          lead="Tray preparation is governed by a small number of principles "
               "that apply equally to a 6-item limited tray and a 120-item "
               "cardiac set. Answer any 'principles of tray preparation' "
               "question with this list, then illustrate it with the "
               "specific tray you have been asked about.",
          figs=[FIG("fig_tray_assembly",
                    "Fig 0.7 — Correct layering of instruments in the tray",
                    w=13.2)],
          plate=PL("Order of assembly, heaviest first",
                   [("richardson", "Heavy retractors — bottom layer"),
                    ("crile", "Ring-handled — on a stringer, jaws open"),
                    ("metzenbaum", "Delicate — uppermost, tips guarded"),
                    ("adson", "Fine forceps — protected, never loose")],
                   cap="Fig 0.8 — Assemble downward in weight, upward in "
                       "delicacy"),
          groups=[
              G("A · Selection principles", [
                  ("1", "Match the tray to the procedure",
                   "Include what is //routinely// needed. Rarely used items "
                   "are kept as separate add-on packs, not carried in every "
                   "set."),
                  ("2", "Satisfy all six functional groups",
                   "Cut, grasp, clamp, expose, stitch, suck — a gap in any "
                   "group makes the tray unusable."),
                  ("3", "Match length to depth",
                   "The deeper the cavity, the longer the instrument; hence "
                   "a dedicated **long instruments tray** for obese or deep "
                   "pelvic work."),
                  ("4", "Match delicacy to tissue",
                   "Atraumatic instruments for bowel, vessel and duct; "
                   "heavy toothed instruments only on tissue to be "
                   "discarded."),
                  ("5", "Standardise and document",
                   "One agreed count sheet per tray, reviewed periodically "
                   "with the surgical team; no informal substitutions."),
              ]),
              G("B · Assembly principles", [
                  ("6", "Clean and dry before assembly",
                   "No item enters a tray until it is decontaminated, "
                   "inspected, functional and dry."),
                  ("7", "Heaviest at the bottom",
                   "Retractors and bone instruments form the base; delicate "
                   "items rest on top, never underneath."),
                  ("8", "Jaws open, ratchets unlocked",
                   "Thread ring-handled instruments on a stringer/rack in "
                   "the open position, in a fixed order."),
                  ("9", "Protect the vulnerable",
                   "Tip guards on microsurgical, ophthalmic and vascular "
                   "tips; delicate items in a foam-lined inner tray."),
                  ("10", "Allow steam to reach every surface",
                   "Perforated base; concave items on edge or inverted; "
                   "disassemble multi-part instruments; open all stopcocks."),
                  ("11", "Respect the mass limit",
                   "A wrapped instrument set should not exceed about "
                   "**11 kg (25 lb)** — heavier sets trap condensate and "
                   "come out wet."),
                  ("12", "Indicators inside and outside",
                   "A chemical indicator **inside** the pack and indicator "
                   "tape **outside**; include the count sheet."),
              ]),
              G("C · Documentation and traceability", [
                  ("13", "Label every pack",
                   "Set name, contents/count sheet, date processed, "
                   "sterilizer and cycle/load number, operator initials."),
                  ("14", "Enable recall",
                   "The load number lets every pack from a failed cycle be "
                   "traced and retrieved."),
                  ("15", "Event-related sterility",
                   "Integrity, not a calendar date, determines usability: "
                   "wet, torn, dropped or compressed = discard and "
                   "reprocess."),
              ]),
          ],
          side_box={"title": "Reject an item at inspection if…",
                    "lines": ["Tips do not meet, or overlap",
                              "Ratchet springs open on tapping",
                              "Box lock is loose or gritty",
                              "Scissors chew instead of cutting",
                              "Any crack, pit, rust, chip or burr",
                              "Illegible or missing identification"]},
          points=[
              "The commonest exam framing is **'principles'** — give "
              "selection, assembly and documentation as three headings.",
              "The **11 kg** mass limit and the **jaws-open** rule are "
              "favourite factual marks.",
              "Include the **count sheet inside the pack**; it is both an "
              "inventory and a legal record.",
              "'Event-related' has replaced 'time-related' shelf life in "
              "modern practice — say so explicitly.",
          ],
          qa=[
              ("State the principles of preparing an instrument tray.",
               "Selection (match procedure, cover all six functional groups, "
               "match length to depth and delicacy to tissue, standardise); "
               "assembly (clean/dry/inspected first, heaviest at the bottom, "
               "jaws open on a stringer, protect delicate tips, allow steam "
               "access, respect the 11 kg limit, indicators inside and out); "
               "documentation (label, traceable load number, event-related "
               "sterility)."),
              ("What is the maximum recommended weight of a wrapped "
               "instrument set and why?",
               "About 11 kg (25 lb). Heavier sets retain condensate, "
               "producing wet packs which are considered contaminated."),
          ]),

        # ================================================== 0.5
        T("0.5", "Decontamination, Packing and Sterilisation",
          aka="The instrument reprocessing cycle",
          lead="A tray is only as good as the cycle that produced it. The "
               "reprocessing chain runs **point of use → transport → "
               "decontamination → inspection → assembly → packaging → "
               "sterilisation → storage**, and it must move in one "
               "direction, from dirty to clean, without crossing back.",
          figs=[FIG("fig_steril_flow",
                    "Fig 0.9 — The reprocessing cycle, step by step",
                    w=12.4)],
          groups=[
              G("Cleaning — the non-negotiable first step", [
                  ("—", "Point-of-use care",
                   "Wipe visible blood; keep instruments **moist** with "
                   "water or an enzymatic gel/foam; never let blood dry."),
                  ("—", "Why cool water first",
                   "Hot water **coagulates protein** onto the surface and "
                   "makes soil far harder to remove."),
                  ("—", "Enzymatic / proteolytic soak",
                   "Breaks down blood, fat and tissue in box locks, "
                   "serrations and lumens."),
                  ("—", "Manual cleaning",
                   "Soft brushes, jaws open, **below the water surface** to "
                   "avoid aerosols; lumen brushes for cannulated items."),
                  ("—", "Ultrasonic cleaner",
                   "Cavitation reaches serrations and box locks; not for "
                   "chrome-plated, cemented optical or dissimilar metals "
                   "together."),
                  ("—", "Washer-disinfector",
                   "Automated wash → thermal disinfection → dry; thermal "
                   "disinfection is measured as an **A0 value**."),
                  ("—", "Final rinse and dry",
                   "Demineralised/distilled water prevents staining and "
                   "pitting; items must be **completely dry** before "
                   "packing."),
                  ("—", "Lubricate",
                   "Water-soluble, steam-permeable instrument milk on box "
                   "locks and hinges. Never use oil — it blocks steam."),
              ]),
              G("Packaging systems", [
                  ("—", "Textile / non-woven wrap",
                   "Sequential double wrap (envelope or square fold) — "
                   "allows aseptic opening."),
                  ("—", "Peel pouch",
                   "Paper–plastic; for one or a few light items; place "
                   "paper-to-plastic when stacking."),
                  ("—", "Rigid container",
                   "Perforated metal box with valve filters and a tamper "
                   "seal; protects heavy sets."),
                  ("—", "Indicators",
                   "Class I tape outside; Class IV–VI chemical indicator or "
                   "integrator inside the pack; biological indicator "
                   "(//Geobacillus stearothermophilus// for steam) per "
                   "policy."),
              ]),
              G("Sterilisation methods", [
                  ("—", "Steam (moist heat) — the default",
                   "**121 °C for 15 min at 15 psi** (gravity) or "
                   "**134 °C for 3–3.5 min** (pre-vacuum). Cheap, fast, "
                   "non-toxic; for all heat- and moisture-stable items."),
                  ("—", "Flash / immediate-use steam (IUSS)",
                   "134 °C for 3–10 min for an urgently needed unwrapped "
                   "item. Emergency use only; never for implants."),
                  ("—", "Ethylene oxide (EO)",
                   "Low temperature, excellent penetration; for optics, "
                   "plastics, cables. **Long aeration** required; toxic, "
                   "flammable, carcinogenic."),
                  ("—", "Hydrogen peroxide gas plasma",
                   "Low temperature, short cycle, no toxic residue; not for "
                   "cellulose (linen, paper) or long narrow lumens."),
                  ("—", "Dry heat",
                   "160 °C/2 h or 170 °C/1 h; for oils, powders, glass and "
                   "sharp cutting edges."),
                  ("—", "Chemical (cold) sterilant",
                   "2 % glutaraldehyde or peracetic acid for heat-sensitive "
                   "endoscopes; requires sterile-water rinse."),
              ]),
          ],
          compare=CMP(
              ["Method", "Conditions", "Best for", "Main limitation"],
              [["Steam — gravity", "121 °C, 15 psi, 15–30 min",
                "Instruments, linen, basins", "Heat/moisture sensitive items"],
               ["Steam — pre-vacuum", "134 °C, 3–3.5 min",
                "Wrapped instrument sets", "Requires air removal test (Bowie-Dick)"],
               ["Ethylene oxide", "37–55 °C, 2–5 h + aeration",
                "Optics, plastics, cables", "Toxic; very long total cycle"],
               ["H₂O₂ gas plasma", "45–50 °C, 28–75 min",
                "Delicate scopes, cameras", "No cellulose; lumen limits"],
               ["Dry heat", "160 °C/2 h or 170 °C/1 h",
                "Oils, powders, glass, sharps", "Slow; damages fabrics"],
               ["Chemical sterilant", "2 % glutaraldehyde, 10 h",
                "Flexible endoscopes", "Toxic; needs sterile rinse"]],
              widths=None,
              cap="Table 0.2 — Sterilisation methods compared"),
          side_box={"title": "Wet pack = contaminated",
                    "lines": ["Any moisture inside or outside a processed "
                              "pack makes it **unusable**.",
                              "Common causes: overloaded tray, exceeding "
                              "11 kg, poor drying time, cold surfaces, "
                              "instruments packed wet."]},
          points=[
              "**Cleaning precedes sterilisation** — an unclean instrument "
              "cannot be sterilised, because soil shields organisms.",
              "Always state **cool water first**; hot water fixes protein.",
              "Learn the two steam pairs verbatim: **121 °C/15 min** and "
              "**134 °C/3 min**.",
              "The biological indicator for **steam** is //Geobacillus "
              "stearothermophilus//; for **EO and dry heat** it is "
              "//Bacillus atrophaeus//.",
              "**Bowie-Dick** test = air removal in a pre-vacuum "
              "steriliser, run daily.",
          ],
          qa=[
              ("Outline the steps of instrument reprocessing.",
               "Point-of-use care → contained transport → decontamination "
               "(sort, cool rinse, enzymatic soak, manual/ultrasonic/washer "
               "cleaning, rinse, dry) → inspection and function testing → "
               "assembly with count sheet → packaging with indicators → "
               "sterilisation → cooling, labelling and controlled storage."),
              ("Why must instruments be dry before packing?",
               "Residual moisture causes wet packs (regarded as "
               "contaminated), staining and corrosion, and can dilute or "
               "impede the sterilant."),
          ]),

        # ================================================== 0.6
        T("0.6", "Setting the Back Table and Mayo Stand",
          aka="Sterile field organisation",
          lead="Two surfaces carry the tray in theatre. The **back table** "
               "holds the bulk of the set and supplies; the **Mayo stand** "
               "is the immediate working surface and carries only what the "
               "current step requires. Organisation is deliberate and "
               "identical every time, so instruments can be found by feel.",
          figs=[FIG("fig_backtable",
                    "Fig 0.10 — Back table: standard zoned arrangement",
                    w=13.2),
                FIG("fig_mayo_stand",
                    "Fig 0.11 — Mayo stand: the working surface", w=13.2)],
          groups=[
              G("Back table — rules of arrangement", [
                  ("—", "Zone by function",
                   "Sharps and suture · instruments · sponges and dressings "
                   "· basins, drapes and gowns."),
                  ("—", "Group and align",
                   "Instruments grouped by functional class with all tips "
                   "pointing the same way."),
                  ("—", "Segregate sharps",
                   "Blades and needles in a magnetic pad, needle book or "
                   "counter — never loose among instruments or sponges."),
                  ("—", "Heaviest and least used furthest away",
                   "Basins, extra drapes and gowns at the far end."),
                  ("—", "Only the top surface is sterile",
                   "A draped table is sterile at table-top level only; "
                   "anything below the edge is unsterile."),
                  ("—", "Never reach across",
                   "Approach the table from your own side; do not lean over "
                   "the sterile field."),
              ]),
              G("Mayo stand — rules of use", [
                  ("—", "Carry only what is needed now",
                   "Knife, scissors, forceps, haemostats, needle holder and "
                   "suture for the current step."),
                  ("—", "Fixed quadrants",
                   "Keep the same layout for every case so instruments can "
                   "be picked without looking."),
                  ("—", "Position after draping",
                   "Never place the stand over the patient until draping is "
                   "complete."),
                  ("—", "Replenish continuously",
                   "Return used instruments to the back table, wiped clean, "
                   "and refresh the stand for the next step."),
              ]),
              G("General sterile-field discipline", [
                  ("—", "Sterile to sterile only",
                   "Sterile items and personnel contact only sterile items."),
                  ("—", "Keep within view",
                   "An unobserved sterile field is considered "
                   "contaminated."),
                  ("—", "Gown sterile zone",
                   "Front from chest to sterile-field level, and sleeves "
                   "from 5 cm above the elbow to the cuff."),
                  ("—", "Hands in sight",
                   "Keep hands above waist and in front; never below the "
                   "table edge or under the arms."),
                  ("—", "Moisture transmits contamination",
                   "Strike-through of a wet drape contaminates the field."),
                  ("—", "Open packs away from you",
                   "The far flap first, near flap last; the 2.5 cm pack "
                   "margin is unsterile."),
              ]),
          ],
          side_box={"title": "Sequence of setting up",
                    "lines": ["Scrub, gown and glove.",
                              "Drape the back table and Mayo stand.",
                              "Arrange in zones; assemble blades on handles "
                              "using a needle holder.",
                              "Load needles onto holders; prepare suture.",
                              "Perform the **first count** with the "
                              "circulating nurse.",
                              "Drape the patient; bring the Mayo stand into "
                              "position last."]},
          points=[
              "**Only the table top is sterile** — a very common one-liner.",
              "Blades are mounted and removed with a **needle holder**, "
              "never fingers.",
              "The **first count occurs before the skin incision**.",
              "The Mayo stand comes over the patient **after** draping is "
              "complete.",
          ],
          qa=[
              ("How is the back table organised?",
               "In fixed functional zones — sharps and suture, instruments "
               "grouped by class with tips aligned, sponges and dressings, "
               "then basins/drapes/gowns furthest away — with sharps "
               "segregated and heavy items away from the edge; only the "
               "table-top surface is sterile."),
              ("Differentiate the back table from the Mayo stand.",
               "The back table holds the entire set and supplies and stays "
               "away from the patient; the Mayo stand is a small movable "
               "surface holding only the instruments required for the "
               "current step, positioned over the patient after draping."),
          ]),

        # ================================================== 0.7
        T("0.7", "The Surgical Count",
          aka="Sponge, sharp and instrument count",
          lead="The count is the systematic, audible, concurrent tally of "
               "every countable item, performed by the **scrub and "
               "circulating nurse together**, and recorded. Its purpose is "
               "to prevent a **retained surgical item** — a sentinel event.",
          figs=[FIG("fig_count",
                    "Fig 0.12 — When to count and what to count", w=12.6)],
          groups=[
              G("What is counted", [
                  ("—", "Sponges and gauze",
                   "Raytex, laparotomy pads, peanuts — all radio-opaque; "
                   "counted in standard bundles of 5 or 10."),
                  ("—", "Sharps",
                   "Blades, suture needles, hypodermic needles, "
                   "electrosurgical tips, safety pins."),
                  ("—", "Instruments",
                   "Every item on the count sheet, including detachable "
                   "parts (blades, screws, inner tubes)."),
                  ("—", "Miscellaneous",
                   "Umbilical and cotton tapes, vessel loops, clip "
                   "cartridges, bulldogs, trocar seals, catheter guidewires."),
              ]),
              G("When to count", [
                  ("1", "Before the incision",
                   "Baseline count — establishes the reference figure."),
                  ("2", "Before closure of a cavity",
                   "e.g. before the peritoneum is closed."),
                  ("3", "Before closure of the wound",
                   "At the fascial / muscle layer."),
                  ("4", "At skin closure",
                   "Final reconciliation and documentation."),
                  ("+", "Additional counts",
                   "On any change of scrub or circulating nurse, whenever "
                   "items are added, and whenever there is any doubt."),
              ]),
              G("How to count", [
                  ("—", "Audibly and concurrently",
                   "Both nurses see and count each item at the same time."),
                  ("—", "In a set sequence",
                   "Field → Mayo stand → back table → off-field "
                   "receptacles; always the same order."),
                  ("—", "Separate and display",
                   "Sponges separated and spread; needles counted on a "
                   "magnetic pad or in a needle box."),
                  ("—", "Record immediately",
                   "Documented on the count sheet/board as each count is "
                   "completed."),
                  ("—", "Never remove counted items",
                   "No counted sponge or sharp leaves the theatre until the "
                   "case ends."),
              ]),
              G("If the count does not reconcile", [
                  ("1", "Inform the surgeon at once", "Closure pauses."),
                  ("2", "Recount", "Repeat the full count in sequence."),
                  ("3", "Search systematically",
                   "Wound, drapes, floor, kick buckets, laundry, waste, "
                   "under the table and equipment."),
                  ("4", "Radiograph",
                   "Intra-operative X-ray of the surgical site if still "
                   "unaccounted for."),
                  ("5", "Document and report",
                   "Record the discrepancy, the actions taken and the "
                   "outcome; complete an incident report."),
              ]),
          ],
          side_box={"title": "High-risk situations",
                    "lines": ["Emergency and unplanned surgery",
                              "Change of operative plan mid-case",
                              "High BMI / deep cavity",
                              "Multiple surgical teams or cavities",
                              "Change of nursing staff during the case",
                              "Large blood loss and rapid packing"]},
          points=[
              "The count is **concurrent and audible** — never performed by "
              "one person alone.",
              "**Four count points** are the standard answer: before "
              "incision, before cavity closure, before wound closure, at "
              "skin closure.",
              "All sponges used in theatre must be **radio-opaque**; plain "
              "gauze is never used inside a cavity.",
              "An incorrect count is a **surgical emergency of "
              "documentation** — inform, recount, search, X-ray, document.",
          ],
          qa=[
              ("When is the surgical count performed?",
               "Before the skin incision (baseline), before closure of a "
               "cavity, before closure of the wound, and at skin closure — "
               "plus on any staff change, whenever items are added, and "
               "whenever there is doubt."),
              ("What are the steps when a count is incorrect?",
               "Inform the surgeon immediately, recount, undertake a "
               "systematic search of wound and environment, obtain an "
               "intra-operative radiograph if still unresolved, then "
               "document fully and file an incident report."),
          ]),

        # ================================================== 0.8
        T("0.8", "Care, Handling and Maintenance of Instruments",
          aka="Prolonging instrument life",
          lead="Instruments are the most expensive reusable asset in "
               "theatre. Most damage is avoidable and arises from four "
               "causes: **dried blood, wrong-use force, incompatible "
               "chemicals and careless handling**.",
          plate=PL("Instruments damaged by misuse",
                   [("metzenbaum", "Metzenbaum used on suture — blunted"),
                    ("needle_holder", "Needle holder used as a clamp — "
                     "worn insert"),
                    ("adson", "Fine forceps dropped — bent, non-apposing "
                     "tips")],
                   cap="Fig 0.13 — Typical avoidable damage"),
          groups=[
              G("Rules of care", [
                  ("1", "Use each instrument only for its purpose",
                   "Tissue scissors never cut suture; needle holders never "
                   "clamp vessels; haemostats never used as towel clips."),
                  ("2", "Keep blood moist, remove it early",
                   "Wipe with a damp sponge during the case; dried blood is "
                   "corrosive and hard to remove."),
                  ("3", "Rinse in cool water",
                   "Hot water coagulates protein onto the surface."),
                  ("4", "Handle delicate items individually",
                   "Microsurgical, ophthalmic and vascular instruments are "
                   "never piled loose; use tip guards and racks."),
                  ("5", "Avoid saline and harsh chemicals",
                   "Sodium chloride causes pitting; bleach, iodine and "
                   "strong acids/alkalis destroy passivation."),
                  ("6", "Lubricate the joints",
                   "Water-soluble, steam-permeable instrument milk after "
                   "each cleaning cycle."),
                  ("7", "Do not mix metals",
                   "Stainless with chrome-plated or aluminium in an "
                   "ultrasonic bath causes electrolytic damage."),
                  ("8", "Inspect every cycle",
                   "Cleanliness, alignment, sharpness, ratchet, box lock, "
                   "cracks, corrosion."),
                  ("9", "Repair or retire promptly",
                   "Tag and remove faulty items; never return them to "
                   "circulation."),
                  ("10", "Store protected",
                   "Cool, dry, dust-free, closed cupboards; do not stack "
                   "heavy sets on delicate ones."),
              ]),
              G("Recognising and dealing with surface problems", [
                  ("—", "Water spots",
                   "White film from hard water — use demineralised water "
                   "for the final rinse."),
                  ("—", "Brown/orange stain",
                   "Usually not rust but a deposit from detergent or water; "
                   "test with a pencil eraser — if it wipes off, it is a "
                   "stain."),
                  ("—", "True rust and pitting",
                   "Breach of the passive chromium-oxide layer, commonly "
                   "from saline or dried blood; item is condemned."),
                  ("—", "Black stain", "Acidic exposure or dissimilar metal "
                   "contact."),
                  ("—", "Bluish-grey stain",
                   "Excess cold sterilant or over-lubrication."),
              ]),
          ],
          side_box={"title": "Passivation",
                    "lines": ["Surgical stainless steel resists corrosion "
                              "because of a thin **chromium-oxide passive "
                              "layer**.",
                              "Saline, dried blood, abrasives and harsh "
                              "chemicals breach it — after which corrosion "
                              "is progressive and irreversible."]},
          points=[
              "**Never use tissue scissors to cut suture** — the single most "
              "quoted misuse.",
              "**Saline is the enemy of stainless steel**; blot and rinse "
              "immediately after any saline contact.",
              "Distinguish **stain** (wipes off) from **rust/pitting** "
              "(does not — condemn the item).",
              "Lubricants must be **water-soluble and steam-permeable**; "
              "mineral oil prevents sterilisation.",
          ],
          qa=[
              ("List the principles of care and handling of surgical "
               "instruments.",
               "Use only for the intended purpose; remove blood early and "
               "keep instruments moist; rinse in cool water; handle "
               "delicate items individually with tip protection; avoid "
               "saline and harsh chemicals; lubricate joints with a "
               "water-soluble agent; do not mix dissimilar metals; inspect "
               "every cycle; remove faulty items from service; store cool, "
               "dry and protected."),
              ("What causes pitting of stainless-steel instruments?",
               "Breach of the passive chromium-oxide layer, most often by "
               "prolonged contact with sodium chloride (saline or blood) or "
               "harsh chemical agents."),
          ]),

        # ================================================== 0.9
        T("0.9", "How the Trays Relate to One Another",
          aka="The tray ladder and the add-on principle",
          lead="The fifty trays in this syllabus are not fifty unrelated "
               "lists. Almost every speciality tray is a **basic tray plus "
               "speciality add-ons**. Learning the three general-surgery "
               "reference trays first — limited, basic/minor and major — "
               "reduces the remaining work enormously, because you then "
               "only have to remember **what is added**.",
          figs=[FIG("fig_tray_ladder",
                    "Fig 0.14 — The general-surgery tray ladder", w=13.2)],
          groups=[
              G("The three reference trays", [
                  ("—", "Limited procedures tray",
                   "The smallest set: superficial, brief procedures — skin "
                   "lesion excision, biopsy, simple suturing."),
                  ("—", "Basic / minor procedures tray",
                   "The general-purpose small set on which most other trays "
                   "are built."),
                  ("—", "Major procedures tray",
                   "Full laparotomy capability: deep retraction, long "
                   "instruments, complete clamping range."),
              ]),
              G("How speciality trays are built", [
                  ("—", "Basic + length",
                   "**Long instruments tray** — the major tray in longer "
                   "patterns for deep or obese fields."),
                  ("—", "Basic + regional exposure",
                   "**Thyroid tray** adds Lahey clamps and small "
                   "right-angled retractors; **rectal tray** adds anal "
                   "retractors and specula."),
                  ("—", "Basic + organ-specific instruments",
                   "**Biliary tray** adds gallbladder forceps, Bakes "
                   "dilators and cholangiography accessories."),
                  ("—", "Basic + endoscopic system",
                   "**Laparoscopy, sigmoidoscopy, choledochoscopy, "
                   "arthroscopy, mediastinoscopy** trays add a scope, light "
                   "source and camera to a small open set kept for "
                   "conversion."),
                  ("—", "Basic + power and implants",
                   "**Orthopaedic and cardiac trays** add powered "
                   "instruments, implant-specific sets and trial "
                   "components."),
                  ("—", "Scaled down",
                   "**Paediatric trays** are the adult trays in shorter, "
                   "finer, lighter patterns with smaller quantities."),
              ]),
          ],
          compare=CMP(
              ["Reference tray", "Depth of field", "Typical contents scale",
               "Built upon by"],
              [["Limited", "Skin and subcutaneous only", "≈ 15–25 items",
                "Minor ENT, ophthalmic, vasectomy, myringotomy"],
               ["Basic / minor", "Superficial cavity, small clean cases",
                "≈ 40–60 items",
                "Thyroid, rectal, D&C, basic ortho, laparoscopy"],
               ["Major", "Deep body cavity — abdomen, chest",
                "≈ 80–120 items",
                "Biliary, GI, hysterectomy, kidney, thoracotomy, cardiac"]],
              cap="Table 0.3 — Choose the reference tray, then add the "
                  "speciality items"),
          side_box={"title": "Exam strategy",
                    "lines": ["For any tray asked, answer in three moves:",
                              "**1.** Name the reference tray it is built on.",
                              "**2.** List contents under the six "
                              "functional groups.",
                              "**3.** Name the **speciality add-ons** that "
                              "make it that particular tray.",
                              "This structure earns marks even where your "
                              "recall of individual items is incomplete."]},
          points=[
              "Learn **limited → basic → major** thoroughly; the other "
              "forty-seven trays are variations.",
              "For every speciality tray, be able to state its **signature "
              "instrument** (the item that identifies it).",
              "Endoscopic trays always retain a **small open set for "
              "conversion** — a frequently forgotten mark.",
          ],
          qa=[
              ("How would you approach a question on any unfamiliar tray?",
               "Identify the reference tray it is built on (limited, basic "
               "or major), list its contents systematically under the six "
               "functional groups, and then state the speciality add-ons "
               "and the signature instrument that define it."),
          ]),
    ])
