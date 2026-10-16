# -*- coding: utf-8 -*-
"""SVG-примитивы деки 2.6: устройства из атласа, облако Интернета, карточки пакетов,
таблица NAT, диаграммы обмена. Сцены рисуются в координатах 1200×560 (или своих vb)."""

from _sw_svg import (txt, box, link, arrow, curve, badge, note, defs as _swdefs,  # noqa: F401
                     CY, MG, LM, AM, RD, OR, INK, SOFT)

YE = "#ffd23f"
VI = "#b077ff"
GR = "#6cf08a"
BL = "#4aa8ff"

TONE = {"y": YE, "o": OR, "v": VI, "g": GR, "c": CY, "r": RD, "b": BL}


def defs():
    extra = (
        '<defs>'
        '<linearGradient id="gcl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5fc8ff"/>'
        '<stop offset="1" stop-color="#1f6fd0"/></linearGradient>'
        '<radialGradient id="glb" cx=".38" cy=".35" r=".7"><stop offset="0" stop-color="#2a7fd8"/>'
        '<stop offset="1" stop-color="#06204a"/></radialGradient>'
        '<linearGradient id="glap" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3aa0ff"/>'
        '<stop offset="1" stop-color="#0b3c9a"/></linearGradient>'
        + "".join('<marker id="mk%s" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">'
                  '<path d="M0 0L9 4.5L0 9z" fill="%s"/></marker>' % (k, c) for k, c in TONE.items())
        + '</defs>')
    return _swdefs() + extra


def fig(body, vb="0 0 1200 560", cls="fig"):
    return '<svg class="%s" viewBox="%s">%s%s</svg>' % (cls, vb, defs(), body)


def _ph(ph, only=False, upto=None):
    if ph is None:
        return ""
    a = ' data-ph="%d"' % ph
    if only:
        a += " data-ph-only"
    if upto is not None:
        a += ' data-ph-upto="%d"' % upto
    return a


def plate(x, y, text, col=CY, size=15, sub="", subcol=SOFT):
    w = max(70, len(text) * size * .58 + 22)
    if sub:
        w = max(w, len(sub) * 12 * .58 + 22)
    h = 26 if not sub else 44
    o = '<rect x="%g" y="%g" width="%g" height="%g" rx="8" fill="rgba(4,16,42,.9)" stroke="%s" stroke-width="1.4"/>' % (
        x - w / 2, y, w, h, col)
    o += txt(x, y + 18, text, size, "#fff", 800)
    if sub:
        o += txt(x, y + 36, sub, 12, subcol, 700, mono=True)
    return o


# ----------------------------------------------------------------------
#  устройства
# ----------------------------------------------------------------------

def dev(sym, x, y, w, label="", sub="", col=CY, ph=None, ghost=None, ly=None):
    g = ' data-ghost="%d"' % ghost if ghost is not None else ""
    o = ['<g%s%s>' % (_ph(ph), g)]
    o.append('<ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="none" stroke="%s" stroke-width="1.6" opacity=".55"/>'
             % (x, y + w * .36, w * .55, w * .14, col))
    flt = ''
    o.append('<g%s><use href="#%s" x="%g" y="%g" width="%g" height="%g"/></g>' % (flt, sym, x - w / 2, y - w / 2, w, w))
    if label:
        o.append(plate(x, (ly if ly is not None else y + w * .5 + 8), label, col, 15, sub))
    o.append('</g>')
    return "".join(o)


def router(x, y, label="Маршрутизатор", sub="", w=96, **k):
    return dev("sd-router-blue", x, y, w, label, sub, **k)


def server(x, y, label="Сервер", sub="", w=92, **k):
    return dev("sd-server", x, y, w, label, sub, **k)


def pc(x, y, label="Компьютер", sub="", w=84, **k):
    return dev("sd-pc", x, y, w, label, sub, **k)


def switch(x, y, label="Коммутатор", sub="", w=100, **k):
    return dev("sd-switch", x, y, w, label, sub, **k)


