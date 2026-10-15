# -*- coding: utf-8 -*-
"""Блок 1, пересобранный по инфографикам методички (p03, p04, p05, p06):
   вместо вставленных картинок — живая вёрстка с теми же панелями и схемами."""

from _r23_lib import (slide, head, sc, g, col, card, step, steps, irow, foot, tag, tags,
                      fig, arrow, link, pill, txt, router, switch, pc, server, laptop,
                      globefig, shieldfig, ban, okmark, ICON)
from _r23_art import (esr_front, esr_ports, glink, badge, subnet, home_router, tile_icon,
                      icon, EXTRA_ICONS)


def it(key, html, tone=""):
    svg = ICON.get(key) or EXTRA_ICONS[key]
    return '<div class="it %s"><span class="hx">%s</span><p>%s</p></div>' % (tone, svg, html)


def scene(view, body):
    return '<div class="scene"><svg viewBox="%s" aria-hidden="true">%s</svg></div>' % (view, body)


# ======================================================================
#  слайд 3 — «Маршрутизатор (Router)» по плакату p03
# ======================================================================

def slide_router():
    X, Y, W = 500, 205, 560
    P = esr_ports(X, Y, W)
    body = (
        glink("M%.0f %.0f C %.0f 60, 360 72, 262 72" % (P[0][0], P[0][1], P[0][0] - 40), "#6d4aff")
        + glink("M%.0f %.0f C %.0f 340, 360 330, 262 330" % (P[4][0], P[4][1], P[4][0] - 40), "#1fb6e8", rev=True)
        + glink("M%.0f %.0f C %.0f 330, 600 345, 655 345" % (P[7][0], P[7][1], P[7][0]), "#d64ae8")
        + glink("M%.0f %.0f C %.0f 70, 690 66, 760 66" % (P[3][0], P[3][1], P[3][0]), "#6d4aff", rev=True)
        + esr_front(X, Y, W)
        + badge(140, 72, 244, "Офисная сеть", "ПК, принтеры, Wi-Fi", "wifi", "v")
        + badge(140, 330, 244, "Серверная сеть", "серверы, хранилища", "srv", "c")
        + badge(790, 345, 270, "Сеть устройств", "IoT, камеры, станки", "cam", "m")
        + badge(870, 66, 220, "Интернет", "глобальная сеть", "globe", "v")
        + subnet(360, 118, "192.168.1.0/24")
        + subnet(360, 288, "10.10.0.0/24")
        + subnet(585, 302, "172.16.0.0/24")
        + subnet(640, 110, "0.0.0.0/0")
    )
    slide("Маршрутизатор — определение", sc(
        head("Маршрутизатор <em>(Router)</em>",
             "Специализированное устройство, которое пересылает пакеты между сегментами сети "
             "на основе правил и таблицы маршрутизации."),
        g("g31 grow",
          col(
            g("g4",
              step(it("swap", "Пересылает пакеты между <b>сегментами сети</b> по правилам и таблице маршрутизации", "")),
              step(it("globe", "Связывает <b>разнородные сети</b> различных архитектур", "c2")),
              step(it("gear", "Решает по данным о <b>топологии сети</b> и правилам администратора", "m")),
              step(it("hub", "Разделяет <b>широковещательные домены</b> и области коллизий", "g"))),
            step(card(None, scene("0 0 1000 400", body), tone="w", cls="fill")),
          ),
          step(card("Уровни OSI",
                    '<div class="osi">'
                    '<div class="lv on"><i>3</i>Маршрутизатор — L3<br>IP-адреса, пакеты</div>'
                    '<div class="lv"><i>2</i>Коммутатор — L2<br>MAC-адреса, кадры</div>'
                    '<div class="lv"><i>1</i>Концентратор (Hub) — L1–L2</div>'
                    '</div>'
                    + '<div class="hr"></div>'
                    + irow("warn", "Концентраторы практически <b>не применяются</b> в современных сетях", "a"),
                    tone="vio")),
          ),
    ))


