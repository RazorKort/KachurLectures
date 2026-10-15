# -*- coding: utf-8 -*-
"""Блок «Соседство»: семь состояний, DR/BDR, Router ID, show-команды, типы маршрутизаторов, типы сетей."""

from _ospf_lib import (slide, head, sc, step, steps, foot, tag, tags, table, cli,
                       router, arrow, link, pill, txt, ok, ban,
                       blob, rack, cloud_icon, laptop, globe, envelope, legend, bubble, sparkle,
                       rowc, nrow, tile, split, ill, mini, panel, vcard, chain, switch, ICON)

STATES = [
    ("Down", "Hello ещё не получен", "p",
     "Маршрутизатор ещё не получил Hello от этого соседа. Это не значит, что интерфейс выключен — речь о состоянии отношений именно с данным соседом.",
     "Состояние относится к конкретному соседу, а не к интерфейсу целиком."),
    ("Init", "Hello получен", "b",
     "R1 получил Hello от R2 и узнал о его существовании. В Hello — Router ID отправителя и служебные параметры. Видит ли R2 его в ответ — пока неизвестно.",
     "Для OSPFv2 на Ethernet Hello отправляется на групповой адрес 224.0.0.5."),
    ("2-Way", "Маршрутизаторы увидели друг друга", "y",
     "R1 получает Hello от R2, где сам R1 указан в списке соседей. Двусторонняя связь подтверждена: R1 слышит R2, и R2 слышит R1.",
     "В общей Ethernet-сети здесь выбираются DR и BDR. Два DROTHER остаются в 2-Way — это норма."),
    ("ExStart", "Согласование обмена", "p",
     "R1 и R2 договариваются, кто будет ведущим, кто ведомым, и с какого номера последовательности начнётся обмен описаниями баз.",
     "Ведущий — маршрутизатор с большим Router ID. Роль DR сама по себе ведущим не делает."),
    ("Exchange", "Обмен описаниями баз DBD", "b",
     "R1 и R2 обмениваются пакетами DBD — краткими сведениями о записях LSA: тип, идентификаторы, возраст, номер последовательности.",
     "DBD помогает понять, какие записи у соседа новее или отсутствуют. Несовпадение MTU здесь приводит к зависанию."),
    ("Loading", "Запрос недостающих LSA", "y",
     "Запрашиваются недостающие сведения: LSR — запрос, LSU — ответ с объявлениями LSA, LSAck — подтверждение получения.",
     "LSA — это содержимое объявления, а не отдельный тип пакета OSPF."),
    ("Full", "Базы состояний каналов синхронизированы", "p",
     "R1 и R2 получили нужные LSA, синхронизация завершена. Дальше каждый считает кратчайшие пути алгоритмом Дейкстры.",
     "FULL — нормальное рабочее состояние соседства."),
]
TONEFUL = {"p": "pink", "b": "blue", "y": "yellow", "g": "green", "v": "violet"}


