# -*- coding: utf-8 -*-
"""Строительные блоки деки OSPF: облачный фон, кавайные роутеры, карточки, таблицы."""

import base64
import os

SL = []
_uid = [0]

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_ospf_assets")
_cache = {}


def uid(pref="u"):
    _uid[0] += 1
    return "%s%d" % (pref, _uid[0])


def b64(name):
    """data-URI для webp-иллюстрации из _ospf_assets."""
    if name not in _cache:
        with open(os.path.join(ASSETS, name + ".webp"), "rb") as fh:
            _cache[name] = "data:image/webp;base64," + base64.b64encode(fh.read()).decode()
    return _cache[name]


# ======================================================================
#  ФОН: облака, точечные полутона, штрихи-искры
# ======================================================================

def background():
    clouds = []
    # (cx, cy, rx, ry, tone, opacity)
    spots = [
        (120, 90, 230, 120, "p", .55), (360, 46, 180, 86, "b", .45),
        (1300, 120, 250, 130, "b", .50), (1120, 60, 170, 80, "p", .40),
        (90, 800, 250, 130, "b", .45), (330, 866, 190, 92, "p", .42),
        (1340, 820, 240, 125, "p", .48), (1090, 872, 180, 86, "b", .38),
        (720, 20, 300, 70, "p", .22),
    ]
    for (cx, cy, rx, ry, tone, op) in spots:
        g = "cg1" if tone == "p" else "cg2"
        clouds.append('<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="url(#%s)" opacity="%.2f"/>'
                      % (cx, cy, rx, ry, g, op))

    dots = []
    for (x, y, w, h, pat) in [(28, 180, 96, 150, "dp"), (1316, 300, 96, 160, "db"),
                              (210, 700, 130, 80, "db"), (1180, 690, 120, 84, "dp"),
                              (640, 846, 150, 48, "dp")]:
        dots.append('<rect x="%d" y="%d" width="%d" height="%d" fill="url(#%s)" opacity=".8"/>'
                    % (x, y, w, h, pat))

    sparks = []
    for (x, y, rot, col, n) in [(1250, 210, -24, "#ff5c9e", 3), (170, 420, 18, "#ffd93d", 2),
                                (1310, 560, 32, "#3b9eff", 3), (90, 620, -16, "#ff5c9e", 2),
                                (560, 60, 14, "#ffd93d", 2)]:
        for i in range(n):
            sparks.append('<path d="M%d %d l26 -34" stroke="%s" stroke-width="8" stroke-linecap="round" '
                          'opacity=".55" transform="rotate(%d %d %d)"/>'
                          % (x + i * 20, y + i * 16, col, rot, x, y))

    return """<svg id="bg" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs>
  <linearGradient id="cg1" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#ffd3e4" stop-opacity=".95"/><stop offset="1" stop-color="#ffd3e4" stop-opacity="0"/>
  </linearGradient>
  <linearGradient id="cg2" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#c7e2fb" stop-opacity=".95"/><stop offset="1" stop-color="#c7e2fb" stop-opacity="0"/>
  </linearGradient>
  <pattern id="dp" width="11" height="11" patternUnits="userSpaceOnUse">
    <circle cx="3" cy="3" r="2.2" fill="#ffc2da"/></pattern>
  <pattern id="db" width="11" height="11" patternUnits="userSpaceOnUse">
    <circle cx="3" cy="3" r="2.2" fill="#b7d9f8"/></pattern>
</defs>
<rect width="1440" height="900" fill="#ffffff"/>
%s
%s
%s
</svg>""" % ("\n".join(clouds), "\n".join(dots), "\n".join(sparks))


# ======================================================================
#  КАРКАС СЛАЙДА
# ======================================================================

BG_CYCLE = [1, 8, 3, 5, 7, 4, 1, 8, 5, 7, 3, 2]


def slide(label, body, scen=None, cover=False, bg=None):
    """bg — номер подложки 1…8 из _ospf_assets/bg; по умолчанию по кругу, у титульных — город в облаках."""
    at = ' data-scen="%s"' % scen if scen else ""
    cl = " cover-slide" if cover else ""
    if bg is None:
        bg = 6 if cover else BG_CYCLE[len(SL) % len(BG_CYCLE)]
    SL.append('<section class="slide bg%d%s" data-label="%s"%s>%s</section>' % (bg, cl, label, at, body))


