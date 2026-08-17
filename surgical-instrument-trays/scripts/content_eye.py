#!/usr/bin/env python3
"""Part IX -- Ophthalmic Trays."""
from schema import T, P, PL, DP, FIG, G, CMP

_TRAYS = []

EYE = P(
    "IX", "Ophthalmic Trays",
    "Basic eye · Eyelid and conjunctiva · Eye muscle · "
    "Dacryocystorhinostomy · Cornea · Cataract and lens · Glaucoma · "
    "Microscope · Retina",
    intro="Ophthalmic trays are the finest in surgery. Three rules govern "
          "every one of them. **First, scale**: the instruments are "
          "measured in millimetres, so almost all work is done under an "
          "**operating microscope** with **7-0 to 11-0 suture**. "
          "**Second, fragility**: tips are so delicate that they are "
          "individually protected in silicone guards and racked, never "
          "piled. **Third, the eye is a closed pressurised globe**: "
          "intraocular pressure must be controlled, the anterior chamber "
          "maintained with viscoelastic, and any full-thickness wound made "
          "watertight.",
    trays=_TRAYS)



# ================================================================ 9.1
_TRAYS.append(T(
    "9.1", "Basic Eye Procedures Tray",
    aka="Basic ophthalmic tray · general eye set",
    lead="The **basic eye tray** is the reference ophthalmic set from which "
         "all the other trays in this Part are built. It provides the "
         "minimum needed to expose the globe, hold the lids apart, grasp "
         "conjunctiva and sclera atraumatically, cut with fine scissors and "
         "suture with microsurgical needle holders. Every instrument is "
         "**short (about 10 cm), fine-tipped and spring-handled**, because "
         "the operator's hand rests on the patient's forehead and works "
         "through a few millimetres of movement.",
    uses=["Examination and minor procedures under anaesthesia",
          "Conjunctival and corneal foreign-body removal",
          "Repair of a conjunctival laceration",
          "Pterygium excision; conjunctival biopsy or graft",
          "Base tray for every other ophthalmic procedure in this Part",
          "Enucleation and evisceration (with additional items)"],
    plate=PL("Signature instruments",
             [("lid_speculum", "Wire lid speculum (Barraquer)"),
              ("fine_forceps", "Fine conjunctival forceps"),
              ("iris_scissors", "Fine spring scissors"),
              ("castroviejo_nh", "Castroviejo needle holder"),
              ("strabismus_hook", "Blunt muscle hook")],
             cap="Fig 9.1 — Short, fine, spring-handled instruments"),
    groups=[
        G("Exposure of the globe", [
            ("1", "**Lid (eyelid) speculum — Barraquer wire or "
                  "Lieberman/Kratz adjustable**",
             "**signature item** — holds both lids apart and keeps lashes "
             "out of the field"),
            ("2", "Desmarres lid retractors, assorted",
             "everts and retracts a lid"),
            ("2", "Lid plate / Jaeger lid plate",
             "supports the lid from behind while it is incised"),
            ("2", "**Blunt muscle hooks (Graefe / von Graefe)**",
             "engages and lifts a rectus muscle or the globe"),
            ("—", "**Traction (bridle) suture, 4-0 silk**",
             "rotates and steadies the globe"),
            ("1", "Eye drape with an adhesive aperture", ""),
        ]),
        G("Grasping — all atraumatic and fine", [
            ("2", "**Conjunctival forceps, fine toothed (0.12 mm) — "
                  "Castroviejo, Bishop-Harmon**",
             "**signature item** — the '0.12' teeth are just visible to the "
             "naked eye"),
            ("2", "Fixation forceps (Elschnig, Lester)",
             "grips the limbus to rotate the globe"),
            ("2", "Tying (non-toothed) forceps",
             "handles 8-0 to 10-0 suture without cutting it"),
            ("2", "Suture-tying platform forceps",
             "the flat platform allows a knot to be tied on it"),
            ("2", "Serrefine / bulldog clip",
             "holds a traction suture"),
        ]),
        G("Cutting", [
            ("1", "Knife handle for micro-blades; **No.15 blade**", ""),
            ("2", "**Beaver / micro-knife handle with No.64, 65, 69 "
                  "blades**",
             "**signature item** — tiny replaceable blades for corneal and "
             "scleral incisions"),
            ("2", "**Westcott spring scissors, curved and blunt-tipped**",
             "**signature item** — the standard conjunctival scissors"),
            ("2", "Vannas scissors, straight and curved",
             "very fine capsulotomy and iris work"),
            ("2", "Iris / tenotomy scissors, fine", ""),
            ("1", "Stevens tenotomy scissors", "blunt dissection"),
            ("1", "Suture scissors", "never used on tissue"),
        ]),
        G("Suturing", [
            ("2", "**Castroviejo or Barraquer needle holder, fine, curved, "
                  "with or without a lock**",
             "**signature item** — spring-handled, holds 8-0 to 10-0 "
             "needles"),
            ("—", "**Suture: 6-0 to 8-0 absorbable (Vicryl) for "
                  "conjunctiva; 9-0 to 10-0 nylon for cornea and sclera; "
                  "4-0 silk for traction**", ""),
            ("2", "Tying forceps and a suture platform", ""),
        ]),
        G("Cautery, irrigation and accessory", [
            ("1", "**Bipolar / wet-field cautery with fine tips**",
             "**bipolar only** — monopolar current is never used near the "
             "globe"),
            ("1", "Disposable low-temperature cautery pen", ""),
            ("2", "**Irrigating cannulae (Rycroft, anterior chamber) with "
                  "syringes**", "balanced salt solution (BSS)"),
            ("—", "**Balanced salt solution**",
             "**never plain saline inside the eye** — BSS is "
             "iso-osmotic and endothelium-friendly"),
            ("1", "Fine suction / sponge (cellulose spear) holder", ""),
            ("—", "Cellulose sponge spears (Weck-cel)",
             "the ophthalmic equivalent of a swab; **counted**"),
            ("1", "Calliper / measuring gauge",
             "measures a lesion or an incision"),
            ("1", "Eye speculum tray / instrument rack with silicone tip "
                  "guards",
             "**instruments are racked, never piled**"),
            ("—", "Mydriatics, miotics, topical anaesthetic and antibiotic",
             "labelled and checked — **wrong-drug errors are a recognised "
             "ophthalmic hazard**"),
            ("—", "Eye pad, cartella shield and tape", ""),
        ]),
    ],
    extras=[("Position", "Supine with the head stabilised on a ring or "
             "horseshoe headrest and the **face horizontal** — the plane of "
             "the iris parallel to the floor — so the microscope looks "
             "straight into the eye. The surgeon usually sits at the head "
             "or temporal side."),
            ("Marking the correct eye",
             "**The operative eye is marked and confirmed at the WHO "
             "checklist.** Wrong-eye surgery is a never-event."),
            ("Instrument care",
             "Ophthalmic instruments are cleaned by hand or in a dedicated "
             "cycle, **never with general instruments**, dried "
             "immediately, and stored in racks with **silicone tip "
             "guards**. Ultrasonic cleaning is avoided for cemented "
             "diamond knives.")],
    side_box={"title": "Never inside the eye",
              "lines": ["**Plain normal saline** — use **balanced salt "
                        "solution**.",
                        "**Monopolar diathermy** — use **bipolar/wet-field** "
                        "cautery.",
                        "**Talc-dusted gloves or lint** — causes a "
                        "granulomatous reaction.",
                        "**Any instrument with a burred or non-apposing "
                        "tip.**"]},
    points=[
        "Describe the tray as **short, fine, spring-handled instruments "
        "used under the microscope with 7-0 to 11-0 suture**.",
        "Name the **lid speculum, 0.12 mm toothed forceps, Westcott "
        "scissors, Castroviejo needle holder and Beaver micro-blades** — "
        "the five basic signatures.",
        "**Balanced salt solution, not saline**, and **bipolar, not "
        "monopolar** — two reliable safety marks.",
        "**Cellulose sponge spears are counted items**.",
        "**Tip guards and racking** — instrument care is examinable in "
        "ophthalmology more than any other speciality.",
        "**Marking the operative eye** and the WHO checklist.",
    ],
    qa=[("List the contents of a basic eye procedures tray.",
         "Exposure — Barraquer wire or adjustable lid speculum, Desmarres "
         "lid retractors, Jaeger lid plate, blunt muscle hooks and a 4-0 "
         "silk traction suture; grasping — 0.12 mm toothed Castroviejo and "
         "Bishop-Harmon conjunctival forceps, fixation forceps, tying "
         "forceps and suture-tying platform forceps with serrefines; cutting "
         "— No.15 blade, Beaver handle with 64/65/69 micro-blades, curved "
         "blunt Westcott spring scissors, Vannas scissors, fine iris and "
         "Stevens tenotomy scissors and separate suture scissors; suturing — "
         "Castroviejo or Barraquer fine needle holders with 6-0 to 8-0 "
         "absorbable, 9-0 to 10-0 nylon and 4-0 silk; plus bipolar wet-field "
         "cautery, Rycroft irrigating cannulae with balanced salt solution, "
         "counted cellulose sponge spears, callipers, an instrument rack "
         "with silicone tip guards, labelled ophthalmic drugs and an eye "
         "pad with cartella shield."),
        ("Why is balanced salt solution used rather than normal saline "
         "inside the eye?",
         "Balanced salt solution is iso-osmotic and contains the "
         "electrolytes, bicarbonate and glucose needed to preserve the "
         "corneal endothelium and other intraocular tissues. Plain normal "
         "saline lacks these and causes endothelial cell loss and corneal "
         "oedema.")]))



