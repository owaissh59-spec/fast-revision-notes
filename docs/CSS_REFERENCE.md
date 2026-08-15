# CSS_REFERENCE.md — Class-by-Class Reference

Every CSS class defined in `templates/base-template.html` and when to use it.

---

## Structural / Text

| Element / Class | Purpose | Notes |
|---|---|---|
| `body` | Base font | 8.5pt Georgia serif, line-height 1.22, black on white. |
| `h1` | Document title | 15pt Helvetica, uppercase, centered. Use once. |
| `.subtitle` | Line under H1 | Italic, 8pt, centered, black underline. Use once. |
| `h2` | Top-level section | Black bar, white text, uppercase. New topic. **No forced page-break.** |
| `h3` | Sub-section | Gray bg with black left border. Groups within a topic. |
| `h4` | Sub-sub-section | Underlined plain text. Rare. |
| `p` | Paragraph | Minimal margin. |
| `ul`, `ol` | Lists | Left padding 16px, tight item spacing. |
| `strong` | Bold | Key term in bullets, key numbers/units. |
| `em`, `i` | Italic | Latin/botanical names, subtle emphasis. |

---

## Semantic Boxes

### `.fact`
Atomic recall card. Use for **one concept, one answer**.
```html
<div class="fact">
  <span class="q">Question stem or concept name</span>
  <span class="a">The answer</span>
  <span class="why">Optional: distractors or nuance in one italic line.</span>
</div>
```
- `.q` — bold black text (the stem).
- `.a` — inline black chip, white text (the answer).
- `.why` — small italic (optional).

### `.key`
Highlighted rule, definition, or worked example. Use when the fact needs visual emphasis but isn't a Q→A pair.
```html
<div class="key">
  <strong>Worked example:</strong> …
</div>
```

### `.formula`
Equations. Centered monospace on gray background.
```html
<div class="formula">
  Sens = TP/(TP+FN) | Spec = TN/(TN+FP)
</div>
```
- Put multiple related formulas on ONE line with `|`.

### `.mnem`
Memory hooks. Dashed border, auto-prefixed with `★ TIP: `.
```html
<div class="mnem">
  <strong>SnNout / SpPin</strong>: high SEN + Negative test = rule OUT; high SPEC + Positive = rule IN.
</div>
```

---

## Tables

Always use standard `<table><thead><tbody>` markup. The CSS handles:
- Black borders on all cells.
- White-on-black `<th>`.
- Zebra striping on even body rows.
- 8pt font, 2×4px cell padding.
- Left-aligned, top-aligned content.

Use `colspan` freely for grouped cells.

---

## Layout Containers

### `.two-col`
2-column layout. Best for pairs of small tables, or a table + its explanation.
```html
<div class="two-col">
  <table>…</table>
  <div class="key">…</div>
</div>
```

### `.three-col`
3-column layout. Reserved for the last-minute fact dump (grid of `.fact` cards).
```html
<div class="three-col">
  <div class="fact">…</div>
  <div class="fact">…</div>
  ...
</div>
```

### `.toc`
Table of contents at the top of the document. 3-column ordered list inside a bordered box.

### `.footer-note`
Small centered footer text. Optional. Use once at the very end.

---

## Utility

| Class | Purpose |
|---|---|
| `.inline-list` | Turns a `<ul>` into a horizontal bullet-separated list. Use sparingly. |
| `.no-print` | Hides an element on print (currently unused, available for future). |

---

## What NOT to Add

Do not introduce new classes without a strong reason. If a new fact type recurs many times, propose adding it — otherwise reuse the existing library. A new class per document defeats the "reusable template" purpose.

Never add:
- Colored backgrounds beyond the gray palette.
- Web fonts (`@import`, `<link>` to Google Fonts, etc.).
- JavaScript.
- External images.
- CSS media queries beyond `@page` and `@media print`.
