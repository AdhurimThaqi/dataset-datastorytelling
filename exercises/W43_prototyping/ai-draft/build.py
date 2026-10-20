"""Build index.html (AI draft of direction A) from template.html + the official CSV.

Run:  python build.py
The numbers are injected as JSON, so the page never holds a hand-typed percentage.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE.parent))
import data_cut as D  # noqa: E402

SUBS = ["total"] + D.AGES + ["gender_women", "gender_men", "party_dem", "party_rep",
                             "race_white_nh", "race_black_nh", "race_hispanic"]
LABEL = {"total": "All US adults", **{g: D.AGE_LABEL[g] for g in D.AGES},
         "gender_women": "Women", "gender_men": "Men", "party_dem": "Democrats", "party_rep": "Republicans",
         "race_white_nh": "White, non-Hispanic", "race_black_nh": "Black, non-Hispanic", "race_hispanic": "Hispanic"}

data = {
    "wave": D.LATEST,
    "waveLabel": D.wave_label(),
    "sentimentQ": "Thinking about AI's growing role in society, which of these options comes closest to how you feel, "
                  "even if none are exactly right?",
    "agencyQ": "Again, thinking about AI, which statement comes closer to your view, even if neither is exactly right?",
    "fakeItem": D.FAKE,
    "groups": {s: {"label": LABEL[s], "n": D.N_SUB[s], "moe": round(D.moe(s), 1),
                   "sentiment": D.dist("ai_sentiment", s),
                   "agency": D.agency(s),
                   "fake": D.fake(s)["detail"]} for s in SUBS},
}
# gap rule for the page text: only call a gap real if it beats the combined margin of error
a18, a65 = D.agency("age_18_34")["can_shape"], D.agency("age_65_plus")["can_shape"]
data["shapeGapReal"] = D.gap_is_real("age_18_34", a18, "age_65_plus", a65)[0]
data["shapeGap1835"] = D.gap_is_real("age_18_34", a18, "age_35_49", D.agency("age_35_49")["can_shape"])[0]
data["fakeWords"] = D.words(D.fake()["seen"])
data["concWords"] = D.words(D.sentiment()["concerned"])
data["inevWords"] = D.words(D.agency()["inevitable"])

html = (HERE / "template.html").read_text(encoding="utf-8")
out = html.replace("__DATA__", json.dumps(data, ensure_ascii=False))
(HERE / "index.html").write_text(out, encoding="utf-8")
print("wrote", HERE / "index.html")
if D.missing:
    print("not reported in the CSV, shown as 0:", ", ".join(sorted(set(D.missing))))
