# -*- coding: utf-8 -*-
"""Строительные блоки деки «Маршрутизаторы» (2.3): неоновый город, стеклянные карточки,
   SVG-устройства в фиолетовой гамме референсных иллюстраций."""

import base64
import os
import random

SL = []
_uid = [0]

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_r23assets")
_cache = {}


def uid(pref="u"):
    _uid[0] += 1
    return "%s%d" % (pref, _uid[0])


def b64(name):
    if name not in _cache:
        with open(os.path.join(ASSETS, name + ".webp"), "rb") as fh:
            _cache[name] = "data:image/webp;base64," + base64.b64encode(fh.read()).decode()
    return _cache[name]


# ======================================================================
#  ФОН: неоновый город, сетка данных, орбита, частицы
# ======================================================================

def background():
    rnd = random.Random(2305)

    def skyline(x0, y0, w, h, n, op, col):
        """Силуэт города из прямоугольных башен."""
        out = []
        x = x0
        while x < x0 + w:
            bw = rnd.randint(16, 42)
            bh = rnd.randint(int(h * 0.26), h)
            out.append('<rect x="%d" y="%d" width="%d" height="%d" rx="3" fill="%s" opacity="%.2f"/>'
                       % (x, y0 - bh, bw, bh, col, op))
            # окна-искры
            for i in range(rnd.randint(1, 4)):
                wx = x + rnd.randint(4, max(5, bw - 8))
                wy = y0 - bh + rnd.randint(8, max(10, bh - 10))
                out.append('<rect class="twk" x="%d" y="%d" width="3.4" height="4.6" fill="#b9a6ff"/>'
                           % (wx, wy))
            x += bw + rnd.randint(5, 16)
        return "".join(out)

    # сеть-созвездие
    nodes = [(rnd.randint(60, 1380), rnd.randint(90, 760)) for _ in range(26)]
    links = []
    for i, (x1, y1) in enumerate(nodes):
        for (x2, y2) in nodes[i + 1:]:
            d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** .5
            if d < 215:
                links.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#9b7bff" '
                             'stroke-width="1" opacity=".16"/>' % (x1, y1, x2, y2))
    dots = "".join('<circle class="twk" cx="%d" cy="%d" r="2.6" fill="#8a63ff"/>' % (x, y)
                   for (x, y) in nodes)

    # потоки данных
    flows = []
    for (x1, y1, x2, y2, c) in [(0, 300, 1440, 220, "#6d4aff"), (0, 520, 1440, 610, "#1fb6e8"),
                                (0, 160, 1440, 120, "#d64ae8"), (0, 700, 1440, 660, "#6d4aff")]:
        flows.append('<path class="flow" d="M%d %d Q720 %d %d %d" stroke="%s" stroke-width="2.4" '
                     'fill="none" opacity=".5" stroke-linecap="round"/>'
                     % (x1, y1, (y1 + y2) // 2 - 70, x2, y2, c))

    # восходящие частицы
    parts = []
    for i in range(16):
        parts.append('<circle class="rise" cx="%d" cy="%d" r="%.1f" fill="%s" opacity=".5"/>'
                     % (rnd.randint(30, 1410), rnd.randint(620, 900), rnd.uniform(1.6, 3.4),
                        rnd.choice(["#8a63ff", "#1fb6e8", "#d64ae8"])))

    # орбиты вокруг «глобуса»
    orb = []
    for (rx, ry, rot, op) in [(188, 188, 0, .30), (188, 72, -18, .34), (188, 118, 22, .26),
                              (150, 150, 0, .20)]:
        orb.append('<ellipse cx="1190" cy="300" rx="%d" ry="%d" fill="none" stroke="#7a5cff" '
                   'stroke-width="1.5" opacity="%.2f" transform="rotate(%d 1190 300)"/>'
                   % (rx, ry, op, rot))
    mer = []
    for k in range(5):
        mer.append('<ellipse cx="0" cy="0" rx="%d" ry="150" fill="none" stroke="#9b7bff" '
                   'stroke-width="1.2" opacity=".30" transform="rotate(%d)"/>' % (40 + k * 28, 0))

    return """<svg id="bg" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#f6f4ff"/><stop offset=".45" stop-color="#eeeaff"/>
    <stop offset="1" stop-color="#e6e9ff"/>
  </linearGradient>
  <radialGradient id="gl1" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#b9a6ff" stop-opacity=".55"/><stop offset="1" stop-color="#b9a6ff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="gl2" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#86e3fb" stop-opacity=".5"/><stop offset="1" stop-color="#86e3fb" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="gl3" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#f0a8ff" stop-opacity=".45"/><stop offset="1" stop-color="#f0a8ff" stop-opacity="0"/>
  </radialGradient>
  <radialGradient id="orbg" cx=".38" cy=".32" r=".72">
    <stop offset="0" stop-color="#cfc3ff" stop-opacity=".75"/>
    <stop offset=".65" stop-color="#9b7bff" stop-opacity=".30"/>
    <stop offset="1" stop-color="#6d4aff" stop-opacity=".05"/>
  </radialGradient>
  <pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse">
    <path d="M48 0H0V48" fill="none" stroke="#8a63ff" stroke-width=".7" opacity=".13"/>
  </pattern>
  <linearGradient id="fade" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity=".92"/>
  </linearGradient>
</defs>
<rect width="1440" height="900" fill="url(#sky)"/>
<rect width="1440" height="900" fill="url(#grid)"/>
<ellipse class="drift" cx="180" cy="130" rx="330" ry="230" fill="url(#gl1)"/>
<ellipse class="drift2" cx="1300" cy="760" rx="330" ry="240" fill="url(#gl3)"/>
<ellipse class="drift" cx="760" cy="880" rx="420" ry="200" fill="url(#gl2)"/>
<g>%s</g>
<g>%s%s</g>
<g opacity=".9">%s</g>
<circle cx="1190" cy="300" r="150" fill="url(#orbg)"/>
<g class="spin" transform="translate(1190 300)">%s</g>
<g>%s</g>
<g>%s</g>
<g>%s</g>
<rect y="640" width="1440" height="260" fill="url(#fade)"/>
<g>%s</g>
</svg>""" % (
        "".join(flows),
        "".join(links), dots,
        "".join(orb),
        "".join(mer),
        skyline(-20, 900, 760, 230, 0, .17, "#5b3fd6"),
        skyline(700, 900, 780, 300, 0, .13, "#4a35b8"),
        "".join(parts),
        skyline(-10, 900, 1460, 150, 0, .10, "#3b2a90"),
    )


# ======================================================================
#  КАРКАС СЛАЙДА
# ======================================================================

def slide(label, body, scen=None, cover=False):
    at = ' data-scen="%s"' % scen if scen else ""
    cl = " cover-slide" if cover else ""
    SL.append('<section class="slide%s" data-label="%s"%s>%s</section>' % (cl, label, at, body))


SPARK = ('<svg class="spark" viewBox="0 0 66 44" aria-hidden="true" fill="none">'
         '<path d="M6 36 L22 8" stroke="#6d4aff" stroke-width="7" stroke-linecap="round" opacity=".85"/>'
         '<path d="M28 38 L42 12" stroke="#d64ae8" stroke-width="7" stroke-linecap="round" opacity=".8"/>'
         '<path d="M48 34 L60 14" stroke="#1fb6e8" stroke-width="7" stroke-linecap="round" opacity=".8"/></svg>')


def head(title, sub=None, spark=True):
    s = '<p class="sub">%s</p>' % sub if sub else ""
    k = SPARK if spark else ""
    return '<div class="head"><div><h1 class="t">%s</h1>%s</div>%s</div>' % (title, s, k)


def sc(*parts):
    return '<div class="sc">%s</div>' % "".join(parts)


def g(cls, *parts, **kw):
    grow = " grow" if kw.get("grow") else ""
    st = ' style="%s"' % kw["style"] if kw.get("style") else ""
    return '<div class="g %s%s"%s>%s</div>' % (cls, grow, st, "".join(parts))


def col(*parts):
    return '<div class="col">%s</div>' % "".join(parts)


NUMTONE = {"vio": "", "cya": "c2", "mag": "m", "grn": "g", "amb": "a", "red": "r",
           "ind": "i", "w": "", "dark": "", "": ""}


def card(title=None, body="", num=None, tone="", cls=""):
    h = ""
    if title:
        n = '<span class="num %s">%s</span>' % (NUMTONE.get(tone, ""), num) if num else ""
        h = '<div class="ch">%s<h3>%s</h3></div>' % (n, title)
    return '<div class="c %s %s">%s%s</div>' % (tone, cls, h, body)


def step(inner):
    return '<div class="step">%s</div>' % inner


def steps(*inner):
    return "".join('<div class="step">%s</div>' % i for i in inner)


def irow(icon, text, tone=""):
    return '<div class="ir %s"><span class="ib">%s</span><span>%s</span></div>' % (tone, ICON[icon], text)


def foot(text, tone=""):
    sym = {"": "i", "warn": "!", "ok": "✓", "note": "?"}[tone]
    return '<div class="foot %s"><i>%s</i><span>%s</span></div>' % (tone, sym, text)


def tag(text, tone="", mono=False):
    cl = (tone + (" mono" if mono else "")).strip()
    return '<span class="tag %s">%s</span>' % (cl, text)


def tags(*t):
    return '<div class="tags">%s</div>' % "".join(t)


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


def cli(lines, typ=False, cap=None):
    """lines: ('prompt','команда'[,'комментарий']) | 'текст вывода' | ('>>', 'выделенный вывод')."""
    out = []
    for ln in lines:
        if isinstance(ln, str):
            out.append('<span class="out">%s</span>' % ln)
        elif ln[0] == ">>":
            out.append('<span class="hl">%s</span>' % ln[1])
        elif ln[0] == "!!":
            out.append('<span class="er">%s</span>' % ln[1])
        elif ln[0] == "//":
            out.append('<span class="rem">%s</span>' % ln[1])
        else:
            rem = ('   <span class="rem">%s</span>' % ln[2]) if len(ln) > 2 else ""
            out.append('<span class="pr">%s</span> <span class="cm">%s</span>%s' % (ln[0], ln[1], rem))
    body = "\n".join(out)
    at = ' data-type="%s"' % body.replace('"', "&quot;") if typ else ""
    c = '<div class="clicap">%s</div>' % cap if cap else ""
    return '%s<div class="cli"><pre%s>%s</pre></div>' % (c, at, body)


def figimg(name, caption=None):
    cap = '<div class="figcap">%s</div>' % caption if caption else ""
    return ('<div class="figimg"><img src="%s" alt="%s" loading="lazy"></div>%s'
            % (b64(name), caption or "", cap))


def imgcard(name, caption=None, grow=True):
    cls = "grow" if grow else ""
    cap = '<div class="figcap">%s</div>' % caption if caption else ""
    return ('<div class="g %s" style="display:flex;flex-direction:column;min-height:0">'
            '<div class="figimg" style="flex:1 1 auto;min-height:0">'
            '<img src="%s" alt="%s" loading="lazy"></div>%s</div>'
            % (cls, b64(name), caption or "", cap))


# ======================================================================
#  ИКОНКИ
# ======================================================================

ICON = {
    "doc":   '<svg viewBox="0 0 24 24"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/><path d="M9 12h6M9 16h6"/></svg>',
    "gear":  '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg>',
    "arr":   '<svg viewBox="0 0 24 24"><path d="M4 12h15"/><path d="M13 6l6 6-6 6"/></svg>',
    "swap":  '<svg viewBox="0 0 24 24"><path d="M4 8h14l-4-4M20 16H6l4 4"/></svg>',
    "db":    '<svg viewBox="0 0 24 24"><ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v6c0 1.7 3.1 3 7 3s7-1.3 7-3V6"/><path d="M5 12v6c0 1.7 3.1 3 7 3s7-1.3 7-3v-6"/></svg>',
    "cpu":   '<svg viewBox="0 0 24 24"><rect x="7" y="7" width="10" height="10" rx="2"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/></svg>',
    "bolt":  '<svg viewBox="0 0 24 24"><path d="M13 3L5 13h6l-1 8 8-10h-6z"/></svg>',
    "clock": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M12 7v5.4l3.4 2"/></svg>',
    "globe": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M3.4 12h17.2M12 3.4c4 4.6 4 11.6 0 17.2M12 3.4c-4 4.6-4 11.6 0 17.2"/></svg>',
    "shield":'<svg viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 4.4-3 8-7 9-4-1-7-4.6-7-9V6z"/><path d="M8.8 12l2.2 2.2L15.4 10"/></svg>',
    "key":   '<svg viewBox="0 0 24 24"><circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v4M15 12v3"/></svg>',
    "eye":   '<svg viewBox="0 0 24 24"><path d="M2.5 12S6 6 12 6s9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6z"/><circle cx="12" cy="12" r="2.8"/></svg>',
    "bulb":  '<svg viewBox="0 0 24 24"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 00-3.5 10.9c.5.4.8 1 .9 1.6h5.2c.1-.6.4-1.2.9-1.6A6 6 0 0012 3z"/></svg>',
    "stop":  '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M6.2 6.2l11.6 11.6"/></svg>',
    "ok":    '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M8.2 12.2l2.6 2.6 5-5.2"/></svg>',
    "down":  '<svg viewBox="0 0 24 24"><path d="M12 4v14M6 13l6 6 6-6"/></svg>',
    "up":    '<svg viewBox="0 0 24 24"><path d="M12 20V6M6 11l6-6 6 6"/></svg>',
    "pc":    '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="11" rx="2"/><path d="M8 20h8M12 16v4"/></svg>',
    "hello": '<svg viewBox="0 0 24 24"><path d="M4 6h16v10H9l-5 4z"/></svg>',
    "wifi":  '<svg viewBox="0 0 24 24"><path d="M3.5 9.5a13 13 0 0117 0M6.8 13a8.4 8.4 0 0110.4 0M10 16.4a3.6 3.6 0 014 0"/><circle cx="12" cy="19.6" r="1"/></svg>',
    "route": '<svg viewBox="0 0 24 24"><circle cx="5" cy="6" r="2.4"/><circle cx="19" cy="18" r="2.4"/><path d="M7.4 6H14a4 4 0 010 8H10a4 4 0 000 4h6.6"/></svg>',
    "lock":  '<svg viewBox="0 0 24 24"><rect x="5" y="10" width="14" height="10" rx="2.4"/><path d="M8 10V7a4 4 0 018 0v3"/></svg>',
    "star":  '<svg viewBox="0 0 24 24"><path d="M12 3.6l2.6 5.4 5.9.8-4.3 4.1 1.1 5.8-5.3-2.8-5.3 2.8 1.1-5.8L3.5 9.8l5.9-.8z"/></svg>',
    "user":  '<svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4.4 3.6-7 8-7s8 2.6 8 7"/></svg>',
    "srv":   '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="6" rx="2"/><rect x="3" y="14" width="18" height="6" rx="2"/><path d="M7 7h.01M7 17h.01"/></svg>',
    "term":  '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 3-3 3M13 15h4"/></svg>',
    "link":  '<svg viewBox="0 0 24 24"><path d="M10 14a4 4 0 006 .5l2-2a4 4 0 00-5.7-5.7l-1 1"/><path d="M14 10a4 4 0 00-6-.5l-2 2a4 4 0 005.7 5.7l1-1"/></svg>',
    "chart": '<svg viewBox="0 0 24 24"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>',
    "warn":  '<svg viewBox="0 0 24 24"><path d="M12 4l9 16H3z"/><path d="M12 10v4M12 17h.01"/></svg>',
    "cal":   '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
    "flag":  '<svg viewBox="0 0 24 24"><path d="M5 21V4M5 4h12l-2.5 4L17 12H5"/></svg>',
    "split": '<svg viewBox="0 0 24 24"><path d="M3 12h5l4-6h9M8 12l4 6h9"/><path d="M17 3l4 3-4 3M17 15l4 3-4 3"/></svg>',
    "box":   '<svg viewBox="0 0 24 24"><path d="M12 3l8 4v10l-8 4-8-4V7z"/><path d="M4 7l8 4 8-4M12 11v10"/></svg>',
}


# ======================================================================
#  SVG-ПРИМИТИВЫ
# ======================================================================

ACOL = {"v": ("#6d4aff", "av"), "c": ("#1fb6e8", "ac"), "m": ("#d64ae8", "am"),
        "g": ("#16b16c", "ag"), "a": ("#f0a419", "aa"), "r": ("#f0486b", "ar"),
        "k": ("#1a1142", "ak"), "s": ("#9890c4", "as")}

FILL = {"v": "#6d4aff", "c": "#1fb6e8", "m": "#d64ae8", "g": "#16b16c", "a": "#f0a419",
        "r": "#f0486b", "k": "#1a1142", "w": "#ffffff", "s": "#9890c4",
        "vb": "#ece8ff", "cb": "#e0f5fd", "mb": "#fbe8ff", "gb": "#e1f7ee", "ab": "#fff3da",
        "rb": "#ffe6ec", "ib": "#e8e9ff", "sol": "#6d4aff"}
INK = {"v": "#fff", "c": "#fff", "m": "#fff", "g": "#fff", "a": "#3a2600", "r": "#fff",
       "k": "#fff", "w": "#1a1142", "s": "#fff",
       "vb": "#4327c9", "cb": "#0a6f94", "mb": "#9d1eb0", "gb": "#0c7a49", "ab": "#8a5c00",
       "rb": "#b11c3d", "ib": "#312bb0", "sol": "#ffffff"}


def arrow_defs():
    mk = "".join('<marker id="m_%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" '
                 'markerHeight="5" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="%s"/></marker>'
                 % (m, c) for (c, m) in ACOL.values())
    gr = ('<linearGradient id="esrBody" x1="0" y1="0" x2="0" y2="1">'
          '<stop offset="0" stop-color="#ffffff"/><stop offset=".55" stop-color="#f1effa"/>'
          '<stop offset="1" stop-color="#dcd8ec"/></linearGradient>'
          '<linearGradient id="dev1" x1="0" y1="0" x2="0" y2="1">'
          '<stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#e2ddf7"/></linearGradient>'
          '<linearGradient id="dev2" x1="0" y1="0" x2="0" y2="1">'
          '<stop offset="0" stop-color="#8a63ff"/><stop offset="1" stop-color="#5b36e0"/></linearGradient>'
          '<linearGradient id="dev3" x1="0" y1="0" x2="0" y2="1">'
          '<stop offset="0" stop-color="#5fd0f5"/><stop offset="1" stop-color="#1fa0d4"/></linearGradient>'
          '<filter id="sh" x="-30%" y="-30%" width="160%" height="170%">'
          '<feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#4a2fb0" flood-opacity=".22"/></filter>')
    return mk + gr


def arrow(x1, y1, x2, y2, tone="v", cls="", w=4.5, dash=False, curve=0, head=True, dasharray=None):
    col, mk = ACOL[tone]
    if curve:
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0 - curve
        d = "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x1, y1, mx, my, x2, y2)
        L = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5 * 1.25) + 30
    else:
        d = "M%.1f %.1f L%.1f %.1f" % (x1, y1, x2, y2)
        L = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5) + 14
    mkr = ' marker-end="url(#m_%s)"' % mk if head else ""
    da = ' stroke-dasharray="%s"' % dasharray if dasharray else ""
    dcl = ("dash " + cls).strip() if dash else cls
    return ('<path class="%s" d="%s" stroke="%s" stroke-width="%.1f" fill="none" stroke-linecap="round" '
            'style="--L:%d"%s%s/>' % (dcl, d, col, w, L, mkr, da))


