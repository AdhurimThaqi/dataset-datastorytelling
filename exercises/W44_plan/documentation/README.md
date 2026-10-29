# W44 documentation (hand-in for W45 · 05.11)

The W44 slides (Gordan, "Implementation plan") ask for **two documents in the research documentation**.
Both are here as PDF, plus an appendix with the research behind them.

| File | What | Slide |
|---|---|---|
| **`01_implementation-plan.pdf`** | One document, four chapters: **1** concept (120 words) · **2** tone (3 adjectives, 3 references, hand sketch of the key moment) · **3** architecture (diagram + what is real, what is facade) · **4** backward plan from 17.12, core vs. nice to have, reflection | 4–6, 8 |
| **`02_sprint-plan.pdf`** | Sprint 1 (05.11 → 12.11): one goal, 5 tasks with who / what / done when, sprint review to fill in | 7 |
| `03_research-appendix.pdf` | Concept refinement from the test, the full user test (v1 → v4), **all prompts** for the prototype | (W43 rule: "the HTML file and all prompts") |

**The prototype itself:** [`../../W43_prototyping/prototype/v4.html`](../../W43_prototyping/prototype/v4.html) ·
online at https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W43_prototyping/prototype/v4.html

## Sources of the PDFs
- `01_implementation-plan.md`, `02_sprint-plan.md`: the text (edit these, not the PDFs)
- `architecture.svg`: the architecture diagram
- `img/key-moment-sketch.jpg`: hand sketch, direction A frames 1–2 (copy of `../../W43_prototyping/photos/A_hand_frames-1-2.jpg`)
- The appendix is built from `../concept-refinement.md`, `../../W43_prototyping/prototype/test.md` and `prompts.md`.

**Rebuild after a change:** `python make_pdf.py` (needs `pip install markdown` and Edge or Chrome).
