# fast-revision-notes

Reusable instructions and templates that let an AI assistant (e.g., **[Kiro](https://kiro.dev)**) convert mock-test / Q&A text files into **print-ready, monochrome, page-efficient HTML revision notes** — without you having to re-explain the requirements each time.

---

## How It Works

1. **Point your AI assistant at this repo** (clone it into your workspace, or reference it as steering).
2. **Paste or attach your mock-test text file** and say: *"Convert this into fast revision notes."*
3. The assistant reads [`AGENTS.md`](./AGENTS.md) → follows the template in [`templates/base-template.html`](./templates/base-template.html) → produces `revision-notes.html`.
4. Open it in a browser → **Ctrl/Cmd + P** → print on any B&W printer.

You never re-explain layout, font sizes, monochrome rules, or organization. It's all in this repo.

---

## What The Output Looks Like

- **A4 print target**, 10 mm margins.
- **Base font 8.5 pt** — dense but readable.
- **Monochrome** — every design element (borders, gray shading, bold, underlines) works on B&W printers.
- **Organized by topic**, not by question number.
- **Tables, formulas, fact cards, mnemonics** — chosen automatically based on the content type.
- **Last-minute fact dump** at the end — one-line facts in a 3-column grid for pre-exam skim.

A full example from a 133-question input is in [`examples/example-output.html`](./examples/example-output.html).

---

## Input Format

Your text file should look like this (numbering + `Q:` / `Answer:` / `Explanation:` labels):

```
1. Q: <question text with options or scenario>
   Answer: <the correct choice>
   Explanation: <why correct + why distractors are wrong>

2. Q: ...
```

That's it. The AI figures out the topics and grouping on its own from the `Answer` and `Explanation` fields.

---

## Repo Structure

```
fast-revision-notes/
├── README.md                       # This file
├── AGENTS.md                       # PRIMARY: instructions the AI reads
├── docs/
│   ├── INSTRUCTIONS.md             # Step-by-step conversion walkthrough
│   ├── STYLE_GUIDE.md              # Rationale for every design choice
│   └── CSS_REFERENCE.md            # Class-by-class reference
├── templates/
│   └── base-template.html          # HTML skeleton with all CSS embedded
├── examples/
│   └── example-output.html         # A complete generated example
└── .kiro/
    └── steering/
        └── revision-notes-workflow.md  # Auto-loaded by Kiro when this repo is the workspace
```

---

## Using With Kiro (Recommended)

### Option A — Clone this repo as the workspace

1. In Kiro, start a new session with this repo (`owaissh59-spec/fast-revision-notes`) as the workspace.
2. Attach your mock-test text file.
3. Say: *"Convert this into revision notes."*
4. Kiro reads `.kiro/steering/revision-notes-workflow.md` automatically, follows `AGENTS.md`, and writes `revision-notes.html` in the workspace.

### Option B — Use alongside another repo

1. Clone this repo into a subfolder of your working repo (e.g., `git clone https://github.com/owaissh59-spec/fast-revision-notes.git .revision-tools`).
2. Say: *"Follow the instructions in `.revision-tools/AGENTS.md` and convert this text file into revision notes."*

### Option C — Copy just the essentials

If you only want the template, copy:
- [`AGENTS.md`](./AGENTS.md) → tells the AI what to do.
- [`templates/base-template.html`](./templates/base-template.html) → the starting HTML skeleton.

Point your AI at those two files and it will produce the same output.

---

## Customization

Common tweaks (just tell the AI):

- *"Make it smaller / fit in fewer pages"* → drops font to ~7 pt, moves to 3-column layouts.
- *"Make it larger"* → 9.5 pt, single-column, wider spacing.
- *"Split by topic into separate files"* → one HTML per topic + an `index.html`.
- *"Add color for my color printer"* → switches to a color-safe palette while remaining print-friendly.

All of these are handled by section 7 of [`AGENTS.md`](./AGENTS.md).

---

## Design Principles

1. **Concepts > MCQs.** The final output is not a question bank — it's a study aid built *from* one.
2. **Every concept preserved.** Nothing informational is dropped, even when text is compressed.
3. **Monochrome-first.** All meaning survives a B&W laser printer.
4. **Page-efficient.** Optimized for the least paper while remaining readable.
5. **Zero external dependencies.** One self-contained HTML file that opens anywhere.

Details in [`docs/STYLE_GUIDE.md`](./docs/STYLE_GUIDE.md).

---

## License

MIT — use, adapt, share freely.
