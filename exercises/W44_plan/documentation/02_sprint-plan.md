# Sprint plan · Sprint 1

**Worried, but it's coming anyway** · Adhurim Thaqi (solo, so every task is mine) · W45 05.11 → W46 12.11.2026

## Sprint goal
**One file, `v5.html`, runs all six steps on a phone, from "Real or AI?" to the key message, and every number in it comes from `build.py`.**

## Tasks

| # | Who | What | Done when … |
|---|---|---|---|
| 1 | Adhurim | **Merge** the v4 hook (clock, random pool, 57 reveal) with steps 3–6 of the AI draft into one template | On my phone (Chrome, Android) I can go from the intro to the close in one go without an error, and `?step=1` … `?step=6` open each step. |
| 2 | Adhurim | **No hand-typed numbers:** `build.py` also injects the hook numbers (57 / 24 / 9 / 2 / 7 / 1), which are still typed into v4 | The check script compares every number in `v5.html` with the CSV and reports **0 mismatches**. |
| 3 | Adhurim | **Step 4, you vs. America:** your outlined dot among the 1,000, and age tabs with the margin-of-error rule | Picking "somewhat concerned" puts my dot in that block, and the 18–34 tab says **"about the same"** as all US adults (61 vs 69 concerned, inside the margin). |
| 4 | Adhurim | **Step 5, the turn:** "coming anyway" and "can shape" by age | The page shows **67.5 %** "coming whether we want it or not", and **27 vs 8 in 100** "can shape" (18–34 vs 65+). That matches CSV lines 7866, 7885 and 7896. |
| 5 | Adhurim | **One tester** goes through v5 | One person from the target group (20–35) has used v5 on their own phone, and their answer to "What did you take away?" is written down in `test.md`. |

## Not in this sprint

- autoplay
- local copies of the pictures
- all four age tabs
- other groups

These are nice to have and come in sprint 2, if there is time. See the backward plan in the implementation plan.

## Status 29.10 (started early)
- **Tasks 1–4 done:** `exercises/W45_sprint1/v5.html`
- **Checks:**
    - `check.py`: 71 checks, 0 mismatches
    - a click-through from the intro to the close in a simulated browser, without a script error
- **Still open:**
    - task 1 on a real phone
    - task 5, the tester

## Sprint review (fill in on 12.11)

- Sprint goal reached? ☐ yes ☐ partly ☐ no
- What the tester took away: ……………………………………
- Moved to sprint 2: ……………………………………
