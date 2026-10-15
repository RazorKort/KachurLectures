# -*- coding: utf-8 -*-
"""Сборка decks/ospf.html — лекция «Протокол OSPF» в кавайном розово-голубом стиле."""
import base64
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _ospf_style import CSS
from _ospf_engine import JS
from _ospf_lib import SL, background, bg_css

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

FONTDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_ospf_assets", "fonts")
CYR = "U+0301,U+0400-045F,U+0490-0491,U+04B0-04B1,U+2116"
LAT = "U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD"


def fonts_css():
    """Встроенные шрифты: Oswald (заголовки) и Golos Text (текст), base64 — работают офлайн."""
    out = []
    for fam, base, wght in (("OspfHead", "oswald", "700"), ("OspfText", "golos", "400 900")):
        for part, rng in (("cyr", CYR), ("lat", LAT)):
            with open(os.path.join(FONTDIR, "%s-%s.woff2" % (base, part)), "rb") as fh:
                data = base64.b64encode(fh.read()).decode()
            out.append("@font-face{font-family:%s;font-style:normal;font-weight:%s;font-display:swap;"
                       "src:url(data:font/woff2;base64,%s) format('woff2');unicode-range:%s}"
                       % (fam, wght, data, rng))
    return "\n".join(out)


MODULES = ["_ospf_intro", "_ospf_dij", "_ospf_work", "_ospf_nbr", "_ospf_areas", "_ospf_cfg", "_ospf_s5"]


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
        "<style>%s\n%s</style>\n</head>\n<body>\n" % (fonts_css(), CSS + bg_css())
        + '\n<div id="stage">\n' + "\n".join(SL) + "\n</div>\n"
        + HUD
        + "\n<script>%s</script>\n</body>\n</html>\n" % JS
    )
    with io.open(OUT, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("готово: %s — %d слайдов, %.2f МБ" % (OUT, len(SL), os.path.getsize(OUT) / 1048576.0))


if __name__ == "__main__":
    main()
