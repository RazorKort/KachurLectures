# -*- coding: utf-8 -*-
"""Вводный блок (слайды 1–8) в стиле инфографик методички: титул, цель, протокол OSPF,
определение, принцип Link State, RIP и OSPF, преимущества, недостатки."""

from _ospf_lib import (slide, head, sc, g, card, step, steps, irow, foot, tag, tags,
                       router, arrow, link, pill, txt, ban, ok,
                       blob, rack, cloud_icon, laptop, globe, envelope, legend, bubble, sparkle,
                       rowc, nrow, tile, split, ill, mini, ICON)


def rc(r, w):
    """Точка крепления линка к роутеру (середина боковины)."""
    return (r[0], r[1] + w * 0.14)


def ln(a, b, w, col="#3a72b0", sw=5, cls="", dash=None):
    (x1, y1), (x2, y2) = rc(a, w), rc(b, w)
    return link(x1, y1, x2, y2, sw, col, cls, dash)


def glow(a, b, w, cls=""):
    (x1, y1), (x2, y2) = rc(a, w), rc(b, w)
    return ('<g class="%s"><path d="M%.0f %.0f L%.0f %.0f" stroke="#ffe9a8" stroke-width="22" stroke-linecap="round"/>'
            '<path d="M%.0f %.0f L%.0f %.0f" stroke="#ff5c9e" stroke-width="7" stroke-dasharray="26 14" '
            'stroke-linecap="round"/></g>' % (cls, x1, y1, x2, y2, x1, y1, x2, y2))


def wifi(x, y, col="#ff5c9e", s=1.0):
    return ('<g transform="translate(%.0f %.0f) scale(%.2f)" fill="none" stroke="%s" stroke-width="7" '
            'stroke-linecap="round"><path d="M-34 -6 a48 48 0 0 1 68 0"/><path d="M-21 8 a30 30 0 0 1 42 0"/>'
            '<circle cx="0" cy="22" r="5" fill="%s" stroke="none"/></g>' % (x, y, s, col, col))


