"""W43 Crazy 6's: digital reference sheet (A4 landscape SVG) for the six interaction ideas.
Run: python make_crazy6.py -> wireframes/crazy6.svg   (redraw by hand; this is not the paper sheet)"""
import html, random
from pathlib import Path
HERE = Path(__file__).parent
W, H, FW, FH, X0, Y0, GX, GY = 1123, 794, 345, 250, 24, 96, 20, 92
INK, MID, LIGHT, ORA, BLU = "#222", "#888", "#ddd", "#eb6834", "#2a78d6"
e = html.escape
def t(x, y, s, size=13, w="normal", fill=INK, a="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill}" text-anchor="{a}">{e(s)}</text>'
def box(x, y, w, h, fill="none", stroke=INK, r=6, sw=2, dash=""):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
def phone(x, y):
    cx = x + FW / 2
    return box(cx - 62, y + 30, 124, FH - 42, "#fafafa", INK, 14) + f'<line x1="{cx-14}" y1="{y+38}" x2="{cx+14}" y2="{y+38}" stroke="{MID}" stroke-width="3"/>'
def dots(x, y, n, cols=20, gap=13, r=4, you=None):
    o = ""
    for i in range(100):
        cx, cy = x + (i % cols) * gap, y + (i // cols) * gap
        o += f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{ORA if i < n else LIGHT}"/>'
        if i == you: o += f'<circle cx="{cx}" cy="{cy}" r="{r+4}" fill="none" stroke="{INK}" stroke-width="2"/>'
    return o
cx = lambda x: x + FW / 2
F = [
 ("1 · Guess", lambda x, y: phone(x, y) + box(cx(x)-48, y+52, 96, 90, LIGHT, MID, 4) + t(cx(x), y+104, "?", 28, "bold", MID, "middle")
   + box(cx(x)-48, y+156, 44, 24, "#fff") + t(cx(x)-26, y+173, "REAL", 11, a="middle") + box(cx(x)+4, y+156, 44, 24, "#fff") + t(cx(x)+26, y+173, "AI", 11, a="middle")
   + t(cx(x), y+206, "57 of 100 struggle too", 10, "bold", ORA, "middle"),
  "The reader guesses if the image is real or AI", "… and then sees: 57 of 100 Americans struggle too"),
 ("2 · Place yourself", lambda x, y: dots(x+52, y+60, 57, you=None) + f'<line x1="{x+52}" y1="{y+168}" x2="{x+300}" y2="{y+168}" stroke="{INK}" stroke-width="3"/>'
   + f'<circle cx="{x+250}" cy="{y+168}" r="9" fill="#fff" stroke="{INK}" stroke-width="3"/>' + t(x+250, y+195, "you", 11, "bold", a="middle")
   + t(x+52, y+195, "never seen it", 10, fill=MID) + t(x+300, y+212, "I've seen this", 10, fill=MID, a="end"),
  "The reader drags their dot to \"I've seen this happen\"", "… and then sees 57 dots light up next to theirs"),
 ("3 · Sort", lambda x, y: "".join(box(x+40+(i%3)*58, y+48+(i//3)*40, 50, 30, "#fff", INK, 3) + f'<line x1="{x+46+(i%3)*58}" y1="{y+60+(i//3)*40}" x2="{x+82+(i%3)*58}" y2="{y+60+(i//3)*40}" stroke="{MID}" stroke-width="2"/><line x1="{x+46+(i%3)*58}" y1="{y+68+(i//3)*40}" x2="{x+74+(i%3)*58}" y2="{y+68+(i//3)*40}" stroke="{MID}" stroke-width="2"/>' for i in range(6))
   + box(x+230, y+48, 80, 60, "none", INK, 6, 2, "5 4") + t(x+270, y+82, "REAL", 11, "bold", a="middle")
   + box(x+230, y+120, 80, 60, "none", INK, 6, 2, "5 4") + t(x+270, y+154, "FAKE", 11, "bold", a="middle")
   + t(x+40, y+170, "you: 4 / 6 right", 11, "bold") + t(x+40, y+188, "57 of 100 struggle too", 10, "bold", ORA),
  "The reader sorts 6 headlines into real and fake", "… and then sees their score next to the 57 of 100"),
 ("4 · Estimate", lambda x, y: t(x+40, y+56, "How many of 100 Americans?", 12, "bold")
   + box(x+40, y+76, 260, 26, "#fafafa", INK, 4) + f'<rect x="{x+40}" y="{y+76}" width="{260*0.35:.0f}" height="26" rx="4" fill="{MID}"/>' + t(x+40+260*0.35+6, y+94, "your guess 35", 11)
   + box(x+40, y+122, 260, 26, "#fafafa", INK, 4) + f'<rect x="{x+40}" y="{y+122}" width="{260*0.57:.0f}" height="26" rx="4" fill="{ORA}"/>' + t(x+40+260*0.57+6, y+140, "real 57", 11, "bold", ORA)
   + f'<path d="M{x+130} {y+180} l18 -14 l6 8 z" fill="{INK}"/>' + t(x+160, y+186, "draw the bar", 10, fill=MID),
  "The reader draws how many Americans struggle with fakes", "… and then sees the real 57 next to their guess"),
 ("5 · Hold", lambda x, y: phone(x, y) + f'<rect x="{cx(x)-48}" y="{y+52}" width="96" height="100" rx="4" fill="{LIGHT}" filter="url(#blur)"/>'
   + t(cx(x), y+108, "~ blurred ~", 11, fill=MID, a="middle") + f'<circle cx="{cx(x)}" cy="{y+178}" r="14" fill="none" stroke="{INK}" stroke-width="2"/><circle cx="{cx(x)}" cy="{y+178}" r="6" fill="{INK}"/>'
   + t(cx(x), y+212, "hold to unblur", 10, fill=MID, a="middle"),
  "The reader holds down to slowly unblur an image", "… and then sees \"57 of 100 couldn't tell either\""),
 ("6 · Wait (new)", lambda x, y: phone(x, y) + box(cx(x)-50, y+56, 92, 40, "#e8f0fb", BLU, 10, 1.5) + t(cx(x)-44, y+73, "Friend:", 10, "bold", BLU)
   + t(cx(x)-44, y+88, "look at this 😳", 10) + box(cx(x)-50, y+104, 92, 60, LIGHT, MID, 6) + f'<path d="M{cx(x)-12} {y+120} l22 14 l-22 14 z" fill="{MID}"/>'
   + t(cx(x), y+188, "57 of 100 had", 10, "bold", ORA, "middle") + t(cx(x), y+202, "this moment", 10, "bold", ORA, "middle"),
  "The reader gets a fake \"message from a friend\" with a video", "… and then sees 57 of 100 Americans had this moment"),
]
body = ""
for i, (title, draw, l1, l2) in enumerate(F):
    x, y = X0 + (i % 3) * (FW + GX), Y0 + (i // 3) * (FH + GY)
    body += box(x, y, FW, FH, "#fff", INK, 4) + t(x + 10, y + 22, title, 15, "bold") + draw(x, y)
    body += t(x + 4, y + FH + 20, l1, 12, "bold") + t(x + 4, y + FH + 37, l2, 12, fill="#555")
svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" font-family="Helvetica,Arial,sans-serif">'
       '<defs><filter id="blur"><feGaussianBlur stdDeviation="3"/></filter></defs>'
       f'<rect width="{W}" height="{H}" fill="#fff"/>{t(24, 36, "Crazy 6s · one aspect, six interactions", 22, "bold")}'
       f'{t(24, 60, "Aspect: 57 of 100 Americans have seen people struggling to tell real from fake (Americans on AI)", 13, fill="#555")}'
       f'{box(W-330, 18, 306, 46, "#fff4e5", ORA, 6, 1.5)}{t(W-318, 37, "DIGITAL REFERENCE, NOT THE PAPER SHEET", 12, "bold", ORA)}'
       f'{t(W-318, 55, "Redraw by hand, one minute per box.", 11, fill="#555")}{body}</svg>')
(HERE / "wireframes" / "crazy6.svg").write_text(svg, encoding="utf-8")
print("wrote wireframes/crazy6.svg")
