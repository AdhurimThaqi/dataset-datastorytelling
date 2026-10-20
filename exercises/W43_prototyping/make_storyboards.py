"""
W43 - three directions as 6-frame storyboards (A4 landscape SVG), numbers read from the survey CSV.
Run: python make_storyboards.py  -> storyboards/*.svg + storyboards.html (print it, redraw by hand).
"""
import html, math, random
from pathlib import Path
import pandas as pd

HERE = Path(__file__).parent
df = pd.read_csv(HERE.parent / "W39_data" / "survey_all_waves_all_subgroups.csv", encoding="utf-8-sig")
PILOT, LAST = "2026-06-12", df.Wave.max()
norc = df[df.Wave != PILOT]
C, E = ["very_concerned", "somewhat_concerned"], ["very_excited", "somewhat_excited"]

def pct(d, q, ans, sg="total", dim=None, mean=False):
    d = d[(d.Question_ID == q) & (d.Subgroup == sg) & d.Answer.isin(ans)]
    if dim: d = d[d.Dimension.str.contains(dim, regex=False)]
    s = d.groupby("Wave").Percentage.sum()
    return round(s.mean() if mean else s[LAST])

N = dict(
    conc=pct(df, "ai_sentiment", C), exc=pct(df, "ai_sentiment", E),
    fake=pct(df, "ai_community_impact", ["have_seen", "starting"], dim="real from"),
    inev=pct(df, "ai_agency", ["inevitable"]), shape=pct(df, "ai_agency", ["can_shape"]),
    c18=pct(norc, "ai_sentiment", C, "age_18_34", mean=True), c65=pct(norc, "ai_sentiment", C, "age_65_plus", mean=True),
    s18=pct(norc, "ai_agency", ["can_shape"], "age_18_34", mean=True), s65=pct(norc, "ai_agency", ["can_shape"], "age_65_plus", mean=True),
    time18=pct(norc, "ai_community_impact", ["have_seen", "starting"], "age_18_34", "saving time", True),
    dem=pct(norc, "ai_regulation", ["somewhat_too_little", "way_too_little"], "party_dem", "environmental", True),
    rep=pct(norc, "ai_regulation", ["somewhat_too_little", "way_too_little"], "party_rep", "environmental", True),
)
W, H, FW, FH = 1123, 794, 345, 280          # A4 landscape, 3x2 frames
X0, Y0, GX, GY = 24, 96, 20, 70
INK, MID, LIGHT, ORA, BLU = "#222", "#888", "#ddd", "#eb6834", "#2a78d6"
e = html.escape

