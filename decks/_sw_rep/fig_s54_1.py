# -*- coding: utf-8 -*-
"""fig_s54_1 — Рисунок 2.4.6.1: классификация VLAN (дерево). Вёрстка + SVG-коннекторы."""

W, H, TOP = 1218, 844, 0
P = "s54"
COLS = [  # x заголовка, ширина, центр стрелки, ствол x, x детей, цвет, заголовок, дети
    (78, 204, 180, 128, 180, "#2ad4ff", "По методу<br>создания", ["По умолчанию", "Статические", "Динамические"]),
    (445, 265, 547, 497, 547, "#9b6bff", "По методу<br>тегирования",
     ["На основе<br>портов", "На основе<br>MAC-адресов", "На основе<br>протоколов", "На основе<br>политик"]),
    (812, 198, 915, 865, 915, "#e05cff", "По виду<br>трафика", ["VLAN<br>управления", "VLAN данных", "Voice VLAN", "Multicast VLAN"]),
]
CY = [374, 497, 620, 742]   # центры дочерних плашек
KW = 164


def _marker(i, col):
    return (f'<marker id="{P}-a{i}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10Z" fill="{col}"/></marker>')


def _top():
    s = [f'<svg style="position:absolute;left:0;top:0;overflow:visible" width="{W}" height="{H}" fill="none" stroke-width="2.6">'
         f'<defs>{_marker("t", "#ffc53d")}</defs>'
         f'<path d="M547 131 L547 170 M180 170 L915 170" stroke="#ffc53d" pathLength="1" class="{P}-dw"/>']
    s += [f'<path d="M{c[2]} 170 L{c[2]} 207" stroke="#ffc53d" marker-end="url(#{P}-at)" pathLength="1" class="{P}-dw" style="animation-delay:.5s"/>'
          for c in COLS]
    s.append('</svg>')
    return "".join(s)


def _col(i):
    hx, hw, _, tx, kx, col, title, kids = COLS[i]
    n = len(kids)
    out = ['<div class="step">',
           f'<div class="{P}-bx {P}-hd" style="left:{hx}px;top:210px;width:{hw}px;height:83px;border-color:{col};box-shadow:0 0 14px {col}88">{title}</div>',
           f'<svg style="position:absolute;left:0;top:0;overflow:visible" width="{W}" height="{H}" fill="none" stroke="{col}" stroke-width="2.6">'
           f'<defs>{_marker(i, col)}</defs><path d="M{tx} 293 L{tx} {CY[n - 1]}" pathLength="1" class="{P}-dw"/>']
    out += [f'<path d="M{tx} {CY[k]} L{kx - 1} {CY[k]}" marker-end="url(#{P}-a{i})" pathLength="1" class="{P}-dw" style="animation-delay:{.3 + k * .2:.1f}s"/>'
            for k in range(n)]
    out.append('</svg>')
    out += [f'<div class="{P}-bx {P}-kid" style="left:{kx}px;top:{CY[k] - 41}px;width:{KW}px;height:82px;border-color:{col};animation-delay:{.4 + k * .2:.1f}s">{t}</div>'
            for k, t in enumerate(kids)]
    out.append('</div>')
    return "".join(out)


HTML = f"""<style>
.{P}-bx{{position:absolute;display:flex;align-items:center;justify-content:center;text-align:center;border:2.5px solid #2ad4ff;border-radius:10px;
  background:rgba(8,26,70,.85);color:#e6f1ff;font-family:"Golos Text",sans-serif;font-size:18px;line-height:24px}}
.{P}-hd{{font-weight:700;font-size:18.5px;color:#fff}}
.{P}-root{{font-weight:700;font-size:24px;border-radius:22px;border-color:#ffc53d;box-shadow:0 0 20px rgba(255,197,61,.55);color:#fff}}
.{P}-dw{{stroke-dasharray:1;stroke-dashoffset:0}}
.vis .{P}-dw{{animation:{P}-dr .8s ease-out both}}
@keyframes {P}-dr{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}
.vis .{P}-kid{{animation:{P}-in .45s ease-out both}}
@keyframes {P}-in{{from{{opacity:0;transform:translateX(-14px)}}to{{opacity:1;transform:none}}}}
.{P}-cap{{position:absolute;font-family:"Golos Text",sans-serif;font-style:italic;color:#cfe0ff;font-size:20px;white-space:nowrap}}
</style>
<div class="{P}-bx {P}-root step" style="left:425px;top:8px;width:245px;height:123px">Типы VLAN</div>
<div class="step">{_top()}</div>
{_col(0)}{_col(1)}{_col(2)}
<div class="{P}-cap step" style="left:355px;top:808px">Рисунок 2.4.6.1. – Классификация VLAN</div>
"""