# ======================================================================
#  слайд 4 — как расходится широковещательный запрос (три мини-сцены)
# ======================================================================

def _broadcast():
    out = []

    def four(cx, cy, cls_lit, tone, lit):
        """Четыре ПК вокруг устройства; источник — левый нижний."""
        pos = [(cx - 120, cy - 70), (cx + 120, cy - 70), (cx - 120, cy + 80), (cx + 120, cy + 80)]
        s = []
        for i, (px, py) in enumerate(pos):
            s.append(link(cx, cy, px, py, w=3, color="#d8d0ff"))
        for i, (px, py) in enumerate(pos):
            s.append(pc(px, py, w=54, tone=("a" if i == 2 else ("v" if i in lit else "s"))))
        s.append(txt(pos[2][0], pos[2][1] + 50, "источник", fs=13.5, color="#8a5c00"))
        s.append(arrow(pos[2][0] + 22, pos[2][1] - 14, cx - 30, cy + 16, tone="a", w=4.5, cls="sq go-f"))
        for i in lit:
            px, py = pos[i]
            s.append(arrow(cx, cy, cx + (px - cx) * .78, cy + (py - cy) * .78, tone=tone, w=4.5,
                           cls="sq go-f"))
        return "".join(s)

    # Hub
    out.append(txt(170, 26, "Hub: во все порты", fs=17, color="#b11c3d"))
    out.append(four(170, 150, "", "r", [0, 1, 3]))
    out.append('<circle cx="170" cy="150" r="30" fill="#f0486b"/>' + txt(170, 156, "HUB", fs=15, color="#fff", weight=800))
    out.append(txt(170, 328, "кадр получают все — даже те, кому он не нужен", fs=13, color="#5d5682", weight=600))
    # Switch
    out.append(txt(520, 26, "Switch: только в нужный порт", fs=17, color="#0a6f94"))
    out.append(four(520, 150, "", "c", [1]))
    out.append(switch(520, 150, w=104))
    out.append(txt(520, 328, "кадр уходит только на MAC получателя", fs=13, color="#5d5682", weight=600))
    # Router
    out.append(txt(870, 26, "Router: broadcast не пропускает", fs=17, color="#4327c9"))
    out.append(pc(740, 90, w=50, tone="a") + pc(740, 220, w=50, tone="v"))
    out.append(txt(740, 132, "источник", fs=13.5, color="#8a5c00"))
    out.append(link(740, 90, 800, 150, w=3, color="#d8d0ff") + link(740, 220, 800, 150, w=3, color="#d8d0ff"))
    out.append(link(940, 150, 1000, 90, w=3, color="#d8d0ff") + link(940, 150, 1000, 220, w=3, color="#d8d0ff"))
    out.append(pc(1000, 90, w=50, tone="s") + pc(1000, 220, w=50, tone="s"))
    out.append(arrow(760, 106, 778, 194, tone="r", w=4, cls="sq go-f"))
    out.append(arrow(764, 98, 816, 140, tone="r", w=4, cls="sq go-f"))
    out.append(router(870, 150, w=120))
    out.append(ban(948, 112, r=16, cls="sq pop"))
    out.append('<rect x="700" y="40" width="130" height="230" rx="18" fill="none" stroke="#f0486b" '
               'stroke-dasharray="6 6" stroke-width="2" class="sq go-f"/>')
    out.append(txt(870, 328, "домен заканчивается на интерфейсе", fs=13, color="#5d5682", weight=600))
    return "".join(out)


