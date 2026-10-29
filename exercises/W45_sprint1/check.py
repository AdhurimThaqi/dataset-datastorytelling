"""Check every number in v5.html against the official CSV (sprint 1, task 2).

Run:  python check.py      → prints each check and "0 mismatches", or the mismatches.
It reads the CSV directly with the csv module (not through data_cut.py), so a bug in the build can't hide itself.
"""
import csv
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).parent
CSV = HERE.parent / "W39_data" / "survey_all_waves_all_subgroups.csv"
META = HERE.parent / "W39_data" / "data.json"
WAVE = "2026-09-10"
FAKE = "People are struggling to tell what's real from what's fake"
sys.stdout.reconfigure(encoding="utf-8")

page = (HERE / "v5.html").read_text(encoding="utf-8")
template = (HERE / "template.html").read_text(encoding="utf-8")
D = json.loads(re.search(r"const D = (\{.*?\});\n", page).group(1))

csv_val = {}
with open(CSV, encoding="utf-8-sig", newline="") as fh:
    for r in csv.DictReader(fh):
        if r["Wave"] == WAVE:
            item = r["Dimension"] if r["Question_ID"] == "ai_community_impact" else ""
            csv_val[(r["Subgroup"], r["Question_ID"], item, r["Answer"])] = float(r["Percentage"])

bad, checked = [], 0


def same(what, page_value, source_value):
    global checked
    checked += 1
    if abs(page_value - source_value) > 1e-9:
        bad.append(f"{what}: page {page_value} vs source {source_value}")


# 1 · every percentage on the page = the CSV (a row missing in the CSV must be 0 on the page)
for code, v in D["hook"]["raw"].items():
    same(f"hook/{code}", v, csv_val.get(("total", "ai_community_impact", FAKE, code), 0.0))
for g, grp in D["groups"].items():
    for code, v in grp["sentiment"].items():
        same(f"{g}/sentiment/{code}", v, csv_val.get((g, "ai_sentiment", "", code), 0.0))
    for code, v in grp["agency"].items():
        same(f"{g}/agency/{code}", v, csv_val.get((g, "ai_agency", "", code), 0.0))

# 2 · the 100 hook dots add up to 100 and each is its percentage rounded to whole people
dots = D["hook"]["dots"]
checked += 1
if sum(dots.values()) != 100:
    bad.append(f"hook dots add up to {sum(dots.values())}, not 100")
for code, k in dots.items():
    checked += 1
    if abs(k - D["hook"]["raw"][code]) >= 1:
        bad.append(f"hook dot {code}: {k} dots for {D['hook']['raw'][code]} %")

# 3 · sample size, margin of error and dates = data.json
meta = json.loads(META.read_text(encoding="utf-8"))
wave = next(w for w in meta["waves"] if w["wave_id"] == WAVE)
same("n", D["n"], wave["sample"]["n"])
same("margin of error", D["moe"], wave["sample"]["margin_of_error"])
for g in D["groups"]:
    if g != "total":
        same(f"{g}/n", D["groups"][g]["n"], next(s["n_unweighted"] for s in wave["subgroups"] if s["id"] == g))

# 4 · the gap rule the closing sentence depends on (18–34 vs 65+ "can shape")
G = D["groups"]
limit = (G["age_18_34"]["moe"] ** 2 + G["age_65_plus"]["moe"] ** 2) ** 0.5
gap = G["age_18_34"]["agency"]["can_shape"] - G["age_65_plus"]["agency"]["can_shape"]
checked += 1
if (abs(gap) > limit) != D["shapeGapReal"]:
    bad.append(f"shapeGapReal is {D['shapeGapReal']} but the gap is {gap:.2f} vs limit {limit:.2f}")

# 5 · no hand-typed survey number in the template (only __DATA__ may bring numbers in)
body = re.sub(r"<style>.*?</style>", "", template, flags=re.S)          # CSS sizes aren't survey numbers
found = lambda s: re.search(rf"(?<![\d.]){re.escape(s)}(?![\d])", body)  # whole numbers only (not 29.10.2026)
typed = sorted({s for v in csv_val.values() for s in (f"{v:.2f}", f"{v:.1f} %") if found(s)})
checked += 1
if typed:
    bad.append("survey numbers typed into template.html: " + ", ".join(typed))

print(f"{checked} checks · wave {WAVE} · {CSV.name}")
print("\n".join(bad) if bad else "0 mismatches")
sys.exit(1 if bad else 0)