# ================================================================ 9.2
_TRAYS.append(T(
    "9.2", "Eyelid and Conjunctival Procedures Tray",
    aka="Oculoplastic tray · lid surgery set",
    lead="The eyelid is a **thin multilayered structure** — skin, orbicularis "
         "muscle, tarsal plate and conjunctiva — whose margin must be "
         "restored to within a fraction of a millimetre or the patient is "
         "left with notching, trichiasis or a corneal abrasion. This tray "
         "is a basic eye tray plus **lid-specific clamps, plates and "
         "markers**, and the instruments needed to protect the globe while "
         "the lid is operated upon.",
    uses=["Chalazion and hordeolum — incision and curettage",
          "Entropion and ectropion correction",
          "Ptosis correction — levator resection or advancement",
          "Excision of a lid tumour with reconstruction; wedge excision",
          "Repair of a lid laceration, including canalicular involvement",
          "Pterygium excision with conjunctival autograft",
          "Blepharoplasty; tarsorrhaphy; epilation for trichiasis"],
    plate=PL("Signature instruments",
             [("chalazion_clamp", "Chalazion clamp"),
              ("ear_curette", "Chalazion (Meyhoefer) curette"),
              ("fine_forceps", "Fine toothed forceps"),
              ("iris_scissors", "Westcott / fine scissors"),
              ("castroviejo_nh", "Fine needle holder")],
             cap="Fig 9.2 — Clamp, evert, curette, reconstruct"),
    groups=[
        G("Base set", [
            ("1", "Basic eye procedures tray", "see 9.1"),
        ]),
        G("Lid-specific instruments", [
            ("2", "**Chalazion clamp (Desmarres)**",
             "**signature item** — one arm is an **open ring** placed over "
             "the lesion and the other a **solid plate** behind the lid; the "
             "thumb screw fixes and everts the lid and provides haemostasis"),
            ("2", "**Chalazion (Meyhoefer) curette, small and large**",
             "**signature item** — scoops out the granulomatous contents"),
            ("2", "**Lid plates (Jaeger)**",
             "**signature item** — supports the lid from behind and "
             "**protects the globe** while the lid is incised"),
            ("2", "**Desmarres lid retractors**, small, medium, large",
             "everts the lid to expose the tarsal conjunctiva"),
            ("2", "**Entropion / tarsal clamp (Snellen)**", ""),
            ("1", "Lid crease / skin marker (gentian violet) with "
                  "callipers",
             "**symmetry is measured and marked before any incision**"),
            ("1", "Ptosis clamp and Berke/Putterman clamp", ""),
            ("2", "Skin hooks, fine single and double", ""),
            ("2", "Tarsal plate forceps and Erhardt lid clamp", ""),
            ("1", "Lacrimal probes (Bowman), graded",
             "checks canalicular integrity in lid trauma"),
            ("1", "Punctum dilator", ""),
            ("1", "Epilation forceps", "trichiasis"),
        ]),
        G("Cutting and dissecting", [
            ("2", "Westcott spring scissors, curved and blunt", ""),
            ("2", "Stevens tenotomy scissors", "blunt tissue planes"),
            ("2", "Fine straight iris scissors", "lid margin"),
            ("1", "Beaver handle with No.64 / 15 micro-blades", ""),
            ("1", "Knife handle with No.15 blade", "skin incision"),
            ("1", "Superblade / crescent blade", ""),
            ("1", "Radiofrequency / fine bipolar needle",
             "cutting and haemostasis"),
        ]),
        G("Grafts and reconstruction", [
            ("1", "**Conjunctival autograft instruments**",
             "for pterygium — fine forceps, spring scissors and a graft "
             "spatula"),
            ("—", "**Fibrin glue** or 8-0 / 10-0 suture",
             "secures a conjunctival graft"),
            ("1", "Mucous membrane / buccal graft harvesting set",
             "posterior lamellar reconstruction"),
            ("1", "**Skin graft knife and template**",
             "full-thickness graft from the upper lid or postauricular skin"),
            ("—", "Tarsal / hard-palate / ear-cartilage graft material", ""),
            ("—", "Amniotic membrane", "ocular surface reconstruction"),
            ("1", "Graft flattening board and marker", ""),
        ]),
        G("Suture, haemostasis and accessory", [
            ("—", "**6-0 / 7-0 absorbable for tarsus and orbicularis; "
                  "6-0 silk or nylon for the lid margin; 8-0 for "
                  "conjunctiva**",
             "**lid-margin sutures are left long and taped away from the "
             "cornea** to prevent abrasion"),
            ("2", "Fine needle holders", ""),
            ("1", "Bipolar / wet-field cautery, fine-tipped", ""),
            ("—", "**Local anaesthetic with adrenaline and hyaluronidase**",
             "haemostasis and diffusion; **injected after marking**"),
            ("—", "Cellulose sponge spears, counted", ""),
            ("—", "Antibiotic ointment, eye pad and shield", ""),
            ("—", "Specimen containers, **orientated and labelled**",
             "**a lid tumour must be orientated for margin reporting**"),
            ("1", "Frozen-section facility",
             "margin control for malignancy"),
            ("—", "Corneal protective shield / lubricant",
             "**protects the cornea throughout lid surgery**"),
        ]),
    ],
    extras=[("Position", "Supine, head on a ring; the lid is usually "
             "operated with the eye closed or protected. Local anaesthesia "
             "with sedation is common; children need general anaesthesia."),
            ("Mark before you inject",
             "Local anaesthetic distorts the tissues, so **skin creases, "
             "excision margins and symmetry are marked before "
             "infiltration**."),
            ("Complications",
             "Lid notching and margin malposition, trichiasis with corneal "
             "abrasion, lagophthalmos and exposure keratopathy, "
             "over- or under-correction of ptosis, asymmetry, "
             "haematoma, and — with deep orbital injection — retrobulbar "
             "haemorrhage.")],
    side_box={"title": "The chalazion clamp",
              "lines": ["One arm is an **open ring**, the other a **solid "
                        "plate**.",
                        "The ring is centred over the lesion on the skin "
                        "side; the plate lies behind the lid.",
                        "Tightening the screw **everts the lid, fixes the "
                        "lesion in the ring and compresses the vessels** — "
                        "exposure and haemostasis in one instrument."]},
    points=[
        "The **chalazion clamp (open ring + solid plate) and Meyhoefer "
        "curette** are the signature pair; describe how the clamp works.",
        "The **Jaeger lid plate protects the globe** while the lid is "
        "incised — a favourite safety point.",
        "**Mark and measure before infiltrating** local anaesthetic.",
        "**Lid-margin sutures are left long and taped away from the "
        "cornea**.",
        "**Orientate and label a lid tumour specimen**; frozen section for "
        "margins.",
        "A **corneal protective shield** is used throughout.",
    ],
    qa=[("Describe the eyelid and conjunctival procedures tray.",
         "A basic eye tray plus lid-specific items: Desmarres chalazion "
         "clamp and Meyhoefer curettes, Jaeger lid plates, Desmarres lid "
         "retractors, Snellen entropion clamp, lid-crease marker with "
         "callipers, ptosis clamps, fine skin hooks, tarsal forceps, Bowman "
         "lacrimal probes with a punctum dilator and epilation forceps; "
         "cutting — Westcott and Stevens scissors, fine iris scissors, "
         "Beaver micro-blades, No.15 blade and fine bipolar needle; "
         "reconstruction — conjunctival autograft instruments with fibrin "
         "glue, mucous-membrane and skin-graft harvesting sets, tarsal and "
         "cartilage graft material and amniotic membrane; and suture and "
         "accessory — 6-0/7-0 absorbable, 6-0 silk for the margin left long, "
         "8-0 conjunctival suture, fine needle holders, wet-field cautery, "
         "local anaesthetic with adrenaline and hyaluronidase, counted "
         "sponge spears, orientated specimen containers, frozen section and "
         "a corneal protective shield."),
        ("How does a chalazion clamp work?",
         "It has two arms — an open ring and a solid plate — joined by a "
         "thumb screw. The ring is placed on the skin over the lesion and "
         "the plate behind the lid; tightening the screw everts the lid, "
         "immobilises the chalazion within the ring and compresses the "
         "surrounding vessels, giving simultaneous exposure and haemostasis "
         "for incision and curettage.")]))



# ================================================================ 9.3
_TRAYS.append(T(
    "9.3", "Basic Eye Muscle Procedures Tray",
    aka="Strabismus (squint) surgery tray · extraocular muscle set",
    lead="**Strabismus surgery** weakens or strengthens the extraocular "
         "muscles to realign the eyes — chiefly by **recession** (moving a "
         "muscle insertion backwards) or **resection** (shortening it). The "
         "tray is a basic eye tray plus instruments to **find, hold, "
         "measure and reattach a muscle**: hooks, a calliper and a "
         "muscle clamp. Precision is in **millimetres** — a 1 mm error "
         "changes the alignment measurably.",
    uses=["Horizontal strabismus — esotropia and exotropia",
          "Vertical strabismus and A- or V-pattern deviations",
          "Recession, resection, tucking and plication of a rectus muscle",
          "Weakening procedures on the inferior or superior oblique",
          "Adjustable-suture strabismus surgery",
          "Correction of nystagmus (Kestenbaum procedure) and abnormal head "
          "posture",
          "Botulinum toxin injection into an extraocular muscle"],
    plate=PL("Signature instruments",
             [("strabismus_hook", "Squint (muscle) hook"),
              ("fine_forceps", "Fine conjunctival forceps"),
              ("iris_scissors", "Westcott scissors"),
              ("castroviejo_nh", "Fine needle holder"),
              ("lid_speculum", "Lid speculum")],
             cap="Fig 9.3 — Find the muscle, hold it, measure, reattach"),
    groups=[
        G("Base set", [
            ("1", "Basic eye procedures tray", "see 9.1"),
        ]),
        G("Muscle hooks — the defining group", [
            ("2", "**Squint / muscle hook (von Graefe, Stevens), small and "
                  "large**",
             "**signature item** — a blunt bulb-tipped hook swept behind the "
             "muscle to engage and lift it out of the orbit"),
            ("2", "**Jameson muscle hook**",
             "has a **flange or heel** that prevents the muscle slipping "
             "off the hook"),
            ("1", "**Green muscle hook**",
             "broad flat blade — holds a muscle while it is sutured"),
            ("1", "**Desmarres / Guyton-Noyes muscle clamp**",
             "**signature item** — clamps the muscle to secure it before it "
             "is detached"),
            ("2", "Tenotomy (Stevens) hook, fine",
             "isolating the oblique muscles and check ligaments"),
            ("1", "Scleral depressor",
             "rotates the globe to expose a posterior insertion"),
        ]),
        G("Measuring — precision to the millimetre", [
            ("1", "**Castroviejo callipers with a locking screw**",
             "**signature item** — sets the exact number of millimetres of "
             "recession or resection"),
            ("1", "**Scleral marker / muscle marker**",
             "marks the sclera at the measured distance from the limbus"),
            ("1", "Steel ruler, millimetre scale", ""),
            ("1", "Limbal / corneal marker", ""),
            ("—", "**Written surgical plan with the measured deviation**",
             "**the number of millimetres is calculated pre-operatively "
             "from the prism-cover-test measurement**"),
        ]),
        G("Cutting and dissecting", [
            ("2", "Westcott spring scissors, curved and blunt",
             "conjunctival and muscle-capsule dissection"),
            ("2", "Fine straight scissors / tenotomy scissors",
             "dividing the muscle at its insertion"),
            ("2", "Vannas scissors", ""),
            ("1", "Beaver handle with No.64 / 65 micro-blades", ""),
            ("2", "Fine toothed (0.3 / 0.12 mm) forceps", ""),
            ("2", "Fixation (Elschnig) forceps",
             "rotates the globe against the pull of the hook"),
        ]),
        G("Suturing and reattachment", [
            ("2", "**Castroviejo / Barraquer needle holders, fine**", ""),
            ("—", "**6-0 polyglactin (Vicryl) double-armed with spatulated "
                  "needles**",
             "**signature requirement** — **spatulated** needles pass within "
             "the scleral lamellae without perforating the globe"),
            ("—", "6-0 / 7-0 absorbable for conjunctival closure", ""),
            ("—", "**Adjustable-suture materials — bow-tie or sliding "
                  "noose**",
             "allows post-operative adjustment of alignment in the "
             "conscious patient"),
            ("2", "Tying forceps and suture platform", ""),
            ("1", "Bipolar wet-field cautery, fine",
             "muscle edge haemostasis"),
        ]),
        G("Accessory and safety", [
            ("—", "**Forced duction / traction test performed and "
                  "recorded**", "assesses restriction before and after"),
            ("—", "Cellulose sponge spears, counted", ""),
            ("—", "Balanced salt solution and irrigating cannula", ""),
            ("—", "**Atropine / cycloplegic, antibiotic-steroid ointment**",
             ""),
            ("—", "**Oculocardiac reflex — atropine drawn up and the "
                  "anaesthetist forewarned**",
             "**traction on a rectus muscle causes bradycardia and can "
             "cause asystole**"),
            ("—", "Eye pad and shield", ""),
            ("—", "**Both eyes prepared and draped**",
             "surgery is frequently bilateral and the fellow eye is "
             "compared"),
        ]),
    ],
    extras=[("Position", "Supine, head on a ring, face horizontal; **both "
             "eyes prepared** because the procedure is often bilateral."),
            ("Approach", "Limbal (Von Noorden), fornix (Parks) or "
             "swinging-eyelid conjunctival incision; the muscle is hooked, "
             "cleared of check ligaments, secured with a double-armed "
             "suture, disinserted, and reattached at the measured "
             "distance."),
            ("The oculocardiac reflex",
             "Traction on the extraocular muscles — especially the medial "
             "rectus — triggers a **trigeminovagal reflex causing "
             "bradycardia, arrhythmia or even asystole**. Management: "
             "**stop the traction immediately**, ensure adequate "
             "ventilation and depth of anaesthesia, and give intravenous "
             "**atropine** if it persists."),
            ("Complications",
             "Over- or under-correction, **slipped or lost muscle**, "
             "**scleral perforation** with retinal injury or endophthalmitis, "
             "diplopia, conjunctival scarring and cyst, anterior segment "
             "ischaemia if several muscles are detached, and infection.")],
    side_box={"title": "Two things examiners always ask",
              "lines": ["**Spatulated needles** — flat in cross-section, so "
                        "they travel between scleral layers and do not "
                        "perforate the globe.",
                        "**Oculocardiac reflex** — muscle traction → "
                        "bradycardia/asystole; stop traction, then "
                        "atropine."]},
    points=[
        "Name the **muscle hooks (von Graefe, Jameson with a flange, Green "
        "flat)** and the **muscle clamp** — the defining group.",
        "**Castroviejo callipers and a scleral marker** — emphasise that "
        "measurement is in **millimetres from the limbus**.",
        "**6-0 Vicryl double-armed on spatulated needles** — and explain "
        "why spatulated.",
        "**Oculocardiac reflex**: state the mechanism and the management.",
        "**Adjustable sutures** allow post-operative fine tuning.",
        "**Both eyes prepared** — surgery is often bilateral.",
    ],
    qa=[("Describe the basic eye muscle procedures tray.",
         "A basic eye tray plus: muscle hooks — von Graefe/Stevens squint "
         "hooks in two sizes, a flanged Jameson hook, a flat Green hook, "
         "fine tenotomy hooks and a scleral depressor, with a "
         "Desmarres/Guyton-Noyes muscle clamp; measuring instruments — "
         "locking Castroviejo callipers, a scleral muscle marker, millimetre "
         "ruler and limbal marker, used with the pre-operative surgical "
         "plan; cutting — curved blunt Westcott scissors, fine straight and "
         "Vannas scissors, Beaver micro-blades, 0.12/0.3 mm toothed forceps "
         "and Elschnig fixation forceps; suturing — fine Castroviejo needle "
         "holders with double-armed 6-0 polyglactin on **spatulated** "
         "needles, conjunctival suture, adjustable-suture materials, tying "
         "forceps and fine wet-field cautery; plus counted sponge spears, "
         "balanced salt solution, cycloplegic and antibiotic ointment, "
         "**atropine drawn up for the oculocardiac reflex**, and both eyes "
         "prepared and draped."),
        ("What is the oculocardiac reflex and how is it managed?",
         "Traction on an extraocular muscle, particularly the medial rectus, "
         "stimulates a trigeminovagal reflex arc producing bradycardia, "
         "arrhythmia or even asystole. It is managed by immediately "
         "releasing the traction, confirming adequate ventilation and "
         "anaesthetic depth, and giving intravenous atropine if the "
         "bradycardia persists; the anaesthetist is forewarned and atropine "
         "is drawn up before surgery begins.")]))