def link(x1, y1, x2, y2, w=4.5, color="#b9b2dd", cls="", dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<path class="%s" d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="%.1f" '
            'stroke-linecap="round" fill="none"%s/>' % (cls, x1, y1, x2, y2, color, w, d))


def pill(x, y, text, tone="v", fs=14, cls="", w=None, h=27, mono=False):
    ww = w or max(h, int(len(text) * fs * .585) + 20)
    fam = ' font-family="ui-monospace,monospace"' if mono else ""
    return ('<g class="%s"><rect x="%.1f" y="%.1f" width="%d" height="%d" rx="%.1f" fill="%s"/>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="800" '
            'fill="%s"%s>%s</text></g>'
            % (cls, x - ww / 2.0, y - h / 2.0, ww, h, h / 2.0, FILL[tone],
               x, y + fs * .35, fs, INK[tone], fam, esc(text)))


def txt(x, y, text, fs=13, color="#1a1142", anchor="middle", weight=700, cls="", mono=False):
    fam = ' font-family="ui-monospace,monospace"' if mono else ""
    return ('<text class="%s" x="%.1f" y="%.1f" text-anchor="%s" font-size="%.1f" font-weight="%d" '
            'fill="%s"%s>%s</text>' % (cls, x, y, anchor, fs, weight, color, fam, esc(text)))


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def circ_num(x, y, n, tone="v", r=16, cls=""):
    return ('<g class="%s"><circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="900" fill="%s">%s</text></g>'
            % (cls, x, y, r, FILL[tone], x, y + r * .36, r * 1.0, INK[tone], n))


