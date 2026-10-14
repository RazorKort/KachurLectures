# -*- coding: utf-8 -*-
"""Строительные блоки деки RIP: фон с ботаникой, маршрутизаторы, стрелки, карточки."""

SL = []           # список готовых слайдов
_uid = [0]


def uid(pref="u"):
    _uid[0] += 1
    return "%s%d" % (pref, _uid[0])


# ======================================================================
#  ФОН: блобы, ботанические листья, точечные сетки, чёрточки
# ======================================================================

LEAF_PATH = ("M0 0 C 26 -34 74 -34 100 0 C 74 34 26 34 0 0 Z")

def _lf(x, y, sc, rot, op):
    return ('<use href="#leaf" class="leaf" transform="translate(%d %d) rotate(%d) scale(%.2f)" '
            'opacity="%.2f"/>' % (x, y, rot, sc, op))


def _bl(cx, cy, rx, ry, g, op=1.0):
    return ('<ellipse cx="%d" cy="%d" rx="%d" ry="%d" fill="url(#%s)" opacity="%.2f"/>'
            % (cx, cy, rx, ry, g, op))


def _dt(x, y, w, h, op=.7):
    return ('<rect x="%d" y="%d" width="%d" height="%d" fill="url(#dotg)" opacity="%.2f"/>'
            % (x, y, w, h, op))


def _ds(x, y, w, op=.5):
    return ('<rect x="%d" y="%d" width="%d" height="13" rx="6.5" fill="#bde3cd" opacity="%.2f"/>'
            % (x, y, w, op))


def _ring(cx, cy, r, w=2, col="#c9e9d7", op=.55):
    return ('<circle cx="%d" cy="%d" r="%d" fill="none" stroke="%s" stroke-width="%d" '
            'opacity="%.2f"/>' % (cx, cy, r, col, w, op))


def _wave(y, amp, col="#cdebdb", w=3, op=.5):
    d = "M-40 %d" % y
    x = -40
    up = True
    while x < 1480:
        d += " Q %d %d %d %d" % (x + 90, y + (-amp if up else amp), x + 180, y)
        x += 180
        up = not up
    return ('<path d="%s" fill="none" stroke="%s" stroke-width="%d" opacity="%.2f" '
            'stroke-linecap="round"/>' % (d, col, w, op))


# Задники: у каждого слайда свой. 0 — титульный, 6 и 7 — спокойные,
# их получают плотные слайды с таблицами и командами.

# Мотивы в видимых зонах: полоса шапки (y < 200) и низ (y > 760).
def _bands():
    B = []
    # 0 · мятно-розовое свечение над заголовком
    B.append("".join([_bl(620, 40, 620, 190, "b2", .9), _bl(120, 60, 360, 150, "b1", .8),
                      _dt(880, 24, 130, 56, .5), _ds(1140, 56, 96, .6), _ds(1264, 96, 54, .4),
                      _bl(700, 880, 560, 170, "b4", .8)]))
    # 1 · розовая волна под шапкой
    B.append("".join([_bl(900, 40, 560, 180, "b2", 1), _wave(150, 20, "#f3cbdd", 3, .6),
                      _dt(120, 30, 120, 52, .45), _ds(620, 40, 110, .5),
                      _bl(260, 880, 480, 160, "b3", .8)]))
    # 2 · лавандовая диагональ через шапку
    B.append("".join([_bl(420, 50, 520, 180, "b3", 1),
                      '<g opacity=".6" transform="rotate(-9 720 110)">%s%s%s</g>'
                      % (_dt(120, 36, 150, 48), _dt(560, 72, 150, 48), _dt(1000, 108, 150, 48)),
                      _ds(1230, 44, 92, .55),
                      _bl(1120, 880, 520, 170, "b1", .8)]))
    # 3 · голубая волна под шапкой
    B.append("".join([_bl(760, 30, 620, 180, "b5", 1), _wave(168, 24, "#c8ddf4", 3, .65),
                      _wave(196, 14, "#dceaf8", 2, .45), _dt(1180, 28, 120, 52, .45),
                      _bl(180, 880, 460, 160, "b4", .85)]))
    # 4 · кольца в правом верхнем углу
    B.append("".join([_bl(1240, 40, 440, 200, "b4", 1),
                      _ring(1320, 46, 210, 2, "#bfe5cf", .55),
                      _ring(1320, 46, 150, 2, "#d2ecdf", .6),
                      _ring(1320, 46, 96, 3, "#bde3cd", .45),
                      _ds(140, 48, 104, .55), _ds(280, 92, 58, .4),
                      _bl(560, 880, 520, 160, "b2", .7)]))
    # 5 · точечные поля по верхним углам
    B.append("".join([_bl(720, 44, 580, 180, "b1", .9),
                      _dt(70, 26, 170, 104, .55), _dt(1200, 26, 170, 104, .55),
                      _ds(640, 150, 120, .5),
                      _dt(70, 800, 170, 90, .45), _dt(1200, 800, 170, 90, .45)]))
    # 6 · спокойный: мягкая волна света
    B.append("".join([_bl(560, 30, 700, 170, "b4", .9), _bl(1180, 60, 380, 150, "b1", .6),
                      _bl(400, 880, 560, 150, "b1", .6)]))
    # 7 · почти пусто: одно свечение над заголовком
    B.append("".join([_bl(500, 20, 760, 150, "b4", .75),
                      _bl(900, 886, 620, 140, "b1", .5)]))
    return B