def laptop(x, y, label="", sub="", s=1.0, col=CY, ph=None):
    w, h = 96 * s, 60 * s
    o = ['<g%s>' % _ph(ph)]
    o.append('<rect x="%g" y="%g" width="%g" height="%g" rx="6" fill="#0a1d44" stroke="%s" stroke-width="2"/>'
             % (x - w / 2, y - h, w, h, col))
    o.append('<rect x="%g" y="%g" width="%g" height="%g" rx="3" fill="url(#glap)" opacity=".9"/>'
             % (x - w / 2 + 6 * s, y - h + 6 * s, w - 12 * s, h - 12 * s))
    o.append('<path d="M%g %g h%g l%g %g h%g z" fill="#11295a" stroke="%s" stroke-width="2"/>'
             % (x - w / 2, y, w, 14 * s, 12 * s, -(w + 28 * s), col))
    if label:
        o.append(plate(x, y + 20 * s, label, col, 15, sub))
    o.append('</g>')
    return "".join(o)


CLOUD = ("M-60 30 a34 34 0 0 1 8 -66 a52 52 0 0 1 98 -14 a40 40 0 0 1 66 30 "
         "a32 32 0 0 1 -6 50 z")


def cloud(x, y, label="Интернет", s=1.0, col=CY, ph=None):
    o = ['<g%s>' % _ph(ph)]
    o.append('<g transform="translate(%g %g) scale(%g)">' % (x - 8 * s, y + 4 * s, s))
    o.append('<path d="%s" fill="url(#gcl)" stroke="#bfeaff" stroke-width="2" opacity=".95" filter="url(#gl)"/>' % CLOUD)
    o.append('</g>')
    o.append(txt(x, y + 6 * s, label, 22 * s, "#fff", 800))
    o.append('</g>')
    return "".join(o)


def globe(x, y, r=46, ph=None):
    o = ['<g%s>' % _ph(ph)]
    o.append('<circle cx="%g" cy="%g" r="%g" fill="url(#glb)" stroke="#6fdcff" stroke-width="2" filter="url(#gl)"/>' % (x, y, r))
    for k in (-.5, 0, .5):
        o.append('<ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="none" stroke="#6fdcff" stroke-width="1" opacity=".55"/>'
                 % (x, y + k * r, r * (1 - abs(k) * .3), r * .14))
    o.append('<ellipse cx="%g" cy="%g" rx="%g" ry="%g" fill="none" stroke="#6fdcff" stroke-width="1" opacity=".55"/>'
             % (x, y, r * .45, r))
    for (dx, dy) in ((-.3, -.2), (.2, .3), (.35, -.35), (-.1, .45), (.05, -.05)):
        o.append('<circle cx="%g" cy="%g" r="3" fill="#ffcf6b"/>' % (x + dx * r, y + dy * r))
    o.append('</g>')
    return "".join(o)


# ----------------------------------------------------------------------
#  карточки пакетов
# ----------------------------------------------------------------------

def hdr(x, y, rows, title="", w=300, ph=None, only=False, upto=None, col=CY):
    """Карточка заголовка пакета: rows = [(подпись, значение, тон)], тон из TONE."""
    rh = 30
    h = (30 if title else 8) + len(rows) * (rh + 6) + 4
    o = ['<g%s>' % _ph(ph, only, upto)]
    o.append(box(x, y, w, h, col, "rgba(5,18,46,.95)", 10, 1.6))
    yy = y + 8
    if title:
        o.append(txt(x + 12, y + 21, title, 14, "#fff", 800, "start"))
        yy = y + 30
    lw = w * .36
    for (lab, val, tone) in rows:
        c = TONE.get(tone, CY)
        o.append('<rect x="%g" y="%g" width="%g" height="%g" rx="6" fill="rgba(70,140,220,.22)"/>' % (x + 8, yy, w - 16, rh))
        o.append(txt(x + 18, yy + 20, lab, 13, SOFT, 700, "start"))
        o.append('<rect x="%g" y="%g" width="%g" height="%g" rx="6" fill="%s"/>' % (x + lw, yy, w - lw - 8, rh, c))
        o.append(txt(x + lw + (w - lw - 8) / 2, yy + 20, val, 13.5, "#08142c", 800, mono=True))
        yy += rh + 6
    o.append('</g>')
    return "".join(o)