def bg_css():
    out = []
    for i in range(1, 9):
        with open(os.path.join(ASSETS, "bg", "bg%d.webp" % i), "rb") as fh:
            out.append(".slide.bg%d{background-image:url(data:image/webp;base64,%s)}"
                       % (i, base64.b64encode(fh.read()).decode()))
    return "\n".join(out)


SPARKS = ('<svg class="sparks" viewBox="0 0 74 46" aria-hidden="true">'
          '<path d="M8 38 L26 6"/><path d="M30 40 L46 10"/><path d="M52 36 L66 12"/></svg>')


def head(title, sub=None, sparks=True):
    s = '<p class="sub">%s</p>' % sub if sub else ""
    k = SPARKS if sparks else ""
    return '<div class="head"><div><h1 class="t">%s</h1>%s</div>%s</div>' % (title, s, k)


def sc(*parts):
    return '<div class="sc">%s</div>' % "".join(parts)


def g(cls, *parts, **kw):
    grow = " grow" if kw.get("grow") else ""
    return '<div class="g %s%s">%s</div>' % (cls, grow, "".join(parts))


def col(*parts):
    return '<div class="col">%s</div>' % "".join(parts)


def card(title=None, body="", num=None, tone="", cls=""):
    h = ""
    if title:
        n = '<span class="num %s">%s</span>' % (NUMTONE.get(tone, ""), num) if num else ""
        h = '<div class="ch">%s<h3>%s</h3></div>' % (n, title)
    return '<div class="c %s %s">%s%s</div>' % (tone, cls, h, body)


NUMTONE = {"pink": "", "blue": "b", "yellow": "y", "green": "g", "violet": "v", "w": "w", "": ""}


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


def cli(lines, typ=False):
    out = []
    for ln in lines:
        if isinstance(ln, str):
            out.append('<span class="rem">%s</span>' % ln)
        else:
            pr, cmd = ln[0], ln[1]
            rem = ('   <span class="rem">%s</span>' % ln[2]) if len(ln) > 2 else ""
            out.append('<span class="pr">%s</span> <span class="cm">%s</span>%s' % (pr, cmd, rem))
    body = "\n".join(out)
    at = ' data-type="%s"' % body.replace('"', "&quot;") if typ else ""
    return '<div class="cli"><pre%s>%s</pre></div>' % (at, body)


def figimg(name, caption=None):
    cap = '<div class="figcap">%s</div>' % caption if caption else ""
    return ('<div class="figimg"><img src="%s" alt="%s" loading="lazy"></div>%s'
            % (b64(name), caption or "", cap))


