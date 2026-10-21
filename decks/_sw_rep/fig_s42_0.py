# -*- coding: utf-8 -*-
"""fig_s42_0 — Рисунок 2.4.1.3: разделение сети на широковещательные домены. Перерисовка в SVG."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fig_s40_0 as K

W, H, TOP = 1288, 814, 0
P = "s42"
SW = [(252, 100, 125, 100), (252, 268, 125, 100), (252, 448, 125, 100)]
COLS = [500, 720, 930]
ROWS = [(95, 72, 60), (262, 255, 220), (445, 438, 400)]
VC = [K.G, K.R, K.B]
RX = [172, 196, 218]   # вертикали к маршрутизатору


def _links():
    out = []
    for i, (sx, sy, _, _) in enumerate(SW):
        r1, r2, r3 = ROWS[i]; y0 = sy + 28; c = VC[i]
        out.append(K.poly([(sx + 108, y0), (475, r3 + 40), (COLS[2] + 20, r3 + 40)], c, 3, P + "-dw"))
        out.append(K.poly([(sx + 110, y0 + 12), (475, r2 + 30), (COLS[1] + 22, r2 + 30)], c, 3, P + "-dw"))
        out.append(K.poly([(sx + 112, y0 + 24), (COLS[0] + 22, r1 + 42)], c, 3, P + "-dw"))
        out.append(K.poly([(RX[i], 640), (RX[i], sy + 72), (sx + 12, sy + 72)], c, 3, P + "-dw"))
    return "".join(out)


def _pcs():
    return "".join(K.pc(P, COLS[j], ROWS[i][j], 95, 124) for i in range(3) for j in range(3))


HTML = K.css(P) + K.defs(P) + "".join([
    K.layer(W, H, P, K.use(P, "rt", 132, 618, 130, 100, 'filter="url(#s42-glow)"')),
    K.layer(W, H, P, _links() + "".join(K.sw(P, *s, label="SW L2") for s in SW)),
    K.layer(W, H, P, _pcs() + K.label(P, 808, 142, "10.10.1.6") + K.label(P, 1015, 122, "10.10.1.5")),
    K.layer(W, H, P, f'<circle cx="975" cy="110" r="44" fill="none" stroke="{K.O}" stroke-width="3" class="{P}-blink"/>'
            + K.arp(P, 842, 0, 172, 98, True, 18, P + "-pop")),
    f'<div class="{P}-cap step" style="left:215px;top:766px;font-size:21px">Рисунок 2.4.1.3. — Разделение сети на широковещательные домены</div>',
])