# ================================================================ 9.4
_TRAYS.append(T(
    "9.4", "Dacryocystorhinostomy Tray",
    aka="DCR tray · dacryocystorhinostomy (DCR) set · lacrimal drainage "
        "surgery",
    lead="**Dacryocystorhinostomy** creates a direct opening between the "
         "**lacrimal sac and the nasal cavity**, bypassing an obstructed "
         "nasolacrimal duct. The tray is unique in this Part because it is "
         "**half ophthalmic and half nasal**: it needs fine lacrimal probes "
         "and eye instruments, **plus a bone-removing set** to make the "
         "osteotomy, **plus nasal instruments** to work inside the nose.",
    uses=["Chronic dacryocystitis and epiphora from nasolacrimal duct "
          "obstruction",
          "Mucocele or lacrimal sac abscess",
          "Failed probing, syringing or intubation",
          "Dacryolithiasis (lacrimal stones)",
          "External DCR (skin incision) or endonasal endoscopic DCR",
          "Conjunctivodacryocystorhinostomy with a Lester Jones tube for "
          "canalicular obstruction"],
    plate=PL("Signature instruments",
             [("lacrimal_probe", "Bowman lacrimal probes, graded"),
              ("rongeur", "Bone punch / rongeur — osteotomy"),
              ("periosteal", "Periosteal elevator"),
              ("nasal_speculum", "Nasal speculum"),
              ("frazier", "Fine suction")],
             cap="Fig 9.4 — Eye instruments, bone instruments and nasal "
                 "instruments in one tray"),
    groups=[
        G("Base set", [
            ("1", "Basic eye procedures tray", "see 9.1"),
            ("1", "Nasal procedures tray items", "see 8.2"),
        ]),
        G("Lacrimal system instruments", [
            ("1", "**Punctum dilator (Nettleship)**",
             "**signature item** — dilates the punctum before probing"),
            ("—", "**Bowman lacrimal probes, graded 0000 to 8**",
             "**signature item** — double-ended graduated probes exploring "
             "and calibrating the canaliculus and duct"),
            ("1", "**Lacrimal cannula with syringe**",
             "syringing to confirm the level of obstruction"),
            ("1", "**Lacrimal sac retractor / Rollet's rougine**", ""),
            ("2", "Lacrimal dissector and sac elevator",
             "frees the sac from the lacrimal fossa"),
            ("1", "**Lacrimal / canalicular trephine**", ""),
            ("—", "**Silicone intubation set — Crawford or bicanalicular "
                  "silicone tube with metal probes**",
             "**signature item** — the stent that keeps the new ostium "
             "patent"),
            ("—", "**Lester Jones (Pyrex) tube**",
             "conjunctivodacryocystorhinostomy for canalicular block"),
            ("1", "Fluorescein and dye disappearance test materials", ""),
            ("1", "Chalazion / lacrimal sac forceps", ""),
        ]),
        G("Bone removal — creating the osteotomy", [
            ("2", "**Bone punch / rongeur (Citelli, Hajek, Kerrison), "
                  "up-biting**",
             "**signature item** — removes the lacrimal bone and frontal "
             "process of the maxilla to make the ostium"),
            ("1", "**Periosteal elevator (Freer, Traquair)**",
             "raises the periosteum and reflects the sac from the fossa"),
            ("2", "**Bone chisel / osteotome and small mallet**",
             "initiates the osteotomy"),
            ("1", "**Bone burr / micro-drill with irrigation**",
             "enlarges and smooths the ostium"),
            ("2", "Small bone curettes and a bone rasp", ""),
            ("—", "**Bone wax**", "haemostasis of the bony edge"),
            ("—", "Suction with a fine tip to clear bone dust", ""),
        ]),
        G("Nasal component", [
            ("—", "Nasal specula (Thudichum, Killian)", ""),
            ("1", "**Nasal endoscope 0° / 30° with camera and monitor**",
             "**endonasal DCR is performed entirely endoscopically**"),
            ("2", "**Blakesley through-cutting and back-biting forceps**",
             "removes mucosa and bone from within the nose"),
            ("1", "Sickle knife and Freer elevator",
             "raises a nasal mucosal flap"),
            ("1", "Microdebrider", ""),
            ("—", "**Topical decongestant — adrenaline / xylometazoline on "
                  "ribbon gauze**",
             "**shrinks the nasal mucosa and reduces bleeding before "
             "starting**"),
            ("2", "Bayonet forceps and fine nasal suction", ""),
            ("—", "Nasal packing", ""),
        ]),
        G("Suture, haemostasis and accessory", [
            ("—", "**6-0 / 7-0 absorbable suture**",
             "anastomosis of the lacrimal sac flaps to the nasal mucosal "
             "flaps — **the flap-to-flap anastomosis is the essence of the "
             "operation**"),
            ("—", "6-0 nylon or absorbable subcuticular for skin",
             "external DCR"),
            ("2", "Fine needle holders and tying forceps", ""),
            ("1", "Bipolar cautery, fine and bayonet", ""),
            ("—", "**Local anaesthetic with adrenaline; infratrochlear and "
                  "infraorbital blocks**", ""),
            ("—", "Mitomycin C",
             "sometimes applied to reduce ostium fibrosis"),
            ("—", "Counted sponge spears and gauze", ""),
            ("—", "Specimen container",
             "sac wall for histology if malignancy suspected"),
            ("—", "Eye pad, shield and nasal dressing", ""),
        ]),
    ],
    extras=[("Position", "Supine with a **15–30° head-up tilt** to reduce "
             "venous congestion and bleeding; head on a ring turned "
             "slightly away for an external approach."),
            ("External versus endonasal",
             "**External DCR** uses a curvilinear skin incision medial to "
             "the medial canthus, gives excellent access and a very high "
             "success rate, but leaves a scar. **Endonasal endoscopic DCR** "
             "avoids a scar, preserves the lacrimal pump, and is now widely "
             "preferred where endoscopic skill and equipment exist."),
            ("Structures at risk",
             "**Medial canthal tendon** (must be preserved or reattached), "
             "**angular vein** (troublesome bleeding), orbital fat and "
             "periorbita, the **ethmoidal air cells and lamina papyracea**, "
             "and the **cribriform plate** superiorly — breaching it causes "
             "a CSF leak."),
            ("Complications",
             "Haemorrhage and epistaxis, failure with re-obstruction of the "
             "ostium, scarring and webbing, tube extrusion or displacement, "
             "cellulitis, CSF leak, and injury to the medial canthal "
             "tendon with telecanthus.")],
    side_box={"title": "Why bone instruments on an eye tray?",
              "lines": ["The lacrimal sac lies in the **lacrimal fossa**, "
                        "separated from the nose by the **thin lacrimal bone "
                        "and frontal process of the maxilla**.",
                        "A **bony ostium must be created** to join sac to "
                        "nose.",
                        "Hence punches, chisels, a burr and bone wax — "
                        "instruments found on no other ophthalmic tray."]},
    points=[
        "Explain that this tray is **ophthalmic + bone + nasal** — the only "
        "one of its kind in this Part.",
        "**Bowman probes and the punctum dilator** are the lacrimal "
        "signatures; **Citelli/Kerrison bone punch** the bony one.",
        "The **silicone (Crawford) intubation set** keeps the ostium patent; "
        "a **Lester Jones tube** is used for canalicular block.",
        "The operation's essence is the **sac-flap to nasal-mucosa-flap "
        "anastomosis** with 6-0 absorbable suture.",
        "**Topical nasal decongestion before starting** and a **head-up "
        "tilt** reduce bleeding.",
        "Name the structures at risk, especially the **medial canthal "
        "tendon, angular vein and cribriform plate**.",
        "Compare **external and endonasal endoscopic DCR**.",
    ],
    qa=[("Describe the dacryocystorhinostomy tray.",
         "A basic eye tray plus nasal tray items, with three specific "
         "groups. **Lacrimal**: Nettleship punctum dilator, graded Bowman "
         "probes 0000–8, lacrimal cannula and syringe, sac retractor and "
         "Rollet's rougine, lacrimal dissectors and elevators, canalicular "
         "trephine, Crawford silicone bicanalicular intubation set and a "
         "Lester Jones tube, with fluorescein. **Bone**: up-biting Citelli, "
         "Hajek or Kerrison bone punches, Freer/Traquair periosteal "
         "elevators, bone chisel with small mallet, irrigated micro-burr, "
         "small curettes, rasp and bone wax. **Nasal**: Thudichum and "
         "Killian specula, 0°/30° endoscope with camera and monitor, "
         "Blakesley through-cutting and back-biting forceps, sickle knife, "
         "Freer elevator, microdebrider, topical decongestant, bayonet "
         "forceps, fine suction and packing. Plus 6-0/7-0 absorbable suture "
         "for the flap-to-flap anastomosis, fine needle holders, bayonet "
         "bipolar cautery, local anaesthetic with adrenaline, mitomycin C, "
         "counted sponge spears and dressings."),
        ("What is the essential surgical step of a DCR?",
         "Creation of a bony ostium between the lacrimal fossa and the nasal "
         "cavity, followed by **anastomosis of flaps of the opened lacrimal "
         "sac to flaps of nasal mucosa** with fine absorbable suture, so "
         "that tears drain directly from the sac into the nose, bypassing "
         "the obstructed nasolacrimal duct. A silicone stent may be left to "
         "maintain patency.")]))



