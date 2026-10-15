# -*- coding: utf-8 -*-
"""Плакатный кит деки 2.5: вечерний город, панели, устройства и иконки для нативных плакатов.

Все плакаты рисуются в системе координат 1600×900.
"""

INK = "#101b1a"
RED = "#dd3326"
CYAN = "#5ec6d8"
AMBER = "#e8a63c"
CREAM = "#f4ecda"
CREAM2 = "#e8dcc2"
GREEN = "#3f9e6a"
FT = "Oswald,Roboto Condensed,Impact,sans-serif"
FB = "Roboto Condensed,Arial Narrow,sans-serif"
FM = "JetBrains Mono,Consolas,monospace"

_n = [0]

import base64 as _b64
import os as _os

_ASSETS = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "_sd_assets")


def asset_uri(name):
    with open(_os.path.join(_ASSETS, name), "rb") as f:
        return "data:image/webp;base64," + _b64.b64encode(f.read()).decode()


POSTER_BG = (1, 2, 3, 5)   # фото-задники, доступные плакатам через <use href="#sdbgN">


def image_defs():
    """Скрытый svg с картинками-задниками: одна копия на весь документ."""
    imgs = "".join('<image id="sdbg%d" href="%s" width="1600" height="900" preserveAspectRatio="none"/>'
                   % (n, asset_uri("bg%d.webp" % n)) for n in POSTER_BG)
    return ('<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>%s</defs></svg>'
            % imgs)


def photo(x, y, w, hh, n=1, dim=.8, fx=.5, fy=.5):
    """Кадр из фото-задника n, вписанный в прямоугольник с обрезкой (как object-fit:cover)."""
    u = nid("ph")
    sc = max(w / 1600.0, hh / 900.0)
    tx = x - (1600 * sc - w) * fx
    ty = y - (900 * sc - hh) * fy
    ov = ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#0b1f1e" opacity="%.2f"/>'
          % (x, y, w, hh, 1 - dim)) if dim < 1 else ""
    return ('<clipPath id="%s"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f"/></clipPath>'
            '<g clip-path="url(#%s)"><use href="#sdbg%d" transform="translate(%.1f %.1f) scale(%.4f)"/>%s</g>'
            % (u, x, y, w, hh, u, n, tx, ty, sc, ov))


def nid(p="p"):
    _n[0] += 1
    return "%s%d" % (p, _n[0])


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ======================================================================
#  ТЕКСТ
# ======================================================================

def t(x, y, s, fs=20, col=INK, anc="middle", w=600, font=FB, ls=None, cls=""):
    l = ' letter-spacing="%s"' % ls if ls else ""
    c = ' class="%s"' % cls if cls else ""
    return ('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="%.1f" font-weight="%d" fill="%s" '
            'font-family="%s"%s%s>%s</text>' % (x, y, anc, fs, w, col, font, l, c, s))


def ml(x, y, s, fs=20, col=INK, anc="middle", w=600, font=FB, lh=1.22):
    """Многострочный текст, строки через «|»."""
    out = []
    for i, ln in enumerate(s.split("|")):
        out.append(t(x, y + i * fs * lh, ln, fs, col, anc, w, font))
    return "".join(out)


def h(x, y, s, fs=34, col=INK, anc="start"):
    """Плакатный заголовок: узкий прописной."""
    return t(x, y, s.upper(), fs, col, anc, 700, FT, ".01em")


# ======================================================================
#  ВЕЧЕРНИЙ ГОРОД
# ======================================================================

class _R:
    def __init__(self, seed):
        self.s = seed * 9301 + 49297

    def r(self):
        self.s = (self.s * 1103515245 + 12345) & 0x7fffffff
        return self.s / 0x7fffffff


SKIES = {
    "dusk":  ("#173c3d", "#33605d", "#c8704c"),
    "teal":  ("#1a4645", "#2c5f5c", "#5d8a84"),
    "night": ("#0e2426", "#163737", "#27504c"),
    "red":   ("#2a2b2e", "#6b3a33", "#e0804e"),
}


