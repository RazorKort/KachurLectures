# -*- coding: utf-8 -*-
"""Неоновые SVG-примитивы и сцены деки «Коммутаторы и коммутация».

Все сцены рисуются в системе координат 1200×560 и управляются атрибутами
data-ph (шаг появления) — их переключают кнопки «Назад / Вперёд».
"""

from _sw_lib import uid

CY = "#2ad4ff"
MG = "#c45cff"
LM = "#9dfc5a"
AM = "#ffc53d"
RD = "#ff4d5e"
OR = "#ff8a3d"
INK = "#eaf6ff"
SOFT = "#a8c8e8"


# ----------------------------------------------------------------------
#  базовые примитивы
# ----------------------------------------------------------------------

def defs():
    return """<defs>
<linearGradient id="gsw" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#1b3f73"/><stop offset="1" stop-color="#0b1e3f"/></linearGradient>
<linearGradient id="gpc" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#17457f"/><stop offset="1" stop-color="#0a1c3a"/></linearGradient>
<filter id="gl" x="-60%" y="-60%" width="220%" height="220%">
  <feGaussianBlur stdDeviation="5" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<marker id="ah" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
  <path d="M0 0L9 4.5L0 9z" fill="#2ad4ff"/></marker>
<marker id="ahr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
  <path d="M0 0L9 4.5L0 9z" fill="#ff4d5e"/></marker>
<marker id="ahg" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
  <path d="M0 0L9 4.5L0 9z" fill="#9dfc5a"/></marker>
<marker id="ahm" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
  <path d="M0 0L9 4.5L0 9z" fill="#c45cff"/></marker>
<marker id="aha" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
  <path d="M0 0L9 4.5L0 9z" fill="#ffc53d"/></marker>
</defs>"""


def fig(body, vb="0 0 1200 560", cls="fig"):
    return '<svg class="%s" viewBox="%s">%s%s</svg>' % (cls, vb, defs(), body)


def txt(x, y, s, size=14, col=INK, w=700, anchor="middle", mono=False, extra=""):
    fam = ' font-family="JetBrains Mono,Consolas,monospace"' if mono else ""
    return ('<text x="%g" y="%g" text-anchor="%s" font-size="%g" font-weight="%d" fill="%s"%s%s>%s</text>'
            % (x, y, anchor, size, w, col, fam, extra, s))


def box(x, y, w, h, col=CY, fill="rgba(10,30,70,.72)", r=10, sw=1.6, extra=""):
    return ('<rect x="%g" y="%g" width="%g" height="%g" rx="%g" fill="%s" stroke="%s" stroke-width="%g"%s/>'
            % (x, y, w, h, r, fill, col, sw, extra))


def panel(x, y, w, h, title, col=CY, extra=""):
    return (box(x, y, w, h, col, extra=extra)
            + txt(x + 12, y + 20, title, 13, col, 800, "start"))


def pc(x, y, name, mac="", col=CY, vlan=""):
    """Компьютер с подписью. Якорь — центр верхней грани монитора."""
    o = ['<g>']
    o.append('<rect x="%g" y="%g" width="104" height="66" rx="7" fill="url(#gpc)" stroke="%s" stroke-width="2"/>'
             % (x - 52, y, col))
    o.append('<rect x="%g" y="%g" width="88" height="46" rx="4" fill="rgba(42,212,255,.14)" stroke="%s" stroke-width="1"/>'
             % (x - 44, y + 8, col))
    o.append('<path d="M%g %gh30" stroke="%s" stroke-width="5" stroke-linecap="round"/>' % (x - 15, y + 78, col))
    o.append('<path d="M%g %gv12" stroke="%s" stroke-width="4"/>' % (x, y + 66, col))
    o.append(txt(x, y + 100, name, 16, "#fff", 800))
    if mac:
        o.append(txt(x, y + 118, mac, 12, SOFT, 600, mono=True))
    if vlan:
        o.append(txt(x, y + 136, vlan, 12, col, 800))
    o.append("</g>")
    return "".join(o)


