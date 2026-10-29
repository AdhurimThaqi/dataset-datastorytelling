# Prompts for the prototype (W43 → W44 research documentation)

| | |
|---|---|
| **Course rule (W43 slides)** | "The HTML file and **all prompts** go into the research documentation." |
| **Tool** | Claude (Claude Code, model Opus 5.5), 22.10.2026 |
| **Input** | Hand-drawn Crazy 6's sheet (`../photos/W43_crazy6.jpg`), box 1 "Guess", and the prototype card in `../in-class.md` |
| **Output** | `v1.html`, `v2.html`, `v3.html`: one file each, no build step, opens in any browser (needs internet for the pictures) |
| **Structure** | As taught in W43: role and goal → guardrails → experience → design reference → data, word for word → output |

> **How it was made:** in the chat I asked for the prototype in one short sentence. The model already had the prototype card, the sketch and the dataset in the conversation. Prompt 1 below is the complete brief that v1 was built from, written out so that anyone can paste it into an LLM and get the same prototype.

---

## Prompt 1: build v1

```text
ROLE AND GOAL
You are a front-end developer and data-visualisation designer. Build a small, clickable prototype
of ONE moment of a data story, so that I can test it with real people this week.
Course: Data Storytelling (HSLU). Target group: young adults in Switzerland (20–35) who use AI weekly.
The moment comes from my hand sketch (Crazy 6's, box 1 "Guess"): the reader first guesses whether a
picture is real or made by AI, and only then sees the survey number.

HYPOTHESIS TO TEST
A reader who first fails or hesitates at the guess will feel that the real-vs-fake problem is shared,
not a personal weakness. I am wrong if testers treat it as a quiz score and do not connect the number
to themselves.

GUARDRAILS
- Deliver exactly one self-contained HTML file (inline CSS and JavaScript, no frameworks, no build step).
- Phone first (390 px wide), but it must also work on a laptop. Light and dark mode.
- One aspect of the data only. Do not add other questions or numbers from the survey.
- Use only the numbers given under DATA. Do not invent, average or re-calculate anything.
  Round to whole people and show every rounding in the source line.
- Keep "not sure" and "no answer" visible as their own categories.
- No red/green, no right/wrong colours that match the colour of the data. The score stays small;
  the survey number is the hero.
- Pictures: a neutral subject (no people, no politics, no brands) with a clear licence, credited on screen.
  All pictures show the same kind of scene, so the subject gives nothing away.
- Accessible: real buttons, keyboard shortcuts (R = real, A = AI), alt texts that do not reveal the answer,
  respect "prefers-reduced-motion".
- Nothing is stored or sent anywhere.

EXPERIENCE (in this order)
1. Intro: title "Real or AI?" and one or two short sentences: four mountain valleys, some are photos,
   some were made by AI, trust your gut. One "Start" button.
2. Four rounds, always in the same order (2 AI, 2 real, mixed). Each round: progress bar, one large
   picture, two large buttons REAL / AI. After the tap: what the picture really was, where it comes from,
   how many seconds the reader took to decide, the credit, and a "Next" button.
3. Reveal, first small: "You got X of 4", the four pictures as thumbnails marked ✓/✗, and the reader's
   longest pause ("Your longest pause: 6.1 s on picture 3").
4. Reveal, then big: "57 of 100 Americans say they already see people around them struggling to tell
   what's real from what's fake because of AI." Below it 100 dots (one dot = one person in 100) fill in
   one by one, stop briefly at the 57th, then the rest fill in. Then a legend with all answers.
5. One closing line as the surprise: only 2 in 100 don't expect it at all.
6. Source line: the question word for word, the survey, the dates, n, the margin of error, the roundings,
   and the picture credits. A "Try again" button.
Add two review shortcuts: ?step=end jumps to the reveal, ?theme=dark / ?theme=light forces a theme.

DESIGN REFERENCE
- My course website: calm off-white surface, system font, thin grey lines, rounded cards, one strong colour.
- Unit chart / "100 people" dot grid (as in my W38 mapping exercise): one dot = one person in 100.
- Tone of the text: short, direct, friendly, no jargon. English.

DATA (word for word; use nothing else)
Question: "Thinking about your local community, how much are you seeing each of the following changes
because of AI? People are struggling to tell what's real from what's fake"
Subgroup: total (all US adults). Wave: 2026-09-10.
have_seen 57.13 · starting 24.39 · expect_soon 8.67 · dont_expect 1.98 · not_sure 6.94 · no_answer 0.89
Survey: "Americans on AI", Athena Insights with NORC at the University of Chicago,
fieldwork 10–14 Sep 2026, n = 1,083, margin of error about ±4 percentage points.

PICTURES (Wikimedia Commons)
1 AI  · "Scenic Valley in the Afternoon (Ideogram 2.0).webp" · public domain
2 Real · "2021 in Val Bavona to south.jpg" · SchmalspurDVZO, CC BY-SA 4.0
3 AI  · "Late Afternoon Cloudy Valley (SD3.5).webp" · public domain
4 Real · "Bavona river near Roseto in Val Bavona.jpg" · SchmalspurDVZO, CC BY-SA 4.0
Load them through https://commons.wikimedia.org/wiki/Special:FilePath/<file name>?width=960
and show a short message if a picture cannot load.

OUTPUT
1. The complete HTML file.
2. A list of every rounding you made, with the original value.
3. A list of everything you had to guess or decide yourself.
```

