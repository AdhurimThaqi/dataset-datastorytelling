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
