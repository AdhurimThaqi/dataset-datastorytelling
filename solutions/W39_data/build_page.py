"""
Builds ../../ai.html (repo root, served by GitHub Pages) from the real survey data.
Run from this folder:  python build_page.py
"""
import json
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).parent
REPO = ROOT.parent.parent
df = pd.read_csv(REPO / "exercises/W39_data/survey_all_waves_all_subgroups.csv", encoding="utf-8-sig")
PILOT, LAST = "2026-06-12", df.Wave.max()
norc = df[df.Wave != PILOT]
WAVE_LABEL = {"2026-06-12": "12 Jun (pilot)", "2026-06-25": "25 Jun", "2026-07-09": "9 Jul", "2026-07-23": "23 Jul",
              "2026-08-13": "13 Aug", "2026-08-27": "27 Aug", "2026-09-10": "10 Sep"}
GROUP = {"total": "All adults", "gender_men": "Men", "gender_women": "Women", "party_dem": "Democrats", "party_rep": "Republicans",
         "age_18_34": "Age 18–34", "age_35_49": "Age 35–49", "age_50_64": "Age 50–64", "age_65_plus": "Age 65+",
         "race_white_nh": "White", "race_black_nh": "Black", "race_hispanic": "Hispanic"}

def share(d, q, answers, dim=None):
    d = d[d.Question_ID == q]
    if dim: d = d[d.Dimension == dim]
    return d[d.Answer.isin(answers)].groupby(["Subgroup", "Wave"]).Percentage.sum()

EXC, CON = ["very_excited", "somewhat_excited"], ["very_concerned", "somewhat_concerned"]
exc, con = share(df, "ai_sentiment", EXC), share(df, "ai_sentiment", CON)
trend = [{"wave": WAVE_LABEL[w], "pilot": w == PILOT, "excited": round(exc["total", w], 1), "concerned": round(con["total", w], 1)}
         for w in sorted(df.Wave.unique())]
waves_norc = sorted(norc.Wave.unique())
groups = [{"id": g, "name": GROUP[g],
           "concerned": round(sum(con[g, w] for w in waves_norc) / len(waves_norc), 1),
           "excited": round(sum(exc[g, w] for w in waves_norc) / len(waves_norc), 1)} for g in GROUP]
groups.sort(key=lambda r: r["concerned"])

def items(q, answers, label_map=None):
    d = df[(df.Question_ID == q) & (df.Subgroup == "total") & (df.Wave == LAST)]
    out = [{"item": (label_map or {}).get(dim, dim), "pct": round(g[g.Answer.isin(answers)].Percentage.sum(), 1)}
           for dim, g in d.groupby("Dimension")]
    return sorted(out, key=lambda r: r["pct"])

small = [
  {"title": "Already seeing it in their community", "unit": "% have seen it or see it starting",
   "rows": items("ai_community_impact", ["have_seen", "starting"],
                 {"People are struggling to tell what's real from what's fake": "Can't tell real from fake", "People are losing connections to others": "Losing connections",
                  "People are pressured to do more, faster": "Pressure to do more, faster", "People are saving time on everyday tasks": "Saving time",
                  "People are getting better health care": "Better health care"})},
  {"title": "AI is making this worse for families", "unit": "% somewhat or much worse",
   "rows": items("ai_family_impact", ["somewhat_worse", "much_worse"])},
  {"title": "Likely within 20 years", "unit": "% already happening or likely",
   "rows": items("ai_risks", ["already", "likely"],
                 {"AI systems behaving in ways their developers did not intend": "AI acts in unintended ways", "AI becoming smarter than humans at most tasks": "Smarter than humans",
                  "AI being used to create weapons of mass destruction": "Weapons of mass destruction", "AI making major scientific and medical breakthroughs": "Medical / science breakthroughs"})},
  {"title": "Government is doing too little about…", "unit": "% too little",
   "rows": items("ai_regulation", ["somewhat_too_little", "way_too_little"],
                 {"AI's effects on children and young people": "Effects on children", "AI's environmental footprint, including from data centers": "Environment / data centres",
                  "AI's effects on workers and jobs": "Workers and jobs", "AI's effect on American competitiveness": "US competitiveness"})},
]
reg = df[(df.Question_ID == "ai_regulation") & df.Subgroup.isin(["party_dem", "party_rep"]) & (df.Wave != PILOT)
         & df.Answer.isin(["somewhat_too_little", "way_too_little"])]
reg = reg.groupby(["Dimension", "Subgroup", "Wave"]).Percentage.sum().groupby(["Dimension", "Subgroup"]).mean().unstack().round(1)
short = {"AI's effects on children and young people": "Effects on children", "AI's environmental footprint, including from data centers": "Environment / data centres",
         "AI's effects on workers and jobs": "Workers and jobs", "AI's effect on American competitiveness": "US competitiveness"}
party = [{"item": short[k], "dem": r.party_dem, "rep": r.party_rep} for k, r in reg.sort_values("party_dem").iterrows()]

last = df[(df.Subgroup == "total") & (df.Wave == LAST)]
hero = {
  "concerned": round(con["total", LAST]),
  "inevitable": round(last[(last.Question_ID == "ai_agency") & (last.Answer == "inevitable")].Percentage.sum()),
  "fake": round(last[(last.Question_ID == "ai_community_impact") & last.Dimension.str.contains("real from what") & last.Answer.isin(["have_seen", "starting"])].Percentage.sum()),
}
data = dict(trend=trend, groups=groups, small=small, party=party, hero=hero, last=WAVE_LABEL[LAST])
tpl = (ROOT / "ai_template.html").read_text(encoding="utf-8")
(REPO / "ai.html").write_text(tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False)), encoding="utf-8")
print("wrote", REPO / "ai.html", "| hero:", hero)
