# -*- coding: utf-8 -*-
"""Неоновые векторные иконки для перерисовок fig_s65_0, fig_s72_0, fig_s74_0, fig_s79_0, fig_s80_0/1, fig_s82_0."""
C, V, M, G, Y, R = "#2ad4ff", "#9b6bff", "#e05cff", "#9dfc5a", "#ffc53d", "#ff4d5e"
F = "rgba(10,40,100,.75)"

CSS = """<style>
.fgk-l{position:absolute;left:0;top:0;overflow:visible;pointer-events:none}
.fgk-gl{filter:drop-shadow(0 0 6px rgba(42,212,255,.7))}
.fgk-t{position:absolute;font-family:'Golos Text',sans-serif;color:#e6f1ff;white-space:nowrap;line-height:1}
.fgk-b{font-weight:700}
.fgk-cap{position:absolute;left:0;width:100%;text-align:center;font-family:'Golos Text',sans-serif;font-style:italic;color:#a9bde6;white-space:nowrap}
@keyframes fgk-draw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}
.fgk-d{stroke-dasharray:1;stroke-dashoffset:0}
.step.vis .fgk-d{animation:fgk-draw 1.1s ease-out forwards}
@keyframes fgk-blink{0%,100%{opacity:1}50%{opacity:.35}}
.step.vis .fgk-bl{animation:fgk-blink 1.4s ease-in-out infinite}
</style>"""


def layer(W, H, body, step=True, delay=0, glow=True):
    return ('<svg class="fgk-l%s%s" width="%d" height="%d" viewBox="0 0 %d %d" style="transition-delay:%dms">%s</svg>'
            % (" step" if step else "", " fgk-gl" if glow else "", W, H, W, H, delay, body))


def t(x, y, s, size=22, color="#e6f1ff", bold=False, anchor="l", step=False, delay=0, extra=""):
    tr = {"l": "", "c": "translateX(-50%)", "r": "translateX(-100%)"}[anchor]
    inner = '<span style="display:inline-block;transform:%s">%s</span>' % (tr, s) if tr else s
    return ('<div class="fgk-t%s%s" style="left:%dpx;top:%dpx;font-size:%dpx;color:%s;transition-delay:%dms;%s">%s</div>'
            % (" fgk-b" if bold else "", " step" if step else "", x, y, size, color, delay, extra, inner))


def line(x1, y1, x2, y2, col=C, w=4, draw=True, extra=""):
    return ('<line x1="%s" y1="%s" x2="%s" y2="%s" stroke="%s" stroke-width="%s" stroke-linecap="round" %s %s/>'
            % (x1, y1, x2, y2, col, w, 'pathLength="1" class="fgk-d"' if draw else "", extra))


def path(d, col=C, w=4, draw=True, extra=""):
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%s" stroke-linecap="round" %s %s/>'
            % (d, col, w, 'pathLength="1" class="fgk-d"' if draw else "", extra))


def dot(x, y, r=14, col=R, blink=False):
    return '<circle cx="%s" cy="%s" r="%s" fill="%s" stroke="#fff" stroke-width="1.5"%s/>' % (x, y, r, col, ' class="fgk-bl"' if blink else "")


def _arrows(cx, cy, s, col="#fff"):
    """Четыре стрелки коммутатора (две вправо, две влево) вокруг центра."""
    out = []
    for k, (dy, d) in enumerate([(-1.5, 1), (-.5, -1), (.5, 1), (1.5, -1)]):
        y = cy + dy * s * .42
        x0 = cx - s * .9 + (k % 2) * s * .25 - (k // 2) * s * .1
        x1 = x0 + s * 1.3
        tip, tail = (x1, x0) if d > 0 else (x0, x1)
        out.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%.1f"/>' % (tail, y, tip, y, col, s * .12))
        out.append('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>' % (tip + d * s * .12, y, tip - d * s * .2, y - s * .17, tip - d * s * .2, y + s * .17, col))
    return "".join(out)


def switch(x, y, w, h, label="", col=C):
    """Изометрический коммутатор: верхняя грань, левая и правая боковины, стрелки, подпись."""
    P = lambda u, v: "%.1f,%.1f" % (x + u * w, y + v * h)
    s = '<polygon points="%s %s %s %s" fill="rgba(8,40,95,.95)" stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % (
        P(0, .2), P(.25, .66), P(.25, 1), P(0, .52), col)
    s += '<polygon points="%s %s %s %s" fill="rgba(14,62,140,.95)" stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % (
        P(.25, .66), P(1, .44), P(1, .76), P(.25, 1), col)
    s += '<polygon points="%s %s %s %s" fill="rgba(30,120,210,.9)" stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % (
        P(0, .2), P(.72, 0), P(1, .44), P(.25, .66), col)
    cx, cy = x + w * .5, y + h * .33
    s += '<g transform="rotate(-12 %.1f %.1f)">%s</g>' % (cx, cy, _arrows(cx, cy, min(w, h * 1.3) * .2))
    if label:
        s += ('<text x="%.1f" y="%.1f" font-family="Golos Text,sans-serif" font-weight="700" font-size="%.0f" fill="#fff" text-anchor="middle" transform="rotate(-12 %.1f %.1f)">%s</text>'
              % (x + w * .63, y + h * .92, h * .16, x + w * .63, y + h * .88, label))
    return s


