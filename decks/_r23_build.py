# -*- coding: utf-8 -*-
"""Сборка decks/marshrutizatory.html — лекция «Маршрутизаторы» (глава 2.3)."""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _r23_style import CSS
from _r23_engine import JS
from _r23_lib import SL, background, global_defs

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "marshrutizatory.html")

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

MODULES = ["_r23_s1", "_r23_s2", "_r23_s3", "_r23_s4", "_r23_s5", "_r23_s6"]


def main():
    for name in MODULES:
        try:
            mod = __import__(name)
        except ImportError as e:
            print("· модуль %s пока не создан (%s) — пропускаю" % (name, e))
            continue
        mod.build()

    html = (
        '<!doctype html>\n<html lang="ru">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>Маршрутизаторы — лекция 2.3</title>\n'
        "<style>%s</style>\n</head>\n<body>\n" % CSS
        + background()
        + global_defs()
        + '\n<div id="stage">\n' + "\n".join(SL) + "\n</div>\n"
        + HUD
        + "\n<script>%s</script>\n</body>\n</html>\n" % JS
    )
    with io.open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("готово: %s — %d слайдов, %.2f МБ"
          % (OUT, len(SL), os.path.getsize(OUT) / 1048576.0))


if __name__ == "__main__":
    main()
