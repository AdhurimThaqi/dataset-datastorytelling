"""
W38 solution - six mappings of the same dataset (01_Coffee-Week.csv).
Run:  python mappings.py   -> sketches/*.svg + index.html (open in a browser). No extra packages needed.
"""
import csv, math, html
from pathlib import Path

ROOT = Path(__file__).parent
SRC = ROOT.parent.parent / "exercises" / "W38_mapping" / "data" / "01_Coffee-Week.csv"
OUT = ROOT / "sketches"; OUT.mkdir(exist_ok=True)
rows = list(csv.DictReader(open(SRC, encoding="utf-8")))
DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for r in rows:
    h, m = map(int, r["Time"].split(":")); r["t"] = h + m / 60
    r["vol"] = int(r["Volume_ml"]); r["joy"] = int(r["Enjoyment_1_5"]); r["d"] = DAYS.index(r["Day"])
PLACES = sorted({r["Place"] for r in rows}); TYPES = sorted({r["Type"] for r in rows}); REASONS = sorted({r["Reason"] for r in rows})
PAL = ["#4e79a7", "#f28e2b", "#59a14f", "#e15759", "#b07aa1", "#76b7b2"]
pcol = {p: PAL[i] for i, p in enumerate(PLACES)}; tcol = {t: PAL[i] for i, t in enumerate(TYPES)}
W, H = 640, 420

def svg(name, title, body, legend=""):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica,Arial,sans-serif" font-size="11">'
         f'<rect width="{W}" height="{H}" fill="#fffdf8"/><text x="16" y="24" font-size="14" font-weight="bold">{html.escape(title)}</text>{body}{legend}</svg>')
    (OUT / f"{name}.svg").write_text(s, encoding="utf-8"); return name

def legend(items, x=16, y=H - 18, shape="circle"):
    out, cx = "", x
    for label, col in items:
        out += (f'<circle cx="{cx+5}" cy="{y-4}" r="5" fill="{col}"/>' if shape == "circle" else f'<rect x="{cx}" y="{y-9}" width="10" height="10" fill="{col}"/>')
        out += f'<text x="{cx+14}" y="{y}">{html.escape(label)}</text>'; cx += 14 + 6.2 * len(label) + 14
    return out

made = []
# 1 conventional: x = time of day, y = day, area = volume, colour = place, lightness = enjoyment
b = ""
for i, d in enumerate(DAYS):
    y = 60 + i * 44; b += f'<text x="16" y="{y+4}">{d}</text><line x1="60" x2="{W-20}" y1="{y}" y2="{y}" stroke="#eee"/>'
for h in range(6, 22, 2):
    x = 60 + (h - 6) / 15 * (W - 90); b += f'<text x="{x}" y="{H-36}" text-anchor="middle" fill="#888">{h}:00</text>'
for r in rows:
    x = 60 + (r["t"] - 6) / 15 * (W - 90); y = 60 + r["d"] * 44; rad = 3 + math.sqrt(r["vol"]) * 0.9
    b += f'<circle cx="{x:.1f}" cy="{y}" r="{rad:.1f}" fill="{pcol[r["Place"]]}" fill-opacity="{0.2 + r["joy"] * 0.16:.2f}" stroke="{pcol[r["Place"]]}"/>'
made.append((svg("1_timeline", "1 · Week as a timetable", b, legend([(p, pcol[p]) for p in PLACES])),
  "x = time of day · y = day · circle area = volume · colour = place · opacity = enjoyment",
  "Conventional (reads like a calendar). Legible immediately; 'Reason' and 'Company' are lost."))

# 2 24-hour clock: angle = time, ring = day, size = volume, colour = type
cx, cy, b = W / 2, H / 2 - 4, ""
for i in range(7):
    rr = 36 + i * 21; b += f'<circle cx="{cx}" cy="{cy}" r="{rr}" fill="none" stroke="#eee"/><text x="{cx+3}" y="{cy-rr+4}" fill="#aaa" font-size="9">{DAYS[i]}</text>'
for h in range(0, 24, 3):
    a = h / 24 * 2 * math.pi - math.pi / 2; b += f'<text x="{cx+math.cos(a)*176:.0f}" y="{cy+math.sin(a)*176+4:.0f}" text-anchor="middle" fill="#888">{h}h</text>'
for r in rows:
    a = r["t"] / 24 * 2 * math.pi - math.pi / 2; rr = 36 + r["d"] * 21
    b += f'<circle cx="{cx+math.cos(a)*rr:.1f}" cy="{cy+math.sin(a)*rr:.1f}" r="{2+math.sqrt(r["vol"])*0.55:.1f}" fill="{tcol[r["Type"]]}"/>'
made.append((svg("2_clock", "2 · Coffee clock (24 h)", b, legend([(t, tcol[t]) for t in TYPES])),
  "angle = time of day · ring = day (Mon inside → Sun outside) · size = volume · colour = coffee type",
  "Uses the learned 'clock' pattern; empty night sector is visible at a glance. Exact times harder to read."))

