# Data Storytelling — *Worried, but it's coming anyway*

HSLU · I.BA_DAS Data Storytelling · autumn semester 2026 · solo project by Adhurim Thaqi
**Live site:** https://adhurimthaqi.github.io/dataset-datastorytelling/

## The idea
A short interactive web game (about 4 minutes, phone first) that lets young adults in Switzerland find out
how their own feeling about AI compares with what Americans actually think, using a real, representative survey
instead of comment sections.

- **Data:** *Americans on AI* (Athena Insights, fieldwork by NORC), a survey of about 1,000–2,400 US adults every two weeks.
  We use the latest wave (10–14 Sep 2026, n = 1,083); the June pilot is excluded because it used a different method.
- **Client / audience for the final presentation:** Interactive Things (Zurich), who build the official platform for this data.
- **Target group:** students and young professionals (20–35) who use AI regularly but haven't made up their minds about it.
- **Key message:** *Most Americans are worried about AI, and most think it's coming anyway. Younger adults are more likely
  than older adults to think it can still be shaped.*

### Direction A — "Real or AI?" (the one we build)
The idea in one line: **first you find out yourself how hard it is to tell real from fake, then you find out that most Americans
already see this around them, and what they think about AI.** The experience on your own screen makes the survey number personal.

## How the prototype works (v8)
**▶ Play it:** https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W47_sprint3/v8.html
(works on a phone and a laptop; about 4 minutes. Normal play sends nothing anywhere: scores stay on your device. Only in a live room, see below, are your player name and score sent to the room screen.)

### The 5 levels
| # | Level | What you do | What you learn |
|---|---|---|---|
| 1 | 🌄 **Real or AI?** | 6 pictures of Swiss mountain valleys: **real photo or AI?** 5 seconds each. The first 2 are easy (older AI); then 🧨 **hard mode**, ×1.5 points: new 2026 AI models against real photos that *look* fake. | Older AI pictures are "too perfect", but "too beautiful" is no proof; look at signs, repeating houses, staged mess. |
| 2 | ✍️ **Texts** | 2 short travel texts: **written by a person or by AI?** | AI text sounds like a brochure and has no names or details you could check. |
| 3 | 🎯 **The number** | Guess with a slider: how many of 100 Americans already see people struggling to tell real from fake? | **57 in 100** already see it, only 2 in 100 don't expect it. |
| 4 | ⚡ **True or false** | 3 quick claims about AI risks and families. Some use the real number, some a wrong one. 8 seconds each. | The real numbers, for example how many say AI is making families' job security worse. |
| 5 | 🫵 **Your turn** | Answer the survey's own two questions, then guess how America answered. | **2 in 3** are concerned; **2 in 3** say AI is coming anyway; younger adults (18–34) are more likely than 65+ to think it can still be shaped. |

