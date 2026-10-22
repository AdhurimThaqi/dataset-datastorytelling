# Prompts for the prototype (W43 → W44 research documentation)

- **Course rule (W43 slides):** "The HTML file and **all prompts** go into the research documentation."
- **Tool:** Claude (Claude Code, model Opus 5.5), 22.10.2026, in my repo.
- **Output:** `v1.html`. One file, no build step, opens in any browser. It needs internet for the four pictures.
- **Input:** my hand-drawn Crazy 6's sheet (`../photos/W43_crazy6.jpg`), box 1 "Guess", and the prototype card in `../in-class.md`.

Every prompt is listed below in order, as I typed it. Changes I made by hand are listed after the prompts.

---

## Prompt 1 (me, as typed)

```text
ok u know what we need to do now - we need to generate a html file or whatever make sure its something
good please and it fulfills whats required - thank you
```

The context the model already had: the W43 slides, my prototype card and the Crazy 6's sheet.
So that the prompt follows the slide structure (guardrails → experience → design reference → data, word for word),
the brief the model worked from is written out here in full:

```text
GUARDRAILS
- One HTML file, no frameworks, no build step. Phone first (390 px wide), also works on a laptop.
- One aspect only: "People are struggling to tell what's real from what's fake". No other question from the survey.
- Only numbers from the CSV (latest wave 2026-09-10, total). Do not invent numbers. Show every rounding.
- Keep "not sure" and "no answer" visible. No red/green, no good/bad framing of the guesses.
- No quiz feeling: the score is small, the 57 is big.
- Pictures with a clear licence and a neutral subject (no people, no politics), credited on screen.

EXPERIENCE (the longest part)
1. Intro: "Real or AI?" One sentence: four mountain valleys, some photos, some made by AI. One button.
2. Four rounds. Each: one picture, two big buttons REAL / AI. After the tap: what it really was, where it is from,
   and how many seconds the reader took. Then "Next".
3. Reveal: small: "You got X of 4", the four pictures with ✓/✗, the reader's longest pause.
   Big: "57 of 100 Americans say they already see people around them struggling to tell what's real from what's fake."
   100 dots fill one by one, pause on the 57th, then the rest fill in. Legend with all six answers.
4. One closing line that surprises: only 2 in 100 don't expect it at all.
5. Source line with the question word for word, the survey, the date, n and the margin of error.

DESIGN REFERENCE
- The calm look of my course site (index.html / w41.html): off-white surface, system font, thin lines, one accent.
- The 100-dot "unit chart" idea from my W38 mappings: one dot = one person in 100.

DATA (word for word from the CSV)
Question: "Thinking about your local community, how much are you seeing each of the following changes because of AI?
People are struggling to tell what's real from what's fake"
total, 2026-09-10: have_seen 57.13 · starting 24.39 · expect_soon 8.67 · dont_expect 1.98 · not_sure 6.94 · no_answer 0.89
Survey: Americans on AI, Athena Insights with NORC, 10–14 Sep 2026, n = 1,083, margin of error about ±4 points.
```

## Pictures (chosen during prompt 1)

Searched on Wikimedia Commons. AI pictures come from the category "AI-generated landscapes". Real photos come from a search for Swiss river valleys.
I picked pictures with the same subject (a valley with a river, afternoon light) so the reader can't guess from the subject.

| # | Truth | File on Wikimedia Commons | Licence |
|---|---|---|---|
| 1 | AI (Ideogram 2.0) | Scenic Valley in the Afternoon (Ideogram 2.0).webp | Public domain |
| 2 | Real, Val Bavona TI | 2021 in Val Bavona to south.jpg | CC BY-SA 4.0, SchmalspurDVZO |
| 3 | AI (Stable Diffusion 3.5) | Late Afternoon Cloudy Valley (SD3.5).webp | Public domain |
| 4 | Real, Val Bavona TI | Bavona river near Roseto in Val Bavona.jpg | CC BY-SA 4.0, SchmalspurDVZO |

## Corrections after the first version (v1 is the result)
- The "wrong" tiles at the end were orange, the same colour as the 57. That mixed up "you were wrong" with "people who see it". I changed them to black with ✗.
- The dot grid was too big on a phone; I made it smaller.
- If someone gets all four right, the heading said "harder than you thought". It now says: "You got all four. But it was only four pictures, and you were looking closely."

## Next prompts go here
`v2.html`, `v3.html` …: one change per prompt, saved as a new file. Write down each prompt here **as typed**.
