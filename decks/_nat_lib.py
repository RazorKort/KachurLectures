# -*- coding: utf-8 -*-
"""Строительные блоки деки «IP-сервисы: DHCP, NAT, NTP» (раздел 2.6).

Каркас (слайд, карточки, сцены с кнопками, тест/задачи) берётся из _sw_lib,
здесь — фон «глобус + созвездие сети» под стиль инфографик 2.6, спрайт иконок
из атласа SVG и плашки этапов как на фото.
"""

import math
import os
import random

from _sw_lib import SL, uid, _esc  # noqa: F401  (SL — общий список слайдов)

HERE = os.path.dirname(os.path.abspath(__file__))


# ======================================================================
#  СЛАЙД с вариантом фона
# ======================================================================

def slide(label, body, bg="a", cover=False):
    cl = " cover-slide" if cover else ""
    SL.append('<section class="slide%s" data-bg="%s" data-label="%s">%s</section>'
              % (cl, bg, _esc(label), body))


def sc(*blocks):
    return '<div class="sc"><div class="wrap">%s</div></div>' % "".join(blocks)


def head(title, sub="", kick=""):
    k = '<p class="kick">%s</p>' % kick if kick else ""
    s = '<p class="sub">%s</p>' % sub if sub else ""
    return '<div class="head">%s<h1 class="t">%s</h1>%s</div>' % (k, title, s)


def pill(n, title, text="", tone="y", step=False):
    """Глянцевая плашка этапа: «① DHCPDISCOVER — клиент ищет сервер»."""
    t = '<span class="pt">%s</span>' % text if text else ""
    h = ('<div class="pill %s"><b class="pn">%s</b><span class="ph">%s</span>%s</div>'
         % ({'c': 'cy'}.get(tone, tone), n, title, t))
    return '<div class="step">%s</div>' % h if step else h


def kv(rows):
    """Строки «Источник: … / Назначение: …» как в пакетах на инфографиках."""
    out = []
    for lab, val, tone in rows:
        out.append('<div class="kv"><span class="kl">%s</span><span class="kvv %s">%s</span></div>'
                   % (lab, {'c': 'cy'}.get(tone, tone), val))
    return '<div class="kvs">%s</div>' % "".join(out)


def big(text, tone=""):
    return '<div class="bigline %s">%s</div>' % (tone, text)


# ======================================================================
#  СПРАЙТ ИКОНОК ИЗ АТЛАСА SVG (decks/svg-atlas.html → _sd_assets/sym)
# ======================================================================

def sprite():
    with open(os.path.join(HERE, "_sd_assets", "sym", "devices.svgsym"), encoding="utf-8") as fh:
        sym = fh.read()
    # перекраска бирюзы атласа в синий неон инфографик 2.6
    for a, b in (("#17707e", "#1a4f9a"), ("#4fd0e2", "#5fb8ff"), ("#28c7b2", "#3aa0ff"),
                 ("#2f9184", "#1d4f9c"), ("#3aa89a", "#2a6fc4"), ("#4cc2b1", "#4a9cf0"),
                 ("#5dd1c2", "#7cc4ff"), ("#d3dedc", "#d8ecff"), ("#cfe1df", "#bfe6ff")):
        sym = sym.replace(a, b)
    return ('<svg id="sprite" aria-hidden="true" style="position:absolute;width:0;height:0;'
            'overflow:hidden"><defs>%s</defs></svg>' % sym)


# ======================================================================
#  ФОН: глобус в сетке связей, созвездия, бегущие импульсы
# ======================================================================

def _globe(cx, cy, r, rnd, gid):
    o = []
    o.append('<circle cx="%d" cy="%d" r="%d" fill="url(#%s_halo)"/>' % (cx, cy, r * 1.45, gid))
    o.append('<circle cx="%d" cy="%d" r="%d" fill="url(#%s_core)"/>' % (cx, cy, r, gid))
    o.append('<clipPath id="%s_cl"><circle cx="%d" cy="%d" r="%d"/></clipPath>' % (gid, cx, cy, r))
    o.append('<g clip-path="url(#%s_cl)">' % gid)
    # параллели
    for k in range(-5, 6):
        y = cy + r * k / 6.0
        rx = r * math.sqrt(max(0, 1 - (k / 6.0) ** 2))
        o.append('<ellipse cx="%d" cy="%.1f" rx="%.1f" ry="%.1f" fill="none" stroke="#3fb8ff" '
                 'stroke-width="1" opacity=".28"/>' % (cx, y, rx, rx * .16))
    # меридианы (вращаются)
    o.append('<g class="spin">')
    for k in range(0, 12):
        a = k * 15
        rx = abs(r * math.cos(math.radians(a)))
        o.append('<ellipse cx="%d" cy="%d" rx="%.1f" ry="%d" fill="none" stroke="#3fb8ff" '
                 'stroke-width="1" opacity=".26"/>' % (cx, cy, rx, r))
    o.append('</g>')
    # огни городов + связи между ними
    pts = []
    for _ in range(70):
        u, v = rnd.uniform(-1, 1), rnd.uniform(-1, 1)
        if u * u + v * v > .9:
            continue
        pts.append((cx + u * r, cy + v * r))
    for i, (x, y) in enumerate(pts):
        for (x2, y2) in pts[i + 1:i + 4]:
            if (x - x2) ** 2 + (y - y2) ** 2 < (r * .45) ** 2:
                o.append('<path d="M%.1f %.1fQ%.1f %.1f %.1f %.1f" fill="none" stroke="#ffb347" '
                         'stroke-width="1.1" opacity=".5"/>'
                         % (x, y, (x + x2) / 2, min(y, y2) - 18, x2, y2))
    for (x, y) in pts:
        c = "#ffcf6b" if rnd.random() < .6 else "#7fe3ff"
        o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" class="tw" style="animation-delay:%.1fs"/>'
                 % (x, y, rnd.uniform(1.4, 3.2), c, rnd.uniform(0, 4)))
    o.append('</g>')
    o.append('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="#6fdcff" stroke-width="2.5" opacity=".75" '
             'filter="url(#%s_bl)"/>' % (cx, cy, r, gid))
    # орбиты-дуги со светящимися точками
    for k, (rr, tilt, op) in enumerate([(1.18, -18, .45), (1.32, 12, .3)]):
        o.append('<ellipse class="orb" cx="%d" cy="%d" rx="%.1f" ry="%.1f" transform="rotate(%d %d %d)" '
                 'fill="none" stroke="#5ad0ff" stroke-width="1.4" stroke-dasharray="3 9" opacity="%.2f"/>'
                 % (cx, cy, r * rr, r * rr * .34, tilt, cx, cy, op))
    return "".join(o)


