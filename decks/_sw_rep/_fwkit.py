# -*- coding: utf-8 -*-
"""Общие детали вёрсток frame_ways / flood_* / forward_known / discard_fcs (префикс классов fw-)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

BLUE, VIO, MAG, GRN, YEL, RED, ORA = "#2ad4ff", "#9b6bff", "#e05cff", "#9dfc5a", "#ffc53d", "#ff4d5e", "#ff9a1f"

CSS = """<style>
.fw-pan{position:absolute;border-radius:8px;border:2px solid rgba(42,212,255,.75);background:rgba(6,24,64,.8);box-shadow:0 0 12px rgba(42,212,255,.35),inset 0 0 18px rgba(42,212,255,.1)}
.fw-sub{position:absolute;border-radius:6px;border:1.5px solid rgba(42,212,255,.45);background:rgba(4,16,46,.7)}
.fw-num{position:absolute;border-radius:50%;border:3px solid #2ad4ff;box-shadow:0 0 12px rgba(42,212,255,.8),inset 0 0 10px rgba(42,212,255,.4);
  display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:500;color:#fff;background:rgba(8,30,80,.9)}
.fw-tt{position:absolute;font-family:Oswald,sans-serif;font-weight:500;color:#2ad4ff;line-height:1.1;white-space:nowrap}
.fw-tx{position:absolute;color:#e6f1ff;line-height:1.3}
.fw-lab{position:absolute;border-radius:6px;border:2px solid rgba(200,225,255,.75);background:rgba(4,14,40,.9);color:#fff;
  font-family:Golos Text,sans-serif;font-weight:600;display:flex;align-items:center;justify-content:center;white-space:nowrap}
.fw-call{position:absolute;border-radius:8px;border:3px solid #ffb020;background:rgba(40,22,0,.82);box-shadow:0 0 18px rgba(255,176,32,.8),inset 0 0 14px rgba(255,140,0,.3)}
.fw-warn{position:absolute;border-radius:6px;border:2px solid #ff3b4e;background:rgba(60,4,14,.9);box-shadow:0 0 14px rgba(255,59,78,.7);
  color:#ff5a6a;font-family:Oswald,sans-serif;font-weight:500;line-height:1.15;text-align:center;display:flex;align-items:center;justify-content:center}
.fw-ok{position:absolute;border-radius:6px;border:2px solid #3ee86a;background:rgba(4,50,20,.9);box-shadow:0 0 14px rgba(62,232,106,.7);
  color:#7dff9a;font-family:Oswald,sans-serif;font-weight:500;line-height:1.15;text-align:center;display:flex;align-items:center;justify-content:center}
.fw-x{position:absolute;z-index:3;border-radius:50%;background:#e8152c;border:2px solid #fff;box-shadow:0 0 14px #ff3b4e;color:#fff;
  display:flex;align-items:center;justify-content:center;font-weight:700;font-family:Oswald,sans-serif}
.fw-tb{position:absolute;border-collapse:collapse;color:#e6f1ff;table-layout:fixed}
.fw-tb td{border:1.5px solid rgba(42,212,255,.4);text-align:center;padding:0;white-space:nowrap}
.fw-tb tr.fw-h td{color:#dfeaff}
.fw-tb tr.fw-g td{background:linear-gradient(180deg,#1f8a3a,#0f5a22);color:#fff;border-color:#4dff7a;box-shadow:inset 0 0 8px rgba(77,255,122,.4)}
.fw-tb{border:1.5px solid rgba(42,212,255,.6)}
.fw-f{position:absolute;border-radius:4px;display:flex;align-items:center;justify-content:center;text-align:center;font-family:Golos Text,sans-serif;
  font-weight:600;color:#10203a;line-height:1;box-shadow:0 0 8px rgba(255,255,255,.25)}
.fw-chipu{position:absolute;border-radius:8px;border:2px solid #2ad4ff;background:rgba(8,34,90,.95);box-shadow:0 0 18px rgba(42,212,255,.8);
  color:#fff;display:flex;align-items:center;justify-content:center;text-align:center;line-height:1.25}
.fw-chipu:before,.fw-chipu:after{content:"";position:absolute;left:10px;right:10px;height:8px;
  background:repeating-linear-gradient(90deg,#2ad4ff 0 6px,transparent 6px 13px)}
.fw-chipu:before{top:-12px}.fw-chipu:after{bottom:-12px}
.fw-svg{position:absolute;left:0;top:0;overflow:visible;pointer-events:none}
.fw-pk{position:absolute;left:0;top:0;width:28px;height:17px;border-radius:3px;offset-rotate:auto;
  animation:fwmove var(--d,2.4s) linear infinite;animation-delay:var(--dl,0s);opacity:0}
@keyframes fwmove{0%{offset-distance:0%;opacity:0}8%{opacity:1}88%{opacity:1}100%{offset-distance:100%;opacity:0}}
.fw-blink{position:absolute;border-radius:4px;border:3px solid currentColor;box-shadow:0 0 14px currentColor,inset 0 0 8px currentColor;animation:fwbl 1.2s ease-in-out infinite}
@keyframes fwbl{0%,100%{opacity:.25}50%{opacity:1}}
.fw-dash{stroke-dasharray:10 8;animation:fwdash 1s linear infinite}
@keyframes fwdash{to{stroke-dashoffset:-18}}
.fw-pulse{animation:fwpu 1.4s ease-in-out infinite}
@keyframes fwpu{0%,100%{filter:drop-shadow(0 0 2px currentColor)}50%{filter:drop-shadow(0 0 14px currentColor)}}
</style>"""


def pan(x, y, w, h, extra="", cls="fw-pan"):
    return '<div class="%s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;%s"></div>' % (cls, x, y, w, h, extra)


def tx(x, y, html, size=17, extra="", cls="fw-tx"):
    return '<div class="%s" style="left:%dpx;top:%dpx;font-size:%dpx;%s">%s</div>' % (cls, x, y, size, extra, html)


def tt(x, y, html, size=22, extra=""):
    return tx(x, y, html, size, extra, "fw-tt")


def pic(name, x, y, w):
    return img("rep/" + name, "left:%dpx;top:%dpx;width:%dpx" % (x, y, w), "ab")


def num(cx, cy, n, r=25, size=34):
    return '<div class="fw-num" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;font-size:%dpx">%s</div>' % (cx - r, cy - r, 2 * r, 2 * r, size, n)


def card(x, y, w, h, n, icon, iw, title, text, tsize=21, xsize=16, tx0=None, num_dx=38, icon_dx=None, ty=None, xy=None, delay=0):
    """Карточка шага: рамка, номер в круге, иконка-вырезка, заголовок, текст."""
    tx0 = tx0 if tx0 is not None else 135
    icon_dx = icon_dx if icon_dx is not None else 72
    ty = ty if ty is not None else 24
    xy = xy if xy is not None else ty + 32
    return ('<div class="step" style="transition-delay:%dms">' % delay + pan(x, y, w, h)
            + num(x + num_dx, y + 46, n) + pic(icon, x + icon_dx, y + 18, iw)
            + tt(x + tx0, y + ty, title, tsize) + tx(x + tx0, y + xy, text, xsize) + '</div>')


def table(x, y, cols, rows, rh, size=19, hl=(), head=True, hsize=None):
    """cols — ширины колонок; rows — списки ячеек (первая — заголовок, если head)."""
    w = sum(cols)
    cg = "".join('<col style="width:%dpx">' % c for c in cols)
    out = []
    for i, r in enumerate(rows):
        cls = "fw-h" if head and i == 0 else ("fw-g" if i in hl else "")
        fs = hsize if (cls == "fw-h" and hsize) else size
        out.append('<tr class="%s" style="height:%dpx;font-size:%dpx">%s</tr>' % (cls, rh[i] if isinstance(rh, (list, tuple)) else rh, fs,
                                                                     "".join("<td>%s</td>" % c for c in r)))
    return '<table class="fw-tb" style="left:%dpx;top:%dpx;width:%dpx"><colgroup>%s</colgroup>%s</table>' % (x, y, w, cg, "".join(out))


FCOL = {"DMAC": "linear-gradient(180deg,#e6f4ff,#a9d4ff)", "SMAC": "linear-gradient(180deg,#e2ffe0,#a6eaa6)",
        "ET": "linear-gradient(180deg,#fff9c8,#f3dc6a)", "DATA": "linear-gradient(180deg,#ffe6e6,#f5b0b0)",
        "FCSR": "linear-gradient(180deg,#ff8a8a,#f04848)", "FCSG": "linear-gradient(180deg,#8dff8d,#38d838)"}


def fields(y, h, spec, size=17):
    """spec: [(kind, x0, x1, text)] — цветные поля кадра."""
    return "".join('<div class="fw-f" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;font-size:%dpx;background:%s">%s</div>'
                   % (x0, y, x1 - x0, h, size, FCOL[k], t) for k, x0, x1, t in spec)


def svg(body, w=1672, h=941):
    return '<svg class="fw-svg" width="%d" height="%d" viewBox="0 0 %d %d">%s</svg>' % (w, h, w, h, body)


def arrow(x1, y1, x2, y2, color, sw=4, head=16, dash=False, glow=True):
    """Линия со стрелкой (наконечник — полигон, без marker id)."""
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(a), y2 - head * math.sin(a)
    px, py = -math.sin(a) * head * .55, math.cos(a) * head * .55
    f = ' style="filter:drop-shadow(0 0 5px %s)"' % color if glow else ""
    d = ' class="fw-dash"' if dash else ""
    return ('<g%s><line x1="%d" y1="%d" x2="%.1f" y2="%.1f" stroke="%s" stroke-width="%s"%s/>'
            '<polygon points="%d,%d %.1f,%.1f %.1f,%.1f" fill="%s"/></g>'
            % (f, x1, y1, bx, by, color, sw, d, x2, y2, bx + px, by + py, bx - px, by - py, color))


def poly(pts, color, sw=4, head=16, dash=False):
    """Ломаная со стрелкой на конце."""
    import math
    (x1, y1), (x2, y2) = pts[-2], pts[-1]
    a = math.atan2(y2 - y1, x2 - x1)
    bx, by = x2 - head * math.cos(a), y2 - head * math.sin(a)
    px, py = -math.sin(a) * head * .55, math.cos(a) * head * .55
    p = " ".join("%d,%d" % q for q in pts[:-1]) + " %.1f,%.1f" % (bx, by)
    d = ' class="fw-dash"' if dash else ""
    return ('<g style="filter:drop-shadow(0 0 5px %s)"><polyline points="%s" fill="none" stroke="%s" stroke-width="%s"%s/>'
            '<polygon points="%d,%d %.1f,%.1f %.1f,%.1f" fill="%s"/></g>' % (color, p, color, sw, d, x2, y2, bx + px, by + py, bx - px, by - py, color))


def packets(path, color, n=3, dur=2.4, delay=0.0, w=28, h=17):
    """Кадр (n квадратиков) летит по пути path (координаты оригинала), CSS offset-path."""
    out = []
    for i in range(n):
        out.append('<div class="fw-pk" style="offset-path:path(\'%s\');width:%dpx;height:%dpx;background:%s;'
                   'box-shadow:0 0 10px %s;--d:%.2fs;--dl:%.2fs"></div>' % (path, w, h, color, color, dur, delay + i * 0.16))
    return "".join(out)


def blink(x, y, w, h, color, delay=0.0):
    return '<div class="fw-blink" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;color:%s;animation-delay:%.2fs"></div>' % (x, y, w, h, color, delay)


def lab(x, y, w, h, html, size=22, extra=""):
    return '<div class="fw-lab" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx;font-size:%dpx;%s">%s</div>' % (x, y, w, h, size, extra, html)


def info(x, y, w, h, icon, ix, iw, text, tx_x, size=20):
    """Нижняя полоса-вывод."""
    return ('<div class="step">' + pan(x, y, w, h) + pic(icon, ix, y + (h - iw) // 2, iw)
            + tx(tx_x, y + (h - size * 1.3) / 2, text, size, "color:#2ad4ff;white-space:nowrap") + '</div>')


def cam_ba(N, dy=0):
    """CAM-таблица до (пустая) → ОБУЧЕНИЕ → после (одна строка SMAC ПК-1)."""
    y = 543 + dy
    return f"""<div class="step">
  {pan(25, y, 630, 157)}{pic(N + "tb.png", 48, y + 10, 40)}{tt(100, y + 9, "САМ-ТАБЛИЦА ДО КАДРА", 26)}
  {table(40, y + 49, [90, 190, 185, 136], [["VID", "MAC-адрес", "Интерфейс", "Тип"], ["—", "—", "—", "—"]], [44, 49], 20)}
</div>
<div class="step">
  {tt(686, y + 53, "ОБУЧЕНИЕ", 24)}
  {svg(arrow(676, y + 103, 842, y + 103, BLUE, 6, 26))}
  {packets("M 680 %d L 820 %d" % (y + 103, y + 103), "#7fe0ff", 1, 1.4, 0, 22, 12)}
</div>
<div class="step">
  {pan(860, y, 787, 157)}{pic(N + "tb2.png", 881, y + 9, 40)}{tt(937, y + 9, "САМ-ТАБЛИЦА ПОСЛЕ КАДРА", 26)}
  {table(873, y + 49, [99, 264, 250, 147], [["VID", "MAC-адрес", "Интерфейс", "Тип"], ["1", "34:60:f9:5f:df:5f", "gigabitethernet 1/0/2", "Dynamic"]], [44, 49], 21, hl=(1,))}
</div>"""


def fcs_proc(N, y=713, w=1088, chip="Проверка<br>FCS отброшен", out="ИСХОДЯЩИЕ КОПИИ"):
    """Панель «Процесс обработки FCS»: входящий кадр → чип → исходящие копии."""
    fy = y + 80
    return f"""<div class="step">
  {pan(25, y, w, 150)}{pic(N + "doc.png", 48, y + 7, 40)}{tt(100, y + 9, "ПРОЦЕСС ОБРАБОТКИ FCS", 25)}
  {pan(40, y + 47, 435, 93, "", "fw-sub")}{tt(52, y + 53, "ВХОДЯЩИЙ КАДР", 17, "color:#fff")}
  {fields(fy, 47, [("DMAC", 52, 125, "DMAC"), ("SMAC", 129, 203, "SMAC"), ("ET", 207, 278, "Ether<br>Type"), ("DATA", 282, 382, "Данные"), ("FCSR", 386, 456, "FCS")])}
  {svg(arrow(462, fy + 22, 505, fy + 22, BLUE, 4, 14) + arrow(642, fy + 22, 682, fy + 22, BLUE, 4, 14))}
  {packets("M 462 %d L 505 %d" % (fy + 22, fy + 22), "#7fe0ff", 1, 1.0, 0, 12, 8)}
  <div class="fw-chipu" style="left:518px;top:{y + 49}px;width:118px;height:88px;font-size:15px">{chip}</div>
  {pan(680, y + 47, 424, 93, "", "fw-sub")}{tt(696, y + 53, out, 17, "color:#fff")}
  {fields(fy, 47, [("DMAC", 697, 770, "DMAC"), ("SMAC", 774, 850, "SMAC"), ("ET", 853, 925, "Ether<br>Type"), ("DATA", 928, 1023, "Данные"), ("FCSG", 1027, 1094, "FCS")])}
</div>"""


def where(N, rows, y=713, x=1128, w=519, size=19):
    """Панель «Куда уходит кадр»."""
    r = "".join(pan(x + 15, y + 49 + i * 46, w - 31, 46, "", "fw-sub") + tx(x + 32, y + 60 + i * 46, t, size) for i, t in enumerate(rows))
    return f"""<div class="step">{pan(x, y, w, 150)}{pic(N + "share.png", x + 10, y + 3, 46)}{tt(x + 72, y + 9, "КУДА УХОДИТ КАДР", 25)}{r}</div>"""


def step_card(N, x, y, w, h, n, ic, ix, iy, iw, title, text, tx0, delay, tsize=20, xsize=14, ty=26, xy=60):
    return ('<div class="step" style="transition-delay:%dms">' % delay + pan(x, y, w, h) + num(x + 38, y + 46, n)
            + pic(N + ic, ix, iy, iw) + tt(tx0, y + ty, title, tsize) + tx(tx0, y + xy, text, xsize) + '</div>')
