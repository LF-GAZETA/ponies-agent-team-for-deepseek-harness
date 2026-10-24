#!/usr/bin/env python3
"""Generate placeholder banner images for both packages (replaceable later)."""
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


def make_banner(out: Path, edition: str, detail: str) -> None:
    img = Image.new("RGB", (W, H))
    px = img.load()
    c1, c2, c3 = (18, 14, 42), (52, 26, 92), (120, 52, 140)
    for y in range(H):
        for x in range(W):
            t = (x / W) * 0.7 + (y / H) * 0.3
            if t < 0.5:
                k = t / 0.5
                col = tuple(int(c1[i] + (c2[i] - c1[i]) * k) for i in range(3))
            else:
                k = (t - 0.5) / 0.5
                col = tuple(int(c2[i] + (c3[i] - c2[i]) * k) for i in range(3))
            px[x, y] = col

    d = ImageDraw.Draw(img, "RGBA")
    rnd = random.Random(20261024)
    for _ in range(260):
        x, y = rnd.randrange(W), rnd.randrange(H)
        r = rnd.choice([1, 1, 1, 2, 2, 3])
        a = rnd.randrange(70, 220)
        d.ellipse([x, y, x + r, y + r], fill=(255, 250, 230, a))

    def center(text, y, f, fill=(255, 255, 255, 255)):
        bbox = d.textbbox((0, 0), text, font=f)
        d.text(((W - (bbox[2] - bbox[0])) / 2, y), text, font=f, fill=fill)

    center("PONIES AGENT TEAM · P.A.T.", 96, font(30, True), (216, 194, 255, 255))
    center("Ponies Agent Team", 158, font(82, True), (255, 255, 255, 255))
    center(edition, 272, font(42, True), (255, 214, 245, 255))
    center(detail, 348, font(27), (226, 224, 255, 255))
    center("IMAGE PLACEHOLDER · replace ./assets/cover.png", 432, font(24), (200, 200, 230, 220))
    center("95 characters · 7 volumes · 19 language patches · 7 global Leads"
           if "plus" in edition else "18 characters · 2 volumes · 9 language patches · 5 global Leads",
           476, font(24), (200, 200, 230, 220))

    # frame
    d.rectangle([14, 14, W - 15, H - 15], outline=(255, 255, 255, 90), width=2)
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out, "PNG")
    print("wrote", out, img.size)


make_banner(ROOT / "ponies-agent-team-v1.1-plus-95c" / "assets" / "cover.png",
            "v1.1-plus-95c",
            "G4 · Equestria Girls · G5 — complete character profiles")
make_banner(ROOT / "ponies-agent-team-v1.1-lite-18c" / "assets" / "cover.png",
            "v1.1-lite-18c",
            "G4 · Equestria Girls · G5 — compact edition")