def ban(x, y, r=15, cls=""):
    k = r * .6
    return ('<g class="%s"><circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="#f0486b" stroke-width="4"/>'
            '<path d="M%.1f %.1f L%.1f %.1f" stroke="#f0486b" stroke-width="4" stroke-linecap="round"/></g>'
            % (cls, x, y, r, x - k, y - k, x + k, y + k))


def okmark(x, y, r=15, cls=""):
    return ('<g class="%s"><circle cx="%.1f" cy="%.1f" r="%.1f" fill="#16b16c"/>'
            '<path d="M%.1f %.1f l%.1f %.1f l%.1f %.1f" stroke="#fff" stroke-width="%.1f" fill="none" '
            'stroke-linecap="round" stroke-linejoin="round"/></g>'
            % (cls, x, y, r, x - r * .42, y, r * .32, r * .34, r * .62, -r * .68, r * .24))


def fig(view, body, cls="", extra_defs=""):
    d = '<defs>%s</defs>' % extra_defs if extra_defs else ""
    return ('<div class="figwrap"><svg class="fig %s" viewBox="%s">%s%s</svg></div>'
            % (cls, view, d, body))


def global_defs():
    """Общие маркеры, градиенты и фильтры — один раз на документ."""
    return ('<svg id="gdefs" width="0" height="0" style="position:absolute;left:-9999px" '
            'aria-hidden="true"><defs>%s</defs></svg>' % arrow_defs())


