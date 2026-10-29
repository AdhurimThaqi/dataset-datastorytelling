# Prototype: "Real or AI?" (Crazy 6's box 1 · Guess)

**Open it (newest):** [`v4.html`](v4.html), online at `https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W43_prototyping/prototype/v4.html` (after the next push)

| Version | What changed | Why |
|---|---|---|
| v1 | First build: 4 pictures → guess → 57 of 100 as dots | Crazy 6's box 1 |
| v2 | Visible 5-second countdown; no answer in time = "not sure" | Lecturer test: "I like the time pressure, but make it more obvious" |
| v3 | Clock as its own funny element (lines that change every second, burning fuse, 3-2-1 screen); end split into "Your result" → CTA "Show me →" → "The number" | My review of v2: end screen too cramped, time still not obvious enough |
| v4 | Pool of 16 pictures (8 real, 8 AI); each round draws 2 real + 2 AI at random, no repeats until the pool is used up | 3 testers: "predictable after several plays, always the same four pictures" |

- **One aspect:** 57 of 100 Americans say they already see people around them struggling to tell what's real from what's fake.
- **One interaction:** guess Real or AI on four pictures, then see the 57 as 100 dots.
- **One test:** see `test.md`.

| File | What |
|---|---|
| `v4.html` | Newest version. Shortcuts: `?step=result`, `?step=number`, `?theme=dark`, `?limit=8` (seconds per picture), `?reset` (forget the pictures already seen) |
| `v1.html`, `v2.html`, `v3.html` | Earlier versions, kept for comparison |
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
