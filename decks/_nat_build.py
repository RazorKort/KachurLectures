# -*- coding: utf-8 -*-
"""Сборка decks/ip-servisy-nat.html — лекция «IP-сервисы: DHCP, NAT, NTP» (раздел 2.6)."""
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _nat_style import CSS
from _nat_engine import JS
from _sw_lib import SL
from _nat_lib import background, sprite

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ip-servisy-nat.html")

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
         'family=Montserrat:wght@700;800;900&family=Golos+Text:wght@400;600;700;800&'
         'family=JetBrains+Mono:wght@400;700&display=swap">')

MODULES = ["_nat_s1", "_nat_s2", "_nat_s3", "_nat_s4", "_nat_s5", "_nat_s6", "_nat_s7", "_nat_s8"]


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

    html = (
        '<!doctype html>\n<html lang="ru">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        "<title>IP-сервисы: DHCP, NAT, NTP — лекция</title>\n"
        + FONTS + "\n"
        "<style>%s</style>\n</head>\n<body>\n" % CSS
        + sprite() + background()
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
