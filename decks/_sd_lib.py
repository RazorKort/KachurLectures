# -*- coding: utf-8 -*-
"""Строительные блоки деки 2.5: панели, плакатные SVG-примитивы, покадровые сцены."""

import base64
import os

SL = []
_uid = [0]
ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_sd_assets")
_cache = {}


def uid(pref="u"):
    _uid[0] += 1
    return "%s%d" % (pref, _uid[0])


def b64(name):
    """data-URI картинки из _sd_assets (webp)."""
    if name not in _cache:
        with open(os.path.join(ASSETS, name), "rb") as f:
            _cache[name] = "data:image/webp;base64," + base64.b64encode(f.read()).decode()
    return _cache[name]


# ======================================================================
#  ФОН
# ======================================================================

def background():
    arcs = []
    for (x1, y1, x2, y2, c, op) in [
        (90, 700, 520, 620, "#dd3326", .45), (520, 620, 980, 660, "#dd3326", .35),
        (980, 660, 1380, 600, "#dd3326", .42), (200, 760, 760, 700, "#5ec6d8", .22),
        (760, 700, 1300, 740, "#5ec6d8", .20)]:
        mx, my = (x1 + x2) / 2, min(y1, y2) - 150
        arcs.append('<path d="M%d %d Q%d %d %d %d" fill="none" stroke="%s" stroke-width="2.2" '
                    'opacity="%.2f"/>' % (x1, y1, mx, my, x2, y2, c, op))
        arcs.append('<circle cx="%d" cy="%d" r="4" fill="%s" opacity="%.2f"/>' % (x1, y1, c, op))
        arcs.append('<circle cx="%d" cy="%d" r="4" fill="%s" opacity="%.2f"/>' % (x2, y2, c, op))
    return ('<div id="bg"><div class="glow"></div>'
            '<div class="city" style="background-image:url(%s)"></div>'
            '<svg class="arcs" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice">%s</svg>'
            '<div class="grain"></div></div>' % (b64("city.webp"), "".join(arcs)))


# ======================================================================
#  СЛАЙД И ПАНЕЛИ
# ======================================================================

def slide(label, body, scen=None, cover=False):
    at = ' data-scen="%s"' % scen if scen else ""
    cl = " cover-slide" if cover else ""
    SL.append('<section class="slide%s" data-label="%s"%s>%s</section>' % (cl, label, at, body))


def head(title, sub=None):
    s = '<p class="sub">%s</p>' % sub if sub else ""
    return ('<div class="head"><span class="mark"></span><div><h1 class="t">%s</h1>%s</div></div>'
            % (title, s))


def sc(*parts):
    return '<div class="sc">%s</div>' % "".join(parts)


def card(title=None, body="", num=None, cls="", plain=False):
    h = ""
    if title:
        n = '<span class="num">%s</span>' % num if num else ""
        h = '<div class="ch%s">%s<h3>%s</h3></div>' % (" non" if plain or num else "", n, title)
    return '<div class="c %s">%s%s</div>' % (cls, h, body)


def step(inner):
    return '<div class="step">%s</div>' % inner


def irow(icon, text, tone=""):
    return '<div class="ir %s"><span class="ib">%s</span><span>%s</span></div>' % (tone, ICON[icon], text)


def foot(text):
    return '<div class="foot"><i></i><span>%s</span><i></i></div>' % text


def band(text):
    return '<div class="band"><span class="bm"></span><p>%s</p></div>' % text


def tags(*t):
    return '<div class="tags">%s</div>' % "".join(t)


def tag(text, tone="", mono=False):
    cl = (tone + (" mono" if mono else "")).strip()
    return '<span class="tag %s">%s</span>' % (cl, text)


def ul(items, cls="ck"):
    return '<ul class="%s">%s</ul>' % (cls, "".join("<li>%s</li>" % i for i in items))


def table(headers, rows, cls=""):
    th = "".join('<th class="%s">%s</th>' % (h[1] if isinstance(h, tuple) else "",
                                             h[0] if isinstance(h, tuple) else h) for h in headers)
    tr = []
    for r in rows:
        rcls = ""
        if isinstance(r, tuple):
            r, rcls = r
        td = "".join('<td class="%s">%s</td>' % (c[1] if isinstance(c, tuple) else "",
                                                 c[0] if isinstance(c, tuple) else c) for c in r)
        tr.append('<tr class="%s">%s</tr>' % (rcls, td))
    return ('<div class="tw %s"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>'
            % (cls, th, "".join(tr)))