def imgcard(name, caption=None, grow=True):
    """Иллюстрация-референс как самостоятельный блок слайда."""
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
    "net":   '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M3.4 12h17.2M12 3.4c4 4.6 4 11.6 0 17.2M12 3.4c-4 4.6-4 11.6 0 17.2"/></svg>',
    "globe": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M3.4 12h17.2M12 3.4c4 4.6 4 11.6 0 17.2M12 3.4c-4 4.6-4 11.6 0 17.2"/></svg>',
    "shield":'<svg viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 4.4-3 8-7 9-4-1-7-4.6-7-9V6z"/><path d="M8.8 12l2.2 2.2L15.4 10"/></svg>',
    "key":   '<svg viewBox="0 0 24 24"><circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v4M15 12v3"/></svg>',
    "eye":   '<svg viewBox="0 0 24 24"><path d="M2.5 12S6 6 12 6s9.5 6 9.5 6-3.5 6-9.5 6-9.5-6-9.5-6z"/><circle cx="12" cy="12" r="2.8"/></svg>',
    "bulb":  '<svg viewBox="0 0 24 24"><path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 00-3.5 10.9c.5.4.8 1 .9 1.6h5.2c.1-.6.4-1.2.9-1.6A6 6 0 0012 3z"/></svg>',
    "stop":  '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M6.2 6.2l11.6 11.6"/></svg>',
    "ok":    '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="8.6"/><path d="M8.2 12.2l2.6 2.6 5-5.2"/></svg>',
    "down":  '<svg viewBox="0 0 24 24"><path d="M12 4v14M6 13l6 6 6-6"/></svg>',
    "up":    '<svg viewBox="0 0 24 24"><path d="M12 20V6M6 11l6-6 6 6"/></svg>',
    "sum":   '<svg viewBox="0 0 24 24"><path d="M6 5h12L11 12l7 7H6"/></svg>',
    "pc":    '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="11" rx="2"/><path d="M8 20h8M12 16v4"/></svg>',
    "hello": '<svg viewBox="0 0 24 24"><path d="M4 6h16v10H9l-5 4z"/></svg>',
    "wifi":  '<svg viewBox="0 0 24 24"><path d="M3.5 9.5a13 13 0 0117 0M6.8 13a8.4 8.4 0 0110.4 0M10 16.4a3.6 3.6 0 014 0"/><circle cx="12" cy="19.6" r="1"/></svg>',
    "tree":  '<svg viewBox="0 0 24 24"><circle cx="12" cy="5" r="2.6"/><circle cx="6" cy="19" r="2.6"/><circle cx="18" cy="19" r="2.6"/><path d="M12 7.6v4.4M12 12H6v4.4M12 12h6v4.4"/></svg>',
    "route": '<svg viewBox="0 0 24 24"><circle cx="5" cy="6" r="2.4"/><circle cx="19" cy="18" r="2.4"/><path d="M7.4 6H14a4 4 0 010 8H10a4 4 0 000 4h6.6"/></svg>',
    "lock":  '<svg viewBox="0 0 24 24"><rect x="5" y="10" width="14" height="10" rx="2.4"/><path d="M8 10V7a4 4 0 018 0v3"/></svg>',
    "star":  '<svg viewBox="0 0 24 24"><path d="M12 3.6l2.6 5.4 5.9.8-4.3 4.1 1.1 5.8-5.3-2.8-5.3 2.8 1.1-5.8L3.5 9.8l5.9-.8z"/></svg>',
}


# ======================================================================
#  КАВАЙНЫЙ МАРШРУТИЗАТОР
# ======================================================================

TONES = {
    "p": ("#fde6f0", "#f6bfd7", "#ec6aa3", "#b9467c"),
    "b": ("#e5f0fd", "#bcd9f6", "#4f97e6", "#3a72b0"),
    "g": ("#f0f2f5", "#d6dce3", "#a9b3be", "#6f7b87"),
    "y": ("#fff5d6", "#ffe39a", "#f2b705", "#a07a00"),
    "v": ("#efe9fb", "#d5c8f6", "#9b7bf0", "#6b4fd0"),
}


def router(x, y, w=92, tone="p", face=False, label=None, cls="", gid=None):
    """Маршрутизатор-шайба как на инфографиках: 4 антенны, эмблема сверху,
    панель индикаторов и подпись на боковине. Без мордочек."""
    top, side, led, out = TONES[tone]
    rx = w / 2.0
    ry = rx * 0.32
    h = w * 0.27
    sw = max(1.6, w * 0.022)
    ant = []
    for (dx, dy, hh) in [(-0.80, -0.15, 0.46), (0.80, -0.15, 0.46), (-0.40, -0.55, 0.58), (0.40, -0.55, 0.58)]:
        ax, ay = x + dx * rx, y + dy * ry
        aw = w * 0.05
        ant.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="%s" stroke="%s" stroke-width="%.1f"/>'
                   % (ax - aw / 2, ay - w * hh, aw, w * hh, aw / 2, side, out, sw * .8))
    er = rx * 0.24
    emb = ('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" opacity=".9"/>'
           '<path d="M%.1f %.1f h%.1f M%.1f %.1f v%.1f" stroke="#fff" stroke-width="%.1f" stroke-linecap="round"/>'
           % (x, y, er, er * .55, led, x - er * .62, y, er * 1.24, x, y - er * .36, er * .72, sw * 1.2))
    pw, ph = rx * 0.50, h * 0.40
    px, py = x - rx * 0.66, y + h * 0.36
    dots = "".join('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
                   % (px + pw * (0.2 + i * 0.2), py + ph / 2, ph * 0.17, c)
                   for i, c in enumerate(["#5ee08f", "#ffd93d", "#5ee08f", "#8fd3ff"]))
    panel = ('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#2a2f3d"/>%s'
             % (px, py, pw, ph, ph * .3, dots))
    lab = ""
    if label:
        fs = min(w * 0.17, w * 1.05 / max(1, len(label)))
        lab = ('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="800" '
               'fill="#1b1f2a">%s</text>' % (x + rx * 0.30, y + h * 0.82, fs, label))
    return """<g class="rtr %s" data-r="%s">
%s
<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" stroke="%s" stroke-width="%.1f"/>
<path d="M%.1f %.1f V%.1f A%.1f %.1f 0 0 0 %.1f %.1f V%.1f Z" fill="%s" stroke="%s" stroke-width="%.1f"/>
<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s" stroke="%s" stroke-width="%.1f"/>
%s%s%s</g>""" % (
        cls, label or "",
        "".join(ant),
        x, y + h, rx, ry, side, out, sw,
        x - rx, y, y + h, rx, ry, x + rx, y + h, y, side, out, sw,
        x, y, rx, ry, top, out, sw,
        emb, panel, lab)