def city(x, y, w, hh, seed=1, sky="dusk", sun=True, arcs=False, clouds=True, water=False, dim=1.0, hor=None):
    """Вечерний город: кадр из фото-задника (выбор по типу неба и seed) + сетевые дуги поверх."""
    pick = {"dusk": (1, 2), "red": (1, 2), "teal": (3, 2), "night": (5, 3)}[sky]
    n = pick[seed % 2]
    fx = (seed * 37 % 100) / 100.0
    fy = .55 if hh < 500 else .5
    out = [photo(x, y, w, hh, n, min(dim, .92), fx, fy)]
    if arcs:
        R = _R(seed)
        base = y + hh
        hb = hh * (hor if hor is not None else (1.0 if hh < 500 else .5))
        pts = [x + w * k for k in (.06, .3, .55, .8, .97)]
        for i in range(len(pts) - 1):
            x1, x2 = pts[i], pts[i + 1]
            y1 = base - hb * (.45 + R.r() * .2)
            y2 = base - hb * (.45 + R.r() * .2)
            my = min(y1, y2) - hb * .3
            out.append('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f" fill="none" stroke="%s" stroke-width="2.4" '
                       'opacity=".8"/>' % (x1, y1, (x1 + x2) / 2, my, x2, y2, RED))
            out.append('<circle cx="%.1f" cy="%.1f" r="4.5" fill="%s"/>' % (x1, y1, RED))
    return "".join(out)


# ======================================================================
#  ПАНЕЛИ
# ======================================================================

def frame(x, y, w, hh, fill=CREAM, sw=4, shadow=True):
    sh = ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#000" opacity=".45"/>'
          % (x + 8, y + 8, w, hh)) if shadow else ""
    return sh + ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="%d"/>'
                 % (x, y, w, hh, fill, INK, sw))


def panel_head(x, y, title, fs=34, num=None, sub=None, subfs=20):
    """Красная планка (или номер) + прописной заголовок панели."""
    out = []
    tx = x + 22
    if num is not None:
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="3"/>'
                   % (x + 14, y + 12, fs * 1.2, fs * 1.2, RED, INK))
        out.append(t(x + 14 + fs * .6, y + 12 + fs * 1.0, str(num), fs * .95, "#fff", "middle", 700, FT))
        tx = x + 28 + fs * 1.2
    else:
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>'
                   % (x + 14, y + 14, fs * .3, fs * 1.08, RED))
        tx = x + 26 + fs * .3
    lines = title.split("|")
    for i, ln in enumerate(lines):
        out.append(h(tx, y + 14 + fs * .93 + i * fs * 1.02, ln, fs))
    if sub:
        out.append(t(tx, y + 14 + fs * (1.0 + 1.02 * (len(lines) - 1)) + subfs * 1.4, sub, subfs, "#2c3a38",
                     "start", 500))
    return "".join(out)


def card(x, y, w, hh, title=None, num=None, sub=None, fs=30, fill=CREAM):
    return frame(x, y, w, hh, fill) + (panel_head(x, y, title, fs, num, sub) if title else "")


def screen(x, y, w, hh, seed=1, sky="teal", sun=False, arcs=False, dim=.85):
    """Тёмное окно с городом внутри панели."""
    return (city(x, y, w, hh, seed, sky, sun=sun, arcs=arcs, dim=dim) +
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="none" stroke="%s" stroke-width="3"/>'
            % (x, y, w, hh, INK))


def strip(x, y, w, s, fs=21, hh=40, fill=CREAM, col=INK):
    """Подпись-полоса под окном."""
    return ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="3"/>'
            % (x, y, w, hh, fill, INK) + t(x + w / 2, y + hh / 2 + fs * .36, s, fs, col, "middle", 700))


def label(x, y, s, fs=19, fill=CREAM, col=INK, mono=False, pad=14, hh=None, w=None, sw=3):
    """Прямоугольная плашка с текстом по центру."""
    lines = s.split("|")
    k = .6 if mono else .5
    ww = w or max(len(l) for l in lines) * fs * k + pad * 2
    hh = hh or (len(lines) * fs * 1.22 + fs * .75)
    font = FM if mono else FB
    out = ['<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="%d"/>'
           % (x - ww / 2, y - hh / 2, ww, hh, fill, INK, sw)]
    y0 = y - (len(lines) - 1) * fs * 1.22 / 2 + fs * .36
    for i, l in enumerate(lines):
        out.append(t(x, y0 + i * fs * 1.22, l, fs, col, "middle", 700, font))
    return "".join(out)


