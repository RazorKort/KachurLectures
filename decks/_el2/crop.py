# -*- coding: utf-8 -*-
"""Вырезка из оригинала pptx: python _el2/crop.py 70 x0 y0 x1 y1 имя.png [--white]
Координаты — доли (0..1) от картинки слайда pptx №70 (_el2ref/s70.jpg, ~1672x941).
.png сохраняется с прозрачностью, если --white: близкий к фону светлый фон делается прозрачным по краям (для иконок)."""
import sys, pathlib
from PIL import Image
D = pathlib.Path(__file__).parent.parent
n, x0, y0, x1, y1, name = int(sys.argv[1]), *map(float, sys.argv[2:6]), sys.argv[6]
im = Image.open(D / "_el2ref" / f"s{n:02d}.jpg").convert("RGB")
W, H = im.size
c = im.crop((round(x0 * W), round(y0 * H), round(x1 * W), round(y1 * H)))
out = D / "_el2assets" / name
if name.lower().endswith(".png"):
    c = c.convert("RGBA")
    if "--white" in sys.argv:
        px = c.load()
        for y in range(c.size[1]):
            for x in range(c.size[0]):
                r, g, b, a = px[x, y]
                lum = min(r, g, b)
                if lum > 225 and max(r, g, b) - lum < 40:
                    px[x, y] = (r, g, b, max(0, int((255 - lum) * 255 / 30)))
    c.save(out, optimize=True)
else:
    c.save(out, quality=90)
print(out.name, c.size)