def t(x, y, s, size=13, w="normal", fill=INK, anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{anchor}">{e(s)}</text>'
def box(x, y, w, h, fill="none", stroke=INK, r=6, sw=2, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def person(x, y, s=1, label=None, col=INK):
    o = (f'<circle cx="{x}" cy="{y}" r="{7*s}" fill="none" stroke="{col}" stroke-width="2"/>'
         f'<path d="M{x} {y+7*s} v{18*s} M{x-10*s} {y+14*s} h{20*s} M{x} {y+25*s} l{-8*s} {12*s} M{x} {y+25*s} l{8*s} {12*s}" stroke="{col}" stroke-width="2" fill="none"/>')
    return o + (t(x, y + 52 * s, label, 11, anchor="middle") if label else "")
def bubble(x, y, w, h, s, size=12):
    lines, out, cur = [], "", ""
    for word in s.split():
        if len(cur + " " + word) * size * 0.55 > w - 16: lines.append(cur); cur = word
        else: cur = (cur + " " + word).strip()
    lines.append(cur)
    out += box(x, y, w, h, "#fff", INK, 12) + f'<path d="M{x+20} {y+h} l-6 12 l16 -12" fill="#fff" stroke="{INK}" stroke-width="2"/>'
    return out + "".join(t(x + 8, y + 18 + i * (size + 3), ln, size) for i, ln in enumerate(lines))
def dots(x, y, n_or, n_bl, cols=20, r=4, gap=11, you=None):
    o = ""
    for i in range(100):
        c = ORA if i < n_or else BLU if i < n_or + n_bl else LIGHT
        cx, cy = x + (i % cols) * gap, y + (i // cols) * gap
        o += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>'
        if you == i: o += f'<circle cx="{cx}" cy="{cy}" r="{r+4}" fill="none" stroke="{INK}" stroke-width="2"/>'
    return o
def bars(x, y, items, maxw=230):
    o = ""
    for i, (label, v, c) in enumerate(items):
        yy = y + i * 34
        o += t(x, yy, label, 12) + f'<rect x="{x}" y="{yy+5}" width="{v/100*maxw:.0f}" height="14" rx="3" fill="{c}"/>' + t(x + v / 100 * maxw + 6, yy + 17, f"{v}%", 12, "bold")
    return o
def phone(x, y):
    return box(x + FW / 2 - 70, y + 8, 140, FH - 72, "#fafafa", INK, 14) + f'<line x1="{x+FW/2-15}" y1="{y+16}" x2="{x+FW/2+15}" y2="{y+16}" stroke="{MID}" stroke-width="3"/>'
def room(x, y):
    return box(x + 34, y + 34, FW - 54, FH - 54, "#fafafa", INK, 2) + t(x + FW - 26, y + 50, "room, seen from above", 10, fill=MID, anchor="end")
def crowd(x, y):
    o, rnd = "", random.Random(7)
    for i in range(100):
        h, v = rnd.random(), rnd.random()
        if i < N["conc"]: cx = x + 190 + h * 120          # concerned side (right)
        elif i < N["conc"] + N["exc"]: cx = x + 55 + h * 60   # excited side (left)
        else: cx = x + 125 + h * 55                        # none / no answer (middle)
        c = ORA if i < N["conc"] else BLU if i < N["conc"] + N["exc"] else "#bbb"
        o += f'<circle cx="{cx:.0f}" cy="{y + 62 + v * 170:.0f}" r="3.5" fill="{c}"/>'
    return o

def sheet(name, title, sub, frames):
    body = ""
    for i, (draw, caption) in enumerate(frames):
        x, y = X0 + (i % 3) * (FW + GX), Y0 + (i // 3) * (FH + GY)
        body += box(x, y, FW, FH, "#fff", INK, 4) + t(x + 10, y + 22, str(i + 1), 16, "bold") + draw(x, y)
        for j, ln in enumerate(caption.split("\n")):
            body += t(x + 4, y + FH + 20 + j * 16, ln, 13, "bold" if j == 0 else "normal", INK if j == 0 else "#555")
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica,Arial,sans-serif">'
           f'<rect width="{W}" height="{H}" fill="#fff"/>{t(24, 36, title, 22, "bold")}{t(24, 60, sub, 13, fill="#555")}'
           f'{box(W-330, 18, 306, 46, "#fff4e5", ORA, 6, 1.5)}{t(W-318, 37, "DIGITAL REFERENCE, NOT THE MILESTONE", 12, "bold", ORA)}'
           f'{t(W-318, 55, "Redraw by hand with a thick pen, then photograph.", 11, fill="#555")}{body}</svg>')
    (HERE / "storyboards" / f"{name}.svg").write_text(svg, encoding="utf-8")
    return name, title

n = N
A = [
 (lambda x, y: phone(x, y) + box(x+FW/2-55, y+40, 110, 90, LIGHT, MID, 4) + t(x+FW/2, y+90, "[ image ]", 12, fill=MID, anchor="middle")
   + box(x+FW/2-55, y+145, 50, 26, "#fff") + t(x+FW/2-30, y+163, "Real", 12, anchor="middle")
   + box(x+FW/2+5, y+145, 50, 26, "#fff") + t(x+FW/2+30, y+163, "AI", 12, anchor="middle"),
  "Hook: Real or AI?\nVisitor guesses on one image."),
 (lambda x, y: phone(x, y) + t(x+FW/2, y+80, f"{n['fake']}%", 40, "bold", ORA, "middle")
   + t(x+FW/2, y+108, "of Americans see people", 11, anchor="middle") + t(x+FW/2, y+123, "struggling to tell real", 11, anchor="middle")
   + t(x+FW/2, y+138, "from fake", 11, anchor="middle") + t(x+FW/2, y+175, "It was AI.", 12, "bold", anchor="middle"),
  "Reveal + first number\nThe hook connects to the data."),
 (lambda x, y: phone(x, y) + t(x+FW/2, y+55, "How do you feel", 12, "bold", anchor="middle") + t(x+FW/2, y+70, "about AI?", 12, "bold", anchor="middle")
   + f'<line x1="{x+FW/2-50}" y1="{y+110}" x2="{x+FW/2+50}" y2="{y+110}" stroke="{INK}" stroke-width="3"/><circle cx="{x+FW/2+20}" cy="{y+110}" r="8" fill="{INK}"/>'
   + t(x+FW/2-52, y+132, "excited", 10, fill=BLU) + t(x+FW/2+52, y+132, "concerned", 10, fill=ORA, anchor="end")
   + box(x+FW/2-45, y+150, 90, 24, "#fff") + t(x+FW/2, y+167, "none of these", 11, anchor="middle"),
  "You answer\nThe survey's own question, nothing stored."),
 (lambda x, y: t(x+20, y+50, "100 Americans", 12, "bold") + dots(x+22, y+70, n['conc'], n['exc'], 20, 5, 15, you=8)
   + t(x+20, y+238, f"{n['conc']} concerned", 12, "bold", ORA) + t(x+140, y+238, f"{n['exc']} excited", 12, "bold", BLU) + t(x+240, y+238, "(o) = you", 12),
  "You vs. America\nYour dot among 100 respondents."),
 (lambda x, y: t(x+20, y+50, "Concerned, by age", 12, "bold") + bars(x+20, y+80, [("Age 18-34", n['c18'], ORA), ("Age 65+", n['c65'], ORA)])
   + t(x+20, y+170, "<- people like you", 12, "bold") + t(x+20, y+192, "(average of comparable waves)", 10, fill=MID),
  "People like you\nSame view, split by age group."),
 (lambda x, y: t(x+20, y+50, "The turn", 12, "bold") + bars(x+20, y+78, [("AI is inevitable", n['inev'], ORA), ("Society can shape it", n['shape'], BLU)])
   + t(x+20, y+172, f"Under 35: {n['s18']}% think it can be shaped", 12) + t(x+20, y+190, f"Over 65: {n['s65']}%", 12),
  "Authored ending\nWorried, but it's coming anyway."),
]
B = [
 (lambda x, y: room(x, y) + f'<rect x="{x+55}" y="{y+120}" width="{FW-85}" height="30" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>'
   + t(x+57, y+113, "excited", 11, fill=BLU) + t(x+FW-32, y+113, "concerned", 11, fill=ORA, anchor="end") + person(x+FW/2+10, y+180, .8) + t(x+FW/2+10, y+250, "entrance", 11, fill=MID, anchor="middle"),
  "Entrance\nA floor strip from excited to concerned."),
 (lambda x, y: room(x, y) + f'<rect x="{x+55}" y="{y+120}" width="{FW-85}" height="30" fill="none" stroke="{INK}" stroke-width="2" stroke-dasharray="6 4"/>'
   + person(x+FW-90, y+95, .8) + t(x+FW/2+10, y+210, "visitor steps where they feel", 12, anchor="middle"),
  "You answer with your body\nNo screen, no form."),
 (lambda x, y: room(x, y) + crowd(x, y) + person(x+FW-90, y+110, .8) + t(x+56, y+250, "excited", 10, fill=BLU) + t(x+FW-32, y+250, "concerned", 10, fill=ORA, anchor="end"),
  "The crowd appears\n100 projected dots = 100 respondents."),
 (lambda x, y: box(x+30, y+40, FW-60, 150, "#fafafa", INK, 2) + t(x+FW/2, y+30, "wall projection", 10, fill=MID, anchor="middle")
   + t(x+FW/2, y+100, "You are standing with", 15, anchor="middle") + t(x+FW/2, y+135, f"{n['conc']} of 100 Americans", 22, "bold", ORA, "middle"),
  "Wall text\nThe number, said plainly."),
 (lambda x, y: room(x, y) + person(x+FW-90, y+100, .8, "you") + person(x+100, y+100, .8, "friend")
   + f'<path d="M{x+110} {y+190} q {FW/2-90} 40 {FW-200} 0" fill="none" stroke="{MID}" stroke-width="2" stroke-dasharray="4 4"/>' + t(x+FW/2+10, y+250, "two clouds, compared", 11, fill=MID, anchor="middle"),
  "With company\nA friend stands elsewhere, you compare."),
 (lambda x, y: box(x+30, y+40, FW-60, 150, "#fafafa", INK, 2) + t(x+FW/2, y+30, "exit wall", 10, fill=MID, anchor="middle")
   + t(x+FW/2, y+95, f"{n['inev']}% say it's coming anyway.", 15, "bold", anchor="middle") + t(x+FW/2, y+130, "What do you think?", 14, anchor="middle"),
  "Exit\nThe turn, as a question to take home."),
]
def table(x, y, people):
    o = f'<rect x="{x+60}" y="{y+170}" width="{FW-120}" height="12" fill="{LIGHT}" stroke="{INK}" stroke-width="2"/>'
    for i, lab in enumerate(people):
        o += person(x + 75 + i * (FW - 150) / max(1, len(people) - 1), y + 110, .9, lab)
    return o
C3 = [
 (lambda x, y: table(x, y, ["Grandma 70", "Student 24", "Dem", "Rep"]), "The table\nFour people from four survey groups."),
 (lambda x, y: table(x, y, ["Grandma 70", "", "", ""]) + bubble(x+40, y+35, 200, 44, "Everyone I know is worried about it.") + t(x+20, y+232, f"65+: {n['c65']}% concerned", 11, "bold", ORA),
  "First voice\nEvery line is backed by a real number."),
 (lambda x, y: table(x, y, ["", "Student 24", "", "Rep"]) + box(x+70, y+30, FW-140, 50, "#fff4e5", ORA, 8) + t(x+FW/2, y+52, "Whom do you listen to next?", 13, "bold", anchor="middle")
   + t(x+FW/2, y+70, "A: the student  /  B: the politics", 11, anchor="middle"),
  "The branch\nViewer chooses whom to follow."),
 (lambda x, y: table(x, y, ["", "Student 24", "", ""]) + bubble(x+135, y+35, 200, 44, "Honestly, it saves me hours every week.") + t(x+20, y+232, f"18-34: {n['time18']}% see time being saved", 11, "bold", BLU),
  "Branch A: the student\nThe young side of the data."),
 (lambda x, y: table(x, y, ["", "", "Dem", "Rep"]) + bubble(x+190, y+28, 150, 40, "Government must do more!", 12) + t(x+20, y+232, f"Env./data centres, 'too little': Dem {n['dem']}%  Rep {n['rep']}%", 11, "bold"),
  "Branch B: the politics\nSame worry, different remedy."),
 (lambda x, y: table(x, y, ["Grandma 70", "Student 24", "Dem", "Rep"]) + box(x+40, y+30, FW-80, 46, "#fff", INK, 8) + t(x+FW/2, y+50, "Worried, but it's coming anyway.", 13, "bold", anchor="middle")
   + t(x+FW/2, y+68, f"{n['inev']}% say AI is inevitable", 11, anchor="middle"),
  "Shared ending\nEvery branch arrives here."),
]
made = [sheet("A_real_or_ai", "A · Real or AI?  (web → interactive prototype)", f"Data: Americans on AI, latest wave {LAST} unless marked; pilot wave excluded.", A),
        sheet("B_stand_where_you_feel", "B · Stand where you feel  (exhibition → animatic)", "Visitors answer with their position in the room; projected dots = survey respondents.", B),
        sheet("C_dinner_table", "C · Dinner table  (branched animatic)", "Each character speaks for a survey group; every line is backed by a number from the data.", C3)]
pages = "".join(f'<section><img src="storyboards/{n_}.svg" alt="{e(t_)}"></section>' for n_, t_ in made)
(HERE / "storyboards.html").write_text(
    '<!doctype html><meta charset="utf-8"><title>W43 storyboards</title><style>body{margin:0;background:#eee;font-family:sans-serif}'
    'section{background:#fff;max-width:1123px;margin:16px auto}img{width:100%;display:block}'
    '@media print{@page{size:A4 landscape;margin:0}body{background:#fff}section{margin:0;page-break-after:always}}</style>' + pages, encoding="utf-8")
print("numbers:", N); print("made", [m[0] for m in made])
