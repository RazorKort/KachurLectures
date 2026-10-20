# -*- coding: utf-8 -*-
"""Сборка decks/kommutaciya.html — лекция «Коммутаторы и коммутация» (раздел 2.2)."""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _sw_style import CSS
from _sw_engine import JS
from _sw_lib import SL, background

OUT = os.environ.get("SW_OUT") or os.path.join(os.path.dirname(os.path.abspath(__file__)), "kommutaciya.html")

HUD = """
<div id="prog" style="width:0"></div>
<div id="hud">
  <button id="btoc" title="Содержание (Esc)">Содержание</button>
  <button id="bprev" title="Назад (←)">←</button>
  <button id="bnext" title="Вперёд (→)">→</button>
  <button id="brun" title="Прогон слайда (R)">Прогон</button>
  <button id="bspeed" title="Скорость">1×</button>
  <span id="count">1 / 1</span>
  <span id="sname"></span>
  <span class="hint">← → шаги · ↑ ↓ слайды · цифры · R прогон · Esc содержание · N/B шаги сцены</span>
</div>
<div id="toc"><h2>Содержание</h2><div id="tocg"></div></div>
"""

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?'
         'family=Oswald:wght@500;600;700&family=Golos+Text:wght@400;600;700;800&'
         'family=JetBrains+Mono:wght@400;700&display=swap">')

MODULES = ["_sw_s1", "_sw_s2", "_sw_s3", "_sw_s4", "_sw_s5", "_sw_s6", "_sw_s7", "_sw_s8"]


def main():
    for name in MODULES:
        try:
            mod = __import__(name)
        except ImportError as e:
            if name in str(e):
                print("· модуль %s пока не создан — пропускаю" % name)
                continue
            raise
        mod.build()
    import _sw_fig
    _sw_fig.apply()

    html = (
        '<!doctype html>\n<html lang="ru">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<title>Коммутаторы и коммутация — лекция</title>\n"
        + FONTS + "\n"
        "<style>%s</style>\n</head>\n<body>\n" % (CSS + __import__("_sw_fig").CSS)
        + background()
        + '\n<div id="stage">\n' + "\n".join(SL) + "\n</div>\n"
        + HUD
        + "\n<script>%s</script>\n</body>\n</html>\n" % (JS + __import__("_sw_fig").JS)
    )
    with io.open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("готово: %s — %d слайдов, %.2f МБ"
          % (OUT, len(SL), os.path.getsize(OUT) / 1048576.0))


if __name__ == "__main__":
    main()
