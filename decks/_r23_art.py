# -*- coding: utf-8 -*-
"""Иллюстрации в манере референсных инфографик 2.3: передняя панель ESR, бейджи сетей,
   светящиеся линии с бегущими пакетами, бытовые устройства, плитки с иконками."""

import re

from _r23_lib import ICON, txt, esc

_id = [0]


def _uid(p):
    _id[0] += 1
    return "%s%d" % (p, _id[0])


# ----------------------------------------------------------------------
#  иконки ICON внутри SVG
# ----------------------------------------------------------------------

EXTRA_ICONS = {
    "music": '<svg viewBox="0 0 24 24"><path d="M9 18V5l11-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/></svg>',
    "play":  '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="3"/><path d="M10 9l5 3-5 3z"/></svg>',
    "cart":  '<svg viewBox="0 0 24 24"><path d="M3 4h2l2.4 11h10.2L20 8H6.2"/><circle cx="9" cy="19" r="1.6"/><circle cx="17" cy="19" r="1.6"/></svg>',
    "mail":  '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
    "list":  '<svg viewBox="0 0 24 24"><path d="M9 6h11M9 12h11M9 18h11"/><circle cx="4.5" cy="6" r="1.2"/><circle cx="4.5" cy="12" r="1.2"/><circle cx="4.5" cy="18" r="1.2"/></svg>',
    "pin":   '<svg viewBox="0 0 24 24"><circle cx="17" cy="6" r="3"/><circle cx="6" cy="18" r="2.4"/><path d="M17 9c0 4-11 3-11 7"/></svg>',
    "fwd":   '<svg viewBox="0 0 24 24"><path d="M4 6l6 6-6 6M12 6l6 6-6 6"/></svg>',
    "hub":   '<svg viewBox="0 0 24 24"><circle cx="12" cy="6" r="2.6"/><circle cx="5" cy="18" r="2.6"/><circle cx="19" cy="18" r="2.6"/><path d="M12 8.6v4M12 12.6l-5 3.6M12 12.6l5 3.6"/></svg>',
    "cam":   '<svg viewBox="0 0 24 24"><rect x="3" y="7" width="13" height="8" rx="2"/><path d="M16 10l5-3v8l-5-3"/><path d="M7 15v4h6"/></svg>',
    "phone": '<svg viewBox="0 0 24 24"><rect x="7" y="2.5" width="10" height="19" rx="2.4"/><path d="M11 18.5h2"/></svg>',
    "tv":    '<svg viewBox="0 0 24 24"><rect x="2.5" y="4" width="19" height="13" rx="2"/><path d="M8 21h8"/></svg>',
    "pad":   '<svg viewBox="0 0 24 24"><path d="M7 8h10a4 4 0 014 4v2a3 3 0 01-5.4 1.8L14.4 14H9.6l-1.2 1.8A3 3 0 013 14v-2a4 4 0 014-4z"/><path d="M8 10.5v3M6.5 12h3"/><circle cx="16" cy="11" r=".8"/><circle cx="17.5" cy="13" r=".8"/></svg>',
}


def icon_inner(key):
    src = ICON.get(key) or EXTRA_ICONS[key]
    return re.sub(r"^<svg[^>]*>|</svg>$", "", src)


def icon(key, x, y, size, color="#fff", sw=2):
    """Иконка из набора ICON, вписанная в квадрат size×size с левым верхним углом (x, y)."""
    return ('<svg x="%.1f" y="%.1f" width="%.1f" height="%.1f" viewBox="0 0 24 24" fill="none" '
            'stroke="%s" stroke-width="%.1f" stroke-linecap="round" stroke-linejoin="round">%s</svg>'
            % (x, y, size, size, color, sw, icon_inner(key)))


TONE = {"v": ("#7c5cff", "#5b36e0"), "c": ("#3fc4f0", "#1593c9"), "m": ("#e46cf3", "#b02cc6"),
        "g": ("#2fcf87", "#119a5c"), "a": ("#ffc24d", "#e08b00"), "r": ("#ff7191", "#d9334f"),
        "i": ("#7b74ff", "#4f46e5")}


