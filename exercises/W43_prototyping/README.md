# W43 · Milestone 2: at least three different designs (due Thu 22 Oct 2026)

From the course (W42 script + project brief):
- "three directions, sketched by hand" = the milestone
- photos of **all** sketches (including rejected ones) in the research documentation
- the weekly process entry
- optional: one AI draft for one direction, **after** sketching, with the prompt and the three checks

## What's here
| File | What |
|---|---|
| `three-sentences.md` | The data shows … / People told us … / How might we …? |
| `directions.md` | A, B, C: context, format, data cut, mapping, who leads, non-clicker, criteria, risks, rejects |
| `wireframes/A.svg` `B.svg` `C.svg` | 6-frame **digital wireframes**: reference for the hand sketch, *not* the sketch |
| `make_wireframes.py` | regenerates the wireframes (`python make_wireframes.py`) |
| `data_cut.py` | every number used, straight from the CSV (`python data_cut.py` prints them) |
| `sketch-guide.md` | what to draw on paper, frame by frame (~30 min) |
| `photos/` | photos of **all** hand sketches go here |
| `ai-draft/` | optional W42 step for A: `index.html` (built by `build.py`), `prompt.md`, `checks.md` |
| `comparison.md` | A/B/C vs. success criteria + W44 feasibility, recommendation **for the group to decide** |
| `build_page.py` | builds the overview page `../../w43.html` |

Data rules:
- latest NORC wave only (10–14 Sep 2026, n = 1,083)
- pilot wave excluded
- "none / neither / not sure / no answer" stay visible
- gaps under the combined margin of error are not called gaps

Python 3, standard library only (no pandas needed).

⚠️ The milestone needs the **hand sketches**. Everything digital here is a reference or an optional extra.