# ======================================================================
#  УСТРОЙСТВА (стиль референсных иллюстраций)
# ======================================================================

def router(x, y, w=104, label=None, cls="", sub=None, tone="v"):
    """Маршрутизатор ESR: рэковая коробка с портами и индикаторами."""
    h = w * 0.40
    x0, y0 = x - w / 2.0, y - h / 2.0
    ports = []
    pw = w * 0.085
    for i in range(6):
        ports.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.6" fill="#2a1f66" opacity=".75"/>'
                     % (x0 + w * 0.30 + i * pw * 1.35, y0 + h * 0.56, pw, h * 0.22))
    leds = []
    for i, c in enumerate(["#6bf0b0", "#ffd76a", "#5fd8ff"]):
        leds.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                    % (x0 + w * 0.10 + i * w * 0.062, y0 + h * 0.30, w * 0.019, c))
    lab = ""
    if label:
        lab = txt(x, y0 + h + 19, label, fs=w * 0.165, weight=800, color="#1a1142")
    s = txt(x, y0 + h + 19 + w * 0.18, sub, fs=w * 0.125, weight=700, color="#5d5682") if sub else ""
    return ('<g class="dev %s">'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="url(#dev2)" filter="url(#sh)"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#fff" opacity=".16"/>'
            '<path d="M%.1f %.1f h%.1f" stroke="#fff" stroke-width="1.4" opacity=".35"/>'
            '%s%s%s%s</g>'
            % (cls, x0, y0, w, h, h * 0.20,
               x0, y0, w, h * 0.42, h * 0.20,
               x0 + w * 0.06, y0 + h * 0.80, w * 0.88,
               "".join(ports), "".join(leds), lab, s))