def router(x, y, w, h, label="", col=C):
    rx, ry = w / 2, h * .3
    cx, cy = x + rx, y + ry
    s = ('<path d="M%.1f,%.1f v%.1f a%.1f,%.1f 0 0 0 %.1f,0 v%.1f" fill="rgba(8,40,95,.92)" stroke="%s" stroke-width="3"/>'
         % (x, cy, h - 2 * ry, rx, ry, w, -(h - 2 * ry), col))
    s += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="rgba(20,90,170,.9)" stroke="%s" stroke-width="3"/>' % (cx, cy, rx, ry, col)
    for ax, ay, out in ((1, -1, True), (-1, 1, True), (-1, -1, False), (1, 1, False)):
        a, b = (.15, .7) if out else (.75, .2)
        s += harrow(cx + ax * rx * a, cy + ay * ry * a, cx + ax * rx * b, cy + ay * ry * b, "#fff", 5)
    if label:
        s += ('<text x="%.1f" y="%.1f" font-family="Golos Text,sans-serif" font-weight="700" font-size="%.0f" fill="#fff" text-anchor="middle">%s</text>'
              % (cx, y + h * .87, h * .2, label))
    return s


def pc(x, y, w, col=C):
    """Монитор (w — ширина экрана), клавиатура и мышь под ним."""
    h = w * .72
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="5" fill="rgba(20,90,170,.85)" stroke="%s" stroke-width="3"/>' % (x, y, w, h, col)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="rgba(42,212,255,.18)"/>' % (x + 8, y + 8, w - 16, h - 16)
    s += '<path d="M%.1f,%.1f v%.1f h%.1f" fill="none" stroke="%s" stroke-width="3"/>' % (x + w * .5, y + h, w * .14, w * .2, col)
    kx, ky = x + w * .35, y + h + w * .2
    s += ('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="rgba(20,90,170,.85)" stroke="%s" stroke-width="3" stroke-linejoin="round"/>'
          % (kx, ky + w * .22, kx + w * .75, ky, kx + w * .85, ky + w * .08, kx + w * .1, ky + w * .3, col))
    s += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="rgba(20,90,170,.85)" stroke="%s" stroke-width="2.5"/>' % (x + w * .25, ky + w * .5, w * .07, w * .045, col)
    return s


def pc_left(x, y, w, col=C):
    """ПК как на рис. s74: клавиатура и мышь левее/под монитором."""
    h = w * .72
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="5" fill="rgba(20,90,170,.85)" stroke="%s" stroke-width="3"/>' % (x, y, w, h, col)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="rgba(42,212,255,.18)"/>' % (x + 8, y + 8, w - 16, h - 16)
    s += '<path d="M%.1f,%.1f v%.1f h%.1f" fill="none" stroke="%s" stroke-width="3"/>' % (x + w * .45, y + h, w * .12, w * .2, col)
    kx, ky = x - w * .22, y + h + w * .25
    s += ('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="rgba(20,90,170,.85)" stroke="%s" stroke-width="3" stroke-linejoin="round"/>'
          % (kx, ky + w * .12, kx + w * .2, ky, kx + w * .78, ky + w * .22, kx + w * .58, ky + w * .36, col))
    s += '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="rgba(20,90,170,.85)" stroke="%s" stroke-width="2.5"/>' % (x + w * .72, y + h + w * .62, w * .08, w * .05, col)
    return s


