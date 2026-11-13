#!/usr/bin/env python3
"""Draw entry.png for news-image-01: a newspaper front-page collage of
13 November 2026's five big stories. Everything is drawn in code with
Pillow; no copied assets."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (245, 240, 226)
INK = (20, 20, 28)
NAVY = (16, 32, 64)
RED = (178, 34, 34)
GREEN = (34, 120, 60)
BLUE = (28, 90, 160)
ORANGE = (230, 110, 20)
GOLD = (200, 160, 40)

F_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
F_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(F_B if bold else F_R, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)

# ---- Masthead -------------------------------------------------------
d.rectangle([0, 0, W, 158], fill=NAVY)
d.rectangle([0, 158, W, 164], fill=GOLD)
d.text((W // 2, 52), "THE WORLD IN ONE DAY", font=font(30), fill=(200, 200, 210), anchor="mm")
d.text((W // 2, 108), "13 NOVEMBER 2026", font=font(64), fill=(255, 255, 255), anchor="mm")

M = 24          # outer margin
G = 16          # gutter
COL = (W - 2 * M - G) // 2   # 488
ROW1_Y, ROW1_H = 184, 300
ROW2_Y, ROW2_H = 500, 300
ROW3_Y, ROW3_H = 816, 184


def panel(x, y, w, h, head, head_color):
    d.rectangle([x, y, x + w, y + h], outline=INK, width=3, fill=(255, 255, 255))
    d.rectangle([x, y, x + w, y + 44], fill=head_color)
    d.text((x + 12, y + 22), head, font=font(22), fill=(255, 255, 255), anchor="lm")
    return x, y + 44, w, h - 44


def caption(x, y, w, text, size=21):
    lines = wrap(d, text, font(size, bold=False), w - 20)
    yy = y + 6
    for ln in lines:
        d.text((x + 10, yy), ln, font=font(size, bold=False), fill=INK)
        yy += size + 5
    return yy


# ---- Panel 1: Nvidia (top-left) ------------------------------------
px, py, pw, ph = panel(M, ROW1_Y, COL, ROW1_H, "1  NVIDIA CHIEF RESIGNS", (20, 70, 40))
# chip
d.rounded_rectangle([px + 24, py + 18, px + 150, py + 128], 10, fill=(24, 90, 50), outline=INK, width=2)
for i in range(3):
    d.line([px + 44 + i * 34, py + 8, px + 44 + i * 34, py + 18], fill=INK, width=4)
    d.line([px + 44 + i * 34, py + 128, px + 44 + i * 34, py + 138], fill=INK, width=4)
d.text((px + 87, py + 73), "NVDA", font=font(30), fill=(255, 255, 255), anchor="mm")
# falling chart
pts = [(px + 190, py + 30), (px + 250, py + 45), (px + 310, py + 42),
       (px + 370, py + 90), (px + 430, py + 120)]
d.line(pts, fill=RED, width=6)
d.polygon([(px + 430, py + 120), (px + 448, py + 112), (px + 438, py + 134)], fill=RED)
d.text((px + 330, py + 168), "-14%", font=font(52), fill=RED, anchor="mm")
caption(px, py + 196, pw, "Jensen Huang quits amid scandal; shares plunge and Wall Street falls.")

# ---- Panel 2: Hormuz oil (top-right) -------------------------------
px, py, pw, ph = panel(M + COL + G, ROW1_Y, COL, ROW1_H, "2  HORMUZ SHOCK", (140, 60, 10))
# sea + tanker
d.rectangle([px + 16, py + 120, px + pw - 16, py + 170], fill=(40, 110, 180))
d.rectangle([px + 70, py + 80, px + 320, py + 122], fill=(60, 60, 66))
d.rectangle([px + 250, py + 48, px + 300, py + 80], fill=(60, 60, 66))
d.line([px + 70, py + 122, px + 320, py + 122], fill=(200, 60, 40), width=4)
# explosion burst
cx, cy = px + 380, py + 70
for r, c in [(46, ORANGE), (34, (255, 190, 40)), (20, (255, 240, 150))]:
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c)
d.text((px + 330, py + 168), "$95.82  +3.3%", font=font(40), fill=RED, anchor="mm")
caption(px, py + 196, pw, "Explosions hit oil tankers in the Strait of Hormuz; Brent crude jumps.")

# ---- Panel 3: Ukraine talks (middle-left) ---------------------------
px, py, pw, ph = panel(M, ROW2_Y, COL, ROW2_H, "3  TALKS RISE IN DUBLIN", (20, 60, 130))
# dove (simple white bird shape)
d.ellipse([px + 60, py + 60, px + 200, py + 120], fill=(255, 255, 255), outline=INK, width=2)
d.polygon([(px + 120, py + 62), (px + 170, py + 20), (px + 185, py + 64)], fill=(255, 255, 255), outline=INK)
d.polygon([(px + 60, py + 88), (px + 18, py + 78), (px + 60, py + 104)], fill=(255, 255, 255), outline=INK)
d.ellipse([px + 178, py + 70, px + 188, py + 80], fill=INK)
# handshake arcs (two clasped hands, simplified)
d.arc([px + 250, py + 30, px + 440, py + 140], 200, 340, fill=INK, width=6)
d.arc([px + 250, py + 30, px + 440, py + 140], 20, 160, fill=INK, width=6)
d.text((px + 345, py + 168), "PEACE TALKS", font=font(36), fill=BLUE, anchor="mm")
caption(px, py + 196, pw, "US envoys meet Zelensky in Dublin; Europe backs the peace push.")

# ---- Panel 4: Trump tariffs (middle-right) --------------------------
px, py, pw, ph = panel(M + COL + G, ROW2_Y, COL, ROW2_H, "4  TARIFFS DOUBLED?", (150, 30, 30))
# tariff wall bars
for i, c in enumerate([(178, 34, 34), (255, 255, 255), (28, 60, 140)]):
    d.rectangle([px + 60 + i * 110, py + 40, px + 150 + i * 110, py + 130],
                fill=c, outline=INK, width=3)
d.text((px + 115, py + 85), "$", font=font(44), fill=(255, 255, 255), anchor="mm")
d.text((px + 225, py + 85), "%", font=font(44), fill=INK, anchor="mm")
d.text((px + 335, py + 85), "x2", font=font(44), fill=(255, 255, 255), anchor="mm")
d.text((px + 244, py + 168), "ON MEXICO", font=font(36), fill=RED, anchor="mm")
caption(px, py + 196, pw, "Trump threatens to double tariffs on Mexico in a new trade warning.")

# ---- Panel 5: Outlook outage (bottom, full width) -------------------
px, py, pw, ph = panel(M, ROW3_Y, W - 2 * M, ROW3_H, "5  OUTLOOK GOES DARK IN 74 COUNTRIES", (60, 60, 90))
# envelope with X
d.rectangle([px + 30, py + 34, px + 190, py + 120], fill=(0, 120, 215), outline=INK, width=3)
d.line([px + 30, py + 34, px + 110, py + 82, px + 190, py + 34], fill=(255, 255, 255), width=5)
d.line([px + 30, py + 120, px + 190, py + 120], fill=(255, 255, 255), width=3)
d.line([px + 70, py + 55, px + 150, py + 105], fill=RED, width=10)
d.line([px + 150, py + 55, px + 70, py + 105], fill=RED, width=10)
d.text((px + 330, py + 60), "74 COUNTRIES", font=font(48), fill=RED)
d.text((px + 330, py + 112), "Microsoft / Outlook outage knocks out mail worldwide.",
        font=font(24, bold=False), fill=INK)

# footer
d.text((W // 2, 1006), "THE DAY IN ONE PICTURE  •  ALL FIVE STORIES  •  13 NOVEMBER 2026",
       font=font(18, bold=False), fill=(90, 90, 90), anchor="mm")

img.save("entry.png", optimize=True)
print("saved entry.png")