def mvhdr(x0, y0, x1, y1, rows, ph, title="", w=270, only=True, col=CY):
    """Летящая карточка пакета: уезжает из (x0,y0) в (x1,y1) на шаге ph."""
    st = "--x0:0px;--y0:0px;--x1:%gpx;--y1:%gpx" % (x1 - x0, y1 - y0)
    inner = hdr(x0 - w / 2, y0, rows, title, w, None, col=col)
    return '<g class="mv"%s style="%s">%s</g>' % (_ph(ph, only), st, inner)


def env(x0, y0, x1, y1, label, ph, col=YE, only=True, w=150):
    """Маленький «конверт» сообщения, едет по линии."""
    st = "--x0:0px;--y0:0px;--x1:%gpx;--y1:%gpx" % (x1 - x0, y1 - y0)
    o = ['<g class="mv"%s style="%s">' % (_ph(ph, only), st)]
    o.append('<rect x="%g" y="%g" width="%g" height="30" rx="8" fill="%s" filter="url(#gl)"/>' % (x0 - w / 2, y0 - 15, w, col))
    o.append(txt(x0, y0 + 5, label, 13, "#08142c", 800, mono=True))
    o.append('</g>')
    return "".join(o)


def nat_table(x, y, rows, w=470, title="Таблица NAT", hdrs=("Внутренний (локальный)", "Внешний (глобальный)"),
              ph=None, col=AM):
    """rows = [(left, right, ph_or_None)]."""
    h = 70 + len(rows) * 32
    o = ['<g%s>' % _ph(ph), box(x, y, w, h, col, "rgba(5,18,46,.95)", 10, 1.8)]
    o.append(txt(x + w / 2, y + 24, title, 16, col, 800))
    o.append(txt(x + w * .27, y + 50, hdrs[0], 12.5, SOFT, 700))
    o.append(txt(x + w * .75, y + 50, hdrs[1], 12.5, SOFT, 700))
    o.append(link(x + 10, y + 58, x + w - 10, y + 58, col, 1, .5))
    for i, r in enumerate(rows):
        l, rr = r[0], r[1]
        rp = r[2] if len(r) > 2 else None
        yy = y + 82 + i * 32
        o.append('<g%s>' % _ph(rp))
        o.append('<rect x="%g" y="%g" width="%g" height="26" rx="6" fill="rgba(255,197,61,.12)"/>' % (x + 8, yy - 18, w - 16))
        o.append(txt(x + w * .27, yy, l, 13.5, YE, 800, mono=True))
        o.append(txt(x + w / 2, yy, "⟷", 15, "#fff", 800))
        o.append(txt(x + w * .75, yy, rr, 13.5, OR, 800, mono=True))
        o.append('</g>')
    o.append('</g>')
    return "".join(o)


def chip(x, y, n, text, tone="y", w=300, ph=None, only=False):
    """Плашка этапа внутри сцены (как «① Перехват пакета»)."""
    c = TONE.get(tone, YE)
    o = ['<g%s>' % _ph(ph, only)]
    o.append('<rect x="%g" y="%g" width="%g" height="38" rx="19" fill="%s" filter="url(#gl)"/>' % (x, y, w, c))
    o.append('<circle cx="%g" cy="%g" r="15" fill="#0b1630"/>' % (x + 20, y + 19))
    o.append(txt(x + 20, y + 25, str(n), 16, "#fff", 800))
    o.append(txt(x + 44, y + 25, text, 15.5, "#0b1630", 800, "start"))
    o.append('</g>')
    return "".join(o)


def seq_msg(x1, x2, y, label, sub="", tone="y", ph=None, dash=False):
    """Стрелка диаграммы обмена между линиями жизни x1→x2 на высоте y."""
    c = TONE.get(tone, YE)
    d = ' stroke-dasharray="10 7"' if dash else ""
    o = ['<g%s>' % _ph(ph)]
    o.append('<path d="M%g %gL%g %g" stroke="%s" stroke-width="3.4" marker-end="url(#mk%s)"%s filter="url(#gl)"/>'
             % (x1, y, x2 - (8 if x2 > x1 else -8), y, c, tone, d))
    o.append(txt((x1 + x2) / 2, y - 10, label, 16, c, 800, mono=True))
    if sub:
        o.append(txt((x1 + x2) / 2, y + 22, sub, 13, SOFT, 600))
    o.append('</g>')
    return "".join(o)