## Prompt 2: corrections to v1

```text
Three corrections, keep everything else the same:
1. The thumbnails of wrong guesses at the end are orange, the same colour as the 57. That mixes up
   "you were wrong" with "people who see it". Make wrong guesses black with a ✗ instead.
2. The 100-dot grid is too big on a phone. Limit it to about 260 px wide.
3. If someone gets all four right, the heading "If that was harder than you thought…" doesn't fit.
   In that case show: "You got all four. But it was only four pictures, and you were looking closely."
```

## Prompt 3: v2, visible time pressure (after the first test)

Test feedback (lecturer, 22.10.2026): *"It's good. I like the time pressure, but it should be more obvious."*
In v1 the time was only measured and shown afterwards. v2 makes it visible.

```text
Make a copy of v1.html as v2.html and change only the time pressure. Keep everything else.

GOAL
The reader should feel the time pressure while looking at the picture, not only read about it afterwards.
Testers said the timing was the most interesting part but it was hidden.

CHANGES
1. Intro: add one bold line "⏱ You only get 5 seconds per picture." and one line that explains why:
   "That's about how long you look at a post before you scroll on." Add to the small print:
   "No answer in time counts as 'not sure'."
2. On each picture: a round countdown in the top-right corner (big number 5 → 1 with a ring that empties)
   and a thin bar under the picture that shrinks. In the last 2 seconds both turn orange and the circle pulses
   (no pulsing when the user prefers reduced motion).
3. The clock only starts when the picture has loaded, so a slow connection does not eat the time.
4. When time runs out: the buttons lock, the picture turns dark grey with "Time's up", and the answer says
   "Time's up. That counts as 'not sure'. It was made by AI / a real photo."
5. Reveal: timed-out pictures get a ⏱ label in grey (not orange: orange is the colour of the 57).
   If the reader ran out of time at least once, replace the "longest pause" line with:
   "You ran out of time on X of 4. In the survey, 7 of 100 Americans also answered 'not sure'."
   Otherwise: "Your longest pause: X of 5 s on picture N."
6. Add the shortcut ?limit=<seconds> (2–30) so I can test other time limits.

DO NOT CHANGE
The pictures, the order, the survey numbers, the 100 dots, the source line.
```

## Prompt 4: v3, a separate, playful clock and a calmer end

Feedback on v2 (my own review, 22.10.2026): the end screen is too cramped, because the picture tiles and the 100 dots sit right on top of each other. The time should be even more obvious, as its own element, and a bit funny.

```text
Make a copy of v2.html as v3.html. Keep the pictures, their order, the survey numbers and the source line.

1. TIME AS ITS OWN ELEMENT (not on top of the picture)
   - Above the picture, a full-width "clock bar": a big round number (5 → 1) on the left and a short,
     funny line on the right that changes every second. Write one set of lines per picture so nothing repeats,
     e.g. 5 "Take a good look 👀" · 4 "Check the light…" · 3 "Hmm. Too perfect?" ·
     2 "Your thumb wants to scroll 👆" · 1 "DECIDE!! 😬".
   - Below it, a burning fuse: a bar that shrinks with a 🔥 riding on its end.
   - In the last 40 % of the time the clock bar turns orange and the number shakes (not with reduced motion).
   - On a tap: the clock stops and says something short ("Locked in! 🔒").
   - On time-out: the picture goes dark and blurred with "🫠 Too slow. The feed moved on.",
     the clock turns grey and says "Time's up! Counts as 'not sure'."
   - Before the first picture, a separate 3-2-1 screen with huge numbers and one line each
     ("Thumbs on REAL and AI…", "Eyes open…", "Here it comes…").
   - The intro shows the rule as its own block: a round "5" and "You get 5 seconds per picture."

2. SPLIT THE END INTO TWO SCREENS, WITH A CTA BETWEEN THEM
   Screen "Your result":
   - a big score "2 / 4" and a heading that reacts:
     all right → "All four! But you knew it was a test." · at least one time-out → "The clock got you, right?" ·
     otherwise → "Not as easy as it looks, right?"
   - the four pictures as a 2×2 grid with a label (✓ REAL / ✗ AI / ⏱ not sure) and the seconds taken
   - small chips: ⚡ fastest, 🐢 slowest, ⏱ how often too slow
   - a bridge sentence: "You're not the only one. How many Americans already see this happening around them?"
   - CTA button at the bottom: "Show me →"
   Screen "The number":
   - "57" very big in the data colour, "of 100 Americans" under it, then the sentence.
   - The 100 dots with more space around them (max. 320 px, 8 px gaps) and "1 dot = 1 person in 100".
   - The legend in its own card, the surprise ("Only 2 in 100 don't expect it at all") as a callout,
     and, if the reader timed out, one line linking their time-out to the 7 of 100 who said "not sure".
   - "Play again" button, then the source line.

3. Review shortcuts: ?step=result and ?step=number.
```