def bubble(x, y, s, fs=19, fill=CREAM, tail="down", w=None):
    """Выноска-облачко с хвостиком."""
    lines = s.split("|")
    ww = w or max(len(l) for l in lines) * fs * .52 + 30
    hh = len(lines) * fs * 1.22 + fs * .9
    x0, y0 = x - ww / 2, y - hh / 2
    if tail == "down":
        tl = "M%.1f %.1f l14 0 l-12 22 z" % (x - 18, y0 + hh - 2)
    elif tail == "left":
        tl = "M%.1f %.1f l0 14 l-22 -4 z" % (x0 + 2, y - 7)
    else:
        tl = "M%.1f %.1f l0 14 l22 -4 z" % (x0 + ww - 2, y - 7)
    out = ['<path d="%s" fill="%s" stroke="%s" stroke-width="3"/>' % (tl, fill, INK),
           '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="8" fill="%s" stroke="%s" stroke-width="3"/>'
           % (x0, y0, ww, hh, fill, INK),
           '<path d="%s" fill="%s"/>' % (tl, fill)]
    yy = y - (len(lines) - 1) * fs * 1.22 / 2 + fs * .36
    for i, l in enumerate(lines):
        out.append(t(x, yy + i * fs * 1.22, l, fs, INK, "middle", 700))
    return "".join(out)


def poster_title(s, sub=None, x=40, y=32, fs=70, sub_ls=None):
    """Главный заголовок плаката: красная планка + кремовые прописные."""
    lines = s.split("|")
    out = ['<rect x="%d" y="%d" width="18" height="%.1f" fill="%s"/>'
           % (x, y + 4, fs * (len(lines) * 1.02) - 6, RED)]
    for i, l in enumerate(lines):
        out.append('<text x="%d" y="%.1f" font-size="%d" font-weight="700" fill="%s" font-family="%s" '
                   'letter-spacing=".01em" style="paint-order:stroke" stroke="#0a1615" stroke-width="5">%s</text>'
                   % (x + 38, y + fs * .9 + i * fs * 1.02, fs, CREAM, FT, l.upper()))
    if sub:
        ls = ' letter-spacing="%s"' % sub_ls if sub_ls else ""
        out.append('<text x="%d" y="%.1f" font-size="25" font-weight="600" fill="#e6efe9" font-family="%s"%s '
                   'style="paint-order:stroke" stroke="#0a1615" stroke-width="4">%s</text>'
                   % (x + 40, y + fs * len(lines) * 1.02 + 30, FB, ls, sub))
    return "".join(out)


def band(x, y, w, s, fs=30, hh=64, fill="#0f2523", col=CREAM, mark=True):
    out = [frame(x, y, w, hh, fill)]
    if mark:
        out.append('<rect x="%.1f" y="%.1f" width="12" height="%.1f" fill="%s"/>' % (x + 18, y + 14, hh - 28, RED))
    out.append(h(x + w / 2, y + hh / 2 + fs * .36, s, fs, col, "middle"))
    return "".join(out)


def terminal(x, y, w, hh, lines, fs=22):
    """Окно терминала с тремя точками."""
    out = [frame(x, y, w, hh, "#0b1716"),
           '<circle cx="%.1f" cy="%.1f" r="7" fill="#e05545"/>' % (x + 24, y + 22),
           '<circle cx="%.1f" cy="%.1f" r="7" fill="#e8b545"/>' % (x + 46, y + 22),
           '<circle cx="%.1f" cy="%.1f" r="7" fill="#7d8c89"/>' % (x + 68, y + 22)]
    for i, ln in enumerate(lines):
        pr, cm = ln if isinstance(ln, tuple) else ("", ln)
        out.append('<text x="%.1f" y="%.1f" font-size="%d" font-family="%s" font-weight="600">'
                   '<tspan fill="#e9e2cf">%s</tspan><tspan fill="#ffd47a">%s</tspan></text>'
                   % (x + 26, y + 62 + i * fs * 1.45, fs, FM, esc(pr), esc(cm)))
    return "".join(out)


