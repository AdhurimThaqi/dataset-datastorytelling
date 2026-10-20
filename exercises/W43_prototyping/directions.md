# Three directions

All numbers come from `../W39_data/survey_all_waves_all_subgroups.csv`, read by `make_storyboards.py`.
"Latest" = wave 10 Sep 2026. Age and party numbers = average of the six NORC waves (25 Jun – 10 Sep); the 12 Jun pilot is excluded (different method).
Test from the W42 script: each direction starts with a different first sketch (phone screen / room from above / a table with people).

| | A · Real or AI? | B · Stand where you feel | C · Dinner table |
|---|---|---|---|
| **Context → format** | Web → interactive prototype | Exhibition → animatic | Web or exhibition → branched animatic |
| **First sketch** | a phone screen | a room seen from above | people around a table |
| **Who leads** | alternating: authored hook + ending, visitor answers in the middle | alternating: visitor positions themselves, wall text authored | author, with one choice for the viewer |
| **Data cut** | `ai_community_impact` (real vs fake) → `ai_sentiment` → by age → `ai_agency` | `ai_sentiment` (total) → `ai_agency` | `ai_sentiment` by age, `ai_community_impact` (time saved) by age, `ai_regulation` by party, `ai_agency` |
| **Key numbers** | 82 % see real/fake problems · 69 % concerned / 21 % excited · 18–34: 66 % vs 65+: 76 % concerned · 68 % inevitable / 17 % can shape | 69 of 100 concerned · 68 % inevitable | 65+: 76 % concerned · 18–34: 54 % see time saved · regulation "too little" (environment): Dem 58 % / Rep 36 % · 68 % inevitable |
| **Mapping** | 1 dot = 1 % of respondents, hue = feeling (orange concerned / blue excited / grey none), position = group | position in the room = your feeling; projected dots = respondents, side = feeling | each character = one survey group; speech bubble = an answer; number under it = the share |
| **Non-clicker gets** | the authored opening and ending | the projected crowd + wall texts | the whole scene plays; one branch is chosen by default |
| **Serves criterion** | #1 people like me · #2 own experience · #3 main finding | #1 (with the body) · #3 | #2 (recognise a voice) · #3 · surprise (party gap) |
| **Strength** | closest to our concept v1, testable in W48 with 5 people online | social and physical, strong for an exhibition | human and emotional, no charts needed |
| **Risks** | answering yourself can feel like a quiz; Swiss users vs US data | needs a room + projection; hard to user-test; few data points | characters can stereotype groups; every line must stay backed by data; party labels mean little in CH |
| **What we'd drop** | race subgroups (small n), party by default | trend over time | race subgroups, the trend |

## Recommendation (for the group to decide)
Take **A** into W44 as the main direction: it matches concept v1, uses the most of our success criteria and is the easiest to build and test.
Keep **B's** "you're standing with 69 of 100" moment as an idea for A's step 4, and **C's** dinner-table voices as a possible tone for the hook text.
