# Process log — Adhurim Thaqi (solo project)

Every week: what was easy, what was hard, what I'll do better next week, plus research (data, processing, sources).
I work alone, so every contribution below is mine. AI tools I used (Claude) are named where I used them.

## W38 · 17.09 — What are data visualisations?
- **Easy:** Understanding the core idea that a visualisation is a deliberate, lossy compression: someone decides what gets left out.
- **Hard:** The data-mapping homework. I chose the coffee-week dataset and used the "LLM route" the brief allows: Claude generated six mappings as SVGs (`solutions/W38_mapping/`). Two break conventions on purpose (time running right to left, a category mapped to size). I didn't draw my own on paper, so I missed the "every mark is a decision" experience.
- **Better next week:** Draw at least a few sketches myself before using AI.
- **Data / sources:** `exercises/W38_mapping/data/01_Coffee-Week.csv` · W38 script.

## W39 · 24.09 — Data exploration
- **Easy:** Loading the "Americans on AI" survey (7 waves, 12 subgroups, 6 questions) and getting first numbers: about 2 in 3 US adults are concerned about AI, and about 2 in 3 say it's coming anyway.
- **Hard:** The methodology. The first wave (12 Jun) is a pilot from a different panel (Prolific, no "No answer" option). The big drop in "excited" after it is mostly a method change, not a change of mood. I also had to learn that differences under the ±3–4 pt margin of error aren't real differences.
- **Better next week:** Read the method notes (`data.json`) *before* drawing conclusions.
- **Data / sources:** master CSV + `data.json` from the course Drive · course notebook · `solutions/W39_data/analysis.py` and `findings.md` (written with Claude, numbers checked against the CSV) · Pew Research 2025 and The Hill (7 Jul 2026) for context.
- **Repo:** set up the GitHub repo and Pages site; findings page `ai.html`.

## W40 · 01.10 — Research and requirements analysis
- **Easy:** Writing open "tell me about the last time…" questions; the funnel structure (broad → deep → success) made sense.
- **Hard:** Technical side: Windows "filename too long" errors in git (OneDrive path + long folder names) forced me to restructure the repo. Content side: defining one target group instead of "everyone".
- **Better next week:** Recruit interviewees earlier; plan the interviews instead of leaving them to the end.
- **Data / sources:** W40 script, Human-Centred Design script · interview guide in `exercises/W41_concept/user-survey.md`.

## W41 · 08.10 — Concept development (Milestone 1)
- **Easy:** The rebriefing: putting the task in my own words, client vs. end users, guard rails (neutral towards AI, honest with uncertainty).
- **Hard:** My concept and quotes were written before the real interviews existed; the Milestone 1 page still had placeholder quotes. Lesson: research first, concept second.
- **Better next week:** Do the real interviews and replace every placeholder.
- **Data / sources:** `exercises/W41_concept/` (rebriefing, user survey, concept v1, drafted with Claude) · Milestone 1 page `w41.html`.

## W42 · 15.10 + W43 · 22.10 — Prototyping (Milestone 2)
- **Easy:** Finding three directions that really start with a different first sketch: a phone screen (A, web), a room from above (B, exhibition), a dinner table (C, branched animatic).
- **Hard:**
  - I did it in the wrong order. I first made an AI-generated storyboard as a reference (`ai-reference/`), then redrew all three directions by hand (`photos/`). The W42 script says sketch first, AI second.
  - Not overstating the data: there is no crosstab between the two questions, so "two majorities" is fine, but "the worried are the ones who say inevitable" is not. "Under 35 are the *most* likely to think it can be shaped" turned out to be inside the margin of error against 35–49, so I changed it to "more likely than older adults".
  - In A, frames 3 and 6 still had the wrong content (frame 3 repeated the real/AI guess instead of the survey question; frame 6 said "Be more critical", which breaks my own neutrality rule). Corrected on paper.
- **Interviews done:** three people (student 22, marketing assistant 29, retail worker 34). All three told a real-vs-fake story. The strongest new insight came from interview 2: comment sections don't tell you what "most people" think, and a representative survey does. That became my surprise criterion. Nobody aged 50+ yet.
- **Better next week:** Sketch before touching AI; add one 50+ interview; decide web vs. exhibition so the W44 implementation plan has a clear target.
- **Data / sources:** `exercises/W43_prototyping/` (directions, comparison, wireframes, AI draft of A with prompt + three checks, all with Claude) · hand sketches in `photos/` · interviews in `exercises/W40_interviews/interviews/`.

### W43 · 22.10 — in class with Gordan: going deeper (one aspect, one interaction, one test)
- **Easy:**
  - The Crazy 6's, drawn by hand (`photos/W43_crazy6.jpg`)
  - choosing box 1 "Guess" as the one moment to prototype
  - writing the prototype card: hypothesis, "we are wrong if", acceptance
- **Hard:**
  - Keeping it to *one* aspect (the 57) and *one* interaction (Real or AI?), instead of building the whole story.
  - Finding pictures that are the same scene, so the subject gives nothing away, and have a clear licence.
- **What happened:**
  - **v1:** built with Claude as one HTML file, with 4 pictures from Wikimedia Commons. Every number was checked against the CSV.
  - **Lecturer test (v1):** "It's good". He liked the time pressure and asked me to make it more obvious.
  - **v2:** a visible 5-second countdown.
  - **v3:** my own review found the end too cramped, so I added a funny clock bar, a 3-2-1 screen, and split the end into "Your result" → "The number".
- **Better next week:** test with people who don't know the project, not only the lecturer and me.
- **Data / sources:** `exercises/W43_prototyping/prototype/` (v1–v3, `prompts.md` with all prompts, `test.md`) · W43 slides (Gordan) · pictures from Wikimedia Commons (credits in the prototype).

## W44 · 29.10 — Feasibility analysis (remote, Gordan)
- **Easy:**
  - The test results were clear and mostly positive. Three testers tried v3: the timing works, it was fun and clear, all three still remembered the 57 after two minutes, and it felt like a fun game challenge, not a quiz.
  - The implementation plan was quick to write, because most parts already run separately (the v3 hook + the AI draft of the 6 steps).
- **Hard:**
  - The one problem from the test: after several plays it gets predictable, because it's always the same four pictures.
  - **The fix (v4):** a pool of 16 (8 real, 8 AI) with a random draw of 2 + 2 per round and no repeats until the pool is used up.
  - **Building the pool was harder than expected:**
    - The AI picture from v1–v3 has a deletion request on Commons.
    - One AI picture has a visible "ai" badge in the corner, which gives the answer away.
    - Some AI pictures look like illustrations.
    - All three kinds were left out. Licences were checked for each picture.
- **What I did:**
  - `W44_plan/`: concept refinement from the test, an implementation plan (architecture, components, risks, timeline to W51) and three design references (Which Face Is Real?, NYT "You Draw It", Pew Political Typology Quiz)
  - prototype v4, with prompt 5 added to `prompts.md`
  - the test results in `test.md`
  - the home page now links v4
- **Coaching (Gordan):** _feedback: ____________________
- **Still open from last week:**
  - web vs. exhibition (the plan assumes web, phone first)
  - one interview with someone 50+
- **Better next week:**
  - Merge the hook with steps 3–6 into one file.
  - Write the coaching feedback down right after the call.
- **Data / sources:**
  - `exercises/W44_plan/` and `exercises/W43_prototyping/prototype/v4.html` (built with Claude; the draw logic was tested with 2,000 simulated players, and all 16 picture links were checked)
  - Wikimedia Commons file pages for licences
  - design references: whichfaceisreal.com · NYT The Upshot (2015) · pewresearch.org