def switch(x, y, w=380, h=74, ports=8, label="Коммутатор", col=CY,
           pid=None, names=None):
    """Коммутатор с рядом портов. Возвращает (svg, координаты портов)."""
    o = ['<g>']
    o.append('<rect x="%g" y="%g" width="%g" height="%g" rx="9" fill="url(#gsw)" stroke="%s" stroke-width="2.2"/>'
             % (x, y, w, h, col))
    o.append('<rect x="%g" y="%g" width="%g" height="3" rx="2" fill="%s" opacity=".85"/>' % (x + 14, y + 6, w - 28, col))
    pts = []
    pw = 26
    gap = (w - 40 - ports * pw) / float(max(1, ports - 1))
    for i in range(ports):
        px = x + 20 + i * (pw + gap)
        py = y + h - 34
        nm = names[i] if names else ("1/0/%d" % (i + 1))
        pts.append((px + pw / 2.0, py, nm))
        o.append('<rect id="%s_p%d" x="%g" y="%g" width="%g" height="20" rx="3" fill="rgba(42,212,255,.15)" stroke="%s" stroke-width="1.2"/>'
                 % (pid or "sw", i, px, py, pw, col))
        o.append(txt(px + pw / 2.0, py + 33, nm, 10.5, SOFT, 700, mono=True))
    o.append(txt(x + w / 2.0, y - 10, label, 15, "#fff", 800))
    o.append("</g>")
    return "".join(o), pts


def link(x1, y1, x2, y2, col=CY, w=2.4, op=.5, dash=False, extra=""):
    d = ' stroke-dasharray="9 7"' if dash else ""
    return ('<path d="M%g %gL%g %g" stroke="%s" stroke-width="%g" opacity="%g" stroke-linecap="round"%s%s/>'
            % (x1, y1, x2, y2, col, w, op, d, extra))


def arrow(x1, y1, x2, y2, col=CY, w=3.4, mk="ah", ph=None, only=False, flow=True, extra=""):
    a = ""
    if ph is not None:
        a = ' data-ph="%d"%s' % (ph, " data-ph-only" if only else "")
    cls = ' class="flow"' if flow else ""
    return ('<path d="M%g %gL%g %g" stroke="%s" stroke-width="%g" fill="none" marker-end="url(#%s)"%s%s%s/>'
            % (x1, y1, x2, y2, col, w, mk, cls, a, extra))


def curve(x1, y1, x2, y2, bow=-70, col=CY, w=3.2, mk="ah", ph=None, only=False, flow=True):
    mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0 + bow
    a = ""
    if ph is not None:
        a = ' data-ph="%d"%s' % (ph, " data-ph-only" if only else "")
    cls = ' class="flow"' if flow else ""
    return ('<path d="M%g %gQ%g %g %g %g" stroke="%s" stroke-width="%g" fill="none" marker-end="url(#%s)"%s%s/>'
            % (x1, y1, mx, my, x2, y2, col, w, mk, cls, a))


def pkt(x0, y0, x1, y1, label, ph, col=AM, w=132, h=30, only=True, sub=""):
    """Летящий кадр: появляется в (x0,y0), уезжает в (x1,y1)."""
    style = "--x0:0px;--y0:0px;--x1:%gpx;--y1:%gpx" % (x1 - x0, y1 - y0)
    o = ['<g class="mv" data-ph="%d"%s style="%s">' % (ph, " data-ph-only" if only else "", style)]
    o.append('<rect x="%g" y="%g" width="%g" height="%g" rx="7" fill="rgba(10,26,58,.95)" stroke="%s" stroke-width="2" filter="url(#gl)"/>'
             % (x0 - w / 2.0, y0 - h / 2.0, w, h, col))
    o.append(txt(x0, y0 + (0 if not sub else -3), label, 12.5, col, 800, mono=True))
    if sub:
        o.append(txt(x0, y0 + 12, sub, 10.5, SOFT, 600, mono=True))
    o.append("</g>")
    return "".join(o)


