# W39 · Assignments B + C — Findings

Numbers from `analysis.py` (run it to reproduce). "NORC waves" = the 6 comparable waves 25 Jun – 10 Sep 2026 (pilot excluded).
Latest wave = 10 Sep 2026 (n = 1,083, ±4.1 pts).

## B · Notebook steps (done in `analysis.py` / course notebook)
Loaded the master CSV (9,176 rows × 7 cols, 0 technical NaNs) · tidy already (one row = subgroup × wave × question × item × answer) ·
7 waves, 12 subgroups, 6 questions / 20 items · "uncertain" answers checked (Q6 below) · charts in `output/`.

## C · Questions → answers

| # | Question | Answer | Surprise? |
|---|---|---|---|
| 1 | Has the mood changed over time? | **Basically no.** Across the NORC waves 66–72 % are concerned and 20–27 % excited. Moves are within the ±3–4 pt margin. The big drop from the pilot (40 % → 24 % excited) is most likely a method change. | Stability is the story, not change |
| 2 | Which groups are most / least concerned? | Most: **65+ (76 %)**, Democrats (73 %), white non-Hispanic (72 %), women (72 %). Least: **Black non-Hispanic (58 %)**, 35–49 (63 %), men (65 %). Every single group is more concerned than excited. | Black Americans are the most optimistic group |
| 3 | Dem vs Rep — do they differ? | On *feeling* only a little: Dem 73 % vs Rep 66 % concerned. On *what government should do* a lot: "government does too little" on the environment/data centres 59 % vs 36 % (+23), workers & jobs 55 vs 34 (+21), children 56 vs 39 (+17). | Worry is bipartisan, the remedy is partisan |
| 4 | Are young people more enthusiastic? | Slightly: 18–34 → 24 % excited vs 65+ → 16 %. But the young also *see* more effects: time saved 54 % vs 34 %, pressure to do more 53 % vs 37 %. The old expect more of everything in the future: breakthroughs 74 % vs 59 %, AI smarter than humans 73 % vs 63 %. | Young = experience it now, old = imagine the future |
| 5 | What do people already see happening? | **82 % already see people struggling to tell real from fake.** Losing connections 61 %, pressure 49 %, saving time 49 %, better health care only 18 %. | Fakes are *the* lived experience |
| 6 | What does AI do to families? | Job security worse **75 %** (better 14 %), children's well-being worse 64 %, outlook worse 59 %, household finances worse 42 %. | Jobs + kids = the emotional core |
| 7 | Can we still shape AI? | **68 % say AI is inevitable**, only 17 % think society can shape it. | Concerned *and* powerless — strongest tension in the data |
| 8 | What about the next 20 years? | Over 70 % think each is already happening or likely: AI behaving unintentionally 78 %, smarter than humans 72 %, weapons of mass destruction 71 %, **and** medical breakthroughs 70 %. | People expect the miracle and the disaster at once |
| 9 | Regulation? | Plurality says government does **too little**: children 50 %, environment 48 %, jobs 45 % — only ~25 % say too much. | |
| 10 | How big is "don't know"? | Up to 29 % (better health care), 23 % (competitiveness). Uncertainty is highest where people have no direct experience. | |
| 11 | Do AI events show up? | Possible signal: the 23–28 Jul wave has the **highest concern (72 %) and lowest excitement (20 %)**. It was fielded right after the reported first autonomous AI-agent cyberattack (21 Jul 2026, see Wikipedia "2026 in AI"). But +6 pts vs the previous wave is close to the margin of error, and the next waves stay ~69 %. → hypothesis only, needs a proper event timeline. | |

## Insights for the concept
1. **"Worried but powerless"** — 69 % concerned, 68 % "inevitable". That gap is a story with tension.
2. **Real vs fake** is the experience almost everyone shares (82 %) — a strong point of connection for any visitor.
3. **The split is about solutions, not feelings** — Democrats and Republicans worry similarly but disagree on regulation.
4. **Stability over time** — the honest headline is "nothing changes", which is itself interesting in a fast-moving AI news cycle.
5. **"People like you"** works with this data: 12 subgroups → visitor picks their group, sees where they stand vs. others (NYT jobless-rate pattern from W41).

## Open questions
- How do Independents feel? (not published as a group)
- Does concern differ by education or income? (weighted for, not published)
- Would a longer series show event effects? Build a timeline of AI news per wave.
- What's in "none of these" (~10 %)?

## Sources for thematic research
- Pew Research Center (Apr 2025) — 51 % of US adults more concerned than excited, vs 15 % of AI experts; ~60 % worry regulation won't go far enough.
  https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/
- The Hill on the first NORC wave (65 % concerned, 24 % excited, ~70 % can't control AI in their lives) — https://thehill.com/policy/technology/5955918-americans-ai-sentiment-poll/
- 2026 in artificial intelligence (event timeline, incl. 21 Jul agent cyberattack report) — https://en.wikipedia.org/wiki/2026_in_artificial_intelligence
- NORC on AI and health information — https://www.norc.org/research/library/ai-changing-how-americans-access-health-information-many-remain-skeptical.html
- To do: search the Swiss Media Database (SMD via HSLU library) for Swiss coverage of AI attitudes.
