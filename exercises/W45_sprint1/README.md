# Sprint 1 · v5: all six steps in one file

**Open it:** [`v5.html`](v5.html), online at https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W45_sprint1/v5.html
Sprint plan: `../W44_plan/documentation/02_sprint-plan.pdf` (goal: one file runs all six steps on a phone, and every number comes from `build.py`)

| Step | Screen | What happens | Numbers (latest wave, 10–14 Sep 2026) |
|---|---|---|---|
| 1 | Hook | Real or AI? 4 pictures from a pool of 16, with a 5-second clock (the v4 hook, unchanged) | — |
| 2 | Reveal | 57 of 100 as 100 dots, then the legend and "only 2 in 100 don't expect it" | community question, "real vs fake" item |
| 3 | Your answer | The survey's own question and answers, word for word | sentiment question |
| 4 | You vs. America | Your outlined dot among 1,000; tabs for all adults and the 4 age groups; the text only says "more" or "less" if the gap beats the margin of error | sentiment by group |
| 5 | The turn | A second survey question; "2 in 3 say it's coming anyway"; "can shape" by age (27 vs 8 in 100, a real gap) | agency question by age |
| 6 | Close | The key message, your path (eyes / feel / think), the source, all numbers as a table, "Play again" | — |

## Files
| File | What |
|---|---|
| `template.html` | The page, **without numbers**: edit this one |
| `build.py` | Reads the CSV (through `../W43_prototyping/data_cut.py`) and writes `v5.html` with the numbers as JSON |
| `v5.html` | **Generated**, don't edit by hand. Run `python build.py` after every change to the template. |
| `check.py` | Compares every number in `v5.html` with the CSV (read directly) and `data.json`, and checks that no survey number is typed into the template |

```
python build.py   # → v5.html
python check.py   # → "71 checks … 0 mismatches"
```

**Review shortcuts:**
- `?step=1` … `?step=6` (or `result`, `number`, `ask`, `you`, `turn`, `close`)
- `&a=somewhat_concerned`: the answer to question 1
- `&b=can_shape`: the answer to question 2
- `&g=age_18_34`: the group tab
- `?theme=dark` · `?limit=8` · `?reset`

## Sprint 1 status (29.10.2026)
| # | Task | Done when … | Status |
|---|---|---|---|
| 1 | Merge the hook with steps 2–6 | intro → close in one go, without an error; `?step=1…6` open each step | ✅ in a simulated browser (jsdom), clicked through twice without a script error (once with two time-outs); screenshots of every step in headless Edge. **Still to do: on a real phone.** |
| 2 | No hand-typed numbers | check script: 0 mismatches | ✅ 71 checks, 0 mismatches; also tested with a planted wrong number and a typed number, and both were caught |
| 3 | Step 4 | "somewhat concerned" puts the dot in that block; the 18–34 tab says "about the same" (61 vs 69) | ✅ |
| 4 | Step 5 | 67.5 %, and 27 vs 8 in 100 | ✅ |
| 5 | One tester | one person (20–35) on their own phone, take-away written down | ⏳ open: needs a person |
