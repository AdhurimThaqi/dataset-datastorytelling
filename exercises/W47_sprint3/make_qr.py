"""QR codes for a live round (v8): the audience scans it and plays in the same room.

Run:  python make_qr.py            -> room "hslu"
      python make_qr.py final      -> room "final"
Writes qr/qr-<room>.png (for slides), qr/qr-<room>.svg (for print) and qr/slide-<room>.png (a ready 16:9 slide).
The projector page live.html?room=<room> shows the same QR code and the live leaderboard.
"""
import re
import sys
from pathlib import Path

import qrcode
import qrcode.image.svg
from PIL import Image, ImageDraw, ImageFont

BASE = "https://adhurimthaqi.github.io/dataset-datastorytelling/exercises/W47_sprint3/v8.html"
HERE = Path(__file__).parent
room = (sys.argv[1] if len(sys.argv) > 1 else "hslu").lower()
if not re.fullmatch(r"[a-z0-9-]{2,24}", room):
    raise SystemExit("room code: 2-24 characters, a-z, 0-9 or -")
url = f"{BASE}?room={room}"
out = HERE / "qr"; out.mkdir(exist_ok=True)


def make(factory=None):
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=24, border=4, image_factory=factory)
    q.add_data(url); q.make(fit=True)
    return q.make_image()


make(qrcode.image.svg.SvgPathImage).save(out / f"qr-{room}.svg")
qr = make().convert("RGB")
qr.save(out / f"qr-{room}.png")

# a ready slide: 1920x1080, title left, QR right
W, H = 1920, 1080
slide = Image.new("RGB", (W, H), (243, 242, 237))
d = ImageDraw.Draw(slide)
font = lambda size, bold=True: ImageFont.truetype("C:/Windows/Fonts/" + ("segoeuib.ttf" if bold else "segoeui.ttf"), size)
d.text((140, 250), "Real or AI?", font=font(150), fill=(20, 21, 27))
d.text((146, 450), "Scan to play on your phone.", font=font(58, False), fill=(84, 86, 95))
d.text((146, 530), "Same pictures for everyone,", font=font(58, False), fill=(84, 86, 95))
d.text((146, 610), "about 4 minutes.", font=font(58, False), fill=(84, 86, 95))
d.text((146, 760), f"Room {room.upper()}", font=font(52), fill=(122, 79, 240))
size = 720
card = Image.new("RGB", (size + 60, size + 60), "white")
card.paste(qr.resize((size, size), Image.NEAREST), (30, 30))
mask = Image.new("L", card.size, 0); ImageDraw.Draw(mask).rounded_rectangle((0, 0, *card.size), radius=40, fill=255)
slide.paste(card, (W - card.width - 140, (H - card.height) // 2), mask)
slide.save(out / f"slide-{room}.png")
print("room", room, "->", url)
print("wrote", *(f"qr/{n}" for n in (f"qr-{room}.png", f"qr-{room}.svg", f"slide-{room}.png")))
