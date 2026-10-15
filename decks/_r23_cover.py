# -*- coding: utf-8 -*-
"""Титул и слайд «В этой главе» деки «Маршрутизаторы» (2.3)."""

from _r23_lib import (slide, sc, tag, router, switch, pc, server, laptop, globefig,
                      txt, pill, ICON)


def _scene():
    """Живая сцена титула: ESR на стеклянной платформе, вокруг сеть, бегут пакеты."""
    links = [
        ("M470 300 C 560 240 640 170 720 130", "#6d4aff"),   # к Интернету
        ("M470 300 C 380 360 300 400 210 420", "#1fb6e8"),   # к коммутатору
        ("M470 300 C 580 330 660 380 760 420", "#d64ae8"),   # к серверу
        ("M470 300 C 380 240 300 190 200 160", "#6d4aff"),   # к ноутбуку
    ]
    paths = "".join('<path d="%s" stroke="%s" stroke-width="4" fill="none" opacity=".55" '
                    'stroke-linecap="round"/>' % (d, c) for d, c in links)
    dots = []
    for i, (d, c) in enumerate(links):
        for k, rev in ((0, False), (1, True)):
            kp = "1;0" if rev else "0;1"
            dots.append('<circle r="7" fill="%s" filter="url(#sh)"><animateMotion dur="%.1fs" '
                        'begin="%.1fs" repeatCount="indefinite" path="%s" keyPoints="%s" '
                        'keyTimes="0;1" calcMode="linear"/></circle>'
                        % (c, 3.2 + i * .4, k * 1.6 + i * .3, d, kp))
    rings = "".join('<ellipse cx="470" cy="330" rx="%d" ry="%d" fill="none" stroke="#8a63ff" '
                    'stroke-width="1.5" opacity="%.2f"><animate attributeName="opacity" '
                    'values="%.2f;.05;%.2f" dur="4s" begin="%.1fs" repeatCount="indefinite"/></ellipse>'
                    % (rx, ry, op, op, op, b) for (rx, ry, op, b) in
                    [(150, 44, .55, 0), (215, 64, .4, .7), (285, 86, .28, 1.4)])
    return (
        '<svg class="cov-scene" viewBox="0 0 900 560" aria-hidden="true">'
        '<defs><radialGradient id="plat" cx=".5" cy=".4" r=".6">'
        '<stop offset="0" stop-color="#fff" stop-opacity=".95"/>'
        '<stop offset="1" stop-color="#d8d0ff" stop-opacity=".35"/></radialGradient></defs>'
        + rings
        + '<ellipse cx="470" cy="330" rx="130" ry="36" fill="url(#plat)" stroke="#fff" stroke-width="2"/>'
        + paths + "".join(dots)
        + router(470, 290, w=230, label="ESR", sub="маршрутизатор")
        + globefig(745, 115, r=58)
        + txt(745, 200, "Интернет · WAN", fs=17, weight=800)
        + switch(190, 425, w=150, label="Коммутатор", sub="LAN")
        + pc(110, 505, w=62) + pc(270, 505, w=62)
        + server(780, 430, w=78, label="AAA-сервер", sub="RADIUS")
        + laptop(190, 155, w=110, label="SSH-доступ")
        + pill(470, 40, "show ip route", "w", fs=15, mono=True)
        + pill(700, 290, "ping 10.25.8.85", "w", fs=14, mono=True)
        + pill(250, 300, "gi1/0/1.20", "w", fs=14, mono=True)
        + '</svg>'
    )


def build_cover():
    slide("Титул", sc(
        '<div class="cov">'
        '<div class="cov-l">'
        '<p class="kick">Сети и телекоммуникации · Глава 2.3</p>'
        '<h1 class="cov-h">Маршрути&shy;заторы</h1>'
        '<div class="orn" aria-hidden="true"><i></i><b></b><i></i></div>'
        '<p class="cov-sub">Типы интерфейсов ESR, базовая настройка, проверка соединения, '
        'ICMP-диагностика и система AAA</p>'
        '<div class="au"><span>Ананко Софья Михайловна</span><span>Качур Анна Юрьевна</span></div>'
        '</div>'
        '<div class="cov-r">%s</div>'
        '</div>' % _scene()
    ), cover=True)


AGENDA = [
    ("01", "vio", "box", "Интерфейсы ESR", "Три класса интерфейсов",
     "Физические порты, sub- и QinQ-интерфейсы, loopback. Как читается имя "
     "<span class='kv'>gi1/0/1.20.420</span>, скорость и дуплекс.",
     ["gigabitethernet", "loopback", "speed auto"]),
    ("02", "cya", "chart", "Проверка соединения", "Протокол ICMPv4",
     "Команды <span class='kv'>show</span>, утилиты <span class='kv'>ping</span> и "
     "<span class='kv'>traceroute</span>, сообщения ICMP и поле TTL.",
     ["show interfaces", "ping", "traceroute"]),
    ("03", "mag", "shield", "Аутентификация", "Система AAA",
     "Локальная база, RADIUS, TACACS+, LDAP — чем отличаются и когда какой способ применяют.",
     ["AAA", "RADIUS", "TACACS+"]),
    ("04", "grn", "gear", "Базовая настройка", "Базовая настройка ESR",
     "Первое включение, пароль, имя устройства, IP-адресация, SSH, дата и время, баннеры.",
     ["hostname", "ip address", "commit / confirm"]),
    ("05", "amb", "user", "Учётные записи", "Пользователи по умолчанию",
     "Создание пользователей и уровни привилегий 1–15: кому какие команды разрешены.",
     ["username", "privilege 15", "show user accounts"]),
]


def build_agenda():
    rows = []
    for (n, tone, ic, title, go, text, cmds) in AGENDA:
        chips = "".join(tag(c, "w", True) for c in cmds)
        rows.append(
            '<button class="ag-row step %s" data-go="%s">'
            '<span class="ag-n">%s</span>'
            '<span class="ag-ic">%s</span>'
            '<span class="ag-t"><b>%s</b><span>%s</span></span>'
            '<span class="ag-c">%s</span>'
            '<span class="ag-go">→</span>'
            '</button>' % (tone, go, n, ICON[ic], title, text, chips))
    slide("О чём глава", sc(
        '<div class="head"><div><h1 class="t">В этой главе <em>разберём</em></h1>'
        '<p class="sub">Всё — от первого включения «из коробки» до учётных записей и диагностики. '
        'Нажмите на строку, чтобы перейти к разделу.</p></div></div>'
        '<div class="agenda grow">%s</div>'
        '<div class="step foot note"><i>?</i><span>Каждый блок заканчивается тренажёром, '
        'а вся глава — <b>практикумом из пяти задач</b> и <b>тестом из 12 вопросов</b>.</span></div>'
        % "".join(rows)
    ))
