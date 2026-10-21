# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _figkit_s65 import *  # noqa
"""Рис. 2.6.1.2.1 — подключение к коммутатору по SSH."""
W, H, TOP = 1396, 646, 0
CURVE = "M290,510 C420,600 900,600 1135,500"
_net = (path("M245,215 V400", "#cfe0ff", 3) + path("M215,205 C175,280 180,360 200,395", C, 7)
        + line(318, 455, 445, 455, "#cfe0ff", 3))
_dev = laptop(110, 62, 165, rot=-8) + cloud(95, 385, 235, 140) + router(445, 380, 180, 145, "R1") + switch(1125, 370, 185, 160, "SW-1")
_trunk = ('<rect x="618" y="418" width="517" height="54" fill="rgba(255,77,94,.22)" stroke="rgba(255,77,94,.55)" stroke-width="1.5"/>'
          + line(618, 440, 1135, 440, "#cfe0ff", 3) + line(618, 456, 1135, 456, R, 4) + dot(618, 460, 15, R, True))
_svi = line(1195, 382, 1195, 323, R, 4) + line(1145, 323, 1243, 323, R, 4) + dot(1195, 382, 15, R, True)
_ssh = (path(CURVE, C, 7) + harrow(1100, 512, 1142, 497, C, 7)
        + '<g><rect x="-22" y="-14" width="44" height="28" rx="4" fill="#ffc53d"/><text x="0" y="6" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="14" font-weight="700" fill="#10213f">SSH</text>'
          '<animateMotion dur="3s" repeatCount="indefinite" path="M200,395 C180,450 230,480 290,510 C420,600 900,600 1135,500"/></g>')
HTML = CSS + layer(W, H, _net + _dev, step=False) + layer(W, H, _trunk) + t(625, 482, "Gi1/0/1.20", 22, "#fff", True, step=True)     + t(625, 512, "IP add: 10.10.1.1", 22, step=True) + t(1010, 392, "Gi1/0/24", 22, "#fff", True, step=True)     + layer(W, H, _svi, delay=100) + t(1195, 297, "VLAN20", 22, R, True, "c", True)     + t(1060, 230, "IP add: 10.10.1.28 /24", 24, step=True) + t(1060, 262, "DefGW: 10.10.1.1", 24, step=True)     + t(210, 440, "Internet", 30, "#fff", anchor="c") + layer(W, H, _ssh)     + '<div class="fgk-cap" style="top:620px;font-size:21px">Рисунок 2.6.1.2.1 – Подключение к коммутатору по протоколу SSH</div>'
