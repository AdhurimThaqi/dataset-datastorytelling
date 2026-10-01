"""
Data Storytelling (I.BA_DAS) - dataset examples
------------------------------------------------
Each dataset runs through the same 4 steps you'll need for the project:

    1. INSPECT    - what's in the file? size, columns, missing values
    2. CLEAN      - fix types, drop/fill gaps, derive new columns
    3. FIND STORY - compute the few numbers that carry the message
    4. VISUALISE  - charts with headline titles (the title states the insight)

Run:
    python explore.py            -> all datasets + output/report.html
    python explore.py titanic    -> just one (gapminder | co2 | titanic | weather)

Every chart is also saved on its own in output/ (open in a browser,
use the camera icon to export a PNG for storyboards/animatics).
"""

import sys
from pathlib import Path

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

ROOT = Path(__file__).parent
DATA = ROOT / "data"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)

TEMPLATE = "plotly_white"


# ---------------------------------------------------------------- helpers
def header(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)


def inspect(df, name):
    """Step 1: the first thing you do with ANY dataset."""
    print(f"\n[1] INSPECT {name}")
    print(f"    rows x cols : {df.shape[0]:,} x {df.shape[1]}")
    print(f"    columns     : {', '.join(df.columns)}")
    missing = df.isna().sum()
    missing = missing[missing > 0]
    if len(missing):
        print("    missing values:")
        for col, n in missing.items():
            print(f"      {col:<28}{n:>7,}  ({n / len(df):.0%})")
    else:
        print("    missing values: none")
    print("\n    first rows:")
    print("    " + df.head(3).to_string().replace("\n", "\n    "))


def save(fig, filename):
    fig.update_layout(template=TEMPLATE, title_font_size=18)
    fig.write_html(OUT / filename, include_plotlyjs="directory")  # plotly.min.js saved once next to it -> works offline
    print(f"    -> saved output/{filename}")
    return fig


# ---------------------------------------------------------------- 1. Gapminder
def gapminder():
    header("GAPMINDER - health & wealth of nations, 1952-2007")
    df = pd.read_csv(DATA / "gapminder.csv")
    inspect(df, "gapminder.csv")

    print("\n[2] CLEAN")
    df["pop"] = df["pop"].astype(int)
    print("    population -> integer; data is already tidy (one row = country + year)")

    print("\n[3] FIND THE STORY")
    first, last = df[df.year == 1952], df[df.year == 2007]
    w1 = (first.lifeExp * first["pop"]).sum() / first["pop"].sum()
    w2 = (last.lifeExp * last["pop"]).sum() / last["pop"].sum()
    print(f"    world life expectancy (pop-weighted): {w1:.1f} -> {w2:.1f} years")
    gain = (last.set_index("country").lifeExp - first.set_index("country").lifeExp).sort_values()
    print(f"    biggest gain : {gain.index[-1]} (+{gain.iloc[-1]:.1f} yrs)")
    print(f"    smallest gain: {gain.index[0]} ({gain.iloc[0]:+.1f} yrs)")

    print("\n[4] VISUALISE")
    figs = []
    figs.append(save(px.scatter(
        df, x="gdpPercap", y="lifeExp", size="pop", color="continent",
        animation_frame="year", animation_group="country", hover_name="country",
        log_x=True, size_max=55, range_x=[200, 60000], range_y=[20, 90],
        labels={"gdpPercap": "GDP per capita (USD, log)", "lifeExp": "Life expectancy"},
        title="Press play: almost every country got richer AND healthier"),
        "gapminder_1_bubbles.html"))

    by_cont = (df.assign(w=df.lifeExp * df["pop"]).groupby(["continent", "year"])
               .agg(w=("w", "sum"), pop=("pop", "sum")).reset_index())
    by_cont["lifeExp"] = by_cont.w / by_cont["pop"]
    figs.append(save(px.line(
        by_cont, x="year", y="lifeExp", color="continent", markers=True,
        labels={"lifeExp": "Life expectancy (years)"},
        title=f"The gap is closing - but Africa still lags ~{by_cont[by_cont.year==2007].lifeExp.max()-by_cont[(by_cont.year==2007)&(by_cont.continent=='Africa')].lifeExp.iloc[0]:.0f} years behind"),
        "gapminder_2_continents.html"))
    return figs


