# -*- coding: utf-8 -*-
"""fig_s59_1 — вывод CLI из pptx 2.2, перерисован неоновой консолью (строки печатаются, команды набираются)."""
W, H, TOP = 952, 162, 0
BOX = (10, 4, 938, 154)  # рамка консоли: left, top, width, height
FS, FW = 29, 400  # кегль и жирность моноширинного
CAP = None  # подпись «Рисунок …»: текст, y-центр, кегль
# строки: (y-центр, шаг, [(x, [(вид, текст)])]); вид: p-приглашение, c-команда, o/h/y/r/d-вывод, cur-курсор
LINES = [(31, 0, [(30, [('p', 'switch(config)#'), ('c', 'interface gigabitethernet 1/0/1')])]),
 (79, 1, [(30, [('p', 'switch(config-if)#'), ('c', 'switchport mode access')])]),
 (128, 2, [(30, [('p', 'switch(config-if)#'), ('c', 'switchport access vlan 10')])])]

P = "fs591"  # префикс классов


def _seg(kind, text):
    from html import escape
    if kind == "c":  # команда/ввод: печатается посимвольно
        n = max(len(text), 1)
        return '<span class="%s-c" style="--n:%d;animation-duration:%dms">%s</span>' % (P, n, 150 + n * 30, escape(text))
    if kind == "cur":
        return '<span class="%s-cur">&nbsp;</span>' % P
    return '<span class="%s-%s">%s</span>' % (P, kind, escape(text))


CSS = ("<style>"
       ".{p}-box{{position:absolute;border-radius:10px;border:2px solid #2ad4ff;background:linear-gradient(180deg,rgba(4,10,28,.96),rgba(8,18,46,.96));"
       "box-shadow:0 0 16px rgba(42,212,255,.45),inset 0 0 26px rgba(42,212,255,.08)}}"
       ".{p}-ln{{position:absolute;font-family:'JetBrains Mono',monospace;white-space:pre;line-height:1;font-size:{fs}px;"
       "font-weight:{fw};color:#e6f1ff;transform:translateY(-50%)}}"
       ".{p}-p{{color:#8fb4e8}}.{p}-o{{color:#e6f1ff}}.{p}-h{{color:#2ad4ff}}.{p}-d{{color:#9b6bff}}.{p}-y{{color:#ffc53d}}.{p}-r{{color:#ff4d5e}}"
       ".{p}-c{{color:#9dfc5a;font-weight:700;text-shadow:0 0 8px rgba(157,252,90,.45);display:inline-block;vertical-align:bottom}}"
       ".step.vis .{p}-c{{animation-name:{p}-ty;animation-timing-function:steps(var(--n));animation-fill-mode:both}}"
       "@keyframes {p}-ty{{from{{clip-path:inset(0 100% 0 0)}}to{{clip-path:inset(0 0 0 0)}}}}"
       ".{p}-cur{{display:inline-block;width:.6em;background:#9dfc5a;box-shadow:0 0 8px #9dfc5a;animation:{p}-bl 1s steps(2) infinite}}"
       "@keyframes {p}-bl{{50%{{opacity:0}}}}"
       ".{p}-cap{{position:absolute;left:0;width:{w}px;text-align:center;font-family:'Golos Text',sans-serif;font-style:italic;"
       "color:#b9cdf0;transform:translateY(-50%)}}"
       "</style>").format(p=P, fs=FS, fw=FW, w=W)


def _build():
    out = [CSS, '<div class="%s-box" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"></div>' % ((P,) + BOX)]
    groups = {}
    for y, step, toks in LINES:
        body = "".join('<span class="%s-ln" style="left:%dpx;top:%dpx">%s</span>'
                       % (P, x, y, "".join(_seg(k, t) for k, t in segs)) for x, segs in toks)
        groups.setdefault(step, []).append(body)
    for s in sorted(groups):  # строки шага печатаются по очереди
        out.append('<div class="step">%s</div>' % "".join(
            '<div class="%s-li" style="animation-delay:%dms">%s</div>' % (P, j * 260, b) for j, b in enumerate(groups[s])))
    out.append("<style>.step.vis .%s-li{animation:%s-in .25s both}@keyframes %s-in{from{opacity:0}}</style>" % (P, P, P))
    if CAP:
        out.append('<div class="step"><div class="%s-cap" style="top:%dpx;font-size:%dpx">%s</div></div>' % (P, CAP[1], CAP[2], CAP[0]))
    return "".join(out)


HTML = _build()