def scene(nm, w=300, h=200):
    """Мини-сцена состояния для карточки и для отдельного слайда."""
    W = 104
    a, b = (70, 120), (230, 120)
    base = (router(a[0], a[1], W, "g" if nm == "Down" else "b", label="R1") +
            ("" if nm == "Down" else router(b[0], b[1], W, "p", label="R2")))
    if nm == "Down":
        return mini("0 0 300 200", router(120, 120, 130, "g", label="R1") +
                    '<ellipse cx="230" cy="50" rx="52" ry="34" fill="#fff" stroke="#121212" stroke-width="3"/>' +
                    "".join('<circle cx="%d" cy="50" r="6" fill="#121212"/>' % x for x in (212, 230, 248)))
    if nm == "Init":
        return mini("0 0 300 200", base + '<rect x="100" y="16" width="100" height="44" rx="14" fill="#c7e2fb"/>' +
                    txt(150, 46, "Hello", fs=20, weight=900) + arrow(190, 80, 120, 80, "b", w=5))
    if nm == "2-Way":
        return mini("0 0 300 200", base + arrow(110, 50, 190, 50, "b", w=6) + arrow(190, 76, 110, 76, "p", w=6) +
                    sparkle(140, 20, "#ffd93d", 3))
    if nm == "ExStart":
        return mini("0 0 300 200", base + '<rect x="125" y="6" width="50" height="62" rx="8" fill="#fff" stroke="#121212" stroke-width="3"/>'
                    '<path d="M135 24h30M135 36h30M135 48h20" stroke="#121212" stroke-width="3"/>' +
                    arrow(118, 64, 92, 88, "b", w=5) + arrow(182, 64, 208, 88, "p", w=5))
    if nm == "Exchange":
        return mini("0 0 300 200", base +
                    '<rect x="85" y="8" width="66" height="40" rx="10" fill="#fff" stroke="#121212" stroke-width="3"/>' +
                    txt(118, 35, "DBD", fs=17, weight=900) +
                    '<rect x="152" y="38" width="66" height="40" rx="10" fill="#fff" stroke="#121212" stroke-width="3"/>' +
                    txt(185, 65, "DBD", fs=17, weight=900) +
                    '<path d="M120 100 h60" stroke="#3b9eff" stroke-width="5" marker-end="url(#m_b)" marker-start="url(#m_b)"/>')
    if nm == "Loading":
        return mini("0 0 300 200", base + '<rect x="120" y="6" width="64" height="76" rx="8" fill="#fff" stroke="#121212" stroke-width="3"/>' +
                    txt(152, 38, "LSA", fs=18, weight=900) + '<path d="M132 52h40M132 64h30" stroke="#ff5c9e" stroke-width="4"/>' +
                    arrow(190, 100, 110, 100, "b", w=5))
    return mini("0 0 300 200", base +
                '<ellipse cx="150" cy="22" rx="30" ry="9" fill="#c7e2fb" stroke="#3a72b0" stroke-width="2.6"/>'
                '<path d="M120 22 V64 a30 9 0 0 0 60 0 V22" fill="#e3f0fd" stroke="#3a72b0" stroke-width="2.6"/>'
                '<ellipse cx="150" cy="22" rx="30" ry="9" fill="#c7e2fb" stroke="#3a72b0" stroke-width="2.6"/>' +
                '<path d="M118 92 h64" stroke="#3b9eff" stroke-width="5" marker-end="url(#m_b)" marker-start="url(#m_b)"/>' +
                sparkle(100, 30, "#ffd93d", 2) + sparkle(200, 30, "#ffd93d", 2))


def big_scene(nm):
    """Крупная сцена для слайда отдельного состояния."""
    W = 210
    r1, r2 = (230, 420), (770, 420)
    out = [switch(500, 450, 230, "b"), link(230, 450, 385, 458, 6, "#7d9cc0"), link(615, 458, 770, 450, 6, "#7d9cc0"),
           router(r1[0], r1[1], W, "g" if nm == "Down" else "b", label="R1"),
           router(r2[0], r2[1], W, "p", label="R2"),
           '<rect x="330" y="40" width="340" height="80" rx="22" fill="#e3f0fd" stroke="#8fbff0" stroke-width="2.6"/>' +
           txt(500, 72, "Общий сегмент Ethernet", fs=22, weight=800) + txt(500, 104, "203.0.113.0/24", fs=22, weight=800, color="#1f6fc4"),
           pill(230, 560, "R1 — BDR · 203.0.113.1", "bb", 19, h=40), pill(770, 560, "R2 — DR · 203.0.113.2", "pb", 19, h=40)]
    if nm == "Down":
        out.append(bubble(500, 170, "Hello ещё не получен", "y", 22))
        out.append(ban(500, 380, 30))
    elif nm == "Init":
        out.append('<g class="pstep go-f">' + arrow(690, 300, 320, 300, "p", w=8) + pill(500, 266, "Hello от R2", "p", 20, h=40) + '</g>')
        out.append('<g class="pstep go-f">' + bubble(230, 150, "Кто-то есть!", "b", 20) + '</g>')
    elif nm == "2-Way":
        out.append('<g class="pstep go-f">' + arrow(320, 270, 690, 270, "b", w=8) + pill(500, 240, "Hello: вижу R2", "b", 18, h=38) + '</g>')
        out.append('<g class="pstep go-f">' + arrow(690, 330, 320, 330, "p", w=8) + pill(500, 360, "Hello: вижу R1", "p", 18, h=38) + '</g>')
        out.append('<g class="pstep go-f">' + ok(500, 330, 26) + '</g>')
    elif nm == "ExStart":
        out.append('<g class="pstep go-f">' + arrow(320, 270, 690, 270, "y", w=8) + pill(500, 240, "DBD пустой, seq = X", "y", 18, h=38) + '</g>')
        out.append('<g class="pstep go-f">' + arrow(690, 330, 320, 330, "y", w=8) + pill(500, 360, "DBD пустой, seq = Y", "y", 18, h=38) + '</g>')
        out.append('<g class="pstep go-f">' + bubble(770, 150, "У меня ID больше —|я ведущий", "p", 18) + '</g>')
    elif nm == "Exchange":
        out.append('<g class="pstep go-f">' + arrow(320, 270, 690, 270, "v", w=8) + pill(500, 240, "DBD: опись моей LSDB", "v", 18, h=38) + '</g>')
        out.append('<g class="pstep go-f">' + arrow(690, 330, 320, 330, "v", w=8) + pill(500, 360, "DBD: опись, seq = Y + 1", "v", 18, h=38) + '</g>')
    elif nm == "Loading":
        out.append('<g class="pstep go-f">' + arrow(320, 250, 690, 250, "p", w=7) + pill(500, 222, "LSR — пришли эти LSA", "p", 17, h=36) + '</g>')
        out.append('<g class="pstep go-f">' + arrow(690, 300, 320, 300, "g", w=7) + pill(500, 300, "LSU с объявлениями LSA", "g", 17, h=36) + '</g>')
        out.append('<g class="pstep go-f">' + arrow(320, 350, 690, 350, "b", w=7) + pill(500, 376, "LSAck — получил", "b", 17, h=36) + '</g>')
    else:
        out.append('<path d="M320 330 H690" stroke="#3fc47c" stroke-width="12" stroke-linecap="round"/>')
        out.append('<g class="pstep go-f">' + pill(500, 266, "LSDB R1 = LSDB R2", "g", 22, h=44) +
                   sparkle(380, 230, "#ffd93d") + sparkle(600, 230, "#ffd93d") + '</g>')
    return ill("0 0 1000 620", "".join(out))


