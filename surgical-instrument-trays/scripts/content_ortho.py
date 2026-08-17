#!/usr/bin/env python3
"""Part VI -- Orthopaedic Trays."""
from schema import T, P, PL, DP, FIG, G, CMP

ORTHO = P(
    "VI", "Orthopaedic Trays",
    "Basic orthopaedic · Minor orthopaedic · Hip replacement · "
    "Knee or ankle arthroscopy",
    intro="Orthopaedic trays are unlike all others because the target tissue "
          "is **bone**. Bone must be cut, shaped, held, drilled and fixed, "
          "so the trays carry **osteotomes, chisels, gouges, saws, rasps, "
          "rongeurs, curettes, mallets, bone-holding clamps and powered "
          "instruments**. Two further features are constant: "
          "**intra-operative imaging** and an **uncompromising attitude to "
          "asepsis**, because bone and implant infection is a catastrophe.",
    trays=[

        # ============================================================ 6.1
        T("6.1", "Basic Orthopaedic Procedures Tray",
          aka="Basic bone tray · fracture fixation tray · general "
              "orthopaedic set",
          lead="The **basic orthopaedic tray** is the reference bone set. It "
               "contains the soft-tissue instruments of a major tray plus a "
               "complete range of **bone-cutting, bone-shaping and "
               "bone-holding instruments** and the means to **drill and fix**. "
               "Every other orthopaedic tray in this Part is this set plus "
               "procedure-specific implants and jigs.",
          uses=["Open reduction and internal fixation of long-bone fractures",
                "Plating, screw fixation and intramedullary nailing",
                "Osteotomy and corrective bone surgery",
                "Bone grafting — harvest and application",
                "Debridement and sequestrectomy for osteomyelitis",
                "Amputation; excision of bone tumours",
                "Arthrodesis of a major joint"],
          plate=PL("Signature instruments",
                   [("osteotome", "Osteotome — bevel both sides"),
                    ("chisel", "Chisel — bevel one side"),
                    ("gouge", "Gouge — U-shaped trough"),
                    ("mallet", "Mallet"),
                    ("rongeur", "Bone rongeur"),
                    ("bone_holder", "Bone-holding forceps")],
                   cap="Fig 6.1 — The bone-working core of every "
                       "orthopaedic tray"),
          groups=[
              G("Base set", [
                  ("1", "Major procedures tray",
                   "soft-tissue exposure and closure"),
              ]),
              G("Bone cutting and shaping", [
                  ("6", "Osteotomes, graded widths",
                   "**bevelled on both faces** — cuts through cancellous "
                   "bone, splits and shapes"),
                  ("4", "Chisels, graded widths",
                   "**bevelled on one face only** — cuts a flat surface, "
                   "raises a cortical flake"),
                  ("4", "Gouges, graded widths",
                   "**U-shaped (troughed) blade** — scoops cancellous bone "
                   "and takes bone graft"),
                  ("2", "Mallet, metal and nylon-faced",
                   "**never a hammer** — drives osteotomes and impactors"),
                  ("2", "Bone rongeur (single- and double-action)",
                   "nibbles away bone in small bites"),
                  ("2", "Bone cutting forceps (Liston / Horsley)",
                   "divides small bones"),
                  ("4", "Bone curettes, straight and angled",
                   "removes cancellous bone, granulation and tumour"),
                  ("2", "Bone rasp / file",
                   "smooths a sharp bone edge — prevents soft-tissue injury"),
                  ("1", "Gigli saw with two handles",
                   "flexible wire saw for a through-and-through cut"),
                  ("1", "Amputation / hand saw", ""),
                  ("1", "Oscillating power saw with blades",
                   "the modern method of straight bone division"),
              ]),
              G("Bone holding and reduction", [
                  ("4", "Bone-holding forceps (Lane / Fergusson)",
                   "**signature item** — heavy ratcheted toothed clamps "
                   "gripping the shaft"),
                  ("2", "Bone-holding forceps, self-centring (Lowman)",
                   "holds a plate to the bone"),
                  ("2", "Reduction forceps, pointed (Verbrugge)",
                   "holds fragments reduced"),
                  ("2", "Bone levers / spikes (Trethowan, Bristow)",
                   "levers fragments into position"),
                  ("2", "Periosteal elevator (Farabeuf / Cobb)",
                   "raises periosteum before cutting"),
                  ("1", "Bone hook", "manipulates fragments"),
                  ("2", "Bone clamps, serrated", ""),
              ]),
              G("Drilling and fixation", [
                  ("1", "Power drill with chuck, guard and keys",
                   "battery or air-driven; **sterile motor**"),
                  ("1", "Hand drill (Hudson brace) with drill bits",
                   "back-up if power fails"),
                  ("—", "Drill bits, graded diameters", ""),
                  ("1", "Drill guide (neutral and load) and sleeves",
                   "directs the bit accurately"),
                  ("1", "Depth gauge",
                   "**signature item** — measures the hole so the correct "
                   "screw length is chosen"),
                  ("1", "Tap and tap handle",
                   "cuts a thread for a cortical screw"),
                  ("1", "Countersink", "seats the screw head flush"),
                  ("2", "Screwdrivers — hexagonal, cruciate, "
                   "self-retaining", ""),
                  ("—", "Bone plates — assorted patterns and lengths",
                   "DCP, locking, reconstruction"),
                  ("—", "Screws — cortical, cancellous, locking, assorted "
                   "lengths", "with an organised screw rack"),
                  ("1", "Plate bender and plate-holding forceps",
                   "contours the plate to the bone"),
                  ("—", "Kirschner wires, Steinmann pins and cerclage wire",
                   "with a wire passer, tensioner and cutter"),
                  ("—", "Intramedullary nails with reamers, guidewires and "
                   "jigs", "if nailing is planned"),
                  ("1", "External fixator set",
                   "for open or contaminated fractures"),
              ]),
              G("Irrigation, imaging and accessory", [
                  ("1", "**Pulsatile lavage / irrigation system with warm "
                   "saline**",
                   "**bone debris and marrow must be washed out**"),
                  ("1", "Bone graft harvesting set with a graft container",
                   "usually iliac crest"),
                  ("—", "Bone substitute / allograft chips",
                   "if autograft is insufficient"),
                  ("—", "**Bone wax**", "cancellous bleeding"),
                  ("1", "**Image intensifier (C-arm) with sterile drape**",
                   "**essential** — reduction and implant position confirmed"),
                  ("—", "**Lead aprons and thyroid shields for all staff**",
                   ""),
                  ("1", "**Pneumatic tourniquet with cuff and pressure "
                   "monitor**",
                   "provides a bloodless field; **time must be recorded**"),
                  ("1", "Suction (Yankauer) with wide-bore tubing",
                   "bone debris blocks fine tips"),
                  ("—", "Plaster of Paris / splinting materials",
                   "immobilisation after fixation"),
                  ("—", "Closed suction drain", ""),
                  ("—", "Specimen and microbiology containers",
                   "bone and tissue for culture in infection"),
              ]),
          ],
          extras=[("Position", "Depends on the bone — supine, lateral or "
                   "prone; a fracture table or traction table is used for "
                   "the femur and hip."),
                  ("Tourniquet", "Applied over padding, inflated to about "
                   "**100 mmHg above systolic for the arm and 150 mmHg "
                   "above systolic for the thigh**; safe duration "
                   "approximately **90–120 minutes**, and the **time of "
                   "inflation is recorded and announced**."),
                  ("Asepsis", "Orthopaedic implant surgery uses the "
                   "strictest asepsis — laminar-flow theatre, double "
                   "gloving, impervious gowns, minimal traffic, and "
                   "antibiotic prophylaxis given within 60 minutes of "
                   "incision.")],
          side_box={"title": "The three bevels",
                    "lines": ["**Osteotome** — bevelled on **both** faces; "
                              "cuts and splits.",
                              "**Chisel** — bevelled on **one** face; cuts "
                              "a flat surface.",
                              "**Gouge** — **U-shaped trough**; scoops "
                              "cancellous bone.",
                              "This is the most frequently asked "
                              "orthopaedic distinction — learn it "
                              "verbatim."]},
          compare=CMP(
              ["Instrument", "Blade form", "Action", "Typical use"],
              [["Osteotome", "Bevelled on both sides",
                "Splits along a line", "Cutting cancellous bone, osteotomy"],
               ["Chisel", "Bevelled on one side only",
                "Cuts a flat plane", "Raising a cortical flake, flattening"],
               ["Gouge", "U-shaped trough (concave)",
                "Scoops a channel", "Harvesting cancellous bone graft"],
               ["Rongeur", "Cup-shaped biting jaws",
                "Nibbles small bites", "Trimming bone edges, laminectomy"],
               ["Curette", "Spoon / loop",
                "Scrapes", "Removing granulation, tumour, cancellous bone"],
               ["Rasp / file", "Abrasive cross-hatched face",
                "Abrades", "Smoothing a sharp bone edge"]],
              cap="Table 6.1 — Bone-cutting instruments distinguished by "
                  "blade form"),
          points=[
              "**Osteotome (both bevels) / chisel (one bevel) / gouge "
              "(U-shaped)** — this trio is almost guaranteed to be asked.",
              "A **mallet**, never a hammer, is used with these "
              "instruments.",
              "**Depth gauge → correct screw length** is a small but "
              "commonly rewarded chain of reasoning.",
              "**Image intensifier with lead protection** and a "
              "**pneumatic tourniquet with recorded time** are part of tray "
              "preparation.",
              "**Pulsatile lavage** to remove bone debris and **bone wax** "
              "for cancellous bleeding.",
              "Mention **laminar flow and strict asepsis** because implant "
              "infection is devastating.",
              "A **hand drill (Hudson brace)** is kept as back-up if power "
              "fails.",
          ],
          qa=[("List the bone instruments in a basic orthopaedic tray and "
               "state the use of each.",
               "Osteotomes (bevelled both sides — split and cut cancellous "
               "bone); chisels (bevelled one side — cut a flat surface); "
               "gouges (U-shaped trough — scoop cancellous graft); mallet "
               "(drives them); rongeurs (nibble bone in small bites); bone "
               "cutting forceps (divide small bones); bone curettes (scrape "
               "granulation and cancellous bone); rasp/file (smooth sharp "
               "edges); Gigli and oscillating power saws (divide bone); "
               "bone-holding forceps such as Lane and Lowman and pointed "
               "reduction forceps (grip and reduce fragments); periosteal "
               "elevators and bone levers; and the drilling and fixation "
               "group — power drill with bits, drill guide, depth gauge, "
               "tap, countersink, screwdrivers, plates, screws, K-wires and "
               "cerclage wire."),
              ("Differentiate an osteotome, a chisel and a gouge.",
               "An osteotome is bevelled on both faces and is used to split "
               "and cut cancellous bone along a line; a chisel is bevelled "
               "on one face only and cuts a flat surface or raises a "
               "cortical flake; a gouge has a U-shaped troughed blade and "
               "scoops out cancellous bone, chiefly for harvesting graft.")]),

        # ============================================================ 6.2
        T("6.2", "Minor Orthopaedic Procedures Tray",
          aka="Small bone tray · hand and foot surgery set",
          lead="The **minor orthopaedic tray** is the small-bone equivalent "
               "of the basic set: the same instruments in **fine, short "
               "patterns** for the bones of the hand, wrist, foot and "
               "ankle, together with the fine soft-tissue instruments those "
               "regions demand.",
          uses=["Carpal tunnel and ulnar nerve decompression",
                "Trigger finger and de Quervain's release",
                "Excision of a ganglion; Dupuytren's fasciectomy",
                "Fixation of metacarpal, phalangeal and metatarsal fractures",
                "Hallux valgus correction; hammer-toe correction",
                "Removal of exostoses; K-wire fixation; tendon repair",
                "Removal of superficial orthopaedic implants"],
          plate=PL("Signature instruments",
                   [("scalpel_15", "No.15 blade — small incisions"),
                    ("bone_curette", "Small bone curette"),
                    ("bone_rasp", "Small bone rasp"),
                    ("weitlaner", "Small self-retaining retractor"),
                    ("fine_forceps", "Fine forceps")],
                   cap="Fig 6.2 — The same principles in miniature"),
          groups=[
              G("Base set", [
                  ("1", "Basic / minor procedures tray", "see 1.2"),
              ]),
              G("Small bone instruments", [
                  ("4", "Osteotomes, small (2–8 mm)", ""),
                  ("2", "Chisels, small", ""),
                  ("2", "Gouges, small", ""),
                  ("1", "Mallet, small", ""),
                  ("2", "Bone rongeur, fine (Luer, small)", ""),
                  ("2", "Bone nibbler / small bone cutter", ""),
                  ("4", "Bone curettes, small and angled", ""),
                  ("2", "Small bone rasp / file", ""),
                  ("1", "Small oscillating saw with fine blades", ""),
                  ("2", "Small bone-holding forceps", ""),
                  ("2", "Fine reduction forceps", ""),
                  ("2", "Small periosteal elevator (Freer)", ""),
                  ("1", "Small bone hook and elevator", ""),
              ]),
              G("Fine soft-tissue instruments", [
                  ("2", "Fine (Adson / Gillies) toothed forceps", ""),
                  ("2", "Fine non-toothed forceps", ""),
                  ("2", "Iris and tenotomy scissors, fine", ""),
                  ("2", "Fine curved Metzenbaum scissors", ""),
                  ("8", "Mosquito artery forceps, fine", ""),
                  ("2", "Skin hooks, single and double", ""),
                  ("1", "Small self-retaining (Weitlaner) retractor", ""),
                  ("2", "Small Langenbeck / Senn retractors", ""),
                  ("1", "**Nerve retractor and nerve hook**",
                   "carpal tunnel and nerve decompression"),
                  ("1", "Tendon passer / tendon hook",
                   "tendon repair and transfer"),
                  ("1", "Fine needle holder", ""),
                  ("—", "Fine suture — absorbable and monofilament", ""),
              ]),
              G("Fixation for small bones", [
                  ("—", "Kirschner wires, fine (0.8–1.6 mm)",
                   "with a K-wire driver, bender and cutter"),
                  ("—", "Mini-fragment plates and screws (1.5–2.7 mm)",
                   "with the matching mini instrument set"),
                  ("1", "Mini drill / power driver with fine bits", ""),
                  ("1", "Mini depth gauge and screwdriver", ""),
                  ("—", "Interosseous / cerclage wire, fine", ""),
                  ("—", "Bone graft substitute, small volume", ""),
              ]),
              G("Accessory", [
                  ("1", "**Pneumatic tourniquet — arm or ankle cuff**",
                   "**essential** for a bloodless field in hand and foot "
                   "surgery"),
                  ("1", "Exsanguinating (Rhys-Davies) roll or Esmarch "
                   "bandage", ""),
                  ("1", "**Image intensifier (mini C-arm) with drape**",
                   "small-field fluoroscopy"),
                  ("—", "Lead protection", ""),
                  ("1", "Hand table / arm-board", ""),
                  ("1", "Fine suction (Frazier)", ""),
                  ("1", "Bipolar diathermy",
                   "**bipolar preferred near digital nerves and vessels**"),
                  ("—", "Loupes / magnification", ""),
                  ("—", "Splint / plaster materials", ""),
              ]),
          ],
          side_box={"title": "Why bipolar diathermy",
                    "lines": ["In digits the **nerves and vessels lie "
                              "within millimetres** of the operative field.",
                              "**Bipolar** current passes only between the "
                              "two tips, so there is no spread to adjacent "
                              "structures.",
                              "Monopolar diathermy risks thermal nerve "
                              "injury and, in a digit, tissue loss."]},
          points=[
              "Define this tray as the **basic orthopaedic tray in fine "
              "short patterns** plus fine soft-tissue instruments.",
              "The **pneumatic tourniquet with an exsanguinating roll** is "
              "essential — hand and foot surgery demands a bloodless field.",
              "**K-wires and mini-fragment plates/screws (1.5–2.7 mm)** are "
              "the fixation of small bones.",
              "**Bipolar diathermy** near digital nerves — explain why.",
              "A **hand table** and **mini C-arm** are the practical "
              "additions.",
              "Include the **nerve retractor and nerve hook** for "
              "decompression procedures.",
          ],
          qa=[("How does a minor orthopaedic tray differ from a basic "
               "orthopaedic tray?",
               "It contains the same categories of bone instrument — "
               "osteotomes, chisels, gouges, mallet, rongeurs, curettes, "
               "rasps, saws, bone-holding and reduction forceps and "
               "periosteal elevators — but in **fine, short patterns** "
               "suited to the small bones of the hand, wrist, foot and "
               "ankle. It adds fine soft-tissue instruments (Adson and "
               "Gillies forceps, iris and tenotomy scissors, skin hooks, "
               "nerve retractor and hook, tendon passer), mini-fragment "
               "fixation (K-wires, 1.5–2.7 mm plates and screws with a mini "
               "drill and depth gauge), an arm or ankle pneumatic "
               "tourniquet with an exsanguinating roll, a hand table, mini "
               "C-arm, fine suction, bipolar diathermy and magnification.")]),

        # ============================================================ 6.3
        T("6.3", "Hip Replacement Tray",
          aka="Total hip arthroplasty (THA) tray · hip prosthesis set",
          lead="**Total hip replacement** removes the femoral head and "
               "resurfaces the acetabulum, replacing both with a "
               "prosthesis. The tray is a basic orthopaedic set plus three "
               "additional systems: **instruments to dislocate and resect "
               "the femoral head**, a **matched set of reamers, broaches, "
               "trials and impactors** for the specific implant, and the "
               "**implant itself with cement or cementless fixation**. "
               "Asepsis is at its most rigorous.",
          uses=["Osteoarthritis of the hip — the commonest indication",
                "Rheumatoid and other inflammatory arthritis",
                "Avascular necrosis of the femoral head",
                "Displaced intracapsular neck-of-femur fracture in the "
                "elderly",
                "Failed hemiarthroplasty or previous surgery — revision "
                "arthroplasty",
                "Post-traumatic arthritis; hip dysplasia"],
          plate=PL("Signature instruments",
                   [("bone_holder", "Bone-holding / femoral clamp"),
                    ("osteotome", "Osteotome — capsule and neck"),
                    ("mallet", "Mallet — impaction"),
                    ("bone_rasp", "Rasp / broach — canal preparation"),
                    ("rongeur", "Rongeur — acetabular rim")],
                   cap="Fig 6.3 — Resect, prepare, trial, implant, impact"),
          groups=[
              G("Base set", [
                  ("1", "Complete basic orthopaedic procedures tray",
                   "see 6.1"),
                  ("1", "Major procedures tray", "deep soft-tissue exposure"),
              ]),
              G("Exposure and dislocation", [
                  ("2", "**Hohmann retractors**, assorted",
                   "**signature item** — curved, spiked-tip levers "
                   "retracting around the femoral neck and acetabulum"),
                  ("2", "Charnley / Cobra self-retaining hip retractor",
                   "maintains the deep exposure"),
                  ("2", "Deep Deaver and Langenbeck retractors", ""),
                  ("1", "Bone hook", "dislocating the femoral head"),
                  ("1", "Corkscrew / femoral head extractor",
                   "**signature item** — screws into the head to remove it"),
                  ("2", "Large osteotomes and periosteal elevators",
                   "capsulotomy and soft-tissue release"),
                  ("1", "Femoral neck osteotomy guide and oscillating saw",
                   "resects the neck at the planned level"),
                  ("1", "Femoral elevator / skid",
                   "levers the femur during exposure"),
              ]),
              G("Acetabular preparation", [
                  ("1", "**Acetabular reamers, graded sizes, with a "
                   "T-handle or power reamer**",
                   "**signature item** — hemispherical reamers prepare the "
                   "socket"),
                  ("2", "Acetabular rim rongeur and curettes",
                   "clears osteophytes and residual cartilage"),
                  ("1", "**Acetabular trial cups and sizers**",
                   "confirms fit before the definitive implant"),
                  ("1", "**Cup introducer / positioner with alignment "
                   "guide**",
                   "sets abduction and anteversion angles"),
                  ("1", "Cup impactor and mallet", ""),
                  ("1", "Liner inserter and liner impactor", ""),
                  ("—", "Acetabular screws with drill and screwdriver",
                   "supplementary cup fixation"),
                  ("1", "Pulsatile lavage",
                   "cleans the bone bed before cementing"),
              ]),
              G("Femoral preparation", [
                  ("1", "**Canal finder / box osteotome and canal "
                   "reamers**", "opens and sizes the medullary canal"),
                  ("1", "**Femoral broaches / rasps, graded sizes**",
                   "**signature item** — shape the canal to the stem "
                   "geometry"),
                  ("1", "Canal brush and canal plug / cement restrictor",
                   "contains the cement distally"),
                  ("1", "**Femoral trial stems, heads and neck lengths**",
                   "**trial reduction** assesses leg length, offset and "
                   "stability before the real implant"),
                  ("1", "Stem inserter / introducer and impactor", ""),
                  ("1", "Head impactor", ""),
                  ("1", "Calcar planer / neck trimmer", ""),
                  ("1", "Stem and head extractor",
                   "removal in revision surgery"),
              ]),
              G("The implant and its fixation", [
                  ("—", "**Acetabular cup, liner, femoral stem and head — "
                   "full size range present and checked**",
                   "**the complete range must be confirmed in theatre "
                   "before the incision**"),
                  ("—", "**Bone cement (PMMA) with mixing bowl, spatula, "
                   "vacuum mixer and cement gun**",
                   "for cemented fixation"),
                  ("—", "Antibiotic-loaded cement", "where indicated"),
                  ("—", "Bone graft / allograft chips",
                   "acetabular deficiency"),
                  ("1", "Cement removal set — osteotomes, curettes, "
                   "ultrasonic tools", "revision surgery"),
                  ("—", "Trochanteric wires / cables with tensioner",
                   "if a trochanteric osteotomy is performed"),
              ]),
              G("Asepsis, imaging and accessory", [
                  ("—", "**Laminar-flow theatre, body-exhaust or hood "
                   "suits, double gloving, impervious gowns**",
                   "**periprosthetic infection is catastrophic — asepsis is "
                   "part of tray preparation**"),
                  ("—", "**Antibiotic prophylaxis within 60 minutes of "
                   "incision**", ""),
                  ("1", "Pulsatile lavage with warm saline and antiseptic",
                   ""),
                  ("1", "Image intensifier with drape and lead protection",
                   "component position and leg length"),
                  ("1", "Leg-length measuring device / callipers", ""),
                  ("1", "Wide-bore suction with several tips",
                   "bone debris and cement"),
                  ("—", "**Cross-matched blood and a cell saver**",
                   "blood loss is significant"),
                  ("—", "Closed suction drain", ""),
                  ("—", "Specimen and microbiology containers",
                   "**multiple tissue samples in revision surgery** to "
                   "identify infection"),
                  ("—", "Abduction pillow / brace",
                   "prevents early dislocation post-operatively"),
              ]),
          ],
          extras=[("Position", "**Lateral decubitus** with the operative "
                   "side up, secured in a hip positioner, for the posterior "
                   "and lateral approaches; supine for the direct anterior "
                   "approach."),
                  ("Approaches", "Posterior (commonest; higher dislocation "
                   "risk), direct lateral (Hardinge), and direct anterior "
                   "(muscle-sparing, steeper learning curve)."),
                  ("Complications",
                   "**Dislocation**, periprosthetic infection, "
                   "**venous thromboembolism**, leg-length discrepancy, "
                   "periprosthetic fracture, sciatic or femoral nerve "
                   "injury, aseptic loosening, heterotopic ossification "
                   "and fat embolism during cementing."),
                  ("Trial reduction",
                   "Before the definitive components are implanted, **trial "
                   "components are assembled and the hip reduced** to check "
                   "leg length, offset, range of movement and stability. "
                   "This step is why a complete set of trials is on the "
                   "tray.")],
          side_box={"title": "Sizes must be complete",
                    "lines": ["Trials, reamers, broaches and implants come "
                              "as a **matched, manufacturer-specific "
                              "system**.",
                              "**The whole size range must be present and "
                              "checked before the skin incision** — a "
                              "missing size stops the operation with the "
                              "hip dislocated.",
                              "Implant lot numbers are recorded for "
                              "traceability."]},
          points=[
              "Structure the answer as **exposure → acetabular preparation "
              "→ femoral preparation → implant and fixation → asepsis and "
              "accessory**.",
              "Name **Hohmann retractors** and the **femoral head "
              "corkscrew extractor** — the two most characteristic "
              "instruments.",
              "**Acetabular reamers** and **femoral broaches** are the "
              "preparation signatures.",
              "**Trial components and trial reduction** — explain the "
              "purpose (leg length, offset, stability).",
              "**Bone cement with vacuum mixer and cement gun**, plus a "
              "**cement restrictor**.",
              "**Laminar flow, hood suits, double gloving and antibiotic "
              "prophylaxis** — infection control is examinable content.",
              "In **revision** surgery add a cement-removal set and "
              "**multiple microbiology samples**.",
          ],
          pitfalls=["Not confirming the full implant size range before "
                    "incision.",
                    "Forgetting trial components and the purpose of trial "
                    "reduction.",
                    "Omitting cement preparation equipment.",
                    "Neglecting asepsis and thromboprophylaxis, which carry "
                    "marks."],
          qa=[("Describe the tray for a total hip replacement.",
               "A basic orthopaedic and major tray plus four systems. "
               "**Exposure**: Hohmann retractors, Charnley/Cobra "
               "self-retaining hip retractor, deep hand-held retractors, "
               "bone hook, femoral head corkscrew extractor, large "
               "osteotomes and periosteal elevators, neck osteotomy guide "
               "and oscillating saw. **Acetabulum**: graded hemispherical "
               "reamers, rim rongeur and curettes, trial cups and sizers, "
               "cup positioner with alignment guide, impactors, liner "
               "inserter and acetabular screws. **Femur**: canal finder and "
               "reamers, graded broaches/rasps, canal brush and cement "
               "restrictor, trial stems, heads and neck lengths, stem "
               "inserter, impactors, calcar planer and extractors. "
               "**Implant and fixation**: the full range of cups, liners, "
               "stems and heads checked in advance, bone cement with vacuum "
               "mixer and gun, graft and trochanteric wires. Plus "
               "laminar-flow asepsis with hood suits, antibiotic "
               "prophylaxis, pulsatile lavage, image intensifier, "
               "leg-length callipers, wide-bore suction, cross-matched "
               "blood and cell saver, drain and abduction pillow."),
              ("What is trial reduction and why does it require a separate "
               "set of components?",
               "Trial components — a trial stem, head, neck length and cup "
               "or liner — are assembled and the hip reduced before the "
               "definitive implants are inserted, to verify leg length, "
               "femoral offset, range of movement and stability. A separate "
               "complete set of trials in every size is therefore required, "
               "so the fit can be optimised and the correct definitive "
               "implant selected without compromising a sterile "
               "implant.")]),

        # ============================================================ 6.4
        T("6.4", "Knee or Ankle Arthroscopy Tray",
          aka="Diagnostic and operative arthroscopy set",
          lead="**Arthroscopy** inspects and operates within a joint "
               "through small portals, using a rigid telescope and "
               "continuous fluid **irrigation to distend the joint**. The "
               "tray is a small open set plus a complete **endoscopic "
               "system**: scope and camera, an irrigation/inflow system, "
               "fine hand instruments designed to work through a portal, "
               "and a motorised shaver.",
          uses=["Diagnostic arthroscopy of the knee or ankle",
                "Meniscectomy and meniscal repair",
                "Anterior cruciate ligament reconstruction",
                "Removal of a loose body; synovial biopsy and synovectomy",
                "Chondroplasty, microfracture and cartilage procedures",
                "Ankle arthroscopy for impingement, osteochondral lesions "
                "and debridement",
                "Lavage and debridement in septic arthritis"],
          plate=PL("Signature instruments",
                   [("arthroscope", "Arthroscope, 30° / 70°"),
                    ("trocar", "Cannula and blunt obturator"),
                    ("scalpel_11", "No.11 blade — portal incisions"),
                    ("probe", "Arthroscopic probe / hook")],
                   cap="Fig 6.4 — Distend, visualise, work through portals"),
          groups=[
              G("Base set", [
                  ("1", "Basic / minor procedures tray",
                   "portals and closure"),
                  ("1", "Basic orthopaedic tray available",
                   "for conversion to open surgery"),
              ]),
              G("The arthroscopic system", [
                  ("1", "Arthroscope, 4 mm 30° (knee) and 2.7 mm (ankle)",
                   "**signature item** — 70° available for difficult "
                   "corners"),
                  ("1", "Arthroscope sheath and **blunt obturator**",
                   "**blunt, to avoid scuffing the cartilage on entry**"),
                  ("1", "Fibre-optic light cable and light source", ""),
                  ("1", "Camera head, coupler, control unit and monitor", ""),
                  ("1", "Image recorder / printer", ""),
                  ("—", "Sterile camera and cable drapes", ""),
                  ("1", "Anti-fog solution and warm saline for the lens", ""),
              ]),
              G("Irrigation — the defining requirement", [
                  ("1", "**Arthroscopy fluid pump or gravity inflow set "
                   "with warm normal saline / Ringer's**",
                   "**signature requirement** — the joint must be "
                   "**distended with fluid** to create a working space"),
                  ("1", "Inflow and outflow cannulae with taps", ""),
                  ("—", "Several litres of irrigation fluid",
                   "**fluid balance is monitored** — extravasation causes "
                   "swelling and, rarely, compartment syndrome"),
                  ("1", "Suction tubing and collection system", ""),
              ]),
              G("Portal creation and joint access", [
                  ("1", "Knife handle with No.11 blade",
                   "portal skin incisions"),
                  ("2", "Cannulae with blunt and sharp obturators",
                   "establishes each portal"),
                  ("1", "Switching stick / exchange rod",
                   "moves the scope between portals"),
                  ("1", "Blunt trocar and joint distractor", ""),
                  ("1", "**Ankle / joint distractor or traction device**",
                   "opens the tight ankle joint"),
                  ("1", "Leg holder or lateral post",
                   "stabilises the knee and allows valgus/varus stress"),
              ]),
              G("Hand instruments (long, fine, portal-sized)", [
                  ("1", "Arthroscopic probe / hook",
                   "**the first instrument used** — palpates and assesses "
                   "structures"),
                  ("2", "Arthroscopic punch / basket forceps, straight and "
                   "angled", "excises meniscal tissue"),
                  ("2", "Arthroscopic grasping forceps",
                   "removes loose bodies and fragments"),
                  ("2", "Arthroscopic scissors", ""),
                  ("1", "**Motorised shaver / burr with assorted blades**",
                   "**signature item** — resects synovium, cartilage and "
                   "bone under suction"),
                  ("1", "Radiofrequency / electrothermal probe",
                   "ablation and haemostasis"),
                  ("1", "Curettes and rasps, arthroscopic", ""),
                  ("1", "Microfracture awls", "cartilage stimulation"),
                  ("1", "Meniscal repair set",
                   "all-inside implants, sutures and suture passers"),
                  ("1", "**ACL reconstruction set**",
                   "graft harvest instruments, aiming guides, reamers, "
                   "guidewires, graft tensioner and fixation devices "
                   "(screws, buttons)"),
              ]),
              G("Accessory", [
                  ("1", "**Pneumatic tourniquet with cuff**",
                   "improves the view if bleeding obscures it"),
                  ("1", "Image intensifier",
                   "available for ACL tunnel placement"),
                  ("—", "Local anaesthetic with adrenaline",
                   "portal infiltration; adrenaline reduces bleeding"),
                  ("—", "Fine suture or adhesive strips",
                   "portal closure"),
                  ("—", "Compressive dressing and cryotherapy device", ""),
                  ("—", "Specimen containers",
                   "synovium, cartilage, fluid for microscopy and culture"),
                  ("1", "Wide-bore suction", ""),
              ]),
          ],
          extras=[("Position", "**Knee** — supine with the knee over a "
                   "break in the table or in a leg holder, tourniquet high "
                   "on the thigh. **Ankle** — supine with a bolster under "
                   "the calf, with or without a distraction device."),
                  ("Portals", "Knee: anterolateral (viewing) and "
                   "anteromedial (working), with superomedial for inflow. "
                   "Ankle: anteromedial and anterolateral, avoiding the "
                   "superficial peroneal nerve and dorsalis pedis."),
                  ("Complications",
                   "Haemarthrosis, infection (septic arthritis), "
                   "**iatrogenic cartilage scuffing on entry**, neurovascular "
                   "injury at the portals (saphenous nerve, superficial "
                   "peroneal nerve), fluid extravasation and compartment "
                   "syndrome, thromboembolism, and instrument breakage "
                   "within the joint."),
                  ("Broken instrument",
                   "A fragment of a fine arthroscopic instrument inside the "
                   "joint is a **retained item** and must be retrieved; "
                   "instruments are inspected before and after use.")],
          side_box={"title": "Fluid, not gas",
                    "lines": ["Joints are distended with **saline or "
                              "Ringer's solution**, not with CO₂ as in "
                              "laparoscopy.",
                              "So **inflow, outflow and fluid balance** are "
                              "central to the tray.",
                              "Excess extravasation can cause swelling and, "
                              "rarely, **compartment syndrome** — monitor "
                              "the volumes."]},
          compare=CMP(
              ["", "Laparoscopy", "Arthroscopy"],
              [["Distending medium", "**CO₂ gas**, 12–15 mmHg",
                "**Saline / Ringer's fluid** under pump or gravity"],
               ["Scope", "10 mm 0°/30° laparoscope",
                "4 mm 30° (knee) / 2.7 mm (ankle)"],
               ["Obturator", "Sharp or blunt trocar",
                "**Blunt** — protects cartilage"],
               ["Power instrument", "Ultrasonic / bipolar devices",
                "**Motorised shaver / burr**"],
               ["Main fluid hazard", "Gas embolism, hypercapnia",
                "Extravasation, compartment syndrome"],
               ["Conversion set", "Open laparotomy tray",
                "Open orthopaedic tray"]],
              cap="Table 6.2 — Endoscopic principles compared: the "
                  "distending medium changes everything"),
          points=[
              "The defining requirement is **fluid irrigation to distend "
              "the joint** — contrast this with CO₂ in laparoscopy.",
              "The **obturator is blunt** to avoid scuffing articular "
              "cartilage — a favourite detail.",
              "The **motorised shaver/burr** is the signature working "
              "instrument.",
              "The **probe is the first instrument used** for systematic "
              "assessment.",
              "Mention **fluid balance monitoring** and **compartment "
              "syndrome** as the fluid-related complication.",
              "**Tourniquet, leg holder and a joint distractor for the "
              "ankle** are the positioning aids.",
              "Keep an **open orthopaedic tray available** for conversion, "
              "and note that a **broken instrument fragment is a retained "
              "item**.",
          ],
          qa=[("List the contents of a knee arthroscopy tray.",
               "A minor tray for portals plus: a 4 mm 30° arthroscope (2.7 mm "
               "for ankle, 70° available) with sheath and **blunt** "
               "obturator, light cable and source, camera, monitor and "
               "recorder with anti-fog; an irrigation system — fluid pump or "
               "gravity set with warm saline, inflow and outflow cannulae and "
               "several litres of fluid with balance monitoring; portal "
               "instruments — No.11 blade, cannulae with obturators, "
               "switching stick, leg holder or lateral post and an ankle "
               "distractor; hand instruments — probe/hook, punch and basket "
               "forceps, graspers, scissors, curettes and rasps, motorised "
               "shaver and burr, radiofrequency probe, microfracture awls, "
               "meniscal repair set and an ACL reconstruction set with "
               "guides, reamers and fixation; plus tourniquet, image "
               "intensifier, local anaesthetic with adrenaline, portal "
               "closure materials, compressive dressing, specimen containers "
               "and an open orthopaedic tray for conversion."),
              ("Why is the arthroscope introduced with a blunt obturator?",
               "A sharp trocar would scuff or gouge the articular cartilage "
               "on entry, causing permanent iatrogenic chondral damage. A "
               "blunt obturator pushes the capsule and synovium aside "
               "without cutting the joint surface.")]),
    ])
