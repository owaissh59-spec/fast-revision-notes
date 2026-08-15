---
inclusion: always
---

# Fast Revision Notes — Workflow Steering

This repository is a **template + instruction set** for converting mock-test text files into printable revision notes. When the user provides a mock-test text file (or attaches one), you MUST follow the workflow defined here.

## Trigger

Any user request that resembles:

- "Convert this into revision notes"
- "Turn this into fast revision notes"
- "Make revision notes from this"
- "Print-friendly notes from this Q&A file"

... and the input contains numbered Q/Answer/Explanation blocks.

## Required Reading Before You Start

Read these files in this order:

1. [`AGENTS.md`](../../AGENTS.md) — primary instructions (rules, workflow, output format).
2. [`templates/base-template.html`](../../templates/base-template.html) — the HTML skeleton to start from.

Optionally consult if a question arises:
- [`docs/INSTRUCTIONS.md`](../../docs/INSTRUCTIONS.md) — worked walkthrough.
- [`docs/STYLE_GUIDE.md`](../../docs/STYLE_GUIDE.md) — design rationale.
- [`docs/CSS_REFERENCE.md`](../../docs/CSS_REFERENCE.md) — class-by-class reference.
- [`examples/example-output.html`](../../examples/example-output.html) — a full working example.

## Non-Negotiable Output Rules

Repeated here for emphasis (full details in `AGENTS.md`):

1. **Single self-contained HTML file** named `revision-notes.html` (or user-specified).
2. **Monochrome-safe** — all meaning must survive B&W printing.
3. **Body font 8.5pt** by default, line-height 1.22, A4 with 10mm margins.
4. **NO forced page breaks** between H2 sections.
5. **Organize by concept**, not by question number.
6. **Preserve every distinct concept** — nothing dropped.
7. **Include a Last-Minute Fact Dump** with 25–35 one-line facts in a 3-column layout.

## What NOT To Do

- Do not produce a Q&A dump (the input format).
- Do not add color-dependent styling.
- Do not add JavaScript, web fonts, or external assets.
- Do not force page breaks that waste paper.
- Do not truncate content to save space — compress structure, not concepts.

## Delivery

After writing `revision-notes.html`:

1. Summarize the sections you created.
2. Mention any mnemonics you invented.
3. Tell the user: open the file → Ctrl/Cmd + P → print on A4.
4. If in a git-tracked workspace, offer to push it to a branch.
