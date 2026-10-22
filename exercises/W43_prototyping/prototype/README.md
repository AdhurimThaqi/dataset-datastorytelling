# Prototype: "Real or AI?" (Crazy 6's box 1 · Guess)

**Open it (newest):** [`v2.html`](v2.html), online at `https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W43_prototyping/prototype/v2.html`

| Version | What changed | Why |
|---|---|---|
| v1 | First build: 4 pictures → guess → 57 of 100 as dots | Crazy 6's box 1 |
| v2 | Visible 5-second countdown; no answer in time = "not sure" | Lecturer test: "I like the time pressure, but make it more obvious" |

- **One aspect:** 57 of 100 Americans say they already see people around them struggling to tell what's real from what's fake.
- **One interaction:** guess Real or AI on four pictures, then see the 57 as 100 dots.
- **One test:** see `test.md`.

| File | What |
|---|---|
| `v2.html` | Newest version. Shortcuts: `?step=end` (straight to the reveal), `?theme=dark`, `?limit=8` (seconds per picture) |
| `v1.html` | First version, kept for comparison |
| `prompts.md` | All prompts and the brief (needed for W44) |
| `test.md` | Test script and a sheet to write down what testers say |

## Number check (against `exercises/W39_data/survey_all_waves_all_subgroups.csv`, total, wave 2026-09-10)

| Shown | CSV | OK |
|---|---|---|
| 57 already see it | have_seen 57.13 | ✅ |
| 24 starting to see it | starting 24.39 | ✅ |
| 9 expect it soon | expect_soon 8.67 | ✅ |
| 2 don't expect it | dont_expect 1.98 | ✅ |
| 7 not sure + 1 no answer | not_sure 6.94 · no_answer 0.89 | ✅ |
| Sum of dots | 100 | ✅ |

The pictures load from Wikimedia Commons, so the prototype needs internet. Credits are shown after each answer.