def tile_icon(key, x, y, s, tone="v"):
    """Иконка в скруглённом «самоцветном» квадрате с бликом, как на плакатах."""
    a, b = TONE[tone]
    gid = _uid("ti")
    return ('<defs><linearGradient id="%s" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="%s"/>'
            '<stop offset="1" stop-color="%s"/></linearGradient></defs>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="url(#%s)" filter="url(#sh)"/>'
            '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#fff" opacity=".18"/>%s'
            % (gid, a, b, x, y, s, s, s * .28, gid,
               x + 2, y + 2, s - 4, s * .42, s * .26, icon(key, x + s * .22, y + s * .22, s * .56)))


# ----------------------------------------------------------------------
#  передняя панель маршрутизатора ESR (1U, как на фото методички)
# ----------------------------------------------------------------------

def esr_front(x, y, w=520, cls="", label=None):
    h = w * 0.205
    x0, y0 = x - w / 2.0, y - h / 2.0
    out = ['<g class="esr %s">' % cls]
    # корпус и крышка в перспективе
    out.append('<path d="M%.1f %.1f L%.1f %.1f L%.1f %.1f L%.1f %.1f Z" fill="#eceaf6" stroke="#cfcae6" '
               'stroke-width="1.2"/>' % (x0 + w * .03, y0, x0 + w * .07, y0 - h * .34,
                                         x0 + w * 1.0 - w * .02, y0 - h * .34, x0 + w, y0))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="url(#esrBody)" '
               'stroke="#c9c4de" stroke-width="1.4" filter="url(#sh)"/>' % (x0, y0, w, h, h * .07))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#fff" opacity=".8"/>'
               % (x0 + 3, y0 + 2, w - 6, h * .06))
    # вентиляция слева и справа
    for (vx, cols) in ((x0 + w * .025, 9), (x0 + w * .70, 10)):
        for r in range(3):
            for c in range(cols):
                out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#9b94c2" opacity=".55"/>'
                           % (vx + c * w * .0125 + (w * .006 if r % 2 else 0), y0 + h * (.22 + r * .13), w * .0042))
    # слот и USB
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.5" fill="#3b3458"/>'
               % (x0 + w * .03, y0 + h * .72, w * .07, h * .07))
    for i, col in enumerate(("#3b3458", "#4f7dff")):
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.5" fill="%s"/>'
                   % (x0 + w * (.155 + i * .028), y0 + h * .56, w * .016, h * .26, col))
    # 8 портов RJ-45 (2×4) с индикаторами линка
    pw, ph = w * .044, h * .25
    for r in range(2):
        for c in range(4):
            px = x0 + w * .245 + c * pw * 1.18 + (w * .02 if c >= 2 else 0)
            py = y0 + h * (.24 + r * .37)
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#f7f6fc" stroke="#aaa3cc" '
                       'stroke-width="1"/>' % (px - 1.5, py - 1.5, pw + 3, ph + 3))
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.5" fill="#2e2850"/>'
                       % (px, py, pw, ph))
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#2e2850"/>'
                       % (px + pw * .3, py + ph, pw * .4, ph * .18))
            dur = 0.7 + ((r * 4 + c) * 0.37) % 1.3
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1" fill="#41e39a">'
                       '<animate attributeName="opacity" values="1;.25;1" dur="%.2fs" repeatCount="indefinite"/></rect>'
                       % (px + pw * .1, py + ph * .1, pw * .2, ph * .14, dur))
            num = r * 4 + c + 1
            ty = py - h * .045 if r == 0 else py + ph + h * .12
            out.append(txt(px + pw / 2, ty, str(num), fs=h * .085, color="#6c6596", weight=700))
    # SFP 2×2
    for r in range(2):
        for c in range(2):
            sx = x0 + w * .505 + c * w * .052
            sy = y0 + h * (.27 + r * .33)
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="1.5" fill="#d9d6ea" '
                       'stroke="#9d96c4"/>' % (sx, sy, w * .045, h * .2))
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#3a3358"/>'
                       % (sx + w * .006, sy + h * .05, w * .033, h * .1))
    # светодиоды состояния
    for i, (nm, col) in enumerate((("Power", "#41e39a"), ("Status", "#41e39a"), ("Alarm", "#ffb547"),
                                   ("Fan", "#41e39a"))):
        ly = y0 + h * (.3 + i * .14)
        out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s"/>' % (x0 + w * .625, ly, w * .0045, col))
        out.append(txt(x0 + w * .635, ly + h * .03, nm, fs=h * .075, color="#6c6596", anchor="start", weight=600))
    # консоль
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#2e2850" stroke="#aaa3cc"/>'
               % (x0 + w * .69 - w * .045, y0 + h * .58, w * .04, h * .24))
    # разъём питания
    px0 = x0 + w * .86
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#26213f"/>'
               % (px0, y0 + h * .22, w * .1, h * .58, h * .06))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#0f0c1f"/>'
               % (px0 + w * .015, y0 + h * .32, w * .07, h * .38, h * .05))
    for dx in (.03, .05, .07):
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#c9c4de"/>'
                   % (px0 + w * dx - w * .003, y0 + h * .42, w * .006, h * .16))
    out.append(txt(x0 + w * .05, y0 + h * .14, "ELTEX  ESR", fs=h * .08, color="#7c75a8", anchor="start", weight=800))
    if label:
        out.append(txt(x, y0 + h + h * .42, label, fs=h * .2, weight=800))
    out.append("</g>")
    return "".join(out)


