# -*- coding: utf-8 -*-
"""Строительные блоки деки «Коммутаторы и коммутация»: фон, панели, сцены, картинки."""

import base64
import os

SL = []
_uid = [0]

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_sw_assets")
_cache = {}


def uid(pref="u"):
    _uid[0] += 1
    return "%s%d" % (pref, _uid[0])


def b64(name):
    """data-URI для webp-инфографики из _sw_assets."""
    if name not in _cache:
        with open(os.path.join(ASSETS, name + ".webp"), "rb") as fh:
            _cache[name] = "data:image/webp;base64," + base64.b64encode(fh.read()).decode()
    return _cache[name]


# ======================================================================
#  ФОН: ночной неоновый город + сетка схемы
# ======================================================================

def background():
    """Слоистый фон: сетка платы, силуэт города, неоновые дуги связей."""
    # силуэт города — два плана прямоугольников
    import random
    rnd = random.Random(20260214)

    def skyline(y0, h_min, h_max, col, op, step):
        out, x = [], -20
        while x < 1460:
            w = rnd.randint(26, 64)
            h = rnd.randint(h_min, h_max)
            out.append('<rect x="%d" y="%d" width="%d" height="%d" fill="%s" opacity="%.2f"/>'
                       % (x, y0 - h, w, h, col, op))
            # окошки
            for r in range(0, h - 14, 16):
                for cx in range(6, w - 8, 14):
                    if rnd.random() < .22:
                        out.append('<rect x="%d" y="%d" width="4" height="5" fill="#4fd8ff" opacity="%.2f"/>'
                                   % (x + cx, y0 - h + 10 + r, op * .9))
            x += w + step
        return "\n".join(out)

    far = skyline(900, 90, 250, "#0a1c3e", .85, 8)
    near = skyline(900, 60, 170, "#05142c", .95, 12)

    arcs = []
    for (x1, y1, x2, y2, c, op) in [
        (-40, 300, 520, 120, "#2ad4ff", .22), (420, 90, 1020, 260, "#2ad4ff", .18),
        (960, 160, 1480, 60, "#c45cff", .18), (-30, 540, 460, 420, "#2ad4ff", .12),
        (980, 460, 1470, 360, "#c45cff", .12), (160, 150, 900, 420, "#2ad4ff", .1),
    ]:
        mx, my = (x1 + x2) / 2, min(y1, y2) - 120
        arcs.append('<path d="M%d %d Q%d %d %d %d" fill="none" stroke="%s" stroke-width="2" opacity="%.2f"/>'
                    % (x1, y1, mx, my, x2, y2, c, op))
        arcs.append('<circle cx="%d" cy="%d" r="3.5" fill="%s" opacity="%.2f"/>' % (x1, y1, c, op * 2.4))
        arcs.append('<circle cx="%d" cy="%d" r="3.5" fill="%s" opacity="%.2f"/>' % (x2, y2, c, op * 2.4))

    return """<svg id="bg" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs>
  <linearGradient id="sky" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#02060f"/><stop offset=".55" stop-color="#051127"/>
    <stop offset="1" stop-color="#071a3c"/>
  </linearGradient>
  <pattern id="pcb" width="60" height="60" patternUnits="userSpaceOnUse">
    <path d="M0 30H60M30 0V60" stroke="#1b4e86" stroke-width="1" opacity=".30"/>
    <circle cx="30" cy="30" r="2.4" fill="#2ad4ff" opacity=".22"/>
    <path d="M0 0L18 18M60 60L42 42" stroke="#1b4e86" stroke-width="1" opacity=".20"/>
  </pattern>
  <radialGradient id="glow" cx=".5" cy=".5" r=".5">
    <stop offset="0" stop-color="#2ad4ff" stop-opacity=".30"/><stop offset="1" stop-color="#2ad4ff" stop-opacity="0"/>
  </radialGradient>
</defs>
<rect width="1440" height="900" fill="url(#sky)"/>
<rect width="1440" height="900" fill="url(#pcb)"/>
<ellipse cx="250" cy="200" rx="420" ry="300" fill="url(#glow)"/>
<ellipse cx="1210" cy="640" rx="420" ry="300" fill="url(#glow)" opacity=".7"/>
%s
%s
%s
<rect y="640" width="1440" height="260" fill="url(#sky)" opacity=".45"/>
</svg>
<div id="bgfx"></div>""" % ("\n".join(arcs), far, near)


# ======================================================================
#  КАРКАС СЛАЙДА
# ======================================================================

def slide(label, body, cover=False):
    cl = " cover-slide" if cover else ""
    SL.append('<section class="slide%s" data-label="%s">%s</section>' % (cl, _esc(label), body))


def _esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def head(title, sub=""):
    """Заголовок слайда. В title допускается <em>акцент</em>."""
    s = '<p class="sub">%s</p>' % sub if sub else ""
    return '<div class="head"><h1 class="t">%s</h1>%s</div>' % (title, s)


def sc(*blocks):
    return '<div class="sc">%s</div>' % "".join(blocks)


