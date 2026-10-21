# -*- coding: utf-8 -*-
"""fig_s32_0 — широковещательный кадр не проходит маршрутизатор: локальный трафик PC-A→PC-B. SVG."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fig_s40_0 as K

W, H, TOP = 1216, 784, 0
P = "s32"


def _net():
    s = "".join(K.poly([a, b], "#7fb6e0", 2, P + "-dw") for a, b in [
        ((735, 92), (850, 200)), ((530, 275), (772, 275)), ((445, 320), (410, 440)), ((478, 312), (792, 446)),
        ((380, 535), (282, 600)), ((460, 560), (528, 610))])
    s += K.use(P, "cl", 570, 0, 200, 112) + ('<text x="670" y="45" text-anchor="middle" class="s32-tx" font-size="19">Интернет</text>'
                                            '<text x="670" y="72" text-anchor="middle" class="s32-tx" font-size="19">провайдер</text>')
    s += K.use(P, "rt", 762, 190, 182, 160, 'filter="url(#s32-glow)"')
    s += K.sw(P, 350, 170, 185, 160) + K.sw(P, 360, 425, 185, 160) + K.sw(P, 735, 430, 185, 160)
    s += K.pc(P, 185, 562, 125, 175) + K.pc(P, 482, 578, 125, 175)
    s += ('<g font-family="Oswald,sans-serif" font-size="27" fill="#fff" font-weight="500">'
          '<text x="222" y="630" transform="rotate(12 222 630)">PC-A</text><text x="500" y="652" transform="rotate(-12 500 652)">PC-B</text></g>')
    return s


def _arc():
    return (f'<path d="M252 622 C 300 470, 520 470, 545 628" fill="none" stroke="{K.R}" stroke-width="7" stroke-linecap="round" '
            f'pathLength="1" class="{P}-dw" filter="url(#{P}-glow)"/>'
            f'<path d="M528 606 L548 636 L564 602 Z" fill="{K.R}" class="{P}-pop" style="animation-delay:.9s"/>')


ENV = [(315, 572, -20), (502, 560, 30), (390, 392, -70), (570, 316, 30), (708, 240, 0)]


def _bc():
    return "".join(f'<g class="{P}-pop" style="animation-delay:{i * 250}ms">' + K.env(P, x, y, a, 74) + '</g>'
                   for i, (x, y, a) in enumerate(ENV))


HTML = K.css(P) + K.defs(P) + "".join([
    K.layer(W, H, P, _net()),
    K.layer(W, H, P, _arc()),
    K.layer(W, H, P, _bc()),
    K.layer(W, H, P, f'<g stroke="{K.R}" stroke-width="7" stroke-linecap="round" class="{P}-pop" filter="url(#{P}-glow)">'
            '<line x1="728" y1="214" x2="796" y2="284"/><line x1="796" y1="214" x2="728" y2="284"/></g>'),
])
