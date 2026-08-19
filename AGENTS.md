# AGENTS.md — Instructions for AI Agents

**This file is the primary instruction sheet.** When a user asks you to convert a mock-test / Q&A text file into revision notes, read this file first and follow it.

---

## 1. Task Summary

**Input:** A plain-text file (or pasted content) containing numbered mock-test questions in the format:

```
1. Q: <question text>
   Answer: <correct answer>
   Explanation: <why the answer is correct and distractors are wrong>

2. Q: ...
```

**Output:** A single, self-contained HTML file named `revision-notes.html` (or a user-specified name) that is:

- Optimized for **printing on A4 paper**
- **Monochrome-safe** (works perfectly on black-and-white printers)
- **Compact** (minimum page count while remaining readable)
- **Organized by topic**, not by question number
- Designed for **fast revision** (skimming, not re-reading MCQs)

The user's goal is to print these notes and refresh concepts quickly. **Do NOT produce a Q&A-style dump** — produce revision material.

---

## 2. Non-Negotiable Rules

1. **Preserve every distinct concept** from the input. No factual content may be dropped.
2. **No color-dependent information.** All meaning must survive black-and-white printing. Use borders, underlines, bold, grayscale shading only.
3. **Single self-contained HTML file.** All CSS inline in a `<style>` tag. No external fonts, no external CSS, no JavaScript, no images.
4. **A4 print target.** Use `@page { size: A4; margin: 12mm; }`.
5. **Base font size 8.5pt** for the body. Do not go above this by default. The user prefers dense notes.
6. **Never insert forced page breaks** (`page-break-before: always`) between top-level sections. Let content flow naturally to save paper.
7. **Do not add tests, quiz mode, or interactive features.** This is a print artifact.
8. **File name:** `revision-notes.html` unless the user specifies otherwise.
9. **Never print source question numbers.** Do NOT write "Q8:", "Q30", "(Q113)", "Question 5", or any reference to the original question number anywhere in the output — not in points, not next to worked examples, not in the fact dump. The notes must read as clean revision material, not as annotated answers. The order of questions in the source is arbitrary and the numbers carry no revision value.
10. **Deduplicate concepts — one concept, one place.** When several questions test the same underlying concept, consolidate them into a **single** table row, bullet, fact card, or box. Never repeat the same fact because it appeared in multiple questions. Merge overlapping questions; keep only the most complete version, absorbing any extra detail from the duplicates into that single entry.

---

## 3. Workflow (Follow in Order)

### Step 1 — Read ALL Questions First, Then Categorize
**Before writing anything, read every question together with its Answer and Explanation, end to end.** Only after you have the full picture should you design the notes. During this pass you must:

- Identify the **distinct concepts** actually being tested (there are always far fewer concepts than questions).
- **Detect duplicates and overlaps:** note every set of questions that hit the same concept so you can merge them into one entry later (see Non-Negotiable Rule 10).
- Decide the best structure for the material as a whole — do not convert questions one-by-one in source order.

Then group the distinct concepts into thematic sections. Common categories include:

- Public Health / Health Administration / Programmes
- Epidemiology / Biostatistics / Screening
- Sterilization / Disinfection / Vector Control
- Pharmacognosy / Natural Products
- Anatomy / Physiology
- Pharmaceutics / Dosage Forms / Compounding
- Pharmacology
- Chemistry / Biochemistry

You are NOT limited to these — pick whatever categories match the actual content. **Group questions on the same concept together**, even if they appear far apart in the input.

### Step 2 — Convert to Concepts (Not Q&A)
For each group of related questions, extract the underlying **facts and relationships**. Do not write "Q: … A: …". **Collapse duplicates as you go:** if three questions all test "autoclave = 121°C/15 min/15 psi", that becomes exactly one entry, not three. Instead, produce:

- **Tables** for anything comparative (dose ranges, classifications, hierarchies, populations, timings, ratios, drug classes, etc.).
- **Bullet lists** for enumerable facts.
- **Fact cards** (`.fact` boxes) for atomic Q→A recall pairs.
- **Formula boxes** (`.formula`) for equations, on a single line where possible.
- **Key highlights** (`.key`) for critical rules, worked examples, and definitions.
- **Mnemonics** (`.mnem`) where a memorable hook exists or you can construct one.

Include **all worked examples** from the source, but **without any question-number label** (no "Q8:", no "(Q30)"). Present each worked example purely as the concept + calculation. If two or more questions are variations of the same worked example, keep **one** representative example only.

### Step 3 — Apply the Template
Use `templates/base-template.html` as the starting HTML skeleton. It already has the correct CSS. Do not modify the CSS unless the user explicitly asks for a size/spacing change.

