#!/usr/bin/env python3
"""Part X -- Paediatric Trays."""
from schema import T, P, PL, DP, FIG, G, CMP

_TRAYS = []

PEDS = P(
    "X", "Paediatric Trays",
    "Paediatric major · Paediatric minor · Paediatric gastrointestinal",
    intro="A child is **not a small adult**, and a paediatric tray is not "
          "merely a smaller tray. Four differences shape every set in this "
          "Part. **Scale** — instruments are shorter, finer and lighter, "
          "and quantities are reduced. **Physiology** — a neonate's total "
          "blood volume is about **80 mL/kg**, so a loss that would be "
          "trivial in an adult is life-threatening; blood loss is measured "
          "by weighing swabs. **Thermoregulation** — a large surface-area "
          "to weight ratio means hypothermia develops within minutes, so "
          "warming is part of tray preparation. **Tissue delicacy** — "
          "structures are millimetres wide, so magnification and fine "
          "atraumatic instruments are the rule.",
    trays=_TRAYS)



# =============================================================== 10.1
_TRAYS.append(T(
    "10.1", "Paediatric Major Procedures Tray",
    aka="Paediatric laparotomy tray · neonatal major set",
    lead="The **paediatric major tray** is the child's equivalent of the "
         "adult major tray (1.1): a complete set covering all six "
         "functional groups for entry into a body cavity, but in **short, "
         "fine, light patterns** and in **smaller numbers**. Its "
         "preparation is dominated less by the instruments themselves than "
         "by the **physiological support** — warming, meticulous blood-loss "
         "measurement and precise fluid management — that must accompany "
         "them.",
    uses=["Neonatal laparotomy — necrotising enterocolitis, malrotation, "
          "atresia",
          "Repair of congenital diaphragmatic hernia; oesophageal atresia "
          "with tracheo-oesophageal fistula",
          "Excision of Wilms' tumour, neuroblastoma and other solid tumours",
          "Splenectomy, nephrectomy and major hepatobiliary surgery in "
          "children",
          "Pull-through procedures for Hirschsprung's disease and "
          "anorectal malformation",
          "Repair of exomphalos and gastroschisis",
          "Major thoracic surgery in children"],
    plate=PL("Signature instruments",
             [("scalpel_15", "No.3 handle + No.15 blade"),
              ("metzenbaum", "Fine Metzenbaum scissors"),
              ("mosquito", "Mosquito forceps — the workhorse"),
              ("debakey_forceps", "Fine DeBakey forceps"),
              ("senn", "Small Senn / Langenbeck retractor"),
              ("frazier", "Fine vented suction")],
             cap="Fig 10.1 — Adult range, paediatric scale"),
    groups=[
        G("Cutting and dissecting", [
            ("2", "Knife handle No.3 with **No.15** blade",
             "**No.15, not No.20** — the incision is short and precise"),
            ("1", "Knife handle No.7, fine", "deep dissection"),
            ("2", "**Metzenbaum scissors, fine 11–14 cm**",
             "the principal dissecting instrument"),
            ("1", "Mayo scissors, small curved", "tougher tissue"),
            ("1", "Iris / tenotomy scissors", "very fine work"),
            ("1", "Suture scissors", ""),
            ("1", "Potts-Smith angled scissors, fine",
             "vessels and duct anastomoses"),
        ]),
        G("Grasping and holding", [
            ("2", "**Adson / fine toothed forceps**", "skin and fascia"),
            ("2", "**DeBakey forceps, fine 13–16 cm**",
             "atraumatic — bowel, vessels, ureter"),
            ("2", "Dressing forceps, fine", ""),
            ("2", "Non-toothed fine forceps", ""),
            ("4", "**Babcock forceps, small**",
             "atraumatic bowel handling"),
            ("4", "Allis forceps, small", ""),
            ("4", "Towel clips, small", ""),
            ("2", "Sponge-holding forceps, small", ""),
        ]),
        G("Clamping and occluding", [
            ("12", "**Mosquito (Halsted) forceps, curved — the "
                   "workhorse**",
             "**signature point** — in paediatric surgery the mosquito "
             "replaces the Crile as the standard haemostat"),
            ("6", "Crile forceps, small 12–14 cm", ""),
            ("4", "Right-angled (Mixter) forceps, fine",
             "encircling small pedicles"),
            ("4", "**Bulldog clamps, small**",
             "vascular occlusion in vessels 2–3 mm wide"),
            ("4", "**Non-crushing (Doyen-type) intestinal clamps, small**",
             "bowel that must survive"),
            ("2", "Kocher clamps, small", "crushing, specimen side"),
            ("—", "**Ligating clips, small and micro, with appliers**",
             "often safer and faster than ties on tiny vessels"),
        ]),
        G("Exposing and retracting", [
            ("2", "**Senn and small Langenbeck retractors**", ""),
            ("2", "Army-Navy retractors, small", ""),
            ("2", "**Malleable retractors, narrow (1–2 cm)**",
             "protects viscera"),
            ("1", "**Small self-retaining retractor — Weitlaner, "
                  "Denis Browne ring or a small Balfour**",
             "**signature item** — the Denis Browne ring retractor with "
             "assorted small blades is the classic paediatric "
             "self-retainer"),
            ("2", "Skin hooks, fine", ""),
            ("2", "Small Deaver retractors", ""),
            ("1", "Head-light", ""),
            ("1", "Magnifying loupes", "**routinely used in neonates**"),
        ]),
        G("Suturing", [
            ("2", "**Needle holders, fine 13–15 cm**", ""),
            ("1", "Castroviejo / micro needle holder",
             "vascular and duct anastomoses"),
            ("—", "**Fine suture — 4-0 to 7-0 absorbable; 5-0 to 7-0 "
                  "monofilament**",
             "**heavier suture cuts through neonatal tissue**"),
            ("—", "Fine vascular suture 6-0 to 8-0", ""),
            ("—", "Absorbable subcuticular skin suture",
             "avoids the distress of suture removal"),
        ]),
        G("Suction and accessory", [
            ("2", "**Fine suction tips (Frazier) with a thumb vent**",
             "**signature item** — the vent limits the force applied to "
             "friable neonatal tissue; **a Poole tip is too large**"),
            ("1", "Small Yankauer tip", ""),
            ("—", "**Low-suction, small-volume reservoir with graduated "
                  "measurement**",
             "**every millilitre of loss is measured**"),
            ("1", "**Bipolar diathermy with fine tips, low power "
                  "settings**",
             "**bipolar preferred; monopolar spreads through a small body**"),
            ("—", "**Paediatric electrosurgical return electrode**",
             "correctly sized for the child's weight"),
            ("—", "**Small radio-opaque swabs and gauze, counted, and a "
                  "weighing scale**",
             "**signature requirement** — swabs are **weighed** to quantify "
             "blood loss"),
            ("—", "Small kidney dish, gallipots and specimen containers",
             ""),
            ("—", "Fine feeding tubes, infant catheters and small drains",
             ""),
        ]),
        G("Physiological support — inseparable from the tray", [
            ("—", "**Forced-air or radiant warmer, warming mattress and "
                  "overhead heater**",
             "**signature requirement** — hypothermia occurs within "
             "minutes"),
            ("—", "**Warmed irrigation fluid, warmed intravenous fluids and "
                  "a fluid warmer**", ""),
            ("—", "**Raised theatre ambient temperature (24–26 °C for "
                  "neonates)**", ""),
            ("—", "**Temperature probe and continuous core temperature "
                  "monitoring**", ""),
            ("—", "**Cross-matched blood in paediatric aliquots**",
             "**neonatal blood volume ≈ 80 mL/kg — a 30 mL loss in a 2 kg "
             "baby is nearly 20 % of the circulating volume**"),
            ("—", "**Volumetric infusion pumps and syringe drivers**",
             "fluids are given in millilitres per kilogram"),
            ("—", "**Padding, gel supports and eye protection**",
             "pressure injury occurs quickly in a small body"),
            ("—", "**Glucose monitoring**",
             "neonates have limited glycogen reserve"),
            ("—", "Neonatal resuscitation equipment", ""),
        ]),
    ],
    extras=[("Position", "Supine on a warming mattress with the limbs "
             "padded and secured; small rolls rather than sandbags. The "
             "child is positioned to give access while **preserving "
             "temperature** — exposure is kept to the minimum area and "
             "duration."),
            ("Consent and identification",
             "Consent is by the parent or legal guardian; identity, weight "
             "and the operative side are confirmed at the WHO checklist. "
             "**The weight is documented because every drug, fluid and "
             "blood volume is calculated from it.**"),
            ("Complications",
             "**Hypothermia**, hypoglycaemia, fluid overload or depletion, "
             "**relatively rapid haemorrhagic shock**, anastomotic leak, "
             "pressure injury, and — with monopolar diathermy — "
             "disproportionate thermal spread.")],
    side_box={"title": "The three paediatric constants",
              "lines": ["**Warm** — warming mattress, overhead heater, "
                        "warmed fluids, theatre at 24–26 °C.",
                        "**Measure** — weigh the swabs; blood volume is "
                        "only about **80 mL/kg**.",
                        "**Miniaturise** — short fine instruments, mosquito "
                        "forceps as the workhorse, 4-0 to 7-0 suture, fine "
                        "vented suction.",
                        "Quote these three in any paediatric tray answer."]},
    compare=CMP(
        ["Feature", "Adult major tray", "Paediatric major tray"],
        [["Skin blade", "No.20 on a No.4 handle",
          "**No.15 on a No.3 handle**"],
         ["Standard haemostat", "Crile / Kelly",
          "**Mosquito (Halsted)**"],
         ["Suture calibre", "0 to 3-0", "**4-0 to 7-0**"],
         ["Suction", "Poole + Yankauer",
          "**Fine vented Frazier**, small graduated reservoir"],
         ["Self-retainer", "Balfour with bladder blade",
          "**Denis Browne ring retractor** / small Weitlaner"],
         ["Blood-loss assessment", "Estimated volume in the reservoir",
          "**Swabs weighed; loss calculated against 80 mL/kg**"],
         ["Temperature control", "Routine warming",
          "**Active warming is essential and continuous**"]],
        cap="Table 10.1 — Adult versus paediatric major tray"),
    points=[
        "Open with the principle: **a child is not a small adult** — then "
        "give scale, physiology, thermoregulation and tissue delicacy.",
        "**No.15 blade, mosquito forceps as the workhorse, 4-0 to 7-0 "
        "suture, fine vented Frazier suction** are the concrete "
        "substitutions.",
        "**Denis Browne ring retractor** is the classic paediatric "
        "self-retaining retractor.",
        "**Weigh the swabs** and quote **blood volume ≈ 80 mL/kg** — the "
        "most reliably rewarded facts in this Part.",
        "**Active warming (mattress, overhead heater, warmed fluids, "
        "theatre 24–26 °C) is part of tray preparation.**",
        "**Bipolar diathermy at low settings with a correctly sized return "
        "electrode.**",
        "**Loupes are routine** in neonatal work.",
    ],
    qa=[("How does a paediatric major tray differ from an adult major tray?",
         "It contains the same six functional groups but in short, fine, "
         "light patterns and smaller quantities: a No.15 blade on a No.3 "
         "handle instead of a No.20 on a No.4; fine 11–14 cm Metzenbaum "
         "scissors; mosquito forceps as the standard haemostat rather than "
         "Crile or Kelly; fine DeBakey and Adson forceps, small Babcock and "
         "small non-crushing intestinal clamps, small bulldogs and micro "
         "clips; Senn, small Langenbeck, narrow malleable and a Denis Browne "
         "ring or small Weitlaner self-retaining retractor with loupes and a "
         "head-light; fine 13–15 cm needle holders with 4-0 to 7-0 suture; "
         "and fine vented Frazier suction with a small graduated reservoir. "
         "Beyond instruments it requires active warming — warming mattress, "
         "overhead heater, warmed fluids and theatre at 24–26 °C — "
         "continuous temperature monitoring, bipolar diathermy at low power "
         "with a correctly sized return electrode, volumetric pumps, glucose "
         "monitoring, cross-matched blood in paediatric aliquots and "
         "**weighing of swabs** to measure blood loss against a circulating "
         "volume of only about 80 mL/kg."),
        ("Why is blood loss measured by weighing swabs in paediatric "
         "surgery?",
         "Because a neonate's total blood volume is only about 80 mL/kg — "
         "roughly 240 mL in a 3 kg baby — so a loss of 25–30 mL, which would "
         "be visually negligible in an adult, represents more than 10 % of "
         "the circulating volume. Visual estimation is far too imprecise, so "
         "swabs are weighed (1 g ≈ 1 mL) and suction volumes measured in "
         "small graduated reservoirs to allow accurate, timely "
         "replacement.")]))



