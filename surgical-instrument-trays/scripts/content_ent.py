#!/usr/bin/env python3
"""Part VIII -- Otorhinolaryngologic (ENT) Trays."""
from schema import T, P, PL, DP, FIG, G, CMP

ENT = P(
    "VIII", "Otorhinolaryngologic (ENT) Trays",
    "Basic ear · Nasal · Myringotomy · Tonsillectomy and adenoidectomy · "
    "Tracheostomy · Antral puncture",
    intro="ENT surgery is performed in **small, deep, angled cavities "
          "reached through natural orifices**. Three consequences follow, "
          "and they define every tray in this Part: instruments are "
          "**short-shafted, fine, angled and often bayonet-shaped**; "
          "**illumination and magnification** (head-light, microscope, "
          "endoscope) are as essential as the instruments; and because the "
          "**airway** is shared with the anaesthetist, airway safety "
          "equipment is part of tray preparation.",
    trays=[

        # ============================================================ 8.1
        T("8.1", "Basic Ear Procedures Tray",
          aka="Otologic tray · middle-ear and mastoid set",
          lead="The **basic ear tray** serves operations on the external "
               "canal, tympanic membrane, middle ear and mastoid. Because "
               "the ossicles are measured in millimetres, this is a "
               "**microsurgical tray**: it is used with an **operating "
               "microscope**, its instruments are the smallest in general "
               "ENT practice, and it carries a **micro-drill** for the "
               "mastoid bone.",
          uses=["Myringoplasty and tympanoplasty for a perforation",
                "Cortical mastoidectomy and modified radical mastoidectomy "
                "for chronic suppurative otitis media",
                "Ossiculoplasty; stapedectomy / stapedotomy for otosclerosis",
                "Excision of a cholesteatoma",
                "Exploratory tympanotomy",
                "Removal of a deeply impacted foreign body or exostosis",
                "Cochlear implantation (with the implant-specific set)"],
          plate=PL("Signature instruments",
                   [("ear_speculum", "Aural speculum (funnel)"),
                    ("ear_curette", "Fine ear curette"),
                    ("myringotomy_knife", "Fine angled ear knife"),
                    ("frazier", "Fine suction with thumb vent"),
                    ("periosteal", "Periosteal elevator")],
                   cap="Fig 8.1 — Microsurgical instruments for a "
                       "millimetre-scale field"),
          groups=[
              G("Base set", [
                  ("1", "Limited / minor procedures tray",
                   "the incision itself is very small"),
              ]),
              G("Exposure and magnification", [
                  ("—", "**Aural specula, graded sizes (Hartmann)**",
                   "**signature item** — simple metal funnels holding the "
                   "external canal open"),
                  ("1", "Speculum holder", "frees both hands"),
                  ("1", "**Operating microscope with sterile drapes**",
                   "**essential** — the ossicles cannot be seen or handled "
                   "without it"),
                  ("1", "Otoendoscope with camera",
                   "endoscopic ear surgery"),
                  ("2", "Self-retaining (mastoid / Weitlaner) retractors",
                   "postauricular incision"),
                  ("2", "Small Langenbeck retractors", ""),
                  ("2", "Periosteal elevators (Lempert)",
                   "raises periosteum off the mastoid cortex"),
                  ("—", "Ear wicks, cotton and adrenaline solution",
                   "canal decongestion and haemostasis"),
              ]),
              G("Micro-instruments for the middle ear", [
                  ("4", "**Ear (middle-ear) picks and needles, straight and "
                   "angled**",
                   "**signature item** — elevate the tympanic membrane and "
                   "manipulate ossicles"),
                  ("4", "**Fine ear curettes, assorted angles**",
                   "removes bone and granulation from the canal wall and "
                   "attic"),
                  ("2", "**Ear knives — sickle, round and Rosen "
                   "needle**", "incising and elevating the tympanic flap"),
                  ("2", "**Tympanomeatal flap elevator (Duckbill, "
                   "Plester)**", "raises the flap"),
                  ("2", "**Micro cup forceps and micro-alligator forceps**",
                   "**signature item** — grasping a graft or ossicle at "
                   "depth in a narrow canal"),
                  ("2", "Micro-scissors, straight and angled", ""),
                  ("2", "Micro-hooks, blunt and sharp (45°, 90°)", ""),
                  ("2", "Ossicle holding forceps and measuring rod",
                   "sizes an ossicular prosthesis"),
                  ("1", "Stapes (Rosen) elevator, footplate perforator and "
                   "crurotomy scissors", "stapes surgery"),
                  ("—", "**Ossicular prostheses (PORP/TORP) and sizers**",
                   "with a piston/stapes prosthesis for otosclerosis"),
                  ("1", "Fine nerve stimulator / facial nerve monitor",
                   "**identifies and protects the facial nerve**"),
              ]),
              G("Mastoid bone work", [
                  ("1", "**High-speed micro-drill with cutting and diamond "
                   "burrs, graded**",
                   "**signature item** — cutting burrs remove bone quickly, "
                   "diamond burrs polish safely near the facial nerve and "
                   "dura"),
                  ("—", "**Continuous suction–irrigation**",
                   "cools the burr and clears bone dust — **essential to "
                   "avoid thermal injury**"),
                  ("2", "Mastoid gouges, chisels and curettes",
                   "manual bone removal"),
                  ("1", "Mallet, small", ""),
                  ("2", "Bone rongeur, fine", ""),
                  ("—", "Bone pate collector", "used to obliterate a cavity"),
                  ("—", "Bone wax", ""),
              ]),
              G("Grafting and reconstruction", [
                  ("1", "**Temporalis fascia / perichondrium harvesting "
                   "set**", "the standard graft for tympanoplasty"),
                  ("1", "**Fascia press / graft flattener and drying "
                   "board**",
                   "**signature item** — thins and dries the fascia graft"),
                  ("2", "Cartilage knife and cartilage crusher",
                   "cartilage graft for the attic or tympanum"),
                  ("—", "Gelfoam / silastic sheeting",
                   "supports the graft in the middle ear"),
                  ("—", "Fine absorbable and non-absorbable suture", ""),
              ]),
              G("Suction, haemostasis and accessory", [
                  ("4", "**Fine ear suction tips (Baron / Frazier), "
                   "0.5–3 mm, with a thumb vent**",
                   "**signature item** — the vent lets the operator control "
                   "suction so the ossicles and graft are not aspirated"),
                  ("1", "**Bipolar diathermy with fine tips**",
                   "**never monopolar near the facial nerve**"),
                  ("—", "Adrenaline-soaked cotton pledgets, gelatin sponge",
                   ""),
                  ("—", "Warm irrigation and lens defogger", ""),
                  ("—", "Ear dressings, canal packing and a mastoid bandage",
                   ""),
                  ("—", "Specimen containers",
                   "cholesteatoma, granulation for histology and culture"),
                  ("—", "**Facial nerve monitor electrodes**", ""),
              ]),
          ],
          extras=[("Position", "Supine with the head turned so the "
                   "operative ear is uppermost, on a head-ring; a slight "
                   "head-up tilt reduces venous ooze. Hair shaved a short "
                   "distance behind the ear for a postauricular approach."),
                  ("Structures at risk",
                   "**Facial nerve** in its tympanic and mastoid segments "
                   "(the great hazard), chorda tympani, ossicular chain, "
                   "labyrinth and horizontal semicircular canal, dura of "
                   "the middle and posterior fossa, and the sigmoid sinus."),
                  ("Complications",
                   "Facial nerve palsy, sensorineural hearing loss, "
                   "vertigo, tinnitus, graft failure with persistent "
                   "perforation, CSF leak, and injury to the sigmoid sinus "
                   "with bleeding.")],
          side_box={"title": "Cutting versus diamond burr",
                    "lines": ["**Cutting burr** — removes bone quickly; "
                              "used in the bulk of the mastoid.",
                              "**Diamond burr** — abrades slowly and is "
                              "**safer near the facial nerve, dura and "
                              "sinus**; also useful for haemostasis of bone.",
                              "Both need **continuous "
                              "suction–irrigation** to prevent heat "
                              "injury."]},
          points=[
              "State that this is **microsurgery** — the microscope is part "
              "of the tray, not an optional extra.",
              "Name the **graded aural specula** and the **fine vented ear "
              "suction tips (0.5–3 mm)**.",
              "**Micro picks, curettes, alligator and cup forceps** are the "
              "middle-ear instruments.",
              "**Micro-drill with cutting and diamond burrs plus continuous "
              "irrigation** — explain the difference between the burrs.",
              "The **facial nerve monitor** and **bipolar only** near the "
              "nerve are important safety marks.",
              "**Temporalis fascia graft with a fascia press** for "
              "tympanoplasty.",
          ],
          qa=[("Describe the basic ear procedures tray.",
               "A limited/minor tray plus: graded Hartmann aural specula "
               "with a holder, an operating microscope with drapes, "
               "otoendoscope, mastoid self-retaining and Langenbeck "
               "retractors and Lempert periosteal elevators; micro-"
               "instruments — straight and angled ear picks and needles, "
               "fine curettes, sickle and round knives with a Rosen needle, "
               "tympanomeatal flap elevators, micro cup and alligator "
               "forceps, micro-scissors and hooks, ossicle forceps with a "
               "measuring rod, stapes instruments and ossicular prostheses "
               "with sizers; a high-speed micro-drill with cutting and "
               "diamond burrs under continuous suction–irrigation, with "
               "mastoid gouges, curettes, rongeur and bone wax; a temporalis "
               "fascia harvesting set with a fascia press, cartilage knife "
               "and crusher and Gelfoam; and fine vented Baron/Frazier "
               "suction tips 0.5–3 mm, bipolar diathermy, adrenaline "
               "pledgets, ear packing and a facial nerve monitor."),
              ("What is the difference between a cutting and a diamond burr?",
               "A cutting burr has sharp flutes and removes bone rapidly, "
               "used for the bulk of mastoid bone. A diamond burr has an "
               "abrasive diamond-coated surface that removes bone slowly and "
               "controllably, and is used close to the facial nerve, dura, "
               "sigmoid sinus and labyrinth, where it is far safer; it also "
               "produces haemostasis of bleeding bone. Both require "
               "continuous irrigation to prevent thermal injury.")]),

        # ============================================================ 8.2
        T("8.2", "Nasal Procedures Tray",
          aka="Rhinologic tray · septoplasty, polypectomy and FESS set",
          lead="The **nasal tray** covers septal, turbinate and sinus "
               "surgery. Its instruments are **long, thin and often "
               "bayonet-shaped**, so that the operator's hand and the "
               "instrument shaft do not obstruct the line of sight down the "
               "nostril. Two constants: **decongestion and topical "
               "vasoconstriction** are part of the preparation, and "
               "**endoscopic vision** has become standard.",
          uses=["Septoplasty and submucous resection for a deviated septum",
                "Reduction of a fractured nose; septorhinoplasty",
                "Polypectomy; turbinate reduction",
                "Functional endoscopic sinus surgery (FESS) — "
                "antrostomy, ethmoidectomy, sphenoidotomy",
                "Control of severe epistaxis; arterial ligation",
                "Excision of a nasal tumour; closure of a septal "
                "perforation",
                "Dacryocystorhinostomy (endonasal approach)"],
          plate=PL("Signature instruments",
                   [("nasal_speculum", "Nasal speculum (Thudichum/Killian)"),
                    ("periosteal", "Freer septal elevator"),
                    ("bone_rasp", "Nasal rasp"),
                    ("rongeur", "Nasal / antral punch forceps"),
                    ("frazier", "Fine nasal suction")],
                   cap="Fig 8.2 — Long, thin, bayonet-shaped instruments"),
          groups=[
              G("Base set", [
                  ("1", "Basic / minor procedures tray", "see 1.2"),
              ]),
              G("Exposure and visualisation", [
                  ("—", "**Nasal specula, graded (Thudichum, Killian, "
                   "Cottle)**",
                   "**signature item** — Killian has long blades for deep "
                   "septal work"),
                  ("1", "Head-light or head-mirror",
                   "illumination down a narrow passage"),
                  ("1", "**Rigid nasal endoscopes 0°, 30°, 45°, 70° (4 mm "
                   "and 2.7 mm) with camera, light source and monitor**",
                   "**signature item** — the basis of all modern sinus "
                   "surgery"),
                  ("—", "Endoscope lens cleaning / anti-fog system", ""),
                  ("2", "Nasal retractors (Aufricht, Cottle)",
                   "open rhinoplasty"),
                  ("—", "**Topical decongestant — adrenaline / "
                   "xylometazoline on ribbon gauze or neuropatties**",
                   "**shrinks mucosa, reduces bleeding and enlarges the "
                   "working space — done before instrumentation**"),
                  ("—", "Local anaesthetic with adrenaline and a fine "
                   "long needle", "infiltration and blocks"),
              ]),
              G("Septal instruments", [
                  ("2", "**Freer / Cottle septal elevator (mucoperiosteal "
                   "elevator)**",
                   "**signature item** — raises the mucoperichondrial flap "
                   "off the septal cartilage"),
                  ("1", "**Ballenger swivel knife**",
                   "**signature item** — cuts the septal cartilage in a "
                   "controlled sweep"),
                  ("1", "Septal (D-knife) and Cottle knives", ""),
                  ("2", "**Jansen-Middleton / Tilley-Henckel septum "
                   "cutting forceps**",
                   "**signature item** — removes the deviated bony and "
                   "cartilaginous septum"),
                  ("2", "Luc's / Tilley nasal forceps",
                   "removes fragments and polyps"),
                  ("1", "Septal scissors, angled", ""),
                  ("2", "Cartilage crusher and cartilage scorer",
                   "reshapes a graft"),
                  ("—", "Septal splints and quilting suture",
                   "prevents haematoma and adhesions"),
              ]),
              G("Bone and turbinate instruments", [
                  ("2", "**Nasal rasps and files, fine and coarse**",
                   "smooths a bony hump or spur"),
                  ("2", "Nasal osteotomes, straight and curved, with a "
                   "guard", "lateral and medial osteotomies in rhinoplasty"),
                  ("1", "Mallet, small", ""),
                  ("2", "Nasal gouges and chisels", ""),
                  ("2", "Turbinate scissors and turbinate reduction "
                   "instruments",
                   "with a microdebrider or radiofrequency probe"),
                  ("2", "Bone nibbler / nasal rongeur", ""),
                  ("1", "Mallet-driven bone punch", ""),
              ]),
              G("Sinus (FESS) instruments", [
                  ("2", "**Sickle knife and Freer elevator**",
                   "uncinectomy — opening the ethmoidal infundibulum"),
                  ("2", "**Back-biting forceps**",
                   "**signature item** — cuts backwards, enlarging the "
                   "maxillary antrostomy safely"),
                  ("2", "**Blakesley-Wilde and Blakesley through-cutting "
                   "forceps, straight and up-angled**",
                   "**signature item** — the principal FESS instrument"),
                  ("2", "**Antral / ostium-seeking punch forceps "
                   "(Stammberger)**", "enlarges the natural ostium"),
                  ("2", "Giraffe forceps and Kuhn-Bolger curettes",
                   "frontal recess"),
                  ("2", "Sinus seekers / probes, curved",
                   "locates the natural ostium"),
                  ("1", "**Microdebrider (powered shaver) with straight and "
                   "angled blades**",
                   "removes polyps and mucosa while suctioning — "
                   "**mucosa-sparing**"),
                  ("1", "Suction–irrigation and image-guided navigation "
                   "system",
                   "navigation used in revision and skull-base surgery"),
                  ("2", "Ethmoid forceps, up-biting", ""),
              ]),
              G("Haemostasis, packing and accessory", [
                  ("4", "**Fine nasal suction tips (Frazier, Fergusson), "
                   "with thumb vent**", ""),
                  ("1", "**Bipolar diathermy — including a bayonet-shaped "
                   "nasal bipolar**",
                   "**signature item** — for the sphenopalatine and "
                   "ethmoidal arteries"),
                  ("1", "Suction cautery", ""),
                  ("—", "**Nasal packing — ribbon gauze with paraffin, "
                   "Merocel, absorbable haemostatic packs**", ""),
                  ("—", "**Foley catheter or posterior balloon pack**",
                   "posterior epistaxis"),
                  ("2", "Bayonet forceps and Tilley's dressing forceps",
                   "**bayonet shape keeps the hand out of the line of "
                   "sight**"),
                  ("—", "Silver nitrate / cautery sticks", ""),
                  ("—", "Kidney dish and specimen containers",
                   "polyps and tissue for histology"),
                  ("—", "External nasal splint and tape", ""),
                  ("—", "**Throat pack** and its documented removal",
                   "**a throat pack is a counted item — its removal must be "
                   "recorded**"),
              ]),
          ],
          extras=[("Position", "Supine with a 15–30° head-up tilt "
                   "(reverse Trendelenburg) to reduce venous congestion and "
                   "bleeding; head on a ring, slightly extended."),
                  ("Airway", "Oral endotracheal tube with a **throat "
                   "pack** to prevent blood entering the airway and "
                   "stomach; the pack must be counted, recorded and its "
                   "removal documented."),
                  ("Structures at risk",
                   "**Orbit and optic nerve** (thin lamina papyracea), "
                   "**anterior ethmoidal artery**, **cribriform plate and "
                   "dura** (CSF leak), lacrimal apparatus, and the "
                   "internal carotid artery adjacent to the sphenoid."),
                  ("Complications",
                   "Haemorrhage, septal haematoma and perforation, saddle "
                   "deformity, adhesions, anosmia, orbital injury with "
                   "diplopia or blindness, CSF rhinorrhoea and "
                   "meningitis.")],
          side_box={"title": "Why bayonet-shaped?",
                    "lines": ["Looking down a nostril, a **straight "
                              "instrument and the hand holding it block the "
                              "view**.",
                              "A **bayonet** offset displaces the hand and "
                              "shaft sideways, keeping the line of sight "
                              "clear.",
                              "The same reasoning explains why FESS forceps "
                              "are **up-angled** and why **back-biting** "
                              "forceps exist."]},
          points=[
              "Explain **why instruments are long, thin and bayonet-shaped** "
              "— it demonstrates understanding, not just recall.",
              "**Topical decongestion before instrumentation** is part of "
              "the preparation.",
              "Septal signatures: **Freer elevator, Ballenger swivel knife, "
              "Jansen-Middleton forceps**.",
              "FESS signatures: **Blakesley through-cutting forceps, "
              "back-biting forceps, microdebrider**.",
              "**Bayonet bipolar** for the sphenopalatine artery in "
              "epistaxis.",
              "**Throat pack counted and its removal documented** — a "
              "reliable safety mark.",
              "Name the structures at risk: **orbit, cribriform plate, "
              "anterior ethmoidal artery**.",
          ],
          qa=[("List the instruments of a nasal procedures tray.",
               "A minor tray plus: graded Thudichum, Killian and Cottle "
               "nasal specula, head-light, rigid 0–70° nasal endoscopes with "
               "camera and monitor, Aufricht/Cottle retractors, topical "
               "decongestant and local anaesthetic with adrenaline; septal "
               "instruments — Freer/Cottle elevators, Ballenger swivel "
               "knife, septal knives, Jansen-Middleton and Tilley-Henckel "
               "septum cutting forceps, Luc's forceps, septal scissors, "
               "cartilage crusher and septal splints; bone instruments — "
               "nasal rasps and files, guarded osteotomes, mallet, gouges, "
               "turbinate scissors and rongeurs; FESS instruments — sickle "
               "knife, back-biting forceps, straight and up-angled "
               "Blakesley through-cutting forceps, Stammberger antral punch, "
               "giraffe forceps, Kuhn-Bolger curettes, sinus seekers, "
               "microdebrider and navigation; plus fine vented suction, "
               "bayonet bipolar diathermy, suction cautery, nasal packing, "
               "a Foley or balloon pack for posterior epistaxis, bayonet "
               "forceps, external splint and a counted throat pack."),
              ("Why must a throat pack be documented?",
               "It is inserted to stop blood entering the airway and "
               "stomach, but it is out of sight in the pharynx. If not "
               "removed it causes fatal airway obstruction, so it is "
               "included in the count, recorded on the board or count sheet, "
               "and its removal is explicitly documented before "
               "extubation.")]),

        # ============================================================ 8.3
        T("8.3", "Myringotomy Tray",
          aka="Grommet (ventilation tube) insertion tray",
          lead="**Myringotomy** is a small radial incision in the tympanic "
               "membrane to drain middle-ear fluid, usually followed by "
               "insertion of a **ventilation tube (grommet)**. It is one of "
               "the **smallest trays in surgery** — a handful of "
               "microsurgical instruments used under the operating "
               "microscope — but it is performed extremely commonly, "
               "especially in children.",
          uses=["Otitis media with effusion ('glue ear') with hearing loss",
                "Recurrent acute otitis media — grommet insertion",
                "Acute otitis media with severe pain or impending "
                "complication",
                "Eustachian tube dysfunction; barotrauma",
                "Aspiration of middle-ear fluid for culture",
                "Instillation of intratympanic medication"],
          plate=PL("Signature instruments",
                   [("ear_speculum", "Aural speculum"),
                    ("myringotomy_knife", "Myringotomy knife (lance tip)"),
                    ("ear_curette", "Fine curette / wax hook"),
                    ("frazier", "Fine vented suction, 0.5–2 mm")],
                   cap="Fig 8.3 — Four instruments and a microscope"),
          groups=[
              G("Base set", [
                  ("1", "Limited procedures tray",
                   "very few instruments are needed"),
              ]),
              G("The essential instruments", [
                  ("—", "**Aural specula, graded (including small "
                   "paediatric sizes)**",
                   "**signature item** — the child's canal is narrow"),
                  ("1", "**Operating microscope with sterile drapes**",
                   "**essential** — the incision is 1–2 mm"),
                  ("1", "**Myringotomy knife (lance- or "
                   "sickle-shaped, fine and angled)**",
                   "**signature item** — makes a small radial incision, "
                   "usually antero-inferior"),
                  ("2", "**Fine vented suction tips (Baron), 0.5, 1 and "
                   "2 mm**",
                   "**signature item** — aspirates thin serous or thick "
                   "'glue' effusion; the thumb vent controls the force"),
                  ("2", "**Micro-alligator or crocodile forceps**",
                   "**signature item** — grasps and positions the grommet"),
                  ("1", "Fine ear pick / Rosen needle",
                   "manipulates the tube into place"),
                  ("1", "Wax hook and fine curette",
                   "clears the canal before starting"),
                  ("1", "Blunt-ended ear probe", ""),
              ]),
              G("The ventilation tubes", [
                  ("—", "**Ventilation tubes (grommets) — Shepard, "
                   "Shah, collar-button (short-term)**",
                   "extrude spontaneously in 6–12 months"),
                  ("—", "**T-tubes (long-term)**",
                   "stay in place for years; higher perforation rate"),
                  ("—", "Tube inserter / applicator", ""),
                  ("—", "**Assorted sizes available and checked**",
                   "**tubes are tiny and countable — a dropped grommet must "
                   "be accounted for**"),
              ]),
              G("Accessory", [
                  ("—", "Cotton-wool balls and ear wicks", ""),
                  ("—", "Adrenaline / topical anaesthetic solution",
                   "canal preparation"),
                  ("—", "Antibiotic ear drops",
                   "instilled at the end where indicated"),
                  ("—", "Sterile specimen tube / culture swab",
                   "middle-ear fluid for microbiology"),
                  ("—", "Kidney dish and small gallipot", ""),
                  ("—", "Suction tubing and trap", ""),
              ]),
          ],
          extras=[("Position", "Supine, head turned with the operative ear "
                   "uppermost on a head-ring; brief general anaesthesia in "
                   "children (usually inhalational with a face mask or "
                   "laryngeal mask), local anaesthesia in adults."),
                  ("Site of incision",
                   "The **antero-inferior quadrant** of the tympanic "
                   "membrane. This avoids the **ossicles and the incudostapedial "
                   "joint** (postero-superior quadrant) and the **round "
                   "window**."),
                  ("Post-operative advice",
                   "Keep the ear dry; avoid diving; the tube usually "
                   "extrudes spontaneously in 6–12 months; report "
                   "persistent discharge."),
                  ("Complications",
                   "Otorrhoea, tube blockage, premature extrusion, "
                   "persistent perforation after extrusion, "
                   "tympanosclerosis, and rarely cholesteatoma or "
                   "displacement of the tube into the middle ear.")],
          side_box={"title": "Which quadrant?",
                    "lines": ["Incise the **antero-inferior quadrant**.",
                              "The **postero-superior quadrant** contains "
                              "the **ossicular chain (incudostapedial "
                              "joint)** and must be avoided.",
                              "A guaranteed one-mark question."]},
          points=[
              "This is a **limited tray** procedure — the smallest set in "
              "this syllabus.",
              "The four essentials are **aural speculum, myringotomy knife, "
              "fine vented suction, micro-alligator forceps** — plus the "
              "**microscope**.",
              "**Antero-inferior quadrant** for the incision; avoid the "
              "postero-superior quadrant because of the ossicles.",
              "**Grommets are tiny countable items** — assorted sizes "
              "checked, and a dropped tube accounted for.",
              "Distinguish **short-term grommets (extrude in 6–12 months)** "
              "from **long-term T-tubes**.",
              "Send **middle-ear fluid for culture** where indicated.",
          ],
          qa=[("List the contents of a myringotomy tray.",
               "A limited tray plus graded aural specula including "
               "paediatric sizes, the operating microscope, a fine angled "
               "lance or sickle myringotomy knife, fine vented Baron suction "
               "tips of 0.5, 1 and 2 mm, micro-alligator forceps, a fine ear "
               "pick, wax hook and curette; ventilation tubes — short-term "
               "Shepard/Shah grommets and long-term T-tubes in assorted "
               "checked sizes with an inserter; and cotton wool, ear wicks, "
               "topical adrenaline, antibiotic drops, a culture tube, kidney "
               "dish and suction tubing."),
              ("Where is the myringotomy incision made and why?",
               "In the antero-inferior quadrant of the tympanic membrane. "
               "The postero-superior quadrant is avoided because the "
               "ossicular chain, particularly the incudostapedial joint, and "
               "the round window lie deep to it and could be injured.")]),

        # ============================================================ 8.4
        T("8.4", "Tonsillectomy and Adenoidectomy Tray",
          aka="T&A tray · adenotonsillectomy set",
          lead="Tonsils and adenoids are removed **through the open mouth**, "
               "working around the endotracheal tube in a field that is "
               "**vascular, shared with the airway and impossible to pack "
               "off**. The tray therefore centres on a **mouth gag with "
               "tongue plate** for exposure, instruments to dissect and "
               "snare the tonsil, and a **generous set of long "
               "haemostatic instruments**, because reactionary haemorrhage "
               "is the feared complication.",
          uses=["Recurrent acute tonsillitis meeting accepted criteria",
                "Obstructive sleep apnoea and adenotonsillar hypertrophy "
                "(the commonest paediatric indication)",
                "Peritonsillar abscess (quinsy) — recurrent or interval "
                "tonsillectomy",
                "Suspected tonsillar malignancy — diagnostic tonsillectomy",
                "Chronic adenoiditis; recurrent otitis media with effusion",
                "Halitosis / tonsillar concretions unresponsive to "
                "treatment"],
          plate=PL("Signature instruments",
                   [("mouth_gag", "Boyle-Davis mouth gag"),
                    ("tonsil_snare", "Eves tonsil snare"),
                    ("adenoid_curette", "St Clair Thomson adenoid curette"),
                    ("tonsil_clamp", "Tonsil artery forceps, curved"),
                    ("allis", "Tonsil holding forceps"),
                    ("yankauer", "Wide-bore suction")],
                   cap="Fig 8.4 — Expose the mouth, dissect, snare, "
                       "secure haemostasis"),
          groups=[
              G("Base set", [
                  ("1", "Basic / minor procedures tray",
                   "though most instruments are speciality patterns"),
              ]),
              G("Exposure of the oropharynx", [
                  ("1", "**Boyle-Davis mouth gag with assorted tongue "
                   "blades**",
                   "**signature item** — opens the mouth and depresses the "
                   "tongue, and its slot accommodates the endotracheal tube"),
                  ("1", "**Draffin bipods (suspension rods) with a base "
                   "plate**",
                   "**signature item** — suspends the gag so it holds "
                   "itself and both hands are free"),
                  ("1", "Doughty tongue blade with a tube slot", ""),
                  ("2", "Tongue depressors, assorted", ""),
                  ("1", "**Soft palate retractor and small "
                   "nasopharyngeal (Yankauer) mirror**",
                   "the adenoid bed is seen indirectly with a mirror"),
                  ("1", "Head-light", ""),
                  ("—", "Mouth props and lip/dental protection", ""),
              ]),
              G("Tonsil instruments", [
                  ("2", "**Tonsil holding forceps (Denis Browne, "
                   "Blohmke)**",
                   "**signature item** — grasps the tonsil and applies "
                   "medial traction"),
                  ("1", "**Tonsil dissector / Hurd dissector and pillar "
                   "retractor**",
                   "**signature item** — separates the tonsil from its bed "
                   "in the correct plane"),
                  ("1", "**Eves tonsil snare with wire**",
                   "**signature item** — a wire loop that snares and "
                   "amputates the tonsil at its pedicle"),
                  ("1", "Tonsil knife / Fisher's knife",
                   "incising the mucosa of the anterior pillar"),
                  ("1", "Tonsil scissors, curved", ""),
                  ("1", "**Mollison's / Waugh's tonsil pillar retractor**",
                   ""),
                  ("1", "Coblation / bipolar dissection wand or "
                   "harmonic device",
                   "modern alternatives with reduced blood loss"),
                  ("—", "Bipolar / monopolar diathermy with an insulated "
                   "long tip", ""),
              ]),
              G("Adenoid instruments", [
                  ("2", "**St Clair Thomson adenoid curette with a cage / "
                   "guard**",
                   "**signature item** — the boxed cage captures the "
                   "adenoid tissue so it is not aspirated"),
                  ("2", "Adenoid curettes, assorted sizes, without cage",
                   ""),
                  ("1", "**Adenotome (La Force) and adenoid punch "
                   "forceps**", ""),
                  ("1", "Suction diathermy / microdebrider for adenoid "
                   "ablation",
                   "endoscopically guided adenoidectomy"),
                  ("1", "Nasopharyngeal mirror and 45° endoscope", ""),
              ]),
              G("Haemostasis — the critical group", [
                  ("6", "**Tonsil artery forceps (Negus, Birkett), long and "
                   "curved**",
                   "**signature item** — long curved clamps reaching the "
                   "tonsil bed"),
                  ("2", "**Tonsil (Negus) ligature/knot-tying forceps**",
                   "ties a ligature deep in the fossa"),
                  ("2", "Long needle holders with tonsil sutures",
                   "under-running a bleeding point"),
                  ("—", "**Tonsil swabs / gauze balls on a holder "
                   "(Wilson / peanut swabs)**",
                   "pressure haemostasis in the fossa; **counted**"),
                  ("2", "**Wide-bore suction (Yankauer) with spare "
                   "tubing**",
                   "**blood and clot obscure the airway instantly**"),
                  ("—", "Suction cautery and bipolar forceps, long", ""),
                  ("—", "Haemostatic agents and adrenaline-soaked swabs",
                   ""),
                  ("—", "**Cross-matched blood availability for a "
                   "bleeding tonsil**", ""),
              ]),
              G("Airway safety — part of tray preparation", [
                  ("—", "**Complete difficult-airway trolley and spare "
                   "endotracheal tubes**",
                   "the airway is shared and can be lost"),
                  ("—", "**Working suction — two independent units**",
                   "**essential** if brisk bleeding occurs"),
                  ("—", "Laryngoscope, bougie, oral and nasal airways", ""),
                  ("—", "**Tracheostomy set available**", ""),
                  ("—", "Throat pack, if used — **counted and its removal "
                   "documented**", ""),
                  ("—", "Specimen containers",
                   "**tonsils sent separately labelled left and right** "
                   "when malignancy is suspected"),
              ]),
          ],
          extras=[("Position", "**Supine with the head extended and a "
                   "sandbag or head-ring under the shoulders (Rose "
                   "position)**; the surgeon sits or stands at the head of "
                   "the table. The gag is suspended on Draffin bipods."),
                  ("Anaesthesia", "General anaesthesia with an oral "
                   "endotracheal tube (or laryngeal mask), which sits in "
                   "the slot of the tongue blade."),
                  ("Haemorrhage", "**Primary** — during surgery; "
                   "**reactionary (secondary primary)** — within 24 hours, "
                   "usually from a slipped ligature and requiring a return "
                   "to theatre; **secondary** — 5–10 days, usually from "
                   "infection of the fossa. Distinguishing these is a very "
                   "common question."),
                  ("Complications",
                   "Haemorrhage (the major risk), airway obstruction from "
                   "clot, injury to teeth and lips from the gag, "
                   "dehydration and pain, velopharyngeal insufficiency and "
                   "nasal regurgitation after adenoidectomy, and Grisel's "
                   "syndrome (atlantoaxial subluxation).")],
          side_box={"title": "The bleeding tonsil",
                    "lines": ["A post-tonsillectomy bleed is an "
                              "**emergency**: the patient may be "
                              "hypovolaemic with a **stomach full of "
                              "swallowed blood**.",
                              "Preparation: **two working suctions**, "
                              "difficult-airway trolley, cross-matched "
                              "blood, rapid-sequence induction, and a "
                              "**tonsil bleeding set** — gag, long curved "
                              "artery forceps, ligature forceps and "
                              "swabs."]},
          points=[
              "**Boyle-Davis gag with Draffin bipods** is the exposure "
              "signature — explain that the tongue blade has a slot for the "
              "endotracheal tube.",
              "Name **Eves snare, tonsil holding forceps, Hurd dissector** "
              "for the tonsil and **St Clair Thomson caged curette** for the "
              "adenoid.",
              "Explain **why the adenoid curette has a cage** — to capture "
              "tissue and prevent aspiration.",
              "**Long curved tonsil artery forceps and ligature forceps** "
              "plus **two working suctions** for haemostasis.",
              "Classify haemorrhage as **primary, reactionary and "
              "secondary** with timings and causes.",
              "The **airway is shared** — difficult-airway trolley and "
              "tracheostomy set available.",
              "**Rose position** with the head extended, gag suspended on "
              "bipods.",
          ],
          pitfalls=["Forgetting that the tongue blade must accommodate the "
                    "endotracheal tube.",
                    "Providing only one suction unit.",
                    "Omitting the classification of post-tonsillectomy "
                    "haemorrhage.",
                    "Not sending tonsils separately labelled when "
                    "malignancy is suspected."],
          qa=[("Describe the tonsillectomy and adenoidectomy tray.",
               "**Exposure**: Boyle-Davis mouth gag with assorted tongue "
               "blades having a slot for the endotracheal tube, suspended on "
               "Draffin bipods with a base plate; Doughty blade, tongue "
               "depressors, soft palate retractor, nasopharyngeal mirror and "
               "head-light. **Tonsil**: Denis Browne or Blohmke tonsil "
               "holding forceps, Hurd dissector and pillar retractor, Eves "
               "snare with wire, Fisher's tonsil knife, curved tonsil "
               "scissors, Mollison's pillar retractor, and coblation or "
               "bipolar dissection devices. **Adenoid**: St Clair Thomson "
               "caged adenoid curette, plain curettes in assorted sizes, La "
               "Force adenotome, adenoid punch and suction diathermy or "
               "microdebrider with a 45° endoscope. **Haemostasis**: long "
               "curved Negus or Birkett tonsil artery forceps, Negus "
               "ligature-tying forceps, long needle holders with sutures, "
               "counted tonsil swabs on holders, two wide-bore Yankauer "
               "suctions, long bipolar and suction cautery, haemostatic "
               "agents and cross-matched blood. **Airway safety**: "
               "difficult-airway trolley with spare tubes, two independent "
               "suction units, a tracheostomy set, and a counted, documented "
               "throat pack if used, with separately labelled specimen "
               "containers."),
              ("Classify post-tonsillectomy haemorrhage.",
               "**Primary** haemorrhage occurs during the operation itself. "
               "**Reactionary** haemorrhage occurs within the first 24 hours, "
               "typically from a slipped ligature or as the vasoconstrictor "
               "effect wears off and blood pressure rises; it usually "
               "requires return to theatre. **Secondary** haemorrhage occurs "
               "5–10 days post-operatively and is usually due to infection "
               "of the tonsillar fossa; it is often managed with "
               "antibiotics, though severe bleeding requires surgery.")]),

        # ============================================================ 8.5
        T("8.5", "Tracheostomy Tray",
          aka="Tracheostomy set · surgical airway tray",
          lead="**Tracheostomy** creates an opening in the trachea and "
               "inserts a tube to provide a secure airway. The tray is "
               "small but is the **most time-critical set in surgery**: it "
               "may be needed in seconds, so it is kept **pre-assembled, "
               "checked and immediately available** wherever airway "
               "obstruction is a possibility. Its defining items are the "
               "**tracheal dilator, tracheal hook and a checked range of "
               "tracheostomy tubes**.",
          uses=["Upper airway obstruction — tumour, trauma, bilateral vocal "
                "cord palsy, severe infection",
                "Prolonged mechanical ventilation and weaning",
                "Bronchial toilet in a patient unable to clear secretions",
                "Elective, as part of major head-and-neck or laryngeal "
                "surgery",
                "Protection of the airway against aspiration",
                "Emergency surgical airway (though cricothyroidotomy is "
                "faster in a true emergency)"],
          plate=PL("Signature instruments",
                   [("trach_tube", "Tracheostomy tube with flange"),
                    ("trousseau", "Trousseau tracheal dilator"),
                    ("weitlaner", "Small self-retaining retractor"),
                    ("scalpel_15", "No.15 blade"),
                    ("mosquito", "Fine artery forceps")],
                   cap="Fig 8.5 — Open the trachea, hold it open, "
                       "insert the tube"),
          groups=[
              G("Base set", [
                  ("1", "Basic / minor procedures tray",
                   "the incision is short and superficial"),
              ]),
              G("The three defining instruments", [
                  ("1", "**Trousseau (or Laborde) tracheal dilator**",
                   "**signature item** — its three blades open on squeezing "
                   "the rings, holding the tracheal incision open while the "
                   "tube is introduced"),
                  ("1", "**Tracheal hook (sharp, single or double)**",
                   "**signature item** — steadies the trachea and pulls the "
                   "cricoid upward, preventing the trachea from slipping "
                   "away"),
                  ("—", "**Tracheostomy tubes — full range of sizes, "
                   "cuffed and uncuffed, fenestrated and non-fenestrated, "
                   "with inner cannulae, obturators and flanges**",
                   "**signature requirement** — the size chosen and the "
                   "**next size smaller** must both be checked, cuffs "
                   "tested and connectors verified"),
              ]),
              G("Exposure of the trachea", [
                  ("2", "Knife handle No.3 with No.15 and No.10 blades",
                   "transverse or vertical skin incision"),
                  ("2", "Small self-retaining (Weitlaner) retractors", ""),
                  ("2", "Langenbeck / Army-Navy retractors", ""),
                  ("1", "**Cricoid hook and thyroid (Green) retractor**",
                   "retracts the thyroid isthmus"),
                  ("2", "Fine Metzenbaum scissors and dissecting forceps",
                   "separating the strap muscles in the midline"),
                  ("8", "**Fine mosquito and Crile artery forceps**",
                   "the anterior jugular veins and thyroid isthmus bleed"),
                  ("2", "Kocher clamps", ""),
                  ("1", "Small periosteal / tracheal elevator", ""),
                  ("—", "Local anaesthetic with adrenaline",
                   "even under general anaesthesia, reduces bleeding"),
              ]),
              G("Securing the tube and closure", [
                  ("2", "Needle holders",
                   "stay sutures and skin closure"),
                  ("—", "**Tracheal stay sutures (2-0 or 3-0 "
                   "non-absorbable)**",
                   "**signature requirement** — placed through the tracheal "
                   "wall on each side of the opening and left long; if the "
                   "tube is displaced early, traction on them reopens the "
                   "trachea. **Especially vital in children.**"),
                  ("—", "Flange sutures / tracheostomy tapes",
                   "secures the tube to the skin and around the neck"),
                  ("—", "Keyhole dressing and barrier film", ""),
                  ("—", "Absorbable suture for platysma; loose skin closure",
                   "**skin is closed loosely** — tight closure risks "
                   "surgical emphysema"),
              ]),
              G("Airway and emergency equipment — inseparable from the tray",
                [("—", "**Two working suction units with wide-bore and fine "
                   "catheters**",
                   "**essential** — blood and secretions must be cleared "
                   "instantly"),
                 ("—", "**Spare tracheostomy tube of the same size AND one "
                   "size smaller, at the bedside**",
                   "**the single most examined safety point**"),
                 ("—", "**Tracheal dilator and spare tracheal hook kept at "
                   "the bedside**", "for accidental decannulation"),
                 ("—", "Difficult-airway trolley, laryngoscope, bougie, "
                   "spare endotracheal tubes", ""),
                 ("—", "Self-inflating bag with tracheostomy connector, "
                   "oxygen and humidification", ""),
                 ("—", "Cuff-pressure manometer and 10 mL syringe", ""),
                 ("—", "**Cricothyroidotomy set**",
                   "faster than tracheostomy in a true 'cannot intubate, "
                   "cannot oxygenate' emergency"),
                 ("—", "Rigid bronchoscope available", ""),
                 ("—", "Capnography and pulse oximetry", "")]),
          ],
          extras=[("Position", "Supine with the **neck extended over a "
                   "sandbag or pillow between the shoulders and the head "
                   "on a ring**, giving maximum tracheal prominence. "
                   "In a child the extension must not be excessive."),
                  ("Level of incision",
                   "Through the **2nd to 4th tracheal rings**. Higher risks "
                   "subglottic stenosis and cricoid injury; lower risks "
                   "injury to the great vessels and a "
                   "tracheo-innominate fistula."),
                  ("Structures at risk",
                   "Anterior jugular veins, thyroid isthmus, "
                   "**inferior thyroid veins and the thyroid ima artery**, "
                   "recurrent laryngeal nerves in the paratracheal groove, "
                   "the pleural domes (especially in children), and the "
                   "oesophagus posteriorly."),
                  ("Complications",
                   "**Immediate** — haemorrhage, pneumothorax, "
                   "pneumomediastinum, tube misplacement, apnoea. "
                   "**Early** — tube blockage or displacement, surgical "
                   "emphysema, infection, dysphagia. **Late** — tracheal "
                   "stenosis, tracheomalacia, tracheo-oesophageal or "
                   "tracheo-innominate fistula, persistent stoma and "
                   "unsightly scar.")],
          side_box={"title": "The bedside four",
                    "lines": ["Every tracheostomy patient must have at the "
                              "bedside:",
                              "**1.** A spare tube of the **same size**.",
                              "**2.** A spare tube **one size smaller**.",
                              "**3.** A **tracheal dilator**.",
                              "**4.** Working **suction**.",
                              "Plus the **stay sutures** left long. This "
                              "list is examined again and again."]},
          compare=CMP(
              ["", "Cuffed tube", "Uncuffed tube", "Fenestrated tube"],
              [["Seals the airway", "Yes", "No", "Partially"],
               ["Allows positive-pressure ventilation", "Yes",
                "Poorly", "No (unless the inner tube is non-fenestrated)"],
               ["Protects against aspiration", "Yes", "No", "No"],
               ["Permits speech", "No (unless deflated)", "Yes",
                "**Yes — air passes to the larynx**"],
               ["Typical use", "Ventilation, aspiration risk",
                "Children, long-term stable airway",
                "**Weaning and rehabilitation of voice**"]],
              cap="Table 8.1 — Types of tracheostomy tube"),
          points=[
              "The three defining instruments are the **Trousseau tracheal "
              "dilator, the tracheal hook and the checked range of tubes**.",
              "**Incision through the 2nd–4th tracheal rings** — state the "
              "level.",
              "**Tracheal stay sutures left long**, and why (early "
              "displacement).",
              "The **bedside four** — same-size tube, smaller tube, "
              "dilator, suction.",
              "**Close the skin loosely** to avoid surgical emphysema.",
              "Distinguish **cuffed / uncuffed / fenestrated** tubes and "
              "their indications.",
              "**Cricothyroidotomy is faster** in a true emergency — worth "
              "noting.",
              "Classify complications as **immediate, early and late**.",
          ],
          qa=[("List the contents of a tracheostomy tray.",
               "A minor tray plus the three defining items — a Trousseau or "
               "Laborde tracheal dilator, a sharp tracheal hook, and a full "
               "checked range of tracheostomy tubes (cuffed, uncuffed and "
               "fenestrated, with inner cannulae, obturators and "
               "connectors); exposure instruments — No.15 and No.10 blades, "
               "Weitlaner and Langenbeck retractors, cricoid hook and "
               "thyroid retractor, fine Metzenbaum scissors and dissecting "
               "forceps, numerous fine mosquito and Crile forceps, Kocher "
               "clamps and adrenaline-containing local anaesthetic; needle "
               "holders with non-absorbable tracheal stay sutures, flange "
               "sutures and tapes with a keyhole dressing; and inseparable "
               "airway equipment — two working suction units, a spare tube "
               "of the same size and one smaller at the bedside, a bedside "
               "dilator, difficult-airway trolley, self-inflating bag with "
               "tracheostomy connector, humidification, cuff manometer, a "
               "cricothyroidotomy set and capnography."),
              ("What must be kept at the bedside of every new tracheostomy "
               "patient?",
               "A spare tracheostomy tube of the same size, a spare tube one "
               "size smaller, a tracheal dilator, and working suction — with "
               "the tracheal stay sutures left long and taped to the chest "
               "so the trachea can be reopened if the tube is displaced "
               "before the track has matured.")]),

        # ============================================================ 8.6
        T("8.6", "Antral Puncture Tray",
          aka="Antral lavage tray · proof puncture and sinus washout set",
          lead="**Antral puncture (proof puncture)** perforates the medial "
               "wall of the maxillary sinus through the **inferior "
               "meatus** of the nose, to aspirate and irrigate the antrum "
               "both diagnostically and therapeutically. It is one of the "
               "**smallest ENT trays** and is centred on a single "
               "instrument: the **Lichtwitz antral trocar and cannula**.",
          uses=["Diagnostic aspiration of maxillary sinus contents for "
                "culture ('proof puncture')",
                "Therapeutic lavage of chronic maxillary sinusitis "
                "unresponsive to medical treatment",
                "Drainage of an antral empyema",
                "Instillation of medication into the antrum",
                "Assessment before more definitive sinus surgery",
                "Largely superseded by FESS but retained where endoscopic "
                "facilities are unavailable"],
          plate=PL("Signature instruments",
                   [("nasal_speculum", "Nasal speculum"),
                    ("trocar", "Lichtwitz antral trocar and cannula"),
                    ("frazier", "Fine nasal suction"),
                    ("probe", "Antral probe")],
                   cap="Fig 8.6 — One puncture, one cannula, one lavage"),
          groups=[
              G("Base set", [
                  ("1", "Limited procedures tray", "very small set"),
              ]),
              G("The defining instruments", [
                  ("1", "**Lichtwitz antral trocar and cannula**",
                   "**signature item** — a sharp trocar within a cannula; "
                   "the trocar perforates the medial antral wall and is "
                   "withdrawn, leaving the cannula in the sinus"),
                  ("1", "Tilley-Lichtwitz antral trocar",
                   "alternative pattern"),
                  ("1", "**Higginson's rubber syringe or a 20 mL "
                   "Luer-lock syringe with a connector**",
                   "**signature item** — delivers the lavage fluid through "
                   "the cannula"),
                  ("—", "**Warm sterile normal saline for lavage**", ""),
                  ("1", "Antral cannula with a curved tip",
                   "reaches the antral floor"),
                  ("—", "Sterile specimen containers and culture bottles",
                   "**the first aspirate is sent for culture before "
                   "irrigation**"),
              ]),
              G("Nasal exposure", [
                  ("—", "Nasal specula, graded (Thudichum, Killian)", ""),
                  ("1", "Head-light or head-mirror", ""),
                  ("1", "Nasal endoscope",
                   "confirms the puncture site and drainage"),
                  ("2", "Bayonet dressing forceps (Tilley's)",
                   "placing and removing packs"),
                  ("—", "**Topical anaesthetic and decongestant — 4 % "
                   "lignocaine with adrenaline on ribbon gauze or "
                   "cotton applicators**",
                   "**applied to the inferior meatus and lateral wall "
                   "before puncture**"),
                  ("2", "Fine nasal suction tips (Frazier)", ""),
                  ("1", "Antral probe / sinus seeker", ""),
              ]),
              G("Accessory and safety", [
                  ("1", "**Kidney dish / receiver held under the nose and "
                   "mouth**",
                   "collects the returning lavage fluid and pus"),
                  ("—", "Gauze, cotton wool and a protective gown/apron",
                   "the lavage return can be forceful"),
                  ("—", "Nasal packing material",
                   "if bleeding follows the puncture"),
                  ("—", "Silver nitrate / cautery", ""),
                  ("—", "**Suction immediately available**",
                   "the patient must not aspirate pus — this is the key "
                   "hazard"),
                  ("—", "Antibiotics and antral instillation medication",
                   ""),
                  ("—", "Radiographs / CT of the sinuses on display",
                   "confirms the side and the presence of an antrum"),
              ]),
          ],
          extras=[("Position", "**Sitting upright, head slightly forward, "
                   "leaning over a receiver** if performed under local "
                   "anaesthesia — so that pus and fluid drain out of the "
                   "nose and mouth rather than into the pharynx. If under "
                   "general anaesthesia, supine with the head turned and a "
                   "**cuffed endotracheal tube with a throat pack** to "
                   "protect the airway."),
                  ("Site of puncture",
                   "Through the **medial wall of the maxillary antrum at "
                   "the highest point of the inferior meatus, about "
                   "1–1.5 cm behind the anterior end of the inferior "
                   "turbinate** — where the bone is thinnest. The trocar is "
                   "directed **upwards, outwards and backwards, aiming "
                   "towards the outer canthus of the eye on the same "
                   "side**."),
                  ("Contraindication",
                   "**Acute sinusitis with cellulitis** — puncture may "
                   "spread infection into the orbit or soft tissues. Also "
                   "avoided in children with an undeveloped antrum and in "
                   "bleeding disorders."),
                  ("Complications",
                   "Haemorrhage, **penetration of the orbit** (proptosis, "
                   "diplopia, orbital cellulitis), penetration of the "
                   "cheek soft tissues causing emphysema, **air embolism "
                   "if air is injected instead of fluid**, false passage, "
                   "and **aspiration of pus** into the airway.")],
          side_box={"title": "Never inject air",
                    "lines": ["The antrum is irrigated with **fluid, never "
                              "air**.",
                              "Injecting air risks **air embolism**, which "
                              "can be fatal.",
                              "Equally: **aspirate for culture before "
                              "irrigating**, or the diagnostic value of the "
                              "procedure is lost."]},
          points=[
              "The signature items are the **Lichtwitz antral trocar and "
              "cannula** with a **Higginson's syringe and warm saline**.",
              "Puncture is through the **inferior meatus**, at the "
              "**thinnest part of the medial antral wall**, directed "
              "**towards the outer canthus**.",
              "**Aspirate for culture first, then irrigate** — state the "
              "order.",
              "**Never inject air** (air embolism); irrigate with fluid "
              "only.",
              "**Sitting position leaning over a receiver** under local "
              "anaesthesia; **throat pack** under general anaesthesia — to "
              "prevent aspiration of pus.",
              "**Acute sinusitis with cellulitis is a contraindication**.",
              "Note that it has been **largely replaced by FESS** — showing "
              "current awareness earns credit.",
          ],
          qa=[("Describe the antral puncture tray and the technique.",
               "A limited tray plus a Lichtwitz (or Tilley-Lichtwitz) antral "
               "trocar and cannula, a Higginson's rubber or 20 mL Luer-lock "
               "syringe with connector, warm sterile saline, curved antral "
               "cannula and sterile specimen containers; graded nasal "
               "specula, head-light, nasal endoscope, bayonet dressing "
               "forceps, topical 4 % lignocaine with adrenaline, fine nasal "
               "suction and an antral probe; with a kidney dish receiver, "
               "packing material, cautery, immediately available suction and "
               "sinus imaging on display. Technique: decongest and "
               "anaesthetise the inferior meatus; introduce the trocar at "
               "the highest point of the inferior meatus about 1–1.5 cm "
               "behind the anterior end of the inferior turbinate, directed "
               "upwards, outwards and backwards toward the ipsilateral outer "
               "canthus; withdraw the trocar; **aspirate and send for "
               "culture**; then irrigate with warm saline, never air, "
               "collecting the return in a receiver."),
              ("Why must air never be injected during antral lavage?",
               "Because injected air can enter a breached vein in the antral "
               "wall and cause air embolism, which may be fatal. Irrigation "
               "is therefore always performed with warm sterile fluid.")]),
    ])