def slide_devices():
    slide("Хаб · коммутатор · маршрутизатор", sc(
        head("Три устройства — <em>три зоны ответственности</em>",
             "Чем выше уровень, тем «умнее» решение о пересылке."),
        g("g3",
          step(card("Концентратор (Hub)", (
              "<p>Повторяет полученный сигнал <b>во все порты</b> без разбора. Все устройства "
              "оказываются в одном домене коллизий.</p>"
              + tags(tag("L1", "w"), tag("Все порты", "r"), tag("Устарел", "r"))), num="L1", tone="red")),
          step(card("Коммутатор (Switch)", (
              "<p>Читает <b>MAC-адрес</b> получателя и отправляет кадр только в нужный порт. "
              "Каждый порт — свой домен коллизий, но <b>широковещательный домен общий</b>.</p>"
              + tags(tag("L2", "w"), tag("MAC-адрес", "c2"), tag("Кадр", "c2"))), num="L2", tone="cya")),
          step(card("Маршрутизатор (Router)", (
              "<p>Читает <b>IP-адрес</b> получателя и по таблице выбирает интерфейс. Каждый "
              "интерфейс — <b>отдельный широковещательный домен</b>.</p>"
              + tags(tag("L3", "w"), tag("IP-адрес", "sol"), tag("Пакет", "w"))), num="L3", tone="vio")),
          ),
        step(card("Как расходится широковещательный кадр", scene("-20 0 1080 340", _broadcast()),
                  tone="w", cls="fill")),
    ), scen="sqf")


# ======================================================================
#  слайд 7 — «Маршрутизатор в сети Интернет» по плакату p04
# ======================================================================

