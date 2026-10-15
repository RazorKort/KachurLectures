# -*- coding: utf-8 -*-
"""Блок «Как работает OSPF»: шесть этапов, базы данных, пакеты, форматы, коды маршрутов."""

from _ospf_lib import (slide, head, sc, step, steps, foot, tag, tags, table, cli,
                       router, arrow, link, pill, txt, ok, ban, circ_num,
                       blob, rack, cloud_icon, laptop, globe, envelope, legend, bubble, sparkle,
                       rowc, nrow, tile, split, ill, mini, panel, vcard, chain, switch, ICON)

PAL = ["#ffd3e4", "#c7e2fb", "#ffe9a8", "#c6efd6", "#ddd2fa"]


def rc(p, w):
    return p[0], p[1] + w * 0.14


def ln(a, b, w, col="#7d9cc0", sw=5, dash=None, cls=""):
    (x1, y1), (x2, y2) = rc(a, w), rc(b, w)
    return link(x1, y1, x2, y2, sw, col, cls, dash)


def bitdiag(rows, w=960, rh=62, title="0                                       15 16                                      31"):
    """Диаграмма полей по 32 бита в строке, как в RFC. rows = [[(name, bits), ...], ...]."""
    out = [txt(20, 22, "0", fs=15, anchor="start", color="#56606b"),
           txt(20 + w / 2 - 6, 22, "15", fs=15, anchor="end", color="#56606b"),
           txt(20 + w / 2 + 6, 22, "16", fs=15, anchor="start", color="#56606b"),
           txt(20 + w, 22, "31", fs=15, anchor="end", color="#56606b")]
    k = 0
    for r, row in enumerate(rows):
        x = 20.0
        for name, bits in row:
            ww = w * bits / 32.0
            y = 34 + r * rh
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="%d" rx="10" fill="%s" stroke="#fff" stroke-width="4"/>'
                       % (x, y, ww, rh, PAL[k % len(PAL)]))
            out.append(txt(x + ww / 2, y + rh / 2 + 7, name, fs=19 if ww > 200 else 16, weight=800))
            x += ww
            k += 1
    return "".join(out), 34 + len(rows) * rh + 10


def stage(label, num, title, sub, art, rows, tone="p"):
    slide(label, sc(
        head(title, sub),
        split(steps(*rows), art, "44fr 56fr")
    ))


