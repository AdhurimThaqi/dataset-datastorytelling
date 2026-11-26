"""Final presentation (W51, 17.12.2026): fills "Adhurim Thaqi — School Template.pptx" with the project content.

Run from the repo root:  python Final-presentation/build_deck.py
Writes Final-presentation/Real-or-AI_final-presentation.pptx (+ .pdf when PowerPoint is installed). The template's fonts (Syne + Outfit, embedded),
colours and slide designs are kept; only text, bar heights and pictures change.
Survey numbers are the ones v8 shows (from the official CSV, checked by check.py).
"""
import copy
from pathlib import Path

from pptx import Presentation
from pptx.util import Pt, Emu

ROOT = Path(__file__).resolve().parents[1]
HERE = Path(__file__).parent
TEMPLATE = ROOT / "Adhurim Thaqi — School Template.pptx"
OUT = HERE / "Real-or-AI_final-presentation.pptx"
IMG = HERE / "img"
FOOT = "Data Storytelling · HSLU"

prs = Presentation(TEMPLATE)
T = list(prs.slides)                      # template slides 1..12 -> T[0]..T[11]


def dup(src):
    """Copy a template slide (background, shapes) to a new slide at the end."""
    new = prs.slides.add_slide(src.slide_layout)
    new._element.replace(new._element.cSld, copy.deepcopy(src._element.cSld))
    new.__dict__.pop("shapes", None)   # python-pptx caches the shape tree; drop the old one
    return new


def shape(slide, name):
    for sh in slide.shapes:
        if sh.name == name:
            return sh
    raise KeyError(name)


def put(tf, text):
    """Replace the text but keep the first run's formatting. A list = one paragraph each."""
    lines = text if isinstance(text, list) else [text]
    p0 = tf.paragraphs[0]
    for extra in tf.paragraphs[1:]:
        extra._p.getparent().remove(extra._p)
    runs = p0.runs
    for r in runs[1:]:
        r._r.getparent().remove(r._r)
    runs[0].text = lines[0]
    for line in lines[1:]:
        p = copy.deepcopy(p0._p); tf._txBody.append(p)
        tf.paragraphs[-1].runs[0].text = line


def txt(slide, name, text, **geo):
    sh = shape(slide, name)
    put(sh.text_frame, text)
    for k, v in geo.items():
        setattr(sh, k, Pt(v))
    return sh


def geo(slide, name, **g):
    sh = shape(slide, name)
    for k, v in g.items():
        setattr(sh, k, Pt(v))


def foot(slide, n):
    """Footer: module name left, page number right (the template's last two text boxes)."""
    texts = [sh for sh in slide.shapes if sh.has_text_frame and sh.top > Pt(480)]
    put(texts[0].text_frame, FOOT); texts[0].width = Pt(220)
    put(texts[1].text_frame, f"{n:02d}")


def notes(slide, text):
    slide.notes_slide.notes_text_frame.text = text