# ======================================================================
#  УСТРОЙСТВА
# ======================================================================

def wrouter(x, y, w=150, lab=None, leds=5, ants=2, labfs=22):
    """Чёрный маршрутизатор с антеннами, вид в три четверти."""
    hh = w * .26
    dep = w * .16
    out = []
    ax = [x - w * .3, x + w * .3] if ants == 2 else [x - w * .36, x - w * .12, x + w * .12, x + w * .36]
    for i, a in enumerate(ax):
        x2 = a + (i - (len(ax) - 1) / 2) * 3
        y2 = y - hh * .2 - w * .38
        out.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="#000" stroke-width="%.1f" stroke-linecap="round"/>'
                   % (a, y - hh * .2, x2, y2, w * .035 + 5))
        out.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="#3d5352" stroke-width="%.1f" stroke-linecap="round"/>'
                   % (a, y - hh * .2, x2, y2, w * .035))
    # верх
    out.append('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z" fill="#2b3a39" stroke="%s" stroke-width="3"/>'
               % (x - w / 2, y - hh * .25, x - w / 2 + dep, y - hh * .25 - dep * .7,
                  x + w / 2 + dep * .2, y - hh * .25 - dep * .7, x + w / 2, y - hh * .25, INK))
    # лицевая
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="4" fill="#161f1f" stroke="%s" stroke-width="3"/>'
               % (x - w / 2, y - hh * .25, w, hh, INK))
    for i in range(leds):
        lx = x - w * .17 + i * w * .085
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.5" fill="%s"/>'
                   % (lx, y + hh * .2, w * .045, hh * .2, RED))
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" opacity=".35"/>'
                   % (lx - 3, y + hh * .2 - 3, w * .045 + 6, hh * .2 + 6, RED))
    if lab:
        out.append(label(x, y + hh * .75 + 24, lab, labfs, CREAM, INK, hh=labfs * 1.6))
    return "<g>%s</g>" % "".join(out)


def puck(x, y, r=46, lab=None, tone="dark", labfs=20):
    """Цилиндр-маршрутизатор с белым крестом стрелок."""
    body = {"dark": ("#1c2827", "#2f3e3d"), "blue": ("#1f5a7a", "#3b86ad"),
            "red": ("#9c2219", "#d64236")}[tone]
    ry = r * .36
    hh = r * .55
    sw = max(2.5, r * .09)
    a = r * .55
    hw = r * .16
    ar = []
    for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ex, ey = x + dx * a, y - hh / 2 + dy * a * .36
        sx, sy = x + dx * a * .25, y - hh / 2 + dy * a * .09
        ar.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="#fff" stroke-width="%.1f" stroke-linecap="round"/>'
                  % (sx, sy, ex, ey, sw))
        if dx:
            ar.append('<path d="M%.1f %.1f l%.1f %.1f l%.1f %.1f z" fill="#fff"/>'
                      % (ex + dx * hw, ey, -dx * hw * 1.4, -hw * .55, 0, hw * 1.1))
        else:
            ar.append('<path d="M%.1f %.1f l%.1f %.1f l%.1f %.1f z" fill="#fff"/>'
                      % (ex, ey + dy * hw * .45, -hw * .7, -dy * hw * .6, hw * 1.4, 0))
    out = ['<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" stroke="%s" stroke-width="3"/>'
           % (x, y + hh / 2, r, ry, body[0], INK),
           '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>' % (x - r, y - hh / 2, r * 2, hh, body[0]),
           '<path d="M%.1f %.1f V%.1f M%.1f %.1f V%.1f" stroke="%s" stroke-width="3"/>'
           % (x - r, y - hh / 2, y + hh / 2, x + r, y - hh / 2, y + hh / 2, INK),
           '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" stroke="%s" stroke-width="3"/>'
           % (x, y - hh / 2, r, ry, body[1], INK)]
    out += ar
    for i in range(3):
        out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (x - r * .2 + i * r * .2, y + hh * .3, r * .05, RED))
    if lab:
        out.append(label(x, y + hh / 2 + ry + 22, lab, labfs, CREAM, INK, hh=labfs * 1.6))
    return "<g>%s</g>" % "".join(out)