def slide_home():
    b = []
    # панель LAN
    b.append('<rect x="14" y="14" width="350" height="400" rx="22" fill="#fff" fill-opacity=".72" stroke="#fff" filter="url(#sh)"/>')
    b.append(icon("box", 34, 30, 26, "#6d4aff"))
    b.append(txt(70, 50, "ДОМАШНЯЯ СЕТЬ (LAN)", fs=17, anchor="start", color="#4327c9", weight=800))
    devs = [("phone", "Смартфон", 34, 74), ("pc", "Ноутбук", 196, 74),
            ("tv", "Смарт-ТВ", 34, 242), ("pad", "Игровая консоль", 196, 242)]
    for k, nm, x, y in devs:
        b.append('<rect x="%d" y="%d" width="148" height="152" rx="16" fill="#fff" stroke="#e5e0f7"/>' % (x, y))
        b.append(icon(k, x + 34, y + 18, 80, "#6d4aff", sw=1.6))
        b.append(txt(x + 74, y + 134, nm, fs=14.5))
    # линии от устройств к LAN-портам
    hx, hy, hw = 600, 250, 330
    for i, (k, nm, x, y) in enumerate(devs):
        sx, sy = x + 148, y + 76
        px = hx - hw / 2 + hw * (.16 + i * .11) + hw * .042
        py = hy - hw * .34 / 2 + hw * .34 * .6
        b.append(glink("M%d %d C %d %d, %d %d, %.0f %.0f" % (sx, sy, sx + 70, sy, px - 90, py + 40, px, py),
                       "#1fb6e8", packets=1, dur=2.6 + i * .3))
    b.append(home_router(hx, hy, hw))
    # WAN к провайдеру и в Интернет
    wx = hx - hw / 2 + hw * .68 + hw * .042
    wy = hy - hw * .34 / 2 + hw * .34 * .6
    b.append(glink("M%.0f %.0f C 800 330, 820 250, 868 230" % (wx, wy), "#6d4aff", packets=2, dur=2.8))
    # панель Интернет
    b.append('<rect x="860" y="14" width="330" height="400" rx="22" fill="#fff" fill-opacity=".72" stroke="#fff" filter="url(#sh)"/>')
    b.append(icon("globe", 880, 30, 26, "#6d4aff"))
    b.append(txt(916, 50, "ИНТЕРНЕТ (WAN)", fs=17, anchor="start", color="#4327c9", weight=800))
    b.append(txt(880, 80, "Сервисы: сообщения · музыка · видео", fs=13.5, anchor="start", color="#5d5682", weight=600))
    b.append(txt(880, 100, "покупки · web-сайты · e-mail", fs=13.5, anchor="start", color="#5d5682", weight=600))
    sv = [("hello", "v"), ("music", "m"), ("play", "r"), ("cart", "a"), ("globe", "c"), ("mail", "g")]
    for i, (k, t) in enumerate(sv):
        x = 890 + (i % 3) * 98
        y = 130 + (i // 3) * 104
        b.append(tile_icon(k, x, y, 72, t))
    for i in range(5):
        b.append(server(905 + i * 58, 368, w=34))
    slide("Домашний маршрутизатор", sc(
        head("Маршрутизатор <em>в сети Интернет</em>",
             "Домашний маршрутизатор объединяет устройства локальной сети и обеспечивает доступ в Интернет."),
        step(card(None, scene("0 0 1204 430", "".join(b)), tone="w", cls="fill")),
        step(card("Как передаётся IP-пакет?",
                  g("g5",
                    it("doc", "<b>1.</b> Пакет поступает на <b>входной интерфейс</b>", ""),
                    it("eye", "<b>2.</b> Маршрутизатор определяет <b>сеть назначения</b>", "c2"),
                    it("split", "<b>3.</b> Выбирает необходимый <b>выходной интерфейс</b>", "m"),
                    it("fwd", "<b>4.</b> Пересылает пакет <b>к следующему узлу</b> или получателю", "g"),
                    it("bulb", "Каждая подключённая сеть требует <b>отдельного интерфейса</b>", "a")),
                  tone="w")),
    ))


# ======================================================================
#  слайд 9 — «Основные функции маршрутизаторов» по плакату p05
# ======================================================================

def slide_functions():
    X, Y, W = 330, 300, 470
    P = esr_ports(X, Y, W)
    body = (
        glink("M%.0f %.0f C %.0f 200, 420 190, 430 150" % (P[1][0], P[1][1], P[1][0]), "#6d4aff", packets=2)
        + glink("M%.0f %.0f C %.0f 160, 150 180, 130 150" % (P[0][0], P[0][1], P[0][0] - 20), "#1fb6e8", rev=True)
        + glink("M%.0f %.0f C %.0f 220, 560 210, 600 170" % (P[3][0], P[3][1], P[3][0]), "#d64ae8")
        + glink("M%.0f %.0f C %.0f 420, 560 410, 610 380" % (P[7][0], P[7][1], P[7][0]), "#1fb6e8", rev=True)
        + globefig(430, 95, r=66)
        + server(120, 110, w=62)
        + laptop(630, 140, w=104)
        + shieldfig(650, 290, w=60, tone="v")
        + pc(640, 400, w=74)
        + esr_front(X, Y, W)
    )
    slide("Основные функции · 1", sc(
        head("Основные функции <em>маршрутизаторов</em>",
             "Семь задач, ради которых устройство и ставят в сеть."),
        g("g32 grow",
          '<div class="g g2" style="grid-auto-rows:1fr">'
          + steps(
              it("list", "Поддержка <b>таблицы маршрутизации</b> и маршрутной информации", ""),
              it("pin", "Определение <b>наилучшего маршрута</b> для передачи пакетов к удалённым сетям", "c2"),
              it("fwd", "<b>Пересылка пакетов</b> к месту назначения", "m"),
              it("hub", "<b>Изоляция широковещательного</b> домена", "g"),
              it("globe", "<b>Доступ</b> к глобальной сети", "a"),
              it("swap", "<b>Преобразование</b> сетевых адресов (NAT)", "r"))
          + '</div>',
          col(step(card(None, scene("0 0 720 470", body), tone="w", cls="fill")),
              step(it("lock", "Специальные функции <b>обеспечения безопасности</b>: списки доступа, "
                              "межсетевой экран", ""))),
          ),
    ))


# ======================================================================
#  слайд 13 — функции на схеме R1 ↔ R2 по плакату p06
# ======================================================================

def slide_scheme():
    b = []
    for (x0, title, net) in ((14, "ЛОКАЛЬНАЯ СЕТЬ (LAN)", "192.168.1.0/24"),
                             (866, "ЛОКАЛЬНАЯ СЕТЬ (LAN)", "192.168.2.0/24")):
        b.append('<rect x="%d" y="14" width="320" height="330" rx="22" fill="#fff" fill-opacity=".72" '
                 'stroke="#fff" filter="url(#sh)"/>' % x0)
        b.append(txt(x0 + 20, 42, title, fs=13.5, anchor="start", color="#6d4aff", weight=800))
        b.append(txt(x0 + 20, 70, net, fs=18, anchor="start", mono=True, weight=800))
    # левая LAN
    b.append(server(230, 120, w=46) + pc(80, 140, w=58) + laptop(80, 270, w=70) + pc(230, 300, w=50))
    for (px, py) in ((230, 120), (80, 140), (80, 270), (230, 300)):
        b.append(link(170, 210, px, py, w=3, color="#d8d0ff"))
    b.append(switch(170, 210, w=100, label="SW1"))
    # правая LAN
    b.append(server(930, 120, w=46) + pc(1090, 140, w=58) + laptop(1090, 270, w=70) + pc(930, 300, w=50))
    for (px, py) in ((930, 120), (1090, 140), (1090, 270), (930, 300)):
        b.append(link(1020, 210, px, py, w=3, color="#d8d0ff"))
    b.append(switch(1020, 210, w=100, label="SW2"))
    # WAN
    b.append('<rect x="470" y="50" width="260" height="86" rx="18" fill="#fff" fill-opacity=".85" stroke="#fff" filter="url(#sh)"/>')
    b.append(txt(600, 84, "WAN", fs=18, weight=800))
    b.append(txt(600, 112, "192.168.3.0/30", fs=17, mono=True, weight=800, color="#4327c9"))
    b.append(glink("M60 140 L170 210 L460 210 L740 210 L1020 210 L1090 140", "#6d4aff", packets=3, dur=5))
    b.append(router(460, 210, w=118, label="R1"))
    b.append(router(740, 210, w=118, label="R2"))
    b.append(pill(530, 178, "G1 · .1", "vb", fs=13, h=24) + pill(670, 178, "G1 · .2", "vb", fs=13, h=24))
    # вывод show ip route
    b.append('<rect x="560" y="270" width="380" height="104" rx="14" fill="#1d1450" stroke="#8a63ff" stroke-opacity=".5"/>')
    b.append(txt(578, 296, "R2# show ip route", fs=14, anchor="start", mono=True, color="#ffd76a"))
    b.append(txt(578, 320, "C  192.168.3.0/30  G1", fs=13.5, anchor="start", mono=True, color="#d9d2ff"))
    b.append(txt(578, 342, "C  192.168.2.0/24  G2", fs=13.5, anchor="start", mono=True, color="#d9d2ff"))
    b.append(txt(578, 364, "S  192.168.1.0/24 via 192.168.3.1", fs=13.5, anchor="start", mono=True, color="#6bf0b0"))
    slide("Функции на схеме R1 — R2", sc(
        head("Функции маршрутизатора <em>на схеме</em>",
             "Соединяют сети, находят оптимальные пути и обеспечивают передачу данных между ними."),
        step(card(None, scene("0 0 1200 390", "".join(b)), tone="w", cls="fill")),
        g("g4",
          step(card("Выбор маршрута", "<p>Таблица маршрутизации хранит <b>оптимальные пути</b> "
                    "до сетей назначения.</p>", num="01", tone="vio")),
          step(card("Пересылка пакета", "<p>Маршрутизатор определяет <b>выходной интерфейс</b> "
                    "и следующий узел.</p>", num="02", tone="cya")),
          step(card("Новая инкапсуляция", "<p>Пакет извлекается из входного кадра и помещается "
                    "<b>в новый кадр</b>.</p>", num="03", tone="mag")),
          step(card("Статика и динамика", "<p>Удалённые сети изучаются с помощью "
                    "<b>статических и динамических</b> маршрутов.</p>", num="04", tone="grn")),
          ),
        step(foot("Тип кадра зависит от интерфейса и среды передачи: "
                  "<span class='kv'>Ethernet</span> · <span class='kv'>PPP</span> · "
                  "<span class='kv'>802.11</span>", "")),
    ))