def cat(x, y, s=1.0, cls=""):
    """Кавайный котик-талисман (белый, розовые ушки)."""
    u = 40.0 * s
    return ('<g class="%s" transform="translate(%.1f %.1f) scale(%.3f)">'
            '<path d="M-26 -16 l-6 -26 l22 10 z" fill="#fff" stroke="#e23b80" stroke-width="3"/>'
            '<path d="M26 -16 l6 -26 l-22 10 z" fill="#fff" stroke="#e23b80" stroke-width="3"/>'
            '<path d="M-24 -30 l-3 -13 l11 5 z" fill="#ffc2da"/>'
            '<path d="M24 -30 l3 -13 l-11 5 z" fill="#ffc2da"/>'
            '<ellipse cx="0" cy="0" rx="34" ry="29" fill="#fff" stroke="#e23b80" stroke-width="3"/>'
            '<circle cx="-12" cy="-3" r="3.6" fill="#121212"/>'
            '<circle cx="12" cy="-3" r="3.6" fill="#121212"/>'
            '<path d="M-5 7 q5 5 10 0" stroke="#121212" stroke-width="2.6" fill="none" stroke-linecap="round"/>'
            '<ellipse cx="-21" cy="6" rx="6" ry="4" fill="#ff9dc3" opacity=".85"/>'
            '<ellipse cx="21" cy="6" rx="6" ry="4" fill="#ff9dc3" opacity=".85"/>'
            '<path d="M-33 -2 h-12 M-33 5 h-11 M33 -2 h12 M33 5 h11" stroke="#ffc2da" '
            'stroke-width="2.4" stroke-linecap="round"/></g>' % (cls, x, y, 1.0))


def cloudsvg(x, y, w, h, label=None, sub=None, tone="b", fs=14.5):
    fill = {"b": "#e3f0fd", "p": "#fde7f0", "y": "#fef6dc", "g": "#e6f7ec", "v": "#efe9fb"}[tone]
    ink = {"b": "#1f6fc4", "p": "#d8276f", "y": "#8a6a00", "g": "#1d8a51", "v": "#6b4fd0"}[tone]
    rx, ry = w / 2.0, h / 2.0
    s = ('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" fill="%s" opacity=".9">%s</text>'
         % (x, y + 15, fs - 2.5, ink, sub)) if sub else ""
    dy = -3 if sub else 5
    t = ('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="800" fill="%s">%s</text>'
         % (x, y + dy, fs, ink, label)) if label else ""
    return ('<g><ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>'
            '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>'
            '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>%s%s</g>'
            % (x, y, rx, ry, fill,
               x - rx * .52, y - ry * .38, rx * .56, ry * .82, fill,
               x + rx * .52, y - ry * .32, rx * .52, ry * .78, fill, t, s))


# ======================================================================
#  SVG-ПРИМИТИВЫ
# ======================================================================

ACOL = {"p": ("#ff5c9e", "ap"), "b": ("#3b9eff", "ab"), "y": ("#ffd93d", "ay"),
        "g": ("#3fc47c", "ag"), "v": ("#9b7bf0", "av"), "k": ("#121212", "ak")}


def arrow_defs():
    return "".join('<marker id="m_%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5.2" '
                   'markerHeight="5.2" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="%s"/></marker>'
                   % (mk, col) for (col, mk) in ACOL.values())