# ================================================================ 9.5
_TRAYS.append(T(
    "9.5", "Corneal Procedures Tray",
    aka="Keratoplasty tray · corneal graft (PK / DALK / DSAEK) set",
    lead="**Corneal surgery** replaces or repairs a tissue **half a "
         "millimetre thick and optically perfect**. The tray's defining "
         "instruments are the **trephines** that cut a precisely circular "
         "graft and host bed, and it is entirely a **microscope-and-"
         "11-0-suture** operation. A second, non-instrument requirement is "
         "absolute: the **donor cornea must be present, checked and within "
         "its expiry** before the host cornea is cut.",
    uses=["Penetrating keratoplasty (PK) — full-thickness corneal graft",
          "Deep anterior lamellar keratoplasty (DALK)",
          "Endothelial keratoplasty — DSAEK and DMEK",
          "Keratoconus, corneal scarring, dystrophy, bullous keratopathy",
          "Repair of a corneal laceration or perforation; tectonic graft",
          "Corneal collagen cross-linking; pterygium with corneal "
          "involvement",
          "Keratoprosthesis implantation"],
    plate=PL("Signature instruments",
             [("trephine", "Corneal trephine with cutting crown"),
              ("fine_forceps", "Colibri / suturing forceps"),
              ("castroviejo_nh", "Castroviejo needle holder"),
              ("iris_scissors", "Corneal (Castroviejo) scissors"),
              ("lid_speculum", "Lid speculum")],
             cap="Fig 9.5 — Trephine the host, trephine the donor, suture"),
    groups=[
        G("Base set", [
            ("1", "Basic eye procedures tray", "see 9.1"),
            ("1", "Operating microscope with fine focus and coaxial "
                  "illumination", "**essential**"),
        ]),
        G("Trephines — the defining group", [
            ("—", "**Corneal trephines, graded 6.0–9.0 mm in 0.25 mm "
                  "steps**",
             "**signature item** — a circular cutting crown that cuts a "
             "perfectly round graft bed"),
            ("1", "**Hand-held (Castroviejo) and suction (Barron) "
                  "trephine**",
             "the suction trephine stabilises the globe and controls depth"),
            ("1", "**Donor punch with a Teflon cutting block**",
             "**signature item** — the donor button is punched from the "
             "**endothelial side** on a concave block"),
            ("1", "Femtosecond laser interface",
             "where laser-assisted keratoplasty is available"),
            ("1", "**Optical zone / corneal marker (radial, 8- or "
                  "16-blade)**",
             "marks radial guides so sutures are placed symmetrically"),
            ("1", "Calliper and depth gauge",
             "for lamellar dissection depth"),
        ]),
        G("Corneal cutting and dissecting", [
            ("2", "**Castroviejo corneal scissors, left and right**",
             "**signature item** — angled blades completing the trephination "
             "in each direction"),
            ("2", "**Corneal (Colibri) forceps, 0.12 mm**",
             "**signature item** — very fine angled toothed forceps for the "
             "graft edge"),
            ("2", "Vannas and Westcott scissors", ""),
            ("1", "**Beaver / diamond knife, and crescent and "
                  "keratome blades**",
             "lamellar dissection and paracentesis"),
            ("2", "**Lamellar dissectors and cyclodialysis spatula**",
             "DALK / DSAEK plane dissection"),
            ("1", "**Big-bubble cannula (DALK)**",
             "injects air to separate Descemet's membrane"),
            ("2", "**Descemet's stripper / reverse Sinskey hook**",
             "endothelial keratoplasty"),
            ("1", "**Graft inserter / glide (Busin, Tan EndoGlide)**",
             "delivers a thin endothelial graft without damaging it"),
            ("1", "Corneal dissector and Paufique knife", ""),
        ]),
        G("Anterior chamber management", [
            ("—", "**Viscoelastic (OVD — sodium hyaluronate)**",
             "**signature requirement** — maintains the anterior chamber and "
             "protects the endothelium"),
            ("2", "**Anterior chamber (Rycroft) cannula with BSS**", ""),
            ("1", "**Air / gas injection cannula and syringe**",
             "tamponades an endothelial graft against the host"),
            ("2", "Iris repositor and iris spatula",
             "frees iris adhesions and reposits prolapsed iris"),
            ("2", "Sinskey and Kuglen hooks", ""),
            ("1", "Iris scissors (de Wecker) and iris forceps",
             "peripheral iridectomy or synechiolysis"),
            ("—", "Miotic (acetylcholine) and mydriatic",
             "constricts or dilates the pupil as required"),
        ]),
        G("Suturing — the finest in surgery", [
            ("2", "**Castroviejo / Barraquer needle holder, fine, "
                  "non-locking**", ""),
            ("—", "**10-0 and 11-0 nylon monofilament on a spatulated "
                  "needle**",
             "**signature requirement** — interrupted, continuous or "
             "combined; **buried knots**"),
            ("2", "**Tying forceps with a suture platform**", ""),
            ("1", "**Suture adjusting hook / Sinskey hook**",
             "distributes tension"),
            ("1", "**Hand-held keratoscope or Placido disc**",
             "**signature item** — checks the corneal curvature "
             "intra-operatively so astigmatism is minimised"),
            ("1", "Suture-cutting scissors, fine", ""),
        ]),
        G("The donor tissue and accessory — non-negotiable checks", [
            ("—", "**Donor cornea in its storage medium (Optisol / "
                  "Eusol-C), with the eye-bank documentation**",
             "**identity, serology, endothelial cell count and expiry are "
             "checked and recorded BEFORE the host cornea is cut**"),
            ("—", "**Sterile Teflon cutting block and storage vial**", ""),
            ("—", "Corneal storage / transport container", ""),
            ("1", "Specular microscope / pachymeter",
             "graft thickness and endothelial assessment"),
            ("—", "Counted cellulose sponge spears", ""),
            ("—", "Antibiotic, steroid and cycloplegic drops",
             "labelled and checked"),
            ("—", "**Bandage contact lens**", "protects the epithelium"),
            ("—", "Eye pad and cartella shield", ""),
            ("—", "Specimen container",
             "**the excised host button is sent for histology**"),
        ]),
    ],
    extras=[("Position", "Supine, head stabilised, **iris plane exactly "
             "horizontal** so the trephine cuts perpendicular to the cornea "
             "— an oblique cut produces astigmatism."),
            ("Intraocular pressure",
             "The eye must be **soft** before a full-thickness trephination: "
             "hypotensive anaesthesia, mannitol, ocular compression or a "
             "Flieringa ring in a soft eye. A firm eye risks **expulsive "
             "haemorrhage** and iris or lens prolapse when the cornea is "
             "opened."),
            ("The 'open-sky' interval",
             "Between removing the host cornea and securing the donor, the "
             "eye is fully open. This interval is kept as **short as "
             "possible** and all instruments and suture are prepared in "
             "advance."),
            ("Complications",
             "Graft rejection and failure, **expulsive suprachoroidal "
             "haemorrhage** (the catastrophe of open-sky surgery), wound "
             "leak, high post-keratoplasty astigmatism, glaucoma, "
             "endophthalmitis, cataract, and epithelial or interface "
             "problems in lamellar grafts.")],
    side_box={"title": "Before you cut the host",
              "lines": ["**Confirm the donor cornea is present**, correctly "
                        "identified, serology-cleared and **in date**.",
                        "**Soften the eye** — a firm eye risks expulsive "
                        "haemorrhage.",
                        "**Have every instrument and the 10-0 suture ready** "
                        "— the open-sky interval must be minimal.",
                        "Cutting the host before these three checks is an "
                        "irreversible error."]},
    points=[
        "The **graded trephines and the donor punch on a Teflon block** are "
        "the signature items — note the donor is punched **from the "
        "endothelial side**.",
        "**Castroviejo corneal scissors (left and right)** and **0.12 mm "
        "Colibri forceps** are the corneal handling pair.",
        "**10-0 / 11-0 nylon on spatulated needles with buried knots**.",
        "**Viscoelastic (OVD) to protect the endothelium** and maintain the "
        "chamber.",
        "**Donor tissue checked before the host is cut** — the single most "
        "important safety point.",
        "**Soften the eye** to avoid **expulsive haemorrhage**; minimise the "
        "**open-sky interval**.",
        "An **intra-operative keratoscope** minimises astigmatism.",
        "Mention modern lamellar techniques — **DALK big-bubble cannula, "
        "DSAEK Descemet's stripper and graft inserter**.",
    ],
    qa=[("Describe the corneal procedures tray.",
         "A basic eye tray with the operating microscope, plus: trephines — "
         "graded 6.0–9.0 mm hand-held Castroviejo and suction Barron "
         "trephines, a donor punch with Teflon cutting block, optical-zone "
         "and radial markers, callipers and a depth gauge; corneal cutting — "
         "left and right Castroviejo corneal scissors, 0.12 mm Colibri "
         "forceps, Vannas and Westcott scissors, diamond/crescent/keratome "
         "blades, lamellar dissectors, a DALK big-bubble cannula, Descemet's "
         "stripper and a graft inserter glide; anterior chamber management — "
         "viscoelastic, Rycroft cannula with BSS, air injection cannula, iris "
         "repositor and spatula, Sinskey and Kuglen hooks, de Wecker "
         "scissors, miotics and mydriatics; suturing — fine non-locking "
         "Castroviejo needle holders with 10-0 and 11-0 nylon on spatulated "
         "needles, tying forceps with platform, suture-adjusting hook and an "
         "intra-operative keratoscope; and the donor cornea in storage "
         "medium with full eye-bank documentation checked in advance, a "
         "pachymeter, counted sponge spears, drops, a bandage contact lens "
         "and a specimen container for the host button."),
        ("What must be confirmed before the host cornea is trephined?",
         "That the donor cornea is physically present in theatre, correctly "
         "identified against the eye-bank documentation, serologically "
         "cleared, of acceptable endothelial cell count and within its "
         "expiry date; that the eye has been softened to reduce the risk of "
         "expulsive haemorrhage; and that all instruments and 10-0 suture "
         "are prepared so the open-sky interval is as short as possible.")]))



