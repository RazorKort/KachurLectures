# -*- coding: utf-8 -*-
"""Сборка decks/glava12-teal.html — глава 12 «Характеристики компьютерных сетей»."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _g12_style import CSS
from _g12_engine import JS
from _g12_lib import SL, background
import _g12_s1
import _g12_s2

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "glava12-teal.html")

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
  <span class="hint" style="font-size:11.5px;color:#8aa8a2">← → шаги · ↑ ↓ слайды · цифры · R прогон · Esc содержание</span>
</div>
<div id="toc"><h2>Содержание</h2><div id="tocg"></div></div>
"""


def main():
    _g12_s1.build()
    _g12_s2.build()

    html = (
        '<!doctype html>\n<html lang="ru">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>Характеристики компьютерных сетей — глава 12</title>\n'
        '<style>' + CSS + '</style>\n</head>\n<body>\n'
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
