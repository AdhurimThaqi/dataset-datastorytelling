"""The data cut for all three W43 directions, read straight from the official CSV.

Run it to print every number the wireframes and the AI draft use:  python data_cut.py
Rules (rebriefing R12/R13):
- pilot wave 2026-06-12 (Prolific, other method) is excluded
- latest NORC wave only, unless a function says otherwise
- "none" / "neither" / "not sure" / "no answer" are kept as their own band
- a missing row in the CSV means the answer was not reported -> 0.0, flagged in `missing`
- subgroup gaps smaller than the estimated margin of error are marked "not a real gap"
"""
import csv
import json
import math
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE.parent / "W39_data"
CSV = DATA / "survey_all_waves_all_subgroups.csv"
JSON = DATA / "data.json"

PILOT = "2026-06-12"
AGES = ["age_18_34", "age_35_49", "age_50_64", "age_65_plus"]
AGE_LABEL = {"age_18_34": "18–34", "age_35_49": "35–49", "age_50_64": "50–64", "age_65_plus": "65+"}
FAKE = "People are struggling to tell what's real from what's fake"

SENTIMENT = ["very_excited", "somewhat_excited", "somewhat_concerned", "very_concerned", "none", "no_answer"]
AGENCY = ["can_shape", "inevitable", "neither", "no_answer"]
COMMUNITY = ["have_seen", "starting", "expect_soon", "dont_expect", "not_sure", "no_answer"]

missing = []