# ================================================================ 9.6
_TRAYS.append(T(
    "9.6", "Cataract Extraction and Lens Procedures Tray",
    aka="Cataract tray · phacoemulsification and IOL implantation set",
    lead="**Cataract surgery** removes the opacified lens and replaces it "
         "with an **intraocular lens (IOL)**. Modern practice is "
         "**phacoemulsification**: the lens is emulsified by an ultrasonic "
         "probe and aspirated through a 2–3 mm incision, leaving the "
         "posterior capsule intact to support a foldable IOL. The tray is "
         "therefore a **machine-plus-microinstruments** set, and it "
         "**always** carries the means to convert to a manual technique and "
         "to manage a ruptured capsule.",
    uses=["Age-related, traumatic, congenital and metabolic cataract",
          "Phacoemulsification with posterior chamber IOL implantation",
          "Manual small-incision cataract surgery (MSICS) and "
          "extracapsular extraction",
          "Intracapsular extraction in subluxated lens (rarely)",
          "Secondary IOL implantation; IOL exchange or repositioning",
          "Lens removal in phacomorphic or phacolytic glaucoma",
          "Refractive lens exchange"],
    plate=PL("Signature instruments",
             [("phaco", "Phacoemulsification handpiece"),
              ("fine_forceps", "Capsulorhexis forceps"),
              ("iris_scissors", "Vannas / capsulotomy scissors"),
              ("castroviejo_nh", "Fine needle holder"),
              ("lid_speculum", "Lid speculum")],
             cap="Fig 9.6 — Machine, microinstruments and an implant"),
    groups=[
        G("Base set", [
            ("1", "Basic eye procedures tray", "see 9.1"),
            ("1", "Operating microscope with coaxial illumination and foot "
                  "control", "**essential**"),
        ]),
        G("Incision and entry", [
            ("2", "**Keratome / slit knife, 2.2–3.2 mm**",
             "**signature item** — makes the main clear-corneal incision"),
            ("1", "**Side-port (15°/MVR) blade**",
             "**signature item** — the paracentesis for the second "
             "instrument"),
            ("1", "Crescent blade", "scleral tunnel in MSICS"),
            ("1", "Beaver handle with micro-blades", ""),
            ("2", "Conjunctival and corneal 0.12 mm forceps", ""),
            ("1", "Calliper / incision gauge", ""),
            ("1", "Fixation ring / Thornton ring",
             "stabilises the globe during entry"),
        ]),
        G("Capsulotomy — the critical step", [
            ("2", "**Capsulorhexis forceps (Utrata)**",
             "**signature item** — creates a **continuous curvilinear "
             "capsulorhexis**, the step on which the whole operation "
             "depends"),
            ("1", "**Cystotome / bent 26G needle on a syringe**",
             "initiates the capsular flap"),
            ("1", "Vannas / capsulotomy micro-scissors", ""),
            ("—", "**Capsular dye — trypan blue**",
             "**stains the capsule in a dense white cataract** so the rhexis "
             "is visible"),
            ("1", "Femtosecond laser platform",
             "laser-assisted capsulotomy where available"),
        ]),
        G("Phacoemulsification and lens removal", [
            ("1", "**Phacoemulsification machine with handpiece, "
                  "titanium tip, irrigating sleeve and foot pedal**",
             "**signature item** — ultrasonic vibration emulsifies the "
             "nucleus while irrigation and aspiration remove it"),
            ("1", "**Irrigation / aspiration (I/A) handpiece with "
                  "straight and curved tips**",
             "removes the soft cortex"),
            ("2", "**Nucleus rotator / Sinskey and Kuglen hooks**",
             "rotates and manipulates the nucleus"),
            ("2", "**Chopper (nucleus chopper) and phaco spatula**",
             "**signature item** — divides the nucleus in "
             "divide-and-conquer or phaco-chop"),
            ("1", "**Lens loop / vectis and irrigating vectis**",
             "**signature item for MSICS** — delivers the whole nucleus"),
            ("1", "Simcoe cannula",
             "manual irrigation–aspiration of cortex"),
            ("1", "Capsule polisher", "cleans the posterior capsule"),
            ("1", "Bimanual I/A set", ""),
            ("—", "**Balanced salt solution with the infusion bottle at a "
                  "set height**",
             "maintains the chamber; height controls infusion pressure"),
        ]),
        G("The intraocular lens", [
            ("—", "**Intraocular lenses — foldable posterior-chamber IOLs, "
                  "full power range, with the calculated power confirmed**",
             "**signature requirement** — power from pre-operative "
             "biometry; **checked against the patient's notes and the "
             "correct eye**"),
            ("—", "**Rigid PMMA IOL available**",
             "for MSICS or a large-incision conversion"),
            ("—", "**Anterior-chamber and sulcus/scleral-fixated IOLs "
                  "available**",
             "**for capsular rupture — the tray must be able to cope with "
             "the complication**"),
            ("1", "**IOL injector / cartridge and forceps**",
             "folds and delivers the lens through the small incision"),
            ("2", "**Lens dialler / Sinskey hook**",
             "positions the IOL in the capsular bag"),
            ("1", "Capsular tension ring with inserter",
             "for zonular weakness"),
        ]),
        G("Viscoelastic, complication management and closure", [
            ("—", "**Viscoelastic (OVD) — cohesive and dispersive**",
             "**signature requirement** — maintains the chamber, protects "
             "the endothelium and flattens the capsule for the rhexis"),
            ("1", "**Anterior vitrectomy (vitrector) set**",
             "**must be available** — for posterior capsular rupture with "
             "vitreous loss"),
            ("2", "**Iris hooks / retractors and a pupil expansion ring "
                  "(Malyugin)**", "for a small or floppy pupil"),
            ("1", "Iris repositor, de Wecker scissors and iris forceps", ""),
            ("—", "**Intracameral mydriatic, miotic (acetylcholine) and "
                  "intracameral antibiotic (cefuroxime / moxifloxacin)**",
             "intracameral antibiotic markedly reduces endophthalmitis"),
            ("—", "**10-0 nylon suture and fine needle holder**",
             "**available** — most incisions are self-sealing but a leaking "
             "wound must be sutured"),
            ("1", "Wound hydration cannula and Seidel test fluorescein",
             "confirms the wound is watertight"),
            ("—", "Counted cellulose sponge spears", ""),
            ("—", "Eye pad, cartella shield and post-operative drops", ""),
        ]),
    ],
    extras=[("Position", "Supine, head stabilised, **iris plane "
             "horizontal**; surgeon at the head or temporally. Topical or "
             "peribulbar/sub-Tenon anaesthesia is usual; general "
             "anaesthesia for children and the uncooperative."),
            ("Biometry and the correct lens",
             "**IOL power is calculated pre-operatively by biometry.** The "
             "power, model and **correct eye** are confirmed at the "
             "checklist. Implanting the wrong-power lens is a recognised "
             "never-event and requires explantation."),
            ("Posterior capsular rupture",
             "The commonest serious intra-operative complication. Management "
             "requires **viscoelastic to tamponade, an anterior vitrectomy "
             "to remove prolapsed vitreous, and an alternative IOL** (sulcus, "
             "anterior chamber or scleral-fixated). This is why those items "
             "are on the tray from the start."),
            ("Complications",
             "Posterior capsular rupture with vitreous loss, dropped nucleus, "
             "**endophthalmitis** (the most feared), corneal endothelial "
             "damage and oedema, iris trauma, cystoid macular oedema, "
             "IOL decentration, refractive surprise, and — rarely — "
             "expulsive haemorrhage.")],
    side_box={"title": "Three checks before the first incision",
              "lines": ["**Correct patient, correct eye** — marked and "
                        "confirmed.",
                        "**Correct IOL power and model**, verified against "
                        "the biometry.",
                        "**Back-up plan present** — anterior vitrector and "
                        "alternative IOLs available in case of capsular "
                        "rupture."]},
    compare=CMP(
        ["", "Phacoemulsification", "MSICS / extracapsular"],
        [["Incision", "2.2–3.2 mm clear cornea",
          "6–7 mm scleral tunnel"],
         ["Nucleus removal", "**Ultrasonic emulsification and aspiration**",
          "**Delivered whole with a lens loop / vectis**"],
         ["Key instrument", "Phaco handpiece and chopper",
          "Irrigating vectis / lens loop"],
         ["IOL type", "Foldable, injected", "Rigid PMMA, forceps-inserted"],
         ["Sutures", "Usually none — self-sealing",
          "Often none, but suture available"],
         ["Best suited to", "Most cataracts; faster visual recovery",
          "Very dense cataract, high-volume or low-resource settings"]],
        cap="Table 9.1 — The two techniques the tray must support"),
    points=[
        "Name the **phaco handpiece, Utrata capsulorhexis forceps, chopper "
        "and IOL injector** — the four signatures of modern cataract "
        "surgery.",
        "**Continuous curvilinear capsulorhexis** is the critical step; "
        "**trypan blue** stains the capsule in a white cataract.",
        "**Viscoelastic protects the endothelium and maintains the "
        "chamber** — state both functions.",
        "**IOL power from biometry, verified for the correct eye** — a "
        "never-event if wrong.",
        "The tray must carry an **anterior vitrector and alternative IOLs "
        "for capsular rupture** — this is the mark most candidates miss.",
        "**Intracameral antibiotic** reduces endophthalmitis, the most "
        "feared complication.",
        "Be able to compare **phacoemulsification with MSICS** (Table 9.1).",
    ],
    pitfalls=["Listing the phaco machine but omitting the capsulorhexis "
              "forceps.",
              "Forgetting the back-up items for posterior capsular rupture.",
              "Not mentioning verification of IOL power and the correct eye.",
              "Omitting viscoelastic, or not knowing its two functions."],
    qa=[("Describe the cataract extraction and lens procedures tray.",
         "A basic eye tray with the operating microscope, plus: incision — "
         "2.2–3.2 mm keratome, side-port/MVR blade, crescent blade, 0.12 mm "
         "forceps, gauge and fixation ring; capsulotomy — Utrata "
         "capsulorhexis forceps, cystotome, capsulotomy micro-scissors and "
         "trypan blue dye; lens removal — phacoemulsification machine with "
         "handpiece, titanium tip, sleeve and foot pedal, irrigation/"
         "aspiration handpiece, nucleus rotator, Sinskey and Kuglen hooks, "
         "nucleus chopper and spatula, lens loop/irrigating vectis, Simcoe "
         "cannula, capsule polisher and balanced salt solution; the implant "
         "— foldable posterior-chamber IOLs of verified power with an "
         "injector and cartridge, rigid PMMA and anterior-chamber or "
         "scleral-fixated lenses available, lens dialler and a capsular "
         "tension ring; and viscoelastic (cohesive and dispersive), an "
         "anterior vitrectomy set, iris hooks and a pupil expansion ring, "
         "intracameral mydriatic, miotic and antibiotic, 10-0 nylon with a "
         "fine needle holder, wound hydration cannula, fluorescein for a "
         "Seidel test, counted sponge spears and a shield."),
        ("Why must an anterior vitrector and alternative IOLs be available "
         "for every cataract operation?",
         "Because posterior capsular rupture with vitreous loss is the "
         "commonest serious intra-operative complication. Prolapsed vitreous "
         "must be removed with an anterior vitrector to prevent traction, "
         "retinal detachment and cystoid macular oedema, and the planned "
         "in-the-bag IOL can no longer be used — a sulcus, "
         "anterior-chamber or scleral-fixated lens is required instead. "
         "Having these ready avoids abandoning the operation.")]))