def laptop(x, y, w, col=C, rot=0):
    """Ноутбук «Admin»: экран (w×0.7w), клавиатурная база снизу."""
    h = w * .72
    s = '<g transform="rotate(%s %.1f %.1f)">' % (rot, x + w / 2, y + h / 2)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="6" fill="rgba(20,90,170,.85)" stroke="%s" stroke-width="3"/>' % (x, y, w, h, col)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="rgba(42,212,255,.15)"/>' % (x + 9, y + 9, w - 18, h - 18)
    s += ('<text x="%.1f" y="%.1f" font-family="Golos Text,sans-serif" font-weight="700" font-size="%.0f" fill="#fff" text-anchor="middle" transform="rotate(22 %.1f %.1f)">Admin</text>'
          % (x + w / 2, y + h * .45, w * .16, x + w / 2, y + h * .42))
    s += '</g>'
    bx, by = x - w * .05, y + h
    s += ('<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="rgba(8,40,95,.92)" stroke="%s" stroke-width="3" stroke-linejoin="round"/>'
          % (x, by, x + w, by, x + w + w * .02, by + w * .14, bx - w * .05, by + w * .14, col))
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="rgba(42,212,255,.35)"/>' % (x + w * .3, by + w * .05, w * .3, w * .05)
    return s


def phone(x, y, w, h, col=C):
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="14" fill="rgba(20,90,170,.85)" stroke="%s" stroke-width="3" transform="rotate(12 %.1f %.1f)"/>' % (
        x + w * .15, y, w * .8, h, col, x + w / 2, y + h / 2)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="10" fill="rgba(8,40,95,.95)" stroke="%s" stroke-width="3" transform="rotate(12 %.1f %.1f)"/>' % (
        x, y + h * .05, w * .3, h * .62, col, x + w / 2, y + h / 2)
    s += '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="4" fill="rgba(42,212,255,.35)" stroke="%s" stroke-width="2" transform="rotate(12 %.1f %.1f)"/>' % (
        x + w * .5, y + h * .12, w * .32, h * .22, col, x + w / 2, y + h / 2)
    for i in range(3):
        for j in range(3):
            s += '<circle cx="%.1f" cy="%.1f" r="4" fill="#cfefff" transform="rotate(12 %.1f %.1f)"/>' % (
                x + w * (.5 + .12 * i), y + h * (.5 + .12 * j), x + w / 2, y + h / 2)
    return s


def cloud(x, y, w, h, col=C):
    d = ("M{a},{b} c{c1},0 {c2},{c3} {c4},{c5} c{c6},{c7} {c8},{c9} {c10},{c11} c{c12},{c13} {c14},{c15} {c16},{c17} "
         "c{c18},{c19} {c20},{c21} {c22},{c23} c{c24},{c25} {c26},{c27} {c28},{c29} c{c30},{c31} {c32},{c33} {c34},{c35} z")
    u, v = w / 100, h / 100
    pts = dict(a=x + 18 * u, b=y + 85 * v,
               c1=-14 * u, c2=-22 * u, c3=-26 * v, c4=-6 * u, c5=-36 * v,
               c6=0, c7=-22 * v, c8=22 * u, c9=-30 * v, c10=36 * u, c11=-20 * v,
               c12=10 * u, c13=-24 * v, c14=44 * u, c15=-24 * v, c16=52 * u, c17=4 * v,
               c18=20 * u, c19=-2 * v, c20=32 * u, c21=24 * v, c22=10 * u, c23=40 * v,
               c24=4 * u, c25=26 * v, c26=-34 * u, c27=34 * v, c28=-46 * u, c29=12 * v,
               c30=-10 * u, c31=20 * v, c32=-48 * u, c33=18 * v, c34=-46 * u, c35=-4 * v)
    return '<path d="%s" fill="rgba(10,40,100,.8)" stroke="%s" stroke-width="3" stroke-linejoin="round"/>' % (d.format(**pts), col)


def envelope(x, y, w, h, col):
    s = '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" fill-opacity=".18" stroke="%s" stroke-width="3"/>' % (x, y, w, h, col, col)
    s += '<path d="M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f" fill="none" stroke="%s" stroke-width="2.5"/>' % (x, y, x + w / 2, y + h * .55, x + w, y, col)
    s += '<path d="M%.1f,%.1f h%.1f v%.1f l%.1f,%.1f l%.1f,%.1f v%.1f h%.1f z" fill="%s"/>' % (
        x + w * .7, y + h * .62, -w * .38, -h * .14, -w * .2, h * .24, w * .2, h * .24, -h * .14, w * .38, col)
    return s


def harrow(x0, y0, x1, y1, col=C, w=4):
    """Стрелка с треугольным наконечником (без marker, чтобы не плодить id)."""
    import math
    a = math.atan2(y1 - y0, x1 - x0)
    L = w * 3.2
    bx, by = x1 - L * math.cos(a), y1 - L * math.sin(a)
    px, py = -math.sin(a) * L * .6, math.cos(a) * L * .6
    return ('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"/>'
            '<polygon points="%.1f,%.1f %.1f,%.1f %.1f,%.1f" fill="%s"/>'
            % (x0, y0, bx, by, col, w, x1, y1, bx + px, by + py, bx - px, by - py, col))
