# -*- coding: utf-8 -*-
"""Сверка вёрстки 1:1: python _sw_rep/_cmp.py snap hub ... -> _sw_rep/_cmp/<имя>.jpg (сверху оригинал, снизу вёрстка, все шаги видны)."""
import sys, os, pathlib, subprocess, tempfile, re
from PIL import Image
from playwright.sync_api import sync_playwright
D = pathlib.Path(__file__).resolve().parent.parent
OUT = D / "_sw_rep" / "_cmp"; OUT.mkdir(exist_ok=True)
tmp = pathlib.Path(tempfile.gettempdir()) / f"sw_cmp_{os.getpid()}.html"
r = subprocess.run([sys.executable, str(D / "_sw_build.py")], cwd=D, capture_output=True, text=True, encoding="utf-8",
                   env={**os.environ, "PYTHONIOENCODING": "utf-8", "SW_OUT": str(tmp)})
if r.returncode:
    print(r.stdout[-500:], r.stderr[-2000:]); sys.exit(1)
with sync_playwright() as pw:
    b = pw.chromium.launch(channel="chrome"); pg = b.new_page(viewport={"width": 1920, "height": 1080})
    pg.goto(tmp.as_uri()); pg.wait_for_timeout(1200)
    for name in sys.argv[1:]:
        k = pg.evaluate("n=>[...document.querySelectorAll('section.slide')].findIndex(s=>s.querySelector('[data-rep=\"'+n+'\"]'))", name)
        if k < 0:
            print("нет вёрстки/слайда", name); continue
        pg.evaluate("k=>document.querySelectorAll('#tocg .tocit')[k].click()", k)
        pg.wait_for_timeout(400)
        pg.add_style_tag(content='.step{opacity:1!important;transform:none!important}')
        pg.wait_for_timeout(1500)
        shot = OUT / f"_{name}.png"
        pg.locator(f'.slide.on [data-rep="{name}"] .repc').screenshot(path=str(shot))
        a = Image.open(D / "_sw_assets" / f"{name}.webp").convert("RGB").resize((1672, 941))
        c2 = Image.open(shot).convert("RGB"); c2 = c2.resize((1672, round(c2.height * 1672 / c2.width)))
        c = Image.new("RGB", (1672, 941 + 16 + c2.height), "red"); c.paste(a, (0, 0)); c.paste(c2, (0, 957))
        c.thumbnail((1500, 1800)); c.save(OUT / f"{name}.jpg", quality=85); shot.unlink()
        print("ok", name, "слайд", k + 1)
    b.close()
tmp.unlink()
