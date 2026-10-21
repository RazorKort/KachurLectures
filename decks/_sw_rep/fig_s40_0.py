# -*- coding: utf-8 -*-
"""fig_s40_0 — Рисунок 2.4.1.1: отправка компьютером ARP-запроса. Перерисовка в SVG.
Здесь же общий набор неоновых иконок (kit) для fig_s30_0/s32_0/s41_0/s42_0/s43_0."""

C = "#2ad4ff"; V = "#9b6bff"; M = "#e05cff"; G = "#9dfc5a"; Y = "#ffc53d"; R = "#ff4d5e"; O = "#ff9a3d"; B = "#5b7bff"


def css(p):
    """Общий CSS для префикса p (анимации запускаются, когда шаг .step получает .vis)."""
    return f"""<style>
.{p}-l{{position:absolute;left:0;top:0;pointer-events:none;overflow:visible}}
.{p}-dw{{stroke-dasharray:1;stroke-dashoffset:0}}
.vis .{p}-dw{{animation:{p}-dr 1.1s ease-out both}}
@keyframes {p}-dr{{from{{stroke-dashoffset:1}}to{{stroke-dashoffset:0}}}}
.vis .{p}-pop{{animation:{p}-pp .5s cubic-bezier(.3,1.6,.5,1) both;transform-box:fill-box;transform-origin:center}}
@keyframes {p}-pp{{from{{transform:scale(.2);opacity:0}}to{{transform:none;opacity:1}}}}
.vis .{p}-blink{{animation:{p}-bl 1.4s ease-in-out infinite;transform-box:fill-box;transform-origin:center}}
@keyframes {p}-bl{{50%{{opacity:.45}}}}
.vis .{p}-jig{{animation:{p}-jg 1.2s ease-in-out infinite alternate}}
@keyframes {p}-jg{{from{{transform:translate(-7px,0)}}to{{transform:translate(7px,0)}}}}
.{p}-tx{{font-family:"Golos Text",sans-serif;fill:#e6f1ff}}
.{p}-cap{{position:absolute;font-family:"Golos Text",sans-serif;font-style:italic;color:#cfe0ff;white-space:nowrap}}
</style>"""