def cli(lines):
    out = []
    for ln in lines:
        if isinstance(ln, str):
            out.append('<span class="rem">%s</span>' % ln)
        else:
            pr, cmd = ln[0], ln[1]
            rem = ('   <span class="rem">%s</span>' % ln[2]) if len(ln) > 2 else ""
            out.append('<span class="pr">%s</span> <span class="cm">%s</span>%s' % (pr, cmd, rem))
    return ('<div class="cli"><div class="dots"><i></i><i></i><i></i></div><pre>%s</pre></div>'
            % "\n".join(out))


def shot(name, cls=""):
    """Плакат-референс из _sd_assets."""
    return '<div class="shot %s"><img src="%s" alt=""></div>' % (cls, b64(name))


# ======================================================================
#  SVG-ПРИМИТИВЫ В ПЛАКАТНОМ СТИЛЕ
# ======================================================================

INK = "#101b1a"
RED = "#dd3326"
CYAN = "#5ec6d8"
AMBER = "#e8a63c"
CREAM = "#f4ecda"
DIMI = "#9fb8b4"

ICON = {
    "doc":   '<svg viewBox="0 0 24 24"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/><path d="M9 12h6M9 16h6"/></svg>',
    "gear":  '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg>',
    "pin":   '<svg viewBox="0 0 24 24"><path d="M12 21s7-6 7-11a7 7 0 10-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>',
    "arr":   '<svg viewBox="0 0 24 24"><path d="M4 12h15"/><path d="M13 6l6 6-6 6"/></svg>',
    "db":    '<svg viewBox="0 0 24 24"><ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3.1 3 7 3s7-1.3 7-3V6"/><path d="M5 12v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6"/></svg>',
    "bars":  '<svg viewBox="0 0 24 24"><path d="M5 20V12M12 20V5M19 20v-5"/></svg>',
    "stop":  '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M6.2 6.2l11.6 11.6"/></svg>',
    "clock": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M12 7v5.4l3.4 2"/></svg>',
    "net":   '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M3.4 12h17.2M12 3.4c4 4.6 4 11.6 0 17.2M12 3.4c-4 4.6-4 11.6 0 17.2"/></svg>',
    "shield":'<svg viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 4.4-3 8-7 9-4-1-7-4.6-7-9V6z"/><path d="M8.8 12l2.2 2.2L15.4 10"/></svg>',
    "bolt":  '<svg viewBox="0 0 24 24"><path d="M13 3L5 13h6l-1 8 8-10h-6z"/></svg>',
    "loop":  '<svg viewBox="0 0 24 24"><path d="M4 12a8 8 0 0113.6-5.7L20 8"/><path d="M20 4v4h-4"/><path d="M20 12a8 8 0 01-13.6 5.7L4 16"/><path d="M4 20v-4h4"/></svg>',
    "cloud": '<svg viewBox="0 0 24 24"><path d="M7 18h10a4 4 0 000-8 5.5 5.5 0 00-10.6 1.6A3.3 3.3 0 007 18z"/></svg>',
    "key":   '<svg viewBox="0 0 24 24"><circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v4M15 12v3"/></svg>',
    "eye":   '<svg viewBox="0 0 24 24"><path d="M2.5 12S6 6 12 6s9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6z"/><circle cx="12" cy="12" r="2.8"/></svg>',
    "scale": '<svg viewBox="0 0 24 24"><path d="M12 4v16M6 8h12M4 8l-2 6h4zM20 8l-2 6h4z"/></svg>',
    "box":   '<svg viewBox="0 0 24 24"><path d="M4 8l8-4 8 4v8l-8 4-8-4z"/><path d="M4 8l8 4 8-4M12 12v8"/></svg>',
    "sum":   '<svg viewBox="0 0 24 24"><path d="M6 5h12L11 12l7 7H6"/></svg>',
    "wifi":  '<svg viewBox="0 0 24 24"><path d="M3.5 9.5a13 13 0 0117 0M6.8 13a8.4 8.4 0 0110.4 0M10 16.4a3.6 3.6 0 014 0"/><circle cx="12" cy="19.6" r="1"/></svg>',
    "users": '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.4"/><path d="M17 14c2.6 0 4.6 2 4.6 4.6"/></svg>',
}


