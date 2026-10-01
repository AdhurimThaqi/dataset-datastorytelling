# Solutions — I.BA_DAS exercises (W38–W41)

AI-assisted drafts (Claude). Read them, check them, make them yours — and note in the process log which parts were AI-assisted.

| Exercise | Status | Files |
|---|---|---|
| W38 Data mapping | ✅ 6 mappings of the coffee dataset (2 deliberately broken) + answers | `W38_mapping/README.md`, `index.html`, `sketches/`, `mappings.py` |
| W39 A · Context & method | ✅ | `W39_data/context_method.md` |
| W39 B · Notebook steps | ✅ as a script | `W39_data/analysis.py` → `output/` charts |
| W39 C · Questions & research | ✅ 11 questions answered + insights + sources | `W39_data/findings.md` |
| W40 Interview guide | ✅ ready to run | `W40_interviews/interview-guide.md` |
| W40 3 interviews | ❌ **you** — real people, real quotes | `exercises/W40_interviews/interviews/` |
| W40 Criteria | ⚠️ hypotheses from the data — confirm with quotes | `W40_interviews/criteria-hypotheses.md` |
| W41 Rebriefing | ✅ draft v1 (4 open questions for Alain) | `W41_concept/rebriefing.md` |
| W41 Concept | ⚠️ draft v0 — revise after interviews | `W41_concept/concept.md` |
| W41 User survey | ❌ after interviews | `W41_concept/user-survey.md` |

## Run
```
pip install pandas plotly
cd solutions/W39_data   && python analysis.py     # numbers + charts in output/
cd solutions/W38_mapping && python mappings.py    # SVG sketches + index.html
```

## Top findings (latest wave 10 Sep 2026)
- **Two in three Americans are concerned** about AI (69 %), one in five excited (21 %) — stable since late June.
- **Two in three think AI is inevitable** (68 %), only 17 % think society can still shape it → "worried but powerless".
- **82 % already see people struggling to tell real from fake.** 75 % think AI makes job security worse.
- Worry is bipartisan; the **remedy is partisan** (Democrats want much more regulation).
- Most concerned: 65+, Democrats, women. Least: Black Americans, 35–49, men.