## Prompt 5: v4, a random picture pool (29.10.2026)

Feedback on v3 (three testers, see `test.md`): positive, the timing works, it's fun and clear. But after several plays it gets predictable, because it's always the same four pictures.
In the chat I asked: *"start v4 with the random picture pool"*. The model already had the test notes and `../../W44_plan/concept-refinement.md` in the conversation. Written out as a full brief:

```text
Make a copy of v3.html as v4.html. Keep the clock, the 3-2-1 screen, the result screen, the survey numbers,
the 100 dots and the source line. Change only how the pictures are chosen.

1. A POOL INSTEAD OF FOUR FIXED PICTURES
   - At least 12 pictures, half real, half AI, all mountain valleys with a river (same scene, so the subject
     gives nothing away). Only from Wikimedia Commons, with a licence you have checked:
     AI pictures public domain / CC0, photos CC BY or CC BY-SA, credit shown after each answer.
   - Leave out any picture with a visible watermark or AI badge, any that looks like an illustration,
     and any with an open deletion request on Commons.
2. A RANDOM DRAW EVERY ROUND
   - Each round: exactly 2 real + 2 AI, in random order. The round is still 4 pictures × 5 seconds.
   - Remember (in localStorage, per viewer) which pictures were already shown. No repeats until the pool
     is used up; then start over, but never repeat the round just played.
   - If storage is blocked (private mode), it must still work, just random.
   - Preload only the four pictures of the current round.
3. TEXT
   - Intro: "Two are photos. Two were made by AI." and "New pictures every round (16 in the pool)."
   - The end button: "Play again · new pictures".
   - The source line lists the picture authors and licences.
4. Review shortcut ?reset to forget the pictures already seen.
5. Test it: 2+2 in every round, no repeat from the round before, all pictures covered before any repeat,
   and every picture URL loads.
```

**What was checked (29.10.2026):**
- the draw logic in Node.js: 2,000 simulated viewers × 12 rounds. Always 2 real + 2 AI, no repeat from the round before, all 16 pictures shown within the first 4 rounds, and it still works with storage blocked.
- all 16 picture links load from Wikimedia (HTTP 200)
- licences and authors read from the Commons file pages

## How the pictures were chosen
- **AI pictures:** from the Wikimedia Commons category "AI-generated landscapes".
  - From v4, all 8 come from one Commons user (VulcanSphere), who generated the same valley prompt with different models (Imagen 3.0, Reve, HiDream, AuraFlow, FLUX, Stable Diffusion 3.5). All are public domain (CC0).
- **Real photos:** from a Commons search for Swiss river valleys (Val Bavona, Ticino).
  - From v4 there are 8, by SchmalspurDVZO (CC BY-SA 4.0), Alain Rouiller (CC BY-SA 2.0) and Adrian Michael (CC BY-SA 3.0).
- **Why this scene:** every picture shows the same scene (a valley with a river), so the subject gives nothing away.
- **Left out in v4:**
  - the Ideogram 2.0 valley from v1–v3, because it has a deletion request on Commons (Sept 2026)
  - the Imagen 4.0 valley, which has a visible "ai" badge in the corner
  - the SD1.5 and FLUX poster images, which look like illustrations

## Checks
All numbers checked against `exercises/W39_data/survey_all_waves_all_subgroups.csv` (see `README.md`): 0 mismatches, and the dots add up to 100.

## Next prompts (v5 …)
One change per prompt, based on what testers said (`test.md`). Save each version as a new file and add the prompt here.