def _variants():
    V = []

    # 0 · ботаника по обоим краям, мятно-розовое свечение
    V.append("".join(
        [_bl(200, 140, 330, 250, "b1"), _bl(1240, 760, 360, 270, "b4"),
         _bl(1140, 150, 280, 210, "b2"), _bl(330, 810, 300, 200, "b3"),
         _bl(760, 470, 420, 300, "b1", .5)] +
        [_dt(300, 120, 92, 64), _dt(1060, 180, 78, 52), _dt(520, 760, 110, 58)] +
        [_ds(1120, 120, 86), _ds(250, 690, 70)] +
        [_lf(-26, 88, 1.25, -28, .8), _lf(-52, 250, 1.6, 14, .62), _lf(-18, 430, 1.05, -52, .72),
         _lf(-44, 612, 1.45, 28, .55), _lf(-10, 790, .95, -14, .68),
         _lf(1360, 70, 1.35, 198, .74), _lf(1392, 232, 1.65, 166, .58),
         _lf(1352, 418, 1.1, 214, .7), _lf(1386, 596, 1.5, 152, .54),
         _lf(1344, 772, 1.0, 192, .66)]))

    # 1 · розовый рассвет справа, ботаника только справа
    V.append("".join(
        [_bl(1180, 110, 430, 320, "b2"), _bl(240, 700, 380, 280, "b1"),
         _bl(820, 420, 400, 300, "b4", .55)] +
        [_dt(180, 150, 96, 62), _dt(980, 700, 84, 56)] +
        [_ds(120, 430, 92), _ds(300, 470, 54, .35)] +
        [_lf(1372, 120, 1.5, 192, .72), _lf(1398, 330, 1.75, 158, .56),
         _lf(1358, 540, 1.2, 206, .66), _lf(1382, 740, 1.4, 168, .5)]))

    # 2 · лавандовая диагональ
    V.append("".join(
        [_bl(300, 830, 420, 300, "b3"), _bl(1150, 220, 360, 260, "b4"),
         _bl(700, 500, 380, 280, "b1", .45)] +
        ['<g opacity=".55" transform="rotate(-18 720 450)">%s%s%s</g>'
         % (_dt(260, 250, 120, 48), _dt(620, 330, 120, 48), _dt(980, 410, 120, 48))] +
        [_ds(1140, 640, 78), _ds(1040, 690, 46, .34)] +
        [_lf(-34, 640, 1.4, 22, .6), _lf(-14, 800, 1.1, -12, .7),
         _lf(1376, 96, 1.3, 196, .62)]))

    # 3 · голубая волна поперёк
    V.append("".join(
        [_bl(760, 120, 460, 300, "b5"), _bl(1200, 760, 360, 260, "b1"),
         _bl(200, 540, 340, 260, "b4", .6)] +
        [_wave(300, 26), _wave(360, 18, "#dff0e7", 2, .45)] +
        [_dt(1060, 150, 88, 58), _dt(300, 760, 96, 52)] +
        [_lf(-28, 120, 1.2, -26, .62), _lf(-40, 300, 1.45, 16, .5),
         _lf(1370, 500, 1.3, 206, .6), _lf(1388, 700, 1.5, 162, .46)]))

    # 4 · кольца справа
    V.append("".join(
        [_bl(1180, 440, 420, 340, "b4"), _bl(240, 180, 360, 270, "b1"),
         _bl(420, 820, 340, 240, "b2", .5)] +
        [_ring(1230, 440, 300, 2, "#c9e9d7", .5), _ring(1230, 440, 220, 2, "#d6eee1", .55),
         _ring(1230, 440, 150, 3, "#bde3cd", .4)] +
        [_dt(180, 620, 92, 60)] + [_ds(640, 110, 86), _ds(760, 160, 48, .35)] +
        [_lf(-30, 420, 1.5, 10, .62), _lf(-16, 620, 1.1, -32, .66)]))

    # 5 · бенто-поля в углах
    V.append("".join(
        [_bl(1120, 760, 420, 300, "b1"), _bl(340, 140, 380, 280, "b4"),
         _bl(900, 380, 360, 260, "b3", .45)] +
        [_dt(90, 110, 150, 96, .55), _dt(1210, 110, 150, 96, .5),
         _dt(90, 700, 150, 96, .5), _dt(1210, 700, 150, 96, .55)] +
        [_ds(640, 820, 92), _ds(560, 60, 64, .4)] +
        [_lf(1368, 380, 1.35, 200, .6), _lf(-24, 500, 1.25, -18, .6)]))

    # 6 · спокойный: мягкое свечение и пара листьев
    V.append("".join(
        [_bl(420, 260, 520, 380, "b1", .75), _bl(1120, 660, 480, 340, "b4", .7),
         _bl(1180, 120, 300, 220, "b2", .4)] +
        [_lf(-22, 700, 1.2, -16, .5), _lf(1378, 180, 1.25, 198, .48)]))

    # 7 · почти пусто: одно большое свечение
    V.append("".join(
        [_bl(760, 420, 620, 440, "b4", .8), _bl(180, 820, 340, 240, "b1", .5),
         _bl(1280, 120, 320, 240, "b3", .35)] +
        [_lf(1384, 560, 1.15, 190, .4)]))

    bands = _bands()
    return [v + bands[i] for i, v in enumerate(V)]