def arrow(x1, y1, x2, y2, tone="p", cls="", w=5, dash=False, curve=0, head=True):
    col, mk = ACOL[tone]
    if curve:
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0 - curve
        d = "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x1, y1, mx, my, x2, y2)
        L = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5 * 1.2) + 24
    else:
        d = "M%.1f %.1f L%.1f %.1f" % (x1, y1, x2, y2)
        L = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5) + 12
    mkr = ' marker-end="url(#m_%s)"' % mk if head else ""
    dcl = ("dash " + cls).strip() if dash else cls
    return ('<path class="%s" d="%s" stroke="%s" stroke-width="%d" fill="none" stroke-linecap="round" '
            'style="--L:%d"%s/>' % (dcl, d, col, w, L, mkr))


def link(x1, y1, x2, y2, w=5, color="#9fb3c4", cls="", dash=None):
    d = ' stroke-dasharray="%s"' % dash if dash else ""
    return ('<path class="%s" d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="%d" '
            'stroke-linecap="round" fill="none"%s/>' % (cls, x1, y1, x2, y2, color, w, d))


def pill(x, y, text, tone="p", fs=15, cls="", w=None, h=28, mono=False):
    fill = {"p": "#ff5c9e", "b": "#3b9eff", "y": "#ffd93d", "g": "#3fc47c", "v": "#9b7bf0",
            "pb": "#fde7f0", "bb": "#e3f0fd", "yb": "#fef6dc", "gb": "#e6f7ec", "w": "#ffffff"}[tone]
    ink = {"p": "#fff", "b": "#fff", "y": "#121212", "g": "#fff", "v": "#fff",
           "pb": "#d8276f", "bb": "#1f6fc4", "yb": "#8a6a00", "gb": "#1d8a51", "w": "#121212"}[tone]
    ww = w or max(h, int(len(text) * fs * .60) + 20)
    fam = ' font-family="ui-monospace,monospace"' if mono else ""
    return ('<g class="%s"><rect x="%.1f" y="%.1f" width="%d" height="%d" rx="%.1f" fill="%s"/>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="800" '
            'fill="%s"%s>%s</text></g>'
            % (cls, x - ww / 2.0, y - h / 2.0, ww, h, h / 2.0, fill,
               x, y + fs * .36, fs, ink, fam, text))


def txt(x, y, text, fs=13.5, color="#121212", anchor="middle", weight=700, cls=""):
    return ('<text class="%s" x="%.1f" y="%.1f" text-anchor="%s" font-size="%.1f" font-weight="%d" '
            'fill="%s">%s</text>' % (cls, x, y, anchor, fs, weight, color, text))


def circ_num(x, y, n, tone="p", r=17, cls=""):
    fill = {"p": "#ff5c9e", "b": "#3b9eff", "y": "#ffd93d", "g": "#3fc47c", "v": "#9b7bf0"}[tone]
    ink = "#121212" if tone == "y" else "#fff"
    return ('<g class="%s"><circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="900" fill="%s">%s</text></g>'
            % (cls, x, y, r, fill, x, y + r * .36, r * 1.0, ink, n))


def ban(x, y, r=16, cls=""):
    k = r * .62
    return ('<g class="%s"><circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="#ff5c9e" stroke-width="4.5"/>'
            '<path d="M%.1f %.1f L%.1f %.1f" stroke="#ff5c9e" stroke-width="4.5" stroke-linecap="round"/></g>'
            % (cls, x, y, r, x - k, y - k, x + k, y + k))


def ok(x, y, r=16, cls=""):
    return ('<g class="%s"><circle cx="%.1f" cy="%.1f" r="%.1f" fill="#3fc47c"/>'
            '<path d="M%.1f %.1f l%.1f %.1f l%.1f %.1f" stroke="#fff" stroke-width="%.1f" fill="none" '
            'stroke-linecap="round" stroke-linejoin="round"/></g>'
            % (cls, x, y, r, x - r * .42, y, r * .32, r * .34, r * .62, -r * .68, r * .24))


def fig(view, body, cls="", extra_defs=""):
    return ('<div class="figwrap" style="display:flex;min-height:0"><svg class="fig %s" viewBox="%s">'
            '<defs>%s%s</defs>%s</svg></div>' % (cls, view, arrow_defs(), extra_defs, body))


# ======================================================================
#  ИЛЛЮСТРАЦИИ В СТИЛЕ ИНФОГРАФИК
# ======================================================================

import math as _m