def dots(x, y, w, h, col="#ffc2da"):
    return "".join('<circle cx="%d" cy="%d" r="2.6" fill="%s"/>' % (x + i * 12, y + j * 12, col)
                   for i in range(int(w // 12)) for j in range(int(h // 12)))


def build():
    # ================================================================ 1. ТИТУЛ
    W = 120
    R = {"R1": (180, 190), "R2": (440, 170), "R3": (300, 360),
         "R4": (610, 400), "R5": (790, 530), "R6": (520, 560)}
    topo = (
        dots(40, 40, 120, 72) + dots(760, 610, 110, 60, "#b7d9f8") +
        rack(720, 20, 74, 150) + rack(806, 44, 74, 150) +
        cloud_icon(680, 200, 1.0) + cloud_icon(110, 600, .8, "#fff", "#f6c9dc") +
        blob(330, 270, 300, 210, "p", "Area 0", seed=.6, lab_y=82, fs=22) +
        blob(660, 480, 250, 175, "b", "Area 1", seed=2.1, lab_y=330, fs=22) +
        ln(R["R1"], R["R2"], W) + ln(R["R1"], R["R3"], W) + ln(R["R2"], R["R3"], W) +
        ln(R["R4"], R["R6"], W) + ln(R["R4"], R["R5"], W) + ln(R["R6"], R["R5"], W) +
        glow(R["R3"], R["R4"], W) +
        "".join(router(x, y, W, "p" if n in ("R1", "R2", "R3") else "b", label=n) for n, (x, y) in R.items()) +
        arrow(440, 410, 520, 420, "p", w=6) +
        wifi(70, 330) + sparkle(560, 70, "#ff5c9e") + sparkle(40, 470, "#ffd93d", 2) +
        laptop(130, 690, 130, "p")
    )
    slide("Титул", sc(
        '<div class="big-cover">'
        '<div class="ttl">' +
        tags(tag("Лекция · Динамическая маршрутизация", "b"), tag("Академия ElTex", "y")) +
        '<h1>Протокол<br>OSPF</h1>'
        '<p class="lead">Кратчайший путь <u>в сети</u>.<br>Open Shortest Path First — протокол состояния каналов '
        'и алгоритм Дейкстры.</p>' +
        tags(tag("IP-протокол 89", "p", True), tag("224.0.0.5 · 224.0.0.6", "p", True), tag("OSPFv2 · OSPFv3", "g")) +
        tags(tag("Ананко · Качур", "w")) +
        '</div>' + ill("0 0 900 720", topo) + '</div>'
    ), cover=True)

    # ================================================================ 2. ЦЕЛЬ
    slide("Цель лекции", sc(
        head("Цель лекции", "Изучить работу группы протоколов маршрутизации по состоянию каналов на примере OSPF."),
        '<div class="g g2 grow" style="grid-auto-rows:1fr">' +
        steps(
            rowc("net", "Принцип Link State",
                 "Как маршрутизатор собирает <b>полную карту области</b> и почему все маршрутизаторы видят одинаковую топологию.", "b"),
            rowc("route", "Алгоритм Дейкстры",
                 "Пошаговый расчёт кратчайших путей: метки вершин, посещённые вершины, дерево SPF.", "p"),
            rowc("sum", "Стоимость маршрута",
                 "Формула cost, сумма стоимостей интерфейсов на пути, равноценные маршруты ECMP.", "y"),
            rowc("hello", "Соседство и пакеты",
                 "Пять типов пакетов, семь состояний соседства, выбор DR и BDR, Router ID.", "g"),
            rowc("tree", "Области и LSA",
                 "Магистраль Area 0, Stub, NSSA, роли ABR и ASBR, типы LSA и куда они распространяются.", "v"),
            rowc("gear", "Настройка на ESR",
                 "Процесс, область, интерфейс, аутентификация, таймеры и команды проверки.", "b"),
        ) + '</div>',
        step(foot("В конце — пять практикумов: стоимость пути, Дейкстра своими руками, выбор типа области, "
                  "разбор таблицы маршрутизации, диагностика соседства. И итоговый тест.", "ok"))
    ))

    # ================================================================ 3. ПРОТОКОЛ OSPF (как r27)
    W = 112
    R = {"R1": (170, 180), "R2": (440, 160), "R3": (290, 330),
         "R4": (600, 370), "R5": (780, 500), "R6": (510, 520)}
    topo = (
        dots(30, 520, 96, 84) + dots(780, 330, 96, 72, "#b7d9f8") +
        rack(760, 16, 64, 130) + rack(832, 34, 60, 130) + cloud_icon(705, 180, .9) +
        blob(320, 240, 290, 190, "p", "Area 0", seed=.6, lab_y=60, fs=22) +
        blob(650, 450, 240, 165, "b", "Area 1", seed=2.1, lab_y=300, fs=22) +
        ln(R["R1"], R["R2"], W) + ln(R["R1"], R["R3"], W) + ln(R["R2"], R["R3"], W) +
        ln(R["R4"], R["R6"], W) + ln(R["R4"], R["R5"], W) + ln(R["R6"], R["R5"], W) +
        glow(R["R3"], R["R4"], W) +
        "".join(router(x, y, W, "p" if n in ("R1", "R2", "R3") else "b", label=n) for n, (x, y) in R.items()) +
        pill(445, 300, "ABR", "y", 15) + wifi(60, 360, "#ff5c9e", .8) + sparkle(560, 40)
    )
    slide("Протокол OSPF", sc(
        head("Протокол OSPF", "Кратчайший путь в сети: принцип, параметры, версии и из чего состоит протокол."),
        split(
            steps(
                rowc("net", "Принцип",
                     "<b>Бесклассовая внутренняя</b> маршрутизация • состояние каналов • кратчайший путь по Дейкстре • "
                     "разделение сети на области.", "p"),
                rowc("gear", "Параметры",
                     "IP-протокол: <b>89</b> • Preference: <b>150</b> • IP multicast: <b>224.0.0.5 / 224.0.0.6</b><br>"
                     "MAC multicast: <b>01-00-5E-00-00-05 / 01-00-5E-00-00-06</b>", "b"),
                rowc("doc", "Версии",
                     "<b>OSPFv2</b> — IPv4 (RFC 1247, RFC 2328) • <b>OSPFv3</b> — IPv6 и расширения для IPv4 (RFC 2740).", "y"),
                rowc("db", "Компоненты",
                     "3 базы данных • 5 типов пакетов • 7 состояний • 4 типа маршрутизаторов • 6 типов областей • "
                     "11 типов записей LSDB • 4 типа сетей • 3 роли маршрутизаторов", "p"),
                rowc("tree", "Область",
                     "Общая база состояния каналов • собственные IP-сети • рекомендуется до 50 маршрутизаторов "
                     "в области.", "b")),
            ill("0 0 900 640", topo), "50fr 50fr")
    ))

    # ================================================================ 4. ОПРЕДЕЛЕНИЕ ПОДРОБНО
    enc = (
        '<rect x="30" y="20" width="540" height="600" rx="28" fill="#fde7f0"/>' +
        txt(60, 66, "Кадр Ethernet", fs=26, anchor="start", weight=800) +
        txt(60, 100, "MAC назначения:", fs=19, anchor="start", weight=600, color="#56606b") +
        txt(60, 130, "01-00-5E-00-00-05 / -06", fs=21, anchor="start", weight=800) +
        '<rect x="60" y="160" width="480" height="430" rx="24" fill="#e3f0fd"/>' +
        txt(90, 204, "IP-пакет", fs=26, anchor="start", weight=800) +
        txt(90, 240, "Protocol = 89", fs=21, anchor="start", weight=800) +
        txt(90, 272, "224.0.0.5 — все маршрутизаторы OSPF", fs=18, anchor="start", weight=700) +
        txt(90, 300, "224.0.0.6 — только DR и BDR", fs=18, anchor="start", weight=700) +
        '<rect x="90" y="330" width="420" height="230" rx="22" fill="#fef6dc" stroke="#efcf6a" stroke-width="3"/>' +
        txt(300, 380, "Пакет OSPF", fs=28, weight=800) +
        txt(300, 416, "заголовок — 24 октета", fs=19, color="#56606b", weight=600) +
        txt(300, 456, "поле Type = 1…5", fs=21, weight=800) +
        txt(300, 496, "Hello · DBD · LSR", fs=20, weight=700) +
        txt(300, 528, "LSU · LSAck", fs=20, weight=700) +
        bubble(470, 640, "Без UDP и TCP!", "p", 18)
    )
    slide("Что такое OSPF", sc(
        head("Что такое OSPF", "Определение из методички — целиком, без сокращений."),
        split(
            card(None,
                 '<p style="font-size:clamp(16px,1.35vw,27px);line-height:1.38">'
                 '<b>OSPF (Open Shortest Path First)</b> — протокол динамической маршрутизации, основанный на '
                 'технологии отслеживания <b>состояния каналов</b> (link-state) и использующий для нахождения '
                 'кратчайшего пути <b>алгоритм Дейкстры</b>. Информация о топологии распространяется по области '
                 '<b>без изменений</b> — у всех маршрутизаторов одна и та же карта.</p>'
                 '<div class="hr"></div>'
                 '<p style="font-size:clamp(15px,1.2vw,24px);line-height:1.38">'
                 '<b>Область OSPF</b> — группа маршрутизаторов, которые совместно используют данные о состоянии '
                 'каналов в своей области. Каждая область работает с собственным набором IP-сетей.</p>', "", "w") +
            '<div class="g g2" style="flex:1 1 auto;grid-auto-rows:1fr">' +
            steps(rowc("route", "IGP", "Протокол <b>внутренней</b> маршрутизации внутри одной автономной системы.", "p"),
                  rowc("star", "Preference 150", "Административное расстояние OSPF на ESR по умолчанию.", "y"),
                  rowc("doc", "RFC 2328", "OSPFv2 для IPv4. Ранняя редакция — RFC 1247.", "b"),
                  rowc("doc", "RFC 2740", "OSPFv3: IPv6 и расширения для IPv4.", "g")) + '</div>',
            ill("0 0 600 700", enc), "60fr 40fr")
    ))

    # ================================================================ 5. ПРИНЦИП LINK STATE (как r33)
    def ic_list():
        return mini("0 0 80 64", '<rect x="6" y="6" width="34" height="46" rx="5" fill="#fff" stroke="#121212" stroke-width="3"/>'
                    '<path d="M14 18h18M14 28h18M14 38h12" stroke="#121212" stroke-width="3" stroke-linecap="round"/>' +
                    router(58, 38, 40, "p"))

    def ic_nb():
        return mini("0 0 80 64", router(22, 34, 38, "b") + router(60, 34, 38, "b") +
                    '<path d="M32 14 a12 12 0 0 1 16 0 M28 8 a20 20 0 0 1 24 0" stroke="#3b9eff" stroke-width="3" fill="none" stroke-linecap="round"/>')

    def ic_lsp():
        return mini("0 0 80 64", '<rect x="18" y="4" width="44" height="56" rx="6" fill="#fff" stroke="#121212" stroke-width="3"/>'
                    '<text x="40" y="26" text-anchor="middle" font-size="15" font-weight="900">LSP</text>'
                    '<path d="M26 38h28M26 48h20" stroke="#121212" stroke-width="3" stroke-linecap="round"/>')

    def ic_flood():
        return mini("0 0 80 64", router(40, 30, 40, "p") +
                    "".join(arrow(40 + dx * 8, 36 + dy * 8, 40 + dx * 30, 36 + dy * 26, "b", w=3)
                            for dx, dy in ((-1, 0), (1, 0), (0, -1), (-.8, .8), (.8, .8))))

    def ic_db():
        return mini("0 0 80 64", '<ellipse cx="40" cy="12" rx="22" ry="7" fill="#c7e2fb" stroke="#121212" stroke-width="3"/>'
                    '<path d="M18 12v38c0 4 10 7 22 7s22-3 22-7V12" fill="#e3f0fd" stroke="#121212" stroke-width="3"/>'
                    '<path d="M18 25c0 4 10 7 22 7s22-3 22-7M18 38c0 4 10 7 22 7s22-3 22-7" fill="none" stroke="#121212" stroke-width="3"/>')

    def ic_tree():
        return mini("0 0 80 64", '<path d="M40 14 L22 46 M40 14 L58 46" stroke="#121212" stroke-width="3"/>'
                    '<circle cx="40" cy="14" r="8" fill="#3b9eff"/><circle cx="22" cy="48" r="8" fill="#3b9eff"/>'
                    '<circle cx="58" cy="48" r="8" fill="#3b9eff"/><path d="M48 4 v14 M48 4 h12 l-4 4 l4 4 h-12" '
                    'stroke="#ff5c9e" stroke-width="3" fill="#ff5c9e"/>')

    def ic_rib():
        return mini("0 0 80 64", '<rect x="6" y="6" width="44" height="52" rx="6" fill="#fff" stroke="#121212" stroke-width="3"/>'
                    '<path d="M14 20h28M14 32h28M14 44h18" stroke="#121212" stroke-width="3" stroke-linecap="round"/>'
                    '<circle cx="58" cy="44" r="14" fill="#ff5c9e"/><path d="M51 44h12M58 38l6 6-6 6" stroke="#fff" '
                    'stroke-width="3" fill="none" stroke-linecap="round"/>')

    W = 74
    A = {"a1": (55, 260), "a2": (165, 170), "a3": (165, 350), "abr1": (300, 260),
         "b1": (450, 185), "b2": (450, 335), "abr2": (600, 260),
         "c1": (735, 170), "c2": (735, 350), "c3": (850, 260)}
    E = [("a1", "a2"), ("a1", "a3"), ("a2", "abr1"), ("a3", "abr1"), ("abr1", "b1"), ("abr1", "b2"),
         ("b1", "abr2"), ("b2", "abr2"), ("abr2", "c1"), ("c1", "c3"), ("c2", "c3")]
    topo = (
        blob(170, 265, 165, 160, "y", "Область 1.1.1.1", seed=.3, lab_y=82, fs=17) +
        blob(450, 262, 150, 150, "v", "Область 0.0.0.0", seed=1.4, lab_y=92, fs=17) +
        blob(740, 265, 165, 160, "b", "Область 2.2.2.2", seed=2.4, lab_y=82, fs=17) +
        "".join(ln(A[a], A[b], W, "#121212", 3) for a, b in E) +
        ln(A["abr2"], A["c2"], W, "#121212", 3) +
        '<g>' + "".join(
            '<path d="M%.0f %.0f L%.0f %.0f" stroke="#ff5c9e" stroke-width="3.4" marker-end="url(#m_p)" '
            'marker-start="url(#m_p)"/>' % (
                (A[a][0] * .72 + A[b][0] * .28), (A[a][1] * .72 + A[b][1] * .28) - 16,
                (A[a][0] * .28 + A[b][0] * .72), (A[a][1] * .28 + A[b][1] * .72) - 16)
            for a, b in E[:8]) + '</g>' +
        "".join(router(x, y, W, "b") for (x, y) in A.values()) +
        '<g>' + ban(668, 318, 15) + '</g>' +
        bubble(735, 6, "Все маршрутизаторы|имеют одинаковую карту!", "p", 15) +
        legend(20, 450, [("arrow", "#ff5c9e", "Обмен LSP (состояние каналов)"),
                         ("line", "#121212", "Физический канал")], w=420, fs=15) +
        legend(460, 450, [("cross", "#ff5c9e", "Неисправный канал"),
                          ("dash", "#ff5c9e", "Дерево SPF к назначению")], w=420, fs=15)
    )
    slide("Принцип Link State", sc(
        head("Принцип работы протокола Link State", "Алгоритм SPF Эдсгера Дейкстры: семь шагов от включения до таблицы маршрутизации."),
        split(
            steps(nrow("1", "Сбор данных", ic_list(), "Каждый маршрутизатор собирает информацию о состоянии своих интерфейсов (каналов).", "p"),
                  nrow("2", "Обнаружение соседей", ic_nb(), "Маршрутизаторы обнаруживают соседей на непосредственно подключённых каналах.", "b"),
                  nrow("3", "Создание пакета состояния канала (LSP)", ic_lsp(), "Формируется LSP с информацией о своих интерфейсах и соседях.", "y"),
                  nrow("4", "Лавинная рассылка LSP", ic_flood(), "LSP распространяется по всей области OSPF ко всем маршрутизаторам.", "p"),
                  nrow("5", "Создание базы данных LSDB", ic_db(), "Каждый формирует одинаковую базу состояния каналов на основе полученных LSP.", "b"),
                  nrow("6", "Расчёт дерева SPF по Дейкстре", ic_tree(), "На основе LSDB рассчитывается дерево кратчайших путей.", "y"),
                  nrow("7", "Маршруты в таблицу", ic_rib(), "Наиболее оптимальные маршруты добавляются в таблицу маршрутизации.", "p")),
            ill("0 0 900 610", topo) +
            step(rowc("gear", "Настройка OSPF",
                      "Процесс создают <b>глобально</b>, затем привязывают по номеру к интерфейсу или туннелю — OSPF "
                      "активируется только на выбранном интерфейсе. Туннель используют в DMVPN. В RIP, наоборот, "
                      "глобальная настройка применяется ко всем интерфейсам.", "p")),
            "47fr 53fr"),
        step(foot("<b>Канал</b> — интерфейс маршрутизатора • <b>Состояние канала</b> — сведения о связи между "
                  "интерфейсами: сосед, сеть, стоимость.", ""))
    ))

    # ================================================================ 6. RIP И OSPF
    rip = (
        ln((110, 150), (400, 150), 120, "#a9b3be", 6) + ln((400, 150), (690, 150), 120, "#a9b3be", 6) +
        router(110, 150, 120, "g", label="R1") + router(400, 150, 120, "g", label="R2") +
        router(690, 150, 120, "g", label="R3") +
        bubble(255, 20, "сеть X — 2 hop через R2", "y", 16) +
        bubble(545, 20, "сеть X — 1 hop", "y", 16) +
        cloud_icon(820, 260, .9, "#fff", "#c7d6e4") + txt(820, 300, "сеть X", fs=16, weight=800) +
        txt(400, 300, "Маршрутизатор знает только направление и расстояние", fs=18, weight=700, color="#56606b")
    )
    ospf = (
        blob(400, 175, 360, 150, "b", None, seed=1.1) +
        ln((140, 120), (400, 80), 100) + ln((400, 80), (660, 120), 100) + ln((140, 120), (270, 230), 100) +
        ln((270, 230), (540, 230), 100) + ln((540, 230), (660, 120), 100) + ln((400, 80), (540, 230), 100) +
        router(140, 120, 100, "b", label="R1") + router(400, 80, 100, "b", label="R2") +
        router(660, 120, 100, "b", label="R3") + router(270, 230, 100, "b", label="R4") +
        router(540, 230, 100, "b", label="R5") +
        txt(400, 360, "Каждый видит всю карту области и считает путь сам", fs=18, weight=700, color="#56606b")
    )
    slide("RIP и OSPF", sc(
        head("Два подхода к маршрутизации", "Дистанционно-векторный RIP и протокол состояния каналов OSPF решают одну задачу по-разному."),
        '<div class="g g2 grow" style="grid-template-rows:minmax(0,1fr)">' +
        '<div class="col" style="min-height:0">' + ill("0 0 860 330", rip) +
        steps(rowc("route", "Дистанционно-векторный (RIP)",
                   "Сосед сообщает <b>готовый результат</b>: «до сети X — столько-то переходов». Карты сети нет.", "y"),
              rowc("clock", "Метрика и сходимость",
                   "Метрика — число переходов, предел 15. Обновления по таймеру, сходимость медленная, возможны петли.", "y")) +
        '</div>'
        '<div class="col" style="min-height:0">' + ill("0 0 860 380", ospf) +
        steps(rowc("net", "Состояние каналов (OSPF)",
                   "Маршрутизатор собирает <b>полную карту области</b>: кто с кем соединён и какова стоимость каждого канала.", "b"),
              rowc("bolt", "Метрика и сходимость",
                   "Метрика — стоимость (cost). Обновления по событию, быстрая сходимость, дерево SPF без петель.", "b")) +
        '</div></div>'
    ))

    # ================================================================ 7. ПРЕИМУЩЕСТВА (как r14, с анимацией)
    W = 104
    P = {"R1": (130, 200), "R2": (330, 120), "R3": (150, 370), "R4": (480, 290), "R5": (360, 455)}
    B = {"R6": (700, 175), "R7": (790, 330), "R8": (650, 460)}
    pts = dict(P, **B)
    topo = (
        blob(300, 300, 290, 240, "p", "Область 1", seed=.9, lab_y=62, fs=20) +
        blob(730, 300, 165, 215, "b", "Область 2", seed=2.6, lab_y=92, fs=20) +
        globe(840, 50, 30) + cloud_icon(560, 70, .7) +
        # стабильные соединения
        ln(pts["R4"], pts["R5"], W, "#121212", 4) + ln(pts["R4"], pts["R6"], W, "#121212", 4) +
        ln(pts["R4"], pts["R7"], W, "#121212", 4) + ln(pts["R6"], pts["R7"], W, "#121212", 4) +
        ln(pts["R7"], pts["R8"], W, "#121212", 4) + ln(pts["R5"], pts["R8"], W, "#121212", 4) +
        # дерево SPF
        ln(pts["R1"], pts["R2"], W, "#f2b705", 7) + ln(pts["R1"], pts["R3"], W, "#f2b705", 7) +
        ln(pts["R3"], pts["R5"], W, "#f2b705", 7) +
        # сбой R2–R4
        ln(pts["R2"], pts["R4"], W, "#ff5c9e", 4, dash="8 8") +
        "".join(router(x, y, W, "p", label=n) for n, (x, y) in P.items()) +
        "".join(router(x, y, W, "b", label=n) for n, (x, y) in B.items()) +
        '<g class="lcut go-f">' + '<path d="M392 186 l28 28 M420 186 l-28 28" stroke="#ff2e6e" stroke-width="9" stroke-linecap="round"/>' +
        bubble(470, 108, "Сбой|канала", "p", 16) + '</g>' +
        '<g class="lwave go-f">' + arrow(440, 300, 205, 230, "y", w=6, dash=False) + pill(320, 250, "LSP", "y", 15) + '</g>' +
        '<g class="lwave go-f">' + arrow(445, 330, 215, 375, "y", w=6) + pill(330, 335, "LSP", "y", 15) + '</g>' +
        '<g class="lwave go-f">' + arrow(470, 345, 400, 425, "y", w=6) + pill(470, 400, "LSP", "y", 15) + '</g>' +
        '<g class="lcalm go-f">' + bubble(770, 540, "Область 2|работает стабильно", "b", 15) + '</g>' +
        legend(20, 560, [("line", "#f2b705", "Дерево кратчайших путей (SPF)"),
                         ("arrow", "#f2b705", "Распространение LSP после изменения")], w=430, fs=15) +
        legend(470, 640, [("cross", "#ff2e6e", "Сбой канала")], w=210, fs=15)
    )
    slide("Преимущества LS", sc(
        head("Преимущества протоколов по состоянию каналов", "Точная карта сети и быстрая реакция на изменения."),
        split(
            '<div class="g g2" style="flex:1 1 auto;grid-auto-rows:1fr">' +
            steps(tile("tree", "Карта топологии",
                       "Каждый маршрутизатор строит общую карту области и вычисляет дерево кратчайших путей SPF.", "p"),
                  tile("bolt", "Быстрая сходимость",
                       "Получив LSP, маршрутизатор <b>сразу</b> рассылает его через остальные интерфейсы — без ожидания таймеров.", "b"),
                  tile("clock", "Обновления по событию",
                       "После исходной рассылки LSP идут только <b>при изменении топологии</b> — в отличие от регулярных обновлений distance-vector.", "y"),
                  tile("net", "Иерархия областей",
                       "Меньшие базы LSDB, агрегация маршрутов, сбой локализуется внутри области.", "p")) + '</div>',
            ill("0 0 900 700", topo), "50fr 50fr")
    ), scen="lspros")

    # ================================================================ 8. НЕДОСТАТКИ (как r05)
    mem = mini("0 0 360 150",
               "".join('<ellipse cx="80" cy="%d" rx="58" ry="17" fill="#e3f0fd" stroke="#3a72b0" stroke-width="3"/>'
                       '<path d="M22 %d v24 a58 17 0 0 0 116 0 v-24" fill="#c7e2fb" stroke="#3a72b0" stroke-width="3"/>'
                       % (y, y) for y in (100, 70, 40)) +
               '<ellipse cx="80" cy="40" rx="58" ry="17" fill="#e3f0fd" stroke="#3a72b0" stroke-width="3"/>' +
               "".join('<g transform="translate(%d %d) rotate(%d)"><rect width="150" height="34" rx="5" fill="%s" stroke="#121212" stroke-width="2.6"/>%s</g>'
                       % (x, y, r, c, "".join('<rect x="%d" y="8" width="13" height="18" rx="2" fill="#2a2f3d"/>' % (12 + i * 22) for i in range(6)))
                       for (x, y, r, c) in ((175, 52, -12, "#ffc2da"), (190, 92, -4, "#bcd9f6"))) +
               sparkle(318, 30, "#ff5c9e", 2))
    cpu = mini("0 0 360 150",
               '<rect x="30" y="38" width="100" height="90" rx="12" fill="#c9ccd8" stroke="#121212" stroke-width="3"/>'
               '<rect x="50" y="56" width="60" height="54" rx="6" fill="#e9ebf1"/>' +
               txt(80, 91, "CPU", fs=20, weight=900) +
               "".join('<path d="M%d 38 v-10 M%d 128 v10" stroke="#ff5c9e" stroke-width="3"/>' % (46 + i * 14, 46 + i * 14) for i in range(6)) +
               "".join(link(a[0], a[1], b[0], b[1], 3, "#9b7bf0") for a, b in
                       (((190, 50), (240, 90)), ((240, 90), (300, 50)), ((240, 90), (220, 130)), ((240, 90), (300, 120)), ((190, 50), (300, 50)))) +
               "".join('<circle cx="%d" cy="%d" r="11" fill="%s"/>' % (x, y, c) for x, y, c in
                       ((190, 50, "#ff5c9e"), (240, 90, "#3b9eff"), (300, 50, "#ff5c9e"), (220, 130, "#3b9eff"), (300, 120, "#9b7bf0"))) +
               '<circle cx="330" cy="30" r="20" fill="#fff" stroke="#121212" stroke-width="3"/>'
               '<path d="M330 30 v-12 M330 30 l9 6" stroke="#121212" stroke-width="3" stroke-linecap="round"/>')
    bw = mini("0 0 360 150",
              router(55, 80, 92, "p") + router(305, 80, 92, "b") +
              '<rect x="95" y="94" width="170" height="16" rx="8" fill="#2a2f3d"/>' +
              "".join(envelope(x, y, 30, t) for x, y, t in
                      ((120, 70, "p"), (155, 60, "b"), (190, 74, "y"), (225, 62, "p"), (140, 128, "b"), (205, 130, "p"), (250, 122, "y"))) +
              '<path d="M180 6 l22 38 h-44 z" fill="#ff5c9e"/>' + txt(180, 38, "!", fs=24, color="#fff", weight=900))
    slide("Недостатки LS", sc(
        head("Недостатки протоколов по состоянию каналов", "Цена точной карты — память, процессор и полоса в момент сходимости."),
        '<div class="wide grow" style="display:grid;grid-template-rows:repeat(3,1fr)">' +
        steps(
            '<div class="rowc" style="grid-template-columns:auto 1fr minmax(0,34%%)">%s</div>'
            % ('<span class="ico">%s</span><div><h3>Память</h3><p>Для базы данных состояния каналов (LSDB) и дерева '
               'кратчайших путей SPF нужны <b>дополнительные ресурсы памяти</b>. Чем больше область — тем больше база.</p></div>%s'
               % (ICON["db"], mem)),
            '<div class="rowc b" style="grid-template-columns:auto 1fr minmax(0,34%%)">%s</div>'
            % ('<span class="ico">%s</span><div><h3>Обработка ЦП</h3><p>Алгоритм SPF требует <b>больше времени ЦП</b>, '
               'так как строит полную карту топологии — и запускается заново при каждом изменении.</p></div>%s'
               % (ICON["cpu"], cpu)),
            '<div class="rowc y" style="grid-template-columns:auto 1fr minmax(0,34%%)">%s</div>'
            % ('<span class="ico">%s</span><div><h3>Полоса пропускания</h3><p>Обмен пакетами Hello и <b>лавинная рассылка LSP</b> '
               'при первом запуске могут перегружать нестабильные сети с низкой пропускной способностью.</p></div>%s'
               % (ICON["swap"], bw))) + '</div>',
        step(foot("В установившейся сети трафик OSPF небольшой: Hello раз в 10 секунд и обновления только по событию. "
                  "Пиковая нагрузка — при запуске и при нестабильных каналах.", "note"))
    ))