def pick_bg(markup, i):
    """Плотным слайдам (таблицы, команды) достаётся спокойный задник."""
    heavy = markup.count("<table") + markup.count('class="cli"')
    if i == 0:
        return 0
    if heavy >= 2 or markup.count("<tr") > 9:
        return 7
    if heavy:
        return 6
    return 1 + (i % 5)


def background():
    """Полотно + набор задников; активный переключает движок по data-bg слайда."""
    layers = "".join('<g class="bgv">%s</g>' % v for v in _variants())
    return """<svg id="bg" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs>
  <radialGradient id="b1"><stop offset="0" stop-color="#9fe0bf" stop-opacity=".55"/><stop offset="1" stop-color="#9fe0bf" stop-opacity="0"/></radialGradient>
  <radialGradient id="b2"><stop offset="0" stop-color="#f6c9dd" stop-opacity=".50"/><stop offset="1" stop-color="#f6c9dd" stop-opacity="0"/></radialGradient>
  <radialGradient id="b3"><stop offset="0" stop-color="#d8d1f4" stop-opacity=".48"/><stop offset="1" stop-color="#d8d1f4" stop-opacity="0"/></radialGradient>
  <radialGradient id="b4"><stop offset="0" stop-color="#c6efd9" stop-opacity=".60"/><stop offset="1" stop-color="#c6efd9" stop-opacity="0"/></radialGradient>
  <radialGradient id="b5"><stop offset="0" stop-color="#c3dcf7" stop-opacity=".48"/><stop offset="1" stop-color="#c3dcf7" stop-opacity="0"/></radialGradient>
  <linearGradient id="lf" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#a7dfc0"/><stop offset="1" stop-color="#d9f2e4"/>
  </linearGradient>
  <pattern id="dotg" width="14" height="14" patternUnits="userSpaceOnUse">
    <circle cx="3" cy="3" r="2.1" fill="#bde3cd"/>
  </pattern>
  <g id="leaf">
    <path d="%s" fill="url(#lf)"/>
    <path d="M2 0 H98" stroke="#8ecfa9" stroke-width="1.6" fill="none"/>
    <path d="M24 -2 C 36 -12 44 -16 56 -17" stroke="#8ecfa9" stroke-width="1.2" fill="none"/>
    <path d="M44 -2 C 56 -11 64 -14 76 -15" stroke="#8ecfa9" stroke-width="1.2" fill="none"/>
    <path d="M24 2 C 36 12 44 16 56 17" stroke="#8ecfa9" stroke-width="1.2" fill="none"/>
    <path d="M44 2 C 56 11 64 14 76 15" stroke="#8ecfa9" stroke-width="1.2" fill="none"/>
  </g>
</defs>
<rect width="1440" height="900" fill="#f3fbf7"/>
%s
</svg>""" % (LEAF_PATH, layers)