def router(x, y, w=92, label=None, cls="", tone="dark"):
    """Чёрный маршрутизатор с антеннами и красными светодиодами (как на плакатах)."""
    h = w * .30
    ant = w * .40
    leds = "".join('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.5" fill="%s"/>'
                   % (x - w * .22 + i * w * .11, y - h * .06, w * .055, h * .17, RED)
                   for i in range(5))
    lab = ""
    if label:
        lw = max(44, 17 + len(label) * 11)
        lab = ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="23" fill="%s" stroke="%s" stroke-width="2.5"/>'
               '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="14.5" font-weight="700" '
               'fill="%s">%s</text></g>'
               % (x - lw / 2, y + h / 2 + 7, lw, CREAM, INK, x, y + h / 2 + 23, INK, label))
    body = "#1a2726" if tone == "dark" else "#2d3b39"
    return ('<g class="%s">'
            '<path d="M%.1f %.1f l-%.1f -%.1f M%.1f %.1f l%.1f -%.1f" stroke="%s" stroke-width="5" '
            'stroke-linecap="round"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="3"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#2b3a38"/>'
            '%s%s</g>'
            % (cls,
               x - w * .30, y - h / 2, w * .10, ant, x + w * .30, y - h / 2, w * .10, ant, "#1a2726",
               x - w / 2, y - h / 2, w, h, h * .22, body, INK,
               x - w / 2 + 4, y - h / 2 + 3.5, w - 8, h * .30, 2,
               leds, lab))


def pc(x, y, s=1.0, label=None):
    w, h = 54 * s, 38 * s
    lab = ('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="700" fill="%s">%s</text>'
           % (x, y + h / 2 + 20 * s, 13 * s, CREAM, label)) if label else ""
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#13302e" stroke="%s" '
            'stroke-width="3"/><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#2b6f7d"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s"/>%s</g>'
            % (x - w / 2, y - h / 2, w, h, INK,
               x - w / 2 + 5 * s, y - h / 2 + 5 * s, w - 10 * s, h - 10 * s,
               x - 9 * s, y + h / 2, 18 * s, 5 * s, INK, lab))


def server(x, y, s=1.0, label=None):
    w, h = 40 * s, 62 * s
    rows = "".join('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#2b3a38"/>'
                   '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                   % (x - w / 2 + 4 * s, y - h / 2 + (7 + i * 14) * s, w - 8 * s, 9 * s,
                      x + w / 2 - 9 * s, y - h / 2 + (11.5 + i * 14) * s, 2.2 * s, RED)
                   for i in range(4))
    lab = ('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="700" fill="%s">%s</text>'
           % (x, y + h / 2 + 18 * s, 13 * s, CREAM, label)) if label else ""
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="#13302e" stroke="%s" '
            'stroke-width="3"/>%s%s</g>'
            % (x - w / 2, y - h / 2, w, h, INK, rows, lab))


def cloudnet(x, y, w, h, label, sub=None):
    """Облако-сеть кремового цвета с жёсткой обводкой."""
    # исходный контур нарисован в системе 40..162 по X и 36..104 по Y
    sx, sy = w / 126.0, h / 70.0
    tx, ty = x - w / 2 - 38 * sx, y - h / 2 - 34 * sy
    d = ("M40 104 A26 26 0 0 1 44 53 A40 40 0 0 1 116 40 "
         "A30 30 0 0 1 160 58 A24 24 0 0 1 162 104 Z")
    s = ('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="12.5" font-weight="600" fill="%s">%s</text>'
         % (x, y + 18, "#3b4b48", sub)) if sub else ""
    dy = 0 if sub else 7
    return ('<g><g transform="translate(%.2f %.2f) scale(%.4f %.4f)">'
            '<path d="%s" fill="%s" stroke="%s" stroke-width="%.1f" stroke-linejoin="round"/></g>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="14.5" font-weight="700" fill="%s">%s</text>%s</g>'
            % (tx, ty, sx, sy, d, CREAM, INK, 3 / max(sx, sy), x, y + dy, INK, label, s))