def g(cls, *items):
    return '<div class="g %s">%s</div>' % (cls, "".join(items))


def grow(cls, *items):
    return '<div class="g grow %s">%s</div>' % (cls, "".join(items))


def col(*items):
    return '<div class="col">%s</div>' % "".join(items)


def card(title, body, tone="", icon="", step=False):
    """Панель с неоновой рамкой."""
    h = ""
    if title:
        ic = '<div class="num %s">%s</div>' % (tone_num(tone), icon) if icon else ""
        h = '<div class="ch">%s<h3>%s</h3></div>' % (ic, title)
    cls = "c " + tone if tone else "c"
    out = '<div class="%s">%s%s</div>' % (cls, h, body)
    return '<div class="step">%s</div>' % out if step else out


def tone_num(tone):
    return {"cy": "", "mg": "v", "lm": "g", "am": "y", "rd": "r"}.get(tone, "")


def step(html):
    return '<div class="step">%s</div>' % html


def p(*txt):
    return "".join("<p>%s</p>" % t for t in txt)


def li(items, tone=""):
    return '<ul class="li %s">%s</ul>' % (tone, "".join("<li>%s</li>" % i for i in items))


def irow(text, tone="", icon="dot"):
    return '<div class="ir %s"><div class="ib">%s</div><span>%s</span></div>' % (tone, ICON.get(icon, ICON["dot"]), text)


def foot(text, kind=""):
    sign = {"warn": "!", "ok": "✓", "note": "⚑"}.get(kind, "i")
    return '<div class="foot %s"><i>%s</i><span>%s</span></div>' % (kind, sign, text)


def tags(*items):
    return '<div class="tags">%s</div>' % "".join(items)


def tag(text, tone="", mono=False):
    c = "tag " + tone + (" mono" if mono else "")
    return '<span class="%s">%s</span>' % (c.strip(), text)


def table(headers, rows, cls=""):
    th = "".join("<th>%s</th>" % h for h in headers)
    tr = []
    for r in rows:
        rcls = ""
        if isinstance(r, tuple):
            r, rcls = r
        tds = "".join("<td>%s</td>" % c for c in r)
        tr.append('<tr class="%s">%s</tr>' % (rcls, tds))
    return '<div class="tw %s"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div>' % (
        cls, th, "".join(tr))


def cli(lines, title="SWITCH (CLI)"):
    """Блок команд. Разметка: '#' комментарий, '>' подсветка команды."""
    out = []
    for ln in lines:
        if ln.startswith("# "):
            out.append('<span class="c">%s</span>' % _esc(ln[2:]))
        elif ln.startswith("> "):
            out.append('<span class="k">%s</span>' % _esc(ln[2:]))
        elif ln.startswith("! "):
            out.append('<span class="h">%s</span>' % _esc(ln[2:]))
        else:
            out.append(_esc(ln))
    body = "\n".join(out)
    t = '<div class="clih">%s</div>' % title if title else ""
    return "%s<pre class=\"cli\">%s</pre>" % (t, body)


def rep_html(name):
    """Вёрстка 1:1 инфографики из _sw_rep/<name>.py (W, H, HTML) или None."""
    import importlib.util
    f = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_sw_rep", name + ".py")
    if not os.path.exists(f):
        return None
    spec = importlib.util.spec_from_file_location("rep_" + name, f)
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
        m.W, m.H, m.HTML
    except Exception as e:  # вёрстка в процессе правки не должна валить сборку
        print("ОШИБКА вёрстки", name, e)
        return None
    top = getattr(m, "TOP", 0)  # срезать полосу заголовка оригинала сверху (заголовок даёт head слайда)
    return ('<div class="rep" data-rep="%s"><div class="repc" style="width:%dpx;height:%dpx;overflow:hidden">'
            '<div style="position:relative;width:%dpx;height:%dpx;margin-top:-%dpx">%s</div></div></div>'
            % (name, m.W, m.H - top, m.W, m.H, top, m.HTML))


def img(rel, style="", cls=""):
    """Картинка из _sw_assets (rel = 'rep/имя.png'), инлайн base64."""
    import mimetypes
    p = os.path.join(ASSETS, rel)
    if rel not in _cache:
        import io
        from PIL import Image
        buf = io.BytesIO()  # PNG-кропы пережимаются в webp при сборке: дека в разы легче
        Image.open(p).save(buf, "WEBP", quality=86, method=5)
        _cache[rel] = "data:image/webp;base64,%s" % base64.b64encode(buf.getvalue()).decode()
    return '<img class="%s" src="%s" style="%s" alt="">' % (cls, _cache[rel], style)


def pic(name, cap=""):
    """Инфографика-иллюстрация из комплекта лекции (если есть вёрстка 1:1 — она)."""
    r = rep_html(name)
    if r:
        return r
    c = '<div class="piccap">%s</div>' % cap if cap else ""
    return '<div class="pic"><img src="%s" alt="%s" loading="lazy"></div>%s' % (b64(name), _esc(cap), c)


def picblock(name, cap=""):
    return '<div class="g grow"><div class="col">%s</div></div>' % pic(name, cap)