def with_bg(slides, picker):
    """Проставляет каждому слайду свой задник: data-bg="N"."""
    out = []
    for i, m in enumerate(slides):
        k = picker(m, i)
        out.append(m.replace('<section class="slide', '<section data-bg="%d" class="slide' % k, 1))
    return out


# ======================================================================
#  СЛАЙД
# ======================================================================

def slide(label, body, scen=None, cover=False):
    at = ' data-scen="%s"' % scen if scen else ""
    cl = " cover-slide" if cover else ""
    SL.append('<section class="slide%s" data-label="%s"%s>%s</section>' % (cl, label, at, body))


def head(title, sub=None, mark=True):
    s = '<p class="sub">%s</p>' % sub if sub else ""
    m = '<span class="mark"></span>' if mark else ""
    return ('<div class="head">%s<div><h1 class="t">%s</h1><div class="ul"></div>%s</div></div>'
            % (m, title, s))


def sc(*parts):
    return '<div class="sc">%s</div>' % "".join(parts)


def card(title=None, body="", num=None, cls="", icon_mix=False):
    h = ""
    if title:
        n = '<span class="num">%s</span>' % num if num else ""
        mix = " mix" if icon_mix else ""
        h = '<div class="ch">%s<h3 class="%s">%s</h3></div>' % (n, mix.strip(), title)
    return '<div class="c %s">%s%s</div>' % (cls, h, body)


def step(inner):
    return '<div class="step">%s</div>' % inner


def irow(icon, text, tone=""):
    return '<div class="ir %s"><span class="ib">%s</span><span>%s</span></div>' % (tone, ICON[icon], text)


def foot(text):
    return '<div class="foot"><i></i><span>%s</span><i></i></div>' % text


def tagline(*tags):
    return '<div class="tags">%s</div>' % "".join(tags)


def tag(text, tone="", mono=False):
    cl = (tone + (" mono" if mono else "")).strip()
    return '<span class="tag %s">%s</span>' % (cl, text)


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
    """lines: список строк вида ('esr(config-rip)#', 'network 192.168.10.0/24', 'комментарий')."""
    out = []
    for ln in lines:
        if isinstance(ln, str):
            out.append('<span class="rem">%s</span>' % ln)
        else:
            pr, cmd = ln[0], ln[1]
            rem = ('   <span class="rem">%s</span>' % ln[2]) if len(ln) > 2 else ""
            out.append('<span class="pr">%s</span> <span class="cm">%s</span>%s' % (pr, cmd, rem))
    return '<div class="cli"><pre>%s</pre></div>' % "\n".join(out)


# ======================================================================
#  SVG-ПРИМИТИВЫ
# ======================================================================

ICON = {
    "doc":   '<svg viewBox="0 0 24 24"><path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4"/><path d="M9 12h6M9 16h6"/></svg>',
    "gear":  '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg>',
    "pin":   '<svg viewBox="0 0 24 24"><path d="M12 21s7-6 7-11a7 7 0 10-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.6"/></svg>',
    "arr":   '<svg viewBox="0 0 24 24"><path d="M4 12h15"/><path d="M13 6l6 6-6 6"/></svg>',
    "users": '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.4"/><path d="M17 14c2.6 0 4.6 2 4.6 4.6"/></svg>',
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
}


