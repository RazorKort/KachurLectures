# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _figkit_s65 import *  # noqa
"""Рис. 2.5.4.2.3 — транковый порт с нативной VLAN 20: ПК шлёт кадр без метки, телефон добавляет голосовой трафик с меткой."""
W, H, TOP = 1350, 494, 0
CSS2 = """<style>
@keyframes s65-fly{0%{transform:translateX(0);opacity:0}10%,85%{opacity:1}100%{transform:translateX(-300px);opacity:0}}
.s65-fl{position:absolute;animation:s65-fly 2.6s linear infinite}
.s65-fl svg{display:block}
</style>"""


def _env(x, y, col, delay=0):
    return layer(W, H, envelope(x, y, 85, 55, col), delay=delay)


def _fly(x, y, col, delay):
    return ('<div class="s65-fl" style="left:%dpx;top:%dpx;animation-delay:%dms"><svg width="52" height="34" class="fgk-gl">%s</svg></div>'
            % (x, y, delay, envelope(2, 2, 48, 30, col)))


_dev = switch(160, 140, 195, 170) + phone(650, 142, 120, 150) + pc(1065, 90, 135)
_lines = line(355, 256, 665, 258, "#cfe0ff", 4) + line(760, 256, 1070, 253, "#cfe0ff", 4) + dot(355, 252, 20, G, True)
HTML = CSS + CSS2 + layer(W, H, _dev, step=False) + layer(W, H, _lines)     + _env(880, 190, Y) + '<div class="step">' + _fly(1010, 232, Y, 0) + '</div>'     + _env(540, 190, Y) + _env(418, 190, R, 250) + '<div class="step">' + _fly(640, 232, Y, 0) + _fly(640, 232, R, 1300) + '</div>'     + t(362, 286, "Gi0/1", 22, "#fff", anchor="c", step=True) + t(362, 316, "Trunk", 22, "#fff", anchor="c", step=True)     + t(362, 346, "A100", 22, R, True, "c", True, 150) + t(362, 374, "N20", 22, Y, True, "c", True, 300)     + '<div class="fgk-cap" style="top:455px;font-size:21px">Рисунок 2.5.4.2.3. – Применение транкового порта с нативной VLAN 20</div>'