def switch(x, y, w=96, label=None, cls="", sub=None):
    """Коммутатор: более плоская коробка с рядом портов, бирюзовый."""
    h = w * 0.30
    x0, y0 = x - w / 2.0, y - h / 2.0
    ports = []
    pw = w * 0.062
    for i in range(10):
        ports.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.4" fill="#0a5f80" opacity=".7"/>'
                     % (x0 + w * 0.08 + i * pw * 1.46, y0 + h * 0.52, pw, h * 0.30))
    lab = txt(x, y0 + h + 18, label, fs=w * 0.17, weight=800, color="#1a1142") if label else ""
    s = txt(x, y0 + h + 18 + w * 0.185, sub, fs=w * 0.135, weight=700, color="#5d5682") if sub else ""
    return ('<g class="dev %s">'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="url(#dev3)" filter="url(#sh)"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#fff" opacity=".2"/>'
            '%s%s%s</g>'
            % (cls, x0, y0, w, h, h * 0.22, x0, y0, w, h * 0.40, h * 0.22,
               "".join(ports), lab, s))


def pc(x, y, w=74, label=None, cls="", sub=None, tone="v"):
    """Рабочая станция: монитор на подставке."""
    h = w * 0.68
    x0, y0 = x - w / 2.0, y - h / 2.0
    lab = txt(x, y0 + h + 26, label, fs=w * 0.22, weight=800, color="#1a1142") if label else ""
    s = txt(x, y0 + h + 26 + w * 0.24, sub, fs=w * 0.175, weight=700, color="#5d5682") if sub else ""
    return ('<g class="dev %s">'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#fff" stroke="#b9b2dd" '
            'stroke-width="2" filter="url(#sh)"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" opacity=".30"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#8a7fc4"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="4" rx="2" fill="#8a7fc4"/>'
            '%s%s</g>'
            % (cls, x0, y0, w, h, w * 0.07,
               x0 + w * 0.07, y0 + h * 0.10, w * 0.86, h * 0.62, w * 0.04, FILL[tone],
               x - w * 0.05, y0 + h, w * 0.10, h * 0.16,
               x - w * 0.22, y0 + h + h * 0.16, w * 0.44,
               lab, s))


