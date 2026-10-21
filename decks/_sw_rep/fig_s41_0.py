# -*- coding: utf-8 -*-
"""fig_s41_0 — Рисунок 2.4.1.2: рассылка ARP-запроса на все порты коммутатора. Перерисовка в SVG."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fig_s40_0 as K

W, H, TOP = 1346, 762, 0
P = "s41"
SW = [(268, 95, 125, 100), (268, 255, 125, 100), (268, 420, 125, 100), (162, 565, 125, 100)]
COLS = [500, 705, 895]
ROWS = [(85, 60, 45), (245, 230, 200), (405, 395, 365)]
ARPS = [  # ряд, x, y, w, h
    (0, 360, 78, 165, 132), (0, 568, 14, 168, 136),
    (1, 360, 236, 165, 130), (1, 578, 205, 168, 132), (1, 762, 166, 152, 138),
    (2, 372, 395, 168, 130), (2, 578, 368, 168, 132), (2, 775, 336, 162, 132),
]


def _links():
    out = []
    for i, (sx, sy, _, _) in enumerate(SW[:3]):
        r1, r2, r3 = ROWS[i]; y0 = sy + 30
        out.append(K.poly([(sx + 108, y0), (475, r3 + 45), (COLS[2] + 20, r3 + 45)], K.C, 3, P + "-dw"))
        out.append(K.poly([(sx + 110, y0 + 12), (475, r2 + 30), (COLS[1] + 22, r2 + 30)], K.C, 3, P + "-dw"))
        out.append(K.poly([(sx + 112, y0 + 24), (COLS[0] + 22, r1 + 38)], K.C, 3, P + "-dw"))
    out.append(K.poly([(190, 590), (190, 160), (278, 160)], K.C, 3, P + "-dw"))
    out.append(K.poly([(212, 590), (212, 320), (278, 320)], K.C, 3, P + "-dw"))
    out.append(K.poly([(236, 590), (236, 490), (278, 490)], K.C, 3, P + "-dw"))
    return "".join(out)


def _pcs():
    return "".join(K.pc(P, COLS[j], ROWS[i][j], 95, 124) for i in range(3) for j in range(3))


def _arps(row):
    return "".join(f'<g style="animation-delay:{k * 350}ms" class="{P}-pop">' + K.arp(P, x, y, w, h, False, 18) + '</g>'
                   for k, (r, x, y, w, h) in enumerate(a for a in ARPS if a[0] == row))


HTML = K.css(P) + K.defs(P) + "".join([
    K.layer(W, H, P, _links() + "".join(K.sw(P, *s, label="SW L2") for s in SW)),
    K.layer(W, H, P, _pcs() + K.label(P, 1000, 120, "10.10.1.5") + K.label(P, 805, 172, "10.10.1.6")),
    K.layer(W, H, P, _arps(0)),
    K.layer(W, H, P, _arps(1)),
    K.layer(W, H, P, _arps(2)),
    f'<div class="{P}-cap step" style="left:205px;top:716px;font-size:21px">Рисунок 2.4.1.2. — Рассылка ARP-запроса на все порты коммутатора</div>',
])
