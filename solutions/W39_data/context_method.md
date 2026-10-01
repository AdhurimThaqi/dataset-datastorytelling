# W39 · Assignment A — Context & method

Sources: `data.json` (methodology_notes + per-wave notes), The Hill (7 Jul 2026), EA Forum launch post — links at the bottom.

## Context
**Who collects the data, and for whom?**
Athena Insights, a newly founded US non-profit, publishes it as "Americans on AI" (americanson.ai).
Fieldwork: NORC at the University of Chicago (AmeriSpeak panel); the pilot was run on Prolific.
Audience: people working on AI policy, journalists, the public. Interactive Things is building the official platform.

**Why is it collected / intended purpose?**
To track US opinion on AI *continuously* instead of one-off polls: separate stable attitudes from short-term swings
and see which outside events move opinion. Research lead Colin Bortner on the design: a deliberately "very neutral instrument"
so that if AI affects people negatively, it shows up in the data.

**Who could benefit?** Policymakers and regulators, journalists, AI companies (public trust), advocacy groups on both sides,
and the public — "how do people like me feel?".
Caution: the project comes out of the AI-policy community (launched on the Effective Altruism forum). That doesn't make the numbers
wrong, but it's worth naming when we judge which questions were chosen.

## Method
**How was it collected?** Online/phone questionnaire, 6 fixed questions (20 items), repeated every ~2 weeks.
- Pilot (12–18 Jun 2026): Prolific, **non-probability** online panel, n = 1,799, forced response (no "No answer"), party without leaners.
- From 25 Jun 2026: NORC **AmeriSpeak, probability-based** household panel, mixed mode (~90–98 % web, rest phone),
  n = 1,055–2,430 per wave, margin of error **±2.5 to ±4.2 points**. Weighted (raking) to Census benchmarks on age, sex, region,
  race/ethnicity, education, plus 2024 presidential vote. Party is *not* a weighting target.

**Who/what is included?** US adults 18+, nationwide, June–September 2026 (7 waves). Subgroups: gender, party (Dem/Rep), 4 age bands,
3 race/ethnicity groups (from the first NORC wave on). Not included: Independents as their own group, under-18s, non-US, income,
education or urban/rural breakdowns (weighted for, but not published).

**How might the method influence the results?**
1. **Pilot ≠ later waves.** Excitement drops from 40 % (pilot) to 24 % (first NORC wave). Different panel, forced answers,
   different party coding → most of that jump is probably the **method change**, not a change of mood. Treat the pilot as a separate series.
2. **Margins of error of ±3–4 points per wave** (larger for subgroups) → wave-to-wave moves of 2–5 points are mostly noise.
3. **Question wording sets the frame:** "excited vs concerned" forces a two-pole view; "none of these" is the only escape.
   Pew asks a different version ("more concerned / more excited / equal mix") and gets 51 % "more concerned" — so the 68 % here is not directly comparable.
4. **Non-response counts:** "No answer" and "Not sure" are real categories (up to ~28 % on some items). Dropping them would inflate every other share.
5. **Weighting to 2024 vote** keeps the party balance stable but means party composition shifts are partly smoothed away.

## Sources
- The Hill, 7 Jul 2026 — https://thehill.com/policy/technology/5955918-americans-ai-sentiment-poll/
- EA Forum launch post — https://forum.effectivealtruism.org/posts/AnW5Whvkjhafmetns/americans-on-ai-a-new-tracker-of-us-public-opinion-on-ai
- Pew Research Center (Apr 2025), *How the U.S. Public and AI Experts View AI* — https://www.pewresearch.org/internet/2025/04/03/how-the-us-public-and-ai-experts-view-artificial-intelligence/
- Data + methodology: `exercises/W39_data/data.json`