def switch(x, y, w=110):
    hh = w * .2
    ports = "".join('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#0b1414"/>'
                    % (x - w * .38 + i * w * .13, y - hh * .15, w * .08, hh * .35) for i in range(6))
    return ('<g><path d="M%.1f %.1f l%.1f %.1f h%.1f l%.1f %.1f z" fill="#2b3a39" stroke="%s" stroke-width="3"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#1b2626" stroke="%s" stroke-width="3"/>'
            '%s<circle cx="%.1f" cy="%.1f" r="3" fill="%s"/></g>'
            % (x - w / 2, y - hh / 2, w * .1, -hh * .5, w * .85, w * .05, hh * .5, INK,
               x - w / 2, y - hh / 2, w, hh, INK, ports, x + w * .4, y, RED))


def monitor(x, y, s=1.0):
    w, hh = 64 * s, 46 * s
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#162423" stroke="%s" stroke-width="3"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#3b8ea0"/>'
            '<path d="M%.1f %.1f l-%.1f %.1f h%.1f z" fill="#162423" stroke="%s" stroke-width="2.5"/></g>'
            % (x - w / 2, y - hh / 2, w, hh, INK, x - w / 2 + 5 * s, y - hh / 2 + 5 * s, w - 10 * s, hh - 10 * s,
               x, y + hh / 2, 10 * s, 10 * s, 20 * s, INK))


def laptop(x, y, s=1.0):
    w, hh = 66 * s, 42 * s
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#162423" stroke="%s" stroke-width="3"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#3b8ea0"/>'
            '<path d="M%.1f %.1f h%.1f l%.1f %.1f h-%.1f z" fill="#2b3a39" stroke="%s" stroke-width="3"/></g>'
            % (x - w / 2, y - hh / 2, w, hh, INK, x - w / 2 + 5 * s, y - hh / 2 + 5 * s, w - 10 * s, hh - 10 * s,
               x - w / 2, y + hh / 2, w, 10 * s, 12 * s, w + 20 * s, INK))


def tower(x, y, s=1.0):
    w, hh = 26 * s, 56 * s
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#1b2626" stroke="%s" stroke-width="3"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#0b1414"/>'
            '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/></g>'
            % (x - w / 2, y - hh / 2, w, hh, INK, x - w / 2 + 5 * s, y - hh / 2 + 7 * s, w - 10 * s, 5 * s,
               x, y + hh * .3, 2.5 * s, RED))


def rack(x, y, s=1.0, n=5):
    w, hh = 58 * s, (16 * n + 10) * s
    rows = "".join('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#253534"/>'
                   '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/><circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                   % (x - w / 2 + 5 * s, y - hh / 2 + (6 + i * 16) * s, w - 10 * s, 12 * s,
                      x + w / 2 - 12 * s, y - hh / 2 + (12 + i * 16) * s, 2.2 * s, RED,
                      x + w / 2 - 19 * s, y - hh / 2 + (12 + i * 16) * s, 2.2 * s, "#5ec6d8")
                   for i in range(n))
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#121c1c" stroke="%s" stroke-width="3"/>%s</g>'
            % (x - w / 2, y - hh / 2, w, hh, INK, rows))


CLOUD_D = ("M40 104 A26 26 0 0 1 44 53 A40 40 0 0 1 116 40 "
           "A30 30 0 0 1 160 58 A24 24 0 0 1 162 104 Z")


def cloud(x, y, w, hh, fill=CREAM, sw=4, edge=INK):
    sx, sy = w / 126.0, hh / 70.0
    tx, ty = x - w / 2 - 38 * sx, y - hh / 2 - 34 * sy
    return ('<g transform="translate(%.2f %.2f) scale(%.4f %.4f)"><path d="%s" fill="%s" stroke="%s" '
            'stroke-width="%.2f" stroke-linejoin="round"/></g>' % (tx, ty, sx, sy, CLOUD_D, fill, edge, sw / max(sx, sy)))


