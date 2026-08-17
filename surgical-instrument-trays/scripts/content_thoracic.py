#!/usr/bin/env python3
"""Part IV -- Thoracic Trays."""
from schema import T, P, PL, DP, FIG, G, CMP

THORACIC = P(
    "IV", "Thoracic Trays",
    "Mediastinoscopy · Thoracotomy · Pacemaker",
    intro="Thoracic trays are governed by one anatomical fact: the chest is "
          "a **rigid bony cage containing a negative-pressure space**. Every "
          "tray therefore needs instruments to **get through or between the "
          "ribs**, and every thoracic procedure ends with **restoration of "
          "negative intrapleural pressure** through an underwater-seal chest "
          "drain. A pacemaker tray is the exception — a small subcutaneous "
          "set that nevertheless carries the same pneumothorax risk.",
    trays=[

        # ============================================================ 4.1
        T("4.1", "Mediastinoscopy Tray",
          aka="Cervical mediastinoscopy · Carlens procedure tray",
          lead="**Mediastinoscopy** inspects and biopsies the "
               "**paratracheal and tracheobronchial lymph nodes** through a "
               "small suprasternal incision, using a tapered open scope "
               "passed down the pretracheal plane by blunt finger "
               "dissection. It is a small set with a very large potential "
               "complication: the scope lies between the great vessels, so "
               "the tray must be able to support **immediate "
               "thoracotomy or sternotomy**.",
          uses=["Staging of bronchogenic carcinoma — mediastinal node "
                "sampling",
                "Diagnosis of mediastinal lymphadenopathy — lymphoma, "
                "sarcoidosis, tuberculosis",
                "Biopsy of a mediastinal mass",
                "Assessment before thoracotomy for resectability",
                "Drainage of a mediastinal abscess (rarely)"],
          plate=PL("Signature instruments",
                   [("mediastinoscope", "Mediastinoscope (tapered open tube)"),
                    ("frazier", "Fine insulated suction"),
                    ("right_angle", "Long biopsy / dissecting forceps"),
                    ("weitlaner", "Small self-retaining retractor")],
                   cap="Fig 4.1 — A small set with major back-up "
                       "requirements"),
          groups=[
              G("Base set", [
                  ("1", "Basic / minor procedures tray",
                   "see 1.2 — the incision itself is small"),
              ]),
              G("The scope system", [
                  ("1", "Mediastinoscope, tapered open tube",
                   "**signature item** — slightly flattened, open-ended, "
                   "with an integral or attachable light"),
                  ("1", "Fibre-optic light carrier, cable and source",
                   "cold light"),
                  ("1", "Camera, coupler and monitor",
                   "for video-assisted mediastinoscopy and teaching"),
                  ("1", "Suction–coagulation (insulated) cannula",
                   "combined suction and cautery down the scope"),
              ]),
              G("Instruments passed down the scope", [
                  ("2", "Long mediastinal biopsy forceps, cup pattern",
                   "node sampling"),
                  ("2", "Long aspirating (fine) needle with syringe",
                   "**a node is aspirated before it is biopsied** — to "
                   "confirm it is not a vessel"),
                  ("2", "Long blunt dissectors / peanut carriers",
                   "sweeping tissue off the node"),
                  ("1", "Long insulated suction tip", ""),
                  ("2", "Long clip applier with clips",
                   "haemostasis at depth"),
                  ("—", "Long swab carriers with gauze pledgets",
                   "pressure haemostasis in a narrow channel"),
              ]),
              G("Neck exposure", [
                  ("2", "Small Langenbeck / Army-Navy retractors",
                   "suprasternal incision"),
                  ("1", "Weitlaner self-retaining retractor",
                   "holds the strap muscles apart"),
                  ("2", "Fine artery forceps and Adson forceps", ""),
                  ("1", "Fine Metzenbaum scissors",
                   "dividing the pretracheal fascia"),
                  ("2", "Malleable retractor, narrow",
                   "protects the trachea"),
              ]),
              G("Emergency back-up — the defining requirement", [
                  ("1", "**Complete thoracotomy tray, open and ready**",
                   "see 4.2 — for uncontrollable bleeding"),
                  ("1", "**Sternal saw and sternotomy set available**",
                   "median sternotomy gives the fastest access to the "
                   "great vessels"),
                  ("—", "Vascular clamps, vascular suture and "
                   "haemostatic agents", ""),
                  ("—", "**Cross-matched blood immediately available**",
                   "haemorrhage from the innominate artery or azygos vein "
                   "is catastrophic"),
                  ("—", "Chest drain with underwater seal",
                   "the pleura may be entered"),
              ]),
          ],
          extras=[("Position", "Supine with the neck extended over a "
                   "head-ring and slight head-up tilt, as for "
                   "thyroidectomy; a small transverse incision one "
                   "finger-breadth above the sternal notch."),
                  ("Technique", "The pretracheal plane is opened by **blunt "
                   "finger dissection** anterior to the trachea, the scope "
                   "is passed along the finger track, and nodes are "
                   "identified, **aspirated with a needle first** and then "
                   "biopsied."),
                  ("Structures at risk",
                   "**Innominate (brachiocephalic) artery, aortic arch, "
                   "azygos vein, superior vena cava, pulmonary artery, "
                   "recurrent laryngeal nerve, trachea and oesophagus.** "
                   "This concentration of great vessels in a blind narrow "
                   "channel is what makes the procedure hazardous."),
                  ("Complications",
                   "Major haemorrhage, pneumothorax, recurrent laryngeal "
                   "nerve palsy, oesophageal or tracheal injury, wound "
                   "infection, mediastinitis and air embolism.")],
          side_box={"title": "Aspirate before you biopsy",
                    "lines": ["In the mediastinum a **node and a vessel can "
                              "look identical** through a narrow scope.",
                              "A **fine needle is passed and aspirated "
                              "first**: blood means vessel — do not biopsy.",
                              "This single step is the most examined safety "
                              "point of the procedure."]},
          points=[
              "The signature item is the **tapered open mediastinoscope**; "
              "all working instruments are **long**.",
              "State the **aspirate-before-biopsy rule** explicitly.",
              "The **thoracotomy tray and sternal saw must be open and "
              "ready** — marks are given for recognising this.",
              "Name the vessels at risk, particularly the **innominate "
              "artery and azygos vein**.",
              "Access is by **blunt finger dissection in the pretracheal "
              "plane** — mention it.",
          ],
          qa=[("What does a mediastinoscopy tray contain?",
               "A minor tray for the suprasternal incision plus: a tapered "
               "open mediastinoscope with fibre-optic light carrier, cable, "
               "source and camera; long cup biopsy forceps, long aspirating "
               "needle and syringe, long blunt dissectors, long insulated "
               "suction–coagulation cannula, long clip applier and long swab "
               "carriers; small Langenbeck and Weitlaner retractors with "
               "fine Metzenbaum scissors and Adson forceps; and — "
               "essentially — a complete thoracotomy tray with sternal saw, "
               "vascular clamps and suture, haemostatic agents, chest drain "
               "and cross-matched blood immediately available."),
              ("Why is a node aspirated before biopsy?",
               "Because a great vessel can be mistaken for a lymph node in "
               "the narrow, poorly lit mediastinal channel. Aspiration "
               "returning blood identifies a vessel and prevents "
               "catastrophic haemorrhage from biopsying it.")]),

        # ============================================================ 4.2
        T("4.2", "Thoracotomy Tray",
          aka="Posterolateral thoracotomy tray · lung resection set",
          lead="**Thoracotomy** opens the chest between the ribs to reach "
               "the lung, pleura, oesophagus or mediastinum. The tray is a "
               "major tray plus three distinct groups: **rib instruments** "
               "to enter and spread the chest, **pulmonary vascular and "
               "bronchial instruments** to divide the hilum, and "
               "**closure/drainage** equipment to restore negative "
               "intrapleural pressure.",
          uses=["Lobectomy, pneumonectomy and wedge resection for carcinoma",
                "Decortication and pleurectomy for empyema or trapped lung",
                "Open lung biopsy; excision of a bulla or blebs",
                "Oesophagectomy (thoracic component)",
                "Repair of thoracic trauma; drainage of a haemothorax",
                "Excision of a mediastinal mass"],
          plate=PL("Signature instruments",
                   [("finochietto", "Finochietto rib spreader"),
                    ("rib_shears", "Rib shears"),
                    ("rib_raspatory", "Doyen periosteal elevator"),
                    ("rib_approximator", "Rib approximator — closure"),
                    ("satinsky", "Satinsky vascular clamp"),
                    ("bronchoscope", "Bronchoscope")],
                   cap="Fig 4.2 — Enter, spread, divide, close, drain"),
          groups=[
              G("Base set", [
                  ("1", "Complete major procedures tray", "see 1.1"),
                  ("1", "Long instruments tray",
                   "the hilum is deep within the cage"),
              ]),
              G("Rib instruments — entering and spreading the chest", [
                  ("1", "Finochietto rib spreader (self-retaining)",
                   "**signature item** — rack-and-crank retractor that "
                   "spreads the intercostal space"),
                  ("1", "Rib shears / rib cutter", "divides a rib"),
                  ("1", "Doyen periosteal elevator (rib raspatory)",
                   "**signature item** — semicircular hook stripping "
                   "periosteum from the rib"),
                  ("1", "Rib rongeur / bone nibbler",
                   "trimming the cut rib end"),
                  ("1", "Rib approximator",
                   "**signature item** — pulls adjacent ribs together for "
                   "closure"),
                  ("1", "Bone rasp and bone wax", ""),
                  ("1", "Gigli saw with handles", "alternative rib division"),
                  ("1", "Sternal saw and sternal wire set",
                   "if the approach is converted to sternotomy"),
                  ("1", "Alexander / Matson periosteotome",
                   "raising periosteum along the rib"),
              ]),
              G("Lung, hilar and bronchial instruments", [
                  ("4", "Lung (Duval / Pennington) grasping forceps",
                   "**signature item** — triangular atraumatic jaws for "
                   "holding lung tissue"),
                  ("2", "Bronchus clamp (Sarot / Lees)",
                   "occludes the bronchus before division"),
                  ("2", "Satinsky (side-biting) vascular clamps",
                   "pulmonary artery and vein"),
                  ("4", "Bulldog clamps", "small pulmonary vessels"),
                  ("4", "DeBakey vascular forceps, long", "atraumatic"),
                  ("2", "Potts-Smith angled vascular scissors", ""),
                  ("6", "Long right-angled (Mixter) forceps",
                   "encircling hilar structures"),
                  ("—", "Vessel loops and umbilical tapes", ""),
                  ("1", "Bronchial / pulmonary stapler with reloads",
                   "the modern method of dividing bronchus and vessels"),
                  ("1", "Bronchoscope with light source",
                   "available — checks the bronchial stump and clears "
                   "secretions"),
                  ("—", "Vascular suture 3-0 to 5-0 double-armed", ""),
              ]),
              G("Retraction and exposure", [
                  ("2", "Deaver retractors, deep", ""),
                  ("2", "Malleable retractors",
                   "protects lung and pericardium"),
                  ("2", "Richardson retractors", "chest wall layers"),
                  ("1", "Scapular retractor",
                   "elevates the scapula in a posterolateral approach"),
                  ("—", "Moist packs / lung swabs",
                   "packing the lung away"),
                  ("—", "Head-light", ""),
              ]),
              G("Closure and drainage — never omitted", [
                  ("—", "**Chest drain(s), 28–32 Fr, with trocar or "
                   "clamp**",
                   "**signature requirement** — apical drain for air, "
                   "basal drain for fluid"),
                  ("1", "**Underwater-seal drainage system**",
                   "restores and maintains negative intrapleural pressure"),
                  ("2", "Chest drain (tube) clamps",
                   "**two clamps must accompany every chest drain**"),
                  ("—", "Heavy non-absorbable suture / sternal wire",
                   "pericostal closure"),
                  ("—", "Rib approximator", "brings the ribs together"),
                  ("1", "Wire twister and wire cutter",
                   "if sternotomy was performed"),
                  ("—", "Absorbable suture for muscle layers", ""),
                  ("—", "Suction source and tubing", ""),
                  ("—", "Specimen container",
                   "lung specimen orientated and labelled; nodes sent "
                   "separately by station"),
              ]),
          ],
          extras=[("Position", "**Lateral decubitus** with the operative "
                   "side up, arm forward on an arm-board, axillary roll, "
                   "table flexed to open the intercostal spaces; the lower "
                   "leg flexed with padding between the knees."),
                  ("Anaesthesia", "Double-lumen endotracheal tube for "
                   "**one-lung ventilation**, allowing the operative lung "
                   "to be collapsed."),
                  ("Incision", "Posterolateral thoracotomy through the 5th "
                   "or 6th intercostal space is standard; anterolateral for "
                   "trauma; median sternotomy for bilateral or mediastinal "
                   "access."),
                  ("Complications",
                   "Haemorrhage, persistent air leak, bronchopleural "
                   "fistula, empyema, atelectasis and pneumonia, "
                   "post-thoracotomy pain, arrhythmia and chylothorax.")],
          side_box={"title": "Chest drain rules",
                    "lines": ["Drains are placed **apically for air** and "
                              "**basally for fluid**.",
                              "The **underwater seal** acts as a one-way "
                              "valve, letting air out and none in.",
                              "**Two clamps travel with every chest drain.**",
                              "The bottle is kept **below the level of the "
                              "chest** at all times."]},
          points=[
              "Name the **four rib instruments**: Finochietto spreader, rib "
              "shears, Doyen periosteal elevator, rib approximator.",
              "**Duval lung forceps** is the lung-specific grasper.",
              "**Chest drain + underwater seal + two clamps** must appear in "
              "every answer.",
              "Mention **one-lung ventilation via a double-lumen tube** — an "
              "easy mark showing you understand the operation.",
              "Describe the **lateral decubitus position with the table "
              "flexed and an axillary roll**.",
              "**Bronchoscope available** to check the bronchial stump.",
          ],
          pitfalls=["Omitting the chest drain and underwater seal.",
                    "Forgetting the rib approximator for closure — "
                    "candidates remember how to open but not how to close.",
                    "Not mentioning cross-matched blood.",
                    "Confusing Finochietto (spreads ribs apart) with the rib "
                    "approximator (brings them together)."],
          qa=[("Describe the thoracotomy tray.",
               "A major tray with a long instruments tray, plus: rib "
               "instruments — Finochietto self-retaining rib spreader, rib "
               "shears, Doyen periosteal elevator, rib rongeur, rib "
               "approximator, rasp, bone wax, Gigli saw and a sternal saw "
               "with wire set; lung and hilar instruments — Duval lung "
               "forceps, bronchus clamps, Satinsky and bulldog vascular "
               "clamps, DeBakey forceps, Potts scissors, long Mixter "
               "forceps, vessel loops, pulmonary staplers, bronchoscope and "
               "vascular suture; deep Deaver, malleable, Richardson and "
               "scapular retractors with a head-light; and closure and "
               "drainage — 28–32 Fr chest drains with an underwater-seal "
               "system and two clamps, heavy pericostal suture, wire "
               "twister and specimen containers."),
              ("Why is an underwater-seal drainage system used after "
               "thoracotomy?",
               "The pleural space is normally at negative pressure. The "
               "underwater seal acts as a one-way valve that allows air and "
               "fluid to escape from the pleural cavity during expiration "
               "but prevents atmospheric air from entering, so the lung "
               "re-expands and negative intrapleural pressure is "
               "re-established.")]),

        # ============================================================ 4.3
        T("4.3", "Pacemaker Tray",
          aka="Permanent pacemaker insertion tray · PPM implantation set",
          lead="A **permanent pacemaker** consists of a **pulse generator** "
               "implanted in a subcutaneous or subpectoral pocket, "
               "connected to one or more **leads** positioned in the heart. "
               "Transvenous implantation is a **small-tray procedure "
               "performed under fluoroscopy** — so the tray is a minor set "
               "plus vascular access equipment, the device itself, and "
               "radiation protection.",
          uses=["Symptomatic bradycardia; sick sinus syndrome",
                "Complete (third-degree) and symptomatic second-degree "
                "atrioventricular block",
                "Atrial fibrillation with slow ventricular response",
                "Cardiac resynchronisation therapy (biventricular pacing)",
                "Implantable cardioverter-defibrillator insertion",
                "Generator change (elective replacement for battery "
                "depletion) and lead revision"],
          plate=PL("Signature instruments",
                   [("pacemaker", "Pulse generator with endocardial leads"),
                    ("scalpel_15", "No.15 blade — pocket incision"),
                    ("metzenbaum", "Metzenbaum scissors — pocket"),
                    ("mosquito", "Fine mosquito forceps"),
                    ("weitlaner", "Small self-retaining retractor")],
                   cap="Fig 4.3 — A minor set plus the device and imaging"),
          groups=[
              G("Base set", [
                  ("1", "Basic / minor procedures tray",
                   "see 1.2 — the pocket is a superficial dissection"),
              ]),
              G("Venous access", [
                  ("1", "Introducer needle with syringe",
                   "subclavian, axillary or cephalic vein puncture"),
                  ("—", "Guidewires (J-tipped)", "Seldinger technique"),
                  ("2", "Peel-away introducer sheaths and dilators, sized",
                   "**signature item** — admit the lead, then peel away"),
                  ("1", "Vein pick / cephalic vein cut-down set",
                   "for the cephalic vein approach"),
                  ("1", "Fine vascular dissecting forceps and scissors", ""),
                  ("—", "Heparinised saline flush", ""),
              ]),
              G("The device and leads", [
                  ("1", "Pulse generator (single- or dual-chamber)",
                   "**checked for model, serial number and battery status "
                   "before opening**"),
                  ("2", "Endocardial pacing leads — active (screw-in) or "
                   "passive (tined) fixation",
                   "right atrium and right ventricle"),
                  ("—", "Lead stylets, straight and curved",
                   "shape the lead for positioning"),
                  ("1", "Torque wrench / hex screwdriver",
                   "**signature item** — tightens the set-screw in the "
                   "generator header; **it is tiny and must be counted**"),
                  ("—", "Lead anchoring sleeves and non-absorbable ties",
                   "secure the lead to the pectoral fascia"),
                  ("1", "Pacing system analyser (PSA) with cables",
                   "measures threshold, impedance and R-wave amplitude"),
                  ("1", "Programmer / telemetry wand",
                   "interrogates and programmes the device"),
                  ("—", "Epicardial lead set and screw-in electrodes",
                   "for the surgical/epicardial route"),
              ]),
              G("Pocket formation and closure", [
                  ("1", "Knife handle No.3 with No.15 blade",
                   "infraclavicular incision"),
                  ("2", "Metzenbaum scissors",
                   "blunt dissection of the pocket"),
                  ("2", "Weitlaner / small self-retaining retractor", ""),
                  ("2", "Army-Navy or Langenbeck retractors", ""),
                  ("8", "Fine mosquito and Crile forceps", "haemostasis"),
                  ("1", "Diathermy pencil",
                   "**used with caution** — interference with the device"),
                  ("2", "Needle holders",
                   "absorbable to fascia and subcutaneous tissue, "
                   "subcuticular to skin"),
                  ("—", "Antibiotic irrigation / antibacterial envelope",
                   "device infection is a serious complication"),
              ]),
              G("Imaging and radiation protection", [
                  ("1", "**Image intensifier (C-arm) with sterile drape**",
                   "**essential** — lead position is confirmed "
                   "fluoroscopically"),
                  ("—", "**Lead aprons, thyroid shields and dosimeters for "
                   "all staff**", "radiation protection is part of tray "
                   "preparation"),
                  ("—", "Radiolucent operating table and arm-boards", ""),
                  ("1", "ECG monitor, defibrillator and external pacing "
                   "capability",
                   "**must be immediately available** — lead placement can "
                   "provoke arrhythmia or asystole"),
                  ("—", "Contrast medium",
                   "venography if venous access is difficult"),
                  ("—", "Chest drain and thoracotomy back-up available",
                   "for pneumothorax or cardiac perforation/tamponade"),
              ]),
          ],
          extras=[("Position", "Supine with the arm on the operative side "
                   "adducted or slightly abducted; the head turned away; "
                   "left infraclavicular site is usual (favourable lead "
                   "curve to the right ventricle)."),
                  ("Preparation", "Antibiotic prophylaxis, ECG monitoring, "
                   "intravenous access, anticoagulation reviewed, skin "
                   "prepared widely from the neck to the nipple, and the "
                   "device model confirmed against the plan."),
                  ("Complications",
                   "**Pneumothorax and haemothorax** (subclavian puncture), "
                   "pocket haematoma, lead displacement, cardiac "
                   "perforation with tamponade, arrhythmia during lead "
                   "placement, diaphragmatic pacing, device infection and "
                   "erosion, and Twiddler's syndrome.")],
          side_box={"title": "Small parts, big risk",
                    "lines": ["The **torque wrench** is a tiny item that is "
                              "easily lost in the pocket — **include it in "
                              "the count**.",
                              "**Lead stylets and anchoring sleeves** are "
                              "also small and countable.",
                              "**Pneumothorax** is the classic early "
                              "complication of subclavian puncture — a "
                              "chest X-ray follows every implant."]},
          points=[
              "This is a **minor tray** procedure — say so, then list the "
              "additions.",
              "Name the **peel-away introducer sheath** and the **torque "
              "wrench**; both are unique to this tray.",
              "**Fluoroscopy with an image intensifier and lead aprons for "
              "all staff** is part of tray preparation.",
              "A **defibrillator with external pacing must be immediately "
              "available**.",
              "**Pneumothorax** is the complication to quote, with a "
              "post-procedure chest X-ray.",
              "The **pacing system analyser** confirms thresholds before "
              "closure — a detail that distinguishes a good answer.",
          ],
          qa=[("List the requirements of a pacemaker insertion tray.",
               "A minor tray plus: venous access equipment — introducer "
               "needle, guidewires, peel-away introducer sheaths and "
               "dilators, cephalic cut-down set and heparinised flush; the "
               "device — pulse generator, endocardial leads with active or "
               "passive fixation, stylets, torque wrench, anchoring sleeves, "
               "pacing system analyser and programmer; pocket instruments — "
               "No.15 blade, Metzenbaum scissors, self-retaining and "
               "hand-held retractors, fine haemostats, diathermy, needle "
               "holders and antibiotic irrigation; and imaging and safety — "
               "a draped image intensifier, lead aprons and thyroid shields, "
               "ECG monitor with defibrillator and external pacing, contrast "
               "medium, and chest drain back-up."),
              ("What is the commonest early complication of transvenous "
               "pacemaker insertion?",
               "Pneumothorax from subclavian vein puncture, which is why a "
               "chest radiograph is obtained after every implantation and a "
               "chest drain is kept available.")]),
    ])