# ---------------------------------------------------------------- 2. CO2
def co2():
    header("CO2 EMISSIONS - Our World in Data, 1950-today")
    df = pd.read_csv(DATA / "co2-emissions.csv")
    inspect(df, "co2-emissions.csv")

    print("\n[2] CLEAN")
    # rows without iso_code are aggregates (World, Europe, 'High-income countries'...)
    countries = df[df.iso_code.notna() & ~df.iso_code.str.startswith("OWID", na=False)]
    world = df[df.country == "World"]
    latest = int(countries.dropna(subset=["co2"]).year.max())
    print(f"    split real countries ({countries.country.nunique()}) from aggregates; latest year = {latest}")

    print("\n[3] FIND THE STORY")
    w0, w1 = world[world.year == 1950].co2.iloc[0], world[world.year == latest].co2.iloc[0]
    print(f"    world CO2: {w0:,.0f} -> {w1:,.0f} Mt  (x{w1 / w0:.1f})")
    ch = df[(df.country == "Switzerland")].set_index("year")
    yr = int(ch.consumption_co2_per_capita.dropna().index.max())
    t, c = ch.loc[yr, "co2_per_capita"], ch.loc[yr, "consumption_co2_per_capita"]
    print(f"    Switzerland {yr}: {t:.1f} t/person produced at home, "
          f"but {c:.1f} t/person consumed (+{c / t - 1:.0%} imported)")

    print("\n[4] VISUALISE")
    figs = []
    fuels = world.melt(id_vars="year", value_vars=["coal_co2", "oil_co2", "gas_co2", "cement_co2", "flaring_co2"],
                       var_name="source", value_name="Mt")
    fuels["source"] = fuels.source.str.replace("_co2", "").str.title()
    figs.append(save(px.area(
        fuels, x="year", y="Mt", color="source",
        labels={"Mt": "CO2 (million tonnes)"},
        title=f"World emissions grew {w1 / w0:.0f}x since 1950 - coal is still the biggest slice"),
        "co2_1_world_by_source.html"))

    # Same data, two stories: total vs per person (good ethics discussion!)
    snap = countries[countries.year == latest].dropna(subset=["co2", "co2_per_capita"])
    snap = snap[snap.population > 1_000_000]
    top_total = snap.nlargest(10, "co2")
    top_pc = snap.nlargest(10, "co2_per_capita")
    fig = go.Figure()
    fig.add_bar(x=top_total.country, y=top_total.co2, name="Total (Mt)")
    fig.add_bar(x=top_pc.country, y=top_pc.co2_per_capita, name="Per person (t)", visible=False)
    fig.update_layout(
        title=f"Same data, different story: who is the 'biggest emitter' depends on how you ask ({latest})",
        updatemenus=[dict(type="buttons", direction="right", x=0, y=1.12, buttons=[
            dict(label="Total", method="update", args=[{"visible": [True, False]}]),
            dict(label="Per person", method="update", args=[{"visible": [False, True]}]),
        ])])
    figs.append(save(fig, "co2_2_total_vs_per_person.html"))

    sw = ch.reset_index()[["year", "co2_per_capita", "consumption_co2_per_capita"]].dropna()
    sw = sw.rename(columns={"co2_per_capita": "Produced in Switzerland",
                            "consumption_co2_per_capita": "Consumed by Swiss (incl. imports)"})
    figs.append(save(px.line(
        sw, x="year", y=sw.columns[1:], markers=True,
        labels={"value": "t CO2 per person", "variable": ""},
        title="Switzerland looks clean - until you count what it imports"),
        "co2_3_switzerland.html"))
    return figs


# ---------------------------------------------------------------- 3. Titanic
def titanic():
    header("TITANIC - who survived? (891 passengers)")
    df = pd.read_csv(DATA / "titanic.csv")
    inspect(df, "titanic.csv")

    print("\n[2] CLEAN")
    df["Class"] = df.Pclass.map({1: "1st", 2: "2nd", 3: "3rd"})
    df["AgeGroup"] = pd.cut(df.Age, [0, 12, 18, 40, 60, 100],
                            labels=["Child", "Teen", "Adult", "Middle-aged", "Senior"])
    df["Outcome"] = df.Survived.map({1: "Survived", 0: "Died"})
    print("    added Class / AgeGroup / Outcome labels; 177 unknown ages stay NaN (not guessed)")

    print("\n[3] FIND THE STORY")
    print(f"    overall survival: {df.Survived.mean():.0%}")
    table = df.pivot_table(index="Sex", columns="Class", values="Survived", aggfunc="mean")
    print("    survival rate by sex x class:")
    print("    " + (table * 100).round(0).astype(int).astype(str).add("%").to_string().replace("\n", "\n    "))
    print("    -> branching idea: 'pick a passenger' and each choice (sex, class, age) changes the odds")

    print("\n[4] VISUALISE")
    figs = []
    rate = df.groupby(["Class", "Sex"]).Survived.mean().reset_index()
    rate["Survived"] *= 100
    figs.append(save(px.bar(
        rate, x="Class", y="Survived", color="Sex", barmode="group", text_auto=".0f",
        labels={"Survived": "Survival rate (%)"},
        title="'Women and children first' - but only if you had a 1st or 2nd class ticket"),
        "titanic_1_class_sex.html"))
    figs.append(save(px.histogram(
        df.dropna(subset=["Age"]), x="Age", color="Outcome", nbins=40, barmode="overlay",
        color_discrete_map={"Survived": "#2a9d8f", "Died": "#e76f51"},
        title="Children under 5 were the only age group more likely to survive than die"),
        "titanic_2_age.html"))
    figs.append(save(px.sunburst(
        df, path=["Class", "Sex", "Outcome"], color="Outcome",
        color_discrete_map={"Survived": "#2a9d8f", "Died": "#e76f51", "(?)": "#ccc"},
        title="Click to drill down: class -> sex -> fate (a ready-made branching structure)"),
        "titanic_3_branching.html"))
    return figs