# ======================================================================
#  СЦЕНА С КНОПКАМИ ВПЕРЁД / НАЗАД
# ======================================================================

def scene(svg, phases, sid=None):
    """Пошаговая анимация: svg + панель управления.

    phases — список подписей к шагам; элементы с data-ph="N" показываются,
    когда текущий шаг >= N. data-ph-only="N" — только на шаге N.
    """
    sid = sid or uid("sc")
    dots = "".join("<i></i>" for _ in phases)
    caps = "".join('<b data-cap="%d">%s</b>' % (i, c) for i, c in enumerate(phases))
    return (
        '<div class="scene" data-scene="%s" data-n="%d">'
        '<div class="figwrap">%s</div>'
        '<div class="scbar">'
        '<button class="sec" data-act="first">↺</button>'
        '<button data-act="prev">◀ Назад</button>'
        '<span class="pos">1 / %d</span>'
        '<button data-act="next">Вперёд ▶</button>'
        '<button class="sec" data-act="play">▷ Авто</button>'
        '<span class="dots">%s</span>'
        '<span class="cap" data-caps>%s</span>'
        "</div></div>"
    ) % (sid, len(phases), svg, len(phases), dots, caps)


# ======================================================================
#  ИКОНКИ
# ======================================================================

ICON = {
    "dot": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="6"/></svg>',
    "bolt": '<svg viewBox="0 0 24 24"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>',
    "sw": '<svg viewBox="0 0 24 24"><rect x="2" y="7" width="20" height="10" rx="2"/><path d="M6 12h.01M10 12h.01M14 12h.01M18 12h.01"/></svg>',
    "pc": '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></svg>',
    "tbl": '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 10h18M9 10v10"/></svg>',
    "shield": '<svg viewBox="0 0 24 24"><path d="M12 3 20 6v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/></svg>',
    "key": '<svg viewBox="0 0 24 24"><circle cx="8" cy="12" r="4"/><path d="M12 12h9l-2 3M17 12v3"/></svg>',
    "eye": '<svg viewBox="0 0 24 24"><path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg>',
    "gear": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3.4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M5 5l2 2M17 17l2 2M19 5l-2 2M7 17l-2 2"/></svg>',
    "warn": '<svg viewBox="0 0 24 24"><path d="M12 3 22 20H2z"/><path d="M12 10v4M12 17h.01"/></svg>',
    "ok": '<svg viewBox="0 0 24 24"><path d="M4 12.5 9.5 18 20 6"/></svg>',
    "no": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M7 7l10 10"/></svg>',
    "arrow": '<svg viewBox="0 0 24 24"><path d="M4 12h15M13 6l6 6-6 6"/></svg>',
    "tag": '<svg viewBox="0 0 24 24"><path d="M3 11V4h7l11 11-7 7z"/><circle cx="7.5" cy="7.5" r="1.4"/></svg>',
    "cable": '<svg viewBox="0 0 24 24"><path d="M5 3v6a4 4 0 0 0 8 0V3"/><path d="M9 13v8"/></svg>',
    "clock": '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
    "net": '<svg viewBox="0 0 24 24"><circle cx="12" cy="5" r="2.5"/><circle cx="5" cy="19" r="2.5"/><circle cx="19" cy="19" r="2.5"/><path d="M12 7.5v5M10 14l-3.5 3M14 14l3.5 3"/></svg>',
    "doc": '<svg viewBox="0 0 24 24"><path d="M6 3h8l4 4v14H6z"/><path d="M9 12h6M9 16h6"/></svg>',
    "chip": '<svg viewBox="0 0 24 24"><rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/></svg>',
    "split": '<svg viewBox="0 0 24 24"><path d="M4 6h5l5 6 5-6M4 18h5l5-6"/></svg>',
    "lock": '<svg viewBox="0 0 24 24"><rect x="4" y="10" width="16" height="11" rx="2"/><path d="M8 10V7a4 4 0 0 1 8 0v3"/></svg>',
}


# ======================================================================
#  ТЕСТ И ЗАДАЧИ
# ======================================================================

def quiz(question, options, correct, explain=""):
    """Вопрос теста: options — список строк, correct — индекс правильного."""
    opts = "".join('<button data-ok="%d">%s</button>' % (1 if i == correct else 0, o)
                   for i, o in enumerate(options))
    ex = '<div class="ex">%s</div>' % explain if explain else ""
    return '<div class="q"><div class="qt">%s</div><div class="opts">%s</div>%s</div>' % (question, opts, ex)


def task(tid, question, answer, explain, placeholder="ответ"):
    """Задача со свободным вводом ответа."""
    return (
        '<div class="q task" data-task="%s" data-ans="%s">'
        '<div class="qt">%s</div>'
        '<div class="inrow"><input type="text" placeholder="%s" autocomplete="off">'
        '<button data-act="check">Проверить</button>'
        '<button class="sec" data-act="show">Показать ответ</button></div>'
        '<div class="note" data-note></div>'
        '<div class="ex" data-ex>%s</div></div>'
    ) % (tid, _esc(answer), question, placeholder, explain)