# ================================================================ 9.7
_TRAYS.append(T(
    "9.7", "Glaucoma Procedure Tray",
    aka="Trabeculectomy tray · filtration surgery set",
    lead="**Glaucoma surgery** creates a new route for aqueous to leave the "
         "eye, lowering intraocular pressure. The standard operation, "
         "**trabeculectomy**, raises a partial-thickness **scleral flap** "
         "under a conjunctival flap, removes a block of trabecular tissue, "
         "and allows aqueous to drain into a subconjunctival **bleb**. The "
         "tray is a basic eye tray plus the instruments to raise those "
         "flaps, punch the sclerostomy, and — critically — the "
         "**antifibrotic agents** that stop the bleb scarring closed.",
    uses=["Primary open-angle glaucoma uncontrolled by medical therapy",
          "Angle-closure glaucoma after iridotomy has failed",
          "Trabeculectomy with mitomycin C or 5-fluorouracil",
          "Glaucoma drainage device implantation (Ahmed, Baerveldt, "
          "Molteno)",
          "Minimally invasive glaucoma surgery (MIGS) — stents and "
          "goniotomy",
          "Cyclodestructive procedures — cyclophotocoagulation, "
          "cyclocryotherapy",
          "Congenital glaucoma — goniotomy and trabeculotomy"],
    plate=PL("Signature instruments",
             [("fine_forceps", "Fine conjunctival forceps"),
              ("iris_scissors", "Westcott scissors — flaps"),
              ("trephine", "Kelly Descemet's punch"),
              ("castroviejo_nh", "Fine needle holder"),
              ("lid_speculum", "Lid speculum")],
             cap="Fig 9.7 — Raise the flaps, punch the sclerostomy, "
                 "control fibrosis"),
    groups=[
        G("Base set", [
            ("1", "Basic eye procedures tray", "see 9.1"),
            ("1", "Operating microscope", "**essential**"),
        ]),
        G("Conjunctival and scleral flaps", [
            ("2", "**Westcott spring scissors, curved and blunt**",
             "**signature item** — raises the fornix- or limbus-based "
             "conjunctival flap"),
            ("2", "**Conjunctival forceps, non-toothed and 0.12 mm "
                  "toothed**",
             "handles conjunctiva without buttonholing it"),
            ("1", "**Crescent blade / lamellar dissector**",
             "**signature item** — dissects the **partial-thickness scleral "
             "flap** at about half scleral depth"),
            ("1", "Beaver handle with No.64 / 69 blades", ""),
            ("1", "**Scleral / corneal marker and callipers**",
             "marks the flap dimensions (e.g. 4 × 3 mm)"),
            ("2", "Tenon's dissecting scissors and Tenon's forceps", ""),
            ("1", "Bipolar wet-field cautery, fine",
             "**light, focal cautery only** — excess cautery causes "
             "scarring and bleb failure"),
            ("—", "4-0 silk corneal traction suture",
             "rotates the globe to expose the superior limbus"),
        ]),
        G("Sclerostomy and iridectomy", [
            ("1", "**Kelly (Descemet's) punch**",
             "**signature item** — punches out a precise block of "
             "trabecular tissue and Descemet's membrane, creating the "
             "sclerostomy"),
            ("1", "**Keratome / MVR blade**",
             "enters the anterior chamber beneath the flap"),
            ("2", "**Vannas scissors and de Wecker iris scissors**",
             "peripheral iridectomy"),
            ("2", "**Iris forceps (Colibri, fine toothed)**",
             "grasps the iris for the iridectomy"),
            ("1", "Iris repositor / spatula",
             "reposits the iris and confirms the sclerostomy is patent"),
            ("1", "Trabeculotome / goniotomy knife",
             "congenital glaucoma"),
            ("1", "**Gonioscopy / surgical gonioprism**",
             "views the angle for MIGS and goniotomy"),
            ("1", "Sinskey hook", ""),
        ]),
        G("Antifibrotic agents — the defining requirement", [
            ("—", "**Mitomycin C (0.2–0.4 mg/mL) on cellulose sponges**",
             "**signature requirement** — applied to the scleral bed for "
             "1–3 minutes to inhibit fibroblast proliferation, then "
             "**copiously irrigated away**"),
            ("—", "**5-fluorouracil**", "alternative antifibrotic"),
            ("—", "**Dedicated sponges, forceps and a separate "
                  "disposal container for the antimetabolite**",
             "**cytotoxic — handled with separate instruments, counted, and "
             "disposed of as cytotoxic waste**"),
            ("—", "**Copious balanced salt solution for irrigation**",
             "**every trace must be washed out** — residual agent causes "
             "hypotony, wound melt and toxicity"),
            ("—", "Collagen matrix implant (Ologen)",
             "non-pharmacological bleb modulation"),
        ]),
        G("Drainage devices and MIGS", [
            ("—", "**Glaucoma drainage device — Ahmed, Baerveldt or "
                  "Molteno — with its plate and tube**", ""),
            ("1", "Tube-trimming scissors and a tube introducer", ""),
            ("—", "**Donor scleral or pericardial patch graft**",
             "covers the tube to prevent erosion through the conjunctiva"),
            ("1", "23G / 25G needle", "creates the tube track"),
            ("—", "**MIGS implants — trabecular micro-bypass stents, "
                  "with injectors**", ""),
            ("1", "Cyclophotocoagulation / cyclocryotherapy probe", ""),
            ("—", "Non-absorbable 8-0 / 9-0 suture to fix the plate", ""),
        ]),
        G("Suture, chamber management and accessory", [
            ("2", "**Castroviejo needle holder, fine**", ""),
            ("—", "**10-0 nylon for the scleral flap — including "
                  "releasable or adjustable sutures**",
             "**signature requirement** — flap tension controls the rate of "
             "drainage; releasable sutures allow post-operative titration"),
            ("—", "**8-0 / 9-0 absorbable (Vicryl) for conjunctiva**",
             "a **watertight conjunctival closure** is essential to form a "
             "bleb"),
            ("—", "**Viscoelastic (OVD)**", "reforms the chamber"),
            ("2", "Anterior chamber cannula with BSS",
             "reforms the chamber and tests flap flow"),
            ("1", "**Fluorescein for the Seidel test**",
             "**confirms there is no conjunctival leak** at the end"),
            ("—", "Laser suture-lysis lens", "post-operative titration"),
            ("—", "Counted cellulose sponge spears", ""),
            ("—", "Subconjunctival / topical steroid and antibiotic",
             "**intensive post-operative steroid suppresses fibrosis**"),
            ("—", "Eye pad and cartella shield", ""),
        ]),
    ],
    extras=[("Position", "Supine, head stabilised, iris plane horizontal; a "
             "superior traction suture rotates the globe downwards to expose "
             "the superior limbus where the bleb is created."),
            ("Why antifibrotics",
             "The commonest cause of trabeculectomy failure is **fibrosis of "
             "the bleb**, which seals the new drainage route. Mitomycin C or "
             "5-FU inhibits fibroblast proliferation and greatly improves "
             "long-term success — which is why they, and their safe "
             "handling, are central to this tray."),
            ("Balance of pressure",
             "The scleral flap must drain **enough but not too much**. Too "
             "tight → pressure remains high; too loose → **hypotony**, with "
             "choroidal effusion, maculopathy and a flat anterior chamber. "
             "**Releasable or adjustable sutures and laser suture lysis** "
             "allow this balance to be adjusted afterwards."),
            ("Complications",
             "Hypotony with choroidal effusion or maculopathy, flat anterior "
             "chamber, bleb leak, **blebitis and endophthalmitis**, bleb "
             "fibrosis with failure, cataract progression, suprachoroidal "
             "haemorrhage, and tube erosion or corneal decompensation with "
             "drainage devices.")],
    side_box={"title": "Mitomycin C safety",
              "lines": ["It is a **cytotoxic agent**.",
                        "Use **dedicated sponges and forceps**, keep them "
                        "separate from the rest of the tray, and "
                        "**count them**.",
                        "**Irrigate the bed copiously** afterwards — "
                        "residual drug causes hypotony and scleral melt.",
                        "Dispose of everything as **cytotoxic waste**."]},
    points=[
        "Name the three signatures: **crescent blade for the scleral flap, "
        "Kelly Descemet's punch for the sclerostomy, and mitomycin C**.",
        "Explain the **partial-thickness scleral flap** and that its "
        "**suture tension governs drainage**.",
        "**Releasable / adjustable 10-0 sutures and laser suture lysis** "
        "allow post-operative titration.",
        "**Watertight conjunctival closure** with a **Seidel test** at the "
        "end.",
        "**Antifibrotic handling** — dedicated instruments, counted, copious "
        "irrigation, cytotoxic disposal.",
        "**Use cautery sparingly** — excess cautery promotes fibrosis and "
        "bleb failure.",
        "Know the alternatives — **drainage devices with a patch graft** and "
        "**MIGS stents**.",
        "**Hypotony** is the complication of over-drainage; **fibrosis** of "
        "under-drainage.",
    ],
    qa=[("Describe the glaucoma procedure (trabeculectomy) tray.",
         "A basic eye tray with the microscope, plus: flap instruments — "
         "curved blunt Westcott scissors, toothed and non-toothed "
         "conjunctival forceps, a crescent blade or lamellar dissector for "
         "the partial-thickness scleral flap, Beaver micro-blades, scleral "
         "marker and callipers, Tenon's scissors and forceps, fine "
         "wet-field cautery and a 4-0 silk traction suture; sclerostomy — "
         "Kelly Descemet's punch, keratome/MVR blade, Vannas and de Wecker "
         "scissors, fine iris forceps and repositor, trabeculotome and a "
         "surgical gonioprism; antifibrotics — mitomycin C or 5-FU with "
         "**dedicated counted sponges and forceps, copious BSS irrigation "
         "and cytotoxic disposal**; drainage devices and MIGS — Ahmed/"
         "Baerveldt/Molteno implant with tube trimmer, scleral patch graft "
         "and 23G needle, MIGS stents with injectors and a "
         "cyclophotocoagulation probe; and closure — fine needle holders "
         "with 10-0 nylon including releasable sutures for the flap, 8-0/9-0 "
         "absorbable for a watertight conjunctival closure, viscoelastic, "
         "an anterior chamber cannula, fluorescein for the Seidel test, "
         "counted sponge spears and intensive post-operative steroid."),
        ("Why are antifibrotic agents used in trabeculectomy and what "
         "precautions do they require?",
         "The principal cause of late failure is fibrosis of the "
         "subconjunctival bleb, which closes the new drainage pathway. "
         "Mitomycin C or 5-fluorouracil applied to the scleral bed inhibits "
         "fibroblast proliferation and improves long-term pressure control. "
         "Because they are cytotoxic, they are applied on dedicated sponges "
         "with dedicated forceps kept separate from the main tray, the "
         "sponges are counted, the bed is then irrigated copiously with "
         "balanced salt solution to remove every trace — residual agent "
         "causes hypotony and scleral melt — and all materials are discarded "
         "as cytotoxic waste.")]))



