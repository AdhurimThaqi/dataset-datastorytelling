# Three checks before we trust the draft (W42 §9.3)

**Draft:** `index.html` (direction A), built by `build.py` from `template.html` + the official CSV.
- Open it in a browser: double-click `index.html`.
- **Review shortcuts:** `index.html?step=4&a=somewhat_concerned&g=age_18_34`
  - `step` = 1–6
  - `a` = sentiment answer code
  - `b` = agency answer code
  - `g` = subgroup
  - `theme` = light / dark

## 1 · Check the numbers: three numbers, against the CSV

Source: `exercises/W39_data/survey_all_waves_all_subgroups.csv`, line numbers as in the file (header = line 1).

| # | Shown in the draft | CSV rows (Subgroup, Wave, Question_ID, Answer, Percentage) | Match? |
|---|---|---|---|
| 1 | Step 2: **"4 in 5"** … "81.5 %" have seen or are starting to see people struggling to tell real from fake | l. 8125 `total, 2026-09-10, ai_community_impact` (item "…what's real from what's fake"), `have_seen, 57.13` + l. 8126 `starting, 24.39` = **81.52** | ✅ 81.52 → "81.5 %"; "4 in 5" = 80 ± 3.5 pts (rule in `data_cut.words`) |
| 2 | Step 5: **"AI is coming into our lives whether we want it or not 67.5 %"** | l. 7866 `total, 2026-09-10, ai_agency, inevitable, 67.51` | ✅ 67.51 → "67.5 %" |
| 3 | Step 5: **"18–34: 27 in 100 vs 65+: 8 in 100"** ("can shape") | l. 7885 `age_18_34, 2026-09-10, ai_agency, can_shape, 26.66` · l. 7896 `age_65_plus, 2026-09-10, ai_agency, can_shape, 8.13` | ✅ 26.66 → 27, 8.13 → 8 |

- **Extra check, by code:**
  - every value embedded in `index.html` (12 subgroups × sentiment, agency and real/fake codes) was compared with the CSV by a script on 20.10.2026: **0 mismatches**
  - a missing CSV row is shown as 0 (see §2)
- To reproduce: `python ../data_cut.py` prints the same values.

## 2 · Read the AI's list: filters, averages, roundings, guesses

**Mappings used**
- dot = about 1 in 1,000 US adults
- answer → position in the dot field (scale order, then none / no answer)
- excited → blue (very = darker), concerned → orange (very = darker), none / neither / no answer → greys. No red/green.
- visitor → one extra dot with an outline, inside the block of their answer ("You + 1,000")
- subgroup tab → the same 1,000 dots re-coloured with that group's distribution
- second question → the dots re-sort (explicitly *not* the same people)
- "can shape" by age → bar length 0–100 %

**Filters**
- latest NORC wave only (`2026-09-10`, field dates 10–14 Sep 2026, n = 1,083)
- pilot wave `2026-06-12` (Prolific, different method) excluded
- earlier NORC waves not shown

**Grouping**
- "excited" = very + somewhat excited
- "concerned" = very + somewhat concerned
- "seen" (real/fake) = have seen + starting to see
- These nets are the same as in `data.json` (`excited_sum`, `concerned_sum`, `seen_sum`).

**Averaging:** none. No averages across waves or across groups.

**Rounding**
- percentages shown with 1 decimal ("67.5 %"), or as "x in 100" (rounded to whole numbers)
- the headline words ("4 in 5", "2 in 3") come from `data_cut.words()`: a fraction is used only if the value is within ±3.5 pts of it
- dots: share × 10, rounded with the largest-remainder method so the dots always add up to 1,000. Example: 'none' 9.10 % → 91 dots.
- values above 0 but below 0.05 % are shown as "<0.1 %"

**Missing values**
- 8 "no answer" rows are not in the CSV for the latest wave: 50–64 (sentiment, agency, real/fake), women (sentiment), Hispanic (sentiment, agency), white non-Hispanic (sentiment, real/fake)
- they are shown as 0 % (the categories still add up to ~100)

**Assumptions / guesses**
1. **Subgroup margin of error is estimated, not published:** ±4.05 × √(1,083 / n), i.e. the same design effect as the full sample, at p = 0.5 (conservative).
   - A gap counts as "real" only if it is bigger than √(MoE₁² + MoE₂²).
   - Result: 18–34 vs 65+ on "can shape" = 18.5 pts > ±11.8 → real. 18–34 vs 35–49 = 4.1 pts < ±12.4 → "about the same".
   - Tab text vs "all US adults" uses the same rule. 18–34 concerned 61 vs 69 → "about the same", because the test is strict: 18–34 is part of the total.
2. **No crosstab between the two questions.** The closing sentence says "most are worried, and most think it's coming anyway" (two separate majorities).
   It does **not** say "the worried are the ones who think it's inevitable". The lower bound of the overlap is 36.3 % of all adults.
3. **Changed wording vs. concept v1:** the concept says "people under 35 are the *most* likely to think it can still be shaped".
   - 18–34 (26.7) vs 35–49 (22.5) is inside the margin, so "most likely" isn't supported.
   - The draft says "**younger adults are more likely than older adults**", and only while the 18–34 vs 65+ gap is real (checked again at every build).
   - → The group should decide on the wording in `concept.md`.
4. **Hook image:** placeholder. It isn't dataset content and gets chosen in W44.
5. **Colours:** blue/orange from the course palette. Each arm was validated as an ordinal ramp (light and dark mode), with direct labels + a table view as relief for the light steps.
   - [A] blue/orange reads as neutral → test in W48.

## 3 · Protect people: no names, quotes or personal data

- [x] **`prompt.md` contains no names, no ages, no study programme and no verbatim interview quotes.** The two interview points are rewritten in our own words ("an older interviewee felt left out of the decision about AI"; "a younger one could not tell whether a video online was real").
- [x] **`index.html` / `template.html` contain no interview content at all.** Checked by search on 20.10.2026 for every quote keyword from `../W40_interviews/` (TikTok, Pope, dinner, boss, "Nobody asks", P1–P3): 0 hits.
- [x] **The page stores nothing:** no cookies, no localStorage, no network requests (the page loads no external scripts). The visitor's answers live only in page memory and are gone on reload.
- [x] **Only the official aggregated dataset** (weighted % per subgroup) went into the draft, no individual respondents.
- Follow the HSLU rules on AI tools. The prompt and the result are saved here as research documentation (W42 §9.4).

## Still to do (W42 §9.4: "it's still a sketch")
- [ ] Make a second version with a different example (e.g. a different look borrowed from another reference) and compare. Note what doesn't work.
- [ ] Re-run the prompt with the photo of the **hand sketch** of A instead of the wireframe.
