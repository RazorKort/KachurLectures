# -*- coding: utf-8 -*-
"""Компоненты мятно-бирюзовой деки: фон, иконки, карточки, схемы."""
import html as _h

def esc(s): return _h.escape(str(s), quote=False)

# ----------------------------------------------------------------- иконки
# тонкий контур 24x24, stroke-width задаётся классом .ci
I = {
 "gauge":   '<circle cx="12" cy="13" r="8"/><path d="M12 13l4.2-3.4M12 4v1.6M4.6 7.2l1.1 1.1M19.4 7.2l-1.1 1.1"/>',
 "wifi":    '<path d="M3.5 9.5a13 13 0 0 1 17 0M6.5 13a8.5 8.5 0 0 1 11 0M9.5 16.4a4 4 0 0 1 5 0"/><circle cx="12" cy="19.4" r="1"/>',
 "wave":    '<path d="M2 12h3l2.2-6 3 13 3-9.5 2.2 4.5H22"/>',
 "bolt":    '<path d="M13 2L5 13h6l-1 9 9-12h-6z"/>',
 "queue":   '<rect x="3" y="4" width="18" height="4.2" rx="1.2"/><rect x="3" y="10" width="18" height="4.2" rx="1.2"/><rect x="3" y="16" width="18" height="4.2" rx="1.2"/>',
 "trash":   '<path d="M4 7h16M9 7V4.6h6V7M6.4 7l1 13.4h9.2L17.6 7"/>',
 "doc":     '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
 "layers":  '<path d="M12 3l9 4.6-9 4.6-9-4.6z"/><path d="M3 12.4l9 4.6 9-4.6M3 16.9l9 4.6 9-4.6"/>',
 "calc":    '<rect x="4" y="2.6" width="16" height="18.8" rx="2.2"/><path d="M7.6 7h8.8M8 12h.01M12 12h.01M16 12h.01M8 16.4h.01M12 16.4h.01M16 16.4h.01"/>',
 "clock":   '<circle cx="12" cy="12" r="8.6"/><path d="M12 7v5.3l3.4 2"/>',
 "shield":  '<path d="M12 2.8l7.6 3v5.6c0 4.6-3.1 8.2-7.6 9.8-4.5-1.6-7.6-5.2-7.6-9.8V5.8z"/><path d="M8.8 12l2.3 2.3 4.1-4.3"/>',
 "lock":    '<rect x="4.6" y="10.4" width="14.8" height="10" rx="2.2"/><path d="M8.2 10.4V7.6a3.8 3.8 0 0 1 7.6 0v2.8"/>',
 "server":  '<rect x="3" y="4" width="18" height="6.4" rx="1.6"/><rect x="3" y="13.6" width="18" height="6.4" rx="1.6"/><path d="M6.6 7.2h.01M6.6 16.8h.01"/>',
 "people":  '<circle cx="9" cy="8.4" r="3.2"/><path d="M3.4 19.6c0-3.1 2.5-5.4 5.6-5.4s5.6 2.3 5.6 5.4"/><path d="M16.2 6.4a3 3 0 0 1 0 5.6M17.4 14.6c2 .7 3.3 2.5 3.3 5"/>',
 "cam":     '<path d="M3 7.4l13-2.6 1.4 5.4L4.4 13z"/><path d="M6 13.4V19M17.6 8.6l3.4-1.2"/>',
 "link":    '<path d="M10 13.6a4 4 0 0 0 5.7.3l2.6-2.6a4 4 0 0 0-5.7-5.7l-1.3 1.3"/><path d="M14 10.4a4 4 0 0 0-5.7-.3l-2.6 2.6a4 4 0 0 0 5.7 5.7l1.3-1.3"/>',
 "check":   '<path d="M5 12.6l4.6 4.6L19 7.4"/>',
 "cloud":   '<path d="M7 18.4a4.2 4.2 0 0 1-.3-8.4 5.6 5.6 0 0 1 10.8-1.3A3.9 3.9 0 0 1 17.6 18.4z"/>',
 "globe":   '<circle cx="12" cy="12" r="8.6"/><path d="M3.4 12h17.2M12 3.4a14 14 0 0 1 0 17.2 14 14 0 0 1 0-17.2"/>',
 "router":  '<rect x="3" y="13" width="18" height="6.4" rx="1.8"/><path d="M6.4 16.2h.01M9.6 16.2h.01M12 9.6V5.4M12 5.4l-2.4 2M12 5.4l2.4 2"/>',
 "switch":  '<rect x="3" y="7.6" width="18" height="9" rx="1.8"/><path d="M6.4 12h.01M9.4 12h.01M12.4 12h.01M15.4 12h.01M18 12h.01"/>',
 "chart":   '<path d="M4 20V4"/><path d="M4 20h16"/><rect x="7.4" y="12" width="2.8" height="5"/><rect x="12" y="8.4" width="2.8" height="8.6"/><rect x="16.6" y="5" width="2.8" height="12"/>',
 "gear":    '<circle cx="12" cy="12" r="3.1"/><path d="M12 2.8v2.4M12 18.8v2.4M21.2 12h-2.4M5.2 12H2.8M18.5 5.5l-1.7 1.7M7.2 16.8l-1.7 1.7M18.5 18.5l-1.7-1.7M7.2 7.2L5.5 5.5"/>',
 "key":     '<circle cx="8" cy="12" r="3.6"/><path d="M11.6 12H21M18 12v3.2M15 12v2.4"/>',
 "bug":     '<rect x="8" y="8" width="8" height="10" rx="4"/><path d="M8 11H4.6M16 11h3.4M8 15H4.6M16 15h3.4M9.4 7l-1.6-2M14.6 7l1.6-2"/>',
 "fish":    '<path d="M3 6v6a5 5 0 0 0 5 5h2"/><path d="M14.5 19.5c-2.6 0-4.5-1.9-4.5-4.2 0-2.3 1.9-4.2 4.5-4.2s4.5 1.9 4.5 4.2c0 2.3-1.9 4.2-4.5 4.2z"/><path d="M19 15.3l2.4-2v4z"/>',
 "mask":    '<path d="M4.4 9.6c0-3.4 3.4-6.2 7.6-6.2s7.6 2.8 7.6 6.2c0 5.2-3.4 11-7.6 11S4.4 14.8 4.4 9.6z"/><path d="M9 11h.01M15 11h.01"/>',
 "coins":   '<ellipse cx="12" cy="6.4" rx="7.6" ry="3.2"/><path d="M4.4 6.4v5c0 1.8 3.4 3.2 7.6 3.2s7.6-1.4 7.6-3.2v-5"/><path d="M4.4 11.6v5c0 1.8 3.4 3.2 7.6 3.2s7.6-1.4 7.6-3.2v-5"/>',
 "build":   '<path d="M4 20.4V5.2l8-2.6v17.8M12 20.4h8V9.6l-8-2.6"/><path d="M7 9h2M7 13h2M15.4 13h1.6M15.4 16.6h1.6"/>',
 "scale":   '<path d="M12 3.4v17M6 7.4h12M8.6 20.4h6.8"/><path d="M3 15l3-7.6L9 15a3 3 0 0 1-6 0zM15 15l3-7.6L21 15a3 3 0 0 1-6 0z"/>',
 "net":     '<circle cx="12" cy="4.6" r="2.2"/><circle cx="4.6" cy="18" r="2.2"/><circle cx="19.4" cy="18" r="2.2"/><path d="M10.6 6.6L6 16M13.4 6.6L18 16M6.8 18h10.4"/>',
 "grow":    '<path d="M4 18L9.6 11.6l3.6 3.2L20 6"/><path d="M15 6h5v5"/>',
 "eye":     '<path d="M2.4 12S5.8 6 12 6s9.6 6 9.6 6-3.4 6-9.6 6-9.6-6-9.6-6z"/><circle cx="12" cy="12" r="2.8"/>',
 "ban":     '<circle cx="12" cy="12" r="8.6"/><path d="M6.2 6.2l11.6 11.6"/>',
 "alert":   '<path d="M12 3.6L21 19.4H3z"/><path d="M12 9.4v4.4M12 16.6h.01"/>',
 "bulb":    '<path d="M9 17.4h6M10 20.6h4"/><path d="M12 3.4a5.6 5.6 0 0 1 3.4 10.1c-.6.5-.9 1.1-.9 1.8H9.5c0-.7-.3-1.3-.9-1.8A5.6 5.6 0 0 1 12 3.4z"/>',
 "flag":    '<path d="M5 21V3.6h12l-2.4 4 2.4 4H5"/>',
 "book":    '<path d="M4 4.6h6a3 3 0 0 1 3 3v12a2.4 2.4 0 0 0-2.4-2.4H4z"/><path d="M20 4.6h-6a3 3 0 0 0-3 3v12a2.4 2.4 0 0 1 2.4-2.4H20z"/>',
 "dl":      '<path d="M12 4v11M7.4 10.6L12 15.2l4.6-4.6M4.6 19.4h14.8"/>',
 "ul":      '<path d="M12 20V9M7.4 13.4L12 8.8l4.6 4.6M4.6 4.6h14.8"/>',
 "swap":    '<path d="M4 8.6h13l-3.2-3.2M20 15.4H7l3.2 3.2"/>',
 "star":    '<path d="M12 3.6l2.6 5.4 5.9.8-4.3 4.1 1 5.9-5.2-2.8-5.2 2.8 1-5.9L3.5 9.8l5.9-.8z"/>',
 "home":    '<path d="M3.6 10.6L12 3.8l8.4 6.8V20a.9.9 0 0 1-.9.9H4.5a.9.9 0 0 1-.9-.9z"/><path d="M9.6 20.9v-6.4h4.8v6.4"/>',
 "laptop":  '<rect x="4" y="5" width="16" height="10.4" rx="1.6"/><path d="M2 18.8h20"/>',
 "bank":    '<path d="M3 9.4L12 4l9 5.4M4.6 9.4v8.8M9.2 9.4v8.8M14.8 9.4v8.8M19.4 9.4v8.8M3 20.6h18"/>',
 "fire":    '<path d="M12 3.2s4.6 3.8 4.6 8.2a4.6 4.6 0 0 1-9.2 0c0-1.4.6-2.6 1.4-3.6 0 1.6.8 2.6 1.8 2.6 1.4 0 1.4-2.4 1.4-7.2z"/><path d="M12 20.8v-1.8"/>',
 "pkg":     '<path d="M12 3.2l8 4v9.6l-8 4-8-4V7.2z"/><path d="M4 7.2l8 4 8-4M12 11.2v9.6"/>',
 "stop":    '<circle cx="12" cy="12" r="8.6"/><path d="M9.2 9.2l5.6 5.6M14.8 9.2l-5.6 5.6"/>',
 "refresh": '<path d="M20 5.6v5h-5"/><path d="M19.4 10.6A7.6 7.6 0 1 0 19 15.4"/>',
}