def esr_ports(x, y, w=520):
    """Координаты центров портов 1…8 — чтобы подводить к ним линии."""
    h = w * 0.205
    x0, y0 = x - w / 2.0, y - h / 2.0
    pw, ph = w * .044, h * .25
    pts = []
    for r in range(2):
        for c in range(4):
            px = x0 + w * .245 + c * pw * 1.18 + (w * .02 if c >= 2 else 0)
            py = y0 + h * (.24 + r * .37)
            pts.append((px + pw / 2, py + ph / 2))
    return pts


# ----------------------------------------------------------------------
#  светящаяся линия с бегущими «кубиками»-пакетами
# ----------------------------------------------------------------------

def glink(d, col="#7c5cff", packets=2, dur=3.2, rev=False, cls=""):
    out = ['<g class="%s">' % cls,
           '<path d="%s" stroke="%s" stroke-width="11" fill="none" opacity=".16" stroke-linecap="round"/>' % (d, col),
           '<path d="%s" stroke="%s" stroke-width="3.2" fill="none" opacity=".75" stroke-linecap="round"/>' % (d, col),
           '<path class="flowl" d="%s" stroke="#fff" stroke-width="2.4" fill="none" stroke-linecap="round"/>' % d]
    kp = "1;0" if rev else "0;1"
    for i in range(packets):
        out.append('<g><rect x="-8" y="-8" width="16" height="16" rx="3.5" fill="#fff" stroke="%s" '
                   'stroke-width="2.4" transform="rotate(45)" filter="url(#sh)"/>'
                   '<rect x="-4" y="-4" width="8" height="8" rx="2" fill="%s" transform="rotate(45)" opacity=".75"/>'
                   '<animateMotion dur="%.1fs" begin="%.2fs" repeatCount="indefinite" path="%s" '
                   'keyPoints="%s" keyTimes="0;1" calcMode="linear"/></g>'
                   % (col, col, dur, i * dur / packets, d, kp))
    out.append("</g>")
    return "".join(out)


# ----------------------------------------------------------------------
#  бейдж сети (белая стеклянная плашка с иконкой)
# ----------------------------------------------------------------------