def server(x, y, w=64, label=None, cls="", sub=None, tone="v"):
    """Сервер: стойка из трёх блоков."""
    h = w * 1.26
    x0, y0 = x - w / 2.0, y - h / 2.0
    uh = h / 3.0
    bl = []
    for i in range(3):
        bl.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="url(#dev1)" '
                  'stroke="#b9b2dd" stroke-width="1.6"/>' % (x0, y0 + i * uh + 1.5, w, uh - 3, w * 0.09))
        bl.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                  % (x0 + w * 0.16, y0 + i * uh + uh / 2, w * 0.045, FILL[tone]))
        bl.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.5" fill="#cfc8ea"/>'
                  % (x0 + w * 0.30, y0 + i * uh + uh / 2 - 2, w * 0.52, 4))
    lab = txt(x, y0 + h + 18, label, fs=w * 0.26, weight=800, color="#1a1142") if label else ""
    s = txt(x, y0 + h + 18 + w * 0.28, sub, fs=w * 0.21, weight=700, color="#5d5682") if sub else ""
    return '<g class="dev %s" filter="url(#sh)">%s%s%s</g>' % (cls, "".join(bl), lab, s)


def cloudfig(x, y, w, h, label=None, sub=None, tone="cb", fs=15):
    rx, ry = w / 2.0, h / 2.0
    t = (txt(x, y + (-3 if sub else 5), label, fs=fs, weight=800, color=INK[tone])) if label else ""
    s = (txt(x, y + 16, sub, fs=fs - 2.5, weight=700, color=INK[tone])) if sub else ""
    return ('<g><ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>'
            '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>'
            '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>%s%s</g>'
            % (x, y, rx, ry, FILL[tone],
               x - rx * .52, y - ry * .38, rx * .56, ry * .84, FILL[tone],
               x + rx * .52, y - ry * .32, rx * .52, ry * .80, FILL[tone], t, s))