def defs(p):
    """SVG-символы: коммутатор, ПК, маршрутизатор, конверт, облако."""
    return f"""<svg width="0" height="0" style="position:absolute"><defs>
<linearGradient id="{p}-gt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1a4f9a"/><stop offset="1" stop-color="#0c2c66"/></linearGradient>
<linearGradient id="{p}-gf" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#0c2c66"/><stop offset="1" stop-color="#071a40"/></linearGradient>
<filter id="{p}-glow" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<symbol id="{p}-sw" viewBox="0 0 120 100" overflow="visible">
 <path d="M8 22 L86 8 L116 30 L116 70 L38 92 L8 66 Z" fill="url(#{p}-gf)" stroke="{C}" stroke-width="2.4" stroke-linejoin="round"/>
 <path d="M8 22 L86 8 L116 30 L38 50 Z" fill="url(#{p}-gt)" stroke="{C}" stroke-width="2.4" stroke-linejoin="round"/>
 <path d="M38 50 L38 92" stroke="{C}" stroke-width="2"/>
 <g stroke="#dff6ff" stroke-width="3" stroke-linecap="round" fill="none">
  <path d="M40 22 L70 17 M64 13 L70 17 L65 21"/><path d="M78 26 L48 31 M54 27 L48 31 L54 35"/><path d="M52 40 L82 35 M76 31 L82 35 L77 39"/></g>
</symbol>
<symbol id="{p}-pc" viewBox="0 0 100 130" overflow="visible">
 <path d="M14 8 L72 20 L72 78 L14 66 Z" fill="#0d2d66" stroke="{C}" stroke-width="2.6" stroke-linejoin="round"/>
 <path d="M20 16 L66 26 L66 70 L20 60 Z" fill="#123f8a" opacity=".85"/>
 <path d="M40 72 L40 84 L54 88 M30 86 L60 92" stroke="{C}" stroke-width="2.6" fill="none" stroke-linecap="round"/>
 <path d="M4 98 L48 110 L58 102 L14 90 Z" fill="#0d2d66" stroke="{C}" stroke-width="2.2" stroke-linejoin="round"/>
 <ellipse cx="72" cy="114" rx="5" ry="3.5" fill="{C}"/>
</symbol>
<symbol id="{p}-rt" viewBox="0 0 140 100" overflow="visible">
 <path d="M6 36 L6 66 A64 26 0 0 0 134 66 L134 36" fill="url(#{p}-gf)" stroke="{C}" stroke-width="2.4"/>
 <ellipse cx="70" cy="36" rx="64" ry="26" fill="url(#{p}-gt)" stroke="{C}" stroke-width="2.4"/>
 <g stroke="#dff6ff" stroke-width="3.2" stroke-linecap="round" fill="none">
  <path d="M60 30 L40 20 M40 20 L48 18 M40 20 L44 26"/><path d="M80 30 L100 20 M100 20 L92 18 M100 20 L96 26"/>
  <path d="M60 42 L40 52 M40 52 L44 46 M40 52 L48 54"/><path d="M80 42 L100 52 M100 52 L96 46 M100 52 L92 54"/></g>
</symbol>
<symbol id="{p}-env" viewBox="0 0 80 56" overflow="visible">
 <rect x="2" y="2" width="76" height="52" rx="3" fill="rgba(255,197,61,.18)" stroke="{Y}" stroke-width="2.6"/>
 <path d="M2 4 L40 30 L78 4" fill="none" stroke="{Y}" stroke-width="2.4"/>
 <path d="M18 36 L56 36 L56 28 L72 40 L56 52 L56 44 L18 44 Z" fill="{Y}" opacity=".9"/>
</symbol>
<symbol id="{p}-cl" viewBox="0 0 200 110" overflow="visible">
 <path d="M40 92 C10 92 6 60 30 54 C22 24 62 14 76 30 C88 4 132 6 138 30 C164 16 196 40 178 62 C200 76 182 100 160 94 C140 110 60 112 40 92 Z" fill="rgba(42,212,255,.08)" stroke="{C}" stroke-width="2.4"/>
</symbol>
</defs></svg>"""


def use(p, sym, x, y, w, h, extra="", cls=""):
    return f'<use href="#{p}-{sym}" x="{x}" y="{y}" width="{w}" height="{h}" class="{cls}" {extra}/>'


def sw(p, x, y, w=120, h=100, label=None):
    s = use(p, "sw", x, y, w, h, 'filter="url(#%s-glow)"' % p)
    if label:
        s += (f'<text x="{x + w * .55}" y="{y + h * .78}" text-anchor="middle" font-family="Oswald,sans-serif" font-size="{int(h * .17)}" '
              f'fill="#fff" font-weight="500">{label}</text>')
    return s


def pc(p, x, y, w=100, h=130, cls=""):
    return use(p, "pc", x, y, w, h, 'filter="url(#%s-glow)"' % p, cls)


def env(p, cx, cy, ang=0, w=76, cls=""):
    h = w * 56 / 80
    return (f'<g transform="translate({cx} {cy}) rotate({ang})"><g class="{cls}">'
            f'{use(p, "env", -w / 2, -h / 2, w, h)}</g></g>')


def poly(pts, col, wdt=2.6, cls="", extra=""):
    d = "M" + " L".join("%s %s" % q for q in pts)
    return f'<path d="{d}" fill="none" stroke="{col}" stroke-width="{wdt}" stroke-linejoin="round" pathLength="1" class="{cls}" {extra}/>'


