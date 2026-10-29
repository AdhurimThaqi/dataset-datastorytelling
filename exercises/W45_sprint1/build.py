"""Build v5.html (all six steps of direction A) from template.html + the official CSV.

Run:  python build.py
Every number on the page comes from here: data_cut.py reads the CSV, this script puts the numbers
into the page as JSON. The page itself holds no hand-typed percentage (check.py tests that).
New survey wave → run it again.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent / "W43_prototyping"))
import data_cut as D  # noqa: E402

GROUPS = ["total"] + D.AGES
LABEL = {"total": "All US adults", **{g: D.AGE_LABEL[g] for g in D.AGES}}

meta = json.loads(D.JSON.read_text(encoding="utf-8"))
QUESTIONS = {q["id"]: q for q in meta["questions"]}


def labels(qid):
    """Answer code -> official answer label, from data.json."""
    return {c["code"]: c["label"] for c in QUESTIONS[qid]["response_space"]["codes"]}


def per_100(dist):
    """Largest-remainder rounding, so the 100 dots always add up to exactly 100."""
    base = {k: int(v) for k, v in dist.items()}
    left = 100 - sum(base.values())
    for k in sorted(dist, key=lambda k: dist[k] - int(dist[k]), reverse=True)[:max(0, left)]:
        base[k] += 1
    return base


def date_label(wave):
    f = D._wave[wave]["field_dates"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    s, e = f["start"].split("-"), f["end"].split("-")
    return f"{int(s[2])}–{int(e[2])} {months[int(e[1]) - 1]} {e[0]}"


def full_question(qid, item=None):
    import csv
    with open(D.CSV, encoding="utf-8-sig", newline="") as fh:
        for r in csv.DictReader(fh):
            if r["Wave"] == D.LATEST and r["Question_ID"] == qid and (item is None or r["Dimension"] == item):
                return r["Full_Question"]
    raise KeyError(qid)


fake = D.fake()["detail"]
a18, a65 = D.agency("age_18_34")["can_shape"], D.agency("age_65_plus")["can_shape"]
data = {
    "wave": D.LATEST,
    "dates": date_label(D.LATEST),
    "n": D.N_TOTAL,
    "moe": D.MOE_TOTAL,
    "q": {
        "fake": full_question("ai_community_impact", D.FAKE),
        "sentiment": full_question("ai_sentiment"),
        "agency": full_question("ai_agency"),
    },
    "labels": {"sentiment": labels("ai_sentiment"), "agency": labels("ai_agency")},
    "hook": {"raw": fake, "dots": per_100(fake)},
    "groups": {g: {"label": LABEL[g], "n": D.N_SUB[g], "moe": round(D.moe(g), 1),
                   "sentiment": D.dist("ai_sentiment", g), "agency": D.agency(g)} for g in GROUPS},
    # gap rule (rebriefing R12): a gap is only called a gap if it beats the combined margin of error
    "shapeGapReal": D.gap_is_real("age_18_34", a18, "age_65_plus", a65)[0],
    "shapeGap1835": D.gap_is_real("age_18_34", a18, "age_35_49", D.agency("age_35_49")["can_shape"])[0],
    "words": {"inevitable": D.words(D.agency()["inevitable"]), "concerned": D.words(D.sentiment()["concerned"])},
}

html = (HERE / "template.html").read_text(encoding="utf-8")
out = html.replace("__DATA__", json.dumps(data, ensure_ascii=False))
(HERE / "v5.html").write_text(out, encoding="utf-8")
print("wrote", HERE / "v5.html")
if D.missing:
    print("not reported in the CSV, shown as 0:", ", ".join(sorted(set(D.missing))))
