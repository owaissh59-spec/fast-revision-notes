#!/usr/bin/env python3
"""Part VII -- Neurologic Procedures Trays."""
from schema import T, P, PL, DP, FIG, G, CMP

NEURO = P(
    "VII", "Neurologic Procedures Trays",
    "Craniotomy · Laminectomy",
    intro="Neurosurgical trays exist to solve one problem: **the nervous "
          "system does not regenerate and is enclosed in bone**. Every tray "
          "must therefore (a) remove bone safely without touching neural "
          "tissue, (b) achieve absolute haemostasis, since a small clot in "
          "a closed compartment is lethal, and (c) handle dura and nerve "
          "with instruments finer than those used anywhere else. **Bipolar "
          "diathermy, fine suction with a thumb vent, cottonoid patties and "
          "magnification** are constant features.",
    trays=[

        # ============================================================ 7.1
        T("7.1", "Craniotomy Tray",
          aka="Cranial tray · supratentorial craniotomy set",
          lead="**Craniotomy** raises a bone flap from the skull to expose "
               "the brain. The tray divides into four clear systems: "
               "**scalp and haemostasis**, **bone removal and flap "
               "elevation**, **dura and intradural work**, and **closure "
               "with flap replacement**. Its most distinctive items are the "
               "**Raney scalp clips**, the **perforator and craniotome**, "
               "and the **bipolar diathermy with cottonoid patties**.",
          uses=["Excision of an intracranial tumour — meningioma, glioma, "
                "metastasis",
                "Evacuation of an extradural, subdural or intracerebral "
                "haematoma",
                "Clipping of an intracranial aneurysm; excision of an AVM",
                "Decompressive craniectomy for refractory raised "
                "intracranial pressure",
                "Repair of a depressed skull fracture or dural tear",
                "Epilepsy surgery and functional neurosurgery",
                "Drainage of a cerebral abscess"],
          plate=PL("Signature instruments",
                   [("hudson_brace", "Hudson brace with perforator"),
                    ("kerrison", "Kerrison rongeur"),
                    ("periosteal", "Periosteal / dural elevator"),
                    ("frazier", "Frazier suction with thumb vent"),
                    ("cerebellar", "Self-retaining cerebellar retractor"),
                    ("rongeur", "Bone rongeur")],
                   cap="Fig 7.1 — Scalp, bone, dura, brain — four systems"),
          groups=[
              G("Base set", [
                  ("1", "Basic / minor procedures tray",
                   "scalp incision and closure"),
                  ("1", "Major procedures tray items as required", ""),
              ]),
              G("Scalp incision and haemostasis", [
                  ("1", "Knife handle No.3 with No.10 / No.15 blades", ""),
                  ("—", "**Raney scalp clips with applier**",
                   "**signature item** — plastic clips applied along the cut "
                   "scalp edge; the galea bleeds profusely and clips give "
                   "instant haemostasis"),
                  ("6", "Dandy / Kocher scalp clamps",
                   "alternative to Raney clips"),
                  ("2", "**Fish-hooks with elastic bands (or Gelpi "
                   "retractors)**", "retract the scalp flap"),
                  ("2", "Periosteal elevator (Adson / Langenbeck)",
                   "raises the pericranium"),
                  ("2", "Small self-retaining (Weitlaner / mastoid) "
                   "retractor", ""),
                  ("8", "Fine mosquito and Crile forceps", ""),
                  ("—", "Local anaesthetic with adrenaline",
                   "infiltrated for scalp haemostasis"),
              ]),
              G("Bone removal and flap elevation", [
                  ("1", "**Hudson brace with perforator and burrs**",
                   "**signature item** — hand drill making the burr holes"),
                  ("1", "**Power craniotome with dura guard (footplate) "
                   "attachment**",
                   "**signature item** — cuts between burr holes while the "
                   "footplate protects the dura beneath"),
                  ("1", "Power drill with burrs, cutting and diamond", ""),
                  ("1", "Gigli saw with guide and handles",
                   "manual alternative for connecting burr holes"),
                  ("2", "**Kerrison rongeurs, up-biting, assorted**",
                   "**signature item** — footplate slides under the bone "
                   "edge and bites upward, away from the dura"),
                  ("2", "Bone rongeurs (Leksell, Adson)",
                   "nibbles the bone edge"),
                  ("2", "**Penfield / Adson dural elevator (dissector)**",
                   "**signature item** — separates dura from the inner "
                   "table before the flap is lifted"),
                  ("1", "Bone flap elevator / osteotome", ""),
                  ("—", "**Bone wax**", "diploic (bone-edge) bleeding"),
                  ("1", "Bone dust collector / graft container",
                   "bone dust used to fill burr holes"),
                  ("1", "Rasp and bone curette", ""),
              ]),
              G("Dura and intradural instruments", [
                  ("2", "**Dural hooks**",
                   "lift the dura away from the brain before it is incised"),
                  ("1", "**Dural (Beaver) knife with No.11 or dural "
                   "blade**", "the dural incision"),
                  ("2", "**Dural scissors (Metzenbaum, fine)**", ""),
                  ("4", "Dural clips / dura forceps",
                   "haemostasis of the dural edge"),
                  ("—", "Dural stay sutures 4-0",
                   "tack the dura back and out of the field"),
                  ("2", "**Brain (Cushing) retractors and malleable brain "
                   "spatulas**",
                   "**signature item** — broad, thin, atraumatic blades "
                   "gently displacing brain"),
                  ("1", "Self-retaining brain retractor system (Leyla, "
                   "Greenberg) with a flexible arm", ""),
                  ("2", "Cerebellar self-retaining retractor",
                   "posterior fossa"),
                  ("2", "Micro-dissectors, blunt and sharp (Rhoton set)",
                   "microsurgical dissection"),
                  ("2", "Nerve hooks, fine", ""),
                  ("2", "Fine tumour / pituitary forceps",
                   "removes tumour piecemeal"),
                  ("2", "Brain biopsy needle / cannula", ""),
                  ("1", "Ventricular cannula / catheter with a brain needle",
                   "CSF drainage and ventriculostomy"),
                  ("—", "**Aneurysm clips with appliers, full range**",
                   "if an aneurysm is planned; temporary and permanent "
                   "clips"),
                  ("1", "**Ultrasonic aspirator (CUSA)**",
                   "tumour debulking"),
                  ("1", "Operating microscope with sterile drapes",
                   "**essential** for microsurgery"),
              ]),
              G("Haemostasis — the neurosurgical priority", [
                  ("1", "**Bipolar diathermy with fine forceps tips and "
                   "irrigation**",
                   "**signature requirement** — current passes only between "
                   "the two tips, sparing adjacent brain; monopolar is "
                   "never used on neural tissue"),
                  ("—", "**Cottonoid patties (with radio-opaque strings)**",
                   "**signature item** — small cotton squares for gentle "
                   "pressure haemostasis and brain protection; **the "
                   "strings make them countable and traceable**"),
                  ("—", "Haemostatic agents — oxidised cellulose (Surgicel), "
                   "gelatin sponge (Gelfoam), fibrin sealant, thrombin", ""),
                  ("1", "**Frazier suction tips, fine, several sizes, with "
                   "thumb vent**",
                   "**signature item** — the vent lets the operator control "
                   "suction force with a fingertip, so brain is not drawn "
                   "into the tip"),
                  ("—", "Warm saline irrigation with bulb syringe", ""),
                  ("—", "Cross-matched blood available", ""),
              ]),
              G("Closure", [
                  ("—", "Dural closure suture 4-0 non-absorbable, or a "
                   "dural graft / substitute",
                   "watertight closure prevents CSF leak"),
                  ("—", "**Cranial fixation plates, burr-hole covers, "
                   "screws, or titanium wires**",
                   "replaces and secures the bone flap"),
                  ("1", "Screwdriver and plate bender", ""),
                  ("—", "Absorbable suture to pericranium, galea and "
                   "muscle", ""),
                  ("—", "Skin staples or non-absorbable suture", ""),
                  ("—", "Subgaleal / epidural drain",
                   "**used with caution** — sudden decompression is "
                   "hazardous"),
                  ("—", "Head bandage", ""),
                  ("—", "**Intracranial pressure monitor**", "where "
                   "indicated"),
              ]),
          ],
          extras=[("Position", "Supine with the head turned, lateral, prone "
                   "or sitting depending on the lesion; the head is fixed "
                   "in a **Mayfield three-pin skull clamp** (or on a "
                   "horseshoe headrest) to give absolute immobility. "
                   "**Head elevated above the heart** to aid venous "
                   "drainage and reduce intracranial pressure."),
                  ("Neuro-anaesthetic measures",
                   "Mannitol or hypertonic saline, controlled "
                   "hyperventilation, steroids for oedema, "
                   "anticonvulsants, and avoidance of hypertension and "
                   "coughing at extubation."),
                  ("Neuronavigation and monitoring",
                   "Image-guided stereotactic navigation, intra-operative "
                   "ultrasound, cortical mapping and evoked-potential "
                   "monitoring may all be required — they are part of the "
                   "set-up."),
                  ("Complications",
                   "Haematoma and re-bleeding, cerebral oedema, seizures, "
                   "CSF leak, meningitis, focal neurological deficit, "
                   "venous air embolism (sitting position) and tension "
                   "pneumocephalus.")],
          side_box={"title": "Three things that make it neurosurgery",
                    "lines": ["**Bipolar** diathermy — no current spread to "
                              "brain.",
                              "**Cottonoid patties on strings** — gentle, "
                              "countable haemostasis.",
                              "**Frazier suction with a thumb vent** — the "
                              "operator, not the wall vacuum, controls the "
                              "force.",
                              "Name these three and you have shown you "
                              "understand the speciality."]},
          points=[
              "Answer in **four systems**: scalp/haemostasis, bone "
              "removal, dura/intradural, closure.",
              "**Raney scalp clips** for galeal bleeding; **fish-hooks with "
              "elastic** for flap retraction.",
              "**Perforator/Hudson brace + craniotome with dura guard** — "
              "explain that the footplate protects the dura.",
              "**Kerrison rongeur bites upward, away from the dura** — say "
              "why.",
              "**Bipolar diathermy, cottonoid patties, Frazier vented "
              "suction** are the three haemostatic signatures.",
              "**Mayfield three-pin skull clamp** and **head above heart** "
              "for positioning.",
              "**Bone wax** for diploic bleeding; **cranial plates/wires** "
              "to replace the flap.",
              "**Watertight dural closure** prevents CSF leak.",
          ],
          pitfalls=["Suggesting monopolar diathermy on neural tissue.",
                    "Forgetting that cottonoid patties are counted items.",
                    "Omitting bone wax and flap fixation.",
                    "Not mentioning the skull clamp or head positioning."],
          qa=[("Describe the craniotomy tray.",
               "**Scalp and haemostasis**: No.10/15 blades, Raney scalp "
               "clips with applier, Dandy clamps, fish-hooks with elastic "
               "bands, periosteal elevators, self-retaining retractors, fine "
               "haemostats and adrenaline infiltration. **Bone**: Hudson "
               "brace with perforator and burrs, power craniotome with dura "
               "guard, power drill and burrs, Gigli saw, up-biting Kerrison "
               "rongeurs, Leksell rongeurs, Penfield/Adson dural elevators, "
               "flap elevator, bone wax and a bone-dust collector. **Dura "
               "and brain**: dural hooks, dural knife and scissors, dural "
               "clips and stay sutures, Cushing brain retractors and "
               "malleable spatulas, a self-retaining brain retractor system, "
               "Rhoton micro-dissectors, nerve hooks, tumour forceps, "
               "ventricular cannula, aneurysm clips with appliers, ultrasonic "
               "aspirator and the operating microscope. **Haemostasis**: "
               "bipolar diathermy with irrigation, cottonoid patties on "
               "radio-opaque strings, oxidised cellulose and gelatin sponge, "
               "fine vented Frazier suction tips and warm irrigation. "
               "**Closure**: dural suture or graft, cranial plates, "
               "burr-hole covers, screws or wires, layered absorbable "
               "suture, skin staples, a cautious drain and a head bandage. "
               "With a Mayfield skull clamp and neuronavigation."),
              ("Why is bipolar rather than monopolar diathermy used in "
               "neurosurgery?",
               "In bipolar diathermy the current passes only between the two "
               "tips of the forceps, so heating is confined to the tissue "
               "grasped. Monopolar current spreads through surrounding "
               "tissue to a distant return electrode and would cause "
               "thermal injury to adjacent brain, which cannot "
               "regenerate.")]),

        # ============================================================ 7.2
        T("7.2", "Laminectomy Tray",
          aka="Spinal tray · discectomy and spinal decompression set",
          lead="**Laminectomy** removes the vertebral lamina to decompress "
               "the spinal cord or nerve roots. The operative field is a "
               "**narrow, deep bony corridor** in which the cord and roots "
               "lie immediately beneath the bone being removed. The tray "
               "therefore centres on **up-biting Kerrison rongeurs**, "
               "**nerve-root retractors**, **disc instruments** and "
               "**bipolar haemostasis** — with fusion instrumentation added "
               "if the spine is to be stabilised.",
          uses=["Lumbar disc prolapse — discectomy or microdiscectomy",
                "Lumbar canal stenosis — decompressive laminectomy",
                "Cervical myelopathy — laminectomy or laminoplasty",
                "Excision of a spinal or intradural tumour",
                "Drainage of a spinal epidural abscess or haematoma",
                "Spinal trauma with cord compression",
                "Spinal fusion and instrumentation for instability or "
                "deformity"],
          plate=PL("Signature instruments",
                   [("kerrison", "Kerrison rongeur, up-biting"),
                    ("rongeur", "Laminectomy rongeur"),
                    ("bone_curette", "Angled bone curette"),
                    ("periosteal", "Cobb periosteal elevator"),
                    ("cerebellar", "Self-retaining spinal retractor"),
                    ("frazier", "Fine vented suction")],
                   cap="Fig 7.2 — Remove bone upward, away from the cord"),
          groups=[
              G("Base set", [
                  ("1", "Basic orthopaedic procedures tray",
                   "see 6.1 — bone instruments"),
                  ("1", "Major / minor procedures tray",
                   "soft-tissue exposure and closure"),
              ]),
              G("Exposure of the spine", [
                  ("1", "Knife handle with No.10 blade",
                   "midline incision over the spinous processes"),
                  ("2", "**Cobb periosteal elevators (curved and "
                   "straight)**",
                   "**signature item** — strips paraspinal muscle "
                   "subperiosteally off the lamina"),
                  ("2", "**Self-retaining spinal retractors (Taylor, "
                   "Beckman, Meyerding, Gelpi)**",
                   "**signature item** — holds the deep paraspinal muscle "
                   "apart"),
                  ("2", "Tubular retractor system / muscle dilators",
                   "minimally invasive approach"),
                  ("2", "Deep Langenbeck and Deaver retractors", ""),
                  ("2", "Bone rongeur (Leksell)",
                   "removes the spinous process"),
                  ("1", "Head-light or microscope",
                   "**illumination of a deep narrow corridor is essential**"),
                  ("—", "**Radiographic marker and image intensifier**",
                   "**confirms the correct spinal level — wrong-level "
                   "surgery is a serious never-event**"),
              ]),
              G("Bone removal — decompression", [
                  ("4", "**Kerrison rongeurs, up-biting, 2/3/4/5 mm, "
                   "various angles**",
                   "**signature item** — the footplate slides between bone "
                   "and dura and bites **upward**, so the cutting action is "
                   "always away from neural tissue"),
                  ("2", "Laminectomy / duckbill rongeur", ""),
                  ("4", "Bone curettes, angled and reverse-angled",
                   "removes ligament and cancellous bone"),
                  ("1", "High-speed drill with fine burrs and a guard",
                   "thins the lamina before rongeur removal"),
                  ("2", "Osteotomes and chisels, fine", ""),
                  ("1", "Mallet, small", ""),
                  ("2", "Ligamentum flavum elevator / dissector",
                   "separates ligament from dura"),
                  ("—", "**Bone wax**",
                   "epidural venous and cancellous bone bleeding"),
                  ("1", "Bone graft collector",
                   "local bone saved for fusion"),
              ]),
              G("Neural and disc instruments", [
                  ("2", "**Nerve-root retractors (Love, Scoville)**",
                   "**signature item** — gently displaces and protects the "
                   "root while the disc is removed"),
                  ("2", "**Dural / nerve-root hooks and Penfield "
                   "dissectors**",
                   "frees dura and root from adhesions"),
                  ("2", "**Pituitary rongeurs, straight and up-angled**",
                   "**signature item** — the instrument used to remove disc "
                   "material"),
                  ("2", "**Disc (Cushing) rongeurs and disc forceps**", ""),
                  ("2", "Ring curettes / disc curettes, angled",
                   "clears the disc space"),
                  ("1", "Annulotomy knife / No.11 blade on a long handle",
                   "incises the annulus"),
                  ("2", "Micro-dissectors and micro-curettes", ""),
                  ("2", "Nerve hook, blunt, fine", ""),
                  ("1", "Epidural probe / Woodson elevator", ""),
                  ("1", "Operating microscope or loupes",
                   "microdiscectomy"),
              ]),
              G("Haemostasis", [
                  ("1", "**Bipolar diathermy with fine tips**",
                   "**never monopolar near the dura or root**"),
                  ("—", "**Cottonoid patties on radio-opaque strings**",
                   "gentle pressure and neural protection; **counted**"),
                  ("—", "Haemostatic agents — oxidised cellulose, gelatin "
                   "sponge, thrombin",
                   "epidural venous plexus bleeding"),
                  ("1", "**Frazier suction tips, fine, with thumb vent**",
                   "controlled suction near the dura"),
                  ("—", "Warm saline irrigation", ""),
                  ("—", "Cross-matched blood available", ""),
              ]),
              G("Fusion and instrumentation (if performed)", [
                  ("—", "**Pedicle screws, rods, connectors and locking "
                   "caps**", "with the manufacturer's instrument set"),
                  ("1", "Pedicle awl, probe, sounder and tap", ""),
                  ("1", "Screwdriver, rod bender, rod holder, persuader and "
                   "counter-torque", ""),
                  ("—", "**Interbody cages (PLIF / TLIF) with inserters and "
                   "trials**", ""),
                  ("—", "Bone graft — local autograft, iliac crest, "
                   "allograft or substitute", ""),
                  ("1", "Cage / graft impactor and distractor", ""),
                  ("—", "**Neuromonitoring — evoked potentials and EMG**",
                   "detects impending cord or root injury during "
                   "instrumentation"),
                  ("1", "Image intensifier / navigation",
                   "screw placement"),
              ]),
              G("Closure", [
                  ("—", "Dural repair suture 5-0/6-0 and dural sealant",
                   "if the dura is breached — prevents CSF leak"),
                  ("—", "Fat or fascial graft", "dural patch"),
                  ("—", "Absorbable suture to fascia and muscle",
                   "**meticulous fascial closure**"),
                  ("—", "Subcutaneous suture and skin staples/suture", ""),
                  ("—", "Closed suction drain", "deep to the fascia"),
                  ("—", "Specimen containers",
                   "disc material, bone and tissue for histology and "
                   "culture"),
              ]),
          ],
          extras=[("Position", "**Prone** on a spinal frame or bolsters "
                   "(Wilson frame, Montreal mattress), with the abdomen "
                   "free to reduce epidural venous engorgement; or the "
                   "**knee-chest / kneeling** position. The **eyes, face, "
                   "breasts, genitalia and bony prominences must be "
                   "protected and checked**, and the arms positioned to "
                   "avoid brachial plexus traction."),
                  ("Level confirmation",
                   "**The spinal level must be confirmed radiologically "
                   "before bone is removed.** Operating at the wrong level "
                   "is a recognised never-event; a marker needle and image "
                   "intensifier are used."),
                  ("Complications",
                   "Dural tear with CSF leak, nerve-root or cord injury, "
                   "epidural haematoma causing acute compression, "
                   "discitis and wound infection, recurrent disc "
                   "prolapse, instability requiring fusion, vascular injury "
                   "anterior to the disc, and **wrong-level surgery**."),
                  ("Prone-position hazards",
                   "Post-operative visual loss from ocular pressure, "
                   "pressure necrosis, brachial plexus injury and "
                   "venous air embolism.")],
          side_box={"title": "Why up-biting?",
                    "lines": ["The **Kerrison rongeur** has a thin "
                              "**footplate** that slides between the bone "
                              "and the dura.",
                              "Its blade then bites **upward** — the "
                              "cutting force is directed **away from the "
                              "cord and root**.",
                              "This is why it is the defining instrument of "
                              "spinal decompression."]},
          compare=CMP(
              ["Feature", "Craniotomy tray", "Laminectomy tray"],
              [["Bone opened", "Skull — flap raised and replaced",
                "Lamina — removed, usually not replaced"],
               ["Key bone instrument",
                "Perforator + craniotome with dura guard",
                "**Up-biting Kerrison rongeur**"],
               ["Key retractor",
                "Cushing brain retractor / malleable spatula",
                "**Nerve-root retractor (Love, Scoville)**"],
               ["Tissue-removal instrument", "Tumour forceps, CUSA",
                "**Pituitary and disc rongeurs**"],
               ["Position", "Supine/lateral/prone/sitting, Mayfield clamp",
                "**Prone on a spinal frame**"],
               ["Shared essentials",
                "Bipolar, cottonoids, vented Frazier suction, bone wax, "
                "microscope",
                "Bipolar, cottonoids, vented Frazier suction, bone wax, "
                "microscope"]],
              cap="Table 7.1 — The two neurosurgical trays compared"),
          points=[
              "The **up-biting Kerrison rongeur** is the single most "
              "important instrument — explain the footplate and the upward "
              "bite.",
              "**Cobb elevators** strip muscle; **Taylor/Beckman "
              "self-retaining retractors** hold the exposure.",
              "**Nerve-root retractor (Love/Scoville)** and **pituitary "
              "rongeur** are the neural and disc signatures.",
              "**Confirm the spinal level radiologically** — wrong-level "
              "surgery is a never-event and a guaranteed discussion point.",
              "**Prone positioning with the abdomen free** reduces epidural "
              "venous bleeding; list the prone-position hazards.",
              "**Bipolar, cottonoids and vented Frazier suction** are "
              "shared with the craniotomy tray.",
              "If fusion is planned, add **pedicle screws and rods with "
              "neuromonitoring**.",
          ],
          qa=[("Describe the laminectomy tray.",
               "A basic orthopaedic and minor/major tray plus: **exposure** "
               "— No.10 blade, straight and curved Cobb periosteal "
               "elevators, Taylor/Beckman/Meyerding self-retaining spinal "
               "retractors, tubular retractors, deep hand-held retractors, "
               "Leksell rongeur, head-light or microscope and an image "
               "intensifier with a marker for level confirmation; **bone "
               "removal** — up-biting Kerrison rongeurs 2–5 mm in several "
               "angles, laminectomy rongeurs, angled and reverse-angled "
               "curettes, high-speed drill with guarded burrs, fine "
               "osteotomes, ligamentum flavum elevators, bone wax and a "
               "graft collector; **neural and disc** — Love and Scoville "
               "nerve-root retractors, dural and root hooks, Penfield "
               "dissectors, straight and up-angled pituitary rongeurs, disc "
               "rongeurs and forceps, ring curettes, annulotomy knife and "
               "micro-instruments; **haemostasis** — bipolar diathermy, "
               "cottonoid patties on radio-opaque strings, oxidised "
               "cellulose and gelatin sponge, fine vented Frazier suction "
               "and warm irrigation; **fusion if required** — pedicle screws, "
               "rods and connectors with awl, probe, tap, screwdriver, rod "
               "bender, interbody cages and graft, with neuromonitoring; and "
               "**closure** — fine dural suture and sealant, layered "
               "absorbable closure, drain and specimen containers."),
              ("Why is the Kerrison rongeur the characteristic instrument of "
               "spinal decompression?",
               "Its thin footplate can be slid into the epidural space "
               "between the bone and the dura, and its blade then cuts "
               "upward against the footplate. The cutting force is therefore "
               "always directed away from the spinal cord and nerve roots, "
               "allowing bone and ligament to be removed piecemeal in "
               "safety.")]),
    ])
