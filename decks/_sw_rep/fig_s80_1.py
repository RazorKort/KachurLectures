# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _figkit_s65 import *  # noqa
"""Рис. 2.6.1.3.1 — начальное подключение по Web-интерфейсу (VLAN 1)."""
W, H, TOP = 1040, 436, 0
_dev = laptop(10, 88, 160, rot=-8) + switch(690, 135, 170, 190, "SW-1")
_ln = line(170, 233, 690, 235, "#cfe0ff", 4) + dot(690, 235, 17, C, True)
_svi = line(770, 172, 770, 103, "#cfe0ff", 4) + line(718, 103, 822, 103, "#cfe0ff", 4) + dot(770, 172, 17, C, True)
_pk = ('<g><rect x="-30" y="-14" width="60" height="28" rx="4" fill="#2ad4ff"/><text x="0" y="5" text-anchor="middle" font-family="JetBrains Mono,monospace" font-size="13" font-weight="700" fill="#06203f">HTTP</text>'
       '<animateMotion dur="2.6s" repeatCount="indefinite" path="M180,233 L680,235"/></g>')
HTML = CSS + layer(W, H, _dev, step=False) + layer(W, H, _ln)     + t(138, 278, "IP add: 192.168.1.2/24", 24, step=True) + t(638, 172, "Gi1/0/1", 24, "#fff", True, step=True)     + layer(W, H, _svi) + t(770, 72, "VLAN 1", 24, "#fff", True, "c", True) + t(600, 32, "IP add: 192.169.1.239 /24", 24, step=True)     + layer(W, H, _pk)     + '<div class="fgk-cap" style="top:393px;font-size:20px">Рисунок 2.6.1.3.1 Начальное подключение по Web-интерфейсу</div>'
