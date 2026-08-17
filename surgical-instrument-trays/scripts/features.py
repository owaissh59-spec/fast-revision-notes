#!/usr/bin/env python3
"""
features.py -- key-feature text for instrument rows whose "Notes /
rationale" cell would otherwise be blank.

Roughly a quarter of the rows in the content modules are self-evident
accessories that were left without a note. An empty cell looks like an
omission in a printed table, so every one of them is given a short key
feature here: the distinguishing characteristic, or the reason the item is
on that particular tray.

Lookup is by normalised instrument name, so the inline markup used in the
content modules (**bold**, //italic//) does not have to be repeated.
"""
import re
import unicodedata

_MARKUP = re.compile(r"\*\*|//|__|`")


def norm(name):
    """
    Normalise an instrument name for lookup.

    Folds the inline markup used in the content modules and the typographic
    characters that appear in instrument names -- multiplication sign,
    accents, degree sign, en/em dashes -- so keys below can be written in
    plain ASCII.
    """
    s = _MARKUP.sub("", str(name))
    s = (s.replace("\u00d7", "x")          # × multiplication sign
          .replace("\u2013", "-")          # – en dash
          .replace("\u2014", "-")          # — em dash
          .replace("\u2212", "-")          # − minus
          .replace("\u00b0", "")           # ° degree
          .replace("\u2019", "'"))         # ’ apostrophe
    # strip accents: é -> e
    s = "".join(c for c in unicodedata.normalize("NFKD", s)
                if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


FEATURES = {}       # norm(name) -> generic key feature
OVERRIDES = {}      # (tray_no, norm(name)) -> tray-specific key feature


def add(mapping):
    for k, v in mapping.items():
        FEATURES[norm(k)] = v


def add_for(tray_no, mapping):
    """
    Tray-specific text. Seventeen instrument names appear on more than one
    tray, and for some the rationale is genuinely site-specific -- a deep
    Deaver retractor is doing a different job in a hysterectomy than in a
    thoracotomy. Those are registered here and take precedence.
    """
    for k, v in mapping.items():
        OVERRIDES[(str(tray_no), norm(k))] = v


def feature_for(name, tray_no=None):
    """Key feature for an instrument name, preferring a tray-specific one."""
    key = norm(name)
    if tray_no is not None:
        hit = OVERRIDES.get((str(tray_no), key))
        if hit:
            return hit
    return FEATURES.get(key)


# =====================================================================
#  Part I -- General Surgery
# =====================================================================
add({
    # 1.1 Major
    "Suction tubing":
        "Wide-bore, kink-resistant; a spare set is kept because clot blocks "
        "the line",
    "Electrosurgical pencil with holster and tip cleaner":
        "Holster prevents accidental activation; the tip is scraped clean of "
        "eschar to keep cutting efficiency",

    # 1.2 Basic / minor
    "Needle holders, Mayo-Hegar 15 cm":
        "Ring-handled with a ratchet; tungsten-carbide inserts grip the "
        "needle without rotation",
    "Electrosurgical pencil":
        "Hand-controlled cut and coagulate; the workhorse for haemostasis in "
        "small clean wounds",
    "Kidney dish and gallipot":
        "Kidney dish for specimens and used items, gallipot for antiseptic",

    # 1.3 Limited
    "Needle holder, 13 cm":
        "Short pattern to match a shallow field and fine suture",
    "Gauze swabs, counted":
        "Radio-opaque and counted even for the smallest procedure",

    # 1.4 Thyroid
    "Dressing forceps, fine":
        "Serrated, non-toothed; handles tissue without puncturing the "
        "vascular gland capsule",
    "Towel clips":
        "Sharp crossed points securing drapes to the collar incision field",
    "Sponge-holding forceps":
        "Fenestrated jaws holding a gauze ball for skin preparation and "
        "swabbing",
    "Needle holders, 15 cm":
        "Standard length for the shallow neck field",
    "Yankauer suction tip":
        "Rigid bulbous tip for larger volumes, used with the finer Frazier "
        "tip",

    # 1.5 Long instruments
    "Dressing forceps, 25 cm":
        "Extended length so the hand stays outside a deep wound",
    "Tissue forceps, 25 cm, 1x2 teeth":
        "Toothed grip on fascia at depth",
    "Allis forceps, long":
        "Interlocking teeth reaching tissue at the bottom of a deep cavity",
    "Crile / Kelly forceps, 20-24 cm":
        "Standard haemostats in extended lengths for deep vessels",
    "Kocher clamps, long":
        "Crushing 1x2-toothed clamp for deep fascia and specimen pedicles",
    "Deaver retractors, deep and extra-deep":
        "Narrow curved blade giving depth without a wide incision",
    "Richardson retractors, large":
        "Right-angled blade holding the abdominal wall in a thick patient",
    "Needle holders, 25 cm & 30 cm":
        "Allows suturing at the pelvic floor with the hand clear of the "
        "field",
    "Ligature carrier (Deschamps), long":
        "Blunt eyed hook passing a ligature around a deep pedicle",
    "Long staplers and clip appliers":
        "Extended shafts to reach and divide deep structures",
    "Poole suction tip, long":
        "Perforated shield clearing free fluid from a deep cavity",
    "Yankauer suction tip, long":
        "Localised suction at depth",
    "Electrosurgical pencil with extended tip":
        "Reaches the base of a deep wound without arcing to retractors",
    "Head-light and long light cord":
        "Illumination must extend as far as the instruments; theatre lights "
        "will not reach the bottom of a deep cavity",

    # 1.7 Choledochoscopy
    "Sterile drapes for the camera and cable":
        "Keeps the non-sterile camera and cable out of the sterile field",

    # 1.8 Sigmoidoscopy
    "Disposable gloves and apron":
        "The procedure is contaminated and the lavage return can be forceful",
    "Gauze swabs and receiver":
        "Cleans the lens and mucosa; receiver catches faecal return",

    # 1.9 Gastrointestinal
    "Separate specimen and 'dirty' receivers":
        "Keeps enteric contamination away from the clean part of the field",
    "Change of gloves after the enteric stage":
        "Prevents transfer of bowel organisms to the closure",
    "Needle holders, standard and long":
        "Two lengths: standard for the abdominal wall, long for a deep "
        "pelvic anastomosis",
    "Closed suction drain":
        "Detects an early anastomotic leak and prevents a collection",

    # 1.10 Rectal
    "Kocher clamps":
        "Crushing toothed clamp for the pile pedicle and specimen side",
    "Fine dissecting scissors":
        "Precise division in a shallow, narrow and very sensitive field",
    "Fine suction tip (Frazier)":
        "Small calibre with a thumb vent for a confined anal canal",
})

# =====================================================================
#  Part II -- Gynaecologic and Obstetric
# =====================================================================
add({
    # 2.1 D&C
    "Cervical (Littlewood) forceps":
        "Light-grip cervical forceps, less traumatic than a tenaculum",
    "Local / general anaesthetic equipment":
        "Dilatation is painful; anaesthesia also relaxes the cervix",

    # 2.2 Cone
    "Lateral vaginal wall retractors, insulated":
        "Non-conductive, so diathermy current cannot burn the vaginal wall",
    "Cotton-tipped applicators and swabs":
        "Apply acetic acid and iodine and dry the cervix for inspection",
    "Electrosurgical generator with blend/coagulation settings":
        "Blend cuts the cone; coagulation controls the vascular crater",
    "Silver nitrate sticks":
        "Chemical haemostasis of a small persistent bleeding point",

    # 2.3 Laparoscopy
    "Gas cylinder / supply, checked":
        "Contents confirmed before starting; running out mid-case collapses "
        "the pneumoperitoneum",
    "Fibre-optic light cable and xenon/LED source":
        "Cold light; a damaged cable loses fibres and dims the image",
    "Camera head, coupler, control unit and monitor(s)":
        "White-balanced and focused before insertion",
    "Sterile camera and cable drapes":
        "Keeps the non-sterile camera and cable out of the field",
    "Laparoscopic scissors, hook and straight":
        "Hook pattern for a controlled pull-cut, straight for general "
        "division",
    "Knot pusher and pre-tied ligature loops (Endoloop)":
        "Secures a pedicle without intracorporeal knot tying",
    "Clip applier with clips":
        "Rapid vessel and duct control through a 5 mm port",
    "Specimen retrieval bag":
        "Prevents port-site seeding and spillage of cyst contents",
    "Uterine morcellation containment bag":
        "Contains tissue fragments; reduces the risk of disseminating an "
        "unsuspected malignancy",
    "Vascular clamps and suture":
        "For immediate control if a major vessel is injured at entry",
    "Blood cross-matched and available":
        "Entry injury to a great vessel causes sudden heavy loss",

    # 2.4 Abdominal hysterectomy
    "Deaver retractors, deep":
        "Narrow deep blade exposing the pelvic side wall",
    "Needle holders, long 25 cm":
        "Reaches the vaginal vault from an abdominal incision",
    "Ligating clips and appliers":
        "Rapid alternative to ties on the infundibulopelvic pedicle",
    "Long fine scissors and diathermy extension":
        "Division and haemostasis deep in the pelvis",
    "Closed suction drain and specimen container":
        "Drain for the pelvic dead space; uterus labelled and orientated",

    # 2.5 Caesarean
    "Needle holders":
        "Heavy pattern to drive a large round-bodied needle through "
        "myometrium",
    "Large suction reservoirs":
        "Amniotic fluid volume greatly exceeds that of any other operation",
    "Abdominal packs, counted":
        "Radio-opaque; counted before uterine closure",
    "Skin closure - subcuticular suture or staples":
        "Cosmetic closure of a Pfannenstiel incision",

    # 2.6 Vaginal hysterectomy
    "Cervical tenaculum / Littlewood forceps":
        "Initial grip on the cervix before the vulsellum takes over",
    "Zeppelin / Wertheim clamps, long curved":
        "Long curve reaching the cardinal ligament from below",
    "Needle holders, long straight":
        "Complements the angled Heaney holder for vault sutures",
    "Long fine-tipped diathermy extension":
        "Haemostasis at the top of a deep narrow vaginal field",
    "Suction tip, long fine":
        "Clears blood from a tube-like field without obscuring the view",
})

# =====================================================================
#  Part III -- Genitourinary
# =====================================================================
add({
    # 3.1 Vasectomy
    "Gallipot with antiseptic":
        "Scrotal skin preparation",
    "Small drape with a central aperture":
        "Isolates a very small operative field",
    "Scrotal support and dressing":
        "Compression reduces haematoma, the commonest complication",

    # 3.2 Prostatectomy
    "Deaver retractors, extra-deep":
        "The retropubic space is among the deepest fields in surgery",
    "Bladder neck (Denis Browne) retractor":
        "Purpose-shaped blade exposing the bladder neck after enucleation",
    "Long Rochester-Pean clamps":
        "Heavy long clamp for the dorsal venous complex",
    "Diathermy with long extension tip":
        "Reaches the prostatic cavity without arcing to retractors",
    "Continuous bladder irrigation set with warm normal saline":
        "Warm fluid avoids clot formation and bladder spasm",
    "Catheter introducer / stylet and lubricant":
        "Guides a large three-way catheter through a distorted urethra",
    "Urine drainage bags":
        "Large capacity, since irrigation volumes are high",
    "Irrigation fluid on a stand":
        "Gravity feed; bag height sets the irrigation pressure",

    # 3.3 Kidney
    "Vascular suture 4-0/5-0 on a double-armed needle":
        "Non-absorbable monofilament; double-armed for the renal pedicle",
    "Stone scoop and stone spoon":
        "Retrieves fragments and small calculi from the calyces",
    "Self-retaining ring / Bookwalter retractor":
        "Holds the flank exposure open without an assistant",
    "Head-light":
        "The renal pedicle lies deep and high; theatre lights do not reach it",
    "Urinary catheter":
        "Monitors output and decompresses the bladder during pelvic work",
})



# =====================================================================
#  Part IV -- Thoracic
# =====================================================================
add({
    # 4.1 Mediastinoscopy
    "Long insulated suction tip":
        "Insulation prevents current tracking to the great vessels",
    "Fine artery forceps and Adson forceps":
        "Superficial haemostasis and skin handling at the neck incision",
    "Vascular clamps, vascular suture and haemostatic agents":
        "For control if the innominate artery or azygos vein is injured",

    # 4.2 Thoracotomy
    "Bone rasp and bone wax":
        "Rasp smooths the cut rib so it cannot lacerate lung; wax seals "
        "bleeding marrow",
    "Potts-Smith angled vascular scissors":
        "Angled blades to open a pulmonary vessel accurately",
    "Vessel loops and umbilical tapes":
        "Sling and gently occlude hilar structures without clamping",
    "Vascular suture 3-0 to 5-0 double-armed":
        "Non-absorbable monofilament for the pulmonary artery and vein",
    "Deaver retractors, deep":
        "Narrow blade reaching the hilum between spread ribs",
    "Head-light":
        "Directs light into the depth of the chest cavity",
    "Absorbable suture for muscle layers":
        "Closes latissimus dorsi and serratus in layers",
    "Suction source and tubing":
        "Two circuits: one for the field, one for the chest drain",

    # 4.3 Pacemaker
    "Fine vascular dissecting forceps and scissors":
        "Cephalic vein cut-down needs vascular-quality instruments",
    "Heparinised saline flush":
        "Keeps the sheath and lead lumen free of thrombus",
    "Weitlaner / small self-retaining retractor":
        "Holds the pocket open so both hands are free to handle the leads",
    "Army-Navy or Langenbeck retractors":
        "Retracts the pocket edges during generator insertion",
    "Radiolucent operating table and arm-boards":
        "Allows unobstructed fluoroscopic screening of the lead path",
})

# =====================================================================
#  Part V -- Cardiovascular
# =====================================================================
add({
    # 5.1 Vascular
    "Bulldog clamp applier / holder":
        "Applies and removes a spring clip without distorting its jaws",
    "Fine curved Metzenbaum / dissecting scissors":
        "Frees the vessel from its sheath without intimal injury",
    "Graft sizers and calibrators":
        "Matches graft diameter to the native vessel to avoid turbulence",
    "Topical haemostatic agents and fibrin sealant":
        "Controls needle-hole and anastomotic ooze that suture cannot",
    "Fine suture scissors":
        "Cuts 6-0 to 8-0 monofilament cleanly, leaving a short tail",
    "Cross-matched blood and a cell saver":
        "Aortic work loses blood fast; the cell saver returns washed red "
        "cells",
    "Pressure monitoring lines":
        "Invasive arterial pressure guides clamping and unclamping",
    "Closed suction drain":
        "Detects early anastomotic bleeding and prevents a haematoma around "
        "the graft",

    # 5.2 Shunt
    "Graft sizers, calibrators and tunneller":
        "Sizes the conduit and creates its subcutaneous track",
    "Shunt clamps and shunt-securing tapes":
        "Hold the temporary shunt in place without crushing the vessel",
    "Self-retaining ring retractor":
        "Maintains retroperitoneal exposure for a portosystemic shunt",
    "Head-light":
        "The portal vein and IVC lie deep in the retroperitoneum",
    "Fine polypropylene 6-0 to 8-0, double-armed":
        "Non-absorbable monofilament for a 2-4 mm anastomosis",
    "Fine bulldog clamps and micro-clamps":
        "Occlude a radial artery or cephalic vein without crushing it",
    "Tourniquet and arm-board":
        "Positions and exsanguinates the arm for dialysis access",
    "Heparinised saline with fine cannulae":
        "Flushes a small vessel and prevents thrombus at every stage",
    "Pressure monitoring lines and manometer":
        "Portal pressure is measured before and after shunting",
    "Heparin and protamine":
        "Anticoagulation during clamping and its reversal afterwards",
    "Closed suction drains":
        "These patients are coagulopathic; a drain detects early bleeding",

    # 5.3 Cardiac
    "Complete major procedures tray":
        "Provides the general soft-tissue instruments for access and closure",
    "Long instruments tray":
        "The posterior pericardium and mitral annulus lie deep in the chest",
    "ACT (activated clotting time) monitoring":
        "Confirms adequate heparinisation before bypass begins",
    "Radial artery harvest set":
        "Third conduit option; needs fine clips and atraumatic forceps",
    "Annulus debridement / calcium rongeur":
        "Removes annular calcium so the prosthesis seats evenly",
    "Valve holder and rotator with handle":
        "Holds the prosthesis and orientates it within the annulus",
    "Nerve hook and valve tester":
        "Confirms leaflet mobility and competence before closing",
    "Inotropes and vasoactive infusions, prepared":
        "Drawn up in advance; needed the moment bypass is weaned",
    "Cell saver, cross-matched blood, platelets, FFP, cryoprecipitate":
        "Bypass causes a predictable coagulopathy as well as blood loss",
})

# =====================================================================
#  Part VI -- Orthopaedic
# =====================================================================
add({
    # 6.1 Basic ortho
    "Amputation / hand saw":
        "Manual back-up for straight division of a long bone",
    "Bone clamps, serrated":
        "Hold two fragments in reduction while a plate is applied",
    "Drill bits, graded diameters":
        "Matched to screw core diameter; a blunt bit burns bone",
    "Screwdrivers - hexagonal, cruciate, self-retaining":
        "Self-retaining pattern stops the screw dropping into the wound",
    "Lead aprons and thyroid shields for all staff":
        "Fluoroscopy is used repeatedly; protection is mandatory",
    "Closed suction drain":
        "Bone bleeds after fixation; a haematoma invites infection",

    # 6.2 Minor ortho
    "Osteotomes, small (2-8 mm)":
        "Bevelled both sides; splits small cancellous bone",
    "Chisels, small":
        "Bevelled one side; cuts a flat surface on a phalanx or metatarsal",
    "Gouges, small":
        "U-shaped trough for scooping small volumes of graft",
    "Mallet, small":
        "Light controlled blows; a heavy mallet shatters small bones",
    "Bone rongeur, fine (Luer, small)":
        "Nibbles small bites of bone from an exostosis",
    "Bone nibbler / small bone cutter":
        "Divides a phalanx or metatarsal cleanly",
    "Bone curettes, small and angled":
        "Scrapes out a cyst or granulation from a small bone",
    "Small bone rasp / file":
        "Smooths a cut edge so it cannot irritate tendon or skin",
    "Small oscillating saw with fine blades":
        "Precise osteotomy in hallux valgus correction",
    "Small bone-holding forceps":
        "Grips a metacarpal or metatarsal shaft during fixation",
    "Fine reduction forceps":
        "Pointed tips hold small fragments reduced while a wire is passed",
    "Small periosteal elevator (Freer)":
        "Lifts periosteum from a small bone without stripping it widely",
    "Small bone hook and elevator":
        "Manipulates a small fragment into position",
    "Fine (Adson / Gillies) toothed forceps":
        "Fine teeth for skin of the hand and foot",
    "Fine non-toothed forceps":
        "Handles tendon, nerve and vessel atraumatically",
    "Iris and tenotomy scissors, fine":
        "Very fine division of tendon sheath and fascia",
    "Fine curved Metzenbaum scissors":
        "Blunt dissection along tendon and neurovascular planes",
    "Mosquito artery forceps, fine":
        "The principal haemostat in hand and foot surgery",
    "Skin hooks, single and double":
        "Atraumatic retraction of thin dorsal skin",
    "Small self-retaining (Weitlaner) retractor":
        "Holds a short incision open, freeing the assistant",
    "Small Langenbeck / Senn retractors":
        "Hand-held retraction in a shallow field",
    "Fine needle holder":
        "Drives 4-0 to 6-0 needles for tendon and skin repair",
    "Fine suture - absorbable and monofilament":
        "Absorbable to deep layers, monofilament to skin",
    "Mini drill / power driver with fine bits":
        "Drives K-wires and 1.5-2.7 mm screws",
    "Mini depth gauge and screwdriver":
        "Measures a 10-14 mm hole and inserts the matching screw",
    "Interosseous / cerclage wire, fine":
        "Simple fixation where a plate would be too bulky",
    "Bone graft substitute, small volume":
        "Fills a small defect where autograft is not justified",
    "Exsanguinating (Rhys-Davies) roll or Esmarch bandage":
        "Empties the limb of blood before the tourniquet is inflated",
    "Lead protection":
        "Mini C-arm still emits radiation; aprons are worn",
    "Hand table / arm-board":
        "Stable supported surface at the correct working height",
    "Fine suction (Frazier)":
        "Small vented tip that will not draw in a digital nerve",
    "Loupes / magnification":
        "Digital nerves and vessels are 1-2 mm across",
    "Splint / plaster materials":
        "Immobilises the repair immediately at the end of surgery",

    # 6.3 Hip
    "Deep Deaver and Langenbeck retractors":
        "Supplementary hand-held retraction around the acetabulum",
    "Cup impactor and mallet":
        "Seats the acetabular cup fully with controlled blows",
    "Liner inserter and liner impactor":
        "Locks the bearing liner into the metal shell",
    "Stem inserter / introducer and impactor":
        "Drives the femoral stem along the prepared canal axis",
    "Head impactor":
        "Seats the femoral head on the trunnion; the taper must be clean and "
        "dry",
    "Calcar planer / neck trimmer":
        "Levels the femoral neck cut so the stem collar sits flush",
    "Antibiotic prophylaxis within 60 minutes of incision":
        "Periprosthetic infection is catastrophic; timing determines tissue "
        "levels",
    "Pulsatile lavage with warm saline and antiseptic":
        "Cleans the bone bed of debris and marrow before cementing",
    "Leg-length measuring device / callipers":
        "Leg-length discrepancy is a common cause of dissatisfaction and "
        "litigation",
    "Closed suction drain":
        "Decompresses the deep dead space after arthroplasty",

    # 6.4 Arthroscopy
    "Fibre-optic light cable and light source":
        "Cold light; the joint is otherwise completely dark",
    "Camera head, coupler, control unit and monitor":
        "White-balanced before insertion; the operation is done on the screen",
    "Image recorder / printer":
        "Documents findings for the record and for the patient",
    "Sterile camera and cable drapes":
        "Keeps non-sterile equipment out of the field",
    "Anti-fog solution and warm saline for the lens":
        "A fogged lens stops the operation; warming prevents condensation",
    "Inflow and outflow cannulae with taps":
        "Separate circuits maintain distension and clear debris",
    "Suction tubing and collection system":
        "Measured outflow, so fluid balance can be tracked",
    "Blunt trocar and joint distractor":
        "Blunt tip protects cartilage; distraction opens a tight joint",
    "Arthroscopic scissors":
        "Divides a meniscal flap or adhesion under vision",
    "Curettes and rasps, arthroscopic":
        "Prepares a cartilage defect to a stable rim",
    "Compressive dressing and cryotherapy device":
        "Limits haemarthrosis and swelling after portal closure",
    "Wide-bore suction":
        "Clears resected tissue and irrigation fluid quickly",
})



# =====================================================================
#  Part VII -- Neurologic
# =====================================================================
add({
    # 7.1 Craniotomy
    "Major procedures tray items as required":
        "Provides general soft-tissue instruments for scalp and closure",
    "Knife handle No.3 with No.10 / No.15 blades":
        "No.10 for the scalp incision, No.15 for fine work",
    "Small self-retaining (Weitlaner / mastoid) retractor":
        "Holds the scalp and muscle apart, freeing the assistant",
    "Fine mosquito and Crile forceps":
        "Control galeal and muscle bleeding, which is brisk",
    "Power drill with burrs, cutting and diamond":
        "Cutting burr removes bone quickly; diamond burr is safe near dura "
        "and sinus",
    "Bone flap elevator / osteotome":
        "Lifts the flap once the craniotome cut is complete",
    "Rasp and bone curette":
        "Smooths the bone edge and clears the burr-hole rim",
    "Dural scissors (Metzenbaum, fine)":
        "Opens the dura in a controlled line once it is lifted on a hook",
    "Self-retaining brain retractor system (Leyla, Greenberg) with a flexible "
    "arm":
        "Holds a brain spatula at a fixed angle without an assistant's hand "
        "wavering",
    "Nerve hooks, fine":
        "Blunt tips to free arachnoid and small vessels",
    "Brain biopsy needle / cannula":
        "Takes a core of deep lesion through a small cortical opening",
    "Haemostatic agents - oxidised cellulose (Surgicel), gelatin sponge "
    "(Gelfoam), fibrin sealant, thrombin":
        "Achieve haemostasis where bipolar cannot be applied safely to brain",
    "Warm saline irrigation with bulb syringe":
        "Cools the burr, clears debris and prevents cortical drying",
    "Cross-matched blood available":
        "Tumour and aneurysm surgery can bleed suddenly and heavily",
    "Screwdriver and plate bender":
        "Contours and fixes the cranial plates that hold the flap",
    "Absorbable suture to pericranium, galea and muscle":
        "Layered closure restores the scalp's blood supply and strength",
    "Skin staples or non-absorbable suture":
        "Secure scalp closure; the galea holds the tension",
    "Head bandage":
        "Light compression limits a subgaleal collection",

    # 7.2 Laminectomy
    "Deep Langenbeck and Deaver retractors":
        "Supplementary hand-held retraction of deep paraspinal muscle",
    "Laminectomy / duckbill rongeur":
        "Broad bite for removing the spinous process and lamina",
    "Osteotomes and chisels, fine":
        "Controlled removal of facet or osteophyte",
    "Mallet, small":
        "Light taps only; heavy blows transmit force to the cord",
    "Disc (Cushing) rongeurs and disc forceps":
        "Grasp and extract disc material from the disc space",
    "Micro-dissectors and micro-curettes":
        "Separate dura and root from adhesions under magnification",
    "Nerve hook, blunt, fine":
        "Palpates the root and confirms the foramen is decompressed",
    "Epidural probe / Woodson elevator":
        "Explores the epidural space and lifts ligament off dura",
    "Warm saline irrigation":
        "Cools the burr and clears bone dust from the canal",
    "Cross-matched blood available":
        "The epidural venous plexus can bleed briskly",
    "Pedicle awl, probe, sounder and tap":
        "Create and confirm an intraosseous screw track without breaching "
        "the cortex",
    "Screwdriver, rod bender, rod holder, persuader and counter-torque":
        "Contour the rod and seat it without transmitting torque to the spine",
    "Interbody cages (PLIF / TLIF) with inserters and trials":
        "Restore disc height and provide anterior column support",
    "Bone graft - local autograft, iliac crest, allograft or substitute":
        "Provides the biology for fusion; local bone is collected during "
        "decompression",
    "Cage / graft impactor and distractor":
        "Distracts the disc space and seats the cage centrally",
    "Subcutaneous suture and skin staples/suture":
        "Layered closure over a drain; a deep dehiscence risks discitis",
})

# =====================================================================
#  Part VIII -- ENT
# =====================================================================
add({
    # 8.1 Ear
    "Small Langenbeck retractors":
        "Retracts the postauricular incision",
    "Micro-scissors, straight and angled":
        "Divides adhesions and graft material in a 5 mm space",
    "Micro-hooks, blunt and sharp (45, 90)":
        "Palpates and separates ossicles; angled to reach the attic",
    "Mallet, small":
        "Light taps for mastoid gouges; heavy blows risk labyrinthine injury",
    "Bone rongeur, fine":
        "Removes small pieces of mastoid cortex or canal wall",
    "Bone wax":
        "Seals bleeding from cancellous mastoid bone",
    "Fine absorbable and non-absorbable suture":
        "Absorbable to periosteum and muscle, monofilament to skin",
    "Adrenaline-soaked cotton pledgets, gelatin sponge":
        "Vasoconstriction in a canal too small for a diathermy tip",
    "Warm irrigation and lens defogger":
        "Cools the burr; a fogged endoscope stops the operation",
    "Ear dressings, canal packing and a mastoid bandage":
        "Packing supports the graft; the bandage limits a haematoma",
    "Facial nerve monitor electrodes":
        "Warn of proximity to the nerve before it is damaged",

    # 8.2 Nasal
    "Endoscope lens cleaning / anti-fog system":
        "Blood and mucus coat the lens repeatedly during sinus surgery",
    "Septal (D-knife) and Cottle knives":
        "Incise cartilage and separate it from bone at the septal junction",
    "Septal scissors, angled":
        "Divides cartilage and bone deep in the nasal cavity",
    "Mallet, small":
        "Drives guarded osteotomes for controlled nasal osteotomy",
    "Nasal gouges and chisels":
        "Remove a bony spur or deviated vomer",
    "Bone nibbler / nasal rongeur":
        "Trims small bony fragments from the septum and turbinate",
    "Mallet-driven bone punch":
        "Removes bone from the pyriform aperture or frontal recess",
    "Ethmoid forceps, up-biting":
        "Angled upward to reach the ethmoidal roof safely",
    "Fine nasal suction tips (Frazier, Fergusson), with thumb vent":
        "The vent lets the operator control force near the orbit and "
        "cribriform plate",
    "Suction cautery":
        "Suction and coagulation in one instrument, keeping the view clear",
    "Nasal packing - ribbon gauze with paraffin, Merocel, absorbable "
    "haemostatic packs":
        "Tamponade after septal surgery or epistaxis; prevents haematoma",
    "Silver nitrate / cautery sticks":
        "Chemical cautery of an anterior septal bleeding point",
    "External nasal splint and tape":
        "Maintains the new dorsal contour after osteotomy",

    # 8.3 Myringotomy
    "Blunt-ended ear probe":
        "Confirms the incision is patent and the tube is seated",
    "Tube inserter / applicator":
        "Delivers the grommet without dropping it into the canal",
    "Cotton-wool balls and ear wicks":
        "Absorb discharge and hold drops against the drum",
    "Kidney dish and small gallipot":
        "Receives the tiny tubes and holds antiseptic",
    "Suction tubing and trap":
        "A trap catches a grommet that is accidentally aspirated",

    # 8.4 T&A
    "Doughty tongue blade with a tube slot":
        "Slot accommodates the endotracheal tube, keeping the airway safe",
    "Tongue depressors, assorted":
        "Sized to the child; too large obstructs the view",
    "Head-light":
        "Directs light down the open mouth to the tonsillar fossa",
    "Mouth props and lip/dental protection":
        "The gag can chip teeth and bruise lips",
    "Tonsil scissors, curved":
        "Divides the pillar mucosa and the pedicle",
    "Mollison's / Waugh's tonsil pillar retractor":
        "Holds the anterior pillar aside to show the dissection plane",
    "Bipolar / monopolar diathermy with an insulated long tip":
        "Insulation prevents burns to the lip and tongue on the way in",
    "Adenoid curettes, assorted sizes, without cage":
        "Sized to the nasopharynx; used where the cage is not needed",
    "Adenotome (La Force) and adenoid punch forceps":
        "Guillotine pattern that removes and retains the adenoid",
    "Nasopharyngeal mirror and 45 endoscope":
        "The adenoid bed cannot be seen directly",
    "Suction cautery and bipolar forceps, long":
        "Reach the fossa and nasopharynx while clearing blood",
    "Haemostatic agents and adrenaline-soaked swabs":
        "Pressure plus vasoconstriction for diffuse fossa ooze",
    "Cross-matched blood availability for a bleeding tonsil":
        "A secondary bleed can be heavy and the patient hypovolaemic",
    "Laryngoscope, bougie, oral and nasal airways":
        "The airway is shared and blood-soiled; loss of it must be "
        "anticipated",
    "Tracheostomy set available":
        "Final option if the airway cannot be secured from above",
    "Throat pack, if used - counted and its removal documented":
        "Out of sight in the pharynx; if retained it obstructs the airway",

    # 8.5 Tracheostomy
    "Small self-retaining (Weitlaner) retractors":
        "Holds the strap muscles apart, freeing both hands for the trachea",
    "Langenbeck / Army-Navy retractors":
        "Hand-held retraction of the short superficial incision",
    "Kocher clamps":
        "Crushing clamp on the thyroid isthmus before division",
    "Small periosteal / tracheal elevator":
        "Clears pretracheal fascia from the tracheal rings",
    "Keyhole dressing and barrier film":
        "Protects the peristomal skin from secretions",
    "Difficult-airway trolley, laryngoscope, bougie, spare endotracheal tubes":
        "The airway can be lost at the moment the trachea is opened",
    "Self-inflating bag with tracheostomy connector, oxygen and "
    "humidification":
        "A tracheostomy bypasses the nose, so gas must be humidified",
    "Cuff-pressure manometer and 10 mL syringe":
        "Excess cuff pressure causes tracheal mucosal necrosis and stenosis",
    "Rigid bronchoscope available":
        "Clears distal secretions or blood and confirms tube position",
    "Capnography and pulse oximetry":
        "Confirms the tube is in the trachea, not a pretracheal plane",

    # 8.6 Antral puncture
    "Warm sterile normal saline for lavage":
        "Warm fluid is less likely to provoke pain and vasovagal response",
    "Nasal specula, graded (Thudichum, Killian)":
        "Opens the nostril to expose the inferior meatus",
    "Head-light or head-mirror":
        "Illuminates the inferior meatus for accurate trocar placement",
    "Fine nasal suction tips (Frazier)":
        "Clears pus and blood from the nasal cavity",
    "Antral probe / sinus seeker":
        "Confirms the cannula lies within the antrum, not the soft tissues",
    "Silver nitrate / cautery":
        "Controls bleeding from the puncture site",
    "Antibiotics and antral instillation medication":
        "Instilled after lavage once the aspirate has been sent for culture",
})



# =====================================================================
#  Part IX -- Ophthalmic
# =====================================================================
add({
    # 9.1 Basic eye
    "Eye drape with an adhesive aperture":
        "Seals the lashes and lid margin away from the operative field",
    "Knife handle for micro-blades; No.15 blade":
        "Takes the small replaceable blades used on conjunctiva and lid",
    "Iris / tenotomy scissors, fine":
        "Very fine blades for iris and small conjunctival cuts",
    "Suture: 6-0 to 8-0 absorbable (Vicryl) for conjunctiva; 9-0 to 10-0 "
    "nylon for cornea and sclera; 4-0 silk for traction":
        "Calibre falls as the tissue gets finer; traction suture is the "
        "heaviest",
    "Tying forceps and a suture platform":
        "Non-toothed, so 10-0 monofilament is not cut while a knot is tied",
    "Disposable low-temperature cautery pen":
        "Battery cautery for a single small vessel, no generator needed",
    "Fine suction / sponge (cellulose spear) holder":
        "Holds a spear so fluid is wicked, not aspirated with force",
    "Eye pad, cartella shield and tape":
        "The rigid shield stops the patient rubbing and rupturing a wound",

    # 9.2 Lid
    "Entropion / tarsal clamp (Snellen)":
        "Everts and fixes the tarsal plate for a lid-margin rotation",
    "Ptosis clamp and Berke/Putterman clamp":
        "Isolates and holds the levator or Muller's muscle for resection",
    "Skin hooks, fine single and double":
        "Retract thin lid skin without crushing it",
    "Tarsal plate forceps and Erhardt lid clamp":
        "Grip the full thickness of the lid and give haemostasis",
    "Punctum dilator":
        "Opens the punctum before a probe is passed in lid trauma",
    "Westcott spring scissors, curved and blunt":
        "The standard scissors for conjunctiva and lid dissection",
    "Beaver handle with No.64 / 15 micro-blades":
        "Precise incision through skin, tarsus and conjunctiva",
    "Superblade / crescent blade":
        "Lamellar dissection between the lid layers",
    "Tarsal / hard-palate / ear-cartilage graft material":
        "Substitutes for tarsus in posterior lamellar reconstruction",
    "Graft flattening board and marker":
        "Thins and marks a graft to the exact size of the defect",
    "Fine needle holders":
        "Drive 6-0 to 8-0 needles through tarsus and skin",
    "Bipolar / wet-field cautery, fine-tipped":
        "Haemostasis millimetres from the globe, with no current spread",
    "Cellulose sponge spears, counted":
        "Wick blood from the field; countable items on a small tray",
    "Antibiotic ointment, eye pad and shield":
        "Ointment prevents lash adhesion; the shield protects the repair",

    # 9.3 Muscle
    "Steel ruler, millimetre scale":
        "Independent check on the calliper setting",
    "Limbal / corneal marker":
        "Marks the limbus as the reference point for all measurements",
    "Vannas scissors":
        "Very fine straight or curved cuts in muscle capsule",
    "Beaver handle with No.64 / 65 micro-blades":
        "Opens conjunctiva and muscle capsule cleanly",
    "Fine toothed (0.3 / 0.12 mm) forceps":
        "0.3 mm for conjunctiva, 0.12 mm for the muscle insertion",
    "Castroviejo / Barraquer needle holders, fine":
        "Spring-handled; drives a spatulated needle through sclera",
    "6-0 / 7-0 absorbable for conjunctival closure":
        "Absorbable, so no suture removal in a child",
    "Tying forceps and suture platform":
        "Ties 6-0 without cutting or fraying it",
    "Cellulose sponge spears, counted":
        "Keep the field dry at the muscle insertion",
    "Balanced salt solution and irrigating cannula":
        "Irrigates the surface; never plain saline on the ocular surface",
    "Atropine / cycloplegic, antibiotic-steroid ointment":
        "Reduces ciliary spasm and postoperative inflammation",
    "Eye pad and shield":
        "Both eyes may be padded when surgery is bilateral",

    # 9.4 DCR
    "Lacrimal sac retractor / Rollet's rougine":
        "Holds the sac and periosteum aside while bone is removed",
    "Lacrimal / canalicular trephine":
        "Cuts a clean opening through a stenosed canaliculus",
    "Fluorescein and dye disappearance test materials":
        "Confirms the new passage drains before closure",
    "Chalazion / lacrimal sac forceps":
        "Grips and stabilises the sac wall as it is opened",
    "Small bone curettes and a bone rasp":
        "Enlarge and smooth the bony ostium",
    "Suction with a fine tip to clear bone dust":
        "Bone dust obscures the ostium and can seed granuloma",
    "Nasal specula (Thudichum, Killian)":
        "Opens the nasal cavity for the intranasal part of the anastomosis",
    "Microdebrider":
        "Removes nasal mucosa and bone while suctioning, in endonasal DCR",
    "Bayonet forceps and fine nasal suction":
        "Bayonet offset keeps the hand out of the line of sight",
    "Nasal packing":
        "Supports the flaps and controls epistaxis",
    "Fine needle holders and tying forceps":
        "Suture the sac flaps to nasal mucosa with 6-0 to 7-0",
    "Bipolar cautery, fine and bayonet":
        "Controls angular vein bleeding without spread to the orbit",
    "Local anaesthetic with adrenaline; infratrochlear and infraorbital "
    "blocks":
        "Anaesthesia plus vasoconstriction in a very vascular area",
    "Counted sponge spears and gauze":
        "Countable items shared between the eye and nasal fields",
    "Eye pad, shield and nasal dressing":
        "Protects both operative sites",

    # 9.5 Cornea
    "Vannas and Westcott scissors":
        "Fine cuts in conjunctiva and in the corneal periphery",
    "Corneal dissector and Paufique knife":
        "Develops a lamellar plane at a set depth in the stroma",
    "Anterior chamber (Rycroft) cannula with BSS":
        "Reforms the chamber and washes out blood and debris",
    "Sinskey and Kuglen hooks":
        "Manipulate iris and graft edge without toothed forceps",
    "Castroviejo / Barraquer needle holder, fine, non-locking":
        "Non-locking, so a 10-0 needle can be released instantly",
    "Tying forceps with a suture platform":
        "Ties 10-0 nylon and buries the knot without cutting it",
    "Suture-cutting scissors, fine":
        "Trims 10-0 ends short so they do not irritate the lid",
    "Sterile Teflon cutting block and storage vial":
        "Concave block supports the donor button while it is punched",
    "Corneal storage / transport container":
        "Keeps the donor tissue in medium until the moment it is used",
    "Counted cellulose sponge spears":
        "Countable; used to dry the graft-host junction",
    "Eye pad and cartella shield":
        "A full-thickness wound must be protected from any pressure",

    # 9.6 Cataract
    "Beaver handle with micro-blades":
        "Alternative to a keratome for the paracentesis",
    "Conjunctival and corneal 0.12 mm forceps":
        "Stabilise the globe and handle the wound edge",
    "Calliper / incision gauge":
        "Confirms the incision matches the IOL cartridge size",
    "Vannas / capsulotomy micro-scissors":
        "Rescues a radial capsular tear or completes a rhexis",
    "Bimanual I/A set":
        "Separates irrigation from aspiration for safer subincisional cortex "
        "removal",
    "Iris repositor, de Wecker scissors and iris forceps":
        "Manage iris prolapse and perform an iridectomy if needed",
    "Counted cellulose sponge spears":
        "Dry the wound to test for a leak",
    "Eye pad, cartella shield and post-operative drops":
        "Shield protects a self-sealing wound overnight",

    # 9.7 Glaucoma
    "Beaver handle with No.64 / 69 blades":
        "Outlines the scleral flap at half-thickness",
    "Tenon's dissecting scissors and Tenon's forceps":
        "Separate Tenon's layer cleanly, which determines bleb quality",
    "Sinskey hook":
        "Confirms the sclerostomy is patent and repositions iris",
    "Glaucoma drainage device - Ahmed, Baerveldt or Molteno - with its plate "
    "and tube":
        "Diverts aqueous to an equatorial plate; used when trabeculectomy has "
        "failed",
    "Tube-trimming scissors and a tube introducer":
        "Cuts the tube bevel-up to the correct intracameral length",
    "MIGS implants - trabecular micro-bypass stents, with injectors":
        "Bypass the trabecular meshwork with minimal conjunctival trauma",
    "Cyclophotocoagulation / cyclocryotherapy probe":
        "Reduces aqueous production by ablating ciliary epithelium",
    "Non-absorbable 8-0 / 9-0 suture to fix the plate":
        "Anchors the plate to sclera so it cannot migrate",
    "Castroviejo needle holder, fine":
        "Places 10-0 releasable sutures in the scleral flap",
    "Counted cellulose sponge spears":
        "Also used to deliver mitomycin C; counted separately as cytotoxic",
    "Eye pad and cartella shield":
        "Protects a thin-walled bleb from pressure",

    # 9.8 Microscope
    "Sterilisable handgrips / knobs":
        "Let the surgeon reposition the microscope without breaking asepsis",
    "Assistant's binocular (co-observer) tube":
        "Gives the assistant the same stereoscopic view",
    "Slit illuminator and, for retinal work, a wide-angle viewing system "
    "(BIOM) with an inverter":
        "Slit beam shows depth; the inverter corrects the reversed fundus "
        "image",
    "Spring-handled (non-ratcheted) needle holders - Castroviejo, Barraquer":
        "No ratchet, so the needle is released by relaxing the fingers alone",
    "Colibri and Bishop-Harmon 0.12 mm forceps":
        "Teeth just visible to the naked eye; grip cornea without crushing",
    "Tying forceps with a suture platform":
        "Flat platform lets a knot be tied against it under magnification",
    "Vannas and Westcott spring scissors":
        "Spring handles give millimetre-scale control",
    "Micro-spatulas, iris repositor, Sinskey and Kuglen hooks":
        "Blunt manipulators for iris, capsule and graft edges",
    "Micro-cannulae, 25G-30G, with syringes":
        "Deliver viscoelastic, dye or drug into the anterior chamber",
    "Suture 9-0, 10-0 and 11-0 monofilament on spatulated needles":
        "Spatulated cross-section travels between lamellae without "
        "perforating",
    "Magnetic instrument mat / rack":
        "Holds instruments tip-up and in order of use, within a short reach",
    "Handled one at a time, by the handle, never the tip":
        "A bent or burred tip is unusable and cannot be repaired",
    "Ultrasonic cleaning avoided for cemented diamond knives and delicate "
    "optics":
        "Cavitation loosens cement and damages coatings",
    "Counted - sponge spears, blades, cannulae, IOLs and capsular rings":
        "All are small and easily lost in the drapes",
    "Position the patient with the iris plane horizontal":
        "The microscope looks straight into the eye; an oblique view distorts "
        "depth",
    "Set eyepieces, interpupillary distance and parfocality before scrubbing":
        "Cannot be adjusted once gloved; wrong settings cause eye strain and "
        "loss of stereopsis",
    "Drape the microscope and attach sterile handgrips":
        "The microscope hangs directly over the open eye",
    "Balance and centre the microscope over the eye; check the X-Y and focus "
    "foot controls":
        "An unbalanced head drifts during surgery",
    "Lay out instruments in order of use on a magnetic mat within a small "
    "hand excursion":
        "Long reaches break the hand support and cause tremor",
    "Confirm back-up illumination and a spare handpiece":
        "Loss of light or a failed handpiece mid-procedure is an emergency",

    # 9.9 Retina
    "Buckle-holding forceps and a band/sleeve spreader":
        "Position the silicone band and open the sleeve to lock it",
    "Scleral tunnel / Watzke sleeve forceps":
        "Passes and secures the band beneath the rectus muscles",
    "Diathermy / marker for the break site":
        "Marks the sclera over the retinal break located by indentation",
    "Callipers and a scleral marker":
        "Measure the distance of the break from the limbus",
    "Infusion line with balanced salt solution and an intraocular pressure "
    "control module":
        "Keeps the globe formed as vitreous is removed; prevents collapse",
    "Contact lens set (macular, prism) with a lens ring":
        "High-magnification view of the macula for membrane peeling",
    "Membrane scraper / diamond-dusted sweeper and a Tano scraper":
        "Raise an edge on the internal limiting membrane so it can be grasped",
    "Intraocular magnet and foreign-body forceps":
        "Retrieve a metallic or non-magnetic intraocular foreign body",
    "Air pump / fluid-air exchange facility":
        "Exchanges fluid for air before gas or oil tamponade",
    "Fine needle holders and tying forceps":
        "Close sclerotomies and conjunctiva with 7-0 to 8-0",
    "Bipolar wet-field cautery":
        "Haemostasis at the sclerotomy without charring sclera",
    "Counted cellulose sponge spears and blades":
        "Small countable items on a long, complex procedure",
    "Eye pad and cartella shield":
        "Protects the eye while gas tamponade is in place",
})

# =====================================================================
#  Part X -- Paediatric
# =====================================================================
add({
    # 10.1 Paediatric major
    "Suture scissors":
        "Kept separate so tissue scissors are never blunted on suture",
    "Dressing forceps, fine":
        "Serrated non-toothed; handles friable neonatal tissue",
    "Non-toothed fine forceps":
        "Atraumatic handling of bowel, vessel and ureter",
    "Allis forceps, small":
        "Grips tissue to be excised, on a reduced scale",
    "Towel clips, small":
        "Light clips that will not tear thin neonatal drapes or skin",
    "Sponge-holding forceps, small":
        "Skin preparation over a small surface area",
    "Crile forceps, small 12-14 cm":
        "Secondary haemostat; the mosquito is the workhorse",
    "Senn and small Langenbeck retractors":
        "Shallow-field retraction sized to a neonatal wound",
    "Army-Navy retractors, small":
        "Double-ended, two blade depths in one instrument",
    "Skin hooks, fine":
        "Retract thin skin without crushing it",
    "Small Deaver retractors":
        "Narrow curved blade for a small deep cavity",
    "Head-light":
        "A small deep wound admits very little theatre light",
    "Needle holders, fine 13-15 cm":
        "Sized to 4-0 to 7-0 needles; a heavy holder crushes fine needles",
    "Fine vascular suture 6-0 to 8-0":
        "Non-absorbable monofilament for millimetre-wide vessels",
    "Small Yankauer tip":
        "Larger-volume suction, used with the finer vented Frazier",
    "Small kidney dish, gallipots and specimen containers":
        "Small volumes; specimens are often tiny and must not be lost",
    "Fine feeding tubes, infant catheters and small drains":
        "Sized in French gauge to the child; adult sizes will not pass",
    "Warmed irrigation fluid, warmed intravenous fluids and a fluid warmer":
        "Cold fluid poured into a body cavity causes rapid core cooling",
    "Raised theatre ambient temperature (24-26 C for neonates)":
        "The single most effective measure against intraoperative hypothermia",
    "Temperature probe and continuous core temperature monitoring":
        "Hypothermia develops within minutes and must be detected early",
    "Neonatal resuscitation equipment":
        "Sized airway, bag and drugs, checked before the incision",

    # 10.2 Paediatric minor
    "Knife handle No.3 with No.15 blade":
        "Small curved blade for a short precise incision",
    "Small Mayo scissors, curved":
        "Divides tougher tissue such as the external oblique aponeurosis",
    "Fine dressing forceps":
        "Non-toothed handling of the sac and cord structures",
    "Small towel clips":
        "Secure a small drape without tearing infant skin",
    "Small sponge-holding forceps":
        "Skin preparation of a small field",
    "Mosquito forceps, curved - the principal haemostat":
        "Fine tip suits vessels under a millimetre across",
    "Crile forceps, small":
        "Slightly larger vessels in the inguinal canal",
    "Small Kocher clamps":
        "Crushing grip on aponeurosis during closure",
    "Small Langenbeck retractors":
        "Hand-held retraction of the inguinal incision",
    "Army-Navy retractors, small":
        "Two blade depths for a shallow wound",
    "Skin hooks, fine":
        "Atraumatic retraction of thin skin edges",
    "Small Weitlaner self-retaining retractor":
        "Holds the canal open, freeing the assistant's hands",
    "Needle holders, fine 13 cm":
        "Matched to 4-0 to 6-0 needles",
    "Orchidopexy items - fine non-toothed forceps, small Langenbeck "
    "retractors and a Dartos-pouch dissector":
        "Creates a sub-Dartos pouch and handles the 1 mm vas atraumatically",
    "Small drains, infant feeding tubes and catheters":
        "Sized to the child; used for drainage and bladder emptying",
    "Fine vented suction (Frazier)":
        "The thumb vent limits force near the vas and testicular vessels",
    "Correctly sized paediatric return electrode":
        "An adult pad on a small child gives inadequate contact area and "
        "risks a burn",
    "Small radio-opaque swabs, counted, with a weighing scale":
        "Swabs are weighed because blood volume is only about 80 mL/kg",
    "Small kidney dish, gallipot and specimen containers":
        "Small volumes matched to a small field",

    # 10.3 Paediatric GI
    "Fine needle holders 13 cm and a micro (Castroviejo) needle holder":
        "The micro holder drives 6-0 and 7-0 needles for a 5 mm anastomosis",
    "Fine curved and Potts-Smith angled scissors":
        "Angled blades open a small bowel end or duct accurately",
    "Small self-retaining anal retractor":
        "Exposes the anal canal for a pull-through anastomosis",
    "Stoma appliances, paediatric, with a marking pen":
        "Sited before incision, away from creases and the costal margin",
    "Small warm moist packs and drapes to isolate the bowel":
        "Warm and moist, because exposed neonatal bowel loses heat and fluid "
        "fast",
    "Dedicated fine suction tip for enteric content":
        "Kept separate from the clean suction to limit contamination",
    "Separate specimen and 'dirty' receivers":
        "Prevents enteric organisms reaching the clean part of the field",
    "Change of gloves after the enteric stage":
        "Removes bowel organisms before the abdomen is closed",
    "Continuous core temperature monitoring":
        "An open abdomen cools a neonate within minutes",
    "Volumetric pumps and syringe drivers; fluids in mL/kg":
        "Every fluid is weight-calculated; a free-flowing line can overload",
    "Glucose monitoring and dextrose infusion":
        "Neonates have minimal glycogen reserve and become hypoglycaemic fast",
    "Neonatal resuscitation equipment and a transport incubator":
        "The child must be moved back to intensive care still warm",
})



# ---------------------------------------------------------------------
#  House style
# ---------------------------------------------------------------------
# The notes column reads as a lower-case fragment continuing the
# instrument name ("heavy tissue, fascia"), not as a sentence. Fold the
# leading capital of the features above to match, leaving acronyms and
# proper nouns alone.
_KEEP_CAPITAL = {
    "Bowie", "Doyen", "Kocher", "Kelly", "Crile", "Allis", "Babcock",
    "DeBakey", "Satinsky", "Fogarty", "Randall", "Bakes", "Heaney",
    "Balfour", "Deaver", "Richardson", "Weitlaner", "Finochietto",
    "Yankauer", "Poole", "Frazier", "Castroviejo", "Westcott", "Vannas",
    "Colibri", "Sinskey", "Utrata", "Barraquer", "Desmarres", "Jaeger",
    "Meyhoefer", "Bowman", "Lichtwitz", "Trousseau", "Boyle", "Draffin",
    "Eves", "Blakesley", "Freer", "Cobb", "Kerrison", "Penfield", "Raney",
    "Hudson", "Hohmann", "Charnley", "Millin", "Freyer", "Goodsall",
    "Wilson", "Word", "Mayo", "Metzenbaum", "Adson", "Senn", "Gigli",
    "Payr", "Mixter", "Schnidt", "Backhaus", "Graefe", "Jameson", "Green",
    "Tenon", "Descemet", "Ahmed", "Baerveldt", "Molteno", "Schepens",
    "Tano", "Busin", "Malyugin", "Simcoe", "Ramstedt", "Benson", "Noblett",
    "Hirschsprung", "Wrigley", "Bakri", "Lynch", "Auvard", "Sims", "Graves",
    "Hegar", "Littlewood", "Zeppelin", "Wertheim", "Duval", "Sarot",
    "Javid", "Pruitt", "Lebsche", "Leksell", "Love", "Scoville", "Taylor",
    "Beckman", "Meyerding", "Gelpi", "Cushing", "Leyla", "Greenberg",
    "Rhoton", "Mayfield", "Killian", "Thudichum", "Cottle", "Ballenger",
    "Jansen", "Middleton", "Tilley", "Stammberger", "Kuhn", "Bolger",
    "Hurd", "Negus", "Birkett", "Rollet", "Traquair", "Citelli", "Hajek",
    "Crawford", "Lester", "Jones", "Nettleship", "Kogan", "Monsel",
    "Sturmdorf", "Lugol", "Schiller", "Hulka", "Filshie", "Falope",
    "Spackman", "Rubin", "Hasson", "Veress", "Endoloop", "Ologen",
    "Watzke", "Flynn", "Barron", "Beaver", "Paufique", "Rycroft", "Kuglen",
    "Wecker", "Elschnig", "Bishop", "Harmon", "Weck", "Optisol", "Eusol",
    "Herrick", "Guyon", "Gil", "Vernet", "Bookwalter", "Judd", "Mason",
    "Denis", "Browne", "Langenbeck", "Volkmann", "Lane", "Fergusson",
    "Lowman", "Verbrugge", "Trethowan", "Bristow", "Farabeuf", "Liston",
    "Horsley", "Luer", "Esmarch", "Rhys", "Davies", "Steinmann",
    "Kirschner", "Deschamps", "Ochsner", "Halsted", "Rochester", "Pean",
    "Lahey", "Duplay", "Teale", "Schroeder", "Hawkin", "Ambler", "Goodell",
    "Novak", "Pipelle", "Kehr", "Desjardins", "Dormia", "Eisenhammer",
    "Parks", "Hill", "Ferguson", "Lockhart", "Mummery", "Malecot",
    "Fisher", "Blohmke", "Thomson", "Clair", "Force", "Laborde", "Kehrer",
    "Snellen", "Berke", "Putterman", "Erhardt", "Stevens", "Gillies",
    "Doughty", "Mollison", "Waugh", "Lloyd", "Trendelenburg", "Pfannenstiel",
    "Seldinger", "Seidel", "Placido", "Dacron", "Teflon", "Merocel",
    "Surgicel", "Gelfoam", "Vicryl", "Plastibell", "Mogen", "Gomco",
    "Bard", "Parker", "Sengstaken", "Warren", "Kestenbaum", "Alexander",
    "Matson", "Lees", "Pennington", "Ankeney", "Cooley", "Dietrich",
    "Potts", "Smith", "Gerald", "Beckman", "Woodson", "Tuohy",
}


def _fold(text):
    if not text:
        return text
    first = text.split(" ", 1)[0].strip(",;:.")
    if len(first) > 1 and first.isupper():    # acronym: ACT, MIGS, CO2
        return text
    if first.rstrip("'s") in _KEEP_CAPITAL or first in _KEEP_CAPITAL:
        return text
    if len(first) > 1 and first[0].isupper() and not first[1:].islower():
        return text                           # CamelCase / mixed, e.g. DeBakey
    return text[0].lower() + text[1:]



# ---------------------------------------------------------------------
#  Shared names: generic text, then tray-specific where the site matters
# ---------------------------------------------------------------------
add({
    # these appear on several trays -- keep the wording site-neutral
    "Head-light":
        "Directs light into the depth of the wound; theatre lights do not "
        "reach the bottom of a deep cavity",
    "Closed suction drain":
        "Drains the dead space and gives early warning of bleeding or a leak",
    "Mallet, small":
        "Light controlled blows to drive an osteotome, chisel or impactor",
    "Deaver retractors, deep":
        "Narrow curved blade giving depth without widening the incision",
    "Cross-matched blood available":
        "Confirmed available before starting, because loss can be sudden",
    "Small Langenbeck retractors":
        "Hand-held right-angled blade for a short superficial incision",
    "Dressing forceps, fine":
        "Serrated non-toothed jaws; handles tissue without puncturing it",
    "Suture scissors":
        "Kept separate so tissue scissors are never blunted on suture",
    "Army-Navy retractors, small":
        "Double-ended, giving two blade depths in one instrument",
    "Sterile camera and cable drapes":
        "Keeps the non-sterile camera and light cable out of the field",
    "Gauze swabs, counted":
        "Radio-opaque and counted, however small the procedure",
    "Counted cellulose sponge spears":
        "Wick fluid from a millimetre-scale field; countable items",
    "Cellulose sponge spears, counted":
        "Wick fluid from a millimetre-scale field; countable items",
    "Eye pad and cartella shield":
        "The rigid shield stops the patient rubbing and reopening the wound",
    "Fine needle holders and tying forceps":
        "Spring-handled pair for placing and tying microsurgical suture",
    "Tying forceps with a suture platform":
        "Flat platform lets a knot be tied against it without cutting the "
        "suture",
})

add_for("1.10", {
    "Kocher clamps":
        "crushing toothed clamp on the pile pedicle and specimen side",
    "Fine suction tip (Frazier)":
        "small calibre with a thumb vent for the confined anal canal",
})
add_for("8.5", {
    "Kocher clamps":
        "crushing clamp on the thyroid isthmus before it is divided",
    "Small Langenbeck retractors":
        "retracts the short transverse pretracheal incision",
})
add_for("4.2", {
    "Deaver retractors, deep":
        "narrow blade reaching the pulmonary hilum between spread ribs",
    "Head-light":
        "directs light into the depth of the chest cavity",
})
add_for("2.4", {
    "Deaver retractors, deep":
        "narrow deep blade exposing the pelvic side wall",
})
add_for("3.3", {
    "Deaver retractors, deep":
        "reaches the renal pedicle, which lies deep and high in the flank",
    "Head-light":
        "the renal pedicle lies deep and high; theatre lights do not reach it",
})
add_for("6.2", {
    "Mallet, small":
        "light controlled blows; a heavy mallet shatters small bones",
})
add_for("7.2", {
    "Mallet, small":
        "light taps only; heavy blows transmit force to the cord",
})
add_for("8.1", {
    "Mallet, small":
        "light taps for mastoid gouges; heavy blows risk labyrinthine injury",
    "Small Langenbeck retractors":
        "retracts the postauricular incision",
})
add_for("8.2", {
    "Mallet, small":
        "drives guarded osteotomes for a controlled nasal osteotomy",
})
add_for("1.4", {
    "Dressing forceps, fine":
        "handles tissue without puncturing the vascular thyroid capsule",
})
add_for("7.1", {
    "Cross-matched blood available":
        "tumour and aneurysm surgery can bleed suddenly and heavily",
})
add_for("7.2", {
    "Cross-matched blood available":
        "the epidural venous plexus can bleed briskly",
})
add_for("1.9", {
    "Closed suction drain":
        "detects an early anastomotic leak and prevents a collection",
})
add_for("6.3", {
    "Closed suction drain":
        "decompresses the deep dead space after arthroplasty",
})
add_for("6.1", {
    "Closed suction drain":
        "bone bleeds after fixation, and a haematoma invites infection",
})
add_for("5.1", {
    "Closed suction drain":
        "detects anastomotic bleeding and prevents a haematoma around the "
        "graft",
})

FEATURES = {k: _fold(v) for k, v in FEATURES.items()}
OVERRIDES = {k: _fold(v) for k, v in OVERRIDES.items()}