def _load():
    table = {}
    with open(CSV, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            key = (r["Subgroup"], r["Wave"], r["Question_ID"], r["Dimension"])
            table.setdefault(key, {})[r["Answer"]] = float(r["Percentage"])
    return table


TABLE = _load()
WAVES = sorted({k[1] for k in TABLE})
NORC_WAVES = [w for w in WAVES if w != PILOT]
LATEST = NORC_WAVES[-1]

_meta = json.loads(JSON.read_text(encoding="utf-8"))
_wave = {w["wave_id"]: w for w in _meta["waves"]}
N_TOTAL = _wave[LATEST]["sample"]["n"]
MOE_TOTAL = _wave[LATEST]["sample"]["margin_of_error"]
N_SUB = {s["id"]: s["n_unweighted"] for s in _wave[LATEST]["subgroups"]}
N_SUB["total"] = N_TOTAL


def dist(question, subgroup="total", wave=LATEST, dimension=None):
    """Answer -> percentage, in the order of the answer scale."""
    order = {"ai_sentiment": SENTIMENT, "ai_agency": AGENCY}.get(question, COMMUNITY)
    for (s, w, q, d), answers in TABLE.items():
        if s == subgroup and w == wave and q == question and (dimension is None or d == dimension):
            out = {}
            for a in order:
                if a not in answers:
                    missing.append(f"{subgroup}/{wave}/{question}/{a}")
                out[a] = answers.get(a, 0.0)
            return out
    raise KeyError((question, subgroup, wave, dimension))


def sentiment(subgroup="total", wave=LATEST):
    d = dist("ai_sentiment", subgroup, wave)
    return {"excited": d["very_excited"] + d["somewhat_excited"],
            "concerned": d["somewhat_concerned"] + d["very_concerned"],
            "none": d["none"], "no_answer": d["no_answer"], "detail": d}


def agency(subgroup="total", wave=LATEST):
    return dist("ai_agency", subgroup, wave)


def fake(subgroup="total", wave=LATEST):
    d = dist("ai_community_impact", subgroup, wave, FAKE)
    return {"seen": d["have_seen"] + d["starting"], "detail": d}


def moe(subgroup):
    """Estimated margin of error (pts, 95 %) for one subgroup.

    Assumption: the subgroup has the same design effect as the full sample,
    so MoE scales with sqrt(n_total / n_subgroup). Conservative (p = 0.5).
    """
    return MOE_TOTAL * math.sqrt(N_TOTAL / N_SUB[subgroup])


def gap_is_real(a_sub, a_val, b_sub, b_val):
    """A gap counts only if it is bigger than the combined margin of error."""
    limit = math.hypot(moe(a_sub), moe(b_sub))
    return abs(a_val - b_val) > limit, limit


def in_1000(pct):
    """Percentage -> dots out of 1,000 (one dot ~ one in a thousand US adults)."""
    return round(pct * 10)


def words(pct):
    """Rounded wording for text that must survive new waves (R13)."""
    for frac, txt in [(0.8, "4 in 5"), (2 / 3, "2 in 3"), (0.6, "3 in 5"), (0.5, "1 in 2"),
                      (0.25, "1 in 4"), (0.2, "1 in 5"), (1 / 6, "1 in 6"), (0.1, "1 in 10")]:
        if abs(pct / 100 - frac) <= 0.035:
            return "about " + txt
    return f"about {round(pct)} in 100"


def wave_label(wave=LATEST):
    f = _wave[wave]["field_dates"]
    return f"US adults, {f['start']} to {f['end']}, n = {_wave[wave]['sample']['n']:,}"


if __name__ == "__main__":
    print(f"Latest NORC wave: {LATEST}  (n = {N_TOTAL}, MoE ±{MOE_TOTAL} pts)  pilot {PILOT} excluded")
    print(f"NORC waves: {', '.join(NORC_WAVES)}\n")
    print(f"{'subgroup':14} {'n':>5} {'MoE':>5} | {'excit':>6} {'conc':>6} {'none':>5} {'n/a':>5} | "
          f"{'shape':>6} {'inev':>6} {'neith':>6} {'n/a':>5} | {'fake':>6}")
    for s in ["total"] + AGES + ["gender_women", "gender_men", "party_dem", "party_rep",
                                 "race_white_nh", "race_black_nh", "race_hispanic"]:
        se, ag, fk = sentiment(s), agency(s), fake(s)
        print(f"{s:14} {N_SUB[s]:5} {moe(s):5.1f} | {se['excited']:6.2f} {se['concerned']:6.2f} {se['none']:5.2f} "
              f"{se['no_answer']:5.2f} | {ag['can_shape']:6.2f} {ag['inevitable']:6.2f} {ag['neither']:6.2f} "
              f"{ag['no_answer']:5.2f} | {fk['seen']:6.2f}")

    print("\nAge gaps (18–34 vs 65+), latest wave:")
    for name, a, b in [("concerned", sentiment("age_18_34")["concerned"], sentiment("age_65_plus")["concerned"]),
                       ("can shape", agency("age_18_34")["can_shape"], agency("age_65_plus")["can_shape"]),
                       ("fake seen", fake("age_18_34")["seen"], fake("age_65_plus")["seen"])]:
        real, lim = gap_is_real("age_18_34", a, "age_65_plus", b)
        print(f"  {name:10} {a:6.2f} vs {b:6.2f}  gap {a - b:+6.2f}  limit ±{lim:4.1f}  -> {'REAL' if real else 'not a real gap'}")

    print("\n'Can shape' 18–34 vs 65+ in every NORC wave:")
    for w in NORC_WAVES:
        a, b = agency("age_18_34", w)["can_shape"], agency("age_65_plus", w)["can_shape"]
        print(f"  {w}  {a:6.2f} vs {b:6.2f}  gap {a - b:+6.2f}")

    print("\nTotal over NORC waves (concerned / inevitable):")
    for w in NORC_WAVES:
        print(f"  {w}  {sentiment('total', w)['concerned']:6.2f}  {agency('total', w)['inevitable']:6.2f}")

    se, ag = sentiment(), agency()
    overlap = se["concerned"] + ag["inevitable"] - 100
    print(f"\nNo crosstab in the data: concerned AND inevitable is at least {overlap:.2f} % of all adults "
          f"(= {overlap / se['concerned'] * 100:.1f} % of the concerned), lower bound only.")
    if missing:
        print("\nNot reported in the CSV (treated as 0.0):", ", ".join(sorted(set(missing))))