def blob(cx, cy, rx, ry, tone="p", label=None, seed=0, dash=True, lab_y=None, fs=17):
    """Облачная область с пунктирным контуром и плашкой-названием."""
    fill = {"p": "#fde7f0", "b": "#e3f0fd", "y": "#fef6dc", "g": "#e6f7ec", "v": "#efe9fb"}[tone]
    edge = {"p": "#f29cc2", "b": "#8fbff0", "y": "#efcf6a", "g": "#86d3a8", "v": "#b9a4f2"}[tone]
    labfill = {"p": "#ffd3e4", "b": "#c7e2fb", "y": "#ffe9a8", "g": "#c6efd6", "v": "#ddd2fa"}[tone]
    n = 14
    pts = []
    for i in range(n):
        t = 2 * _m.pi * i / n
        k = 1 + 0.07 * _m.sin(3 * t + seed) + 0.05 * _m.sin(5 * t + seed * 1.7)
        pts.append((cx + rx * k * _m.cos(t), cy + ry * k * _m.sin(t)))
    d = "M%.1f %.1f" % pts[0]
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        d += " C%.1f %.1f %.1f %.1f %.1f %.1f" % (c1 + c2 + p2)
    da = ' stroke-dasharray="10 8"' if dash else ""
    lab = ""
    if label:
        ly = lab_y if lab_y is not None else cy - ry * 0.80
        lw = int(len(label) * fs * .62) + 30
        lab = ('<rect x="%.1f" y="%.1f" width="%d" height="%.1f" rx="%.1f" fill="%s"/>'
               '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="800" fill="#121212">%s</text>'
               % (cx - lw / 2.0, ly - fs, lw, fs * 2, fs, labfill, cx, ly + fs * .36, fs, label))
    return ('<g><path d="%s Z" fill="%s" stroke="%s" stroke-width="2.6"%s/>%s</g>' % (d, fill, edge, da, lab))


def rack(x, y, w=70, h=120):
    """Стойка серверов."""
    out = ['<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="8" fill="#5b5f7a" stroke="#3a3d52" stroke-width="2"/>'
           % (x, y, w, h)]
    n = int(h // 22)
    for i in range(n):
        yy = y + 8 + i * 22
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="15" rx="3" fill="#2c2f42"/>' % (x + 7, yy, w - 14))
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="3" rx="1.5" fill="#7fd0ff"/>' % (x + 13, yy + 6, w * .35))
        out.append('<circle cx="%.1f" cy="%.1f" r="2.4" fill="%s"/>' % (x + w - 16, yy + 7.5, "#5ee08f" if i % 2 else "#ff7ab0"))
    return "".join(out)


def cloud_icon(x, y, s=1.0, fill="#ffffff", edge="#c7dcf3"):
    return ('<path transform="translate(%.1f %.1f) scale(%.2f)" d="M-40 14 h80 a20 20 0 0 0 -6 -39 '
            'a28 28 0 0 0 -52 -6 a22 22 0 0 0 -22 45 z" fill="%s" stroke="%s" stroke-width="2.4"/>'
            % (x, y, s, fill, edge))


def laptop(x, y, w=110, tone="p"):
    c = {"p": "#f6bfd7", "b": "#bcd9f6"}[tone]
    h = w * .62
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="8" fill="#3a3f55"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="4" fill="%s"/>'
            '<path d="M%.1f %.1f h%.1f l%.1f %.1f h%.1f z" fill="#d6dbe4" stroke="#9aa3b2" stroke-width="1.6"/></g>'
            % (x - w / 2, y - h, w, h, x - w / 2 + 7, y - h + 7, w - 14, h - 14, c,
               x - w / 2, y, w, w * .1, w * .12, -w * 1.2))


def globe(x, y, r=26, col="#3b9eff"):
    return ('<g fill="none" stroke="%s" stroke-width="3"><circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff"/>'
            '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f"/>'
            '<path d="M%.1f %.1f h%.1f M%.1f %.1f h%.1f M%.1f %.1f h%.1f"/></g>'
            % (col, x, y, r, x, y, r * .45, r, x - r, y, 2 * r,
               x - r * .86, y - r * .5, r * 1.72, x - r * .86, y + r * .5, r * 1.72))