def citycloud(x, y, w, hh, lab=None, labfs=19, red=False, q=False):
    """Облако-сеть с домиками внутри и подписью-плашкой снизу (как на плакатах)."""
    out = [cloud(x, y, w, hh, CREAM2 if not red else "#f3d8cf", 4, RED if red else INK)]
    bw = w * .1
    for i, k in enumerate((-1.6, -.5, .5, 1.5)):
        bh = hh * (.28 + .12 * ((i * 7) % 3))
        bx = x + k * bw * 1.05 - bw / 2
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#1f3332" stroke="%s" stroke-width="2"/>'
                   % (bx, y + hh * .3 - bh, bw, bh, INK))
        out.append('<path d="M%.1f %.1f v%.1f M%.1f %.1f v%.1f" stroke="#7fd0dc" stroke-width="2" opacity=".7"/>'
                   % (bx + bw * .33, y + hh * .3 - bh + 4, bh - 8, bx + bw * .66, y + hh * .3 - bh + 4, bh - 8))
    if q:
        out = [cloud(x, y, w, hh, CREAM2, 4, INK), t(x, y + hh * .22, "?", hh * .55, INK, "middle", 700, FT)]
    if lab:
        out.append(label(x, y + hh * .5 + 14, lab, labfs, CREAM, INK))
    return "<g>%s</g>" % "".join(out)


def netcloud(x, y, w=170, hh=120, lab=None, sub=None, labfs=20):
    """Облако с компьютерами внутри (Сеть А / Сеть Б)."""
    out = [cloud(x, y, w, hh, CREAM2, 4)]
    out.append(monitor(x - w * .2, y - hh * .05, .55))
    out.append(monitor(x + w * .18, y - hh * .12, .55))
    out.append(laptop(x - w * .02, y + hh * .2, .5))
    if lab:
        text = lab + ("|" + sub if sub else "")
        out.append(label(x, y + hh * .55 + 18, text, labfs, CREAM, INK))
    return "<g>%s</g>" % "".join(out)


# ======================================================================
#  СТРЕЛКИ И ЗНАКИ
# ======================================================================

COLS = {"red": RED, "cyan": CYAN, "amber": AMBER, "cream": CREAM, "green": GREEN, "ink": INK, "white": "#ffffff",
        "blue": "#4aa3d6"}


def defs_arrows(u):
    out = []
    for k, c in COLS.items():
        out.append('<marker id="%s_%s" viewBox="0 0 10 10" refX="7.5" refY="5" markerWidth="3.6" markerHeight="3.6" '
                   'orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="%s"/></marker>' % (u, k, c))
    out.append('<filter id="%s_gl" filterUnits="userSpaceOnUse" x="-200" y="-200" width="2000" height="1300">'
               '<feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/>'
               '<feMergeNode in="SourceGraphic"/></feMerge></filter>' % u)
    return "".join(out)


def ar(x1, y1, x2, y2, col="red", w=7, curve=0, dash=False, both=False, glow=True, cls="dash"):
    """Светящаяся стрелка. В плакате маркеры подставляются через __U__."""
    if curve:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - curve
        d = "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x1, y1, mx, my, x2, y2)
        L = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5 * 1.25) + 30
    else:
        d = "M%.1f %.1f L%.1f %.1f" % (x1, y1, x2, y2)
        L = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5) + 20
    c = COLS[col]
    da = ' stroke-dasharray="14 11"' if dash else ""
    mk = ' marker-end="url(#__U___%s)"' % col
    ms = (' marker-start="url(#__U___%s)"' % col) if both else ""
    cl = "" if dash else ' class="%s" style="--L:%d"' % (cls, L)
    under = ('<path d="%s" fill="none" stroke="%s" stroke-width="%.1f" stroke-linecap="round" opacity=".28"%s/>'
             % (d, c, w * 2.8, cl)) if glow else ""
    return under + ('<path d="%s" fill="none" stroke="%s" stroke-width="%.1f" stroke-linecap="round"%s%s%s%s/>'
                    % (d, c, w, da, mk, ms, cl))