def router(x, y, r=34, label=None, tone="teal", gid=None):
    """Цилиндр-маршрутизатор с белым крестом стрелок и подписью в плашке под ним."""
    g = gid or uid("rg")
    ry = r * .42
    sw = max(2.6, r * .115)
    a = r * .62          # вылет стрелки
    hw = r * .20         # полуширина наконечника
    top = "#8adcb9" if tone == "teal" else "#8adcb9"
    arrows = []
    for (dx, dy) in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ex, ey = x + dx * a, y + dy * a * .78
        arrows.append('<path d="M%.1f %.1f L%.1f %.1f" stroke="#fff" stroke-width="%.1f" '
                      'stroke-linecap="round"/>' % (x, y, ex, ey, sw))
        # наконечник
        if dx:
            arrows.append('<path d="M%.1f %.1f l%.1f %.1f M%.1f %.1f l%.1f %.1f" stroke="#fff" '
                          'stroke-width="%.1f" stroke-linecap="round" fill="none"/>'
                          % (ex, ey, -dx * hw * 1.4, -hw, ex, ey, -dx * hw * 1.4, hw, sw * .85))
        else:
            arrows.append('<path d="M%.1f %.1f l%.1f %.1f M%.1f %.1f l%.1f %.1f" stroke="#fff" '
                          'stroke-width="%.1f" stroke-linecap="round" fill="none"/>'
                          % (ex, ey, -hw, -dy * hw * 1.4, ex, ey, hw, -dy * hw * 1.4, sw * .85))
    lab = ""
    if label:
        lw = max(40, 15 + len(label) * 11)
        ly = y + r * .62 + ry + 10
        lab = ('<g class="rlab"><rect x="%.1f" y="%.1f" width="%d" height="26" rx="10" fill="#dff3e8"/>'
               '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="15" font-weight="800" '
               'fill="#1d7a4f" font-family="inherit">%s</text></g>'
               % (x - lw / 2, ly, lw, x, ly + 18, label))
    return """<g class="rtr" data-r="%s">
<defs><linearGradient id="%s" x1="0" y1="0" x2="0" y2="1">
<stop offset="0" stop-color="#7fd0b0"/><stop offset="1" stop-color="#2e8f6c"/></linearGradient></defs>
<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="#2e8f6c"/>
<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="url(#%s)"/>
<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>
%s%s</g>""" % (label or "", g,
               x, y + r * .62, r, ry,
               x - r, y - r * .62, r * 2, r * 1.24, g,
               x, y - r * .62, r, ry, top,
               "".join(arrows), lab)


def cloud(x, y, w, h, label, sub=None, tone="blue"):
    fill = {"blue": "#dbe9fb", "green": "#dff3e8", "lav": "#e7e2fa", "pink": "#fbe2ed"}[tone]
    ink = {"blue": "#3b6ba8", "green": "#1d7a4f", "lav": "#6a5ab8", "pink": "#c9517f"}[tone]
    rx, ry = w / 2, h / 2
    s = ('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="12.5" fill="%s" opacity=".85">%s</text>'
         % (x, y + 16, ink, sub)) if sub else ""
    dy = -4 if sub else 5
    return ('<g><ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>'
            '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>'
            '<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="%s"/>'
            '<text x="%.1f" y="%.1f" text-anchor="middle" font-size="14.5" font-weight="800" fill="%s">%s</text>%s</g>'
            % (x, y, rx, ry, fill,
               x - rx * .5, y - ry * .35, rx * .55, ry * .8, fill,
               x + rx * .5, y - ry * .3, rx * .5, ry * .75, fill,
               x, y + dy, ink, label, s))


def link(x1, y1, x2, y2, w=5, color="#2e8f6c"):
    return ('<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="%d" stroke-linecap="round"/>'
            % (x1, y1, x2, y2, color, w))


_ARROW_DEFS = []


def arrow_defs():
    """Маркеры стрелок: зелёная, розовая, синяя, лавандовая."""
    out = []
    for (name, col) in (("ag", "#36a56e"), ("ap", "#e58cb4"), ("ab", "#7ba7e0"), ("av", "#9f90dd")):
        out.append('<marker id="m_%s" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" '
                   'markerHeight="4" orient="auto-start-reverse">'
                   '<path d="M0 0L10 5L0 10z" fill="%s"/></marker>' % (name, col))
    return "".join(out)