# =============================================================== 10.2
_TRAYS.append(T(
    "10.2", "Paediatric Minor Procedures Tray",
    aka="Paediatric minor set · children's day-case tray",
    lead="The **paediatric minor tray** is the commonest tray in a "
         "children's theatre. It is the adult basic/minor tray (1.2) in "
         "**fine short patterns**, used for the high-volume day-case "
         "operations of childhood — hernia, hydrocele, circumcision, "
         "undescended testis and minor lumps. Its instruments are simple; "
         "what distinguishes it is **delicacy of handling** and the same "
         "warming and blood-loss discipline as the major tray.",
    uses=["Inguinal herniotomy — the commonest paediatric operation",
          "Hydrocele repair; ligation of a patent processus vaginalis",
          "Orchidopexy for undescended testis",
          "Circumcision; release of preputial adhesions; meatotomy",
          "Excision of a lymph node, dermoid, thyroglossal or branchial "
          "remnant",
          "Incision and drainage of an abscess; wound debridement",
          "Insertion of a central venous line or port; muscle biopsy",
          "Tongue-tie division (frenotomy)"],
    plate=PL("Signature instruments",
             [("scalpel_15", "No.3 handle + No.15 blade"),
              ("mosquito", "Mosquito forceps, curved"),
              ("adson", "Adson fine toothed forceps"),
              ("iris_scissors", "Fine scissors"),
              ("senn", "Small Senn retractor"),
              ("needle_holder", "Fine needle holder")],
             cap="Fig 10.2 — Small, simple and used in large numbers"),
    groups=[
        G("Cutting and dissecting", [
            ("2", "Knife handle No.3 with **No.15** blade", ""),
            ("1", "**Fine Metzenbaum scissors, 11–13 cm**",
             "opening the inguinal canal, dissecting the sac"),
            ("1", "Iris / tenotomy scissors, fine",
             "very fine trimming"),
            ("1", "Small Mayo scissors, curved", ""),
            ("1", "Suture scissors", ""),
            ("1", "Small artery-forceps-mounted swab (peanut)",
             "blunt dissection of the sac"),
        ]),
        G("Grasping and holding", [
            ("2", "**Adson forceps, 1×2 teeth**", "skin"),
            ("2", "Fine non-toothed / DeBakey forceps",
             "**atraumatic — the vas and vessels are handled with these**"),
            ("2", "Fine dressing forceps", ""),
            ("4", "Small Allis forceps",
             "the hernial sac and wound edges"),
            ("4", "Small towel clips", ""),
            ("2", "Small sponge-holding forceps", ""),
        ]),
        G("Clamping", [
            ("10", "**Mosquito forceps, curved — the principal "
                   "haemostat**", ""),
            ("4", "Crile forceps, small", ""),
            ("2", "Small Kocher clamps", ""),
        ]),
        G("Retracting", [
            ("2", "**Senn (double-ended) retractors**",
             "the standard paediatric small retractor"),
            ("2", "Small Langenbeck retractors", ""),
            ("2", "Army-Navy retractors, small", ""),
            ("2", "**Skin hooks, fine**", ""),
            ("1", "Small Weitlaner self-retaining retractor", ""),
            ("1", "**Magnifying loupes**",
             "**the vas deferens in an infant is about 1 mm across**"),
        ]),
        G("Suturing", [
            ("2", "**Needle holders, fine 13 cm**", ""),
            ("—", "**4-0 to 6-0 absorbable suture**",
             "sac transfixion, muscle and subcutaneous layers"),
            ("—", "**5-0 / 6-0 absorbable subcuticular for skin**",
             "**avoids the distress of suture removal in a child**"),
            ("—", "Tissue adhesive / adhesive strips",
             "atraumatic skin closure"),
        ]),
        G("Procedure-specific additions", [
            ("1", "**Circumcision instruments — Mogen or Gomco clamp, "
                  "Plastibell in assorted sizes, or a dorsal-slit set**",
             "**signature item** for circumcision"),
            ("2", "**Fine probe / sinus forceps**",
             "separating preputial adhesions"),
            ("1", "**Orchidopexy items — fine non-toothed forceps, small "
                  "Langenbeck retractors and a Dartos-pouch dissector**",
             ""),
            ("1", "**Nerve stimulator**",
             "identifies nerves in neck and limb procedures"),
            ("1", "Fine grooved director and probe",
             "sinus and fistula tracts"),
            ("—", "**Small drains, infant feeding tubes and catheters**",
             ""),
            ("1", "Frenotomy scissors and grooved retractor",
             "tongue-tie division"),
        ]),
        G("Accessory and physiological support", [
            ("1", "**Fine vented suction (Frazier)**", ""),
            ("1", "**Bipolar diathermy, fine tips, low power**",
             "**essential near the vas, testicular vessels and in a "
             "circumcision**"),
            ("—", "**Correctly sized paediatric return electrode**", ""),
            ("—", "**Small radio-opaque swabs, counted, with a weighing "
                  "scale**", ""),
            ("—", "**Warming mattress, overhead heater and warmed "
                  "fluids**",
             "**even a short day-case procedure cools an infant**"),
            ("—", "**Local anaesthetic for infiltration or a caudal / "
                  "ilioinguinal block**",
             "weight-calculated dose; **reduces opioid requirement and "
             "speeds discharge**"),
            ("—", "Small kidney dish, gallipot and specimen containers", ""),
            ("—", "Non-adherent dressings and hypoallergenic tape",
             "**adhesive dressings damage neonatal skin**"),
        ]),
    ],
    extras=[("Position", "Supine on a warming mattress; a small roll under "
             "the hips for inguinal and genital surgery. Limbs padded and "
             "gently secured; minimal exposure to preserve temperature."),
            ("Herniotomy in a child",
             "A child's inguinal hernia is a **patent processus vaginalis** "
             "and is treated by **simple high ligation of the sac "
             "(herniotomy)** — **no mesh and no repair of the canal**, "
             "unlike the adult operation. This distinction is very commonly "
             "examined alongside the tray."),
            ("Local anaesthetic doses",
             "All doses are **weight-based** and the maximum is calculated "
             "and stated before injection (for example lignocaine "
             "3 mg/kg, or 7 mg/kg with adrenaline; bupivacaine 2 mg/kg)."),
            ("Complications",
             "Recurrence, injury to the **vas deferens or testicular "
             "vessels** with testicular atrophy, iatrogenic ascent of the "
             "testis, haematoma, infection, hypothermia, and — in "
             "circumcision — bleeding, meatal stenosis and excessive or "
             "insufficient skin removal.")],
    side_box={"title": "Herniotomy, not hernioplasty",
              "lines": ["In a child the hernia is a **patent processus "
                        "vaginalis**.",
                        "Treatment is **high ligation of the sac alone — "
                        "herniotomy**.",
                        "**No mesh, no canal repair** — the adult operation "
                        "is quite different.",
                        "Hence the tray needs only fine dissecting "
                        "instruments and transfixion suture."]},
    points=[
        "Define it as the **adult minor tray in fine short patterns** for "
        "high-volume day-case work.",
        "**Mosquito forceps and Senn retractors** dominate; **loupes** are "
        "used because the vas is about **1 mm** wide.",
        "**Absorbable subcuticular skin closure or tissue adhesive** — no "
        "suture removal in a child.",
        "**Herniotomy = high ligation of the sac only**; no mesh — state "
        "this contrast explicitly.",
        "Name the **circumcision devices (Mogen, Gomco, Plastibell)** as "
        "procedure-specific additions.",
        "**Bipolar at low power** near the vas and vessels.",
        "**Warming and swab weighing apply even to short day cases.**",
        "**Weight-based local anaesthetic dose** and regional blocks.",
    ],
    qa=[("Describe the paediatric minor procedures tray.",
         "The adult minor tray in fine short patterns: No.3 handle with "
         "No.15 blade, fine 11–13 cm Metzenbaum, iris and small Mayo "
         "scissors and peanut swabs; Adson fine toothed, fine DeBakey and "
         "dressing forceps with small Allis forceps, towel clips and sponge "
         "holders; about ten curved mosquito forceps as the principal "
         "haemostat with small Crile and Kocher clamps; Senn, small "
         "Langenbeck and Army-Navy retractors, fine skin hooks, a small "
         "Weitlaner and magnifying loupes; fine 13 cm needle holders with "
         "4-0 to 6-0 absorbable suture and 5-0/6-0 absorbable subcuticular "
         "skin closure or tissue adhesive. Procedure-specific additions "
         "include circumcision devices (Mogen or Gomco clamp, Plastibell), "
         "fine probes for preputial adhesions, orchidopexy instruments, a "
         "nerve stimulator, grooved director and small drains. Accessory: "
         "fine vented Frazier suction, low-power bipolar diathermy with a "
         "correctly sized return electrode, counted small radio-opaque swabs "
         "with a weighing scale, warming mattress and warmed fluids, "
         "weight-calculated local anaesthetic for infiltration or a caudal "
         "block, and non-adherent dressings."),
        ("How does the surgical treatment of an inguinal hernia in a child "
         "differ from that in an adult, and how does this affect the tray?",
         "In a child the hernia results from a patent processus vaginalis, "
         "so treatment is **herniotomy — simple high ligation and division "
         "of the sac** — without mesh or repair of the inguinal canal. The "
         "tray therefore needs only fine dissecting instruments (fine "
         "Metzenbaum scissors, peanut swabs, atraumatic non-toothed forceps "
         "and loupes to identify the 1 mm vas and testicular vessels) and "
         "fine absorbable transfixion suture, rather than the mesh, tackers "
         "and heavier instruments of an adult hernioplasty.")]))