def _constellation(rnd, x0, y0, w, h, n, col="#5fd3ff"):
    pts = [(x0 + rnd.uniform(0, w), y0 + rnd.uniform(0, h)) for _ in range(n)]
    o = []
    for i, (x, y) in enumerate(pts):
        near = sorted(pts, key=lambda p: (p[0] - x) ** 2 + (p[1] - y) ** 2)[1:3]
        for (x2, y2) in near:
            o.append('<path d="M%.1f %.1fL%.1f %.1f" stroke="%s" stroke-width=".9" opacity=".32"/>'
                     % (x, y, x2, y2, col))
    for (x, y) in pts:
        o.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" opacity=".85" class="tw" '
                 'style="animation-delay:%.1fs"/>' % (x, y, rnd.uniform(1.2, 2.6), col, rnd.uniform(0, 5)))
    return "".join(o)


def _pulses(rnd, n, y0, y1):
    """Световые импульсы по «трассам» платы."""
    o = []
    for i in range(n):
        y = rnd.randint(y0, y1)
        x = rnd.randint(-100, 900)
        L = rnd.randint(300, 700)
        d = "M%d %d h%d l40 40 h%d" % (x, y, L // 2, L // 2)
        o.append('<path d="%s" fill="none" stroke="#1f5d99" stroke-width="1.2" opacity=".45"/>' % d)
        o.append('<path d="%s" fill="none" stroke="#7fe8ff" stroke-width="2.2" class="run" '
                 'style="animation-delay:%.1fs" stroke-dasharray="60 1400"/>' % (d, rnd.uniform(0, 7)))
    return "".join(o)


def _defs(g):
    return (
        '<radialGradient id="%s_core" cx=".38" cy=".34" r=".75">'
        '<stop offset="0" stop-color="#1b5fae"/><stop offset=".55" stop-color="#0b2d63"/>'
        '<stop offset="1" stop-color="#04122e"/></radialGradient>'
        '<radialGradient id="%s_halo" cx=".5" cy=".5" r=".5">'
        '<stop offset=".6" stop-color="#2aa8ff" stop-opacity=".30"/>'
        '<stop offset="1" stop-color="#2aa8ff" stop-opacity="0"/></radialGradient>'
        '<filter id="%s_bl" x="-20%%" y="-20%%" width="140%%" height="140%%">'
        '<feGaussianBlur stdDeviation="4"/></filter>' % (g, g, g))


def _layer(key, body, gid):
    return ('<svg class="bgl" data-bgk="%s" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" '
            'aria-hidden="true"><defs>%s</defs>%s</svg>' % (key, _defs(gid), body))


def background():
    rnd = random.Random(2606)
    base = ('<rect width="1600" height="900" fill="url(#bgsky)"/>'
            '<rect width="1600" height="900" fill="url(#bggrid)"/>')
    layers = []
    # A — глобус справа сверху, как на заголовках инфографик
    layers.append(_layer("a", _pulses(rnd, 7, 520, 880) + _constellation(rnd, 760, 20, 820, 380, 34)
                         + _globe(1330, 210, 240, rnd, "ga"), "ga"))
    # B — глобус слева снизу
    layers.append(_layer("b", _pulses(rnd, 6, 60, 420) + _constellation(rnd, 20, 420, 700, 460, 30)
                         + _globe(190, 760, 300, rnd, "gb"), "gb"))
    # C — горизонт планеты снизу + созвездие сверху
    layers.append(_layer("c", _constellation(rnd, 0, 0, 1600, 420, 60)
                         + _globe(800, 1650, 980, rnd, "gc"), "gc"))
    # D — два малых глобуса по краям
    layers.append(_layer("d", _pulses(rnd, 8, 300, 640) + _globe(110, 120, 150, rnd, "gd1")
                         + _globe(1500, 800, 190, rnd, "gd2"), "gd1") .replace(
        "</defs>", _defs("gd2") + "</defs>", 1))
    return (
        '<svg id="bg" viewBox="0 0 1600 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
        '<defs><linearGradient id="bgsky" x1="0" y1="0" x2=".3" y2="1">'
        '<stop offset="0" stop-color="#020817"/><stop offset=".5" stop-color="#051432"/>'
        '<stop offset="1" stop-color="#081d45"/></linearGradient>'
        '<pattern id="bggrid" width="80" height="80" patternUnits="userSpaceOnUse">'
        '<path d="M0 40H80M40 0V80" stroke="#1a4a85" stroke-width=".8" opacity=".28"/>'
        '<circle cx="40" cy="40" r="1.8" fill="#3fc0ff" opacity=".3"/></pattern></defs>'
        + base + '</svg>' + "".join(layers) +
        '<div id="bgfx"><i class="blob b1"></i><i class="blob b2"></i><i class="blob b3"></i></div>')
