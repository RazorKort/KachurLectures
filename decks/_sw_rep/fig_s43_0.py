# -*- coding: utf-8 -*-
"""fig_s43_0 — Рисунок 2.4.1.4: рассылка ARP-запроса на все порты коммутатора в одном сегменте. Перерисовка в SVG."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fig_s40_0 as K

W, H, TOP = 1394, 752, 0
P = "s43"
SW = [(392, 90, 125, 100), (392, 250, 125, 100), (392, 415, 125, 100)]
COLS = [615, 815, 1015]
ROWS = [(80, 62, 48), (240, 232, 200), (405, 400, 368)]
VC = [K.G, K.R, K.B]
RX = [318, 342, 366]


def _links():
    out = []
    for i, (sx, sy, _, _) in enumerate(SW):
        r1, r2, r3 = ROWS[i]; y0 = sy + 28; c = VC[i]
        out.append(K.poly([(sx + 108, y0), (595, r3 + 42), (COLS[2] + 20, r3 + 42)], c, 3, P + "-dw"))
        out.append(K.poly([(sx + 110, y0 + 12), (595, r2 + 30), (COLS[1] + 22, r2 + 30)], c, 3, P + "-dw"))
        out.append(K.poly([(sx + 112, y0 + 24), (COLS[0] + 22, r1 + 42)], c, 3, P + "-dw"))
        out.append(K.poly([(RX[i], 600), (RX[i], sy + 70), (sx + 12, sy + 70)], c, 3, P + "-dw"))
    return "".join(out)


def _pcs():
    return "".join(K.pc(P, COLS[j], ROWS[i][j], 95, 124) for i in range(3) for j in range(3))


HTML = K.css(P) + K.defs(P) + "".join([
    K.layer(W, H, P, K.use(P, "rt", 282, 572, 130, 100, 'filter="url(#s43-glow)"')),
    K.layer(W, H, P, _links() + "".join(K.sw(P, *s, label="SW L2") for s in SW)),
    K.layer(W, H, P, _pcs() + K.label(P, 900, 165, "10.10.1.6") + K.label(P, 1100, 135, "10.10.1.5")),
    K.layer(W, H, P, K.arp(P, 152, 518, 150, 124, False, 18, P + "-pop")),
    K.layer(W, H, P, K.arp(P, 490, 56, 158, 128, False, 18, P + "-pop")
            + f'<g class="{P}-pop" style="animation-delay:400ms">' + K.arp(P, 690, 26, 160, 128, False, 18) + '</g>'),
    f'<div class="{P}-cap step" style="left:125px;top:705px;font-size:21px">Рисунок 2.4.1.4. — Рассылка ARP-запроса на все порты коммутатора в одном сегменте сети</div>',
])
