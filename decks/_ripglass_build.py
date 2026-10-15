# -*- coding: utf-8 -*-
"""Сборка decks/rip-glass.html — та же лекция о RIP в стеклянном стиле.

Контент берётся из тех же модулей слайдов, что и rip.html; различаются
оформление (CSS) и сцена (градиентная аврора со стеклянными пластинами).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _ripglass_style import CSS, background, tint, pick_bg
from _rip_engine import JS
import _rip_lib
import _rip_s1
import _rip_s2
import _rip_s3

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rip-glass.html")

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
  <span class="hint">← → шаги · ↑ ↓ слайды · цифры · R прогон · Esc содержание</span>
</div>
<div id="toc"><h2>Содержание</h2><div id="tocg"></div></div>
"""


def main():
    del _rip_lib.SL[:]
    _rip_s1.build()
    _rip_s2.build()
    _rip_s3.build()

    html = (
        '<!doctype html>\n<html lang="ru">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>RIP — стеклянная дека</title>\n'
        '<style>' + CSS + '</style>\n</head>\n<body>\n' + _rip_lib.SPRITE + '\n'
        + background() + '\n<div id="stage">\n'
        + tint("\n".join(_rip_lib.with_bg(_rip_lib.SL, pick_bg))) + '\n</div>\n'
        + HUD + '\n<script>' + JS + '</script>\n</body>\n</html>\n'
    )

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    print("slides:", len(_rip_lib.SL))
    print("size:  ", round(len(html.encode("utf-8")) / 1024, 1), "КБ")
    print("out:   ", OUT)


if __name__ == "__main__":
    main()
