# -*- coding: utf-8 -*-
"""fig_s30_0 — широковещательный шторм в топологии с петлями: локальный трафик PC-A→PC-B и лавина кадров. SVG."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fig_s40_0 as K

W, H, TOP = 1374, 896, 0
P = "s30"
SW = [(505, 30, 180, 150), (915, 30, 180, 150), (495, 260, 180, 150), (915, 260, 180, 150),
      (270, 555, 180, 150), (705, 565, 180, 150), (1135, 555, 180, 150)]
LINKS = [((675, 100), (918, 100)), ((675, 128), (918, 128)),
         ((590, 172), (558, 265)), ((1012, 172), (990, 268)),
         ((640, 165), (930, 290)), ((930, 150), (650, 285)),
         ((665, 333), (918, 333)), ((665, 360), (918, 360)),
         ((525, 405), (412, 592)), ((940, 370), (432, 606)),
         ((570, 405), (760, 578)), ((990, 405), (800, 578)),
         ((615, 400), (1188, 572)), ((1015, 400), (1225, 572)),
         ((300, 678), (205, 738)), ((392, 690), (452, 738))]
ENV = [(715, 70, 0), (870, 150, -25), (545, 215, -70), (675, 240, -25), (855, 235, 25), (972, 212, 70),
       (715, 302, 0), (866, 302, 180), (715, 400, 15), (862, 382, -25), (655, 445, 30), (910, 430, -30),
       (742, 520, 30), (836, 497, -30), (440, 487, -60), (527, 535, -20), (1105, 435, 30), (1090, 512, 15),
       (215, 690, -20), (432, 686, 30)]


def _net():
    s = "".join(K.poly([a, b], "#7fb6e0", 2, P + "-dw") for a, b in LINKS)
    s += f'<g fill="none" stroke="{K.M}" stroke-width="2.6"><ellipse cx="795" cy="114" rx="25" ry="34"/><ellipse cx="790" cy="346" rx="25" ry="34"/></g>'
    s += "".join(K.sw(P, *q) for q in SW)
    s += K.pc(P, 130, 690, 115, 165) + K.pc(P, 405, 690, 115, 165)
    s += ('<g font-family="Oswald,sans-serif" font-size="27" fill="#fff" font-weight="500">'
          '<text x="148" y="752" transform="rotate(12 148 752)">PC-A</text><text x="424" y="752" transform="rotate(-12 424 752)">PC-B</text></g>')
    return s


def _arc():
    return (f'<path d="M175 722 C 230 560, 420 560, 452 722" fill="none" stroke="{K.R}" stroke-width="7" stroke-linecap="round" '
            f'pathLength="1" class="{P}-dw" filter="url(#{P}-glow)"/>'
            f'<path d="M434 700 L456 728 L470 694 Z" fill="{K.R}" class="{P}-pop" style="animation-delay:.9s"/>')


def _storm():
    return "".join(f'<g class="{P}-pop" style="animation-delay:{i * 90}ms">' + K.env(P, x, y, a, 74, P + "-jig") + '</g>'
                   for i, (x, y, a) in enumerate(ENV))


HTML = K.css(P) + K.defs(P) + "".join([
    K.layer(W, H, P, _net()),
    K.layer(W, H, P, _arc()),
    K.layer(W, H, P, _storm()),
    K.layer(W, H, P, f'<g fill="none" stroke="{K.R}" stroke-width="3.5" class="{P}-blink"><ellipse cx="795" cy="114" rx="30" ry="40"/><ellipse cx="790" cy="346" rx="30" ry="40"/></g>'),
])