def arp(p, x, y, w, h, left=True, fs=19, cls=""):
    """Оранжевая стрелка-плашка «ARP Who has 10.10.1.6?» в прямоугольнике x,y,w,h."""
    hd = h * .42; t0, t1 = y + h * .22, y + h * .78
    if left:
        pts = [(x, y + h / 2), (x + hd, y), (x + hd, t0), (x + w, t0), (x + w, t1), (x + hd, t1), (x + hd, y + h)]
        tx = x + w * .6
    else:
        pts = [(x, t0), (x + w - hd, t0), (x + w - hd, y), (x + w, y + h / 2), (x + w - hd, y + h), (x + w - hd, t1), (x, t1)]
        tx = x + w * .42
    d = "M" + " L".join("%.1f %.1f" % q for q in pts) + " Z"
    cy = y + h / 2
    return (f'<g class="{cls}"><path d="{d}" fill="#6e3410" stroke="{O}" stroke-width="2.6" stroke-linejoin="round" filter="url(#{p}-glow)"/>'
            f'<text x="{tx:.0f}" y="{cy - fs * .2:.0f}" text-anchor="middle" font-family="Golos Text,sans-serif" font-weight="700" font-size="{fs}" fill="#fff">ARP Who has</text>'
            f'<text x="{tx:.0f}" y="{cy + fs * .95:.0f}" text-anchor="middle" font-family="Golos Text,sans-serif" font-weight="700" font-size="{fs}" fill="#ffd9b0">10.10.1.6?</text></g>')


def layer(W, H, p, body, step=True):
    return f'<svg class="{p}-l{" step" if step else ""}" width="{W}" height="{H}" viewBox="0 0 {W} {H}">{body}</svg>'


def label(p, x, y, t, fs=20):
    return f'<text x="{x}" y="{y}" class="{p}-tx" font-family="JetBrains Mono,monospace" font-size="{fs}">{t}</text>'


# ---------------- сама картинка 2.4.1.1 ----------------
W, H, TOP = 1152, 854, 0
P = "s40"

SW = [(172, 160, 125, 100), (172, 325, 125, 100), (172, 500, 125, 100), (66, 665, 125, 100)]
COLS = [425, 645, 845]
ROWS = [(150, 150, 110), (315, 315, 278), (490, 490, 455)]   # верх ПК по колонкам


def _links():
    out = []
    for i, (sx, sy, _, _) in enumerate(SW[:3]):
        r1, r2, r3 = ROWS[i]
        y0 = sy + 30
        out.append(poly([(sx + 108, y0 + 0), (395, r3 + 45), (COLS[2] + 20, r3 + 45)], C, 3, P + "-dw"))
        out.append(poly([(sx + 110, y0 + 12), (395, r2 + 22), (COLS[1] + 22, r2 + 22)], C, 3, P + "-dw"))
        out.append(poly([(sx + 112, y0 + 24), (COLS[0] + 22, r1 + 38)], C, 3, P + "-dw"))
    out.append(poly([(92, 690), (92, 232), (182, 232)], C, 3, P + "-dw"))
    out.append(poly([(110, 690), (110, 395), (182, 395)], C, 3, P + "-dw"))
    out.append(poly([(128, 690), (128, 575), (182, 575)], C, 3, P + "-dw"))
    return "".join(out)


def _pcs():
    out = []
    for i in range(3):
        for j in range(3):
            out.append(pc(P, COLS[j], ROWS[i][j], 95, 124))
    return "".join(out)


HTML = css(P) + defs(P) + "".join([
    layer(W, H, P, _links() + "".join(sw(P, *s, label="SW L2") for s in SW)),
    layer(W, H, P, _pcs() + label(P, 940, 188, "10.10.1.5") + label(P, 735, 240, "10.10.1.6")),
    layer(W, H, P, f'<circle cx="890" cy="160" r="46" fill="none" stroke="{O}" stroke-width="3" class="{P}-blink"/>'
          + arp(P, 718, 6, 182, 136, True, 19, P + "-pop")),
    f'<div class="{P}-cap step" style="left:0;width:{W}px;text-align:center;top:810px;font-size:21px">Рисунок 2.4.1.1. — Отправка компьютером ARP-запроса</div>',
])
