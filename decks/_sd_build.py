# -*- coding: utf-8 -*-
"""Сборка decks/statika-dinamika.html — глава 2.5 «Статическая и динамическая маршрутизация»."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _sd_style import CSS
from _sd_engine import JS
from _sd_lib import SL, background, b64
import _sd_s1
import _sd_s2
import _sd_s3

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "statika-dinamika.html")

HUD = """
<div id="prog" style="width:0"></div>
<div id="hud">
  <button id="btoc" title="Содержание (Esc)">Содержание</button>
  <button id="bprev" title="Назад (←)">←</button>
  <button id="bnext" title="Вперёд (→)">→</button>
  <button id="brun" title="Прогон слайда (R)">Прогон</button>
  <button id="bspeed" title="Скорость прогона">1×</button>
  <span id="count">1 / 1</span>
  <span id="sname"></span>
  <span class="hint">← → шаги · ↑ ↓ слайды · Shift+← → кадры сцены · R прогон · Esc содержание</span>
</div>
<div id="toc"><h2>Содержание</h2><div id="tocg"></div></div>
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&'
         'family=Roboto+Condensed:wght@400;600;700&family=JetBrains+Mono:wght@500;600;700&'
         'display=swap" rel="stylesheet">')


def main():
    _sd_s1.build()
    _sd_s2.build()
    _sd_s3.build()

    html = (
        '<!doctype html>\n<html lang="ru">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>Статическая и динамическая маршрутизация</title>\n'
        + FONTS + '\n'
        '<style>' + CSS + ':root{--scenebg:url(' + b64("bg5.webp") + ')}</style>\n</head>\n<body>\n'
        + background() + '\n<div id="stage">\n' + "\n".join(SL) + '\n</div>\n'
        + HUD + '\n<script>' + JS + '</script>\n</body>\n</html>\n'
    )

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    print("slides:", len(SL))
    print("size:  ", round(len(html.encode("utf-8")) / 1024, 1), "КБ")
    print("out:   ", OUT)


if __name__ == "__main__":
    main()
