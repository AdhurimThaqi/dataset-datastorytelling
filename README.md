# Data Storytelling — *Worried, but it's coming anyway*

HSLU · I.BA_DAS Data Storytelling · autumn semester 2026 · solo project by Adhurim Thaqi
**Live site:** https://adhurimthaqi.github.io/dataset-datastorytelling/

## The idea
A short interactive web experience (about 2 minutes, phone first) that lets young adults in Switzerland find out
how their own feeling about AI compares with what Americans actually think, using a real, representative survey
instead of comment sections.

- **Data:** *Americans on AI* (Athena Insights, fieldwork by NORC), a survey of about 1,000–2,400 US adults every two weeks.
  We use the latest wave (10–14 Sep 2026, n = 1,083); the June pilot is excluded because it used a different method.
- **Client / audience for the final presentation:** Interactive Things (Zurich), who build the official platform for this data.
- **Target group:** students and young professionals (20–35) who use AI regularly but haven't made up their minds about it.
- **Key message:** *Most Americans are worried about AI, and most think it's coming anyway. Younger adults are more likely
  than older adults to think it can still be shaped.*

### Direction A — "Real or AI?" (the one we build)
1. **Hook:** the reader guesses whether an image is real or AI-made.
2. **Reveal:** 4 in 5 US adults see people around them struggling to tell real from fake.
3. **You answer:** the survey's own question: excited ↔ concerned, or "none of these".
4. **You vs. America:** your dot among 1,000 dots (one per surveyed American), then by age group.
5. **The turn:** 2 in 3 say AI is coming anyway; 27 % of 18–34 vs 8 % of 65+ think it can still be shaped.
6. **Close:** the key message, plus "US adults, latest wave". Click nothing and it plays on its own.

Alternatives sketched for Milestone 2: **B "Stand where you feel"** (exhibition: visitors stand on a floor scale and a crowd of
dots forms around them) and **C "Dinner table"** (branched animatic: age groups talk at a table, the viewer picks a seat).

### Why it works (from the interviews)
- All three interviewees told a real-vs-fake story → the hook is a shared experience.
- Nobody reads surveys; opinions come from Reddit, comments and polls.
- *"The challenge is knowing whether the people commenting represent the wider population or just a very vocal group."*
  (interview 2) → a representative survey answers exactly that.

## Where we are
| Week | Milestone | Status |
|---|---|---|
| W41 · 08.10 | User research, rebriefing, concept | ✅ [Milestone 1 page](https://adhurimthaqi.github.io/dataset-datastorytelling/w41.html) |
| W43 · 22.10 | At least three designs, sketched by hand | ✅ [Milestone 2 page](https://adhurimthaqi.github.io/dataset-datastorytelling/w43.html) |
| W44 · 29.10 | Implementation plan; refine the concept with the test results; 2–3 design references; the HTML file and all prompts in the research documentation | ⏳ next |
| W48 · 26.11 | Results of the user test | ⏳ |
| W51 · 17.12 | Interactive prototype + short rationale (max. 2 pages), presented to Interactive Things | ⏳ |

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
| [Exercises & process](https://adhurimthaqi.github.io/dataset-datastorytelling/exercises.html) | Process log, W38–W40 exercises, file list |
| [Practice report](https://adhurimthaqi.github.io/dataset-datastorytelling/output/report.html) | Warm-up with four public datasets |

## The repo
| Folder / file | What |
|---|---|
| `exercises/` | The coursework: `W38_mapping`, `W39_data` (survey CSV, `data.json`, notebook), `W40_interviews` (3 interviews, criteria), `W41_concept`, `W43_prototyping` (directions, hand-sketch photos, AI draft), `process-log.md` |
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
