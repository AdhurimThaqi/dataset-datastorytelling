"""
W39 solution - Americans on AI: answers to the exploration questions.
Run from this folder:  python analysis.py   (needs pandas, plotly)
Reads ../../exercises/W39_data/survey_all_waves_all_subgroups.csv, prints numbers, writes charts to output/.
"""
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

ROOT = Path(__file__).parent
DATA = ROOT.parent.parent / "exercises" / "W39_data" / "survey_all_waves_all_subgroups.csv"
OUT = ROOT / "output"; OUT.mkdir(exist_ok=True)
PILOT = "2026-06-12"

df = pd.read_csv(DATA, encoding="utf-8-sig")
norc = df[df.Wave != PILOT]                      # comparable waves only
LAST = df.Wave.max()

POS = {"ai_sentiment": ["very_excited", "somewhat_excited"],
       "ai_agency": ["can_shape"],
       "ai_community_impact": ["have_seen", "starting"],
       "ai_family_impact": ["much_better", "somewhat_better"],
       "ai_regulation": ["somewhat_too_little", "way_too_little"],
       "ai_risks": ["already", "likely"]}
NEG = {"ai_sentiment": ["very_concerned", "somewhat_concerned"],
       "ai_agency": ["inevitable"],
       "ai_community_impact": ["dont_expect"],
       "ai_family_impact": ["much_worse", "somewhat_worse"],
       "ai_regulation": ["somewhat_too_much", "way_too_much"],
       "ai_risks": ["unlikely", "not_at_all_likely"]}
LABEL = {"ai_sentiment": ("Excited", "Concerned"), "ai_agency": ("Can shape", "Inevitable"),
         "ai_community_impact": ("Seen / starting", "Don't expect"), "ai_family_impact": ("Better", "Worse"),
         "ai_regulation": ("Gov. does too little", "Gov. does too much"), "ai_risks": ("Already / likely", "Unlikely")}

def nets(d):
    rows = []
    for (q, sg, w, dim), g in d.groupby(["Question_ID", "Subgroup", "Wave", "Dimension"]):
        p = g[g.Answer.isin(POS[q])].Percentage.sum(); n = g[g.Answer.isin(NEG[q])].Percentage.sum()
        miss = g[g.Answer.isin(["not_sure", "no_answer", "none", "neither", "no_effect"])].Percentage.sum()
        rows.append(dict(q=q, sg=sg, wave=w, dim=dim, pos=p, neg=n, other=miss))
    return pd.DataFrame(rows)

N = nets(df)
short = lambda s: s if len(s) < 70 else s[:67] + "..."

print("=== Q1 Has the mood changed over time? (total, ai_sentiment) ===")
t = N[(N.q == "ai_sentiment") & (N.sg == "total")].set_index("wave")[["pos", "neg", "other"]].round(1)
t.columns = ["excited", "concerned", "none/no answer"]; print(t.to_string())
nn = t.drop(PILOT)
print(f"NORC waves only: concerned {nn.concerned.min()}-{nn.concerned.max()} %, excited {nn.excited.min()}-{nn.excited.max()} %")

print(f"\n=== Q2 Who is most / least concerned? (ai_sentiment, mean of NORC waves) ===")
g = N[(N.q == "ai_sentiment") & (N.wave != PILOT)].groupby("sg")[["pos", "neg"]].mean().round(1)
g.columns = ["excited", "concerned"]; g["gap"] = (g.concerned - g.excited).round(1)
print(g.sort_values("concerned", ascending=False).to_string())

print(f"\n=== Q3 All questions, total population, latest wave {LAST} ===")
lt = N[(N.sg == "total") & (N.wave == LAST)].copy()
for _, r in lt.iterrows():
    a, b = LABEL[r.q]
    print(f"{r.q:<20} {short(r.dim):<72} {a}: {r.pos:5.1f}  {b}: {r.neg:5.1f}  other: {r.other:5.1f}")

print(f"\n=== Q4 Biggest party gaps (Dem - Rep, 'positive' side, mean of NORC waves) ===")
p = N[(N.wave != PILOT) & N.sg.isin(["party_dem", "party_rep"])].groupby(["q", "dim", "sg"]).pos.mean().unstack()
p["gap"] = (p.party_dem - p.party_rep).round(1)
for (q, dim), r in p.reindex(p.gap.abs().sort_values(ascending=False).index).head(8).iterrows():
    print(f"{q:<20} {short(dim):<72} Dem {r.party_dem:5.1f}  Rep {r.party_rep:5.1f}  gap {r.gap:+5.1f}")

print(f"\n=== Q5 Young vs old (18-34 vs 65+, 'positive' side, mean of NORC waves) ===")
a = N[(N.wave != PILOT) & N.sg.isin(["age_18_34", "age_65_plus"])].groupby(["q", "dim", "sg"]).pos.mean().unstack()
a["gap"] = (a.age_18_34 - a.age_65_plus).round(1)
for (q, dim), r in a.reindex(a.gap.abs().sort_values(ascending=False).index).head(6).iterrows():
    print(f"{q:<20} {short(dim):<72} 18-34 {r.age_18_34:5.1f}  65+ {r.age_65_plus:5.1f}  gap {r.gap:+5.1f}")

print("\n=== Q6 How big is 'don't know'? (share not_sure + no_answer, total, latest wave) ===")
u = df[(df.Subgroup == "total") & (df.Wave == LAST) & df.Answer.isin(["not_sure", "no_answer"])]
print(u.groupby(["Question_ID", "Dimension"]).Percentage.sum().round(1).sort_values(ascending=False).head(6).to_string())

# ---------------- charts ----------------
c = N[(N.q == "ai_sentiment") & (N.sg == "total")].melt(id_vars="wave", value_vars=["pos", "neg"], var_name="side", value_name="pct")
c["side"] = c.side.map({"pos": "Excited", "neg": "Concerned"})
fig = px.line(c, x="wave", y="pct", color="side", markers=True, range_y=[0, 100],
              labels={"pct": "% of U.S. adults", "wave": ""},
              title="Two in three Americans are concerned about AI - and that has barely moved since June")
fig.add_vrect(x0=-0.5, x1=0.5, fillcolor="grey", opacity=0.15, line_width=0, annotation_text="pilot, other method")
fig.write_html(OUT / "1_sentiment_trend.html", include_plotlyjs="cdn")

order = g.sort_values("concerned").index.tolist()
fig = go.Figure()
for col, name in [("concerned", "Concerned"), ("excited", "Excited")]:
    fig.add_scatter(x=g.loc[order, col], y=order, mode="markers", name=name, marker_size=12)
fig.update_layout(title="Every group is more concerned than excited - Democrats, women and over-50s most of all",
                  xaxis_title="% (mean of NORC waves)", xaxis_range=[0, 100])
fig.write_html(OUT / "2_sentiment_by_group.html", include_plotlyjs="cdn")

fig = px.bar(lt.assign(dim=lt.dim.map(short)).sort_values("pos"), x="pos", y="dim", color="q", orientation="h",
             labels={"pos": "% 'positive' side (see LABEL in script)", "dim": ""},
             title=f"All 20 items at a glance ({LAST}, total population)")
fig.write_html(OUT / "3_all_items.html", include_plotlyjs="cdn")
print(f"\ncharts -> {OUT}")
