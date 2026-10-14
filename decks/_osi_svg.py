# -*- coding: utf-8 -*-
"""SVG-примитивы для сцен практики: устройства, провода, бегущие пакеты, таблицы."""

from typing import Sequence

PAL = {
    "l1": "#7a8699", "l2": "#e0922f", "l3": "#3b82f6", "l4": "#8b5cf6",
    "l5": "#0ea5a3", "l6": "#d9557f", "l7": "#22a060",
    "red": "#e2504b", "green": "#22a060", "amber": "#e0922f", "ink": "#25314a", "dim": "#6b788f",
    "line": "#d7deea", "deep": "#101726",
}


def svg(w: int, h: int, body: str, x0: int = 0, y0: int = 0) -> str:
    return ('<svg class="sv" viewBox="%d %d %d %d" role="img">%s</svg>' % (x0, y0, w, h, body))


def s_(v) -> str:
    return ("%g" % v)


def txt(x, y, t, size=12, anchor="middle", fill=PAL["ink"], weight=600, mono=False, cls="", extra="") -> str:
    return ('<text x="%s" y="%s" text-anchor="%s" font-size="%s" font-weight="%s" fill="%s"%s%s>%s</text>'
            % (s_(x), s_(y), anchor, size, weight, fill,
               ' class="mono %s"' % cls if mono else (' class="%s"' % cls if cls else ""),
               (" " + extra) if extra else "", t))


def box(x, y, w, h, fill="#ffffff", stroke=PAL["line"], r=10, sw=1.2, extra="") -> str:
    return ('<rect x="%s" y="%s" width="%s" height="%s" rx="%s" fill="%s" stroke="%s" stroke-width="%s"%s/>'
            % (s_(x), s_(y), s_(w), s_(h), r, fill, stroke, sw, (" " + extra) if extra else ""))


def dev(x, y, label, sub="", kind="pc", w=132, h=62, accent=PAL["l3"]) -> str:
    """Устройство: прямоугольник с глифом, подписью и адресом."""
    g = box(x, y, w, h, "#ffffff", PAL["line"], 11)
    ic = x + 16
    cy = y + 21
    if kind == "pc":
        g += box(ic - 9, cy - 8, 20, 15, "rgba(59,130,246,.14)", accent, 3, 1.1)
        g += '<path d="M%s %s h12" stroke="%s" stroke-width="1.6" stroke-linecap="round"/>' % (
            s_(ic - 5), s_(cy + 11), accent)
    elif kind == "srv":
        for k in range(3):
            g += box(ic - 9, cy - 9 + k * 8, 20, 6, "rgba(34,160,96,.16)", PAL["green"], 2, 1)
    elif kind == "sw":
        g += box(ic - 10, cy - 7, 22, 14, "rgba(224,146,47,.16)", PAL["l2"], 3, 1.1)
        g += '<path d="M%s %s h16 M%s %s h16" stroke="%s" stroke-width="1.4"/>' % (
            s_(ic - 7), s_(cy - 2), s_(ic - 7), s_(cy + 3), PAL["l2"])
    elif kind == "rt":
        g += ('<circle cx="%s" cy="%s" r="11" fill="rgba(59,130,246,.14)" stroke="%s" stroke-width="1.2"/>'
              % (s_(ic + 1), s_(cy), PAL["l3"]))
        g += ('<path d="M%s %s h14 M%s %s l-4 -3 M%s %s l-4 3" stroke="%s" stroke-width="1.5" '
              'fill="none" stroke-linecap="round"/>' % (s_(ic - 6), s_(cy), s_(ic + 8), s_(cy),
                                                        s_(ic + 8), s_(cy), PAL["l3"]))
    elif kind == "cloud":
        g = ('<path d="M%s %s a16 16 0 0 1 30 -10 a14 14 0 0 1 26 6 a13 13 0 0 1 -4 25 h-44 '
             'a14 14 0 0 1 -8 -21 z" fill="#f6f8fc" stroke="%s" stroke-width="1.2"/>'
             % (s_(x + 14), s_(y + 34), PAL["line"]))
    g += txt(x + w / 2 + 8, y + 22, label, 11.5, "middle", "#17213a", 760)
    if sub:
        g += txt(x + w / 2 + 8, y + 40, sub, 10.5, "middle", PAL["dim"], 600, mono=True)
    return g


def wire(x1, y1, x2, y2, color=PAL["line"], sw=2.4, dash="") -> str:
    return ('<path d="M%s %s L%s %s" stroke="%s" stroke-width="%s" fill="none" stroke-linecap="round"%s/>'
            % (s_(x1), s_(y1), s_(x2), s_(y2), color, sw,
               ' stroke-dasharray="%s"' % dash if dash else ""))


