# -*- coding: utf-8 -*-
"""fig_s35_1 — перерисовка вывода CLI из pptx 2.2 (консоль, построчная печать)."""
import html

W, H, TOP = 1416, 472, 0
P = "fs35_1"
X0, CW = 57, 16          # левый край текста и ширина символа (px оригинала)
FS = CW / 0.6                    # JetBrains Mono: advance = 0.6em


def row(cols):
    """[(колонка, текст), ...] -> строка с выравниванием колонок как в оригинале."""
    s = ""
    for c, t in cols:
        s = s.ljust(c) + t
    return s


# (y-центр строки, шаг, вид, текст): вид n — обычный, c — команда, d — разделитель, cap — подпись
LINES = [
    (30, 1, 'h', row([(45, 'Flow'), (50, 'Link'), (65, 'Uptime'), (78, 'B')])),
    (77, 1, 'h', row([(0, 'Port'), (9, 'Type'), (22, 'Duplex'), (30, 'Speed'), (36, 'Neg'), (45, 'ctrl'), (50, 'State'), (64, '(d,h:m:s)'), (76, 'Pre')])),
    (123, 1, 'd', row([(0, '--------'), (9, '------------'), (22, '------'), (30, '-----'), (36, '--------'), (45, '----'), (50, '-----------'), (62, '-------------'), (76, '----')])),
    (168, 2, 'n', row([(0, 'gi1/0/1'), (9, '1G-Copper'), (22, 'Full'), (30, '1000'), (36, 'Enabled'), (45, 'Off'), (50, 'Up'), (62, '06,12:37:13'), (76, 'Dis')])),
    (214, 2, 'n', row([(0, 'gi1/0/2'), (9, '1G-Copper'), (22, 'Full'), (30, '1000'), (36, 'Enabled'), (45, 'Off'), (50, 'Up'), (62, '03,01:35:14'), (76, 'Dis')])),
    (260, 3, 'n', row([(0, 'gi1/0/3'), (9, '1G-Copper'), (24, '--'), (32, '--'), (39, '--'), (46, '--'), (50, 'Down (nc)'), (68, '--')])),
    (306, 3, 'n', row([(0, 'gi1/0/4'), (9, '1G-Copper'), (24, '--'), (32, '--'), (39, '--'), (46, '--'), (50, 'Down (nc)'), (68, '--')])),
    (352, 4, 'n', row([(0, 'gi1/0/5'), (9, '1G-Copper'), (22, 'Full'), (30, '1000'), (36, 'Enabled'), (45, 'Off'), (50, 'Up'), (62, '06,12:37:13'), (76, 'Dis')])),
    (404, 5, 'd', '---------------------------часть текста пропущена------------------------'),
    (449, 6, 'cap', 'Рисунок 2.3.1.1. – Первичная диагностика портов коммутатора ³'),
]


def _ln(y, st, kind, text):
    if kind == "cap":
        return ('<div class="%s-cap" style="top:%dpx">%s</div>' % (P, y - 15, html.escape(text)))
    t = html.escape(text)
    if kind == "c":   # команда: **…** -> подсветка
        parts = t.split("**")
        t = "".join(('<b>%s</b>' % x) if i % 2 else x for i, x in enumerate(parts))
    return ('<div class="%s-l %s-%s" style="top:%dpx;left:%dpx">%s</div>' % (P, P, kind, y - FS * 0.66, X0, t))


def _body():
    out, cur = [], None
    for y, st, kind, text in LINES:
        if st != cur:
            if cur is not None:
                out.append("</div>")
            out.append('<div class="step %s-st">' % P)
            cur = st
        out.append(_ln(y, st, kind, text))
    out.append("</div>")
    return "".join(out)


CSS = f"""<style>
.{P}-con{{position:absolute;left:4px;top:2px;width:{W - 8}px;height:{468}px;border-radius:12px;border:2px solid rgba(42,212,255,.55);
  background:linear-gradient(180deg,rgba(4,10,28,.92),rgba(6,16,40,.9));box-shadow:0 0 18px rgba(42,212,255,.35),inset 0 0 30px rgba(42,212,255,.08)}}
.{P}-st{{position:absolute;left:0;top:0;width:{W}px;height:{H}px}}
.{P}-l{{position:absolute;white-space:pre;font-family:'JetBrains Mono',monospace;font-size:{FS:.2f}px;line-height:1.3;color:#d8e8ff;letter-spacing:0}}
.{P}-l b{{color:#9dfc5a;font-weight:700;text-shadow:0 0 8px rgba(157,252,90,.55)}}
.{P}-d{{color:#2ad4ff;opacity:.75}}
.{P}-h{{color:#ffc53d}}
.{P}-cap{{position:absolute;left:0;width:{W}px;text-align:center;font-family:'Golos Text',sans-serif;font-style:italic;font-weight:600;font-size:21px;color:#b8c8ea;line-height:1.45}}
.{P}-cur{{position:absolute;width:{CW:.1f}px;height:{FS * 1.1:.0f}px;background:#9dfc5a;box-shadow:0 0 8px #9dfc5a;animation:{P}-blink 1s steps(1) infinite}}
@keyframes {P}-blink{{50%%{{opacity:0}}}}
</style>"""

HTML = CSS + f'<div class="{P}-con"></div>' + _body() + ''