def badge(x, y, text, col=CY, ph=None, only=False, size=13, pad=12, h=28):
    w = max(60, len(text) * (size * .62) + pad * 2)
    a = ""
    if ph is not None:
        a = ' data-ph="%d"%s' % (ph, " data-ph-only" if only else "")
    return ('<g%s><rect x="%g" y="%g" width="%g" height="%g" rx="7" fill="rgba(6,18,44,.94)" stroke="%s" stroke-width="1.6"/>%s</g>'
            % (a, x - w / 2.0, y - h / 2.0, w, h, col, txt(x, y + size * .36, text, size, col, 800)))


def note(x, y, lines, col=CY, ph=None, w=330, only=False):
    a = ""
    if ph is not None:
        a = ' data-ph="%d"%s' % (ph, " data-ph-only" if only else "")
    h = 16 + len(lines) * 19
    o = ['<g%s>' % a, box(x, y, w, h, col, r=9)]
    for i, l in enumerate(lines):
        o.append(txt(x + 12, y + 24 + i * 19, l, 12.5, SOFT, 600, "start"))
    o.append("</g>")
    return "".join(o)


def cam_table(x, y, rows, title="CAM-таблица", w=360, col=LM, ph=None):
    """Таблица коммутации: rows = [(vid, mac, port, kind, ph_or_None)]."""
    a = ' data-ph="%d"' % ph if ph is not None else ""
    h = 54 + len(rows) * 26
    o = ['<g%s>' % a, box(x, y, w, h, col, r=9)]
    o.append(txt(x + 12, y + 21, title, 13, col, 800, "start"))
    cols = [x + 14, x + 54, x + 182, x + 288]
    hdr = ["VID", "MAC-адрес", "Порт", "Тип"]
    for c, t in zip(cols, hdr):
        o.append(txt(c, y + 42, t, 11, SOFT, 700, "start"))
    o.append('<path d="M%g %gh%g" stroke="%s" stroke-width="1" opacity=".4"/>' % (x + 10, y + 48, w - 20, col))
    for i, r in enumerate(rows):
        vid, mac, port, kind = r[0], r[1], r[2], r[3]
        rph = r[4] if len(r) > 4 else None
        ra = ' data-ph="%d"' % rph if rph is not None else ""
        yy = y + 68 + i * 26
        o.append('<g%s>' % ra)
        if rph is not None:
            o.append('<rect x="%g" y="%g" width="%g" height="22" rx="5" fill="rgba(157,252,90,.14)"/>' % (x + 8, yy - 15, w - 16))
        for c, t in zip(cols, [vid, mac, port, kind]):
            o.append(txt(c, yy, t, 11.5, INK, 600, "start", mono=True))
        o.append("</g>")
    o.append("</g>")
    return "".join(o)


def frame_strip(x, y, fields, w=1000, h=42, ph=None, cap=""):
    """Полоса полей кадра: fields = [(подпись, доля, цвет)]."""
    a = ' data-ph="%d"' % ph if ph is not None else ""
    tot = float(sum(f[1] for f in fields))
    o = ['<g%s>' % a]
    cx = x
    for (name, share, col) in fields:
        fw = w * share / tot
        o.append('<rect x="%g" y="%g" width="%g" height="%g" rx="6" fill="rgba(10,30,70,.85)" stroke="%s" stroke-width="1.8"/>'
                 % (cx + 2, y, fw - 4, h, col))
        o.append(txt(cx + fw / 2.0, y + h / 2.0 + 5, name, 12.5, col, 800))
        cx += fw
    if cap:
        o.append(txt(x + w / 2.0, y - 10, cap, 13, SOFT, 700))
    o.append("</g>")
    return "".join(o)