# ================================================================ 9.8
_TRAYS.append(T(
    "9.8", "Basic Eye Procedures Microscope Tray",
    aka="Ophthalmic microsurgical tray · microscope set-up",
    lead="This tray is best understood not as another set of instruments but "
         "as the **microsurgical platform** on which trays 9.5–9.9 depend: "
         "the **operating microscope itself, its sterile accessories, and "
         "the microinstruments, sutures and handling discipline that go with "
         "it**. Examiners use this heading to test whether you understand "
         "**how microsurgery is set up and how microinstruments are "
         "cared for** — content that carries marks nowhere else.",
    uses=["Any intraocular procedure — cataract, cornea, glaucoma, retina",
          "Microsurgical suturing with 9-0 to 11-0 material",
          "Anterior and posterior segment surgery",
          "Teaching, recording and assistant viewing",
          "Intra-operative imaging — OCT and endoillumination"],
    plate=PL("Microsurgical instruments",
             [("castroviejo_nh", "Castroviejo needle holder"),
              ("fine_forceps", "Colibri 0.12 mm forceps"),
              ("iris_scissors", "Vannas / Westcott spring scissors"),
              ("lacrimal_probe", "Fine cannula")],
             cap="Fig 9.8 — Spring handles, millimetre tips, tip guards"),
    groups=[
        G("The operating microscope and its accessories", [
            ("1", "**Operating microscope with coaxial (co-axial) "
                  "illumination**",
             "**signature item** — coaxial light gives the **red reflex**, "
             "essential for capsulorhexis and lens work"),
            ("1", "**Foot control for zoom, focus and X-Y movement**",
             "leaves both hands free"),
            ("1", "**Sterile drapes for the microscope body and handgrips**",
             "the microscope hangs over the sterile field"),
            ("—", "**Sterilisable handgrips / knobs**", ""),
            ("1", "**Assistant's binocular (co-observer) tube**", ""),
            ("1", "**Beam splitter, camera and monitor with a recorder**",
             "teaching and documentation"),
            ("1", "Eyepieces set to the surgeon's refraction with adjustable "
                  "interpupillary distance",
             "**set and checked before scrubbing**"),
            ("1", "**Slit illuminator and, for retinal work, a "
                  "wide-angle viewing system (BIOM) with an inverter**",
             ""),
            ("1", "Intra-operative OCT",
             "where available — assesses lamellar planes and the macula"),
            ("—", "Spare bulb and a **checked back-up light source**",
             "**failure of illumination mid-procedure is an emergency**"),
        ]),
        G("Microinstrument set", [
            ("2", "**Spring-handled (non-ratcheted) needle holders — "
                  "Castroviejo, Barraquer**", ""),
            ("2", "**Colibri and Bishop-Harmon 0.12 mm forceps**", ""),
            ("2", "**Tying forceps with a suture platform**", ""),
            ("2", "**Vannas and Westcott spring scissors**", ""),
            ("2", "**Micro-spatulas, iris repositor, Sinskey and Kuglen "
                  "hooks**", ""),
            ("—", "**Micro-cannulae, 25G–30G, with syringes**", ""),
            ("1", "**Diamond knife**",
             "the sharpest and most fragile instrument on any tray"),
            ("—", "**Suture 9-0, 10-0 and 11-0 monofilament on spatulated "
                  "needles**", ""),
            ("1", "Magnetic instrument mat / rack", ""),
        ]),
        G("Care and handling of microinstruments — high-yield", [
            ("—", "**Silicone or latex tip guards on every fine tip**",
             "**fitted the moment the instrument leaves the field**"),
            ("—", "**Racked in a slotted, foam-lined tray — never piled "
                  "loose**",
             "instruments touching each other bend and burr the tips"),
            ("—", "**Handled one at a time, by the handle, never the tip**",
             ""),
            ("—", "**Cleaned separately from general instruments**",
             "in a dedicated ophthalmic cycle, to avoid damage and to avoid "
             "**toxic anterior segment syndrome (TASS)** from detergent "
             "residue"),
            ("—", "**Rinsed in distilled / demineralised water and dried "
                  "immediately**",
             "prevents staining, corrosion and residue"),
            ("—", "**Lumens of cannulae and phaco handpieces flushed "
                  "immediately after use**",
             "dried viscoelastic or lens matter is a cause of **TASS**"),
            ("—", "**Ultrasonic cleaning avoided for cemented diamond "
                  "knives and delicate optics**", ""),
            ("—", "**Inspected under magnification before packing**",
             "tips must appose exactly, with no burr, bend or "
             "misalignment"),
            ("—", "**Sterilised by steam or low-temperature methods per the "
                  "manufacturer**",
             "optics and cables usually require EO or plasma"),
            ("—", "**Counted — sponge spears, blades, cannulae, IOLs and "
                  "capsular rings**", ""),
        ]),
        G("Set-up sequence and ergonomics", [
            ("1", "Position the patient with the **iris plane horizontal**",
             ""),
            ("2", "**Set eyepieces, interpupillary distance and "
                  "parfocality** before scrubbing", ""),
            ("3", "Drape the microscope and attach sterile handgrips", ""),
            ("4", "Balance and centre the microscope over the eye; check "
                  "the **X-Y and focus foot controls**", ""),
            ("5", "Adjust the surgeon's **chair, armrests and wrist "
                  "support**",
             "the hands must rest on the patient's forehead — **unsupported "
             "hands tremble**"),
            ("6", "Set the **light to the lowest adequate intensity**",
             "**minimises phototoxic retinal injury**"),
            ("7", "Lay out instruments in **order of use** on a magnetic "
                  "mat within a small hand excursion", ""),
            ("8", "Confirm back-up illumination and a spare handpiece", ""),
        ]),
    ],
    extras=[("Why a microscope and not loupes",
             "Intraocular structures are measured in **micrometres**: the "
             "lens capsule is about 4 µm thick and Descemet's membrane about "
             "10 µm. Only a microscope provides the **magnification (6–25×), "
             "coaxial illumination for the red reflex, stereopsis and "
             "stability** required."),
            ("Phototoxicity",
             "Prolonged high-intensity coaxial light can cause "
             "**phototoxic maculopathy**. The light is kept at the lowest "
             "adequate intensity, the beam is not focused on the macula "
             "longer than necessary, and filters are used."),
            ("Toxic anterior segment syndrome (TASS)",
             "A severe sterile inflammation of the anterior segment caused "
             "by **residues on instruments** — detergent, endotoxin, "
             "denatured viscoelastic or preservatives. It is prevented "
             "almost entirely by the instrument-care rules above: immediate "
             "flushing of lumens, dedicated cleaning cycles and "
             "distilled-water rinsing.")],
    side_box={"title": "TASS is a tray problem",
              "lines": ["**Toxic anterior segment syndrome** is caused by "
                        "**instrument residue**, not by infection.",
                        "Its prevention lies entirely in tray practice: "
                        "**flush lumens immediately, clean ophthalmic "
                        "instruments separately, rinse in distilled water, "
                        "avoid detergent residue**.",
                        "This is why 'care of microinstruments' is "
                        "examinable content, not housekeeping."]},
    points=[
        "Treat this heading as **the microsurgical platform**, not another "
        "instrument list.",
        "**Coaxial illumination gives the red reflex** — say why it "
        "matters.",
        "**Eyepieces, interpupillary distance and parfocality are set "
        "before scrubbing**.",
        "**Tip guards, racking, one-at-a-time handling, separate cleaning "
        "cycle, distilled-water rinse, immediate lumen flushing, inspection "
        "under magnification** — the care rules carry the marks here.",
        "**TASS** is caused by instrument residue and is prevented by tray "
        "practice — a strong, distinguishing answer.",
        "**Lowest adequate light intensity** to avoid phototoxic "
        "maculopathy.",
        "**Back-up bulb and light source checked** — illumination failure "
        "mid-procedure is an emergency.",
        "**Hands rest on the patient's forehead**; unsupported hands "
        "tremble.",
    ],
    qa=[("What does the ophthalmic microscope tray comprise and how is it "
         "set up?",
         "It comprises the operating microscope with coaxial illumination, "
         "foot control for zoom, focus and X-Y movement, sterile body drapes "
         "and sterilisable handgrips, an assistant's co-observer tube, beam "
         "splitter with camera, monitor and recorder, adjustable eyepieces, "
         "a wide-angle viewing system with inverter for retinal work, "
         "intra-operative OCT where available, and a checked spare bulb and "
         "back-up light source; together with the microinstrument set — "
         "spring-handled Castroviejo and Barraquer needle holders, Colibri "
         "and Bishop-Harmon 0.12 mm forceps, tying forceps with a platform, "
         "Vannas and Westcott spring scissors, micro-spatulas and hooks, "
         "25–30G cannulae, a diamond knife and 9-0 to 11-0 suture on "
         "spatulated needles. Set-up: position the iris plane horizontal; "
         "set eyepieces, interpupillary distance and parfocality **before "
         "scrubbing**; drape the microscope and fit sterile handgrips; "
         "balance and centre it and check the foot controls; adjust the "
         "surgeon's chair and wrist support so the hands rest on the "
         "forehead; set the light to the lowest adequate intensity; and lay "
         "the instruments out in order of use on a magnetic mat."),
        ("What is toxic anterior segment syndrome and how is it prevented?",
         "TASS is an acute, severe, **sterile** inflammation of the anterior "
         "segment following intraocular surgery, caused by toxic residues "
         "carried into the eye on instruments — detergent, endotoxin, "
         "denatured viscoelastic, lens material or preservatives. It is "
         "prevented by tray discipline: flushing all cannulae and handpiece "
         "lumens immediately after use, cleaning ophthalmic instruments in a "
         "dedicated cycle separate from general instruments, rinsing in "
         "distilled or demineralised water, avoiding detergent residue, and "
         "inspecting instruments under magnification before packing.")]))