# ---------------------------------------------------------------- 4. Weather
def weather():
    header("SEATTLE WEATHER - 4 years of daily data (2012-2015)")
    df = pd.read_csv(DATA / "seattle-weather.csv", parse_dates=["date"])
    inspect(df, "seattle-weather.csv")

    print("\n[2] CLEAN")
    df["month"] = df.date.dt.month_name().str[:3]
    df["temp_max_30d"] = df.temp_max.rolling(30, center=True).mean()
    print("    parsed dates, added month + 30-day rolling average (smooths daily noise)")

    print("\n[3] FIND THE STORY")
    rainy = (df.precipitation > 0).mean()
    print(f"    days with any precipitation: {rainy:.0%}")
    m = df.groupby("month", sort=False).precipitation.sum() / 4
    print(f"    wettest month: {m.idxmax()} ({m.max():.0f} mm/yr avg), driest: {m.idxmin()} ({m.min():.0f} mm)")

    print("\n[4] VISUALISE")
    figs = []
    fig = go.Figure()
    fig.add_scatter(x=df.date, y=df.temp_max, mode="lines", name="Daily max", line=dict(width=1, color="#f4a261"), opacity=0.5)
    fig.add_scatter(x=df.date, y=df.temp_max_30d, mode="lines", name="30-day average", line=dict(width=3, color="#e76f51"))
    fig.update_layout(title="Raw data is noisy - a rolling average reveals the seasons", yaxis_title="°C")
    figs.append(save(fig, "weather_1_temperature.html"))

    counts = df.groupby(["month", "weather"], sort=False).size().reset_index(name="days")
    figs.append(save(px.bar(
        counts, x="month", y="days", color="weather",
        title=f"Seattle's rainy reputation? It rains on {rainy:.0%} of days - mostly Nov to Apr"),
        "weather_2_by_month.html"))
    return figs


# ---------------------------------------------------------------- report
STORIES = {
    "gapminder": (gapminder, "Gapminder", "Classic Hans Rosling dataset. Good for an <b>animated</b> story: time is the narrative axis."),
    "co2": (co2, "CO2 emissions", "Our World in Data. Good for <b>ethics</b>: the same numbers tell opposite stories depending on framing (total vs per person, produced vs consumed)."),
    "titanic": (titanic, "Titanic", "Small and personal. Good for a <b>branching animatic</b>: every passenger attribute is a decision node."),
    "weather": (weather, "Seattle weather", "Daily time series. Good for practising <b>cleaning & smoothing</b> and seasonal patterns."),
}


def build_report(sections):
    parts = ["""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Data Story Examples</title>
<script src="plotly.min.js"></script>
<style>body{font-family:system-ui,sans-serif;max-width:1000px;margin:auto;padding:16px;color:#222;background:#fff}
h1{margin-bottom:0}h2{margin-top:56px;border-top:2px solid #eee;padding-top:24px}p.lead{color:#555}</style>
</head><body><h1>Data Story Examples</h1>
<p class="lead">I.BA_DAS practice - 4 real datasets, each charted with a headline title that states the insight.</p>"""]
    for title, blurb, figs in sections:
        parts.append(f"<h2>{title}</h2><p>{blurb}</p>")
        for f in figs:
            parts.append(f.to_html(full_html=False, include_plotlyjs=False))
    parts.append("</body></html>")
    (OUT / "report.html").write_text("\n".join(parts), encoding="utf-8")
    print(f"\nReport -> {OUT / 'report.html'}  (open in your browser)")


if __name__ == "__main__":
    pick = sys.argv[1:] or list(STORIES)
    unknown = [p for p in pick if p not in STORIES]
    if unknown:
        sys.exit(f"Unknown dataset {unknown}. Choose from: {', '.join(STORIES)}")
    sections = []
    for key in pick:
        fn, title, blurb = STORIES[key]
        sections.append((title, blurb, fn()))
    build_report(sections)
