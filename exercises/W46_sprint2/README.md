# Sprint 2 · v6: mentoring feedback (05.11.2026)

**Open it:** [`v6.html`](v6.html) (same six steps as v5 in `../W45_sprint1/`)

## What changed from v5
| Feedback (Alain, 05.11) | v6 |
|---|---|
| Remove the progress bar | The 6-step story bar at the top is gone. The small counter during the guess stays, so you know how many items are left. |
| Hints on how to tell it's AI | **During** the guess: a "💡 What should I look for?" button (key **H**) shows a tip, never the answer. **After** each answer: a "How to tell" line. **Result screen:** a "How to spot AI" card with 4 rules of thumb and the note that new models fix these clues. |
| Real vs AI not only with pictures | After the 4 pictures come **2 short travel texts** (1 by a person, 1 by AI), with the buttons **PERSON / AI** and 12 s per text. Pool of 4 + 4, with the same no-repeat draw as the pictures. |

The human texts come word for word from Wikivoyage revisions saved **before ChatGPT existed** (2021 and early 2022), so they can't be AI-written. The AI texts were written by Claude. Sources and prompt: `../W43_prototyping/prototype/prompts.md`, prompt 7.

## Files
| File | What |
|---|---|
| `template.html` | The page, **without numbers**: edit this one |
| `build.py` | Writes `v6.html` with the numbers from the CSV (same as sprint 1) |
| `v6.html` | **Generated**, don't edit by hand |
| `check.py` | Every number in `v6.html` against the CSV: `71 checks … 0 mismatches` |

**Review shortcuts:** the same as v5, plus `?step=text` (jumps to the first text).

## Status (05.11.2026)
- ✅ `check.py`: 0 mismatches
- ✅ jsdom click-through, two full rounds (one with a text timing out), no script error
- ✅ headless Edge screenshots of the intro, the text guess and the result
- ⏳ on a real phone
- ⏳ one tester (20–35)
- ⏳ next time: sketch 1–2 more questions (captcha grid, true/false cards) and look through the PDF