At the end: your **final score and rank**, your **badges**, the **key message**, a "**What you learned**" summary, the
**leaderboard**, and a **challenge link** for a friend (after playing someone's link: a head-to-head per level and a reply link).

### How you play
- **Answer:** tap or click **AI** or **REAL**, swipe (left = AI, right = real), or press **←** / **→** on a keyboard.
- **No "Next" button and no scrolling:** after each answer the result slides over the picture (right or wrong, who made it,
  *how to tell*, the photographer and licence), then the game moves on by itself. Tap or press **Space** to skip,
  or **Keep open** to read it calmly.
- **Fits a phone:** every playing screen fits without scrolling at real phone heights (checked at 375×553, 390×664, 393×740,
  412×780, i.e. with the browser bars). On *The number*, the dots and your guess sit side by side and the exact survey question
  opens with a tap. The two result screens can be longer than a phone, but **Next** stays pinned at the bottom.
- **Hint:** 💡 shows what to look at (never the answer) and costs 40 points.
- **True or false:** after each answer the real number stays up for 9 seconds (tap to pause, **Next ▶** to go on).
- **Screen readers:** every picture has a scene description (`alt.json`) that never gives away the answer.

### The game layer
- **Points:** for being right, a speed bonus, a streak bonus (🔥 in a row), and for guesses close to the real number.
- **7 badges:** Eagle eye, Lightning, On fire, Bullseye, Fact-checker, Mind reader, No hints.
- **Rank:** from *Doom-scroller* to *AI whisperer*.
- **Field notes:** every answer adds a clue (how to spot AI) or a fact (a survey number) to your notebook, so you learn
  while you play.
- **Leaderboard:** the top 10 on the device, good for passing one phone around in class.
- **Challenge a friend:** the link gives them the same pictures and questions, with your score to beat and a live race bar.
  At the end they see **who won, level by level**, and can send a **reply link** back (rematch on the same pictures).
  Scores that reach you by link go on your leaderboard, marked 🔗. There's no server: the link itself carries the name and the points.

### The screen
- **Start screen:** the title, one sentence (*"First, spot the AI fakes among real photos and texts of Swiss valleys. Then guess what US
  adults think about AI and see how your guesses compare."*), a preview of four pictures, your player name (with a dice button for
  a random name) and **Start the game**. No score, levels or badges yet; the header button opens only the leaderboard.
- **While you play, only the challenge:** a minimal top bar (level, points, **☰ Progress**). No side panels.
- **☰ Progress** opens one drawer with three tabs: **You** (score, streak, levels, badges), **Notes**, **Board** (leaderboard).
  It opens only on a click, tap or key: a side drawer on a laptop, a bottom sheet on a phone. It closes with ✕, a click outside or Esc.
- **End screen:** the survey findings come first (key message and three big numbers), then you vs. US adults, then your score.
- Light and dark mode follow the device setting. Sound: three soft cues only (right, wrong, the end), no toggle.
- **One icon family:** [Lucide](https://lucide.dev) outline icons (ISC licence), 16–20 px, inlined from `icons.json`, so the page works offline.
  No emoji in the interface. Icon-only buttons have a tooltip and a screen-reader label. Right/wrong is shown by an icon and a word
  as well as colour, and badges say *Locked* or *Earned*. The homepage uses the same icons.

### The pictures and texts
- **35 pictures** of the same kind of scene (Swiss river valleys), so the subject gives nothing away:
  - 16 from the earlier versions (the warm-up)
  - 8 photoreal AI pictures generated for this prototype in Figma AI (gpt-image-2.5, gemini-3.1-flash-image)
  - 2 AI pictures from Wikimedia Commons
  - 9 real photos from Commons that look "too good"
- **Every picture is cropped, resized and compressed the same way** and renamed `p01…p35`, so the file name or quality
  can't give away the answer.
- New pictures every round until you've seen them all.
- **Texts:** the human texts are word for word from Wikivoyage versions saved *before* ChatGPT existed. The AI texts were
  written by Claude.

### Honesty rules built in
- **Every survey number comes from the official CSV.** `check.py` compares the page with the data (149 checks, 0 mismatches).
- **Not a real difference:** two numbers within the margin of error are called "too close to call", not a difference.
- **True or false:** after the answer, the real number is always shown.
- **Not Swiss opinions:** these are US adults (latest wave, 10–14 Sep 2026, n = 1,083), and the game says so.

### Live round for the presentation: "scan the QR code and let's play together"
1. On the projector, open **https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W47_sprint3/live.html?room=hslu** (any room code works, e.g. `?room=it-final`). Press **F** for fullscreen.
2. The audience scans the QR code (on the projector page, or on your slide: `exercises/W47_sprint3/qr/slide-hslu.png`, or just the code
   `qr/qr-hslu.png` / `.svg`; for another room run `python make_qr.py <room>`). It opens the game in that room (`v8.html?room=…`), so **everyone plays the same round**.
3. The start screen says clearly that the player name and score will appear on the big screen. At the end, each phone shows
   *"You're #3 of 18 in the room"*, and the projector shows the **live top 10** (best round per name) and the number of players.
4. Rude name? **Click it on the projector** to hide it there ("Show hidden" brings it back).
5. **Fresh start:** use a new room code (e.g. one per session). Old rooms stay in the database but never show up.

How it works: a small Supabase project (`real-or-ai-live`, region Zurich) with one table, `room_scores`. It holds only the room code,
player name, score and "x of 8 spotted". The page uses the public publishable key (`room.json`). Row-level security allows
**adding and reading only**, nobody can change or delete scores through the API, and the database rejects impossible values
(score 0–5000, names up to 18 characters). If the connection fails, the phone shows *Try again* and the score stays on the phone.
The GitHub repo does **not** need to be connected to Supabase.

To delete a room's scores after the talk, run this in the Supabase SQL editor: `delete from room_scores where room = 'hslu';`

### Final presentation (17.12.2026)
Everything is in **`Final-presentation/`**, built on my own slide template (`Adhurim Thaqi — School Template.pptx`, Syne + Outfit):
- **`slides.html`**: [open it](https://adhurimthaqi.github.io/dataset-datastorytelling/Final-presentation/slides.html). Arrow keys or Space, **F** fullscreen,
  **N** speaker notes; slide 2 links straight to the live room. Each slide builds in, and the chart bars grow.
- **`Real-or-AI_final-presentation.pptx`**: the same 13 slides with speaker notes, fade transitions and build-in animations
  (they run by themselves, no extra clicks). The fonts are embedded.
- **`Real-or-AI_final-presentation.pdf`**: backup without animations.
- Rebuild the PowerPoint and PDF with `python Final-presentation/build_deck.py` (needs PowerPoint for the PDF).

Order of the talk (about 7 minutes plus the live round): scan and play → why (interviews) → 57 in 100 → the game →
what it looks like → key message → by age → what testing changed → honesty → conclusion.

### How it's built
- **One HTML file** with no framework. It's generated: `template.html` + the survey CSV + `pool.json` + `alt.json` + `icons.json` + `room.json` → `build.py` → `v8.html`
  (and `live_template.html` → `live.html`, the projector page; QR codes with the vendored `vendor/qrcode.js`, MIT).
- **Rebuild:** run `python exercises/W47_sprint3/build.py`, then check it with `python check.py`.
- **Pictures:** `prepare_images.py` downloads and prepares them.
- **Review shortcuts:** `?step=pics`, `?step=text`, `?step=boss`, `?step=tf`, `?step=end` … jump to a level; `?theme=dark` and `?limit=8`
  (seconds per picture) also work.
- **More detail:** `exercises/W47_sprint3/README.md`; all prompts in `exercises/W43_prototyping/prototype/prompts.md`.
- **Earlier versions:**
  - v1–v4: the hook only
  - v5: the six-step story
  - v6: hints and the text round
  - v7: the full game with 7 levels (tested at the 19.11 coaching)

## Background
Alternatives sketched for Milestone 2: **B "Stand where you feel"** (exhibition: visitors stand on a floor scale and a crowd of
dots forms around them) and **C "Dinner table"** (branched animatic: age groups talk at a table, the viewer picks a seat).

### Why it works (from the interviews)
- All three interviewees told a real-vs-fake story → the hook is a shared experience.
- Nobody reads surveys; opinions come from Reddit, comments and polls.
- *"The challenge is knowing whether the people commenting represent the wider population or just a very vocal group."*
  (interview 2) → a representative survey answers exactly that.

## Where we are
*Last updated 26.11.2026: prototype v8 (5 levels) is built; test it on a real phone next.*

| Week | Milestone | Status |
|---|---|---|
| W41 · 08.10 | User research, rebriefing, concept | ✅ [Milestone 1 page](https://adhurimthaqi.github.io/dataset-datastorytelling/w41.html) |
| W43 · 22.10 | At least three designs, sketched by hand; first prototype of the hook (v1–v3) | ✅ [Milestone 2 page](https://adhurimthaqi.github.io/dataset-datastorytelling/w43.html) |
| W44 · 29.10 | Implementation plan, sprint plan, design references; test results (3 testers); v4 with a random picture pool | ✅ [Plan (PDF)](https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W44_plan/documentation/01_implementation-plan.pdf) · [v4](https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W43_prototyping/prototype/v4.html) |
| W45 · 05.11 | Sprint 1: all six steps in one file (v5); mentoring (Alain) → v6 with AI hints and a text round | ✅ [v5](https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W45_sprint1/v5.html) · [v6](https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W46_sprint2/v6.html) |
| W46 · 12.11 | Mentoring 2 (Alain) → v7: the full game (game layout, 7 levels, harder AI pictures, the data as games, leaderboard and challenge link) | ✅ [v7](https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W47_sprint3/v7.html) |
| W47 · 19.11 | Coaching → v8: 5 levels instead of 7 ("more or fewer" removed, one picture level that gets harder), tap/click on the answer buttons, challenge link with a head-to-head and reply | ✅ [v8](https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W47_sprint3/v8.html) |
| W48 · 26.11 | Results of the user test; test v8 on a real phone | ⏳ next |
| W51 · 17.12 | Interactive prototype + short rationale (max. 2 pages), presented to Interactive Things | 🟡 slides ready: [`Final-presentation/`](https://adhurimthaqi.github.io/dataset-datastorytelling/Final-presentation/slides.html); rationale still to write |

**W43 lesson (Gordan Savičić):** a prototype tests *one* aspect of the data with *one* interaction. Build it as one HTML file
with an LLM: interaction first, one change per prompt, save versions (`v1.html`, `v2.html` …), and check every number
against the source. Then watch a stranger use it for three minutes and ask "What did you take away?".

## The site
| Page | What |
|---|---|
| [Home](https://adhurimthaqi.github.io/dataset-datastorytelling/) | Links to everything |
| [Americans on AI](https://adhurimthaqi.github.io/dataset-datastorytelling/ai.html) | The data findings: headline numbers, trend, "find your group" |
| [Milestone 1](https://adhurimthaqi.github.io/dataset-datastorytelling/w41.html) | Rebriefing, user survey, concept |
| [Milestone 2](https://adhurimthaqi.github.io/dataset-datastorytelling/w43.html) | Hand sketches, directions, wireframes, comparison, AI draft |
| [Prototype v8](https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W47_sprint3/v8.html) | The current prototype: Real or AI? as a game, then the survey data as games (5 levels, about 4 minutes) |
| [Slide presentation](https://adhurimthaqi.github.io/dataset-datastorytelling/Final-presentation/slides.html) | The final presentation (17.12): slides in the browser, plus [PDF](https://adhurimthaqi.github.io/dataset-datastorytelling/Final-presentation/Real-or-AI_final-presentation.pdf) and [PowerPoint](https://adhurimthaqi.github.io/dataset-datastorytelling/Final-presentation/Real-or-AI_final-presentation.pptx) |
| [Exercises & process](https://adhurimthaqi.github.io/dataset-datastorytelling/exercises.html) | Process log, W38–W40 exercises, file list |
| [Practice report](https://adhurimthaqi.github.io/dataset-datastorytelling/output/report.html) | Warm-up with four public datasets |

## The repo
| Folder / file | What |
|---|---|
| `exercises/` | The coursework: `W38_mapping`, `W39_data` (survey CSV, `data.json`, notebook), `W40_interviews` (3 interviews, criteria), `W41_concept`, `W43_prototyping` (directions, hand-sketch photos, AI draft, prototypes v1–v4, `prompts.md`), `W44_plan` (implementation and sprint plan), `W45_sprint1` (v5), `W46_sprint2` (v6), `W47_sprint3` (v7, v8), `process-log.md` |
| `solutions/` | Worked versions of W38–W41 (mappings, analysis, findings with sources) |
| `ai.html`, `w41.html`, `w43.html`, `exercises.html`, `index.html` | The site pages (rebuilt by the `build_page.py` scripts) |
| `explore.py`, `data/`, `output/` | The warm-up practice (see below) |

**Rules we keep:** every number comes from the official dataset; differences smaller than the margin of error are not called
differences; "not sure" / "no answer" stay visible; neutral towards AI. **AI use** (Claude) is named in the process log
and on the pages wherever it was used.

**Sources:** Athena Insights / NORC, *Americans on AI* (americanson.ai) · course material by Alain Leclerc von Bonin,
Gordan Savičić and Fiona Zellweger (HSLU) · the four W38 datasets and the course notebook are course material.

---

## Practice: four public datasets (warm-up)
Inspect → clean → find the story → visualise, on four real, public datasets.

## Run it

```bash
pip install -r requirements.txt
python explore.py            # all 4 datasets
python explore.py titanic    # just one: gapminder | co2 | titanic | weather
```

The terminal prints each step (size, missing values, key numbers).
Charts land in `output/` — open **`output/report.html`** in a browser to see them all.
Every chart has a camera icon (top-right) → export PNG for storyboards / animatics.

## The datasets

| File | What | Rows | Story angle | Source |
|---|---|---|---|---|
| `gapminder.csv` | Life expectancy, GDP, population per country, 1952–2007 (5-yr steps) | 1,704 | Animated: "the world got healthier" | Gapminder via [plotly/datasets](https://github.com/plotly/datasets) |
| `co2-emissions.csv` | CO2 per country & fuel, 1950–2024 (trimmed to 16 columns) | 18,984 | Ethics/framing: total vs per person, produced vs consumed (Switzerland!) | [Our World in Data](https://github.com/owid/co2-data) |
| `titanic.csv` | 891 passengers: class, sex, age, fare, survived | 891 | Branching animatic: each attribute = a decision node | [datasciencedojo/datasets](https://github.com/datasciencedojo/datasets) |
| `seattle-weather.csv` | Daily temp, rain, wind, weather type, 2012–2015 | 1,461 | Cleaning & smoothing noisy time series | [vega-datasets](https://github.com/vega/vega-datasets) |

## Things to try
- Change a chart title in `explore.py` — notice how the title alone changes the story.
- In the CO2 chart, toggle **Total / Per person**: who's the "worst" emitter flips.
- Swap `"Switzerland"` for another country in `co2()`.
- Titanic: add `AgeGroup` to the sunburst `path=[...]` for a deeper branch.


# Professor's feedback 
- Questions to ask? 
- a. "What's missing for a 6?"
- b. "Is US survey data okay for a Swiss audience, or should I frame it differently?"
- c. "Is ~5 minutes and 7 levels the right length?"


# Answers 
- It might be a good solution to add a timer onboarding or anything that lets the user prepare for the content. 
- Dense - too much text 
- Responsivness in the phone. Fit on screen (game interface). 
- more or fewer - unsure what number is fewer 
- also add clicking as well besides dragging 
- prompt md information we dont need it to show in the web 