def badge(x, y, w, title, sub=None, key="globe", tone="v", h=None, cls=""):
    h = h or (78 if sub else 54)
    x0, y0 = x - w / 2.0, y - h / 2.0
    s = h * .62
    t_y = y0 + h * (.42 if sub else .6)
    out = ['<g class="%s">' % cls,
           '<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="16" fill="#fff" fill-opacity=".9" '
           'stroke="#fff" filter="url(#sh)"/>' % (x0, y0, w, h),
           tile_icon(key, x0 + 12, y0 + (h - s) / 2, s, tone),
           txt(x0 + 24 + s, t_y, title, fs=17, anchor="start", weight=800)]
    if sub:
        out.append(txt(x0 + 24 + s, t_y + 22, sub, fs=13.5, anchor="start", weight=600, color="#5d5682"))
    out.append("</g>")
    return "".join(out)


def subnet(x, y, text, tone="#6d4aff"):
    w = len(text) * 8.6 + 22
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="26" rx="13" fill="#fff" fill-opacity=".92" '
            'stroke="%s" stroke-opacity=".35"/>%s</g>'
            % (x - w / 2, y - 13, w, tone, txt(x, y + 5, text, fs=13.5, color="#3a2a8c", mono=True)))


# ----------------------------------------------------------------------
#  домашний Wi-Fi маршрутизатор
# ----------------------------------------------------------------------

def home_router(x, y, w=300):
    h = w * .34
    x0, y0 = x - w / 2.0, y - h / 2.0
    out = ['<g class="hrt">']
    # антенны
    for ax in (x0 + w * .16, x0 + w * .84):
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="%.1f" fill="#3b3458" '
                   'transform="rotate(%d %.1f %.1f)"/>'
                   % (ax - w * .018, y0 - h * 1.25, w * .036, h * 1.3, w * .018,
                      -6 if ax < x else 6, ax, y0))
    # волны Wi-Fi
    for i, r in enumerate((w * .09, w * .16, w * .23)):
        out.append('<path d="M%.1f %.1f A%.1f %.1f 0 0 1 %.1f %.1f" stroke="#fff" stroke-width="%.1f" '
                   'fill="none" stroke-linecap="round" opacity=".95"><animate attributeName="opacity" '
                   'values=".15;1;.15" dur="2.4s" begin="%.1fs" repeatCount="indefinite"/></path>'
                   % (x - r * .8, y0 - h * .55 - i * 2, r, r, x + r * .8, y0 - h * .55 - i * 2,
                      w * .022, i * .35))
    out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="#fff"/>' % (x, y0 - h * .45, w * .016))
    # корпус
    out.append('<path d="M%.1f %.1f Q%.1f %.1f %.1f %.1f L%.1f %.1f Q%.1f %.1f %.1f %.1f Z" '
               'fill="url(#esrBody)" stroke="#c9c4de" stroke-width="1.6" filter="url(#sh)"/>'
               % (x0, y0 + h * .2, x, y0 - h * .25, x0 + w, y0 + h * .2,
                  x0 + w * .96, y0 + h, x, y0 + h * 1.1, x0 + w * .04, y0 + h))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="5" rx="2.5" fill="#8a63ff" opacity=".7"/>'
               % (x - w * .1, y0 + h * .1, w * .2))
    # порты LAN (жёлтые) и WAN (синий)
    for i in range(4):
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#f5b638" stroke="#b07a00"/>'
                   % (x0 + w * (.16 + i * .11), y0 + h * .45, w * .085, h * .3))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#2f6bff" stroke="#173f9e"/>'
               % (x0 + w * .68, y0 + h * .45, w * .085, h * .3))
    out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="2" fill="#26213f"/>'
               % (x0 + w * .81, y0 + h * .5, w * .05, h * .2))
    out.append(txt(x0 + w * .38, y0 + h * 1.42, "LAN · локальная сеть", fs=15, color="#8a5c00"))
    out.append(txt(x0 + w * .72, y0 + h * 1.42 + 22, "WAN · в Интернет", fs=15, color="#173f9e"))
    out.append("</g>")
    return "".join(out)