def chip(x, y, text, tone="cream", fs=14.5, w=None, h=28, mono=True):
    """Прямоугольная подпись-плашка."""
    fill = {"cream": CREAM, "red": RED, "cyan": "#bfe9f1", "amber": "#f6dfae", "dark": "#15302e"}[tone]
    ink = "#fff" if tone in ("red", "dark") else INK
    ww = w or max(46, int(len(text) * fs * (.56 if mono else .5)) + 20)
    fam = ' font-family="JetBrains Mono,Consolas,monospace"' if mono else ""
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="2.5"/>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="700" fill="%s"%s>%s</text></g>'
            % (x - ww / 2, y - h / 2, ww, h, fill, INK, x, y + fs * .36, fs, ink, fam, text))


def title_plate(x, y, text, w=None, fs=20):
    ww = w or int(len(text) * fs * .54) + 30
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="3"/>'
            '<rect x="%.1f" y="%.1f" width="7" height="%.1f" fill="%s"/>'
            '<text x="%.1f" y="%.1f" font-size="%.1f" font-weight="700" fill="%s" '
            'font-family="Oswald,Roboto Condensed,sans-serif" letter-spacing=".02em">%s</text></g>'
            % (x, y, ww, fs + 16, CREAM, INK, x + 6, y + 6, fs + 4, RED,
               x + 20, y + fs + 2, fs, INK, text.upper()))


def arrow(x1, y1, x2, y2, tone="red", w=5, dash=False, curve=0, cls="", mid=None):
    col = {"red": RED, "cyan": CYAN, "amber": AMBER, "cream": CREAM, "dim": "#6f8d88"}[tone]
    if curve:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - curve
        d = "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x1, y1, mx, my, x2, y2)
        L = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5 * 1.2) + 24
    else:
        d = "M%.1f %.1f L%.1f %.1f" % (x1, y1, x2, y2)
        L = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5) + 14
    da = ' stroke-dasharray="11 9"' if dash else ""
    lab = ""
    if mid:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - (curve * .5 if curve else 0)
        lab = chip(mx, my - 2, mid, "cream", 13)
    return ('<path class="%s" d="%s" stroke="%s" stroke-width="%d" fill="none" stroke-linecap="round"%s '
            'marker-end="url(#ah_%s)" style="--L:%d"/>%s' % (cls, d, col, w, da, tone, L, lab))


def xmark(x, y, r=17):
    k = r * .55
    return ('<g><circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="3"/>'
            '<path d="M%.1f %.1f l%.1f %.1f M%.1f %.1f l%.1f %.1f" stroke="#fff" stroke-width="4.5" '
            'stroke-linecap="round"/></g>'
            % (x, y, r, RED, INK, x - k, y - k, 2 * k, 2 * k, x + k, y - k, -2 * k, 2 * k))


def okmark(x, y, r=17):
    return ('<g><circle cx="%.1f" cy="%.1f" r="%.1f" fill="#4fb07a" stroke="%s" stroke-width="3"/>'
            '<path d="M%.1f %.1f l%.1f %.1f l%.1f %.1f" stroke="#fff" stroke-width="4.2" fill="none" '
            'stroke-linecap="round" stroke-linejoin="round"/></g>'
            % (x, y, r, INK, x - r * .42, y, r * .32, r * .34, r * .62, -r * .68))


def note(x, y, text, w=None, fs=13.5, tone="cream"):
    """Многострочная выноска: строки разделяются «|»."""
    lines = text.split("|")
    fill = {"cream": CREAM, "cyan": "#bfe9f1", "amber": "#f6dfae", "red": "#f7cfca"}[tone]
    ww = w or max(100, int(max(len(l) for l in lines) * fs * .52) + 24)
    hh = 12 + len(lines) * (fs + 5)
    tt = "".join('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="600" '
                 'fill="%s">%s</text>' % (x, y + 10 + i * (fs + 5) + fs * .6, fs, INK, l)
                 for i, l in enumerate(lines))
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="2.5"/>'
            '%s</g>' % (x - ww / 2, y, ww, hh, fill, INK, tt))


def txt(x, y, text, fs=14, color=CREAM, anchor="middle", weight=700, mono=False):
    fam = ' font-family="JetBrains Mono,Consolas,monospace"' if mono else ""
    return ('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="%.1f" font-weight="%d" fill="%s"%s>%s</text>'
            % (x, y, anchor, fs, weight, color, fam, text))


def link(x1, y1, x2, y2, w=4, color="#7d9c97", dash=False):
    da = ' stroke-dasharray="10 8"' if dash else ""
    return ('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="%d" stroke-linecap="round"%s/>'
            % (x1, y1, x2, y2, color, w, da))