def laptop(x, y, w=76, label=None, cls="", tone="c"):
    h = w * 0.60
    x0, y0 = x - w / 2.0, y - h / 2.0
    lab = txt(x, y0 + h + 24, label, fs=w * 0.21, weight=800, color="#1a1142") if label else ""
    return ('<g class="dev %s">'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#fff" stroke="#b9b2dd" stroke-width="2"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="3" fill="%s" opacity=".28"/>'
            '<path d="M%.1f %.1f h%.1f l%.1f %.1f h%.1f z" fill="#d7d1ee"/>%s</g>'
            % (cls, x0, y0, w, h, w * 0.055,
               x0 + w * 0.07, y0 + h * 0.11, w * 0.86, h * 0.72, FILL[tone],
               x0 - w * 0.10, y0 + h, w * 1.20, -w * 0.06, h * 0.13, -w * 1.08, lab))


def shieldfig(x, y, w=52, tone="v", cls="", label=None):
    h = w * 1.16
    lab = txt(x, y + h * 0.62 + 16, label, fs=w * 0.28, weight=800, color="#1a1142") if label else ""
    return ('<g class="%s"><path d="M%.1f %.1f l%.1f %.1f v%.1f c0 %.1f -%.1f %.1f -%.1f %.1f '
            'c-%.1f -%.1f -%.1f -%.1f -%.1f -%.1f v-%.1f z" fill="%s" opacity=".92" filter="url(#sh)"/>'
            '<path d="M%.1f %.1f l%.1f %.1f l%.1f -%.1f" stroke="#fff" stroke-width="%.1f" fill="none" '
            'stroke-linecap="round" stroke-linejoin="round"/>%s</g>'
            % (cls, x, y - h * 0.5, w * 0.5, w * 0.22, h * 0.34,
               h * 0.33, w * 0.22, h * 0.40, w * 0.50, h * 0.44,
               w * 0.28, h * 0.04, w * 0.50, h * 0.37, w * 0.50, h * 0.44, h * 0.34,
               FILL[tone],
               x - w * 0.20, y, w * 0.14, w * 0.15, w * 0.30, w * 0.32, w * 0.09, lab))