def arrow(x1, y1, x2, y2, color=PAL["l3"], sw=2, dash="", cls="", s=None) -> str:
    a = ('<path d="M%s %s L%s %s" stroke="%s" stroke-width="%s" fill="none" marker-end="url(#ah)"'
         % (s_(x1), s_(y1), s_(x2), s_(y2), color, sw))
    if dash:
        a += ' stroke-dasharray="%s"' % dash
    if cls:
        a += ' class="%s"' % cls
    if s is not None:
        a += ' data-s="%s"' % s
    return a + "/>"


def defs() -> str:
    return ('<defs>'
            '<marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
            'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="%s"/></marker>'
            '<marker id="ahr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
            'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="%s"/></marker>'
            '</defs>' % (PAL["l3"], PAL["red"]))


def pkt(x, y, label, path, s, color=PAL["l3"], w=116, h=30, sub="") -> str:
    """Пакет: группа с data-path (перемещение по шагам) и затуханием."""
    inner = box(0, 0, w, h, "#ffffff", color, 8, 1.6, 'opacity="0.98"')
    inner += box(0, 0, 5, h, color, color, 2)
    inner += txt(w / 2 + 3, h / 2 + (0 if not sub else -3), label, 10.5, "middle", "#17213a", 760, mono=True)
    if sub:
        inner += txt(w / 2 + 3, h / 2 + 9, sub, 9, "middle", PAL["dim"], 600, mono=True)
    keys = ""
    if path:
        parts = []
        for k in path.split("|"):
            st, xy = k.split(":")
            dx, dy = xy.split(",")
            parts.append("%s:%s,%s" % (st, s_(x + float(dx)), s_(y + float(dy))))
        keys = ' data-path="%s"' % "|".join(parts)
    return ('<g class="fade pk" data-s="%s"%s transform="translate(%s,%s)">%s</g>'
            % (s, keys, s_(x), s_(y), inner))


def bits(x, y, pattern: str, size=13, color=PAL["l1"], s=None, gap=13) -> str:
    """Строка нулей и единиц (моно)."""
    out = ""
    for i, ch in enumerate(pattern):
        out += txt(x + i * gap, y, ch, size, "middle",
                   PAL["l3"] if ch == "1" else color, 800, mono=True)
    return ('<g class="fade" data-s="%s">%s</g>' % (s, out)) if s is not None else out


def tbl(x, y, cols: Sequence[str], rows: Sequence[Sequence[str]], cw: Sequence[int],
        title="", rowh=22, s_rows: Sequence = ()) -> str:
    """Табличка внутри SVG; s_rows — номера шагов появления строк."""
    w = sum(cw)
    out = ""
    yy = y
    if title:
        out += txt(x, yy, title, 11, "start", "#17213a", 780)
        yy += 10
    out += box(x, yy, w, rowh * (len(rows) + 1), "#ffffff", PAL["line"], 8)
    cx = x
    out += ('<path d="M%s %s h%s" stroke="%s" stroke-width="1"/>' % (s_(x), s_(yy + rowh), s_(w), PAL["line"]))
    for i, c in enumerate(cols):
        out += txt(cx + 8, yy + rowh - 7, c, 9.5, "start", PAL["dim"], 780)
        cx += cw[i]
    for r, row in enumerate(rows):
        g = ""
        cx = x
        ry = yy + rowh * (r + 2) - 7
        for i, cell in enumerate(row):
            g += txt(cx + 8, ry, cell, 10, "start", "#17213a", 650, mono=True)
            cx += cw[i]
        if r < len(s_rows) and s_rows[r] is not None:
            out += '<g class="fade" data-s="%s">%s</g>' % (s_rows[r], g)
        else:
            out += g
    return out


def lvl_stack(x, y, w=250, rowh=34, labels=None, s_from=1, side="enc") -> str:
    """Столбик уровней OSI 7..1 с подсветкой по шагам."""
    labels = labels or ["L7 прикладной", "L6 представления", "L5 сеансовый", "L4 транспортный",
                        "L3 сетевой", "L2 канальный", "L1 физический"]
    cols = [PAL["l7"], PAL["l6"], PAL["l5"], PAL["l4"], PAL["l3"], PAL["l2"], PAL["l1"]]
    out = ""
    for i, lb in enumerate(labels):
        yy = y + i * rowh
        st = s_from + (i if side == "enc" else len(labels) - 1 - i)
        out += ('<g class="fade" data-s="%d">%s%s</g>'
                % (st,
                   box(x, yy, w, rowh - 5, "#ffffff", cols[i], 8, 1.4),
                   txt(x + 12, yy + rowh / 2 + 1, lb, 11.5, "start", "#17213a", 720)))
    return out
