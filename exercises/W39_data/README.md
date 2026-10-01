# W39 · Data exploration — "Americans on AI"

Where does the data come from, how was it collected and structured, which questions and stories can it answer?
Slides: `course-material/W39_260924_Dataexploration_Slides.pdf` in the course folder (local only, not in git).
Original Drive folder: https://tinyurl.com/y5r355ya · Data source: https://www.americanson.ai/en/download

## The data (this folder)
| File | Content |
|---|---|
| `survey_all_waves_all_subgroups.csv` | everything: 9,176 rows × 7 columns |
| `data.json` | raw source (methodology notes, question definitions, per-wave notes) |
| `HSLU_Data_Storytelling_Analysis.ipynb` | course notebook (Colab) |
| `own_exports/` | your filtered CSVs from the notebook's export cell |

The Drive also has per-wave / per-subgroup splits — they are only filtered copies of the master, so make them with the notebook export when you need one.

Columns: `Subgroup, Wave, Question_ID, Full_Question, Dimension, Answer, Percentage` (weighted %, full sample as base).

- **Waves (7):** 2026-06-12 · 06-25 · 07-09 · 07-23 · 08-13 · 08-27 · 09-10
- **Subgroups (12):** total · gender_men/women · party_dem/rep · age_18_34/35_49/50_64/65_plus · race_white_nh/black_nh/hispanic
- **Questions (6):**
  - `ai_sentiment` — excited ↔ concerned about AI's growing role
  - `ai_agency` — can society still shape AI, or is it inevitable?
  - `ai_community_impact` — changes seen locally (saving time, pressure, losing connections, fake vs real, health care)
  - `ai_family_impact` — job security, outlook, children's well-being, household finances
  - `ai_regulation` — government doing too much/too little (children, environment, jobs, competitiveness)
  - `ai_risks` — next 20 years (smarter than humans, unintended behaviour, breakthroughs, weapons of mass destruction)

## ⚠️ Methodology traps (from data.json)
- **The pilot wave (2026-06-12) is different:** Prolific online panel (non-probability), forced response (no "No answer"),
  party measured without leaners. All later waves: NORC AmeriSpeak (probability panel).
  → A drop from wave 1 to wave 2 may be a **method change, not a mood change**. Don't headline it without saying so.
- Race/ethnicity subgroups only exist from the June NORC wave onward (not in the pilot).
- `no_answer` (~14 %) and `not_sure` (~11 %) are real answers — keep them visible, don't silently drop them.
- Party is not a weighting target, so party composition can shift between waves.

## Tools
- `HSLU_Data_Storytelling_Analysis.ipynb` — course notebook (Google Colab): JSON → tidy table, overview, missing values, first chart, **export cell** (filter by wave/subgroup/question → CSV for Datawrapper / RAWGraphs / Tableau).
- `explore_ai.py` — local version of the key numbers + charts: `python explore_ai.py` → `output/`.

## Questions from the notebook to answer yourself
- Does AI sentiment differ between `party_dem` and `party_rep`?
- Are younger people (`age_18_34`) more enthusiastic than older ones (`age_65_plus`)?
- + your own questions

## W39 assignments (from Fiona's slides)
**A · Context & method** — answer in the process doc:
- Who collects the data, for whom, and why? What is it for, who could benefit?
- How was it collected (survey method)? Who/what was included (area, time period)?
- How might the method influence the results? (Different questions → different data)

**B · Notebook** — load data · inspect JSON · make a tidy table · map subgroup IDs to labels ·
explore categories · check missing / uncertain answers · first visualisation.

**C · From data to story**
1. Develop as many questions to ask the dataset as possible
2. Explore them (notebook, americanson.ai, AI tools)
3. Thematic research: existing projects, studies, articles, similar surveys (e.g. Swiss Media Database)
4. Record findings: insights, surprises, open questions

Suggested questions: Do major AI events show up in the data (make an AI-event timeline)? ·
Have attitudes changed over time? · Which groups are most concerned / most confident?

## My findings
| Question | Answer / number | Surprise? | Open question |
|---|---|---|---|
| | | | |