def packet(x, y, w=38, label="IP", tone="a", cls="", fs=12):
    h = w * 0.62
    return ('<g class="%s"><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" '
            'filter="url(#sh)"/>%s</g>'
            % (cls, x - w / 2, y - h / 2, w, h, h * 0.26, FILL[tone],
               txt(x, y + fs * .36, label, fs=fs, weight=800, color=INK[tone])))


def netlabel(x, y, text, tone="vb", fs=13.5):
    return pill(x, y, text, tone=tone, fs=fs, h=24, mono=True)


def globefig(x, y, r=46, cls=""):
    mer = []
    for k in (0.32, 0.66):
        mer.append('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="none" stroke="#fff" '
                   'stroke-width="1.6" opacity=".75"/>' % (x, y, r * k, r))
    par = []
    for dy in (-r * 0.5, 0, r * 0.5):
        rr = (r ** 2 - dy ** 2) ** .5
        par.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#fff" stroke-width="1.6" '
                   'opacity=".75"/>' % (x - rr, y + dy, x + rr, y + dy))
    return ('<g class="%s"><circle cx="%.1f" cy="%.1f" r="%.1f" fill="url(#dev2)" filter="url(#sh)"/>'
            '%s%s</g>' % (cls, x, y, r, "".join(mer), "".join(par)))