### Step 4 — Add a Last-Minute Fact Dump
At the end, add a `## Last-Minute Fact Dump` section with a **3-column grid** of `.fact` cards, each containing one atomic fact (question + one-line answer). This is for the night before an exam. Aim for 25–35 of the highest-yield facts.

### Step 5 — Verify Coverage
Before finishing, mentally walk through every question in the input and confirm its concept appears somewhere in your HTML output. Do not skip questions.

---

## 4. Content Style Rules

### Compression tactics (always apply)
- Merge short paragraphs into single lines with `•`, `;`, or `|` separators.
- Put multiple related formulas on ONE line separated by `|`.
- Inline short definitions (e.g., "Reliability = repeatability/precision") instead of two-line explanations.
- Use two-column and three-column layouts (`.two-col`, `.three-col`) for lists of small independent facts.
- Prefer tables over sequences of similar bullet points.
- Never leave more than one empty line between elements in source code.

### Writing style
- **Terse and scannable.** No introductory phrases, no "It is important to note that…".
- Use **bold** for the key term in each bullet.
- Use `<em>` for botanical/Latin names.
- Numbers, ratios, and units always in bold when they're the key fact (e.g., **4:2:1**, **160°C**, **1980**).

### Content DO
- Include worked examples with numerical answers, showing the calculation.
- Distinguish confusable pairs (index vs primary case, reservoir vs source, sensitivity vs specificity, direct vs indirect standardization, etc.) using a two-column table or side-by-side layout.
- Include mnemonics like "SnNout / SpPin", "5-30-120 rule", etc. Invent new ones where useful.
- Merge every set of questions that share a concept into a single entry — the reader should never see the same fact twice.

### Content DON'T
- Don't include the full MCQ text ("(a) 5,000 (b) 30,000 …"). Only the concept survives.
- Don't include marketing language, motivational text, or emojis in body content (small icons like ★ inside `.mnem::before` are fine).
- Don't add a section titled "Introduction" or "Conclusion".
- Don't include page numbers, dates, or "prepared by" notes.
- Don't print source question numbers ("Q8", "Q30", "Question 12") anywhere — in points, worked examples, or the fact dump.
- Don't repeat a concept because it appeared in more than one question. One concept = one entry.

---

## 5. Layout & Print Rules

- **Body font:** 8.5pt Georgia/Times serif; line-height 1.22.
- **Headings:** Helvetica/Arial sans-serif.
  - H1: 15pt, uppercase, centered.
  - H2: 10.5pt, uppercase, white-on-black bar.
  - H3: 9pt, black-on-light-gray with left black border.
  - H4: 8.5pt, underlined.
- **Table font:** 8pt; cell padding 2×4px; every-other-row light gray (`#f2f2f2`).
- **@page margin:** 12mm all sides.
- **Never use forced page breaks** between H2 sections. Let flow decide.
- Apply `page-break-inside: avoid` to boxes, tables, fact cards, formulas, and highlights so they don't split across pages.

If the user asks for tighter or looser output, adjust the body font first (e.g., 8pt for tighter, 9.5pt for looser) and scale headings proportionally.

---

## 6. Output & Delivery

1. Write the HTML to `revision-notes.html` in the current working directory (or the workspace root of the user's repository).
2. In your response to the user, briefly summarize:
   - How many sections you created and their names.
   - Any interesting reorganizations or mnemonics you added.
   - Which questions (if any) you could not confidently categorize (usually none).
3. Tell the user how to print: open the file → Ctrl/Cmd+P → Print.
4. If the user is working inside a repository, offer to push it to a branch or open a PR.

---

## 7. When the User Requests Changes

Common follow-up requests and how to handle them:

| User asks | You do |
|---|---|
| "Make it smaller / fewer pages" | Reduce font by ~20% (8.5pt → 7pt), tighten paddings, move more content into 3-column layouts. Never sacrifice concepts. |
| "Make it larger / easier to read" | Increase font by ~20%, allow line-height 1.35, single-column layouts. |
| "Split into per-topic files" | One HTML file per H2 section, same styling; add an `index.html` linking to each. |
| "Add practice questions" | Only if explicitly requested. Add a separate `<section>` at the end. |
| "Change color scheme" | Only if user says the printer is color. Otherwise keep monochrome. |

---

## 8. Reference Files in This Repo

- `templates/base-template.html` — the HTML skeleton with all CSS. **Start here for every new conversion.**
- `docs/INSTRUCTIONS.md` — a longer, worked walkthrough of a conversion.
- `docs/STYLE_GUIDE.md` — the rationale for every design decision (read this if the user challenges a choice).
- `docs/CSS_REFERENCE.md` — every CSS class and when to use it.
- `examples/example-output.html` — a complete example generated from 133 questions.

**When starting a new conversion, at minimum read: this file (`AGENTS.md`) and `templates/base-template.html`.**