def picture(slide, path, box, alt, pad=24):
    """Fit a picture inside the template's white image card (Shape 4), centred."""
    card = shape(slide, box)
    from PIL import Image
    w, h = Image.open(path).size
    bw, bh = card.width - Pt(2 * pad), card.height - Pt(2 * pad)
    s = min(bw / w, bh / h)
    pw, ph = int(w * s), int(h * s)
    pic = slide.shapes.add_picture(str(path), card.left + (card.width - pw) // 2, card.top + (card.height - ph) // 2, pw, ph)
    pic._element.nvPicPr.cNvPr.set("descr", alt)


def bars(slide, values, labels, highlight, takeaway, source):
    """The template's bar chart: four bars on a baseline at y=392pt, tallest bar 190pt."""
    bar_names, val_names, cat_names = ["Shape 4", "Shape 6", "Shape 8", "Shape 10"], ["Text 3", "Text 5", "Text 7", "Text 9"], ["Text 15", "Text 16", "Text 17", "Text 18"]
    fills = [shape(slide, b).fill.fore_color.rgb for b in bar_names]
    dark, light = fills[2], fills[0]                       # template: bar C is the highlighted one
    top = max(values)
    for i, v in enumerate(values):
        h = 190 * v / top
        b = shape(slide, bar_names[i]); b.top = Pt(392 - h); b.height = Pt(h)
        b.fill.solid(); b.fill.fore_color.rgb = dark if i == highlight else light
        t = txt(slide, val_names[i], str(v)); t.top = Pt(392 - h - 25); t.left = b.left; t.width = b.width
        txt(slide, cat_names[i], labels[i])
    # the template colours the highlighted category label; move that colour to the new highlight
    cats = [shape(slide, n).text_frame.paragraphs[0].runs[0] for n in cat_names]
    hl_rgb, hl_b = cats[2].font.color.rgb, cats[2].font.bold
    base_rgb = cats[0].font.color.rgb
    for i, r in enumerate(cats):
        r.font.color.rgb = hl_rgb if i == highlight else base_rgb
        r.font.bold = hl_b if i == highlight else None
    txt(slide, "Text 13", takeaway, height=62)
    txt(slide, "Text 14", source, top=372, height=30)
    geo(slide, "Shape 11", height=160)


def three(slide, label, title, body, points, n):
    txt(slide, "Text 0", label)
    txt(slide, "Text 1", title)
    txt(slide, "Text 2", body)
    for name, p in zip(["Text 3", "Text 4", "Text 5"], points):
        txt(slide, name, p)
    foot(slide, n)


def label_fit(slide, name, text, per_char=6.6, pad=22):
    sh = txt(slide, name, text)
    sh.width = Pt(len(text) * per_char + pad)


# ---------- build the slide list (copies first, then fill) ----------
cover, s_play, s_why, s_57, s_game, s_look, s_key, s_age, s_table, s_honest, s_end, s_refs, s_thanks = (
    T[0], dup(T[7]), T[3], T[6], T[8], T[7], dup(T[3]), dup(T[6]), T[5], dup(T[3]), T[9], T[10], T[11])

# 1 · cover
txt(cover, "Text 3", "Data Storytelling · HS26", width=170)
txt(cover, "Text 4", "Real or AI?")
txt(cover, "Text 5", "A four-minute game about the Americans on AI survey", width=500, top=262)
txt(cover, "Text 6", "Adhurim Thaqi", width=90)
txt(cover, "Text 7", "Alain Leclerc von Bonin · Gordan Savičić · Fiona Zellweger", left=166, width=330)
txt(cover, "Text 8", "17.12.2026", left=508, width=80)
notes(cover, "Hi, I'm Adhurim. My project turns the Americans on AI survey into a short game. "
             "Before I explain anything, I'd like you to play it.")

# 2 · scan and play (image layout + QR code)
label_fit(s_play, "Text 0", "Play along")
txt(s_play, "Text 1", "Scan and play")
txt(s_play, "Text 2", "Everyone in the room gets the same pictures and questions. It takes about four minutes. "
                      "At the end, your name shows up on the big screen.", height=72)
txt(s_play, "Text 3", "Room HSLU · or open the live page: …/W47_sprint3/live.html?room=hslu", top=372, height=34)
picture(s_play, IMG / "qr-hslu.png", "Shape 4", "QR code that opens the game in room HSLU", pad=40)
foot(s_play, 2)
notes(s_play, "Switch to live.html?room=hslu (press F for fullscreen) while people play. "
              "Give it about four minutes, then show the top 10 and come back to the slides. "
              "If the Wi-Fi fails: play it yourself on the phone with screen mirroring.")

# 3 · why
three(s_why, "Why", "Nobody reads surveys",
      "“The challenge is knowing whether the people commenting represent the wider population or just a very vocal group.” (interview 2)",
      ["All 3 interviewees had a real-or-fake story", "None of them reads surveys", "Opinions come from Reddit and comments"], 3)
label_fit(s_why, "Text 0", "Why")
notes(s_why, "I started with three interviews with people from the target group, 20 to 35, using AI regularly. "
             "All three told me about a time they couldn't tell if something was real. None of them reads surveys. "
             "A representative survey can answer the question in that quote.")

# 4 · 57 in 100 (bar chart)
txt(s_57, "Text 1", "57 in 100 already see it around them")
label_fit(s_57, "Text 0", "The data")
bars(s_57, [57, 24, 11, 8], ["Already see it", "Starting to see it", "Expect it, or don't", "Not sure"], 0,
     "Only 2 in 100 don't expect it at all. Being fooled by AI isn't a personal weakness.",
     "Source: Americans on AI, 10–14 Sep 2026, n = 1,083")
foot(s_57, 4)
notes(s_57, "The data: Americans on AI by Athena Insights, run by NORC, about 1,000 US adults every two weeks. "
            "I use the latest wave, 10 to 14 September, 1,083 people. "
            "Question: have people in your community struggled to tell real from fake because of AI? 57 in 100 say they already see it. "
            "Only 2 in 100 don't expect it at all.")

# 5 · how the game works (four steps)
label_fit(s_game, "Text 0", "The game")
txt(s_game, "Text 1", "Play first, then see the data")
el = copy.deepcopy(shape(s_why, "Text 2")._element)          # same style as the body text on slide 3
el.nvSpPr.cNvPr.id = max(sh.shape_id for sh in s_game.shapes) + 1; el.nvSpPr.cNvPr.name = "Lead"
s_game.shapes._spTree.append(el)
lead = shape(s_game, "Lead")
put(lead.text_frame, "Five levels in about four minutes. Every level ends with a real number from the survey, so you compare your guess with 1,083 US adults.")
lead.left, lead.top, lead.width, lead.height = Pt(64), Pt(170), Pt(560), Pt(80)
steps = [("Spot the fakes", "6 pictures, 2 texts: real or AI?"),
         ("The number", "Guess how many of 100 see it"),
         ("True or false", "3 claims, some numbers wrong"),
         ("Your turn", "Your answer vs. US adults")]
for i, (a, b) in enumerate(steps):
    txt(s_game, ["Text 4", "Text 8", "Text 12", "Text 16"][i], a)
    txt(s_game, ["Text 5", "Text 9", "Text 13", "Text 17"][i], b, height=34)
for sh in s_game.shapes:                      # lift the four cards a little so two-line notes fit
    if 300 <= sh.top / 12700 < 470 and sh.name != "Lead":
        sh.top -= Pt(24)
for n in ["Shape 2", "Shape 6", "Shape 10", "Shape 14"]:
    geo(s_game, n, height=158)
foot(s_game, 5)
notes(s_game, "From the first version, the plan was that you experience it before you read the number. "
              "Level 1 is the hook, Swiss valley photos against AI pictures; it gets hard from picture 3. "
              "Then the survey levels: guess the number, true or false, and your own answer compared with the US.")

# 6 · what it looks like (screenshots)
label_fit(s_look, "Text 0", "Prototype v8")
txt(s_look, "Text 1", "What it looks like")
txt(s_look, "Text 2", "You get fooled first. Then the survey shows you're not alone: most Americans already see it happen.", height=72)
txt(s_look, "Text 3", "Fig. 1 — v8 on a phone: a picture answer and the number level", top=372, height=34)
picture(s_look, IMG / "phones2.png", "Shape 4", "Two phone screenshots of the game: a real photo answered wrong, and the number level showing 57 in 100", pad=20)
foot(s_look, 6)
notes(s_look, "Left: you guessed AI, it was a real photo. Middle: the number level, your guess against the real 57. "
              "Right: the end screen puts the survey first, then your score.")

# 7 · key message
three(s_key, "Key message", "Worried, but it's coming anyway",
      "Most Americans are worried about AI, and most think it's coming anyway. Younger adults are more likely than older adults to think it can still be shaped.",
      ["69 in 100 are concerned about AI", "68 in 100 say it's coming anyway", "17 in 100 think it can still be shaped"], 7)
label_fit(s_key, "Text 0", "Key message")
notes(s_key, "If people remember one sentence, it should be this one. 69 in 100 are concerned, 68 in 100 say AI is coming whether we want it or not. "
             "Only 17 in 100 think society can still shape it.")

# 8 · by age (bar chart)
label_fit(s_age, "Text 0", "By age")
txt(s_age, "Text 1", "Younger adults think it can still be shaped")
bars(s_age, [27, 23, 10, 8], ["18–34", "35–49", "50–64", "65+"], 0,
     "27 in 100 of 18–34 vs 8 in 100 of 65+. The gap is bigger than the margin of error.",
     "Source: Americans on AI, 10–14 Sep 2026, n = 1,083")
foot(s_age, 8)
notes(s_age, "Share who say society can still shape AI, by age. 18 to 34: 27 in 100. 65 plus: 8 in 100. "
             "The groups are small, so I checked the margin of error: this gap is bigger, so it's a real difference. "
             "18–34 and 35–49 are too close to call, and the game says so.")

# 9 · what testing changed (table)
label_fit(s_table, "Text 0", "Iteration")
txt(s_table, "Text 1", "What testing changed")
rows = [("Feedback", "From", "What changed", "Version"),
        ("Pictures too easy to tell apart", "Mentoring, 12.11", "Hard mode with new 2026 AI pictures", "v7"),
        ("Always scrolling and clicking Next", "Mentoring, 12.11", "The game moves on by itself", "v7"),
        ("7 levels are too many", "Coaching, 19.11", "5 levels, “more or fewer” removed", "v8"),
        ("Side panels pull attention away", "UI review, 26.11", "One drawer, opened only on a tap", "v8"),
        ("It scrolls on my phone", "Phone test, 26.11", "Every playing screen fits", "v8")]
tbl = shape(s_table, "Table 0").table
for r, row in enumerate(rows):
    for c, val in enumerate(row):
        put(tbl.cell(r, c).text_frame, val)
for c, w in enumerate([250, 150, 341, 90]):
    tbl.columns[c].width = Pt(w)
foot(s_table, 9)
notes(s_table, "Eight versions since October. These are the changes that mattered most, each one from a test or a review. "
               "The biggest one: cutting 7 levels to 5 after the coaching.")

# 10 · honesty
three(s_honest, "Honesty", "Every number is checked",
      "The game reads every survey number from the official CSV, and a script compares the page with the data. These are US adults, not Swiss, and the game says so.",
      ["149 checks, 0 mismatches", "Within the margin: “too close to call”", "The real number is always shown"], 10)
label_fit(s_honest, "Text 0", "Honesty")
notes(s_honest, "Because this is your data, I was careful. No hand-typed numbers. "
                "Differences inside the margin of error are called too close to call. "
                "True or false always shows the real number afterwards, so nobody leaves with a wrong one.")

# 11 · conclusion
txt(s_end, "Text 2", "Being fooled by AI isn't a personal weakness. Most Americans already see it around them.")
txt(s_end, "Text 3", "The game lets you feel it first and then shows you the number.")
notes(s_end, "Thank you. I'd like to hear what you think, especially about how the game uses the data.")

# 12 · references
refs = ["Athena Insights & NORC at the University of Chicago. (2026). Americans on AI [Survey, wave 10–14 Sep 2026]. americanson.ai",
        "Pictures: Wikimedia Commons (credited in the game, CC BY-SA / CC0). AI pictures made in Figma AI (gpt-image-2.5, gemini-3.1-flash-image).",
        "Texts: Wikivoyage (versions from before ChatGPT); AI texts written by Claude. Icons: Lucide (ISC licence).",
        "Design references: Which Face Is Real?; NYT The Upshot, “You Draw It” (2015); Pew Research Center, Political Typology Quiz."]
for name, r in zip(["Text 3", "Text 5", "Text 7", "Text 10"], refs):
    txt(s_refs, name, r)
foot(s_refs, 12)
notes(s_refs, "Sources.")

# 13 · thank you
txt(s_thanks, "Text 5", "Adhurim Thaqi", width=110)
txt(s_thanks, "Text 6", "adhurimthaqi.github.io/dataset-datastorytelling", left=186, width=300)
notes(s_thanks, "Questions.")

# ---------- order: drop the agenda, section divider and team slides ----------
order = [cover, s_play, s_why, s_57, s_game, s_look, s_key, s_age, s_table, s_honest, s_end, s_refs, s_thanks]
lst = prs.slides._sldIdLst
ids = {s.slide_id: el for el in lst for s in prs.slides if s.slide_id == el.id}
keep = [ids[s.slide_id] for s in order]
for el in list(lst):
    if el not in keep:
        prs.part.drop_rel(el.rId); lst.remove(el)
for el in keep:
    lst.remove(el); lst.append(el)

# ---------- animations: a fade between slides, then each slide builds itself (no extra clicks) ----------
from lxml import etree
P = "http://schemas.openxmlformats.org/presentationml/2006/main"
BARS = {"Shape 4", "Shape 6", "Shape 8", "Shape 10"}      # chart bars grow up from the baseline


def animate(slide, is_chart=False):
    sp = slide._element
    for old in sp.findall(f"{{{P}}}transition") + sp.findall(f"{{{P}}}timing"):
        sp.remove(old)
    items = []
    for sh in slide.shapes:
        if sh.top >= Pt(480) or (sh.width >= Pt(950) and sh.height >= Pt(530)):
            continue                                        # footer and full-slide backgrounds stay put
        wipe = is_chart and sh.name in BARS
        items.append((sh.shape_id, wipe, sh.has_text_frame and bool(sh.text_frame.text.strip())))
    ids = iter(range(3, 10_000))
    effects = []
    for k, (spid, wipe, _) in enumerate(items):
        delay = k * (140 if not is_chart else 110)
        if wipe:
            preset, sub, filt = 22, 4, "wipe(up)"           # wipe from bottom
        else:
            preset, sub, filt = 10, 0, "fade"
        effects.append(f"""<p:par><p:cTn id="{next(ids)}" presetID="{preset}" presetClass="entr" presetSubtype="{sub}" fill="hold" nodeType="withEffect">
<p:stCondLst><p:cond delay="{delay}"/></p:stCondLst><p:childTnLst>
<p:set><p:cBhvr><p:cTn id="{next(ids)}" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl>
<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst></p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>
<p:animEffect transition="in" filter="{filt}"><p:cBhvr><p:cTn id="{next(ids)}" dur="{600 if wipe else 450}"/><p:tgtEl><p:spTgt spid="{spid}"/></p:tgtEl></p:cBhvr></p:animEffect>
</p:childTnLst></p:cTn></p:par>""")
    ANIMBG = ' animBg="1"'
    bld = "".join(f'<p:bldP spid="{spid}" grpId="0"{"" if txt else ANIMBG}/>' for spid, _, txt in items
                  if slide.shapes._spTree.xpath(f"./p:sp[p:nvSpPr/p:cNvPr/@id='{spid}']"))
    xml = f"""<p:root xmlns:p="{P}"><p:transition spd="med"><p:fade/></p:transition><p:timing><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot"><p:childTnLst>
<p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq"><p:childTnLst>
<p:par><p:cTn id="{next(ids)}" fill="hold"><p:stCondLst><p:cond delay="indefinite"/><p:cond evt="onBegin" delay="0"><p:tn val="2"/></p:cond></p:stCondLst><p:childTnLst>
<p:par><p:cTn id="{next(ids)}" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>{"".join(effects)}</p:childTnLst></p:cTn></p:par>
</p:childTnLst></p:cTn></p:par>
</p:childTnLst></p:cTn><p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>
<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst></p:seq>
</p:childTnLst></p:cTn></p:par></p:tnLst>{f"<p:bldLst>{bld}</p:bldLst>" if bld else ""}</p:timing></p:root>"""
    root = etree.fromstring(xml)
    anchor = sp.find(f"{{{P}}}clrMapOvr")
    pos = list(sp).index(anchor) + 1
    for el in reversed(list(root)):
        sp.insert(pos, el)


for s in order:
    animate(s, is_chart=s in (s_57, s_age))

prs.save(OUT)
print("wrote", OUT.relative_to(ROOT), "·", len(order), "slides")

# ---------- PDF (needs PowerPoint on Windows; the PDF has no animations) ----------
try:
    import win32com.client
    app = win32com.client.Dispatch("PowerPoint.Application")
    deck = app.Presentations.Open(str(OUT), True, False, False)
    deck.SaveAs(str(OUT.with_suffix(".pdf")), 32)
    deck.Close()
    print("wrote", OUT.with_suffix(".pdf").relative_to(ROOT))
except Exception as e:  # no PowerPoint / no pywin32: export the PDF by hand (File > Export > PDF)
    print("PDF skipped:", e)
