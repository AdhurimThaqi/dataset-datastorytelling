# Implementation plan: "Worried, but it's coming anyway" (direction A)

**Format:** interactive prototype, one web page, phone first, about 2 minutes.
**Builds on:**
- the hook from `../W43_prototyping/prototype/v3.html`
- the full 6-step story from `../W43_prototyping/ai-draft/` (`template.html` + `build.py`)

## 1 · Overview
```
survey_all_waves_all_subgroups.csv ─┐
data.json (wave, n, margin)        ─┼─> data_cut.py ─> build.py ─> index.html ─> GitHub Pages
pictures.json (hook picture pool)  ─┘   (all numbers)  (injects JSON  (one file,     (phone browser)
                                                         into template) no build step
                                                                        for the viewer)
```
- **No hand-typed numbers.** Every percentage comes from the CSV through `data_cut.py`, as in the AI draft.
- **One HTML file** for the viewer: no framework, no server, no tracking. Plain HTML, CSS, JS and SVG.
- **New wave = run `python build.py`.** The gap rule is checked again at every build (rebriefing R13).

## 2 · Components
| # | Part | What it does | Where it comes from |
|---|---|---|---|
| 1 | **Data layer** | `data_cut.py` reads the CSV, drops the pilot, takes the latest NORC wave, computes the dots (largest remainder, adds up to 100 / 1,000), the words ("4 in 5") and the gap rule | exists (`../W43_prototyping/data_cut.py`) |
| 2 | **Picture pool** | `pictures.json`: file, real/AI, what it shows, credit, licence. Draws 2 real + 2 AI per round with no repeats (remembered in `localStorage`, and it still works if storage is blocked) | **done in v4** (29.10): 16 pictures, as a list inside `v4.html` for now (`pictures.json` once the 6 steps are merged) |
| 3 | **Story engine** | 6 steps as a state machine: `hook → reveal → question → you-vs-America → turn → close`. URL shortcuts (`?step=`, `?a=`, `?g=`) for reviewing | merge v3 + AI draft |
| 4 | **Hook** (step 1) | 3-2-1 screen, 4 pictures, 5-second clock with its lines, "time's up = not sure" | exists (v3) |
| 5 | **Reveal** (step 2) | 100 dots, pause on the 57, then the full split incl. "not sure / no answer" | exists (v3) |
| 6 | **Your answer** (step 3) | The survey's own question word for word: very / somewhat excited, somewhat / very concerned, "none of these" | exists (AI draft) |
| 7 | **You vs. America** (step 4) | 1,000 dots + your outlined dot. Age tabs re-colour the dots, and the text says more / less / about the same only if the gap beats the margin | exists (AI draft) |
| 8 | **The turn** (step 5) | "AI is coming anyway" 67.5 %, then "can shape" by age as bars (27 vs 8) | exists (AI draft) |
| 9 | **Close** (step 6) | Key message, source line "US adults, latest wave, n = 1,083", "Play again" | exists (AI draft); "Play again" new |
| 10 | **Autoplay** | No click for 8 s → the story moves on by itself (1 → 2 → 5 → 6) for people who don't click | exists in concept; to build |

## 3 · Rules the code has to keep
- **Accessibility:**
  - big tap targets (thumb)
  - keyboard works
  - `prefers-reduced-motion` turns off the dot animation and the fuse
  - alt text on every picture (after the answer, so it doesn't give it away)
- **Colour:** excited = blue, concerned = orange, none / no answer = grey. No red/green.
- **Privacy:** the visitor's answer stays in the browser. Nothing is sent or stored on a server.
- **Licences:** real photos are CC BY-SA, so the credit is shown after each answer and listed at the end.

## 4 · Feasibility
| Question | Answer |
|---|---|
| Can we build it by W51? | **Yes.** Most parts already run separately (v3 + AI draft). The work is merging them, the picture pool and autoplay. |
| Skills needed | HTML/CSS/JS, a little Python. Built with an LLM, one change per prompt, versions saved (`v4.html` …). |
| Cost | 0 CHF: GitHub Pages, Wikimedia Commons pictures, the public dataset |
| Testable in W48? | **Yes.** A link on a phone, one person, no room or hardware needed |
| New data waves | Rebuild with one command; no text has to be rewritten by hand |

## 5 · Risks
| Risk | How likely | What we do |
|---|---|---|
| Pictures load slowly or not at all (Wikimedia needs internet) | medium | Save the pool as small local files (≤ 200 KB each) next to the page; preload the next picture |
| Not enough good AI pictures with a clear licence | medium | Use public-domain AI images from Wikimedia Commons (as in v3); note the tool for each |
| Too easy or too hard (all right / all wrong) | medium | Mix easy and hard pictures in every draw; check the score spread in W48 |
| It feels like a quiz, not about you | open | That's the W48 test question; the "you" steps 3–4 follow right after the score |
| 1,000 dots too slow on old phones | low | One SVG with fixed positions, or canvas if needed; test on a cheap Android phone |
| A number on the page doesn't match the source | low | Numbers only come from `build.py`; a check script compares the page with the CSV (0 mismatches in the draft) |

## 6 · Timeline
| Week | What | Done when |
|---|---|---|
| W45 · 05.11 | v4: picture pool (≥ 12) + random draw; merge hook into the 6-step story | one file runs all 6 steps on a phone |
| W46–47 | Autoplay, "Play again", accessibility, local pictures, number check script | check script 0 mismatches; works offline |
| W48 · 26.11 | **User test** with 5 people from the target group (`test.md` script) | results in `W48_user-test/` |
| W49–50 | Changes from the test; visual polish (legibility input W48) | v-final frozen 10.12 |
| W51 · 17.12 | Presentation to Interactive Things + rationale (max. 2 pages) | |

## 7 · Open decision: web or exhibition (O1)
This plan assumes **web, phone first**: that matches the target group, the concept and the W48 test.
If it comes back as "exhibition", the same page runs on a tablet in kiosk mode, and autoplay becomes the default. That change is small. Direction B stays a described variant only (`../W43_prototyping/comparison.md`).