def cable(x1, y1, x2, y2, col="red", w=5, dash=False, glow=True):
    da = ' stroke-dasharray="12 9"' if dash else ""
    under = ('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round" opacity=".28"/>'
             % (x1, y1, x2, y2, COLS[col], w * 2.8)) if glow else ""
    return under + ('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="%.1f" stroke-linecap="round"%s/>'
                    % (x1, y1, x2, y2, COLS[col], w, da))


def xbad(x, y, r=24):
    k = r * .5
    return ('<g><circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="4"/>'
            '<path d="M%.1f %.1f l%.1f %.1f M%.1f %.1f l%.1f %.1f" stroke="#fff" stroke-width="%.1f" '
            'stroke-linecap="round"/></g>' % (x, y, r, RED, INK, x - k, y - k, 2 * k, 2 * k, x + k, y - k,
                                               -2 * k, 2 * k, r * .26))


def xcross(x, y, r=22):
    """Красный крест без круга (отказ канала)."""
    return ('<path d="M%.1f %.1f l%.1f %.1f M%.1f %.1f l%.1f %.1f" stroke="%s" stroke-width="%.1f" '
            'stroke-linecap="round" filter="url(#__U___gl)"/>'
            % (x - r, y - r, 2 * r, 2 * r, x + r, y - r, -2 * r, 2 * r, RED, r * .38))


def vgood(x, y, r=24):
    return ('<g><circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="4"/>'
            '<path d="M%.1f %.1f l%.1f %.1f l%.1f %.1f" stroke="#fff" stroke-width="%.1f" fill="none" '
            'stroke-linecap="round" stroke-linejoin="round"/></g>'
            % (x, y, r, GREEN, INK, x - r * .45, y, r * .32, r * .34, r * .62, -r * .7, r * .24))


def vminus(x, y, r=24):
    return ('<g><circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="4"/>'
            '<path d="M%.1f %.1f h%.1f" stroke="#fff" stroke-width="%.1f" stroke-linecap="round"/></g>'
            % (x, y, r, RED, INK, x - r * .5, y, r, r * .26))


def excl(x, y, r=24):
    return ('<g><circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="4"/>'
            '<path d="M%.1f %.1f v%.1f" stroke="#fff" stroke-width="%.1f" stroke-linecap="round"/>'
            '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff"/></g>'
            % (x, y, r, RED, INK, x, y - r * .5, r * .55, r * .22, x, y + r * .48, r * .13))


def dot(x, y, r=6, col="red"):
    return '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="2"/>' % (x, y, r, COLS[col], INK)


# ======================================================================
#  ИКОНКИ (контурные, в системе 0..48)
# ======================================================================

