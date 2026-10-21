# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _figkit_s65 import *  # noqa
"""Схема: ПК1 и ПК2 в VLAN 10 на портах gi 1/0/1 и gi 1/0/2."""
W, H, TOP = 812, 690, 0
_dev = switch(270, 80, 200, 155) + pc_left(70, 350, 118) + pc_left(575, 370, 118)
_ln = line(312, 232, 182, 362, "#cfe0ff", 7) + line(428, 222, 588, 376, "#cfe0ff", 7)
_pk = ('<g><rect x="-26" y="-14" width="52" height="28" rx="4" fill="rgba(255,197,61,.25)" stroke="#ffc53d" stroke-width="2.5"/>'
       '<text x="0" y="5" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="13" font-weight="700" fill="#ffc53d">V10</text>'
       '<animateMotion dur="3.2s" repeatCount="indefinite" path="M182,362 L312,232 Q370,200 428,222 L588,376"/></g>')
HTML = CSS + layer(W, H, _dev, step=False) + layer(W, H, _ln)     + t(135, 222, "gi 1/0/1", 26, "#fff", True, step=True) + t(518, 222, "gi 1/0/2", 26, "#fff", True, step=True, delay=150)     + t(195, 534, "ПК1", 26, step=True) + t(195, 566, "VLAN 10", 24, Y, True, step=True)     + t(698, 534, "ПК2", 26, step=True, delay=150) + t(698, 566, "VLAN 10", 24, Y, True, step=True, delay=150)     + layer(W, H, _pk)