def packet(x, y, label="IP", w=42, cls="", pid=None):
    i = ' id="%s"' % pid if pid else ""
    return ('<g class="%s"%s transform="translate(%.1f %.1f)">'
            '<rect x="%.1f" y="-13" width="%.1f" height="26" fill="%s" stroke="%s" stroke-width="2.5"/>'
            '<text x="0" y="5" text-anchor="middle" font-size="13" font-weight="700" fill="#fff" '
            'font-family="JetBrains Mono,Consolas,monospace">%s</text></g>'
            % (cls, i, x, y, -w / 2, w, RED, INK, label))


def _defs():
    out = []
    for name, col in (("red", RED), ("cyan", CYAN), ("amber", AMBER), ("cream", CREAM), ("dim", "#6f8d88")):
        out.append('<marker id="ah_%s" viewBox="0 0 10 10" refX="8.4" refY="5" markerWidth="4.2" '
                   'markerHeight="4.2" orient="auto-start-reverse">'
                   '<path d="M0 0L10 5L0 10z" fill="%s"/></marker>' % (name, col))
    return "".join(out)


def fig(view, body, cls="", extra_defs=""):
    """SVG-фигура с уникальными id маркеров."""
    u = uid("k")
    defs = _defs()
    for nm in ("red", "cyan", "amber", "cream", "dim"):
        defs = defs.replace('id="ah_%s"' % nm, 'id="ah_%s_%s"' % (nm, u))
        body = body.replace("url(#ah_%s)" % nm, "url(#ah_%s_%s)" % (nm, u))
    return ('<div class="figwrap"><svg class="fig %s" viewBox="%s"><defs>%s%s</defs>%s</svg></div>'
            % (cls, view, defs, extra_defs, body))


# ======================================================================
#  ПОКАДРОВАЯ СЦЕНА: ← / → по кадрам, подпись к каждому кадру
# ======================================================================

def scene(view, base, frames, title=None):
    """frames: список (подпись, svg-слой). Кадры накапливаются: кадр k показывает слои 0..k."""
    u = uid("sx")
    defs = _defs()
    for nm in ("red", "cyan", "amber", "cream", "dim"):
        defs = defs.replace('id="ah_%s"' % nm, 'id="ah_%s_%s"' % (nm, u))
    layers = []
    caps = []
    for i, (cap, body) in enumerate(frames):
        for nm in ("red", "cyan", "amber", "cream", "dim"):
            body = body.replace("url(#ah_%s)" % nm, "url(#ah_%s_%s)" % (nm, u))
        layers.append('<g class="fr" data-fr="%d">%s</g>' % (i, body))
        caps.append(cap)
    for nm in ("red", "cyan", "amber", "cream", "dim"):
        base = base.replace("url(#ah_%s)" % nm, "url(#ah_%s_%s)" % (nm, u))
    caps_js = "|@|".join(caps)
    t = '<div class="sxt">%s</div>' % title if title else ""
    return ('<div class="sx" data-caps="%s">%s<div class="sxv">'
            '<svg viewBox="%s"><defs>%s</defs>%s%s</svg></div>'
            '<div class="sxb"><button class="sxp" type="button">← Назад</button>'
            '<button class="sxn2" type="button">Вперёд →</button>'
            '<span class="sxn">1/%d</span><span class="sxc"></span>'
            '<button class="sxr" type="button">⟲</button></div></div>'
            % (caps_js, t, view, defs, base, "".join(layers), len(frames)))


# ======================================================================
#  ТЕСТЫ И ЗАДАЧИ
# ======================================================================

def quiz(n, question, options, correct, explain):
    """options: список строк; correct: индекс правильного."""
    opts = "".join('<button type="button" data-ok="%d">%s</button>' % (1 if i == correct else 0, o)
                   for i, o in enumerate(options))
    return ('<div class="q" data-q="1"><div class="qt"><i>%s</i><span>%s</span></div>'
            '<div class="opts">%s</div><div class="ex">%s</div></div>' % (n, question, opts, explain))


def task(n, question, answer, hint, placeholder="ответ"):
    return ('<div class="q" data-task="%s"><div class="qt"><i>%s</i><span>%s</span></div>'
            '<div class="inp"><input type="text" placeholder="%s" spellcheck="false">'
            '<button class="chk" type="button">Проверить</button>'
            '<span class="verdict"></span></div><div class="ex">%s</div></div>'
            % (answer, n, question, placeholder, hint))