# =============================================================== 10.3
_TRAYS.append(T(
    "10.3", "Paediatric Gastrointestinal Procedures Tray",
    aka="Paediatric bowel tray · neonatal GI anastomosis set",
    lead="The **paediatric GI tray** applies the adult rule — **crushing "
         "clamps only on the specimen side, non-crushing on bowel that must "
         "survive** — to a bowel that may be **only a few millimetres in "
         "diameter and paper-thin**. Because staplers are usually too large "
         "for neonatal bowel, anastomoses are **hand-sewn with 5-0 to 7-0 "
         "suture under magnification**, and this, together with "
         "contamination control and stoma provision, defines the tray.",
    uses=["Bowel resection and anastomosis for atresia, stenosis or "
          "malrotation",
          "Necrotising enterocolitis — resection, stoma or drainage",
          "Hirschsprung's disease — biopsy, levelling biopsies and "
          "pull-through",
          "Anorectal malformation — colostomy and definitive repair",
          "Pyloromyotomy (Ramstedt) for infantile hypertrophic pyloric "
          "stenosis",
          "Repair of gastroschisis and exomphalos",
          "Meconium ileus; intussusception requiring operation",
          "Formation, revision and closure of an ileostomy or colostomy"],
    plate=PL("Signature instruments",
             [("intestinal_clamp", "Small non-crushing bowel clamp"),
              ("babcock", "Small Babcock forceps"),
              ("debakey_forceps", "Fine DeBakey forceps"),
              ("mosquito", "Mosquito forceps"),
              ("castroviejo_nh", "Fine / micro needle holder")],
             cap="Fig 10.3 — Atraumatic handling of millimetre-wide bowel"),
    groups=[
        G("Base set", [
            ("1", "Complete paediatric major procedures tray", "see 10.1"),
        ]),
        G("Bowel clamps — the defining group", [
            ("4", "**Non-crushing (Doyen-type) intestinal clamps, small and "
                  "fine**",
             "**signature item** — applied only to bowel that will be "
             "**retained**"),
            ("4", "**Rubber-shod mosquito or Crile forceps / clamp guards**",
             "**signature item** — in a neonate even a small Doyen may be "
             "too heavy; a rubber-shod fine clamp is gentler still"),
            ("2", "Small crushing (Kocher / Payr-type) clamps",
             "**specimen side only**"),
            ("4", "**Small Babcock forceps**",
             "atraumatic traction on bowel, appendix and tube"),
            ("4", "**Fine DeBakey forceps**",
             "the instrument that actually holds the bowel wall"),
            ("2", "Fine right-angled forceps", "mesenteric vessels"),
            ("—", "**Soft slings / umbilical tapes, fine**",
             "gentle bowel retraction instead of a clamp"),
        ]),
        G("Anastomosis — hand-sewn, under magnification", [
            ("2", "**Fine needle holders 13 cm and a micro (Castroviejo) "
                  "needle holder**", ""),
            ("—", "**5-0, 6-0 and 7-0 absorbable suture on a fine "
                  "round-bodied (taper) needle**",
             "**signature requirement** — **single-layer interrupted "
             "extramucosal (seromuscular) anastomosis** is standard in "
             "neonates"),
            ("—", "**Stay sutures, fine**",
             "hold the ends in apposition and rotate the anastomosis"),
            ("2", "**Magnifying loupes (2.5–4×) or the operating "
                  "microscope**",
             "**signature requirement** — a neonatal duodenum may be 5 mm "
             "wide"),
            ("2", "Fine curved and Potts-Smith angled scissors", ""),
            ("1", "**Bougies / sizing catheters, small**",
             "calibrates the anastomosis and excludes distal obstruction"),
            ("—", "**Small stapling devices only if size-appropriate**",
             "**most neonatal staplers are too large — say so explicitly**"),
            ("—", "Fibrin sealant", "reinforces a delicate anastomosis"),
        ]),
        G("Procedure-specific additions", [
            ("1", "**Pyloromyotomy spreader (Benson) and pyloric "
                  "knife/blade**",
             "**signature item** for Ramstedt pyloromyotomy — the "
             "hypertrophied muscle is split and spread **without breaching "
             "the mucosa**"),
            ("1", "**Rectal / suction biopsy instrument (Noblett)**",
             "**signature item** — obtains submucosa for ganglion cells in "
             "Hirschsprung's disease"),
            ("—", "**Separate labelled specimen pots for levelling "
                  "biopsies**",
             "**each seromuscular biopsy is labelled with its distance from "
             "the anal verge** to locate the transition zone"),
            ("1", "**Anal dilators, graded small; Hegar dilators, small**",
             "pull-through and post-operative dilatation"),
            ("1", "Small self-retaining anal retractor", ""),
            ("1", "**Silo bag and applicator**",
             "staged reduction of gastroschisis"),
            ("—", "**Stoma appliances, paediatric, with a marking pen**",
             ""),
            ("—", "Contrast medium and image intensifier",
             "on-table contrast study"),
            ("—", "Frozen-section facility",
             "**confirms ganglion cells before the pull-through "
             "anastomosis**"),
        ]),
        G("Contamination control", [
            ("—", "**Separate 'dirty' bowel-technique instrument set**",
             "used after the bowel is opened, then removed from the field"),
            ("—", "**Small warm moist packs and drapes to isolate the "
                  "bowel**", ""),
            ("—", "**Dedicated fine suction tip for enteric content**", ""),
            ("—", "Antiseptic-soaked small swabs",
             "cleansing the divided ends"),
            ("—", "**Separate specimen and 'dirty' receivers**", ""),
            ("—", "**Change of gloves after the enteric stage**", ""),
            ("—", "Culture swabs",
             "peritoneal fluid in necrotising enterocolitis"),
        ]),
        G("Physiological support — critical in this group", [
            ("—", "**Nasogastric / orogastric tube, size-appropriate**",
             "decompression is essential in obstruction"),
            ("—", "**Warming mattress, overhead heater, warmed irrigation "
                  "and warmed intravenous fluids; theatre at 24–26 °C**",
             "**exposed bowel loses heat and fluid extremely rapidly**"),
            ("—", "**Continuous core temperature monitoring**", ""),
            ("—", "**Volumetric pumps and syringe drivers; fluids in "
                  "mL/kg**", ""),
            ("—", "**Cross-matched blood in paediatric aliquots**",
             "blood volume ≈ **80 mL/kg**"),
            ("—", "**Small counted radio-opaque swabs with a weighing "
                  "scale**",
             "**swabs weighed to quantify loss**"),
            ("—", "**Glucose monitoring and dextrose infusion**", ""),
            ("—", "**Parenteral nutrition access — central line or PICC**",
             "prolonged ileus is expected after neonatal bowel surgery"),
            ("—", "Neonatal resuscitation equipment and a transport "
                  "incubator", ""),
        ]),
    ],
    extras=[("Position", "Supine on a warming mattress; lithotomy or prone "
             "for anorectal and pull-through procedures. Exposure is kept "
             "to the minimum area to preserve temperature."),
            ("Ramstedt pyloromyotomy",
             "The **seromuscular layer of the pylorus is incised and spread "
             "with a Benson spreader until the mucosa pouts through, "
             "intact**. The tray must therefore include the spreader and a "
             "means of **testing mucosal integrity** (insufflating air "
             "through the nasogastric tube). A breached mucosa must be "
             "recognised and repaired at once."),
            ("Hirschsprung's levelling biopsies",
             "Seromuscular biopsies are taken at intervals and sent for "
             "**frozen section** to find the level at which ganglion cells "
             "appear. **Each pot must be separately labelled with its "
             "distance from the anal verge** — mislabelling leads to "
             "resection at the wrong level."),
            ("Complications",
             "Anastomotic leak and stricture, **mucosal perforation in "
             "pyloromyotomy**, adhesive obstruction, short-bowel syndrome, "
             "stoma complications, wound dehiscence, sepsis, hypothermia and "
             "hypoglycaemia, and prolonged parenteral-nutrition "
             "dependence.")],
    side_box={"title": "Why hand-sewn, not stapled",
              "lines": ["Neonatal bowel may be **5–10 mm in diameter with a "
                        "wall under 1 mm thick**.",
                        "Standard staplers are **too large and too "
                        "traumatic** and would narrow the lumen.",
                        "So anastomoses are **hand-sewn, single-layer "
                        "interrupted extramucosal, with 5-0 to 7-0 suture "
                        "under loupes**.",
                        "Stating this explicitly distinguishes a strong "
                        "answer."]},
    points=[
        "Restate the **crushing versus non-crushing** rule, then explain "
        "that in a neonate even a Doyen may be too heavy — hence "
        "**rubber-shod fine clamps**.",
        "**Anastomoses are hand-sewn, single-layer interrupted "
        "extramucosal, 5-0 to 7-0, under loupes** — staplers are usually "
        "too large.",
        "**Benson pyloromyotomy spreader** and **testing mucosal "
        "integrity** for Ramstedt's operation.",
        "**Noblett suction rectal biopsy** and **separately labelled "
        "levelling biopsies with frozen section** for Hirschsprung's.",
        "**Contamination control with a separate 'dirty' set and glove "
        "change.**",
        "**Warming, swab weighing and 80 mL/kg** — the paediatric "
        "constants apply with even greater force when bowel is exposed.",
        "**Nasogastric decompression and central access for parenteral "
        "nutrition** are part of preparation.",
    ],
    pitfalls=["Applying a crushing clamp to bowel that will be retained.",
              "Assuming adult staplers can be used in a neonate.",
              "Failing to label levelling biopsies with the distance from "
              "the anal verge.",
              "Omitting warming, swab weighing and glucose monitoring.",
              "Forgetting to test mucosal integrity after pyloromyotomy."],
    qa=[("Describe the paediatric gastrointestinal procedures tray.",
         "A complete paediatric major tray plus: **bowel clamps** — small "
         "fine non-crushing Doyen-type clamps and rubber-shod fine clamps "
         "for retained bowel, small crushing clamps for the specimen side, "
         "small Babcock and fine DeBakey forceps, fine right-angled forceps "
         "and soft slings; **anastomosis** — fine and micro needle holders "
         "with 5-0 to 7-0 absorbable suture on fine round-bodied needles for "
         "a single-layer interrupted extramucosal anastomosis, stay sutures, "
         "loupes or the microscope, fine curved and Potts scissors, small "
         "sizing bougies, size-appropriate staplers only if suitable, and "
         "fibrin sealant; **procedure-specific** — Benson pyloromyotomy "
         "spreader with a pyloric blade, Noblett suction rectal biopsy "
         "instrument, separately labelled pots for levelling biopsies with "
         "frozen section, small graded anal and Hegar dilators, a silo bag, "
         "paediatric stoma appliances and contrast with an image "
         "intensifier; **contamination control** — a separate 'dirty' bowel "
         "set, isolation packs, dedicated suction, separate receivers, glove "
         "change and culture swabs; and **physiological support** — "
         "nasogastric decompression, active warming with warmed fluids and "
         "theatre at 24–26 °C, core temperature monitoring, volumetric "
         "pumps, cross-matched blood in paediatric aliquots, counted swabs "
         "with a weighing scale, glucose monitoring and central access for "
         "parenteral nutrition."),
        ("Why are neonatal bowel anastomoses hand-sewn rather than stapled?",
         "Neonatal bowel may be only 5–10 mm in diameter with a wall less "
         "than a millimetre thick. Standard stapling devices are too bulky "
         "to introduce, would crush a disproportionate amount of tissue and "
         "would significantly narrow the lumen, risking stricture. A "
         "hand-sewn single-layer interrupted extramucosal anastomosis with "
         "5-0 to 7-0 absorbable suture, performed under magnifying loupes, "
         "gives accurate serosa-to-serosa apposition without compromising "
         "the lumen.")]))

# `P()` substitutes a fresh list when given an empty one, so re-bind the
# accumulated chapters onto the part now that they have all been appended.
PEDS["trays"] = _TRAYS
