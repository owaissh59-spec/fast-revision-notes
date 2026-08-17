#!/usr/bin/env python3
"""Part V -- Cardiovascular Trays."""
from schema import T, P, PL, DP, FIG, G, CMP

CARDIO = P(
    "V", "Cardiovascular Trays",
    "Vascular procedures · Vascular shunt · Cardiac procedures",
    intro="Cardiovascular trays obey rules found nowhere else in surgery. "
          "Every instrument that touches a vessel must be **atraumatic**, "
          "because a crushed intima thromboses. Every suture is "
          "**non-absorbable monofilament on a swaged, usually double-armed "
          "needle**. **Heparinised saline** is on the tray from the start. "
          "And the cardiac tray adds the single greatest complexity in "
          "surgery — **cardiopulmonary bypass**.",
    trays=[

        # ============================================================ 5.1
        T("5.1", "Vascular Procedures Tray",
          aka="General vascular tray · arterial reconstruction set",
          lead="The **vascular tray** serves any procedure in which an "
               "artery or vein is opened, repaired, bypassed or replaced. "
               "Its design follows one principle: **the vessel wall must be "
               "controlled without being injured**. Every clamp is "
               "non-crushing, every forceps has atraumatic jaws, and the "
               "tray carries the means to occlude, open, flush, repair and "
               "graft.",
          uses=["Aorto-iliac and femoro-popliteal bypass grafting",
                "Carotid endarterectomy",
                "Abdominal aortic aneurysm repair (open)",
                "Embolectomy and thrombectomy",
                "Repair of arterial trauma",
                "Arteriovenous fistula and graft creation for dialysis",
                "Varicose vein surgery (the venous subset)"],
          plate=PL("Signature instruments",
                   [("debakey_forceps", "DeBakey atraumatic forceps"),
                    ("satinsky", "Satinsky side-biting clamp"),
                    ("bulldog", "Bulldog clamp"),
                    ("potts_scissors", "Potts-Smith angled scissors"),
                    ("castroviejo_nh", "Fine needle holder"),
                    ("aortic_punch", "Aortic punch")],
                   cap="Fig 5.1 — Everything is atraumatic"),
          groups=[
              G("Base set", [
                  ("1", "Major procedures tray",
                   "for exposure of the vessel"),
                  ("1", "Long instruments tray",
                   "for aortic and iliac work"),
              ]),
              G("Vascular clamps — all non-crushing", [
                  ("6", "Bulldog clamps, assorted (DeBakey, Dietrich)",
                   "**signature item** — small spring clips for temporary "
                   "occlusion of small vessels"),
                  ("4", "Satinsky (side-biting) clamps",
                   "**signature item** — allows **partial** occlusion so "
                   "flow continues while a patch or graft is sewn on"),
                  ("4", "Angled DeBakey aortic clamps",
                   "cross-clamping the aorta"),
                  ("4", "Fogarty / Cooley atraumatic clamps",
                   "soft, insert-jawed clamps"),
                  ("2", "Carotid / Javid clamps", "carotid surgery"),
                  ("—", "Vessel loops (silastic) and umbilical tapes",
                   "encircle and gently occlude"),
                  ("—", "Rubber-shod (shodded) clamps",
                   "protects the vessel and graft"),
                  ("—", "Bulldog clamp applier / holder", ""),
              ]),
              G("Atraumatic grasping and dissecting", [
                  ("6", "DeBakey vascular forceps, 15/20/24/30 cm",
                   "**signature item** — longitudinal atraumatic rows, not "
                   "teeth"),
                  ("2", "Gerald forceps, fine", "delicate handling"),
                  ("2", "Potts-Smith angled vascular scissors, 45° and 60°",
                   "**signature item** — extends an arteriotomy accurately"),
                  ("2", "Fine curved Metzenbaum / dissecting scissors", ""),
                  ("2", "Freer / Penfield elevators",
                   "endarterectomy plane dissection"),
                  ("1", "Endarterectomy spatula / dissector",
                   "raises the atheromatous plaque"),
                  ("6", "Long right-angled (Mixter) forceps",
                   "encircling vessels"),
                  ("2", "Nerve hook / vein hook", "lifting side branches"),
              ]),
              G("Opening, flushing and grafting", [
                  ("1", "Knife handle No.7 with No.11 blade",
                   "the arteriotomy is started with a No.11"),
                  ("1", "Aortic punch, sized set",
                   "**signature item** — cuts a clean circular hole for a "
                   "graft anastomosis"),
                  ("—", "**Heparinised saline** with bulb syringe and blunt "
                   "irrigating cannulae",
                   "**signature requirement** — flushes and prevents "
                   "thrombus at every stage"),
                  ("2", "Fogarty embolectomy (balloon) catheters, sized",
                   "**signature item** — withdraws thrombus and embolus"),
                  ("—", "Graft material — PTFE, Dacron, or reversed "
                   "autologous vein", "sized to the vessel"),
                  ("1", "Vein stripper and vein harvesting set",
                   "long saphenous vein harvest"),
                  ("1", "Valvulotome", "in-situ vein bypass"),
                  ("1", "Tunneller",
                   "creates the subcutaneous graft tunnel"),
                  ("—", "Graft sizers and calibrators", ""),
                  ("—", "Topical haemostatic agents and fibrin sealant", ""),
              ]),
              G("Suturing — a distinct discipline", [
                  ("4", "Fine needle holders (Castroviejo, DeBakey pattern)",
                   "delicate, often spring-handled"),
                  ("—", "**Non-absorbable monofilament (polypropylene) "
                   "suture 3-0 to 8-0, double-armed**",
                   "**signature requirement** — never absorbable, never "
                   "braided, in an artery"),
                  ("—", "Teflon pledgets",
                   "buttress sutures in a friable or calcified wall"),
                  ("2", "Fine suture scissors", ""),
                  ("—", "Bulldog clamps on suture ends",
                   "keeps the suture ends controlled"),
                  ("1", "Magnifying loupes", "small-vessel anastomosis"),
              ]),
              G("Monitoring, imaging and pharmacology", [
                  ("1", "Doppler probe (sterile) and machine",
                   "confirms flow before closure"),
                  ("1", "Image intensifier with contrast",
                   "completion angiography"),
                  ("—", "**Systemic heparin and protamine**",
                   "anticoagulation and its reversal"),
                  ("—", "Papaverine / vasodilator", "relieves spasm"),
                  ("—", "**Cross-matched blood and a cell saver**", ""),
                  ("—", "Pressure monitoring lines", ""),
                  ("—", "Closed suction drain", ""),
              ]),
          ],
          extras=[("Position", "Depends on the vessel — supine for aortic, "
                   "carotid (neck extended, turned away) and femoral; "
                   "prone or lateral rarely."),
                  ("Golden rules",
                   "**Proximal control before distal.** Obtain control of "
                   "the vessel above the lesion before opening it. **Never "
                   "grasp the intima.** **Flush before final closure** to "
                   "expel air and debris."),
                  ("Complications",
                   "Haemorrhage, thrombosis of the repair or graft, distal "
                   "embolisation, graft infection, anastomotic "
                   "pseudoaneurysm, reperfusion injury and compartment "
                   "syndrome.")],
          side_box={"title": "Atraumatic means what?",
                    "lines": ["**DeBakey jaws** have fine longitudinal rows "
                              "— they hold without crushing the intima.",
                              "A **toothed forceps on an artery is a "
                              "surgical error**: intimal injury seeds "
                              "thrombosis.",
                              "The same logic makes every vascular clamp "
                              "**non-crushing**."]},
          points=[
              "Open the answer with the principle: **all instruments "
              "atraumatic, all sutures non-absorbable monofilament, "
              "heparinised saline throughout**.",
              "Name **DeBakey forceps, Satinsky clamp, bulldog clamp, "
              "Potts-Smith scissors, Fogarty catheter, aortic punch** — the "
              "six vascular signatures.",
              "**Satinsky = partial (side-biting) occlusion**, so distal "
              "flow is maintained — a favourite distinction.",
              "**Fogarty catheter** for embolectomy and **heparin/"
              "protamine** are reliable marks.",
              "State **proximal control before distal** and **never grasp "
              "the intima**.",
              "**Teflon pledgets** for a friable wall is a detail that "
              "distinguishes a strong answer.",
          ],
          pitfalls=["Suggesting absorbable or braided suture for an "
                    "arterial anastomosis.",
                    "Using toothed forceps on a vessel.",
                    "Forgetting heparinised saline and systemic heparin.",
                    "Omitting completion assessment (Doppler or "
                    "angiography)."],
          qa=[("Enumerate the contents of a vascular procedures tray.",
               "A major and long instruments tray plus: non-crushing clamps "
               "— bulldog, Satinsky side-biting, angled DeBakey aortic, "
               "Fogarty/Cooley, Javid carotid clamps, vessel loops and "
               "rubber-shod clamps; atraumatic DeBakey forceps in several "
               "lengths, Gerald forceps, Potts-Smith angled scissors, "
               "endarterectomy spatula and elevators, Mixter forceps and "
               "vein hooks; No.11 blade, sized aortic punch, heparinised "
               "saline with bulb syringe and cannulae, Fogarty embolectomy "
               "catheters, PTFE/Dacron/vein graft material, vein stripper, "
               "valvulotome and tunneller; fine Castroviejo needle holders "
               "with double-armed polypropylene 3-0 to 8-0 and Teflon "
               "pledgets; plus sterile Doppler, image intensifier with "
               "contrast, heparin and protamine, cross-matched blood, cell "
               "saver and a drain."),
              ("Why is a Satinsky clamp particularly useful?",
               "It is a side-biting clamp that occludes only part of the "
               "vessel circumference, so a patch or graft can be sewn to the "
               "wall while blood continues to flow through the remaining "
               "lumen — avoiding complete occlusion and distal ischaemia.")]),

        # ============================================================ 5.2
        T("5.2", "Vascular Shunt Tray",
          aka="Portosystemic / arteriovenous shunt tray · dialysis access set",
          lead="A **shunt** deliberately diverts blood from one vessel to "
               "another. Two families exist: **portosystemic shunts** for "
               "portal hypertension (portocaval, splenorenal, mesocaval), "
               "and **arteriovenous shunts/fistulae** for haemodialysis "
               "access. Both are built on the vascular tray, with additions "
               "for the specific vessels and shunt material.",
          uses=["Portocaval, mesocaval and distal splenorenal (Warren) shunt "
                "for variceal bleeding",
                "Transjugular intrahepatic portosystemic shunt (TIPS) — "
                "endovascular equivalent",
                "Radiocephalic (Brescia-Cimino) and brachiocephalic "
                "arteriovenous fistula",
                "Arteriovenous graft using PTFE for dialysis access",
                "Temporary intraluminal shunt in vascular trauma to "
                "restore flow",
                "Carotid shunt during endarterectomy"],
          plate=PL("Signature instruments",
                   [("satinsky", "Satinsky clamp — partial occlusion"),
                    ("bulldog", "Bulldog clamps"),
                    ("potts_scissors", "Potts-Smith angled scissors"),
                    ("castroviejo_nh", "Fine needle holder"),
                    ("debakey_forceps", "DeBakey forceps")],
                   cap="Fig 5.2 — Two vessels, one anastomosis"),
          groups=[
              G("Base set", [
                  ("1", "Complete vascular procedures tray",
                   "see 5.1 — the entire set is required"),
                  ("1", "Major and long instruments trays",
                   "for portosystemic (abdominal) shunts"),
              ]),
              G("Shunt material and sizing", [
                  ("—", "PTFE / Dacron graft, 6–10 mm",
                   "interposition portosystemic shunt or AV graft"),
                  ("—", "Reversed autologous vein",
                   "the preferred conduit where suitable"),
                  ("2", "Temporary intraluminal (Javid, Pruitt-Inahara) "
                   "shunts",
                   "**signature item** — maintains distal perfusion while "
                   "the anastomosis is constructed or during trauma repair"),
                  ("—", "Graft sizers, calibrators and tunneller", ""),
                  ("—", "Shunt clamps and shunt-securing tapes", ""),
                  ("1", "Balloon shunt with inflation syringe",
                   "carotid shunting"),
              ]),
              G("Portosystemic shunt additions", [
                  ("2", "Satinsky clamps, large",
                   "partial occlusion of the inferior vena cava"),
                  ("4", "Angled DeBakey / Cooley clamps",
                   "portal vein and superior mesenteric vein"),
                  ("2", "Deep Deaver and malleable retractors",
                   "retroperitoneal exposure"),
                  ("1", "Self-retaining ring retractor", ""),
                  ("—", "**Portal pressure manometry set**",
                   "measures the pressure gradient before and after "
                   "shunting"),
                  ("2", "Long right-angled forceps",
                   "encircling the portal vein"),
                  ("—", "Vessel loops, wide", "portal vein and IVC"),
                  ("1", "Head-light", ""),
                  ("—", "Splenectomy instruments available",
                   "for a splenorenal shunt"),
              ]),
              G("Arteriovenous access additions", [
                  ("1", "Fine (microvascular) instrument set",
                   "radial artery and cephalic vein are 2–4 mm"),
                  ("—", "**Magnifying loupes** or an operating microscope",
                   "**essential** for small-vessel anastomosis"),
                  ("—", "Fine polypropylene 6-0 to 8-0, double-armed", ""),
                  ("2", "Fine bulldog clamps and micro-clamps", ""),
                  ("1", "Vessel dilators, fine, graded",
                   "gently dilates a spastic vessel"),
                  ("—", "Papaverine / lignocaine topical",
                   "relieves vasospasm"),
                  ("1", "Sterile Doppler probe",
                   "**confirms a thrill/bruit before closure**"),
                  ("—", "Tourniquet and arm-board", ""),
                  ("—", "Heparinised saline with fine cannulae", ""),
              ]),
              G("Assessment and closure", [
                  ("1", "Sterile Doppler / flow probe",
                   "patency and flow direction confirmed"),
                  ("1", "Image intensifier with contrast",
                   "completion angiography or shuntogram"),
                  ("—", "Pressure monitoring lines and manometer", ""),
                  ("—", "Heparin and protamine", ""),
                  ("—", "Cross-matched blood and cell saver",
                   "portal hypertension patients bleed and are "
                   "coagulopathic"),
                  ("—", "Closed suction drains", ""),
                  ("—", "Fresh frozen plasma, platelets, vitamin K",
                   "coagulopathy of liver disease"),
              ]),
          ],
          extras=[("Position", "Supine for portocaval (right subcostal or "
                   "midline) and for AV access (arm on an arm-board, "
                   "abducted). Left flank/thoracoabdominal for splenorenal "
                   "shunts."),
                  ("Physiological caution",
                   "A portosystemic shunt diverts portal blood past the "
                   "liver: it relieves variceal bleeding but precipitates "
                   "**hepatic encephalopathy**. **Selective** shunts (distal "
                   "splenorenal) decompress varices while preserving "
                   "portal perfusion and cause less encephalopathy."),
                  ("Maturation of an AV fistula",
                   "A new fistula needs about **6 weeks to mature** before "
                   "it can be cannulated; a graft can be used sooner.")],
          side_box={"title": "Selective versus non-selective",
                    "lines": ["**Non-selective** (portocaval, mesocaval): "
                              "decompresses the whole portal system → "
                              "effective but **high encephalopathy rate**.",
                              "**Selective** (distal splenorenal / Warren): "
                              "decompresses only the gastro-oesophageal "
                              "varices → **less encephalopathy**.",
                              "A very commonly examined distinction."]},
          points=[
              "Divide the answer into **portosystemic** and "
              "**arteriovenous** shunts — the two families have different "
              "additions.",
              "The **temporary intraluminal shunt (Javid, Pruitt-Inahara)** "
              "is the signature item; explain that it maintains distal "
              "perfusion.",
              "For portosystemic shunts include a **portal pressure "
              "manometry set**.",
              "For AV access include **loupes/microscope and fine 6-0 to "
              "8-0 suture** — the vessels are only millimetres wide.",
              "State the **selective vs non-selective** distinction and "
              "**hepatic encephalopathy** as the key complication.",
              "**Doppler confirmation of flow** before closure applies to "
              "both families.",
          ],
          qa=[("What is a vascular shunt tray and how does it differ "
               "according to the type of shunt?",
               "It is a complete vascular tray plus shunt-specific "
               "additions. For portosystemic shunts: large Satinsky and "
               "angled DeBakey/Cooley clamps for the IVC and portal vein, "
               "PTFE or Dacron interposition graft, deep retractors and a "
               "ring retractor, long Mixter forceps, wide vessel loops, a "
               "portal pressure manometry set, head-light and blood "
               "products for coagulopathy. For arteriovenous access: a fine "
               "microvascular set with loupes or a microscope, fine bulldog "
               "and micro-clamps, graded vessel dilators, topical "
               "papaverine, 6-0 to 8-0 double-armed polypropylene, "
               "heparinised saline and a sterile Doppler. Both need "
               "temporary intraluminal shunts, heparin and protamine and "
               "completion imaging."),
              ("Why does a non-selective portosystemic shunt cause "
               "encephalopathy?",
               "It diverts the entire portal venous flow — carrying "
               "nitrogenous products absorbed from the gut — directly into "
               "the systemic circulation, bypassing hepatic detoxification. "
               "Selective shunts decompress only the varices and preserve "
               "portal perfusion of the liver, so encephalopathy is less "
               "frequent.")]),

        # ============================================================ 5.3
        T("5.3", "Cardiac Procedures Tray",
          aka="Open-heart tray · CABG and valve replacement set · "
              "cardiopulmonary bypass tray",
          lead="The **cardiac tray** is the largest and most complex set in "
               "surgery. It combines a **sternotomy set**, a complete "
               "**vascular set**, the **cannulae and lines for "
               "cardiopulmonary bypass**, instruments for the **specific "
               "intracardiac procedure**, and everything needed to "
               "**restart and support the heart**. Its organising idea is "
               "that the circulation is handed over to a machine, the heart "
               "stopped, repaired, and restarted.",
          uses=["Coronary artery bypass grafting (CABG)",
                "Aortic and mitral valve replacement or repair",
                "Repair of congenital defects — ASD, VSD, tetralogy of "
                "Fallot",
                "Ascending aortic and aortic arch replacement; "
                "aortic dissection",
                "Cardiac tumour excision; pulmonary thromboendarterectomy",
                "Heart transplantation and mechanical support device "
                "implantation"],
          plate=PL("Signature instruments",
                   [("sternal_saw", "Sternal saw"),
                    ("finochietto", "Sternal retractor"),
                    ("satinsky", "Aortic cross-clamp"),
                    ("aortic_punch", "Aortic punch — proximal anastomosis"),
                    ("castroviejo_nh", "Fine needle holder"),
                    ("potts_scissors", "Potts-Smith scissors")],
                   cap="Fig 5.3 — Open the sternum, take over the "
                       "circulation, repair, restart"),
          groups=[
              G("Base sets", [
                  ("1", "Complete major procedures tray", ""),
                  ("1", "Complete vascular procedures tray", "see 5.1"),
                  ("1", "Long instruments tray", ""),
              ]),
              G("Sternotomy — opening and closing the chest", [
                  ("1", "Sternal saw (oscillating or reciprocating) with "
                   "spare blades",
                   "**signature item** — median sternotomy"),
                  ("1", "Lebsche knife and mallet",
                   "manual alternative if the saw fails"),
                  ("1", "Sternal (Finochietto / Ankeney) self-retaining "
                   "retractor", "spreads the divided sternum"),
                  ("1", "Internal mammary artery (IMA) retractor",
                   "elevates the sternal edge to harvest the IMA"),
                  ("—", "**Bone wax**", "sternal marrow haemostasis"),
                  ("—", "**Sternal wires** (No.5/No.6) with a heavy needle",
                   "sternal closure"),
                  ("1", "Wire twister, wire cutter and wire holder",
                   "**must be counted — wire fragments are retained "
                   "items**"),
                  ("1", "Sternal punch / awl", "wire passage"),
                  ("1", "Sternal plating set", "for a high-risk sternum"),
              ]),
              G("Cardiopulmonary bypass — the defining group", [
                  ("1", "**CPB circuit: oxygenator, reservoir, heat "
                   "exchanger, arterial pump and tubing**",
                   "**primed and checked by the perfusionist before the "
                   "skin incision**"),
                  ("2", "Aortic cannula with introducer",
                   "arterial return to the aorta"),
                  ("2", "Venous cannulae — single two-stage or bicaval",
                   "drains the right atrium / cavae"),
                  ("1", "Antegrade cardioplegia cannula",
                   "into the aortic root"),
                  ("1", "Retrograde cardioplegia cannula",
                   "into the coronary sinus"),
                  ("1", "Aortic root vent / needle vent",
                   "removes air from the aortic root"),
                  ("1", "Left atrial / ventricular vent", "decompresses the "
                   "left heart"),
                  ("4", "**Aortic cross-clamp and caval (Satinsky) clamps**",
                   "cross-clamping isolates the heart"),
                  ("—", "**Purse-string sutures with tourniquets "
                   "(snuggers)**",
                   "secure each cannula at its insertion site"),
                  ("—", "**Cardioplegia solution, cold, with delivery set**",
                   "arrests the heart in diastole and protects the "
                   "myocardium"),
                  ("—", "Topical cold saline / ice slush", "surface cooling"),
                  ("—", "**Systemic heparin and protamine**",
                   "full heparinisation before cannulation; reversal after "
                   "bypass"),
                  ("—", "ACT (activated clotting time) monitoring", ""),
                  ("1", "Cardiotomy suckers (two) with tubing",
                   "returns shed blood to the circuit"),
              ]),
              G("Coronary bypass (CABG) additions", [
                  ("1", "Internal mammary artery harvesting set",
                   "fine dissecting scissors, clips, IMA retractor"),
                  ("1", "Long saphenous vein harvesting set",
                   "open or endoscopic; vein stripper, fine clips"),
                  ("1", "Radial artery harvest set", ""),
                  ("2", "Coronary (Beaver / micro) knife and blades",
                   "arteriotomy in a 1.5–2 mm coronary artery"),
                  ("2", "Potts-Smith coronary scissors, 45° / 60°",
                   "extending the arteriotomy"),
                  ("1", "Coronary dilators and probes, graded",
                   "sizes the vessel"),
                  ("1", "Aortic punch, sized",
                   "**proximal anastomosis on the aorta**"),
                  ("2", "Coronary bulldog / occluders and silastic slings",
                   "controls the coronary during anastomosis"),
                  ("1", "CO₂ / saline blower-mister",
                   "clears the anastomotic field"),
                  ("—", "**Polypropylene 7-0 / 8-0 double-armed**",
                   "coronary anastomosis"),
                  ("—", "**Magnifying loupes**", "essential"),
              ]),
              G("Valve procedure additions", [
                  ("1", "Valve retractors and leaflet retractors",
                   "exposes the annulus"),
                  ("1", "Valve leaflet excision scissors and rongeur",
                   "excises the diseased valve"),
                  ("1", "Annulus debridement / calcium rongeur", ""),
                  ("1", "**Valve sizers / obturators, complete set**",
                   "**signature item** — selects the prosthesis size"),
                  ("1", "Valve holder and rotator with handle", ""),
                  ("—", "**Prosthetic valves — mechanical and "
                   "bioprosthetic, full size range**",
                   "**confirmed present before bypass begins**"),
                  ("—", "Annuloplasty rings and sizers",
                   "mitral valve repair"),
                  ("—", "Pledgeted mattress sutures, 2-0",
                   "annular fixation"),
                  ("1", "Nerve hook and valve tester", ""),
              ]),
              G("Restarting and supporting the heart", [
                  ("1", "**Internal (sterile) defibrillator paddles**",
                   "**signature requirement** — defibrillates the heart "
                   "directly"),
                  ("—", "**Temporary epicardial pacing wires and external "
                   "pacemaker**",
                   "atrial and ventricular"),
                  ("1", "De-airing needle and vent", "expels intracardiac air"),
                  ("1", "Transoesophageal echocardiography probe",
                   "assesses repair and ventricular function"),
                  ("—", "Inotropes and vasoactive infusions, prepared", ""),
                  ("—", "Intra-aortic balloon pump available",
                   "low cardiac output"),
                  ("—", "Ventricular assist device available",
                   "for failure to wean from bypass"),
                  ("2", "**Mediastinal and pleural chest drains with "
                   "underwater seal**",
                   "always left in place"),
                  ("—", "**Cell saver, cross-matched blood, platelets, "
                   "FFP, cryoprecipitate**", ""),
                  ("—", "**Emergency re-sternotomy set kept at the "
                   "bedside**",
                   "for post-operative tamponade — a critical requirement"),
              ]),
          ],
          extras=[("Position", "Supine, arms tucked; legs prepared and "
                   "exposed for vein harvest; wide skin preparation from "
                   "chin to ankles."),
                  ("Team", "Surgeon, assistants, anaesthetist, "
                   "**perfusionist**, scrub and circulating nurses. The "
                   "perfusionist primes and checks the bypass circuit "
                   "before the incision — an integral part of tray "
                   "preparation."),
                  ("Sequence", "Sternotomy → harvest conduits → "
                   "heparinise → cannulate aorta and right atrium → go on "
                   "bypass → cross-clamp aorta → deliver cardioplegia → "
                   "perform the repair → de-air → release the cross-clamp → "
                   "rewarm → defibrillate/pace as needed → wean from bypass "
                   "→ decannulate → protamine → haemostasis → drains → "
                   "sternal wires."),
                  ("Complications",
                   "Bleeding and re-operation, cardiac tamponade, low "
                   "cardiac output, arrhythmia, stroke and neurocognitive "
                   "injury, renal failure, sternal dehiscence and "
                   "mediastinitis, and heparin-induced "
                   "thrombocytopenia.")],
          side_box={"title": "Count the wire",
                    "lines": ["**Sternal wires, needle fragments and valve "
                              "sizers are all countable items.**",
                              "A broken wire fragment in the mediastinum is "
                              "a classic retained surgical item.",
                              "An **emergency re-sternotomy set stays at "
                              "the bedside** in intensive care for "
                              "tamponade."]},
          mnemonic={"title": "Mnemonic — the five systems of a cardiac tray",
                    "lines": ["**\"S-B-P-V-R\"**",
                              "**S**ternotomy (saw, retractor, wax, wires)",
                              "**B**ypass (cannulae, circuit, cardioplegia, "
                              "clamps)",
                              "**P**rocedure — CABG (conduits, punch, "
                              "coronary set) or valve (sizers, prostheses)",
                              "**V**ascular set (DeBakey, Satinsky, Potts, "
                              "fine suture)",
                              "**R**estart (internal paddles, pacing wires, "
                              "TOE, inotropes, drains)"]},
          points=[
              "Structure the answer as **five systems** — sternotomy, "
              "bypass, procedure-specific, vascular, restart. This is the "
              "only way to cover it completely.",
              "**Cardiopulmonary bypass** items are the defining group: "
              "aortic and venous cannulae, cardioplegia cannulae, aortic "
              "cross-clamp, purse-string sutures with tourniquets, "
              "cardioplegia solution, heparin/protamine.",
              "**Cardioplegia arrests the heart in diastole** and protects "
              "the myocardium — state the purpose, not just the name.",
              "**Internal defibrillator paddles and temporary epicardial "
              "pacing wires** for restarting the heart are commonly "
              "forgotten.",
              "**Sternal wires with wire twister and cutter** — and the fact "
              "that they must be counted.",
              "Mention the **perfusionist** and that the circuit is primed "
              "before incision.",
              "**Emergency re-sternotomy set at the bedside** post-operatively "
              "is a high-value detail.",
          ],
          pitfalls=["Listing instruments without the bypass circuit and "
                    "cannulae.",
                    "Forgetting how the heart is restarted (internal "
                    "paddles, pacing wires).",
                    "Omitting sternal closure items — wax, wires, twister.",
                    "Not confirming prosthesis availability before bypass "
                    "starts."],
          qa=[("Describe the preparation of a cardiac procedures tray.",
               "It comprises five systems. **Sternotomy**: sternal saw with "
               "spare blades, Lebsche knife, sternal self-retaining and IMA "
               "retractors, bone wax, sternal wires with twister, cutter and "
               "punch. **Cardiopulmonary bypass**: a primed circuit with "
               "oxygenator, reservoir and heat exchanger; aortic and venous "
               "cannulae; antegrade and retrograde cardioplegia cannulae; "
               "root and ventricular vents; aortic cross-clamp and caval "
               "clamps; purse-string sutures with tourniquets; cold "
               "cardioplegia; heparin, protamine and ACT monitoring; "
               "cardiotomy suckers. **Procedure-specific**: for CABG — IMA, "
               "saphenous and radial harvest sets, coronary knife, Potts "
               "scissors, coronary dilators, aortic punch, blower-mister, "
               "7-0/8-0 polypropylene and loupes; for valves — valve "
               "retractors, leaflet scissors, calcium rongeur, a complete "
               "set of sizers, valve holder, prostheses and annuloplasty "
               "rings with pledgeted sutures. **Vascular set** in full. "
               "**Restart and support**: internal defibrillator paddles, "
               "temporary epicardial pacing wires with external pacemaker, "
               "de-airing needle, TOE, inotropes, IABP availability, "
               "mediastinal and pleural drains, cell saver and blood "
               "products, and an emergency re-sternotomy set for the "
               "bedside."),
              ("What is the purpose of cardioplegia and how is it "
               "delivered?",
               "Cardioplegia is a cold, high-potassium solution that arrests "
               "the heart in diastole, abolishing electromechanical activity "
               "and greatly reducing myocardial oxygen demand so the "
               "myocardium tolerates the ischaemic period of cross-clamping. "
               "It is delivered antegradely into the aortic root above the "
               "cross-clamp and/or retrogradely through a cannula in the "
               "coronary sinus, and is supplemented by topical cooling.")]),
    ])