IC = {
    "search": '<circle cx="20" cy="20" r="11"/><path d="M28 28l11 11"/><circle cx="14" cy="34" r="3" class="f"/>'
              '<circle cx="30" cy="12" r="3" class="f"/><path d="M14 34L20 20L30 12"/>',
    "refresh": '<rect x="13" y="13" width="22" height="22"/><path d="M17 20h14M17 25h14M17 30h10"/>'
               '<path d="M8 22a16 16 0 0 1 22-14" class="r"/><path d="M40 26a16 16 0 0 1-22 14" class="r"/>',
    "fork": '<path d="M24 44V30C24 22 14 20 14 8" class="r"/><path d="M24 30c0-8 10-10 10-22" class="c"/>'
            '<path d="M9 13l5-6 5 6" class="r"/><path d="M29 13l5-6 5 6" class="c"/>',
    "gear": '<circle cx="24" cy="24" r="7"/><path d="M24 6v6M24 36v6M6 24h6M36 24h6M11 11l4 4M33 33l4 4M37 11l-4 4M15 33l-4 4"/>',
    "target": '<circle cx="24" cy="24" r="14"/><circle cx="24" cy="24" r="5" class="f"/><path d="M24 4v8M24 36v8M4 24h8M36 24h8"/>',
    "tree": '<rect x="18" y="6" width="12" height="9"/><rect x="5" y="33" width="12" height="9"/>'
            '<rect x="31" y="33" width="12" height="9"/><path d="M24 15v9M11 33v-9h26v9"/>',
    "wrench": '<path d="M30 8a9 9 0 0 0-8 12L8 34l6 6 14-14a9 9 0 0 0 12-8l-6 3-5-5z"/>',
    "warn": '<path d="M24 6L44 40H4z"/><path d="M24 18v11"/><circle cx="24" cy="34" r="1.8" class="f"/>',
    "chart": '<path d="M8 40h32"/><rect x="10" y="30" width="6" height="10" class="f"/>'
             '<rect x="20" y="22" width="6" height="18" class="f"/><rect x="30" y="12" width="6" height="28" class="f"/>',
    "cycle": '<path d="M10 20a15 15 0 0 1 26-6" /><path d="M38 28a15 15 0 0 1-26 6"/>'
             '<path d="M36 6v8h-8M12 42v-8h8"/>',
    "db": '<ellipse cx="24" cy="12" rx="14" ry="5"/><path d="M10 12v24c0 3 6 5 14 5s14-2 14-5V12"/>'
          '<path d="M10 24c0 3 6 5 14 5s14-2 14-5"/>',
    "shield": '<path d="M24 5l16 6v12c0 10-7 17-16 20C15 40 8 33 8 23V11z"/><path d="M17 24l5 5 9-10"/>',
    "docgear": '<path d="M10 5h18l8 8v24H10z"/><path d="M15 16h12M15 22h10"/><circle cx="34" cy="36" r="6" class="r"/>',
    "graph": '<circle cx="24" cy="9" r="4" class="f"/><circle cx="10" cy="36" r="4" class="f"/>'
             '<circle cx="38" cy="36" r="4" class="f"/><circle cx="24" cy="26" r="4" class="f"/>'
             '<path d="M24 13v9M21 28L12 33M27 28l9 5M10 36h28"/>',
    "globe": '<circle cx="24" cy="24" r="16"/><path d="M8 24h32M24 8c6 7 6 25 0 32M24 8c-6 7-6 25 0 32"/>',
    "port": '<rect x="7" y="9" width="34" height="30"/><path d="M15 31V21h4v-4h10v4h4v10z" class="f"/>',
    "net": '<circle cx="24" cy="10" r="5"/><circle cx="10" cy="36" r="5"/><circle cx="38" cy="36" r="5"/>'
           '<path d="M21 14L13 32M27 14l8 18M15 36h18"/>',
    "env": '<rect x="6" y="11" width="36" height="26"/><path d="M6 11l18 15 18-15"/>',
    "books": '<rect x="6" y="30" width="34" height="9" class="r"/><rect x="9" y="21" width="30" height="9" class="r"/>'
             '<rect x="12" y="12" width="26" height="9" class="r"/>',
}


def icon(x, y, name, s=1.0, col=INK, badge=True, bg="#0f2523", r=None):
    """Иконка в круглом бейдже (как в плакатах) или без него."""
    r = r or 34 * s
    sc = (r * 1.25) / 48.0
    g = ('<g transform="translate(%.1f %.1f) scale(%.3f)" fill="none" stroke="%s" stroke-width="%.1f" '
         'stroke-linecap="round" stroke-linejoin="round">%s</g>'
         % (x - 24 * sc, y - 24 * sc, sc, col, 3.4, IC[name]))
    g = g.replace('class="f"', 'fill="%s"' % col).replace('class="r"', 'stroke="%s"' % RED) \
         .replace('class="c"', 'stroke="%s"' % CYAN)
    if not badge:
        return g
    return ('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="4"/>'
            % (x, y, r, bg, INK)) + g


def finish(svg_body, vb="0 0 1600 900"):
    """Подставляет уникальные id маркеров и оборачивает в svg."""
    u = nid("P")
    body = svg_body.replace(' filter="url(#__U___gl)"', "").replace("__U__", u)
    return ('<svg class="pst" viewBox="%s" preserveAspectRatio="xMidYMid meet"><defs>%s</defs>%s</svg>'
            % (vb, defs_arrows(u), body))


def S(*parts):
    """Шаг появления внутри плаката."""
    return '<g class="step">%s</g>' % "".join(parts)