ACOL = {"g": ("#36a56e", "ag"), "p": ("#e58cb4", "ap"), "b": ("#7ba7e0", "ab"), "v": ("#9f90dd", "av")}


def arrow(x1, y1, x2, y2, tone="g", cls="", w=5, dash=False, curve=0):
    col, mk = ACOL[tone]
    if curve:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2 - curve
        d = "M%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x1, y1, mx, my, x2, y2)
        L = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5 * 1.15) + 20
    else:
        d = "M%.1f %.1f L%.1f %.1f" % (x1, y1, x2, y2)
        L = int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5) + 12
    style = ' style="--L:%d"' % L
    dcl = ("dash " + cls).strip() if dash else cls
    return ('<path class="%s" d="%s" stroke="%s" stroke-width="%d" fill="none" stroke-linecap="round" '
            'marker-end="url(#m_%s)"%s/>' % (dcl, d, col, w, mk, style))


def ban(x, y, r=17):
    """Знак запрета: белый круг, красный контур, диагональ."""
    k = r * .62
    return ('<g><circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff" stroke="#d94a74" stroke-width="5"/>'
            '<path d="M%.1f %.1f L%.1f %.1f" stroke="#d94a74" stroke-width="5" stroke-linecap="round"/></g>'
            % (x, y, r, x - k, y - k, x + k, y + k))


def ok(x, y, r=17):
    """Галочка: зелёный круг, белая галочка."""
    return ('<g><circle cx="%.1f" cy="%.1f" r="%.1f" fill="#36a56e"/>'
            '<path d="M%.1f %.1f l%.1f %.1f l%.1f %.1f" stroke="#fff" stroke-width="%.1f" fill="none" '
            'stroke-linecap="round" stroke-linejoin="round"/></g>'
            % (x, y, r, x - r * .42, y, r * .32, r * .34, r * .62, -r * .68, r * .22))


def callout(x, y, text, tone="g", w=None, anchor="middle", tail=True, cls="", fs=13.5):
    """Пастельная плашка-выноска с треугольным хвостиком вниз."""
    fill = {"g": "#dff3e8", "p": "#fbe2ed", "b": "#e4eefc", "v": "#eae5fb"}[tone]
    ink = {"g": "#1d7a4f", "p": "#c9517f", "b": "#4a7cc2", "v": "#7566c4"}[tone]
    lines = text.split("|")
    ww = w or max(90, int(max(len(l) for l in lines) * fs * .56) + 26)
    hh = 14 + len(lines) * (fs + 5)
    x0 = x - ww / 2 if anchor == "middle" else x
    tx = x0 + ww / 2
    tl = ('<path d="M%.1f %.1f l9 0 l-4.5 9 z" fill="%s"/>' % (tx - 4.5, y + hh, fill)) if tail else ""
    tt = "".join('<text x="%.1f" y="%.1f" text-anchor="middle" font-size="%.1f" font-weight="700" '
                 'fill="%s">%s</text>' % (tx, y + 12 + i * (fs + 5) + fs * .55, fs, ink, l)
                 for i, l in enumerate(lines))
    return '<g class="%s">%s<rect x="%.1f" y="%.1f" width="%d" height="%d" rx="12" fill="%s"/>%s</g>' \
           % (cls, tl, x0, y, ww, hh, fill, tt)


def axis_label(x, y, text, size=12.5, color="#6a8077", anchor="middle", weight=600):
    return ('<text x="%.1f" y="%.1f" text-anchor="%s" font-size="%.1f" font-weight="%d" fill="%s">%s</text>'
            % (x, y, anchor, size, weight, color, text))


def fig(view, body, cls="", extra_defs=""):
    """Собирает SVG-фигуру. Маркеры стрелок получают уникальный суффикс:
    одинаковые id в нескольких svg одного документа ломают marker-end."""
    u = uid("k")
    defs = arrow_defs()
    for nm in ("ag", "ap", "ab", "av"):
        defs = defs.replace('id="m_%s"' % nm, 'id="m_%s_%s"' % (nm, u))
        body = body.replace("url(#m_%s)" % nm, "url(#m_%s_%s)" % (nm, u))
    return ('<div class="figwrap"><svg class="fig %s" viewBox="%s"><defs>%s%s</defs>%s</svg></div>'
            % (cls, view, defs, extra_defs, body))
