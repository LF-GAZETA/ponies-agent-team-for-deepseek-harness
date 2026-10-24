#!/usr/bin/env python3
"""Generate the collection-level placeholder banner (workspace root ./assets/cover.png).

This intentionally does NOT touch the per-package banners (their bytes are recorded
in the package manifests / zips).
"""
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
W, H = 1280, 640


def font(size: int, bold: bool = False):
    candidates = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
    ]
    for c in candidates:
        try:
            return ImageFont.truetype(c, size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)


img = Image.new("RGB", (W, H))
px = img.load()
c1, c2, c3 = (16, 20, 46), (44, 32, 96), (132, 62, 148)
for y in range(H):
    for x in range(W):
        t = (x / W) * 0.65 + (y / H) * 0.35
        if t < 0.5:
            k = t / 0.5
            col = tuple(int(c1[i] + (c2[i] - c1[i]) * k) for i in range(3))
        else:
            k = (t - 0.5) / 0.5
            col = tuple(int(c2[i] + (c3[i] - c2[i]) * k) for i in range(3))
        px[x, y] = col

d = ImageDraw.Draw(img, "RGBA")
rnd = random.Random(20261024)
for _ in range(320):
    x, y = rnd.randrange(W), rnd.randrange(H)
    r = rnd.choice([1, 1, 1, 2, 2, 3])
    d.ellipse([x, y, x + r, y + r], fill=(255, 250, 230, rnd.randrange(70, 220)))


def center(text, y, f, fill=(255, 255, 255, 255)):
    bbox = d.textbbox((0, 0), text, font=f)
    d.text(((W - (bbox[2] - bbox[0])) / 2, y), text, font=f, fill=fill)


center("PONIES AGENT TEAM · P.A.T. COLLECTION", 70, font(24, True), (216, 194, 255, 255))
center("Ponies Agent Team", 118, font(78, True), (255, 255, 255, 255))
center("Collection — v1.1 · P.A.T.", 234, font(42, True), (255, 214, 245, 255))
center("plus-95c   ·   lite-18c", 306, font(38, True), (255, 255, 255, 255))
center("95 + 18 characters  ·  7 + 2 volume teams  ·  17 fields per character", 382, font(25), (226, 224, 255, 255))
center("19 + 9 language patches  ·  7 + 5 global Leads", 420, font(25), (226, 224, 255, 255))
center("IMAGE PLACEHOLDER · replace ./assets/cover.png", 500, font(22), (205, 205, 235, 225))

d.rectangle([14, 14, W - 15, H - 15], outline=(255, 255, 255, 90), width=2)
out = ROOT / "assets" / "cover.png"
out.parent.mkdir(parents=True, exist_ok=True)
img.save(out, "PNG")
print("wrote", out, img.size)
