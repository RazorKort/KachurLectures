# -*- coding: utf-8 -*-
"""Сборка decks/ospf.html — лекция «Протокол OSPF» в кавайном розово-голубом стиле."""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _ospf_style import CSS
from _ospf_engine import JS
from _ospf_lib import SL, background

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ospf.html")

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

MODULES = ["_ospf_s1", "_ospf_s2", "_ospf_s3", "_ospf_s4", "_ospf_s5"]


def main():
    for name in MODULES:
        try:
            mod = __import__(name)
        except ImportError:
            print("· модуль %s пока не создан — пропускаю" % name)
            continue
        mod.build()

    html = (
        '<!doctype html>\n<html lang="ru">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>Протокол OSPF — лекция</title>\n'
        "<style>%s</style>\n</head>\n<body>\n" % CSS
        + background()
        + '\n<div id="stage">\n' + "\n".join(SL) + "\n</div>\n"
        + HUD
        + "\n<script>%s</script>\n</body>\n</html>\n" % JS
    )
    with io.open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("готово: %s — %d слайдов, %.2f МБ" % (OUT, len(SL), os.path.getsize(OUT) / 1048576.0))


if __name__ == "__main__":
    main()
