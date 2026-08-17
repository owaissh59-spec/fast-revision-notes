#!/usr/bin/env python3
"""Part II -- Gynaecologic and Obstetric Trays."""
from schema import T, P, PL, DP, FIG, G, CMP

GYN = P(
    "II", "Gynaecologic and Obstetric Trays",
    "D&C · Cervical cone · Laparoscopy · Abdominal hysterectomy · "
    "Caesarean section · Vaginal hysterectomy",
    intro="Gynaecological trays divide naturally into **vaginal-route** sets "
          "(D&C, cone biopsy, vaginal hysterectomy) and **abdominal-route** "
          "sets (laparoscopy, abdominal hysterectomy, caesarean section). "
          "Vaginal sets are dominated by **specula, tenaculums, dilators and "
          "curettes**; abdominal sets are major trays with additions for the "
          "uterine pedicles and the vaginal vault.",
    trays=[

        # ============================================================ 2.1
        T("2.1", "Dilatation of the Cervix and Curettage of the Uterus "
                 "(D&C) Tray",
          aka="D&C tray · dilatation and curettage set",
          lead="**D&C** consists of graduated dilatation of the cervical "
               "canal followed by systematic curettage of the endometrial "
               "cavity. The tray is small, entirely vaginal, and is the "
               "**reference set for all vaginal gynaecological "
               "procedures** — cone biopsy, evacuation, hysteroscopy and "
               "vaginal hysterectomy are all built on it.",
          uses=["Diagnostic curettage for abnormal uterine bleeding",
                "Evacuation of retained products of conception; missed or "
                "incomplete miscarriage",
                "Endometrial sampling for suspected malignancy",
                "Removal of an endometrial polyp or small submucous fibroid",
                "Cervical stenosis — therapeutic dilatation",
                "As the base set for hysteroscopy and cone biopsy"],
          plate=PL("Signature instruments",
                   [("graves_speculum", "Graves bivalve speculum"),
                    ("sims_speculum", "Sims speculum"),
                    ("tenaculum", "Uterine tenaculum / vulsellum"),
                    ("hegar_set", "Hegar dilators, graduated"),
                    ("uterine_curette_sharp", "Uterine curette, sharp"),
                    ("uterine_sound", "Uterine sound")],
                   cap="Fig 2.1 — Expose, steady, sound, dilate, curette"),
          groups=[
              G("Exposure of the cervix", [
                  ("1", "Graves (or Cusco) bivalve self-retaining speculum",
                   "opens the vagina and holds itself"),
                  ("1", "Sims speculum, double-ended",
                   "posterior vaginal wall retraction"),
                  ("1", "Anterior vaginal wall retractor / Auvard weighted "
                   "speculum", "weighted blade retracts posteriorly"),
                  ("2", "Sponge-holding forceps",
                   "antiseptic preparation and swabbing"),
              ]),
              G("Steadying the cervix and uterus", [
                  ("2", "Vulsellum forceps (Duplay / Teale)",
                   "grasp the cervix atraumatically"),
                  ("1", "Single-tooth uterine tenaculum (Schroeder)",
                   "**signature item** — traction to straighten the "
                   "uterocervical angle"),
                  ("2", "Allis forceps", "cervical lip"),
                  ("1", "Cervical (Littlewood) forceps", ""),
              ]),
              G("Sounding and dilatation", [
                  ("1", "Uterine sound (graduated)",
                   "measures cavity depth and direction — normal ≈ 6–8 cm"),
                  ("1", "Set of Hegar dilators, 5–20 mm",
                   "**signature item** — double-ended, graduated; passed in "
                   "ascending order"),
                  ("1", "Set of Hawkin-Ambler dilators",
                   "alternative pattern with handles"),
                  ("1", "Cervical dilator (Goodell)",
                   "screw-action dilator, where used"),
              ]),
              G("Curettage and evacuation", [
                  ("2", "Uterine curette, sharp, small & large",
                   "**signature item** — systematic endometrial curettage"),
                  ("2", "Uterine curette, blunt",
                   "safer in the pregnant or soft uterus"),
                  ("1", "Flushing curette", "irrigating pattern"),
                  ("2", "Ovum (sponge) forceps",
                   "removal of retained products"),
                  ("1", "Suction curette with cannulae and tubing",
                   "suction evacuation — safer than sharp curettage in "
                   "pregnancy"),
                  ("1", "Endometrial biopsy curette (Pipelle / Novak)",
                   "targeted sampling"),
              ]),
              G("Accessory", [
                  ("1", "Kidney dish and gallipot",
                   "antiseptic and specimens"),
                  ("—", "Gauze swabs, counted", "radio-opaque"),
                  ("—", "Specimen containers with formalin",
                   "labelled; separate endocervical and endometrial "
                   "samples"),
                  ("—", "Urinary catheter", "bladder emptied before starting"),
                  ("1", "Needle holder with suture",
                   "cervical tear repair if needed"),
                  ("—", "Local / general anaesthetic equipment", ""),
              ]),
          ],
          extras=[("Position", "Lithotomy, buttocks at the table edge, "
                   "under anaesthesia; bladder emptied first."),
                  ("Sequence", "Examine bimanually to determine uterine "
                   "size and version → expose and clean the cervix → grasp "
                   "with vulsellum/tenaculum → **sound the cavity** → "
                   "dilate progressively with Hegar dilators → curette "
                   "systematically (anterior, posterior, lateral walls, "
                   "then fundus and cornua) → inspect and send specimens."),
                  ("Complications",
                   "Uterine perforation (commonest), cervical tear, "
                   "haemorrhage, infection, Asherman's syndrome from "
                   "over-vigorous curettage, and false passage.")],
          side_box={"title": "Why sound before dilating",
                    "lines": ["The **sound** establishes the depth and the "
                              "direction of the uterine axis.",
                              "Dilating without knowing the direction is "
                              "the commonest cause of **perforation**.",
                              "Dilators are passed in **ascending order**, "
                              "never skipping sizes."]},
          points=[
              "The four signature items are **speculum, tenaculum, Hegar "
              "dilators, curette** — name them in that order of use.",
              "**Sound the uterus before dilating** — the single most "
              "examined safety point.",
              "In **pregnancy** prefer **blunt curette or suction "
              "evacuation**; sharp curettage risks perforation and "
              "Asherman's syndrome.",
              "**Perforation is the commonest complication**; the uterus is "
              "softest at the fundus.",
              "Hegar dilators are **double-ended and graduated** and are "
              "used in ascending order.",
          ],
          qa=[("List the instruments in a D&C tray and the order in which "
               "they are used.",
               "Graves bivalve speculum, Sims speculum and Auvard weighted "
               "speculum for exposure with sponge holders; vulsellum and "
               "single-tooth uterine tenaculum to steady the cervix; a "
               "graduated uterine sound; a set of Hegar dilators 5–20 mm; "
               "sharp and blunt uterine curettes, ovum forceps and a "
               "suction curette; plus kidney dish, counted swabs, labelled "
               "formalin containers and a catheter. Order of use: expose → "
               "clean → grasp cervix → sound → dilate → curette → "
               "specimens."),
              ("What is the commonest complication of D&C and how is it "
               "avoided?",
               "Uterine perforation. It is avoided by bimanual examination "
               "to establish uterine size and version, sounding the cavity "
               "before dilatation, dilating gradually in ascending order "
               "without force, and using a blunt curette or suction "
               "evacuation in the soft pregnant uterus.")]),

        # ============================================================ 2.2
        T("2.2", "Cervical Cone Tray",
          aka="Cone biopsy tray · conisation of the cervix set",
          lead="**Cone biopsy (conisation)** excises a cone of cervical "
               "tissue with its apex in the endocervical canal, both to "
               "diagnose and to treat cervical intraepithelial neoplasia. "
               "The tray is a D&C tray plus the means to **define the "
               "lesion, excise a cone and control a very vascular cut "
               "surface**.",
          uses=["Diagnosis and treatment of CIN 2/3 and adenocarcinoma "
                "in situ",
                "Unsatisfactory colposcopy or cytology–histology mismatch",
                "Suspected microinvasive carcinoma requiring assessment of "
                "depth",
                "Lesion extending into the endocervical canal",
                "LLETZ / LEEP as the electrosurgical equivalent"],
          plate=PL("Signature instruments",
                   [("scalpel_11", "No.11 blade — cold-knife cone"),
                    ("tenaculum", "Cervical tenaculum / vulsellum"),
                    ("uterine_curette_sharp", "Endocervical curette"),
                    ("hegar_set", "Hegar dilators"),
                    ("graves_speculum", "Speculum with insulated blades")],
                   cap="Fig 2.2 — Excision of a cone with haemostatic "
                       "control"),
          groups=[
              G("Base set", [
                  ("1", "Complete D&C tray",
                   "see 2.1 — dilatation and curettage complete the "
                   "procedure"),
              ]),
              G("Exposure and lesion definition", [
                  ("1", "Insulated / non-conductive vaginal speculum",
                   "**essential** if electrosurgery is used — prevents "
                   "vaginal burns"),
                  ("1", "Lateral vaginal wall retractors, insulated", ""),
                  ("1", "Colposcope", "defines the transformation zone"),
                  ("—", "Acetic acid 3–5 % and Lugol's iodine "
                   "(Schiller's test)",
                   "**delineates the lesion** before excision"),
                  ("—", "Cotton-tipped applicators and swabs", ""),
                  ("1", "Endocervical speculum (Kogan)",
                   "inspects the canal"),
              ]),
              G("Excision of the cone", [
                  ("1", "Knife handle No.3 with No.11 blade",
                   "cold-knife conisation"),
                  ("1", "LLETZ / LEEP diathermy loop electrode set",
                   "**signature item** in current practice — assorted loop "
                   "sizes"),
                  ("1", "Electrosurgical generator with blend/coagulation "
                   "settings", ""),
                  ("1", "Ball / needle-point electrode",
                   "haemostasis of the crater"),
                  ("2", "Tenaculum or vulsellum forceps",
                   "traction and rotation of the cervix"),
                  ("2", "Long fine dissecting forceps and scissors",
                   "orientating and freeing the specimen"),
                  ("1", "Cervical (Hulka) tenaculum with stay sutures",
                   "lateral cervical stay sutures reduce bleeding"),
              ]),
              G("Haemostasis of the cone bed", [
                  ("1", "Diathermy with ball electrode", "primary method"),
                  ("—", "Monsel's solution (ferric subsulphate) paste",
                   "chemical haemostasis of the crater"),
                  ("—", "Silver nitrate sticks", ""),
                  ("2", "Needle holders with 2-0 absorbable suture",
                   "Sturmdorf or figure-of-eight haemostatic sutures"),
                  ("—", "Vaginal pack with lubricant",
                   "tamponade if oozing persists"),
                  ("—", "Adrenaline-containing local anaesthetic / "
                   "vasopressin", "infiltrated to reduce bleeding"),
              ]),
              G("Specimen handling — critically important", [
                  ("—", "Marking suture at the 12 o'clock position",
                   "**orientates the specimen for the pathologist**"),
                  ("—", "Separate labelled containers",
                   "cone specimen and endocervical curettings kept apart"),
                  ("1", "Endocervical curette",
                   "samples the canal above the cone"),
                  ("—", "Formalin and request forms",
                   "state the site and orientation"),
              ]),
          ],
          extras=[("Position", "Lithotomy under general, regional or local "
                   "anaesthesia with sedation."),
                  ("Smoke evacuation", "LLETZ produces surgical plume; a "
                   "smoke evacuator and appropriate masks are required."),
                  ("Complications",
                   "Primary and secondary haemorrhage, infection, cervical "
                   "stenosis, cervical incompetence with mid-trimester loss "
                   "and preterm labour in later pregnancy, and incomplete "
                   "excision.")],
          side_box={"title": "Two non-negotiables",
                    "lines": ["**Insulated speculum** whenever diathermy is "
                              "used — a metal speculum conducts current to "
                              "the vaginal wall.",
                              "**Orientation suture at 12 o'clock** — "
                              "without it the pathologist cannot report "
                              "which margin is involved."]},
          points=[
              "State that this is a **D&C tray + cone excision and "
              "haemostasis items**.",
              "**Lugol's iodine (Schiller's test) and acetic acid** to "
              "delineate the lesion are frequently rewarded.",
              "The **insulated speculum** with electrosurgery is a safety "
              "mark.",
              "**Monsel's solution and Sturmdorf sutures** are the named "
              "haemostatic measures.",
              "The **12 o'clock orientation suture** and **separate "
              "endocervical curettings** are the specimen-handling marks.",
              "Late complications — **cervical stenosis and cervical "
              "incompetence** — are commonly asked.",
          ],
          qa=[("What does a cervical cone tray contain beyond a D&C tray?",
               "An insulated vaginal speculum and lateral retractors, "
               "colposcope, acetic acid and Lugol's iodine with applicators; "
               "a No.11 blade for cold-knife conisation and/or a LLETZ loop "
               "electrode set with generator and ball electrode; tenaculum "
               "and stay sutures; haemostatic agents — Monsel's solution, "
               "silver nitrate, absorbable suture for Sturmdorf sutures and "
               "a vaginal pack; an endocervical curette; and specimen "
               "containers with a 12 o'clock orientation suture."),
              ("Why is the cone specimen marked with a suture?",
               "To orientate it for the pathologist so that the exact "
               "position of any involved margin can be reported, which "
               "determines whether further excision is required.")]),

        # ============================================================ 2.3
        T("2.3", "Laparoscopy Tray (Gynaecologic)",
          aka="Diagnostic and operative gynaecological laparoscopy set",
          lead="**Laparoscopy** inspects and operates within the peritoneal "
               "cavity through small ports under video vision, after "
               "creating a **pneumoperitoneum**. The tray is a complete "
               "**endoscopic system** — access, insufflation, optics, "
               "energy and hand instruments — and it must always be "
               "accompanied by an **open tray for immediate conversion**.",
          uses=["Diagnostic laparoscopy for pelvic pain, infertility, "
                "endometriosis",
                "Tubal patency testing (chromopertubation) and tubal "
                "sterilisation",
                "Ovarian cystectomy, oophorectomy, adhesiolysis",
                "Management of ectopic pregnancy — salpingostomy or "
                "salpingectomy",
                "Laparoscopic-assisted vaginal hysterectomy (LAVH) and "
                "total laparoscopic hysterectomy",
                "Myomectomy and treatment of endometriotic deposits"],
          plate=PL("Signature instruments",
                   [("veress", "Veress insufflation needle"),
                    ("trocar", "Trocar and cannula (port)"),
                    ("laparoscope", "Laparoscope, 0° / 30°"),
                    ("tenaculum", "Uterine manipulator / tenaculum")],
                   cap="Fig 2.3 — Access, insufflation, vision, manipulation"),
          groups=[
              G("Access and pneumoperitoneum", [
                  ("1", "Veress needle",
                   "**signature item** — spring-loaded blunt stylet for "
                   "closed entry"),
                  ("1", "Hasson cannula",
                   "for open (direct-vision) entry — safer in the "
                   "previously operated abdomen"),
                  ("1", "Primary trocar and cannula, 10–12 mm",
                   "umbilical camera port"),
                  ("3", "Secondary trocars and cannulae, 5 mm",
                   "working ports"),
                  ("1", "CO₂ insufflator with tubing and filter",
                   "**pressure limited to 12–15 mmHg**"),
                  ("1", "Gas cylinder / supply, checked", ""),
                  ("2", "Towel clips or skin-elevating forceps",
                   "lift the abdominal wall during entry"),
                  ("1", "Knife handle with No.11 blade", "port incisions"),
              ]),
              G("Optics and imaging", [
                  ("1", "Laparoscope 10 mm, 0° and 30°",
                   "0° for diagnosis, 30° for angled views"),
                  ("1", "Laparoscope 5 mm", "for a secondary port"),
                  ("1", "Fibre-optic light cable and xenon/LED source", ""),
                  ("1", "Camera head, coupler, control unit and monitor(s)",
                   ""),
                  ("1", "Insufflator/scope warmer and anti-fog solution",
                   "prevents lens misting"),
                  ("—", "Sterile camera and cable drapes", ""),
                  ("1", "Image recorder / printer", "documentation"),
              ]),
              G("Hand instruments (long, 5 mm shafts)", [
                  ("2", "Atraumatic grasping forceps",
                   "bowel, tube and ovary"),
                  ("2", "Toothed grasping forceps", "tough tissue, specimen"),
                  ("1", "Laparoscopic Babcock forceps", "tube and appendix"),
                  ("1", "Laparoscopic scissors, hook and straight", ""),
                  ("1", "Maryland dissecting forceps",
                   "fine curved dissector"),
                  ("1", "Bipolar and monopolar electrosurgical instruments",
                   "with cables and generator"),
                  ("1", "Suction–irrigation cannula with pump",
                   "clears blood and lavages"),
                  ("1", "Needle holders, laparoscopic pair",
                   "intracorporeal suturing"),
                  ("1", "Knot pusher and pre-tied ligature loops (Endoloop)",
                   ""),
                  ("1", "Clip applier with clips", ""),
                  ("1", "Specimen retrieval bag", ""),
                  ("1", "Tissue morcellator", "where used, with caution"),
                  ("1", "Fascial closure device", "port-site closure"),
              ]),
              G("Gynaecology-specific additions", [
                  ("1", "Uterine manipulator / Hulka tenaculum",
                   "**signature item** — moves the uterus from below"),
                  ("1", "Cannula for chromopertubation (Spackman / Rubin)",
                   "with methylene blue or indigo carmine"),
                  ("1", "Tubal sterilisation applicator",
                   "Filshie clip or Falope ring applicator"),
                  ("1", "Vaginal speculum and cervical tenaculum",
                   "for the vaginal component of LAVH"),
                  ("1", "Colpotomiser / vaginal tube",
                   "delineates the vault in total laparoscopic "
                   "hysterectomy"),
                  ("1", "Uterine morcellation containment bag", ""),
              ]),
              G("Conversion capability — never omitted", [
                  ("1", "Complete major / abdominal hysterectomy tray, "
                   "open and ready",
                   "**mandatory** — vascular or bowel injury requires "
                   "immediate laparotomy"),
                  ("—", "Vascular clamps and suture", ""),
                  ("—", "Blood cross-matched and available", ""),
              ]),
          ],
          extras=[("Position", "Lithotomy with Trendelenburg tilt (head "
                   "down 15–30°) to displace the bowel from the pelvis; "
                   "arms tucked; shoulder supports to prevent sliding."),
                  ("Preparation", "Bladder catheterised, stomach "
                   "decompressed, bimanual examination performed, "
                   "vagina and abdomen prepared."),
                  ("Complications",
                   "Entry injury to bowel or great vessels, gas embolism, "
                   "surgical emphysema, hypercapnia, shoulder-tip pain, "
                   "port-site hernia and bleeding, thermal injury "
                   "recognised late, and injury to bladder or ureter.")],
          side_box={"title": "Numbers to remember",
                    "lines": ["Insufflation pressure **12–15 mmHg**.",
                              "Gas used is **carbon dioxide** — "
                              "non-combustible and rapidly absorbed.",
                              "**Trendelenburg 15–30°** for pelvic "
                              "laparoscopy.",
                              "**Veress = closed entry; Hasson = open "
                              "entry.**"]},
          points=[
              "Describe the tray as **five systems**: access, insufflation, "
              "optics/imaging, energy, hand instruments — then add the "
              "gynaecological items.",
              "**CO₂ at 12–15 mmHg** is a standard factual mark.",
              "Distinguish **Veress (closed)** from **Hasson (open)** entry "
              "and know that open entry is preferred after previous "
              "surgery.",
              "The **uterine manipulator** and **chromopertubation "
              "cannula** are the gynaecology-specific signatures.",
              "**Always state that an open tray is kept ready for "
              "conversion** — marks are specifically allocated to this.",
              "Mention **port-site fascial closure** to prevent hernia.",
          ],
          pitfalls=["Forgetting the open conversion tray.",
                    "Omitting the insufflation pressure limit.",
                    "Listing scopes but not the light source, camera and "
                    "monitor.",
                    "Forgetting anti-fog and scope warming — a practical "
                    "detail examiners like."],
          qa=[("Describe the contents of a gynaecological laparoscopy tray.",
               "Access and insufflation — Veress needle, Hasson cannula, "
               "primary 10–12 mm and secondary 5 mm trocars, CO₂ insufflator "
               "with tubing and filter at 12–15 mmHg, No.11 blade; optics — "
               "0° and 30° laparoscopes, light cable and source, camera, "
               "control unit, monitor, anti-fog; hand instruments — "
               "atraumatic and toothed graspers, Babcock, scissors, Maryland "
               "dissector, bipolar and monopolar devices, "
               "suction–irrigation, needle holders, knot pusher and "
               "Endoloops, clip applier, retrieval bag, fascial closure "
               "device; gynaecological items — uterine manipulator, "
               "chromopertubation cannula with dye, tubal occlusion "
               "applicator, vaginal speculum and colpotomiser; and a "
               "complete open tray for immediate conversion."),
              ("Why must an open tray always accompany a laparoscopy set?",
               "Because major vascular or visceral injury, uncontrollable "
               "bleeding or failure to progress may demand immediate "
               "laparotomy; delay in converting is a direct cause of "
               "mortality.")]),

        # ============================================================ 2.4
        T("2.4", "Abdominal Hysterectomy Tray",
          aka="Total abdominal hysterectomy (TAH) tray · pelvic clearance set",
          lead="**Abdominal hysterectomy** removes the uterus through a "
               "laparotomy, dividing a series of vascular pedicles — round "
               "ligament, adnexal pedicle, uterine artery and "
               "cardinal/uterosacral complex — before opening the vaginal "
               "vault. The tray is a **major tray plus strong angled "
               "pedicle clamps** and instruments for the vault.",
          uses=["Fibroid uterus; menorrhagia unresponsive to treatment",
                "Adenomyosis and chronic pelvic pain",
                "Endometrial and cervical malignancy (with staging)",
                "Ovarian pathology requiring hysterectomy",
                "Postpartum haemorrhage — emergency hysterectomy",
                "Pelvic inflammatory disease with tubo-ovarian masses"],
          plate=PL("Signature instruments",
                   [("kocher", "Heaney / Kocher pedicle clamp"),
                    ("tenaculum", "Uterine vulsellum — traction"),
                    ("right_angle", "Right-angled forceps — pedicles"),
                    ("balfour", "Self-retaining retractor"),
                    ("needle_holder_long", "Heaney needle holder, angled")],
                   cap="Fig 2.4 — Pedicle control is the whole operation"),
          groups=[
              G("Base set", [
                  ("1", "Complete major procedures tray", "see 1.1"),
                  ("1", "Long instruments tray",
                   "for a deep pelvis or obese patient"),
              ]),
              G("Pedicle clamps — the defining group", [
                  ("6", "Heaney clamps, curved and angled",
                   "**signature item** — heavy, angled, atraumatic tip for "
                   "the uterine and cardinal pedicles"),
                  ("4", "Zeppelin / Wertheim hysterectomy clamps",
                   "long angled pedicle clamps"),
                  ("4", "Rogers / Kocher heavy crushing clamps",
                   "round ligament and specimen side"),
                  ("4", "Right-angled (Mixter) forceps",
                   "encircling pedicles for ligation"),
                  ("6", "Long Rochester-Péan forceps", "broad ligament"),
                  ("2", "Ovarian / adnexal clamps",
                   "infundibulopelvic ligament"),
              ]),
              G("Grasping and uterine manipulation", [
                  ("2", "Uterine vulsellum (Teale / Duplay) forceps",
                   "traction on the uterine fundus"),
                  ("2", "Myoma screw / corkscrew",
                   "traction on a large fibroid uterus"),
                  ("2", "Lahey or tenaculum forceps",
                   "cervix and vault angles"),
                  ("4", "Allis forceps, long", "vaginal vault edges"),
                  ("2", "DeBakey forceps, long",
                   "ureter and bladder — atraumatic"),
              ]),
              G("Retraction and exposure", [
                  ("1", "Balfour self-retaining retractor with bladder blade",
                   "the standard pelvic self-retainer"),
                  ("1", "O'Sullivan-O'Connor or Bookwalter ring retractor",
                   "alternative self-retaining system"),
                  ("2", "Deaver retractors, deep", ""),
                  ("2", "Malleable retractors",
                   "protect bladder, bowel and ureter"),
                  ("2", "Richardson retractors", "abdominal wall"),
                  ("—", "Moist laparotomy packs",
                   "pack the bowel out of the pelvis"),
              ]),
              G("Vault, suturing and closure", [
                  ("2", "Heaney needle holders, angled",
                   "**signature item** — suturing deep in the pelvis at an "
                   "angle"),
                  ("2", "Needle holders, long 25 cm", ""),
                  ("—", "Absorbable suture 0 and 1 on a heavy round needle",
                   "pedicle ligation and vault closure"),
                  ("—", "Transfixion and stay sutures",
                   "angles of the vault"),
                  ("1", "Ligature carrier (Deschamps)", "deep pedicles"),
                  ("—", "Ligating clips and appliers", ""),
                  ("1", "Long fine scissors and diathermy extension", ""),
                  ("—", "Vaginal pack and antiseptic",
                   "vagina prepared before the abdomen"),
                  ("—", "Urinary catheter",
                   "**bladder must be empty and catheterised**"),
                  ("—", "Closed suction drain and specimen container", ""),
                  ("—", "Ureteric stents / catheters",
                   "available when the anatomy is distorted"),
              ]),
          ],
          extras=[("Position", "Supine, slight Trendelenburg; lithotomy or "
                   "Lloyd-Davies if vaginal access is needed."),
                  ("Preparation", "Vaginal and abdominal antiseptic "
                   "preparation, urinary catheter, prophylactic "
                   "antibiotics, thromboprophylaxis, cross-matched blood."),
                  ("Structures at risk",
                   "**Ureter** (crosses beneath the uterine artery at the "
                   "cardinal ligament — 'water under the bridge'), bladder "
                   "at the vesicouterine fold, rectum posteriorly, and the "
                   "internal iliac vessels.")],
          side_box={"title": "The ureter",
                    "lines": ["The **ureter passes beneath the uterine "
                              "artery** at the base of the broad ligament — "
                              "*water under the bridge*.",
                              "This is the site of the classic surgical "
                              "injury, and the reason the tray carries "
                              "atraumatic DeBakey forceps, malleable "
                              "retractors and available ureteric stents."]},
          points=[
              "The **Heaney clamp and Heaney angled needle holder** are the "
              "signature pair — name them first.",
              "State the **sequence of pedicles**: round ligament → adnexal "
              "(infundibulopelvic or ovarian) → bladder reflection → "
              "uterine artery → cardinal and uterosacral → vault.",
              "The **ureter beneath the uterine artery** is the anatomical "
              "point most often awarded marks.",
              "Mention **vaginal preparation and a urinary catheter** as "
              "part of tray preparation.",
              "**Myoma screw** for a large fibroid uterus is a "
              "distinguishing detail.",
          ],
          qa=[("What additions to a major tray are required for abdominal "
               "hysterectomy?",
               "Heavy angled pedicle clamps — Heaney, Zeppelin/Wertheim and "
               "Rogers — with right-angled Mixter forceps and long "
               "Rochester-Péan clamps; uterine vulsellum forceps and a myoma "
               "screw for traction; a Balfour or ring self-retaining "
               "retractor with bladder blade, deep Deaver and malleable "
               "retractors and laparotomy packs; angled Heaney needle "
               "holders and long needle holders with heavy absorbable "
               "suture, a ligature carrier and clips; plus vaginal "
               "preparation, urinary catheter, drain, specimen container "
               "and available ureteric stents."),
              ("Which structure is most at risk and where?",
               "The ureter, where it passes beneath the uterine artery at "
               "the base of the broad ligament near the cardinal ligament "
               "('water under the bridge'), and again near the vaginal "
               "angle.")]),

        # ============================================================ 2.5
        T("2.5", "Caesarean Section Tray",
          aka="LSCS tray · lower segment caesarean section set",
          lead="Caesarean section delivers the fetus through the abdominal "
               "and uterine walls. Two features make its tray distinctive: "
               "it must be **fast** — assembled and checked for possible "
               "emergency use at any moment — and it must serve **two "
               "patients**, so a complete **neonatal resuscitation set** is "
               "part of the preparation.",
          uses=["Elective LSCS — malpresentation, placenta praevia, previous "
                "sections, maternal request",
                "Emergency LSCS — fetal distress, failure to progress, cord "
                "prolapse, abruption",
                "Classical (upper segment) section for a transverse lie or "
                "anterior praevia",
                "Caesarean hysterectomy for uncontrollable haemorrhage",
                "Concurrent sterilisation or myomectomy"],
          plate=PL("Signature instruments",
                   [("scalpel_20", "No.4 handle + No.20 blade"),
                    ("mayo_straight", "Bandage/umbilical scissors"),
                    ("kocher", "Green-Armytage / Kocher clamp"),
                    ("richardson", "Doyen retractor — bladder"),
                    ("poole", "Suction — amniotic fluid")],
                   cap="Fig 2.5 — Speed, exposure and haemostasis"),
          groups=[
              G("Base set", [
                  ("1", "Basic to major procedures tray",
                   "hospital-standard 'caesarean set' — a reduced major "
                   "tray"),
              ]),
              G("Uterine incision and delivery", [
                  ("2", "Knife handle No.4 with No.20 blade",
                   "skin and a second for the uterus"),
                  ("1", "Bandage / blunt-tipped scissors",
                   "extending the uterine incision without injuring the "
                   "fetus"),
                  ("1", "Doyen retractor",
                   "**signature item** — retracts and protects the bladder "
                   "from the lower segment"),
                  ("6", "Green-Armytage clamps",
                   "**signature item** — atraumatic clamps on the uterine "
                   "incision edges; control bleeding and mark the angles"),
                  ("4", "Allis or sponge forceps",
                   "membrane and edge handling"),
                  ("1", "Amniotomy hook / artery forceps",
                   "rupturing the membranes"),
                  ("1", "Wrigley's obstetric forceps or vacuum cup",
                   "assists a deeply engaged or floating head"),
                  ("1", "Fetal pillow / disimpaction device",
                   "where available for a deeply impacted head"),
              ]),
              G("Cord and neonate", [
                  ("2", "Umbilical cord clamps",
                   "plus a spare for a second twin"),
                  ("1", "Umbilical / cord scissors", "blunt-tipped"),
                  ("2", "Straight artery forceps",
                   "clamping the cord before division"),
                  ("—", "Cord-blood sampling tubes and syringe",
                   "pH, blood group, Coombs"),
                  ("—", "Warm dry towels and a hat", "thermal care"),
                  ("1", "**Complete neonatal resuscitation trolley**",
                   "overhead heater, suction, bag-valve-mask, laryngoscope, "
                   "ET tubes, oxygen, drugs — **checked before the skin "
                   "incision**"),
              ]),
              G("Haemostasis and uterine closure", [
                  ("2", "Needle holders", ""),
                  ("—", "Absorbable suture 1 or 0 on a large round needle",
                   "single- or double-layer uterine closure"),
                  ("6", "Rochester-Péan / Kocher clamps",
                   "angles of the uterine incision"),
                  ("2", "Long right-angled forceps",
                   "extending an angle tear"),
                  ("—", "Uterotonic drugs — oxytocin, ergometrine, "
                   "carboprost, misoprostol",
                   "**checked and drawn up before delivery**"),
                  ("—", "Intrauterine balloon tamponade (Bakri) device",
                   "for atonic postpartum haemorrhage"),
                  ("—", "B-Lynch suture material", "compression suturing"),
                  ("—", "Vascular clamps and hysterectomy clamps available",
                   "if caesarean hysterectomy becomes necessary"),
              ]),
              G("Suction, accessory and closure", [
                  ("1", "Poole or Yankauer suction with wide-bore tubing",
                   "**large volumes of amniotic fluid and blood**"),
                  ("2", "Large suction reservoirs", ""),
                  ("—", "Abdominal packs, counted", ""),
                  ("—", "Placenta receiver / bowl",
                   "placenta examined and weighed"),
                  ("—", "Urinary catheter with drainage bag",
                   "inserted before starting"),
                  ("—", "Skin closure — subcuticular suture or staples", ""),
                  ("—", "Cross-matched blood available",
                   "obstetric haemorrhage can be sudden and massive"),
              ]),
          ],
          extras=[("Position", "Supine with a 15° left lateral tilt or "
                   "manual uterine displacement to avoid aortocaval "
                   "compression."),
                  ("Incision", "Pfannenstiel (transverse suprapubic) is "
                   "usual; a midline vertical incision is used for extreme "
                   "urgency or difficult access."),
                  ("Preparation", "Antacid prophylaxis, urinary catheter, "
                   "prophylactic antibiotics, cross-matched blood, two "
                   "wide-bore intravenous lines, and a "
                   "**paediatrician/neonatal team present**."),
                  ("Critical timing",
                   "For a category-1 emergency the decision-to-delivery "
                   "interval target is **30 minutes**; the tray must "
                   "therefore be pre-assembled and checked, never built "
                   "from scratch.")],
          side_box={"title": "Two patients, one tray",
                    "lines": ["The caesarean tray is the only tray in this "
                              "syllabus prepared for **two patients "
                              "simultaneously**.",
                              "**Neonatal resuscitation equipment is part "
                              "of the tray preparation** and must be "
                              "checked before the skin incision — a mark "
                              "that is very often missed."]},
          points=[
              "Name **Green-Armytage clamps** and the **Doyen retractor** — "
              "the two instruments unique to this tray.",
              "**Uterotonics drawn up in advance** and **cross-matched "
              "blood** are part of preparation, not afterthoughts.",
              "State the **left lateral tilt** to prevent aortocaval "
              "compression.",
              "**Wide-bore suction with large reservoirs** — amniotic fluid "
              "volume is unlike any other operation.",
              "Include the **neonatal resuscitation trolley, checked "
              "beforehand**, and the **30-minute** decision-to-delivery "
              "target.",
              "Have **PPH escalation items** ready: Bakri balloon, B-Lynch "
              "suture, hysterectomy clamps.",
          ],
          qa=[("List the instruments specific to a caesarean section tray.",
               "Green-Armytage clamps for the uterine incision edges; a "
               "Doyen retractor to protect the bladder; blunt bandage "
               "scissors to extend the uterine incision; an amniotomy hook; "
               "Wrigley's forceps or a vacuum cup for the fetal head; "
               "umbilical cord clamps and blunt cord scissors with "
               "cord-blood tubes; wide-bore suction with large reservoirs; "
               "uterotonic drugs drawn up in advance; a Bakri balloon and "
               "B-Lynch suture for haemorrhage; a placenta receiver; and a "
               "fully checked neonatal resuscitation trolley."),
              ("Why is neonatal resuscitation equipment part of the "
               "caesarean tray preparation?",
               "Because the operation delivers a second patient who may "
               "require immediate airway support, warming and "
               "resuscitation; the equipment must be checked and a "
               "paediatric team present before the skin incision, since "
               "there is no time to prepare it after delivery.")]),

        # ============================================================ 2.6
        T("2.6", "Vaginal Hysterectomy Tray",
          aka="VH tray · vaginal route hysterectomy set · pelvic floor repair "
              "tray",
          lead="**Vaginal hysterectomy** removes the uterus entirely through "
               "the vagina. The whole operation is performed in a **narrow, "
               "deep, poorly lit tube**, working from below upward — the "
               "reverse of the abdominal sequence. The tray is therefore "
               "built around **angled, curved and long instruments**, "
               "**self-retaining vaginal retraction** and good "
               "illumination.",
          uses=["Uterine prolapse (the classic indication) with or without "
                "cystocele/rectocele",
                "Benign uterus of modest size with adequate descent",
                "Dysfunctional uterine bleeding in a multiparous woman",
                "Combined with anterior and posterior colporrhaphy "
                "(pelvic floor repair)",
                "Combined with sacrospinous fixation for vault support"],
          plate=PL("Signature instruments",
                   [("sims_speculum", "Auvard weighted speculum"),
                    ("tenaculum", "Uterine vulsellum — traction"),
                    ("kocher", "Heaney pedicle clamp, curved"),
                    ("needle_holder_long", "Heaney needle holder, angled"),
                    ("metzenbaum", "Long curved scissors")],
                   cap="Fig 2.6 — Angled instruments for a deep narrow field"),
          groups=[
              G("Base set", [
                  ("1", "Complete D&C tray",
                   "see 2.1 — provides the vaginal exposure instruments"),
                  ("1", "Abdominal hysterectomy tray, open and available",
                   "**for conversion** if descent is inadequate or "
                   "haemorrhage occurs"),
              ]),
              G("Vaginal exposure", [
                  ("1", "Auvard weighted vaginal speculum",
                   "**signature item** — its weight retracts the posterior "
                   "wall without an assistant"),
                  ("2", "Sims or Landon lateral vaginal retractors",
                   "lateral walls"),
                  ("1", "Anterior vaginal wall retractor",
                   "bladder retraction"),
                  ("1", "Deaver retractor, narrow", "deep lateral exposure"),
                  ("1", "Head-light or lighted retractor",
                   "**illumination is a genuine problem** in this operation"),
                  ("4", "Allis forceps, long",
                   "vaginal wall and vault edges"),
              ]),
              G("Traction and pedicle control", [
                  ("2", "Uterine vulsellum (Teale) forceps",
                   "progressive downward traction on the cervix and uterus"),
                  ("2", "Cervical tenaculum / Littlewood forceps", ""),
                  ("6", "Heaney clamps, curved and angled",
                   "**signature item** — the pedicle clamp of vaginal "
                   "surgery"),
                  ("4", "Zeppelin / Wertheim clamps, long curved", ""),
                  ("4", "Long Rochester-Péan / Kocher clamps",
                   "uterosacral and cardinal ligaments"),
                  ("2", "Right-angled forceps, long",
                   "encircling deep pedicles"),
                  ("2", "Myoma screw", "traction on a bulky uterus"),
              ]),
              G("Cutting, dissecting and suturing", [
                  ("2", "Knife handle No.3 with No.10 / No.15 blades",
                   "circumferential vaginal incision"),
                  ("2", "Long curved Metzenbaum / Mayo scissors",
                   "opening the pouch of Douglas and the "
                   "vesicouterine space"),
                  ("2", "Heaney needle holders, angled",
                   "**signature item** — suturing at depth around a curve"),
                  ("2", "Needle holders, long straight", ""),
                  ("—", "Absorbable suture 0 and 1 on heavy curved needles",
                   "pedicle ligation, vault closure, McCall culdoplasty"),
                  ("1", "Ligature carrier (Deschamps / Miya hook)",
                   "sacrospinous fixation"),
                  ("—", "Long stay sutures", "vault angles"),
                  ("1", "Long fine-tipped diathermy extension", ""),
              ]),
              G("Pelvic floor repair additions", [
                  ("2", "Allis and Kocher forceps",
                   "defining the vaginal flaps"),
                  ("1", "Fascial dissecting scissors",
                   "anterior and posterior colporrhaphy"),
                  ("—", "Delayed absorbable suture 2-0",
                   "plication of pubocervical and rectovaginal fascia"),
                  ("—", "Mesh / graft material",
                   "only if specifically planned"),
                  ("1", "Perineal repair set",
                   "perineorrhaphy where indicated"),
              ]),
              G("Accessory", [
                  ("1", "Suction tip, long fine", ""),
                  ("—", "Vaginal pack with antiseptic or oestrogen cream",
                   "haemostasis and support"),
                  ("—", "Urinary catheter",
                   "indwelling; bladder injury risk is significant"),
                  ("—", "Specimen container", "uterus and cervix"),
                  ("—", "Counted swabs and packs",
                   "**a pack left in the vagina is a classic retained "
                   "item** — count and document"),
              ]),
          ],
          extras=[("Position", "Lithotomy with the buttocks projecting "
                   "slightly beyond the table edge, thighs well flexed and "
                   "abducted; Trendelenburg tilt aids exposure."),
                  ("Prerequisites", "Adequate uterine descent, a mobile "
                   "uterus of no more than about 12 weeks' size, and no "
                   "adnexal mass — otherwise the abdominal route is "
                   "chosen."),
                  ("Structures at risk",
                   "Bladder anteriorly (during the vesicouterine "
                   "dissection), rectum posteriorly, ureters at the "
                   "cardinal ligament, and the vaginal vault vessels.")],
          side_box={"title": "Why everything is angled",
                    "lines": ["The operative field is a **deep narrow "
                              "tube** entered from below.",
                              "Straight instruments cannot reach the "
                              "pedicles at the correct angle, so **Heaney "
                              "clamps and Heaney angled needle holders** "
                              "are used.",
                              "The **Auvard weighted speculum** replaces an "
                              "assistant's retractor."]},
          compare=CMP(
              ["", "Abdominal hysterectomy", "Vaginal hysterectomy"],
              [["Access", "Laparotomy — direct view",
                "Through the vagina — deep narrow tube"],
               ["Pedicle sequence", "Round ligament first, downward",
                "Uterosacral/cardinal first, **upward**"],
               ["Key retractor", "Balfour self-retaining with bladder blade",
                "Auvard weighted speculum"],
               ["Key clamp", "Heaney / Zeppelin (straight approach)",
                "Heaney curved and angled"],
               ["Key needle holder", "Long straight",
                "**Heaney angled**"],
               ["Illumination", "Adequate from theatre lights",
                "Often needs a head-light"],
               ["Main advantages", "Any uterine size; adnexa accessible",
                "No abdominal scar; faster recovery"]],
              cap="Table 2.1 — Abdominal versus vaginal hysterectomy trays"),
          points=[
              "The three signatures are the **Auvard weighted speculum, "
              "Heaney curved clamp and Heaney angled needle holder**.",
              "The pedicle sequence is **the reverse of the abdominal "
              "route** — uterosacral and cardinal ligaments first, working "
              "upward to the adnexal pedicle.",
              "**Illumination (head-light)** is a genuine requirement — "
              "mention it.",
              "Always state that an **abdominal tray is available for "
              "conversion**.",
              "The **vaginal pack must be counted and documented** — a "
              "classic retained-item scenario.",
              "Note that VH is frequently **combined with pelvic floor "
              "repair**, so colporrhaphy instruments are included.",
          ],
          qa=[("What are the special instruments of a vaginal hysterectomy "
               "tray and why?",
               "An Auvard weighted speculum (self-retaining posterior "
               "retraction), Sims lateral retractors and a head-light for "
               "illumination; uterine vulsellum forceps and a myoma screw "
               "for progressive downward traction; curved and angled Heaney "
               "clamps with long Zeppelin and Rochester-Péan clamps for the "
               "pedicles; long curved Metzenbaum scissors; and angled Heaney "
               "needle holders with heavy absorbable suture. All are curved, "
               "angled or long because the operation is performed in a deep "
               "narrow tube entered from below, where straight instruments "
               "cannot reach the pedicles at a workable angle."),
              ("How does the order of pedicle division differ from the "
               "abdominal route?",
               "In vaginal hysterectomy the operation proceeds from below "
               "upward — uterosacral and cardinal ligaments first, then the "
               "uterine vessels, and the round and adnexal pedicles last. "
               "In abdominal hysterectomy the sequence begins with the round "
               "ligament and adnexal pedicle and works downward to the "
               "vault.")]),
    ])