def build():
    W = 120
    # ------------------------------------------------------------ этап 1
    nets = [((140, 110), "192.168.1.0/24", "gi1/0/1"), ((760, 110), "203.0.113.0/30", "gi1/0/2"),
            ((140, 500), "203.0.113.12/30", "gi1/0/3"), ((760, 500), "203.0.113.16/30", "gi1/0/4")]
    art = ("".join(link(450, 320, x, y, 5, "#7d9cc0") for (x, y), _, _ in nets) +
           "".join('<g><rect x="%d" y="%d" width="250" height="96" rx="22" fill="#e3f0fd" stroke="#8fbff0" '
                   'stroke-width="2.6" stroke-dasharray="9 7"/>%s%s</g>'
                   % (x - 125, y - 48, txt(x, y - 6, n, fs=22, weight=800), txt(x, y + 26, i, fs=18, color="#1f6fc4"))
                   for (x, y), n, i in nets) +
           router(450, 290, 190, "p", label="R1") + bubble(450, 140, "Это мои сети!", "p", 18))
    stage("Этап 1: сбор данных", 1, "Этап 1. Сбор данных", "Маршрутизатор начинает с того, что знает сам: свои каналы и напрямую подключённые сети.",
          ill("0 0 900 620", art),
          [nrow("1", "IP-адрес с префиксом", mini("0 0 80 64", txt(40, 40, "/24", fs=22, weight=900)),
                "На интерфейсе настроен IPv4-адрес с маской.", "p"),
           nrow("2", "Интерфейс в состоянии up", mini("0 0 80 64", '<circle cx="40" cy="32" r="20" fill="#3fc47c"/>'),
                "Канал должен работать — по лежащему интерфейсу данных нет.", "b"),
           nrow("3", "Межсетевой экран", mini("0 0 80 64", '<path d="M40 8 l22 9 v14 c0 14 -10 22 -22 26 c-12 -4 -22 -12 -22 -26 v-14 z" '
                                                              'fill="#ffe9a8" stroke="#121212" stroke-width="3"/>'),
                "Отключён или настроен: <b>ip firewall disable</b> либо правила для OSPF.", "y"),
           rowc("doc", "Результат",
                "R1 связан с четырьмя сетями — все они уже записи в таблице маршрутизации, ещё до работы любого протокола.", "g")])

    # ------------------------------------------------------------ этап 2
    nb = {"R2": (150, 140), "R4": (750, 140), "R5": (750, 500)}
    art = (link(450, 340, 150, 520, 5, "#c7d6e4", dash="10 8") +
           "".join(link(450, 340, x, y + 17, 5, "#7d9cc0") for x, y in nb.values()) +
           router(450, 310, 170, "p", label="R1") +
           "".join(router(x, y, 140, "b", label=n) for n, (x, y) in nb.items()) +
           '<g class="pstep go-f">' + arrow(370, 290, 230, 190, "p", w=6) + pill(270, 260, "Hello", "p", 18) +
           arrow(530, 290, 670, 190, "p", w=6) + pill(630, 260, "Hello", "p", 18) +
           arrow(530, 370, 670, 470, "p", w=6) + pill(630, 400, "Hello", "p", 18) + '</g>' +
           '<g class="pstep go-f">' + arrow(200, 205, 360, 320, "b", w=6) + arrow(700, 205, 540, 320, "b", w=6) +
           arrow(700, 470, 540, 390, "b", w=6) + '</g>' +
           '<g class="pstep go-f">' + ban(300, 432, 22) + '<rect x="40" y="520" width="230" height="70" rx="18" fill="#fde7f0"/>' +
           txt(155, 550, "gi1/0/1", fs=20, weight=800) + txt(155, 576, "соседей нет", fs=17, color="#d8276f") + '</g>')
    slide("Этап 2: соседи", sc(
        head("Этап 2. Обнаружение соседей", "Hello-пакеты находят соседей на каждом канале и дальше работают как keepalive."),
        split(steps(
            rowc("hello", "Пакет Hello",
                 "Отправляется периодически со всех интерфейсов с OSPF. На Ethernet — на групповой адрес <b>224.0.0.5</b>.", "p"),
            rowc("eye", "Кто сосед",
                 "Любой маршрутизатор с тем же протоколом и версией, ответивший своим Hello. R2, R4 и R5 откликнулись.", "b"),
            rowc("stop", "Нет ответа — нет соседа",
                 "За gi1/0/1 Hello не пришли — дальше по этому интерфейсу процесс не идёт.", "y"),
            rowc("clock", "Keepalive",
                 "Hello продолжают ходить постоянно. Перестали — сосед недоступен, смежность разрывается, его сети удаляются из таблицы.", "g")),
            ill("0 0 900 620", art), "44fr 56fr")
    ), scen="pkt")

    # ------------------------------------------------------------ этап 3
    doc = ('<rect x="470" y="70" width="400" height="480" rx="26" fill="#fff" stroke="#121212" stroke-width="3"/>'
           '<rect x="470" y="70" width="400" height="80" rx="26" fill="#ffe9a8"/>' +
           txt(670, 122, "LSP от R1", fs=30, weight=900) +
           "".join('<rect x="495" y="%d" width="350" height="78" rx="16" fill="%s"/>%s%s'
                   % (170 + i * 92, c, txt(515, 200 + i * 92, k, fs=17, color="#56606b", anchor="start", weight=700),
                      txt(515, 230 + i * 92, v, fs=22, anchor="start", weight=900))
                   for i, (k, v, c) in enumerate([("Сосед (Router ID)", "R2 · 2.2.2.2", "#e3f0fd"),
                                                  ("Стоимость канала", "cost = 10", "#fef6dc"),
                                                  ("Сеть и маска", "203.0.113.0/30", "#e6f7ec"),
                                                  ("Номер последовательности", "0x80000001", "#fde7f0")])))
    art = router(220, 300, 200, "p", label="R1") + arrow(330, 300, 455, 300, "p", w=7) + doc + sparkle(400, 60)
    stage("Этап 3: LSP", 3, "Этап 3. Создание пакета состояния канала", "LSP (Link State Packet) описывает каждый напрямую подключённый канал.",
          ill("0 0 900 620", art),
          [rowc("doc", "Что внутри", "Для каждого канала: <b>сосед</b>, <b>стоимость</b>, <b>сеть</b> с маской, тип канала.", "p"),
           rowc("clock", "Служебные поля", "<b>Номер последовательности</b> и <b>возраст</b> — чтобы отличить свежий LSP от уже известного.", "b"),
           rowc("db", "В OSPF это LSA", "Роль «кирпичиков» карты играют объявления <b>LSA</b>; их переносят пакеты <b>LSU</b>.", "y")])

    # ------------------------------------------------------------ этап 4
    fl = {"R1": (130, 320), "R2": (450, 140), "R3": (450, 500), "R4": (770, 320)}
    art = (blob(450, 320, 420, 270, "p", "Область OSPF", seed=.7, lab_y=40, fs=20) +
           ln(fl["R1"], fl["R2"], W) + ln(fl["R1"], fl["R3"], W) + ln(fl["R2"], fl["R4"], W) +
           ln(fl["R3"], fl["R4"], W) + ln(fl["R2"], fl["R3"], W) +
           "".join(router(x, y, W, "p" if n == "R1" else "b", label=n) for n, (x, y) in fl.items()) +
           '<g class="lstep go-f">' + arrow(190, 300, 380, 180, "y", w=7) + envelope(280, 225, 44, "y") + '</g>' +
           '<g class="lstep go-f">' + arrow(190, 360, 380, 480, "y", w=7) + envelope(280, 430, 44, "y") + '</g>' +
           '<g class="lstep go-f">' + arrow(520, 180, 710, 300, "y", w=7) + arrow(450, 220, 450, 440, "y", w=7) +
           envelope(615, 225, 44, "y") + '</g>' +
           '<g class="lstep go-f">' + arrow(520, 480, 710, 360, "y", w=7) + envelope(615, 430, 44, "y") + '</g>' +
           '<g class="lstep go-f">' + bubble(770, 470, "Назад|не шлём!", "p", 18) + '</g>')
    slide("Этап 4: лавинная рассылка", sc(
        head("Этап 4. Лавинная рассылка", "Полученный LSP немедленно уходит во все интерфейсы, кроме того, откуда пришёл."),
        split(steps(
            rowc("bolt", "Сразу, без таймеров", "Получив LSP, маршрутизатор пересылает его дальше немедленно — поэтому сходимость быстрая.", "y"),
            rowc("swap", "Кроме входного", "Пакет не отправляется обратно в интерфейс, через который он пришёл.", "p"),
            rowc("up", "Когда запускается", "При первом запуске и перезагрузке, при разрыве канала, при появлении нового маршрутизатора.", "b"),
            rowc("shield", "Защита от дублей", "По номеру последовательности и возрасту старый дубль отбрасывается — лавина затухает.", "g")),
            ill("0 0 900 640", art), "44fr 56fr")
    ), scen="lsaflow")

    # ------------------------------------------------------------ этап 5
    art = (router(130, 120, 130, "b", label="R2") + router(130, 320, 130, "b", label="R3") +
           router(130, 520, 130, "b", label="R4") +
           "".join(arrow(210, y, 500, 320, "b", w=6) for y in (140, 340, 540)) +
           '<ellipse cx="660" cy="170" rx="150" ry="42" fill="#c7e2fb" stroke="#3a72b0" stroke-width="3"/>'
           '<path d="M510 170 V460 a150 42 0 0 0 300 0 V170" fill="#e3f0fd" stroke="#3a72b0" stroke-width="3"/>'
           '<path d="M510 270 a150 42 0 0 0 300 0 M510 365 a150 42 0 0 0 300 0" fill="none" stroke="#3a72b0" stroke-width="3"/>'
           '<ellipse cx="660" cy="170" rx="150" ry="42" fill="#c7e2fb" stroke="#3a72b0" stroke-width="3"/>' +
           txt(660, 330, "LSDB", fs=48, weight=900, color="#1f6fc4") +
           bubble(660, 520, "одинакова у всех в области", "b", 19))
    stage("Этап 5: LSDB", 5, "Этап 5. База данных состояний каналов", "Из полученных LSP собирается LSDB — общая карта топологии области.",
          ill("0 0 900 620", art),
          [rowc("db", "Как наполняется", "Каждый маршрутизатор пишет полученные анонсы в свою LSDB и рассылает обновления дальше.", "b"),
           rowc("ok", "Признак готовности", "Когда новые анонсы совпадают с уже известными — LSDB наполнена и перестала меняться.", "g"),
           rowc("stop", "Главное требование", "LSDB должна быть <b>одинаковой</b> у всех маршрутизаторов области. Расхождение — причина странных маршрутов.", "p")])

    # ------------------------------------------------------------ этап 6
    art = ('<ellipse cx="140" cy="200" rx="100" ry="28" fill="#c7e2fb" stroke="#3a72b0" stroke-width="3"/>'
           '<path d="M40 200 V380 a100 28 0 0 0 200 0 V200" fill="#e3f0fd" stroke="#3a72b0" stroke-width="3"/>'
           '<ellipse cx="140" cy="200" rx="100" ry="28" fill="#c7e2fb" stroke="#3a72b0" stroke-width="3"/>' +
           txt(140, 310, "LSDB", fs=34, weight=900, color="#1f6fc4") +
           arrow(255, 300, 330, 300, "p", w=7) +
           '<rect x="345" y="140" width="250" height="320" rx="24" fill="#fef6dc"/>' + txt(470, 190, "SPF", fs=34, weight=900) +
           '<path d="M470 230 L410 320 M470 230 L530 320 M530 320 L570 400" stroke="#f2b705" stroke-width="7" stroke-linecap="round"/>'
           '<circle cx="470" cy="230" r="18" fill="#ff5c9e"/><circle cx="410" cy="320" r="16" fill="#3fc47c"/>'
           '<circle cx="530" cy="320" r="16" fill="#3fc47c"/><circle cx="570" cy="400" r="16" fill="#3fc47c"/>' +
           arrow(605, 300, 680, 300, "p", w=7) +
           '<rect x="690" y="140" width="190" height="320" rx="20" fill="#fff" stroke="#121212" stroke-width="3"/>' +
           txt(785, 186, "RIB", fs=30, weight=900) +
           "".join('<rect x="710" y="%d" width="150" height="34" rx="8" fill="%s"/>' % (210 + i * 46, c)
                   for i, c in enumerate(["#e6f7ec", "#e6f7ec", "#fde7f0", "#e3f0fd", "#fef6dc"])) +
           bubble(785, 490, "лучшие → FIB", "p", 18))
    stage("Этап 6: SPF и таблица", 6, "Этап 6. Дерево SPF и таблица маршрутизации", "Каждый ставит себя в корень перевёрнутого дерева и считает путь до каждой сети.",
          ill("0 0 900 580", art),
          [rowc("tree", "Расчёт SPF", "Маршрутизатор применяет алгоритм Дейкстры к своей LSDB и строит дерево кратчайших путей.", "y"),
           rowc("doc", "RIB", "Routing Information Base: все известные маршруты от всех источников — OSPF, статика, подключённые сети.", "b"),
           rowc("bolt", "FIB", "Forwarding Information Base: только лучшие маршруты — по ним реально пересылаются пакеты.", "p"),
           rowc("swap", "Деревья разные", "LSDB одна на область, но у каждого маршрутизатора своё дерево — корнем он ставит себя.", "g")])

    # ------------------------------------------------------------ три базы
    a1 = mini("0 0 300 170", router(80, 70, 110, "b", label="R1") + router(220, 70, 110, "p", label="R2") +
              '<path d="M125 50 h50" stroke="#3b9eff" stroke-width="5" marker-end="url(#m_b)" marker-start="url(#m_b)"/>' +
              pill(150, 150, "соседи: FULL", "gb", 16))
    a2 = mini("0 0 300 170", '<ellipse cx="150" cy="30" rx="80" ry="22" fill="#ffd3e4" stroke="#b9467c" stroke-width="3"/>'
              '<path d="M70 30 V130 a80 22 0 0 0 160 0 V30" fill="#fde7f0" stroke="#b9467c" stroke-width="3"/>'
              '<ellipse cx="150" cy="30" rx="80" ry="22" fill="#ffd3e4" stroke="#b9467c" stroke-width="3"/>' +
              txt(150, 100, "LSDB", fs=30, weight=900, color="#d8276f"))
    a3 = mini("0 0 300 170", '<rect x="60" y="10" width="180" height="150" rx="16" fill="#fff" stroke="#121212" stroke-width="3"/>' +
              "".join('<rect x="78" y="%d" width="144" height="24" rx="6" fill="%s"/>' % (30 + i * 32, c)
                      for i, c in enumerate(["#e6f7ec", "#e3f0fd", "#fef6dc", "#fde7f0"])))
    slide("Три базы данных", sc(
        head("Компоненты OSPF: три базы данных", "Все три хранятся и обрабатываются в оперативной памяти маршрутизатора."),
        '<div class="row3 fill">' + steps(
            vcard("1", "База смежности", a1, "<b>Adjacency database</b> — таблица соседних устройств: кто найден, в каком состоянии, кто DR/BDR.<br>"
                  "<b>show ip ospf neighbor</b>", "b", "кого я вижу"),
            vcard("2", "База состояний каналов", a2, "<b>Link-State Database</b> — таблица топологии, все LSA области. Из неё считается дерево SPF.<br>"
                  "<b>show ip ospf database</b>", "p", "как устроена сеть"),
            vcard("3", "База пересылки", a3, "<b>Forwarding database</b> — таблица маршрутизации, результат расчёта.<br>"
                  "<b>show ip route</b>", "g", "куда слать пакет")) + '</div>'
    ))

    # ------------------------------------------------------------ типы пакетов (как r34)
    p1 = mini("0 0 300 190", router(90, 110, 120, "p", label="R1") + router(215, 110, 120, "b", label="R2") +
              '<path d="M118 40 a40 40 0 0 1 64 0 M130 56 a24 24 0 0 1 40 0" stroke="#ff5c9e" stroke-width="7" fill="none" stroke-linecap="round"/>')
    p2 = mini("0 0 300 190", "".join('<ellipse cx="%d" cy="%d" rx="48" ry="14" fill="%s" stroke="#121212" stroke-width="2.6"/>'
                                     '<rect x="%d" y="%d" width="96" height="30" fill="%s" stroke="#121212" stroke-width="2.6"/>'
                                     % (x, y, c, x - 48, y, c) for x, c in ((70, "#c7e2fb"), (230, "#ffd3e4")) for y in (80, 120)) +
              '<rect x="120" y="20" width="60" height="70" rx="8" fill="#fff" stroke="#121212" stroke-width="2.6"/>'
              '<path d="M132 40h36M132 54h36M132 68h24" stroke="#3b9eff" stroke-width="4"/>' +
              '<path d="M125 120 h50" stroke="#ff5c9e" stroke-width="5" marker-end="url(#m_p)" marker-start="url(#m_p)"/>')
    p3 = mini("0 0 300 190", '<rect x="30" y="40" width="100" height="120" rx="12" fill="#fff" stroke="#121212" stroke-width="3"/>'
              '<path d="M50 70h60M50 95h60M50 120h40" stroke="#3b9eff" stroke-width="5"/>' +
              arrow(140, 100, 180, 100, "p", w=7) +
              '<ellipse cx="240" cy="50" rx="45" ry="13" fill="#c7e2fb" stroke="#121212" stroke-width="2.6"/>'
              '<path d="M195 50 V150 a45 13 0 0 0 90 0 V50" fill="#e3f0fd" stroke="#121212" stroke-width="2.6"/>'
              '<ellipse cx="240" cy="50" rx="45" ry="13" fill="#c7e2fb" stroke="#121212" stroke-width="2.6"/>')
    p4 = mini("0 0 300 190", '<rect x="30" y="20" width="240" height="160" rx="16" fill="#fff" stroke="#b9467c" stroke-width="3"/>'
              '<rect x="30" y="20" width="240" height="40" rx="16" fill="#ffd3e4"/>' + txt(150, 50, "LSU", fs=24, weight=900) +
              "".join('<rect x="%d" y="78" width="62" height="84" rx="10" fill="#e3f0fd" stroke="#3a72b0" stroke-width="2"/>%s'
                      % (48 + i * 76, txt(79 + i * 76, 150, "LSA", fs=17, weight=900)) for i in range(3)))
    p5 = mini("0 0 300 190", '<rect x="40" y="30" width="220" height="140" rx="16" fill="#fff" stroke="#b9467c" stroke-width="3" '
              'transform="rotate(-6 150 100)"/>' + txt(150, 80, "LSAck", fs=26, weight=900) + ok(150, 125, 28))
    slide("Пять типов пакетов", sc(
        head("Типы пакетов OSPF", "Обнаружение соседей и обмен данными маршрутизации. Тип задаётся полем Type в заголовке."),
        '<div class="row5 fill">' + steps(
            vcard("01", "Пакет приветствия", p1, "Устанавливает и поддерживает смежность между маршрутизаторами OSPF.", "p", "Hello"),
            vcard("02", "Описание базы данных", p2, "Сокращённый список LSDB для сверки баз маршрутизаторов области.", "b", "DBD"),
            vcard("03", "Запрос состояния канала", p3, "Запрашивает подробные данные о записи, указанной в DBD.", "y", "LSR"),
            vcard("04", "Обновление состояния канала", p4, "Передаёт ответ на LSR и объявляет новые данные; содержит записи LSA.", "p", "LSU"),
            vcard("05", "Подтверждение", p5, "Подтверждает получение пакета LSU.", "b", "LSAck")) + '</div>',
        step('<div class="row2" style="grid-template-columns:3fr 1fr">' +
             chain([("Hello", ""), ("DBD", "b"), ("LSR", "y"), ("LSU", ""), ("LSAck", "b")]) +
             rowc("bulb", "LSU", "Может содержать до 11 типов LSA; обычно 1–5 и 7.", "y") + '</div>')
    ))

    # ------------------------------------------------------------ заголовок OSPF
    body, h = bitdiag([[("Version = 2", 8), ("Type = 1…5", 8), ("Packet Length", 16)],
                       [("Router ID", 32)], [("Area ID", 32)],
                       [("Checksum", 16), ("AuType", 16)], [("Authentication", 32)], [("Authentication (продолжение)", 32)]])
    slide("Заголовок OSPFv2", sc(
        head("Заголовок пакета OSPFv2", "24 октета — одинаковые для всех пяти типов пакетов. Поле Type определяет, что лежит дальше."),
        split(
            ill("0 0 1000 %d" % (h + 10), body),
            panel("doc", "Что означают поля",
                  table(["Поле", "Бит", "Назначение"],
                        [["Version", ("8", "c"), "Версия протокола, для OSPFv2 = 2"],
                         ["Type", ("8", "c"), "1 Hello · 2 DBD · 3 LSR · 4 LSU · 5 LSAck"],
                         ["Packet Length", ("16", "c"), "Длина всего пакета с заголовком"],
                         ["Router ID", ("32", "c"), "Идентификатор отправителя"],
                         ["Area ID", ("32", "c"), "Область, из которой отправлен пакет"],
                         ["Checksum", ("16", "c"), "Контрольная сумма, кроме полей аутентификации"],
                         ["AuType", ("16", "c"), "0 — нет, 1 — открытый текст, 2 — MD5"],
                         ["Authentication", ("64", "c"), "Пароль до 8 символов или данные MD5"]]), "b"),
            "54fr 46fr")
    ))

    # ------------------------------------------------------------ Hello
    body, h = bitdiag([[("Network Mask", 32)], [("Hello Interval", 16), ("Options", 8), ("Priority", 8)],
                       [("Dead Interval", 32)], [("Designated Router (DR)", 32)], [("Backup DR (BDR)", 32)],
                       [("Neighbor ID …", 32)]])
    slide("Формат Hello", sc(
        head("Пакет приветствия Hello", "Type = 1. Самый частый пакет OSPF — и самый придирчивый к совпадению параметров."),
        split(
            ill("0 0 1000 %d" % (h + 10), body) +
            step(rowc("eye", "Зачем нужен", "Обнаружить соседей • объявить параметры, на которые обе стороны обязаны согласиться • "
                      "выбрать DR и BDR на сетях с множественным доступом.", "b")),
            steps(rowc("clock", "Hello Interval", "Как часто шлём Hello. По умолчанию <b>10 с</b>.", "y"),
                  rowc("stop", "Dead Interval", "Сколько ждать Hello, прежде чем считать соседа мёртвым. По умолчанию <b>40 с</b>.", "p"),
                  rowc("star", "Priority", "Приоритет на выборах DR/BDR, 0–255. Значение <b>0</b> — не участвует.", "g"),
                  rowc("doc", "Options", "Флаги возможностей: <b>E</b> — маршрутизатор ASBR, <b>T</b> — несколько метрик.", "v"),
                  rowc("shield", "Должно совпасть", "Hello и Dead, маска подсети, Area ID, тип сети, аутентификация.", "p")),
            "52fr 48fr")
    ))

    # ------------------------------------------------------------ DBD
    body, h = bitdiag([[("Interface MTU", 16), ("Options", 8), ("0 0 0 0 0 I M MS", 8)],
                       [("DD Sequence Number", 32)], [("LSA Header 1 (20 октетов)", 32)], [("LSA Header 2 …", 32)]])
    slide("Формат DBD", sc(
        head("Пакет описания базы данных DBD", "Type = 2. Краткая опись своей LSDB — только заголовки LSA, без содержимого."),
        split(
            ill("0 0 1000 %d" % (h + 10), body) +
            step(rowc("bulb", "Главная идея", "По заголовку LSA видно тип, идентификаторы, возраст и номер последовательности — "
                      "этого хватает, чтобы понять, у кого запись свежее.", "y")),
            steps(rowc("doc", "Interface MTU", "Наибольшая датаграмма без фрагментации. <b>Не совпали MTU — соседство зависнет в ExStart/Exchange.</b>", "p"),
                  rowc("up", "Флаг I — Init", "1 — это первый пакет DBD в обмене.", "b"),
                  rowc("arr", "Флаг M — More", "1 — будет ещё хотя бы один пакет DBD.", "y"),
                  rowc("star", "Флаг MS — Master/Slave", "Кто ведущий. Ведущий — маршрутизатор с большим Router ID.", "g"),
                  rowc("sum", "DD Sequence Number", "Начальное значение задаёт ведущий, дальше +1 с каждым пакетом.", "v")),
            "52fr 48fr")
    ))

    # ------------------------------------------------------------ LSR LSU LSAck
    body1, h1 = bitdiag([[("LS Type", 32)], [("Link State ID", 32)], [("Advertising Router", 32)]])
    body2, h2 = bitdiag([[("Number of LSA", 32)], [("LSA Header + LSA Data", 32)], [("LSA …", 32)]])
    body3, h3 = bitdiag([[("LSA Header 1", 32)], [("LSA Header 2", 32)], [("LSA Header …", 32)]])
    slide("LSR, LSU, LSAck", sc(
        head("Пакеты LSR, LSU и LSAck", "Три пакета, которые завершают синхронизацию баз."),
        '<div class="row3 fill">' + steps(
            panel("hello", "LSR · Type 3", ill("0 0 1000 %d" % (h1 + 10), body1) +
                  '<p>Запрос: «пришли подробности вот об этой записи». Запись определяется тремя полями.</p>', "y"),
            panel("db", "LSU · Type 4", ill("0 0 1000 %d" % (h2 + 10), body2) +
                  '<p>Ответ на LSR и объявление новых данных. Несёт одно или несколько LSA целиком.</p>', "p"),
            panel("ok", "LSAck · Type 5", ill("0 0 1000 %d" % (h3 + 10), body3) +
                  '<p>Подтверждение получения LSU — содержит заголовки подтверждаемых LSA.</p>', "b")) + '</div>',
        step(foot("LSAck делает рассылку надёжной без TCP: неподтверждённый LSU отправляется повторно через retransmit-interval.", "ok"))
    ))

    # ------------------------------------------------------------ полный обмен
    seqs = [("Hello", "«я здесь, вот мои параметры»", "p", 1, "Init"),
            ("Hello", "«вижу тебя в списке соседей»", "b", -1, "2-Way"),
            ("DBD", "пустой — кто ведущий? seq = X", "y", 1, "ExStart"),
            ("DBD", "опись моей LSDB, seq = Y", "y", -1, "Exchange"),
            ("LSR", "пришли вот эти записи", "p", 1, "Loading"),
            ("LSU", "вот объявления LSA", "g", -1, "Loading"),
            ("LSAck", "получил", "b", 1, "Full")]
    art = (router(150, 60, 150, "b", label="R1") + router(850, 60, 150, "p", label="R2") +
           link(150, 120, 150, 670, 4, "#c7d6e4", dash="8 8") + link(850, 120, 850, 670, 4, "#c7d6e4", dash="8 8") +
           "".join('<g class="pstep go-f">' +
                   (arrow(170, 150 + i * 74, 830, 150 + i * 74, t if t != "b" else "b", w=6) if d > 0
                    else arrow(830, 150 + i * 74, 170, 150 + i * 74, t, w=6)) +
                   '<rect x="330" y="%d" width="340" height="44" rx="22" fill="#fff" stroke="#e9eef3" stroke-width="2"/>' % (128 + i * 74) +
                   txt(345, 157 + i * 74, nm, fs=21, weight=900, anchor="start") +
                   txt(430, 157 + i * 74, s, fs=16, weight=600, anchor="start") +
                   pill(60, 150 + i * 74, st, "w", 15, w=100) + '</g>'
                   for i, (nm, s, t, d, st) in enumerate(seqs)))
    slide("Полный обмен", sc(
        head("Полный цикл обмена между соседями", "От первого Hello до синхронизированных баз — слева состояние соседства R1."),
        split(ill("0 0 1000 700", art),
              steps(rowc("hello", "Знакомство", "Два Hello: сначала «я здесь», затем «вижу тебя» — двусторонняя связь.", "p"),
                    rowc("doc", "Сверка", "DBD: первый пустой выбирает ведущего, дальше описи баз.", "y"),
                    rowc("db", "Догрузка", "LSR → LSU → LSAck для каждой недостающей записи.", "g"),
                    rowc("ok", "Итог", "Базы одинаковы — состояние <b>Full</b>, запускается SPF.", "b")),
              "60fr 40fr")
    ), scen="pkt")

    # ------------------------------------------------------------ коды маршрутов
    slide("Коды маршрутов", sc(
        head("Как LSA превращаются в маршруты", "Три группы маршрутов OSPF и их коды в таблице маршрутизации."),
        '<div class="row3" style="flex:none">' + steps(
            vcard("1", "Внутри области", mini("0 0 300 120", blob(150, 60, 130, 50, "p", None) +
                  router(100, 50, 70, "p") + router(200, 50, 70, "p") + link(100, 60, 200, 60, 4, "#7d9cc0")),
                  "Пути к сетям своей области. По <b>LSA-1</b> и <b>LSA-2</b>.", "p", "O"),
            vcard("2", "Между областями", mini("0 0 300 120", blob(80, 60, 70, 50, "p", None) + blob(220, 60, 70, 50, "b", None) +
                  router(150, 50, 70, "y")),
                  "Пути к сетям других областей через ABR. По <b>LSA-3</b> и <b>LSA-4</b>.", "b", "O IA"),
            vcard("3", "Внешние", mini("0 0 300 120", blob(100, 60, 90, 50, "b", None) + router(120, 50, 70, "gr") +
                  globe(250, 60, 30)),
                  "Пути к сетям вне автономной системы. По <b>LSA-5</b>, в NSSA — <b>LSA-7</b>.", "y", "O E1 · O E2")) + '</div>',
        '<div class="row2 fill">' +
        step(panel("doc", "Пример вывода show ip route", cli(
            ["Codes: C - connected, O - OSPF, IA - inter area, E1/E2 - external",
             ("C   ", "192.168.1.0/24  directly connected, gi1/0/1"),
             ("O   ", "203.0.113.4/30  [150/20] via 203.0.113.2"),
             ("O IA", "10.20.0.0/16    [150/35] via 203.0.113.2"),
             ("O E2", "0.0.0.0/0       [150/1]  via 203.0.113.6"),
             ("O E1", "172.30.0.0/16   [150/54] via 203.0.113.6")]), "w")) +
        step(panel("sum", "E1 или E2",
                   '<p><b>E2</b> (по умолчанию) — метрика равна внешней и не растёт внутри OSPF.</p>'
                   '<p><b>E1</b> — к внешней метрике прибавляется стоимость пути до ASBR. Нужно, когда выходов наружу '
                   'несколько и важно выбрать ближайший.</p>'
                   '<p><b>[150/20]</b> — preference и метрика маршрута.</p>', "y")) + '</div>'
    ))

    # ------------------------------------------------------------ суммирование
    art = ("".join('<rect x="40" y="%d" width="270" height="62" rx="20" fill="#e3f0fd"/>%s'
                   % (60 + i * 92, txt(175, 101 + i * 92, s, fs=24, weight=800))
                   for i, s in enumerate(["10.1.0.0/24", "10.1.1.0/24", "10.1.2.0/24", "10.1.3.0/24"])) +
           "".join(arrow(320, 91 + i * 92, 420, 240, "b", w=4) for i in range(4)) +
           router(520, 230, 170, "y", label="ABR") +
           arrow(620, 245, 700, 245, "g", w=8) +
           '<rect x="700" y="200" width="270" height="90" rx="26" fill="#c6efd6"/>' +
           txt(835, 258, "10.1.0.0/22", fs=30, weight=900) +
           bubble(835, 330, "одна запись вместо четырёх", "g", 17) +
           txt(175, 470, "Area 0.0.0.1", fs=20, weight=800, color="#1f6fc4") + txt(835, 470, "в Area 0 — через LSA-3", fs=20, weight=800, color="#1d8a51"))
    slide("Суммирование маршрутов", sc(
        head("Суммирование маршрутов", "Непрерывный набор адресов объявляется одним маршрутом с более короткой маской."),
        split(ill("0 0 1000 500", art),
              steps(rowc("route", "На ABR", "Межобластные маршруты, объявляются через <b>LSA-3</b>.", "y"),
                    rowc("globe", "На ASBR", "Внешние маршруты, объявляются через <b>LSA-5</b>.", "g"),
                    rowc("stop", "Не внутри области", "Внутри области суммирование невозможно и нецелесообразно — там полная топология.", "p"),
                    rowc("gear", "По умолчанию выключено", "Включают осознанно. Диапазон должен быть непрерывным — иначе суммарный маршрут «соврёт».", "b")),
              "56fr 44fr")
    ))
