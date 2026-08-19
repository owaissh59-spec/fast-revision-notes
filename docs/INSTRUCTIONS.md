# INSTRUCTIONS.md — Detailed Conversion Walkthrough

A step-by-step example of how to go from a mock-test text file to a printable `revision-notes.html`. Use this as a worked reference; the authoritative rules are in [`../AGENTS.md`](../AGENTS.md).

---

## Step 1 — Parse the Input

Read the file and identify each question block. A question block has three fields:

```
<number>. Q: <question text>
   Answer: <one-line answer>
   Explanation: <2–5 sentence rationale>
```

Extract from each block:
- The **concept** being tested (from the question stem + explanation).
- The **correct fact** (from the Answer field).
- **Distractor pitfalls** worth mentioning once (from the Explanation field).

Ignore multiple-choice option letters (A/B/C/D). They add no revision value.

---

## Step 2 — Cluster by Topic

Read all questions once before writing anything. Cluster related concepts:

| Signal in question | Likely topic |
|---|---|
| Sub-Centre, PHC, CHC, ANM, block, district | Public Health Administration |
| Epidemic, endemic, screening, sensitivity, RR, mortality rate | Epidemiology & Biostatistics |
| Autoclave, EtO, DDT, IRS, larvicide | Sterilization & Vector Control |
| Acacia, tragacanth, resin, balsam, volatile oil | Pharmacognosy |
| Sclera, action potential, IgM, EF, JVP | Anatomy & Physiology |
| Balance, sieve, extraction, distillation, emulsion | Pharmaceutics |
| Receptor, agonist, T½, Vd, first-pass | Pharmacology |

Group and order sections logically (fundamentals → applications). Within each section, order sub-topics from general → specific.

**Deduplicate while clustering.** Mock tests repeat the same concept across many questions. As you cluster, collapse every group of same-concept questions into a **single** planned entry. If five questions all revolve around "sensitivity = TP/(TP+FN)", that is one fact in the output, not five. Absorb any unique detail from the duplicates into that one entry, then discard the rest.

---

## Step 3 — Choose the Right Component for Each Fact

| Fact type | Component |
|---|---|
| Comparison across ≥3 items with 2+ attributes | `<table>` |
| A single atomic Q→A recall pair | `.fact` card |
| Equation or formula | `.formula` block |
| Critical rule / definition / worked example | `.key` block |
| Memory hook | `.mnem` block |
| Enumerable list of ≤6 short items | `<ul>` |
| Contrasting pairs (e.g., active vs passive immunity) | 2-col `<table>` |
| Long list of one-liners for pre-exam skim | `.three-col` of `.fact` |

**Rule of thumb:** if you'd draw a table on paper, use a table. If it's one line, use a `.fact`.

---

## Step 4 — Compress Ruthlessly

While preserving every concept, apply these compressions:

- **Merge related bullets** into single lines with semicolons.
  - Before: "• DDT is organochlorine.\n• BHC is organochlorine.\n• Malathion is organophosphate."
  - After: "DDT, BHC = organochlorine; Malathion = OP; Propoxur = carbamate."
- **Put formulas on one line** with `|` separators.
  - "Sens = TP/(TP+FN) | Spec = TN/(TN+FP) | PPV = TP/(TP+FP)"
- **Drop stub explanations** that don't add information beyond the answer itself.
- **Inline "why the distractors are wrong"** into a single `.why` line, not a paragraph.

---

## Step 5 — Preserve Worked Examples

Every numerical example in the source is worth keeping. Format:

```html
<div class="key"><strong>Staffing calc:</strong> Block pop 1,20,000 (plain) →
PHCs = 120000÷30000 = <strong>4</strong>;
SCs = 120000÷5000 = <strong>24</strong>.</div>
```

**Do NOT print the source question number** (no "Q8:", no "(Q30)"). Label the box by what it demonstrates (e.g., "Staffing calc:", "Vd example:") instead. If several questions are the same worked example, keep only one.

---

## Step 6 — Build the Last-Minute Fact Dump

At the end of the document, add a section with a `.three-col` container full of `.fact` cards. Each fact = a question stem + a one-line answer. Aim for:

- 25–35 highest-yield facts.
- Numbers, dates, ratios, formulas — anything the user might blank on.
- Cover ALL topics proportionally (not all from one section).

Example fact card:
```html
<div class="fact"><span class="q">Autoclave standard</span><span class="a">121°C / 15 min / 15 psi</span></div>
```

---

## Step 7 — Self-Review Checklist

Before delivering, check:

- [ ] Every input question's concept appears somewhere in the HTML.
- [ ] No source question numbers ("Q8", "Q30", "Question 5") appear anywhere in the output.
- [ ] Concepts tested by multiple questions appear exactly once (no duplicated facts).
- [ ] No forced `page-break-before: always` between H2 sections.
- [ ] Body font 8.5pt, line-height 1.22.
- [ ] All boxes have `page-break-inside: avoid`.
- [ ] Tables have zebra-striping.
- [ ] Every worked example is included (labelled by what it shows, not by a Q-number).
- [ ] Last-minute fact dump has 25+ items.
- [ ] File is a single self-contained HTML (no external assets).
- [ ] Print preview shows no half-empty pages caused by forced breaks.

---

## Step 8 — Deliver

Write the HTML to `revision-notes.html` in the workspace root. In your response:

- Name the sections you created.
- Mention any mnemonics you invented.
- Suggest the user open the file → Ctrl/Cmd+P → print A4.
- If the workspace is a git repo, offer to push to a branch.

---

## Common Pitfalls to Avoid

1. **Producing a Q&A dump.** The output is revision notes, not a question bank. Reorganize by concept.
2. **Using color to convey meaning.** Everything must survive B&W print.
3. **Forced page breaks.** They waste paper. Let content flow.
4. **Redundant boxes.** Don't put a single sentence in a `.key` block — just make it a paragraph.
5. **Missing worked examples.** These are high-value; always keep them.
6. **Over-abbreviating.** "AChE" is fine; "acetylcholinesterase" is fine; "ACE" is not (ambiguous with the enzyme).
7. **Printing question numbers.** Never carry "Q8", "Q30", or "Question 5" into the output — they are source artifacts with no revision value.
8. **Duplicated concepts.** If the same fact shows up in several questions, it must appear only once in the notes. Merge, don't repeat.