def envelope(x, y, w=40, tone="p"):
    c = {"p": "#f29cc2", "b": "#8fbff0", "y": "#efcf6a"}[tone]
    h = w * .66
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="4" fill="#fff" stroke="%s" stroke-width="2.4"/>'
            '<path d="M%.1f %.1f l%.1f %.1f l%.1f %.1f" fill="none" stroke="%s" stroke-width="2.4"/></g>'
            % (x - w / 2, y - h / 2, w, h, c, x - w / 2, y - h / 2, w / 2, h * .55, w / 2, -h * .55, c))


def legend(x, y, items, w=330, fs=14):
    """Легенда: items = [(kind, color, text)], kind: line | dash | cross | arrow."""
    rows = []
    for i, (kind, col_, t) in enumerate(items):
        yy = y + 26 + i * 34
        if kind == "line":
            sym = '<path d="M%.1f %.1f h40" stroke="%s" stroke-width="5" stroke-linecap="round"/>' % (x + 18, yy, col_)
        elif kind == "dash":
            sym = ('<path d="M%.1f %.1f h40" stroke="%s" stroke-width="5" stroke-dasharray="8 6" '
                   'stroke-linecap="round"/>' % (x + 18, yy, col_))
        elif kind == "arrow":
            sym = ('<path d="M%.1f %.1f h34" stroke="%s" stroke-width="4" stroke-linecap="round"/>'
                   '<path d="M%.1f %.1f l-9 -6 v12 z" fill="%s"/>' % (x + 18, yy, col_, x + 60, yy, col_))
        else:
            sym = ('<path d="M%.1f %.1f l16 16 M%.1f %.1f l-16 16" stroke="%s" stroke-width="5" stroke-linecap="round"/>'
                   % (x + 30, yy - 8, x + 46, yy - 8, col_))
        rows.append(sym + txt(x + 72, yy + 5, t, fs=fs, anchor="start", weight=600))
    hh = 18 + len(items) * 34
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="16" fill="#fff" stroke="#e9eef3" '
            'stroke-width="2"/>%s</g>' % (x, y, w, hh, "".join(rows)))


def bubble(x, y, text, tone="p", fs=16, w=None):
    """Выноска с хвостиком."""
    fill = {"p": "#ff5c9e", "b": "#3b9eff", "y": "#ffd93d", "g": "#3fc47c", "v": "#9b7bf0"}[tone]
    ink = "#121212" if tone == "y" else "#fff"
    lines = text.split("|")
    ww = w or int(max(len(l) for l in lines) * fs * .58) + 34
    hh = 18 + len(lines) * (fs + 6)
    tt = "".join('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="800" fill="%s">%s</text>'
                 % (x, y + 12 + i * (fs + 6) + fs * .8, fs, ink, l) for i, l in enumerate(lines))
    return ('<g><rect x="%.1f" y="%.1f" width="%d" height="%d" rx="14" fill="%s"/>'
            '<path d="M%.1f %.1f l10 14 l8 -14 z" fill="%s"/>%s</g>'
            % (x - ww / 2, y, ww, hh, fill, x - 22, y + hh - 1, fill, tt))


def sparkle(x, y, col="#ff5c9e", n=3, rot=-25):
    return "".join('<path d="M%d %d l22 -30" stroke="%s" stroke-width="7" stroke-linecap="round" '
                   'transform="rotate(%d %d %d)"/>' % (x + i * 17, y + i * 12, col, rot, x, y) for i in range(n))


# ======================================================================
#  БЛОКИ ВЁРСТКИ В СТИЛЕ ИНФОГРАФИК
# ======================================================================

ICO_BG = {"p": "#ffd3e4", "b": "#c7e2fb", "y": "#ffe9a8", "g": "#c6efd6", "v": "#ddd2fa"}


def rowc(icon, title, text, tone="p", extra=""):
    """Горизонтальная карточка: круглый значок слева, заголовок и текст справа."""
    return ('<div class="rowc %s"><span class="ico">%s</span><div><h3>%s</h3><p>%s</p>%s</div></div>'
            % (tone, ICON[icon], title, text, extra))


def nrow(n, title, icon_svg, text, tone="p"):
    """Нумерованная строка-этап как на инфографике «Принцип работы Link State»."""
    return ('<div class="nrow %s"><span class="nn">%s</span><h3>%s</h3>'
            '<span class="nill">%s</span><p>%s</p></div>' % (tone, n, title, icon_svg, text))


