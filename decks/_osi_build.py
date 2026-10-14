# -*- coding: utf-8 -*-
"""Сборка decks/praktika-osi.html — учебная практика «Путь данных по модели OSI»."""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from _osi_style import CSS
from _osi_engine import JS
from _osi_lib import SEC, NAV

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "praktika-osi.html")

PARTS = ["_osi_p1", "_osi_p2", "_osi_p3"]


def main() -> None:
    for name in PARTS:
        try:
            mod = __import__(name)
        except ImportError:
            print("пропуск:", name)
            continue
        for fn in sorted(f for f in dir(mod) if f.startswith("build_")):
            getattr(mod, fn)()

    nav = '<div id="nav"><b>Практика OSI</b>' + "".join(
        '<a href="#%s">%s</a>' % (i, t) for i, t in NAV) + "</div>"

    html = (
        '<!doctype html>\n<html lang="ru">\n<head>\n'
        '<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n'
        '<title>Практика: путь данных по модели OSI</title>\n'
        '<style>' + CSS + '</style>\n</head>\n<body>\n'
        '<div id="bg"></div>\n'
        '<div id="top"><div id="prog"></div>' + nav + '</div>\n'
        '<main id="page">\n' + "\n".join(SEC) + '\n'
        '<div class="foot"><b>Практика по дисциплине «Сети и системы передачи информации»</b>'
        '<span>Ананко · Качур</span><span>VK · Telegram</span></div>\n'
        '</main>\n'
        '<script>' + JS + '</script>\n</body>\n</html>\n'
    )

    with open(OUT, "w", encoding="utf-8") as f:
        f.write(html)

    print("секций:", len(SEC))
    print("размер:", round(len(html.encode("utf-8")) / 1024, 1), "КБ")
    print("файл:  ", OUT)


if __name__ == "__main__":
    main()
