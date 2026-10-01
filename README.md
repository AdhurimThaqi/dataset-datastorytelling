# Data Storytelling – dataset examples

Four **real, public** datasets to practise the DAS workflow:
inspect → clean → find the story → visualise.

**Live report:** https://adhurimthaqi.github.io/dataset-datastorytelling/

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

## Where to find a dataset for the real project
- [opendata.swiss](https://opendata.swiss) – Swiss federal/cantonal open data
- [Our World in Data](https://ourworldindata.org) – every chart has a downloadable CSV
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [data.stadt-zuerich.ch](https://data.stadt-zuerich.ch) – City of Zurich
- [BFS / Swiss Federal Statistical Office](https://www.bfs.admin.ch)

## Course exercises & project
All exercise material, the real project dataset ("Americans on AI") and templates for the milestones are in [`exercises/`](exercises/README.md).
