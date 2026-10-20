# -*- coding: utf-8 -*-
"""Сверка: python _el2/compare.py p040 p005 ... -> _el2cmp/p040.jpg (слева оригинал pptx, справа дека, все шаги показаны).
Без аргументов — все слайды. Перед сверкой собирает деку."""
import sys, pathlib, subprocess
from PIL import Image
from playwright.sync_api import sync_playwright
HERE = pathlib.Path(__file__).parent
DECKS = HERE.parent
sys.path.insert(0, str(HERE))
from pptxmap import PPTX
import os, tempfile
DECK = pathlib.Path(tempfile.gettempdir()) / f"el2_cmp_{os.getpid()}.html"
r_ = subprocess.run([sys.executable, str(DECKS / "_el2_build.py")], capture_output=True, text=True, encoding="utf-8",
                    env={**os.environ, "EL2_OUT": str(DECK), "PYTHONIOENCODING": "utf-8"})
print(r_.stdout[-600:], r_.stderr[-1500:])
html = DECK.read_text(encoding="utf-8")
import re
labels = re.findall(r'<section class="[^"]*" data-label', html)
order = [r for r, _ in PPTX]
want = sys.argv[1:] or order
OUT = DECKS / "_el2cmp"; OUT.mkdir(exist_ok=True)
built = [r for r in order]  # индекс в деке = позиция в ORDER среди существующих
src = {}
for p in (HERE).glob("s*.py"):
    src.update({m: 1 for m in re.findall(r'"(p\d+\w?)"', p.read_text(encoding="utf-8"))})
present = [r for r in order if r in src]
from pptxmap import PPTX as _P

with sync_playwright() as pw:
    br = pw.chromium.launch(channel="chrome")
    pg = br.new_page(viewport={"width": 1920, "height": 1080})
    for r in want:
        if r not in present:
            print("нет слайда", r); continue
        k = present.index(r) + 1
        pg.goto(DECK.as_uri() + f"#{k}")
        pg.reload()
        pg.wait_for_timeout(300)
        pg.evaluate("""()=>{document.querySelectorAll('.slide.on [data-s]').forEach(e=>e.classList.add('in'));
          document.querySelectorAll('nav,#nav,.nav').forEach(e=>e.style.display='none')}""")
        pg.wait_for_timeout(1500)
        shot = OUT / f"_{r}.png"; pg.screenshot(path=str(shot))
        n = dict(PPTX)[r]
        a = Image.open(HERE.parent / "_el2ref" / f"s{n:02d}.jpg").convert("RGB").resize((1920, 1080))
        b = Image.open(shot).convert("RGB")
        c = Image.new("RGB", (1920, 2160 + 20), "red"); c.paste(a, (0, 0)); c.paste(b, (0, 1100))
        c.thumbnail((1500, 1700)); c.save(OUT / f"{r}.jpg", quality=85); shot.unlink()
        print("ok", r, "-> pptx", n)
    br.close()
DECK.unlink()
