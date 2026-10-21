# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _figkit_s65 import *  # noqa
"""Рис. 2.6.1.3.4 — подключение по Web-интерфейсу в функционирующей сети (VLAN20)."""
W, H, TOP = 1144, 480, 0
_dev = laptop(50, 122, 165, rot=-8) + switch(735, 185, 210, 190, "SW-1")
_ln = line(225, 272, 740, 272, R, 4) + dot(740, 270, 17, R, True)
_svi = line(825, 212, 825, 146, R, 4) + line(778, 146, 878, 146, R, 4) + dot(825, 212, 17, R, True)
_pk = ('<g><rect x="-30" y="-14" width="60" height="28" rx="4" fill="#ff4d5e"/><text x="0" y="5" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="13" font-weight="700" fill="#fff">HTTP</text>'
       '<animateMotion dur="2.6s" repeatCount="indefinite" path="M235,272 L728,272"/></g>')
HTML = CSS + layer(W, H, _dev, step=False) + layer(W, H, _ln)     + t(192, 312, "IP add: 10.10.1.121/24", 24, step=True) + t(640, 212, "Gi1/0/2", 24, "#fff", True, step=True)     + layer(W, H, _svi) + t(825, 116, "VLAN20", 24, R, True, "c", True)     + t(678, 42, "IP add: 10.10.1.28 /24", 25, step=True) + t(678, 82, "DefGW: 10.10.1.1", 25, step=True)     + layer(W, H, _pk)     + '<div class="fgk-cap" style="top:425px;font-size:20px">Рисунок 2.6.1.3.4. – Подключение по Web-интерфейсу в функционирующей сети</div>'
