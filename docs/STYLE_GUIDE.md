# STYLE_GUIDE.md — Design Rationale

Every design choice in the template exists for a reason. If a user challenges a decision, this file explains why. If you (the AI) are considering changing something, read the rationale first.

---

## Typography

### Body: 8.5pt Georgia serif
- **Why serif?** Higher information density and easier long-form reading on paper.
- **Why 8.5pt?** Users repeatedly ask for "fewer pages." 8.5pt is the smallest comfortable size for revision material. Below 8pt, the fatigue penalty outweighs the paper savings.
- **Line-height 1.22** — tight but not cramped. 1.20 causes descenders to touch ascenders on some renderers; 1.25 wastes half a line per paragraph across a long document.

### Headings: Helvetica/Arial sans-serif
- Creates a strong visual contrast with the serif body, making section boundaries scannable.
- Uppercase H2 in a black bar acts as a "chapter marker" without needing color.

### Font stack
- `"Georgia", "Times New Roman", serif` and `"Helvetica", "Arial", sans-serif` — universally installed. No web fonts (the file must open offline and print identically anywhere).

---

## Color System

### Palette
- **Black (#000)** — text, borders, H2 background.
- **White (#fff)** — page background, H2 text.
- **Light gray (#e2e2e2, #efefef, #f2f2f2, #f6f6f6)** — H3 background, `.key` background, table zebra rows.
- **No other colors.**

### Why monochrome?
- Most home printers are B&W lasers.
- Color often becomes noise on print (light yellow disappears; light red looks like a smudge).
- Constraint forces clean information hierarchy through shape and weight, not hue.

### How hierarchy is conveyed without color
- **H2** = high contrast (white on solid black bar).
- **H3** = medium contrast (light gray background, thick black left border).
- **H4** = low contrast (underlined black text).
- Body emphasis → **bold**.
- Latin/botanical → *italic*.
- Formulas → monospace + light gray box.

---

## Component Library

### `.fact` box
- **Purpose:** atomic recall pair (question stem + one-line answer + optional short explanation).
- **Structure:** bordered rectangle, question in bold, answer in a black-on-white inline chip, explanation in small italic.
- **When to use:** the concept is short enough to fit in ~3 lines and doesn't need comparison.

### `.key` box
- **Purpose:** rules, definitions, worked examples.
- **Structure:** light gray background, thick black left border, no top/bottom border.
- **When to use:** the fact is important enough to visually stop the reader, but doesn't need the "quiz" framing of `.fact`.

### `.formula` box
- **Purpose:** equations.
- **Structure:** monospace, centered, gray background.
- **When to use:** anything with `=`, `/`, `×`. Combine related formulas on one line with `|`.

### `.mnem` box
- **Purpose:** memory hooks and pattern mnemonics.
- **Structure:** dashed black border (visually distinct from solid boxes), auto-prefixed with `★ TIP: `.
- **When to use:** always include at least one per major section if a mnemonic is natural.

### `<table>` element
- **Purpose:** comparisons, hierarchies, dose-population norms.
- **Structure:** black borders, white-on-black header row, zebra-striped body rows.
- **When to use:** ≥3 rows with ≥2 attributes to compare. If it's only 2 items and 1 attribute, use a bullet list.

### `.two-col`, `.three-col`
- **Purpose:** paper-saving columnar layouts.
- **When to use:** collections of independent short items (fact cards, one-liners, small tables). Never for long prose.

---

## Layout Decisions

### 12mm page margins
- A4 is 210mm × 297mm. 12mm margins give 186mm × 273mm usable area.
- Most laser printers can handle 6mm margins reliably; 12mm is a safety buffer that also looks intentional and works on printers with slightly larger non-printable edges.

### No forced page breaks
- **Why:** `page-break-before: always` on every H2 wastes ~1/3 of every page.
- **What we do instead:** allow flow, use `page-break-after: avoid` on headings and `page-break-inside: avoid` on boxes/tables so nothing splits *awkwardly*, but content still packs efficiently.

### Multi-column layouts
- 2-column for fact groups and side-by-side tables + explanations.
- 3-column for the last-minute fact dump only (facts are short enough to be legible at that width).
- Never 4+ columns (line length becomes too short to read).

---

## Content Organization

### Group by concept, not by question number
- A user in revision mode wants to compare related facts. Question order in the source is arbitrary (often randomized).
- The AI reorganizes across the entire input.

### Never print source question numbers
- Question numbers ("Q8", "Q30", "Question 5") are source artifacts. In revision material they are pure visual clutter and carry no meaning once questions are regrouped by concept.
- Do NOT annotate any fact, point, worked example, or fact card with a source question number.
- Label worked examples by what they demonstrate (e.g., "Staffing calc:", "Vd example:"), never by "Q#".

### One concept, one entry (deduplicate)
- Mock tests deliberately repeat concepts across many questions; the revision notes must not.
- When multiple questions test the same concept, merge them into a single table row, bullet, or box, folding in any extra detail from the duplicates.
- The reader should never encounter the same fact twice. Duplication wastes paper and slows revision.

### Last-minute fact dump at the end
- A pre-exam skim needs a single dense page of one-liners.
- 3-column layout of fact cards is the densest legible format for this.

---

## Print Behavior

### `@page` rules
- `size: A4` — fixes the target medium.
- `margin: 12mm` — as above.

### `page-break-inside: avoid` on:
- Tables (so a table doesn't split mid-row).
- `.fact`, `.key`, `.mnem`, `.formula` boxes.
- TOC.

### `page-break-after: avoid` on:
- All headings (so a heading isn't orphaned at the bottom of a page).

### Nothing forces a new page
- The document is one continuous flow. Page count is determined by content volume, not artificial breaks.

---

## Accessibility & Portability

- **No JavaScript** — file opens and prints identically in any browser, offline.
- **No external assets** — everything is inline. The single HTML file is the entire deliverable.
- **Semantic HTML** — headings are `<h1>`–`<h4>`, tables are real `<table>` elements. Screen readers work.
- **High contrast** — black text on white is WCAG AAA.

---

## When to Deviate

Never deviate unless the user explicitly asks. Their common valid requests are documented in [`../AGENTS.md`](../AGENTS.md) §7. If a request seems to fight the design principles, ask a clarifying question rather than silently changing the output.