def ico(name, cls="ci"):
    return ('<svg class="%s" viewBox="0 0 24 24" aria-hidden="true">%s</svg>'
            % (cls, I.get(name, I["check"])))

# ----------------------------------------------------------------- фон
def _cloud(cx, cy, w, h, seed=1):
    """Облачный силуэт из перекрывающихся эллипсов с плоским основанием."""
    import random
    r = random.Random(seed)
    lobes = []
    n = 6
    for i in range(n):
        t = i / (n - 1.0)
        # высота лобов: по краям ниже, в центре выше
        k = 0.42 + 0.58 * (1 - abs(t - 0.5) * 2) ** 0.7
        rx = w * (0.16 + 0.10 * r.random())
        ry = h * k * (0.55 + 0.2 * r.random())
        x = cx - w / 2 + w * t
        y = cy - ry * 0.92
        lobes.append('<ellipse cx="%.0f" cy="%.0f" rx="%.0f" ry="%.0f"/>' % (x, y, rx, ry))
    lobes.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="%.0f"/>'
                 % (cx - w / 2, cy - h * 0.30, w, h * 0.30 + 6, h * 0.14))
    return "".join(lobes)


def background():
    """Облачная сцена: градиентное небо, слои облаков, силуэты города."""
    import random
    rnd = random.Random(12)

    def city(x_from, x_to, y_base, up=True, cls=""):
        out, x = [], x_from
        step_dir = 1 if x_to > x_from else -1
        while (x < x_to) if step_dir > 0 else (x > x_to):
            w = rnd.randint(14, 34)
            h = rnd.randint(34, 190)
            xx = x if step_dir > 0 else x - w
            y = (y_base - h) if up else y_base
            out.append('<rect class="%s" x="%d" y="%d" width="%d" height="%d" fill="url(#%s)"/>'
                       % (cls, xx, y, w, h, "ct" if up else "ct2"))
            # окна
            for r in range(2, h // 22):
                out.append('<rect class="%s" x="%d" y="%d" width="4" height="5" fill="#9fe8d8" opacity=".30"/>'
                           % (cls, xx + 5, y + r * 18 if up else y + r * 18))
            x += step_dir * (w + rnd.randint(4, 11))
        return "".join(out)

    clouds = [
        # (cx, cy, w, h, opacity, class)
        (240, 930, 720, 300, .92, "cl1"),
        (820, 955, 880, 330, .80, "cl1"),
        (1230, 880, 560, 250, .66, "cl2"),
        (60, 770, 480, 190, .46, "cl2"),
    ]
    far = [(1300, 360, 560, 220, .26, "cl3"),
           (-60, 250, 500, 200, .24, "cl3"),
           (680, 10, 800, 140, .18, "cl4")]
    clf = "".join(
        '<g class="%s" fill="url(#cg)" opacity="%.2f">%s</g>'
        % (c, o, _cloud(cx, cy, w, h, i + 31))
        for i, (cx, cy, w, h, o, c) in enumerate(far))
    cl = "".join(
        '<g class="%s" fill="url(#cg)" opacity="%.2f">%s</g>'
        % (c, o, _cloud(cx, cy, w, h, i + 3))
        for i, (cx, cy, w, h, o, c) in enumerate(clouds))

    return f'''<svg id="bg" viewBox="0 0 1280 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs>
 <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#f2fbf8"/><stop offset=".55" stop-color="#e5f4ef"/>
  <stop offset="1" stop-color="#d4ebe3"/>
 </linearGradient>
 <linearGradient id="cg" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#ffffff"/><stop offset=".5" stop-color="#e2f4ed"/>
  <stop offset="1" stop-color="#a6d2c4"/>
 </linearGradient>
 <linearGradient id="ct" x1="0" y1="0" x2="0" y2="1">
  <stop offset="0" stop-color="#2a6b61" stop-opacity=".30"/>
  <stop offset="1" stop-color="#2a6b61" stop-opacity=".05"/>
 </linearGradient>
 <linearGradient id="ct2" x1="0" y1="1" x2="0" y2="0">
  <stop offset="0" stop-color="#2a6b61" stop-opacity=".22"/>
  <stop offset="1" stop-color="#2a6b61" stop-opacity=".04"/>
 </linearGradient>
</defs>
<rect width="1280" height="900" fill="url(#sky)"/>
{clf}
{city(0, 300, 900, up=True, cls="")}
{city(1280, 930, 900, up=True, cls="city2")}
{cl}
</svg>'''


# ----------------------------------------------------------------- карточки
def card(title=None, num=None, icon=None, body="", dark=False, cls="", tint=False):
    k = "c " + ("d" if dark else "l") + (" tint" if tint else "") + (" " + cls if cls else "")
    h = ""
    if title is not None:
        h = '<div class="ch">'
        if num: h += f'<span class="num">{num}</span>'
        h += f'<h3>{title}</h3>'
        if icon: h += ico(icon)
        h += '</div><div class="hr"></div>'
    return f'<div class="{k}">{h}{body}</div>'

def ul(items, kind=""):
    k = "ck" + (" " + kind if kind else "")
    return f'<ul class="{k}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

def res(text, bad=False, mark=None):
    m = mark or ("!" if bad else "✓")
    return f'<div class="res{" bad" if bad else ""}"><i>{m}</i><div>{text}</div></div>'

def bub(text, cls=""):
    return f'<div class="bub {cls}">{text}</div>'

def chain(links):
    """links: [(icon, 'две строки\\nподпись'), ...]; последнее звено — финальное."""
    out = []
    n = len(links)
    for i, (ic, lb) in enumerate(links):
        fin = " fin" if i == n - 1 else ""
        out.append(f'<div class="lk{fin}"><span class="bl">{ico(ic, "")}</span>'
                   f'<span class="lb">{lb}</span></div>')
        if i < n - 1:
            out.append('<span class="cv">›</span>')
    return '<div class="chain">' + "".join(out) + "</div>"

def table(headers, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in headers)
    tb = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tw {cls}"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>'

def grid(cols, items, cls=""):
    return f'<div class="g g{cols} {cls}">' + "".join(items) + "</div>"

def step(html, extra=""):
    return f'<div class="step {extra}">{html}</div>'

def bar(w, kind="", data=True):
    d = f' data-w="{w}"' if data else ""
    return f'<div class="bar {kind}"><i{d} style="width:{"0" if data else w}"></i></div>'

# ----------------------------------------------------------------- слайды
SL = []
def slide(label, head_html, body_html, scen=None):
    s = f'<section class="slide" data-label="{esc(label)}"' + (f' data-scen="{scen}"' if scen else "") + ">"
    if head_html: s += f'<div class="head">{head_html}</div>'
    s += f'<div class="sc">{body_html}</div></section>'
    SL.append(s)
    return s

def head(title, sub=None):
    h = f'<h1 class="t">{title}</h1>'
    if sub: h += f'<p class="sub">{sub}</p>'
    return h
