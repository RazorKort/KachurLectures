# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _figkit_s65 import *  # noqa
"""Q-in-Q (selective): packet №1–4 — на входе Gi0/11 добавляется внешняя метка SVLAN (кроме Vlan 31), на выходе снимается."""
W, H, TOP = 1428, 552, 0
CSS2 = """<style>
.s72-bx{position:absolute;width:96px;height:35px;box-sizing:border-box;border:2px solid #2ad4ff;background:rgba(10,40,100,.85);color:#fff;
  font:500 25px/31px 'Golos Text',sans-serif;text-align:center;box-shadow:0 0 10px rgba(42,212,255,.55)}
.s72-bx.s72-s{border-color:#e05cff;background:rgba(70,15,100,.85);box-shadow:0 0 12px rgba(224,92,255,.7)}
.s72-bx.s72-y{border-color:#ffc53d;background:rgba(80,55,10,.75);box-shadow:0 0 10px rgba(255,197,61,.55)}
.s72-io{position:absolute;width:66px;height:35px;background:rgba(157,252,90,.22);border:2px solid #9dfc5a;box-sizing:border-box;color:#d9ffc4;
  font:500 20px/31px 'Golos Text',sans-serif;text-align:center;box-shadow:0 0 10px rgba(157,252,90,.5)}
.s72-col{position:absolute;left:0;top:0;width:1428px;height:552px}
.s72-pk{position:absolute;width:30px}
.s72-pk i{display:block;height:11px;border-radius:2px;margin-bottom:2px}
@keyframes s72-dn{0%{transform:translateY(0);opacity:0}6%,92%{opacity:1}100%{transform:translateY(262px);opacity:0}}
@keyframes s72-up{0%{transform:translateY(262px);opacity:0}6%,92%{opacity:1}100%{transform:translateY(0);opacity:0}}
@keyframes s72-add{0%,45%{opacity:0;transform:scaleX(0)}55%,100%{opacity:1;transform:none}}
@keyframes s72-rem{0%,45%{opacity:1;transform:none}55%,100%{opacity:0;transform:scaleX(0)}}
.step.vis .s72-pk.s72-d{animation:s72-dn 3s linear infinite}
.step.vis .s72-pk.s72-u{animation:s72-up 3s linear infinite}
.step.vis .s72-pk .s72-add{animation:s72-add 3s linear infinite}
.step.vis .s72-pk .s72-rem{animation:s72-rem 3s linear infinite}
.step.vis .s72-new{animation:s72-pop .6s .5s ease-out both}
@keyframes s72-pop{from{opacity:0;transform:translateX(30px)}to{opacity:1;transform:none}}
</style>"""


def _arrow(c, y0, y1):
    """Полая блок-стрелка от y0 к y1 по оси x=c."""
    d = 1 if y1 > y0 else -1
    hy = y1 - d * 22
    pts = [(c - 8, y0), (c + 8, y0), (c + 8, hy), (c + 18, hy), (c, y1), (c - 18, hy), (c - 8, hy)]
    return ('<polygon points="%s" fill="rgba(10,30,80,.6)" stroke="#cfe0ff" stroke-width="2.5" stroke-linejoin="round"/>'
            % " ".join("%d,%d" % p for p in pts))


def _sw(c):
    x, y = c - 100, 155
    s = '<rect x="%d" y="202" width="180" height="7" rx="2" fill="rgba(155,107,255,.5)" stroke="#9b6bff" stroke-width="2"/>' % (c - 90)
    s += '<rect x="%d" y="%d" width="200" height="47" rx="10" fill="rgba(25,30,90,.92)" stroke="#9b6bff" stroke-width="3"/>' % (x, y)
    for r in range(2):
        for k in range(9):
            s += '<rect x="%d" y="%d" width="9" height="5" rx="1" fill="#b9c6ee"/>' % (x + 14 + k * 15, y + 13 + r * 14)
    s += '<rect x="%d" y="%d" width="30" height="28" rx="4" fill="#e6f1ff"/>' % (c + 57, y + 9)
    s += ('<g stroke="#2a6fe0" stroke-width="2.5"><line x1="%d" y1="%d" x2="%d" y2="%d"/><line x1="%d" y1="%d" x2="%d" y2="%d"/></g>'
          % (c + 63, y + 15, c + 81, y + 31, c + 81, y + 15, c + 63, y + 31))
    return s


def _box(c, y, txt, cls="", side="", extra=""):
    s = '<div class="s72-bx %s" style="left:%dpx;top:%dpx">%s</div>' % (cls, c - 48, y, txt)
    if side:
        s += t(c + 54, y + 7, side, 22, "#e05cff" if side == "SVLAN" else "#2ad4ff")
    return '<div class="%s" style="position:absolute;left:0;top:0">%s</div>' % (extra, s)


def _pk(c, up, tagged, col):
    out, cls = ("s72-u", "s72-rem") if up else ("s72-d", "s72-add")
    stripes = '<i style="background:%s;box-shadow:0 0 8px %s"></i>' % (col, col)
    if tagged:
        stripes += '<i class="%s" style="background:#e05cff;box-shadow:0 0 8px #e05cff"></i>' % cls
    return '<div class="s72-pk %s" style="left:%dpx;top:62px">%s</div>' % (out, c - 15, stripes)


COLS = [  # центр, №, вход?, Vlan
    (222, 1, True, "X"), (538, 2, False, "X"), (853, 3, True, "31"), (1170, 4, False, "31")]


def _col(c, n, inp, v):
    tagged = v == "X"
    col = "#2ad4ff" if tagged else "#ffc53d"
    cls = "" if tagged else "s72-y"
    svg = _sw(c) + (_arrow(c, 57, 152) + _arrow(c, 210, 306) if inp else _arrow(c, 306, 210) + _arrow(c, 152, 57))
    s = layer(W, H, svg, step=False)
    s += t(c - 56, 30, "packet №%d" % n, 22, anchor="r") + _box(c, 20, "Vlan " + v, cls, "CVLAN" if tagged else "")
    s += '<div class="s72-io" style="left:%dpx;top:122px">%s</div>' % (c - 170, "Вход" if inp else "Выход")
    s += t(c - 95, 130, "Gi0/11", 21) + t(c - 95, 219, "Gi0/12", 21)
    s += _box(c, 310, "Vlan " + v, cls, "CVLAN" if tagged else "")
    if tagged:
        s += _box(c, 345, "Vlan X", "s72-s", "SVLAN", "s72-new" if inp else "")
    s += _pk(c, not inp, tagged, col)
    return '<div class="s72-col step">%s</div>' % s


HTML = (CSS + CSS2 + "".join(_col(*c) for c in COLS) + '<div class="s72-col step">'
        + t(68, 422, "Условные обозначения:", 21)
        + t(74, 450, "•&nbsp;&nbsp;X - любой VLAN, кроме 31", 21)
        + t(74, 477, "•&nbsp;&nbsp;При добавлении метки <span style=\"color:#e05cff\">SVLAN</span> является внешней, "
                     "а <span style=\"color:#2ad4ff\">CVLAN</span> - внутренней", 21)
        + '</div>')