# ================================================================ 9.9
_TRAYS.append(T(
    "9.9", "Retinal Procedures Tray",
    aka="Vitreoretinal tray · vitrectomy and retinal detachment set",
    lead="Retinal surgery is divided between an **external (scleral) "
         "approach** — buckles and cryotherapy for retinal detachment — and "
         "an **internal approach**, **pars plana vitrectomy**, in which the "
         "vitreous is removed through three tiny sclerotomies and replaced "
         "by fluid, gas or oil. The tray must support **both**, and it "
         "carries the most complex machinery of any ophthalmic set: a "
         "**vitrectomy console, endoillumination, a wide-angle viewing "
         "system and a range of tamponade agents**.",
    uses=["Rhegmatogenous retinal detachment — scleral buckle or vitrectomy",
          "Tractional detachment in proliferative diabetic retinopathy",
          "Vitreous haemorrhage; endophthalmitis requiring vitreous biopsy",
          "Macular hole and epiretinal membrane surgery",
          "Removal of a dropped nucleus or dislocated IOL",
          "Giant retinal tear; proliferative vitreoretinopathy",
          "Intraocular foreign body removal; ocular trauma"],
    plate=PL("Signature instruments",
             [("fine_forceps", "Intraocular micro-forceps"),
              ("strabismus_hook", "Muscle hook — rectus slings"),
              ("iris_scissors", "Fine scissors"),
              ("castroviejo_nh", "Fine needle holder"),
              ("lid_speculum", "Lid speculum")],
             cap="Fig 9.9 — External buckling and internal vitrectomy in "
                 "one tray"),
    groups=[
        G("Base set", [
            ("1", "Basic eye procedures tray", "see 9.1"),
            ("1", "Basic eye muscle tray items", "see 9.3 — for rectus "
             "slings in scleral buckling"),
            ("1", "Microscope tray / platform", "see 9.8"),
        ]),
        G("External (scleral buckle) approach", [
            ("2", "**Muscle hooks (von Graefe, Jameson)**",
             "isolates the rectus muscles and passes traction slings"),
            ("—", "**4-0 silk / Vicryl rectus slings**",
             "rotates the globe to reach the periphery"),
            ("2", "**Scleral depressors (Schepens, Flynn)**",
             "**signature item** — indents the sclera so the peripheral "
             "retina can be seen"),
            ("1", "**Indirect ophthalmoscope with a 20 D / 28 D lens**",
             "**signature item** — locates the retinal break during external "
             "surgery"),
            ("—", "**Scleral buckle materials — silicone bands, sponges, "
                  "tyres and sleeves (assorted widths)**",
             "**signature item** — indents the sclera to relieve vitreous "
             "traction"),
            ("2", "**Buckle-holding forceps and a band/sleeve "
                  "spreader**", ""),
            ("1", "**Scleral tunnel / Watzke sleeve forceps**", ""),
            ("—", "**5-0 non-absorbable (Mersilene / Dacron) mattress "
                  "sutures**",
             "fixes the buckle to the sclera"),
            ("1", "**Cryotherapy probe with console and foot pedal**",
             "**signature item** — freezes around the break to create a "
             "chorioretinal adhesion"),
            ("1", "**Diathermy / marker for the break site**", ""),
            ("1", "**Subretinal fluid drainage needle / cannula**",
             "with a scleral cut-down"),
            ("1", "Callipers and a scleral marker", ""),
        ]),
        G("Pars plana vitrectomy — the internal approach", [
            ("—", "**Vitrectomy console with cutter handpiece (23G, 25G or "
                  "27G) and foot control**",
             "**signature item** — a guillotine cutter that removes vitreous "
             "in tiny bites while infusing to keep the globe formed"),
            ("—", "**Valved trocar cannula system — three sclerotomies "
                  "(infusion, light, instrument)**",
             "**signature item** — placed **3.5–4 mm behind the limbus at "
             "the pars plana**, avoiding lens and retina"),
            ("1", "**Infusion line with balanced salt solution and an "
                  "intraocular pressure control module**", ""),
            ("1", "**Endoilluminator (light pipe) and chandelier "
                  "illumination**",
             "**signature item** — the eye is dark inside; light must be "
             "introduced"),
            ("1", "**Wide-angle viewing system (BIOM) with an image "
                  "inverter**",
             "**signature item** — gives a panoramic fundus view; the "
             "inverter corrects the reversed image"),
            ("1", "Contact lens set (macular, prism) with a lens ring", ""),
            ("2", "**Intraocular micro-forceps — end-gripping, ILM and "
                  "serrated**",
             "peels epiretinal and internal limiting membranes"),
            ("2", "**Intraocular micro-scissors — vertical and horizontal**",
             "segments and delaminates tractional membranes"),
            ("1", "**Membrane scraper / diamond-dusted sweeper and a "
                  "Tano scraper**", ""),
            ("2", "**Backflush / soft-tip extrusion cannula**",
             "aspirates subretinal fluid and blood"),
            ("1", "**Endolaser probe with a laser console**",
             "**signature item** — endophotocoagulation seals breaks and "
             "treats ischaemic retina"),
            ("1", "**Endodiathermy probe**", "marks retinotomies, haemostasis"),
            ("1", "**Fragmatome (phacofragmentation handpiece)**",
             "removes a dropped nucleus"),
            ("1", "Intraocular magnet and foreign-body forceps", ""),
            ("—", "**Vital dyes — indocyanine green, brilliant blue, "
                  "triamcinolone**",
             "**stains the internal limiting membrane and residual "
             "vitreous** so they can be seen and peeled"),
        ]),
        G("Tamponade agents — the defining group", [
            ("—", "**Perfluorocarbon liquid (heavy liquid)**",
             "**signature item** — heavier than water; flattens the retina "
             "intra-operatively and floats a dropped lens forward"),
            ("—", "**Expansile gases — SF₆ and C₃F₈ — with a gas mixing "
                  "and filling set**",
             "**signature item** — provide temporary tamponade; **the "
             "concentration must be correct — over-expansion raises "
             "intraocular pressure catastrophically**"),
            ("—", "**Silicone oil (1000 / 5000 cSt) with an injection and "
                  "extraction system**",
             "long-term tamponade; requires later removal"),
            ("—", "**Air pump / fluid–air exchange facility**", ""),
            ("—", "**Gas-warning wristband and documentation**",
             "**a patient with intraocular gas must not fly or receive "
             "nitrous oxide** — the gas expands"),
        ]),
        G("Closure and accessory", [
            ("—", "**7-0 / 8-0 absorbable suture for sclerotomies and "
                  "conjunctiva**",
             "small-gauge valved ports are often self-sealing"),
            ("2", "Fine needle holders and tying forceps", ""),
            ("1", "Bipolar wet-field cautery", ""),
            ("—", "**Intravitreal antibiotics / antifungals and "
                  "anti-VEGF agents**",
             "endophthalmitis and neovascular disease"),
            ("—", "**Vitreous biopsy syringe and culture bottles**",
             "**undiluted vitreous sample taken before infusion begins**"),
            ("—", "Counted cellulose sponge spears and blades", ""),
            ("—", "**Positioning instructions for the patient**",
             "posture determines where the gas bubble tamponades"),
            ("—", "Eye pad and cartella shield", ""),
        ]),
    ],
    extras=[("Position", "Supine with the head stabilised and the iris "
             "plane horizontal; the microscope with a wide-angle viewing "
             "system positioned over the eye. Surgery is long, so pressure "
             "care and thromboprophylaxis matter."),
            ("Why the pars plana",
             "The sclerotomies are placed **3.5–4 mm behind the limbus** "
             "(3.0–3.5 mm in a pseudophakic eye). This is the **pars plana** "
             "— posterior to the lens and ciliary processes but anterior to "
             "the retina — the only safe corridor into the vitreous "
             "cavity."),
            ("Gas and altitude",
             "Intraocular gas **expands at reduced atmospheric pressure**. "
             "The patient must be given a **warning wristband**, told not to "
             "fly or travel to altitude until the gas has absorbed, and "
             "**nitrous oxide must be avoided** in any subsequent "
             "anaesthetic."),
            ("Complications",
             "Iatrogenic retinal break and detachment, cataract, raised "
             "intraocular pressure or hypotony, vitreous or suprachoroidal "
             "haemorrhage, endophthalmitis, proliferative vitreoretinopathy "
             "with re-detachment, silicone-oil emulsification and keratopathy, "
             "and phototoxic or laser injury to the macula.")],
    side_box={"title": "Three things unique to this tray",
              "lines": ["**Endoillumination** — no other tray needs a light "
                        "source *inside* the organ.",
                        "**A wide-angle viewing system with an image "
                        "inverter** — because the view is optically "
                        "reversed.",
                        "**Tamponade agents** — heavy liquid, expansile gas "
                        "and silicone oil, each with its own handling "
                        "rules."]},
    compare=CMP(
        ["Tamponade", "Density vs water", "Duration", "Key precaution"],
        [["Perfluorocarbon (heavy) liquid", "**Heavier**",
          "Intra-operative only — must be removed",
          "Retained PFCL causes retinal toxicity"],
         ["SF₆ gas", "Lighter (buoyant)", "About 2 weeks",
          "Correct concentration; **no flying, no N₂O**"],
         ["C₃F₈ gas", "Lighter (buoyant)", "6–8 weeks",
          "Longer expansion; strict pressure monitoring"],
         ["Silicone oil", "Lighter (buoyant)", "Months — needs removal",
          "Emulsification, glaucoma, keratopathy"]],
        cap="Table 9.2 — Tamponade agents: the choice determines "
            "post-operative posture and precautions"),
    points=[
        "Divide the answer into the **external (buckle/cryo)** and "
        "**internal (vitrectomy)** approaches — the tray must serve both.",
        "**Scleral depressor + indirect ophthalmoscope + cryoprobe + "
        "silicone buckle with 5-0 Mersilene** are the external signatures.",
        "**Vitrectomy cutter, valved trocar cannulae, endoilluminator, "
        "wide-angle viewing system with inverter, endolaser** are the "
        "internal signatures.",
        "**Sclerotomies at the pars plana, 3.5–4 mm behind the limbus** — "
        "state the figure and the reason.",
        "**Tamponade agents**: heavy liquid (intra-operative), SF₆/C₃F₈ gas, "
        "silicone oil — know Table 9.2.",
        "**Gas warning: no flying and no nitrous oxide** — a guaranteed "
        "mark.",
        "**Vital dyes (ICG, brilliant blue, triamcinolone)** make the "
        "invisible visible.",
        "**Undiluted vitreous biopsy before infusion** in suspected "
        "endophthalmitis.",
    ],
    pitfalls=["Describing vitrectomy but omitting endoillumination and the "
              "viewing system.",
              "Forgetting the tamponade agents, or their precautions.",
              "Not stating the pars plana entry distance.",
              "Omitting the nitrous-oxide and air-travel warnings."],
    qa=[("Describe the retinal procedures tray.",
         "A basic eye tray, muscle tray items and the microscope platform, "
         "plus two systems. **External**: muscle hooks with rectus slings, "
         "Schepens/Flynn scleral depressors, indirect ophthalmoscope with a "
         "20 D lens, silicone buckle bands, sponges, tyres and sleeves with "
         "holding forceps and a spreader, 5-0 Mersilene mattress sutures, a "
         "cryotherapy probe with console, a break marker, a subretinal fluid "
         "drainage cannula, callipers and a scleral marker. **Internal (pars "
         "plana vitrectomy)**: a vitrectomy console with 23–27G cutter and "
         "foot control, valved trocar cannulae for three sclerotomies placed "
         "3.5–4 mm behind the limbus, an infusion line with IOP control, "
         "endoilluminator and chandelier light, a wide-angle viewing system "
         "with image inverter and contact lenses, intraocular micro-forceps "
         "and micro-scissors, membrane scrapers, backflush cannulae, "
         "endolaser and endodiathermy probes, a fragmatome, intraocular "
         "magnet and vital dyes. **Tamponade**: perfluorocarbon heavy liquid, "
         "SF₆ and C₃F₈ with a gas-mixing set, silicone oil with injection and "
         "extraction, a fluid–air exchange facility and a gas-warning "
         "wristband. Plus 7-0/8-0 absorbable closure, fine needle holders, "
         "wet-field cautery, intravitreal drugs, vitreous biopsy syringe and "
         "culture bottles, counted sponge spears and written positioning "
         "instructions."),
        ("Why must a patient with intraocular gas avoid air travel and "
         "nitrous oxide?",
         "Intraocular gas expands when ambient pressure falls, as at "
         "altitude or during air travel, which can raise intraocular "
         "pressure enough to occlude the retinal circulation and cause "
         "irreversible blindness. Nitrous oxide diffuses rapidly into a "
         "closed gas bubble and expands it in the same way, so it must be "
         "avoided in any anaesthetic until the gas has fully absorbed. The "
         "patient is given a warning wristband and written "
         "instructions.")]))



# `P()` substitutes a fresh list when given an empty one, so re-bind the
# accumulated chapters onto the part now that they have all been appended.
EYE["trays"] = _TRAYS