def tile(icon, title, text, tone="p"):
    """Плитка: значок сверху, крупный заголовок, текст."""
    return ('<div class="tile %s"><span class="ico">%s</span><span class="dash"></span>'
            '<h3>%s</h3><p>%s</p></div>' % (tone, ICON[icon], title, text))


def _stack(part):
    """Колонка только из строк — растягиваем строки на всю высоту."""
    import re as _re
    if 'class="ill' in part or 'class="panel' in part or 'class="g ' in part or _re.search(r'class="row\d', part):
        return part
    return '<div class="stack">%s</div>' % part


def split(left, right, ratio="44fr 56fr"):
    left, right = _stack(left), _stack(right)
    return ('<div class="split" style="grid-template-columns:minmax(0,%s) minmax(0,%s)">'
            '<div class="lcol">%s</div><div class="rcol">%s</div></div>'
            % (ratio.split()[0], ratio.split()[1], left, right))


def ill(view, body, extra_defs=""):
    """Иллюстрация на мягкой подложке, растягивается на доступную площадь."""
    return ('<div class="ill"><svg viewBox="%s" preserveAspectRatio="xMidYMid meet"><defs>%s%s</defs>%s</svg></div>'
            % (view, arrow_defs(), extra_defs, body))


def mini(view, body):
    """Маленькая SVG-картинка внутри строки."""
    return '<svg class="mini" viewBox="%s"><defs>%s</defs>%s</svg>' % (view, arrow_defs(), body)


TONES["gr"] = ("#e9f8ef", "#bfe9cf", "#3fc47c", "#2b8f58")


def panel(icon, title, body, tone="p", cls=""):
    """Панель с пастельной шапкой: значок в кружке + заголовок, ниже содержимое."""
    return ('<div class="panel %s %s"><div class="ph"><span class="ico">%s</span><h3>%s</h3></div>'
            '<div class="pb">%s</div></div>' % (tone, cls, ICON[icon], title, body))


def vcard(num, title, art, text, tone="p", badge=None, cls=""):
    """Вертикальная карточка-этап: номер + заголовок, пилюля, картинка, подпись."""
    b = '<span class="vb">%s</span>' % badge if badge else ""
    return ('<div class="vcard %s %s"><div class="vh"><span class="nn">%s</span><h3>%s</h3></div>%s'
            '<div class="va">%s</div><p>%s</p></div>' % (tone, cls, num, title, b, art, text))


def chain(items):
    """Цепочка пилюль со стрелками: items = [(text, tone)]."""
    out = []
    for i, (t, tone) in enumerate(items):
        if i:
            out.append('<span class="carr">&#10140;</span>')
        out.append('<span class="cpill %s">%s</span>' % (tone, t))
    return '<div class="chain">%s</div>' % "".join(out)


def switch(x, y, w=150, tone="b"):
    top, side, led, out = TONES[tone]
    h = w * .26
    ports = "".join('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#2a2f3d"/>'
                    % (x - w * .40 + i * w * .105, y + h * .32, w * .07, h * .36) for i in range(8))
    return ('<g><path d="M%.1f %.1f l%.1f %.1f h%.1f l%.1f %.1f z" fill="%s" stroke="%s" stroke-width="2.4"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="8" fill="%s" stroke="%s" stroke-width="2.4"/>%s</g>'
            % (x - w / 2, y, w * .08, -h * .7, w * .84, w * .08, h * .7, top, out,
               x - w / 2, y, w, h, side, out, ports))


def mark(x, y, value, status, tone="p"):
    """Метка вершины над роутером: крупное число и статус (как на слайдах Дейкстры)."""
    fill = {"p": "#ffd3e4", "b": "#c7e2fb", "y": "#ffe9a8", "g": "#c6efd6", "w": "#ffffff"}[tone]
    ink = {"p": "#d8276f", "b": "#1f6fc4", "y": "#8a6a00", "g": "#1d8a51", "w": "#121212"}[tone]
    return ('<g><rect x="%.1f" y="%.1f" width="120" height="58" rx="14" fill="%s"/>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="27" font-weight="900" fill="%s">%s</text>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="13" font-weight="700" fill="#121212">%s</text></g>'
            % (x - 60, y - 29, fill, x, y + 2, ink, value, x, y + 21, status))
