# -*- coding: utf-8 -*-
"""Хелперы и исходные данные практики по модели OSI."""

from typing import Iterable, Sequence

# ======================================================================
#  Единая легенда сети — используется во ВСЕХ сценариях практики
# ======================================================================

NET = {
    "lan": "192.168.10.0/24",
    "mask": "255.255.255.0",
    "pc1": {"name": "ПК-1 (Аня)", "ip": "192.168.10.25", "mac": "A4:5E:60:1A:0C:25", "port": "Gi1/0/5"},
    "pc2": {"name": "ПК-2 (Борис)", "ip": "192.168.10.26", "mac": "A4:5E:60:1A:0C:26", "port": "Gi1/0/6"},
    "srv": {"name": "Сервер bitrix.local (1С + Битрикс24)", "ip": "192.168.10.10",
            "mac": "00:1B:21:7F:3D:10", "port": "Gi1/0/1"},
    "dns": {"name": "DNS предприятия", "ip": "192.168.10.5", "mac": "00:1B:21:7F:3D:05", "port": "Gi1/0/2"},
    "gw": {"name": "Маршрутизатор R1 (шлюз)", "ip": "192.168.10.1", "mac": "E8:94:F6:2B:11:01", "port": "Gi1/0/24"},
    "wan": {"ip": "95.84.17.33", "mac": "E8:94:F6:2B:11:02", "isp_ip": "95.84.17.1",
            "isp_mac": "00:25:90:AA:BB:01"},
    "vk": {"host": "vk.com", "ip": "87.240.190.78"},
    "tg": {"host": "api.telegram.org", "ip": "149.154.167.220"},
    "dns_up": "8.8.8.8",
}

SEC: list = []          # готовые <section>
NAV: list = []          # (id, подпись) для верхней навигации


# ======================================================================
#  Базовые хелперы
# ======================================================================

def esc(t: str) -> str:
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def section(sid: str, nav: str, body: str) -> None:
    """Добавляет секцию в страницу и пункт в навигацию."""
    NAV.append((sid, nav))
    SEC.append('<section class="sc" id="%s">\n%s\n</section>' % (sid, body))


def head(kick: str, title: str, lead: str = "") -> str:
    out = '<div class="rv"><div class="kick"><i></i>%s</div><h2>%s</h2>' % (kick, title)
    if lead:
        out += '<p class="lead">%s</p>' % lead
    return out + "</div>"


def card(title: str = "", body: str = "", cls: str = "", num: str = "", lvl: str = "") -> str:
    inner = ""
    if title or num or lvl:
        inner += '<div class="ch">'
        if num:
            inner += '<span class="num">%s</span>' % num
        if title:
            inner += "<h3>%s</h3>" % title
        if lvl:
            inner += lvl
        inner += "</div>"
    return '<div class="c %s">%s%s</div>' % (cls, inner, body)


def lv(n: int) -> str:
    names = {1: "L1 физический", 2: "L2 канальный", 3: "L3 сетевой", 4: "L4 транспортный",
             5: "L5 сеансовый", 6: "L6 представления", 7: "L7 прикладной"}
    return '<span class="lv lv%d"><b>L%d</b> %s</span>' % (n, n, names[n].split(" ", 1)[1])


def ul(items: Iterable[str], cls: str = "") -> str:
    return '<ul class="ck %s">%s</ul>' % (cls, "".join("<li>%s</li>" % i for i in items))


def p(*paras: str) -> str:
    return "".join("<p>%s</p>" % t for t in paras)


def grid(cls: str, *cells: str) -> str:
    return '<div class="g %s rv">%s</div>' % (cls, "".join(cells))


def kv(t: str) -> str:
    return '<span class="kv">%s</span>' % t


def table(cols: Sequence[str], rows: Sequence[Sequence[str]], caption: str = "",
          mono: Sequence[int] = (), row_cls: Sequence[str] = ()) -> str:
    out = '<div class="tw rv"><table>'
    if caption:
        out += "<caption>%s</caption>" % caption
    out += "<thead><tr>" + "".join(
        '<th%s>%s</th>' % (' class="m"' if i in mono else "", c) for i, c in enumerate(cols)
    ) + "</tr></thead><tbody>"
    for r, row in enumerate(rows):
        rc = row_cls[r] if r < len(row_cls) else ""
        out += "<tr%s>" % (' class="%s"' % rc if rc else "")
        for i, cell in enumerate(row):
            out += '<td%s>%s</td>' % (' class="m"' if i in mono else "", cell)
        out += "</tr>"
    return out + "</tbody></table></div>"


def callout(text: str, cls: str = "", mark: str = "i") -> str:
    return '<div class="callout %s rv"><i>%s</i><p>%s</p></div>' % (cls, mark, text)


# ======================================================================
#  Заголовки протоколов: поля с значениями
# ======================================================================

def fields(rows: Sequence[Sequence[str]], cls: str = "") -> str:
    """rows: (имя поля, значение, размер, подсказка, доп.класс)"""
    out = '<div class="hdr rv"><div class="hrow">'
    for r in rows:
        name, val = r[0], r[1]
        size = r[2] if len(r) > 2 else ""
        tip = r[3] if len(r) > 3 else ""
        extra = r[4] if len(r) > 4 else ""
        out += '<div class="fld %s %s" data-tip="%s"><div class="fn">%s</div><div class="fv">%s</div>%s</div>' % (
            cls, extra, tip.replace('"', "&quot;"), name, val,
            '<div class="fw">%s</div>' % size if size else "")
    return out + "</div></div>"


def pdu(parts: Sequence[Sequence[str]]) -> str:
    """parts: (класс, текст)"""
    return '<div class="pdu rv">%s</div>' % "".join(
        '<span class="%s">%s</span>' % (c, t) for c, t in parts)


# ======================================================================
#  Сцена с анимацией
# ======================================================================

def scene(title: str, svg: str, caps: Sequence[str], pace: int = 1200, tools: bool = True) -> str:
    cap = "".join('<div class="t" data-s="%d"><p>%s</p></div>' % (i + 1, c) for i, c in enumerate(caps))
    bar = ""
    if tools:
        bar = ('<button class="btn" data-act="prev">←</button>'
               '<button class="btn" data-act="next">→</button>'
               '<button class="btn" data-act="run">Прогон</button>'
               '<span class="stepn">0 / 0</span>')
    return ('<div class="scene rv" data-pace="%d"><div class="sh"><h4>%s</h4>%s</div>'
            '<div class="body">%s</div><div class="cap">%s</div></div>'
            % (pace, title, bar, svg, cap))


# ======================================================================
#  Задание с проверкой
# ======================================================================

def task(title: str, intro: str, qs: Sequence[Sequence[str]], answer: str) -> str:
    rows = ""
    for q in qs:
        label, ans, ph = q[0], q[1], (q[2] if len(q) > 2 else "")
        rows += ('<div class="qrow"><label>%s<input data-a="%s" placeholder="%s" '
                 'autocomplete="off" spellcheck="false"></label></div>'
                 % (label, ans.replace('"', "&quot;"), ph))
    return ('<div class="task rv"><div class="tt"><span class="tg">задание</span><h4>%s</h4></div>'
            '%s%s<div class="fo"><button class="btn" data-act="check">Проверить</button>'
            '<button class="btn" data-act="show">Показать разбор</button>'
            '<span class="ver"></span></div><div class="ans">%s</div></div>'
            % (title, p(intro) if intro else "", rows, answer))