def build():
    # ------------------------------------------------------------ обзор состояний (как r09)
    top = (cloud_icon(120, 70, .9) + cloud_icon(880, 90, .8) + switch(500, 150, 230, "b") +
           link(250, 165, 385, 165, 6, "#7d9cc0") + link(615, 165, 750, 165, 6, "#7d9cc0") +
           router(230, 140, 190, "b", label="R1") + router(770, 140, 190, "p", label="R2") +
           '<path d="M745 30 l14 22 l14 -16 l14 16 l14 -22 v30 h-56 z" fill="#ffd93d"/>' +
           pill(330, 50, "Hello →", "bb", 20, h=40) + pill(670, 50, "← Hello", "pb", 20, h=40) +
           pill(230, 250, "R1 — BDR · 203.0.113.1/24", "bb", 17, h=36) + pill(770, 250, "R2 — DR · 203.0.113.2/24", "pb", 17, h=36))
    slide("Состояния соседства", sc(
        head("Состояния соседства OSPF", "От обнаружения маршрутизатора до синхронизации баз данных. Общий сегмент Ethernet 203.0.113.0/24."),
        '<div style="flex:0 0 26%;display:flex;min-height:0">' + ill("0 0 1000 280", top) + '</div>' +
        '<div class="row7 fill">' +
        "".join(vcard(str(i + 1), nm, scene(nm), short, t, cls="nbrc go-f")
                for i, (nm, short, t, _, _) in enumerate(STATES)) + '</div>',
        step(foot("На соединении «точка-точка» выбор DR/BDR не требуется. У каждого маршрутизатора своё состояние "
                  "отношений с соседом — R1 и R2 могут переходить между состояниями не строго одновременно."))
    ), scen="nbr")

    # ------------------------------------------------------------ по слайду на состояние
    for i, (nm, short, t, long_, note) in enumerate(STATES):
        prev = STATES[i - 1][0] if i else "—"
        nxt = STATES[i + 1][0] if i < 6 else "—"
        slide("Состояние %s" % nm, sc(
            head("%d. %s — %s" % (i + 1, nm, short.lower()), "Состояние %d из 7 · до него: %s · после него: %s" % (i + 1, prev, nxt)),
            split(big_scene(nm),
                  steps(rowc("eye", "Что происходит", long_, t),
                        rowc("bulb", "Обратите внимание", note, "y"),
                        chain([(s[0], "y" if s[0] == nm else ("g" if k < i else "")) for k, s in enumerate(STATES)])),
                  "56fr 44fr")
        ), scen="pkt")

    # ------------------------------------------------------------ обмен DBD по шагам
    slide("Обмен DBD", sc(
        head("Как идёт обмен DBD", "Разбор по шагам: Router ID R2 больше, поэтому R2 — ведущий."),
        split(panel("doc", "Последовательность",
                    table(["Шаг", "Кто", "Что отправляет", "Результат"],
                          [[("1", "c"), "R1 → R2", "DBD пустой, seq = X", "начало согласования"],
                           [("2", "c"), "R2 → R1", "DBD пустой, seq = Y", "сравнение Router ID"],
                           [("3", "c"), "—", "ID R2 больше", "R2 ведущий, R1 ведомый"],
                           [("4", "c"), "R1 → R2", "DBD с описью LSDB, seq = Y", "R1 — Exchange"],
                           [("5", "c"), "R2 → R1", "DBD с описью LSDB, seq = Y + 1", "R2 — Exchange"],
                           [("6", "c"), "R1 → R2", "подтверждение тем же seq", "ведомый подтверждает каждый DBD"],
                           (["7", "R1", "последний DBD отправлен", "R1 — Loading"], "hi")]), "y"),
              steps(rowc("star", "Ведущий / ведомый", "Определяются <b>сравнением Router ID</b>: больший ID — выше приоритет.", "p"),
                    rowc("sum", "Номер последовательности", "Ведомый берёт номер ведущего, дальше +1 с каждым пакетом.", "b"),
                    rowc("ok", "Подтверждения", "Ведомый подтверждает каждый DBD ведущего пакетом с тем же номером.", "g")),
              "60fr 40fr")
    ))

    # ------------------------------------------------------------ зачем DR
    nodes = [(150, 150), (420, 110), (150, 420), (420, 460), (285, 285)]
    full = "".join(link(*(p + q), w=3, color="#ff8fbc") for i, p in enumerate(nodes) for q in nodes[i + 1:])
    full += "".join(router(x, y - 14, 90, "p") for x, y in nodes)
    hubn = [(610, 150), (880, 150), (610, 420), (880, 420)]
    hub = "".join(link(x, y, 745, 285, 4, "#8fbff0") for x, y in hubn)
    hub += "".join(router(x, y - 14, 90, "b") for x, y in hubn) + router(745, 270, 120, "y", label="DR")
    slide("Зачем DR и BDR", sc(
        head("Зачем нужны DR и BDR", "На общей сети число пар растёт квадратично — и каждая пара означала бы полное соседство."),
        split(ill("0 0 1000 560", blob(285, 290, 250, 250, "p", "Без DR: каждый с каждым", seed=.4, lab_y=40, fs=19) +
                  blob(745, 290, 230, 250, "b", "С DR: все только с DR", seed=2, lab_y=40, fs=19) + full + hub),
              steps(rowc("sum", "Арифметика", "<b>n × (n − 1) ÷ 2</b> пар. 20 маршрутизаторов — <b>190</b> смежностей, 50 — уже <b>1225</b>.", "p"),
                    rowc("star", "DR — точка сбора", "Назначенный маршрутизатор собирает и распространяет LSA для всего сегмента.", "y"),
                    rowc("shield", "BDR — запасной", "Кандидат с лучшими значениями после DR, наблюдает и готов заменить его.", "b"),
                    rowc("net", "DROTHER — остальные", "Полная смежность только с DR и BDR, между собой — 2-Way.", "g")),
              "56fr 44fr")
    ))

    # ------------------------------------------------------------ адреса DR
    art = (switch(500, 330, 260, "b") +
           "".join(link(x, y + 30, 500, 340, 5, "#7d9cc0") for x, y in ((150, 140), (500, 120), (850, 140), (150, 520), (850, 520))) +
           router(150, 140, 150, "p", label="DROTHER") + router(500, 120, 160, "y", label="DR") +
           router(850, 140, 150, "b", label="BDR") + router(150, 520, 150, "p", label="DROTHER") + router(850, 520, 150, "p", label="DROTHER") +
           '<g class="pstep go-f">' + arrow(220, 120, 410, 110, "p", w=7) + pill(310, 70, "LSA → 224.0.0.6", "p", 18, h=38) + '</g>' +
           '<g class="pstep go-f">' + arrow(560, 190, 790, 500, "y", w=7) + arrow(440, 190, 210, 500, "y", w=7) +
           pill(500, 250, "DR → 224.0.0.5 всем", "y", 18, h=38) + '</g>' +
           '<g class="pstep go-f">' + bubble(850, 20, "BDR слушает|и ждёт", "b", 17) + '</g>')
    slide("Адреса DR/BDR", sc(
        head("Как идут объявления через DR", "Два групповых адреса делят работу между ролями."),
        split(ill("0 0 1000 620", art),
              steps(rowc("up", "224.0.0.6 — все DR", "DROTHER отправляют свои LSA <b>только</b> DR и BDR.", "p"),
                    rowc("down", "224.0.0.5 — все OSPF", "DR пересылает объявления всем остальным маршрутизаторам.", "y"),
                    rowc("eye", "BDR наблюдает", "Слушает объявления, но не пересылает. Если DR перестал слать Hello — BDR становится DR.", "b"),
                    rowc("ok", "Подтверждение", "DROTHER подтверждают обновление обратно DR пакетом LSAck.", "g")),
              "56fr 44fr")
    ), scen="pkt")

    # ------------------------------------------------------------ выбор DR
    art = ("".join(router(x, 200, 150, t, label=n) + pill(x, 330, "приоритет %s" % p, "w", 17, h=36) +
                   pill(x, 378, "ID %s" % i, "w", 16, h=34, mono=True)
                   for x, n, t, p, i in ((150, "R1", "b", "128", "1.1.1.1"), (400, "R2", "y", "200", "2.2.2.2"),
                                         (650, "R3", "p", "128", "3.3.3.3"), (880, "R4", "g", "0", "4.4.4.4"))) +
           '<g class="dstep go-f">' + pill(400, 90, "DR — наибольший приоритет", "y", 18, h=40) + '</g>' +
           '<g class="dstep go-f">' + pill(650, 90, "BDR — приоритет равен, ID больше", "p", 16, h=40) + '</g>' +
           '<g class="dstep go-f">' + ban(880, 470, 26) + txt(880, 525, "0 — не участвует", fs=18, weight=800) + '</g>' +
           '<g class="dstep go-f">' + txt(150, 470, "DROTHER", fs=22, weight=800, color="#1f6fc4") + '</g>')
    slide("Выбор DR и BDR", sc(
        head("Выбор DR и BDR", "Два критерия — строго по очереди: сначала приоритет, потом Router ID."),
        split(ill("0 0 1000 560", art),
              steps(rowc("star", "1. Приоритет интерфейса", "Наибольший — DR, следующий — BDR. Диапазон <b>0–255</b>, по умолчанию <b>128</b>.", "y"),
                    rowc("key", "2. Router ID", "Если приоритеты равны — DR становится маршрутизатор с наибольшим Router ID.", "p"),
                    rowc("lock", "Без перевыборов", "Новый маршрутизатор с лучшими значениями роль <b>не отнимает</b>. Перевыбор — только при сбое DR.", "b"),
                    rowc("swap", "Сбой DR", "BDR становится DR, среди DROTHER выбирается новый BDR.", "g")),
              "56fr 44fr")
    ), scen="drbdr")

    # ------------------------------------------------------------ Router ID
    art = (router(500, 260, 260, "p", label="R1") +
           '<g class="dstep go-f">' + pill(500, 70, "1. router-id 1.1.1.1 — задан вручную", "g", 20, h=44) + '</g>' +
           '<g class="dstep go-f">' + pill(500, 130, "2. наибольший адрес Loopback", "b", 20, h=44) + '</g>' +
           '<g class="dstep go-f">' + pill(500, 450, "3. наибольший активный IPv4 интерфейса", "y", 20, h=44) + '</g>' +
           bubble(800, 300, "Loopback|не падает!", "p", 18))
    slide("Router ID", sc(
        head("Идентификатор маршрутизатора — Router ID", "Уникальное имя маршрутизатора в области OSPF, записывается как IPv4-адрес."),
        split(ill("0 0 1000 540", art),
              steps(rowc("key", "Вручную — лучше всего", "Команда <b>router-id</b>. Обычно задают адрес отдельного Loopback-интерфейса.", "g"),
                    rowc("net", "Любой Loopback", "Если не задан — наибольший адрес Loopback, даже не участвующего в OSPF.", "b"),
                    rowc("globe", "Активный интерфейс", "Если Loopback нет — наибольший активный IPv4-адрес.", "y"),
                    rowc("stop", "Ограничения", "Дубль Router ID у соседей — ошибка. Сменить ID можно только перезагрузкой или удалением процесса.", "p")),
              "52fr 48fr")
    ), scen="drbdr")

    # ------------------------------------------------------------ show ip ospf interface
    slide("show ip ospf interface", sc(
        head("Проверка ролей: show ip ospf interface", "Кто на интерфейсе DR, кто BDR, сколько соседей."),
        '<div class="row2 fill">' + steps(
            panel("pc", "Вывод на R1", cli(["Interface gi1/0/1, Area 0.0.0.0",
                                             ("", "Router ID 1.1.1.1, Network Type BROADCAST, Cost 10"),
                                             ("", "State DR, Priority 128"),
                                             ("", "Designated Router 1.1.1.1, address 172.16.10.1"),
                                             ("", "Backup DR 2.2.2.2, address 172.16.10.100"),
                                             ("", "Neighbor Count 1, Adjacent neighbor count 1")]) +
                  rowc("ok", "Разбор", "R1 — <b>DR</b> с приоритетом 128. Одна смежность — с R2 (2.2.2.2), который BDR.", "p"), "p"),
            panel("pc", "Вывод на R2", cli(["Interface gi1/0/1, Area 0.0.0.0",
                                             ("", "Router ID 2.2.2.2, Network Type BROADCAST, Cost 10"),
                                             ("", "State BDR, Priority 128"),
                                             ("", "Designated Router 1.1.1.1, address 172.16.10.1"),
                                             ("", "Backup DR 2.2.2.2, address 172.16.10.100"),
                                             ("", "Neighbor Count 1, Adjacent neighbor count 1")]) +
                  rowc("ok", "Разбор", "R2 — <b>BDR</b>. Видит того же DR. Одна смежность — с R1.", "b"), "b")) + '</div>',
        step(foot("DR здесь R1, хотя у R2 Router ID больше: R1 поднялся первым, а роли без сбоя не перевыбираются.", "note"))
    ))

    # ------------------------------------------------------------ show ip ospf neighbor
    slide("show ip ospf neighbor", sc(
        head("Проверка смежности: show ip ospf neighbor", "Состояние соседа записывается как «состояние / роль»."),
        split(panel("doc", "Как читать",
                    table(["Что видно", "Что это значит"],
                          [[("FULL/DR", "mono"), "Полная смежность с соседом, который DR"],
                           [("FULL/BDR", "mono"), "Полная смежность с соседом, который BDR"],
                           [("FULL/DROTHER", "mono"), "DR или BDR полностью смежен с DROTHER"],
                           [("2-WAY/DROTHER", "mono"), "Два DROTHER — обмен только Hello. Норма"],
                           [("EXSTART/EXCHANGE", "mono"), "Застряли на DBD — чаще всего MTU"],
                           [("INIT", "mono"), "Hello в одну сторону — фильтр, маска, Area ID"]]), "b"),
              steps(rowc("ok", "FULL — норма", "Любое другое <b>конечное</b> состояние — проблема со смежностью.", "g"),
                    rowc("bulb", "2-WAY — тоже норма", "На broadcast-сети DROTHER между собой остаются в 2-WAY и знают друг о друге.", "y"),
                    rowc("stop", "Остальное — разбирать", "EXSTART, EXCHANGE, INIT, LOADING надолго — ищите причину.", "p")),
              "58fr 42fr")
    ))

    # ------------------------------------------------------------ типы маршрутизаторов (как r02)
    Wt = 92
    pos = {"ir1": (90, 330), "ir2": (250, 300), "abr1": (390, 330), "br1": (560, 230), "br2": (560, 430),
           "abr2": (730, 330), "ir3": (880, 250), "ir4": (880, 430), "asbr": (1050, 330)}
    links = [("ir1", "ir2"), ("ir2", "abr1"), ("abr1", "br1"), ("abr1", "br2"), ("abr1", "abr2"), ("br1", "abr2"),
             ("br2", "abr2"), ("abr2", "ir3"), ("abr2", "ir4"), ("ir3", "asbr"), ("ir4", "asbr")]
    roles = {"ir1": ("b", "IR"), "ir2": ("b", "IR"), "abr1": ("p", "ABR"), "br1": ("y", "BR"), "br2": ("y", "BR"),
             "abr2": ("p", "ABR"), "ir3": ("b", "IR"), "ir4": ("b", "IR"), "asbr": ("gr", "ASBR")}
    art = (blob(190, 340, 180, 170, "b", "AREA 0.0.0.1", seed=.2, lab_y=520, fs=19) +
           blob(560, 340, 200, 210, "y", "AREA 0.0.0.0", seed=1.1, lab_y=560, fs=19) +
           blob(900, 340, 200, 180, "g", "AREA 0.0.0.5", seed=2.2, lab_y=540, fs=19) +
           blob(1180, 330, 100, 90, "v", None, seed=3) + globe(1180, 300, 28, "#6b4fd0") +
           txt(1180, 360, "внешняя сеть", fs=15, weight=800) +
           "".join(link(pos[a][0], pos[a][1] + 13, pos[b][0], pos[b][1] + 13, 4, "#121212") for a, b in links) +
           link(1050, 343, 1110, 330, 4, "#121212") +
           "".join('<g class="role go-f" data-keep="">%s</g>' % "" for _ in range(0)) +
           "".join(router(x, y, Wt, roles[k][0]) + pill(x, y + 62, roles[k][1], {"b": "bb", "p": "pb", "y": "yb", "gr": "gb"}[roles[k][0]], 15, h=30)
                   for k, (x, y) in pos.items()))
    slide("Типы маршрутизаторов", sc(
        head("Типы маршрутизаторов OSPF", "Четыре роли в маршрутизации между областями."),
        '<div class="row4" style="flex:none">' +
        "".join('<div class="role go-f">%s</div>' % rowc("net", t, d, tone) for t, d, tone in [
            ("IR — внутренний", "Все интерфейсы в одной области. Одна LSDB.", "b"),
            ("BR — магистральный", "Хотя бы один интерфейс в области 0.0.0.0; не обязательно ABR.", "y"),
            ("ABR — пограничный", "Соединяет области с Area 0; своя LSDB на каждую область.", "p"),
            ("ASBR — граница АС", "Обменивается маршрутами с другими АС и протоколами; может быть где угодно.", "g")]) + '</div>' +
        '<div class="fill" style="display:flex">' + ill("0 130 1290 480", art) + '</div>',
        step(foot("<b>Роли могут сочетаться:</b> внутренний маршрутизатор области 0 одновременно является BR; "
                  "ASBR может быть также IR, BR или ABR.", "note"))
    ), scen="roles")

    # ------------------------------------------------------------ ABR и ASBR
    slide("ABR и ASBR", sc(
        head("ABR и ASBR — не путать", "Обе роли пограничные, но границы у них разные."),
        '<div class="row2 fill">' + steps(
            panel("swap", "ABR — граница между областями",
                  ill("0 0 600 260", blob(150, 130, 130, 100, "p", "Area 1", seed=.3, lab_y=50) +
                      blob(450, 130, 130, 100, "b", "Area 0", seed=1.2, lab_y=50) + router(300, 120, 130, "y", label="ABR")) +
                  rowc("db", "Своя LSDB на каждую область", "Подключён минимум к двум областям, одна из них — Area 0.", "p") +
                  rowc("doc", "Создаёт LSA-3 и LSA-4", "Передаёт сводку о сетях и путь к ASBR, а не топологию.", "p"), "p"),
            panel("globe", "ASBR — граница автономной системы",
                  ill("0 0 600 260", blob(200, 130, 170, 100, "g", "OSPF", seed=.9, lab_y=50) + router(320, 120, 130, "gr", label="ASBR") +
                      globe(510, 120, 50, "#6b4fd0") + txt(510, 205, "BGP · IS-IS · статика", fs=18, weight=800)) +
                  rowc("globe", "Создаёт LSA-5", "Для каждого внешнего префикса. В NSSA — LSA-7.", "g") +
                  rowc("star", "Флаг E в LSA-1", "Сам ASBR сообщает, что он ASBR. LSA-4 о пути к нему создаёт ABR.", "g"), "g")) + '</div>'
    ))

    # ------------------------------------------------------------ типы сетей
    def p2p():
        return mini("0 0 300 150", router(70, 70, 100, "b") + router(230, 70, 100, "p") + link(110, 84, 190, 84, 6, "#121212"))

    def bma():
        return mini("0 0 300 150", switch(150, 110, 140, "b") + "".join(link(x, 74, 150, 112, 3, "#7d9cc0") for x in (50, 150, 250)) +
                    "".join(router(x, 60, 76, "p") for x in (50, 150, 250)))

    def nbma():
        return mini("0 0 300 150", cloud_icon(150, 110, 1.2, "#efe9fb", "#b9a4f2") +
                    "".join(router(x, 40, 70, "b") for x in (50, 150, 250)))

    def p2mp():
        return mini("0 0 300 150", router(150, 40, 86, "y") + "".join(link(150, 52, x, 122, 3, "#121212") for x in (50, 150, 250)) +
                    "".join(router(x, 110, 66, "p") for x in (50, 150, 250)))

    slide("Типы сетей OSPF", sc(
        head("Типы сетей OSPF", "Настройка интерфейса, от которой зависят обнаружение соседей и выбор DR/BDR."),
        '<div class="row4 fill">' + steps(
            vcard("1", "Point-to-Point", p2p(), "Два маршрутизатора, один логический канал. DR/BDR <b>не нужны</b>.", "b", "точка-точка"),
            vcard("2", "Broadcast", bma(), "Несколько маршрутизаторов в Ethernet через коммутатор. DR и BDR <b>выбираются</b>.", "p", "множественный доступ"),
            vcard("3", "NBMA", nbma(), "Общая среда без широковещания (Frame Relay). DR/BDR выбираются, Hello адресно.", "v", "без broadcast"),
            vcard("4", "Point-to-Multipoint", p2mp(), "Hub-and-spoke: набор отдельных каналов. DR/BDR <b>не нужны</b>.", "y", "точка-многоточка")) + '</div>',
        step(foot("Тип сети — настройка OSPF-интерфейса. Она связана с физикой, но не обязана совпадать: "
                  "Ethernet можно настроить как point-to-point, если на нём только два маршрутизатора.", "note"))
    ))

    NETS = [
        ("Point-to-Point", "точка-точка", "b", p2p,
         [("stop", "DR и BDR не выбираются", "Нет общей среды с несколькими участниками.", "p"),
          ("swap", "Hello напрямую", "Соседство между двумя маршрутизаторами, обнаружение автоматическое.", "b"),
          ("net", "Где применяется", "Выделенная WAN-линия. Или Ethernet, если на нём ровно два маршрутизатора.", "g"),
          ("clock", "Таймеры", "Hello 10 с / Dead 40 с — типичные значения.", "y")]),
        ("Broadcast Multi-Access", "широковещательная сеть", "p", bma,
         [("star", "Выбираются DR и BDR", "DR координирует обмен, BDR готов заменить при сбое.", "y"),
          ("net", "Обнаружение автоматически", "Через multicast 224.0.0.5 / 224.0.0.6.", "b"),
          ("ok", "Полное соседство — с DR и BDR", "Остальные между собой остаются в 2-Way.", "g"),
          ("clock", "Таймеры", "Hello 10 с / Dead 40 с. На многих Ethernet-интерфейсах этот тип по умолчанию.", "p")]),
        ("NBMA", "Non-Broadcast Multi-Access", "v", nbma,
         [("star", "DR и BDR обычно выбираются", "И должны иметь связность со всеми участниками.", "y"),
          ("arr", "Hello адресно — unicast", "Широковещания и multicast в среде нет.", "p"),
          ("gear", "Соседей задают вручную", "В классическом режиме NBMA — явная настройка.", "v"),
          ("clock", "Таймеры", "Hello 30 с / Dead 120 с — классические значения режима NBMA.", "b")]),
        ("Point-to-Multipoint", "точка-многоточка", "y", p2mp,
         [("stop", "DR и BDR не выбираются", "OSPF видит сеть как набор отдельных каналов «точка-точка».", "p"),
          ("net", "Отдельное соседство", "Центр устанавливает соседство с каждым филиалом.", "y"),
          ("gear", "Без multicast", "Вариант Non-Broadcast: Hello адресно, соседей задают вручную.", "v"),
          ("route", "Где удобно", "Hub-and-spoke, когда филиалы не соединены друг с другом напрямую.", "g")]),
    ]
    for nm, sub, t, art, rows in NETS:
        slide(nm, sc(
            head(nm, sub.capitalize() + "."),
            split('<div class="ill" style="padding:20px">' + art().replace('class="mini"', 'class="mini" style="width:100%;height:100%"') + '</div>',
                  steps(*[rowc(i, a, b, c) for i, a, b, c in rows]), "50fr 50fr")
        ))

    slide("Сети: сравнение", sc(
        head("Сравнение типов сетей", "Одна таблица, по которой выбирают режим интерфейса."),
        panel("doc", "Сводная таблица",
              table(["Тип сети", "DR/BDR", "Обнаружение соседей", "Hello / Dead", "Где применяется"],
                    [["Point-to-Point", ("нет", "c"), "автоматически", ("10 / 40 с", "mono"), "выделенный канал между двумя маршрутизаторами"],
                     ["Broadcast", ("да", "c"), "автоматически, multicast", ("10 / 40 с", "mono"), "Ethernet-сегмент"],
                     ["NBMA", ("да", "c"), "часто вручную, unicast", ("30 / 120 с", "mono"), "Frame Relay и подобные"],
                     ["Point-to-Multipoint", ("нет", "c"), "автоматически при multicast", ("30 / 120 с", "mono"), "hub-and-spoke"],
                     ["P2MP Non-Broadcast", ("нет", "c"), "вручную, unicast", ("30 / 120 с", "mono"), "hub-and-spoke без multicast"]]), "b"),
        step(foot("Правило таймеров: Dead обычно равен четырём Hello. Значения у соседей обязаны совпадать.", "ok"))
    ))