# 3 stacked bars per day: length = total ml, segments = type
b, maxv = "", max(sum(r["vol"] for r in rows if r["d"] == i) for i in range(7))
for i, d in enumerate(DAYS):
    y, x = 50 + i * 46, 60; b += f'<text x="16" y="{y+20}">{d}</text>'
    for r in sorted([r for r in rows if r["d"] == i], key=lambda r: r["t"]):
        w = r["vol"] / maxv * (W - 140); b += f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="30" fill="{tcol[r["Type"]]}" stroke="#fff"/>'; x += w
    b += f'<text x="{x+6:.0f}" y="{y+20}" fill="#555">{sum(r["vol"] for r in rows if r["d"]==i)} ml</text>'
made.append((svg("3_bars", "3 · How much per day?", b, legend([(t, tcol[t]) for t in TYPES], shape="rect")),
  "bar length = total volume per day · segment = one cup, ordered by time · colour = type",
  "Most familiar form (bar). Answers 'how much' instantly; loses time of day, place, mood."))

# 4 Dear-Data glyphs: one cup per coffee
b = ""
for k, r in enumerate(sorted(rows, key=lambda r: (r["d"], r["t"]))):
    col, row = k % 8, k // 8; x, y = 40 + col * 74, 60 + row * 110
    hcup = 20 + r["vol"] / 300 * 50; fill = tcol[r["Type"]]; dash = "" if r["Company"] == "alone" else ' stroke-dasharray="4 3"'
    b += f'<rect x="{x}" y="{y+70-hcup:.0f}" width="40" height="{hcup:.0f}" fill="{fill}" fill-opacity="0.75" stroke="#333" stroke-width="2"{dash}/>'
    for s in range(r["joy"]): b += f'<path d="M{x+6+s*7} {y+64-hcup:.0f} q -3 -6 0 -12" fill="none" stroke="#999"/>'
    b += f'<text x="{x+20}" y="{y+86}" text-anchor="middle" font-size="9">{r["Day"]} {r["Time"]}</text>'
made.append((svg("4_cups", "4 · One cup per coffee (Dear Data style)", b,
  legend([(t, tcol[t]) for t in TYPES], shape="rect") + f'<text x="{W-260}" y="{H-14}" fill="#555">steam lines = enjoyment · dashed = with others</text>'),
  "one glyph per coffee · cup height = volume · colour = type · steam lines = enjoyment · dashed outline = with others",
  "Shows 5 dimensions per mark, needs a short 'how to read it' — the legend is part of the graphic."))

# 5 BREAKS CONVENTION: time runs right->left, morning at the bottom, volume as lightness, enjoyment as size
b = ""
for r in rows:
    x = W - 40 - (r["t"] - 6) / 15 * (W - 90); y = H - 60 - r["d"] * 44
    light = 90 - r["vol"] / 300 * 70
    b += f'<rect x="{x-4-r["joy"]*3:.0f}" y="{y-4-r["joy"]*3:.0f}" width="{8+r["joy"]*6}" height="{8+r["joy"]*6}" fill="hsl(25,60%,{light:.0f}%)" stroke="#333"/>'
for i, d in enumerate(DAYS): b += f'<text x="16" y="{H-56-i*44}">{d}</text>'
b += f'<text x="{W-40}" y="40" text-anchor="middle" fill="#888">06:00 ←</text><text x="60" y="40" fill="#888">← 21:00</text>'
made.append((svg("5_broken_time", "5 · BROKEN: time runs right→left, Monday at the bottom", b,
  f'<text x="16" y="{H-14}" fill="#555">square size = enjoyment · darkness = volume (dark = big)</text>'),
  "x = time, but reversed (right→left) · y = day, Monday at the bottom · lightness = volume · size = enjoyment",
  "Breaks 2 conventions. Everyone first reads it left→right and gets the day backwards; quantity as lightness is hard to compare."))

# 6 BREAKS CONVENTION (the classic mistake): category on size
b, sizes = "", {rs: 6 + i * 4 for i, rs in enumerate(REASONS)}
for r in rows:
    x = 60 + (r["t"] - 6) / 15 * (W - 90); y = 60 + r["d"] * 44
    b += f'<circle cx="{x:.1f}" cy="{y}" r="{sizes[r["Reason"]]}" fill="#e15759" fill-opacity="0.5"/>'
for i, d in enumerate(DAYS): b += f'<text x="16" y="{64+i*44}">{d}</text>'
leg = "".join(f'<circle cx="{30+i*102}" cy="{H-22}" r="{sizes[rs]/2+2}" fill="#e15759" fill-opacity="0.5"/><text x="{30+i*102+sizes[rs]/2+6}" y="{H-18}">{rs}</text>' for i, rs in enumerate(REASONS))
made.append((svg("6_broken_category_size", "6 · BROKEN: reason (a category) mapped to size", b, leg),
  "x = time · y = day · circle size = reason (alphabetical!)",
  "Deliberate mistake: size claims an order ('Waking up' > 'Break') that isn't in the data. The ranking is invented by the mapping."))

page = "".join(f'<section><h2>{n}</h2><img src="sketches/{n}.svg"><p><b>Mapping:</b> {html.escape(m)}</p><p><b>Legibility:</b> {html.escape(c)}</p></section>' for n, m, c in made)
(ROOT / "index.html").write_text(f'<!doctype html><meta charset="utf-8"><title>W38 Data Mapping</title><style>body{{font-family:sans-serif;max-width:700px;margin:auto;padding:16px}}img{{width:100%;border:1px solid #ddd}}section{{margin-bottom:40px}}</style><h1>Coffee week · 6 mappings of the same data</h1>{page}', encoding="utf-8")
print("made", len(made), "sketches")
