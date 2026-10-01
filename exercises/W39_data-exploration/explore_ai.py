"""
Americans on AI — quick exploration (I.BA_DAS, W39)
Run:  pip install pandas plotly   then   python explore_ai.py
Prints the key numbers and writes charts to output/.
"""
from pathlib import Path
import pandas as pd
import plotly.express as px

ROOT = Path(__file__).parent
DATA = ROOT / "data" / "americans-on-ai" / "1_master" / "survey_all_waves_all_subgroups.csv"
OUT = ROOT / "output"
OUT.mkdir(exist_ok=True)
PILOT = "2026-06-12"  # Prolific pilot, different method than later NORC waves

df = pd.read_csv(DATA, encoding="utf-8-sig")
print(f"rows x cols: {df.shape[0]:,} x {df.shape[1]}")
print("waves     :", ", ".join(sorted(df.Wave.unique())))
print("subgroups :", ", ".join(sorted(df.Subgroup.unique())))
print("questions :", ", ".join(sorted(df.Question_ID.unique())))

# --- sentiment: excited vs concerned -------------------------------------------
s = df[df.Question_ID == "ai_sentiment"].copy()
s["side"] = s.Answer.map({"very_excited": "Excited", "somewhat_excited": "Excited",
                          "somewhat_concerned": "Concerned", "very_concerned": "Concerned"}).fillna("Other / no answer")
net = s.groupby(["Subgroup", "Wave", "side"]).Percentage.sum().reset_index()

trend = net[net.Subgroup == "total"].pivot(index="Wave", columns="side", values="Percentage").round(1)
print("\nTotal population, % per wave (first wave = pilot, different method!):")
print(trend.to_string())

last = net.Wave.max()
snap = net[(net.Wave == last) & (net.side != "Other / no answer")]
print(f"\nLatest wave {last}, % concerned vs excited by subgroup:")
print(snap.pivot(index="Subgroup", columns="side", values="Percentage").round(1)
      .sort_values("Concerned", ascending=False).to_string())

# --- charts --------------------------------------------------------------------
t = net[(net.Subgroup == "total") & (net.side != "Other / no answer")]
fig = px.line(t, x="Wave", y="Percentage", color="side", markers=True,
              title="Concern clearly outweighs excitement (first point = pilot, different method)")
fig.add_vline(x=0.5, line_dash="dot")
fig.write_html(OUT / "ai_1_sentiment_trend.html", include_plotlyjs="cdn")

fig = px.bar(snap, y="Subgroup", x="Percentage", color="side", barmode="group", orientation="h",
             title=f"Who worries most about AI? ({last})")
fig.write_html(OUT / "ai_2_sentiment_by_group.html", include_plotlyjs="cdn")
print(f"\ncharts -> {OUT}")
