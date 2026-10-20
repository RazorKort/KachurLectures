# -*- coding: utf-8 -*-
"""Сборка деки «Сетевые устройства 2.1» из модулей _el2/sNNN_NNN.py."""
import sys, pathlib, importlib, glob, os

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "_el2"))
from _el2_lib import build  # noqa: E402

try:
    from order import ORDER  # _el2/order.py: список ref в порядке лекции
except Exception:
    ORDER = []

mods = sorted(os.path.basename(p)[:-3] for p in glob.glob(str(HERE / "_el2" / "s*.py")))
found = {}
for name in mods:
    try:
        m = importlib.import_module(name)
    except Exception as e:  # чужой модуль в процессе правки не должен валить сборку
        print("ОШИБКА в", name, e)
        continue
    for ref, label, html in m.SLIDES:
        if ref in found:
            print("дубль:", ref, "в", name)
        found[ref] = (label, html)

# слайды, где анимация объясняет суть: шаги листаются вручную; остальные проигрываются сами
MANUAL = {"p020", "p054", "p045", "p001", "p016", "p060", "p024", "p058", "p059", "p011",
          "p074", "p074b", "p067", "p026", "p077", "p014", "p047", "p028", "p053", "p055", "p041",
          "p039", "p009", "p019", "p072", "p029", "p034", "p033", "p036"}

import re

MINPX = 21.0   # нижняя граница кегля на холсте 1920 (на экране 1280 это ~14px)


def _grow(v):
    """мелкое поднимаем до MINPX, среднее — чуть увеличиваем, крупное не трогаем"""
    if v < MINPX:
        return MINPX
    if v < 26:
        return round(v + 1.5, 1)
    return v


def bump(html):
    """Крупнее мелкий и средний текст: мелкий кегль на проекторе не читается."""
    html = re.sub(r'font-size:(\d+(?:\.\d+)?)px',
                  lambda m: 'font-size:%gpx' % _grow(float(m.group(1))), html)
    # кегли в SVG-подписях задаются атрибутом
    html = re.sub(r'font-size="(\d+(?:\.\d+)?)"',
                  lambda m: 'font-size="%g"' % _grow(float(m.group(1))), html)
    # жёсткая высота карточки режет выросший текст — пускаем её расти вниз
    def _soft(tag):
        t = tag.group(0)
        if 'class="card' not in t:
            return t
        return re.sub(r'(?<![a-z-])height:(\d+)px', r'min-height:\1px', t)

    html = re.sub(r'<div\s[^>]*>', _soft, html)
    return html

SKIP = {"p037"}  # заменён титулом
order = [r for r in ORDER if r in found] + sorted(r for r in found if r not in ORDER and r not in SKIP)
# фон по блокам лекции (номера слайдов pptx, с которых начинается блок)
from pptxmap import PPTX
_STARTS = [1, 7, 19, 35, 54, 65]
BLOCK = {r: sum(n >= s for s in _STARTS) - 1 for r, n in PPTX}
ICE = ["ice1.jpg", "ice3.jpg", "ice4.jpg", "ice5.jpg", "ice6.jpg", "ice2.jpg"]
slides = []
for r in order:
    label, html = found[r]
    slides.append((label, bump(html), "0" if r in MANUAL else "1", BLOCK.get(r, 0) % len(ICE)))
n, size = build(slides, os.environ.get("EL2_OUT", str(HERE / "eltex-devices-2.html")),
                assets_dir=str(HERE / "_el2assets"), bg="bg.jpg", ftl="aura_tl.png", fbr="aura_br.png", ice=ICE)
print(f"{n} слайдов, {size/1024/1024:.1f} МБ")
print("нет в ORDER:", [r for r in found if r not in ORDER])
