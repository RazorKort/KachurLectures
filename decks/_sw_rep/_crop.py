# -*- coding: utf-8 -*-
"""Вырезка из инфографики: python _sw_rep/_crop.py snap x0 y0 x1 y1 snap_ico_doc.png
Координаты в пикселях оригинала 1672x941 (полное разрешение из pptx). Результат: _sw_assets/rep/<файл>, в HTML: img('rep/<файл>', 'left:..px;top:..px;width:..px', 'ab')."""
import sys, pathlib
from PIL import Image
D = pathlib.Path(__file__).resolve().parent.parent
n, x0, y0, x1, y1, out = sys.argv[1], *map(int, sys.argv[2:6]), sys.argv[6]
import json
src = json.load(open(D / "_sw_rep" / "_src.json"))
im = (Image.open(D / "_swref" / "media" / src[n]) if n in src else (Image.open(D / "_sw_assets" / f"{n}.webp") if n.startswith("fig_") else Image.open(D / "_sw_assets" / f"{n}.webp").resize((1672, 941)))).convert("RGBA")
c = im.crop((x0, y0, x1, y1)); c.save(D / "_sw_assets" / "rep" / out)
print(out, c.size)
