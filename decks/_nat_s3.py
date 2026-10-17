# -*- coding: utf-8 -*-
"""Блок 3: формат DHCP-сообщения, Wireshark, DHCP Relay, настройка клиента/сервера/ретранслятора, проверка."""

from _sw_lib import grow, g, col, card, p, li, foot, tags, tag, table, cli, step, scene, task, quiz
from _nat_lib import slide, sc, head, pill, kv, big
import _nat_svg as S


def build():
    slide("Формат DHCP-сообщения", sc(
        head("Формат <em>сообщения</em> DHCP", "Поля заголовка и их длина в байтах"),
        grow("g2",
             step(table(["Поле DHCP", "Байт", "Описание"], [
                 ["<b>Операция</b> (op)", "1", "1 — запрос, 2 — ответ"],
                 ["<b>Тип аппаратного адреса</b>", "1", "Ethernet — значение 1"],
                 ["<b>Длина аппаратного адреса</b>", "1", "6 для Ethernet (MAC = 6 байт)"],
                 ["<b>Количество хопов</b> (Hops)", "1", "клиент ставит 0, каждый ретранслятор +1"],
                 ["<b>ID транзакции</b> (XID)", "4", "сопоставляет запросы и ответы"],
                 ["<b>Время</b> (Seconds)", "4", "прошло с начала аренды"],
                 ["<b>Флаги</b> (Flags)", "4", "в т. ч. флаг широковещания"],
             ])),
             step(table(["Поле DHCP", "Байт", "Описание"], [
                 ["<b>CIADDR</b> — адрес клиента", "4", "IP клиента, если известен"],
                 ["<b>YIADDR</b> — «твой» адрес", "4", "IP, предложенный сервером", ],
                 ["<b>SIADDR</b> — след. сервер", "4", "IP следующего сервера в цепочке"],
                 ["<b>GIADDR</b> — ретранслятор", "4", "IP relay-агента, если участвовал"],
                 ["<b>CHADDR</b> — MAC клиента", "4", "аппаратный адрес клиента"],
                 ["<b>SNAME</b> — имя сервера", "8", "обычно не используется"],
                 ["<b>Boot Filename</b>", "64", "имя файла загрузки, обычно пусто"],
                 ["<b>Magic Cookie</b>", "4", "99, 130, 83, 99 — «это DHCP»"],
                 ["<b>Опции</b> (Options)", "128", "маска, шлюз, DNS, срок аренды…"],
             ], "hl"))),
    ), bg="d")

    slide("Ключевые поля на схеме", sc(
        head("Ключевые поля <em>на схеме</em>", "Что меняется от сообщения к сообщению"),
        grow("g", col(_scene_fields()))
    ), bg="a")

    # -------- Wireshark
    slide("Wireshark: DHCPDISCOVER", sc(
        head("Wireshark · <em class='y'>DHCPDISCOVER</em>", "Анализатор трафика показывает сообщения DHCP подробно"),
        grow("g21",
             step(_ws("509  244.440747  0.0.0.0  →  255.255.255.255  DHCP  317  DHCP Discover", [
                 "> Frame 509: 317 bytes on wire",
                 "v Ethernet II, Src: EltexEnt_1f:f4:80 (e4:5a:d4:1f:f4:80)",
                 "!2   Destination: Broadcast (ff:ff:ff:ff:ff:ff)",
                 "     Source: EltexEnt_1f:f4:80 (e4:5a:d4:1f:f4:80)",
                 "     Type: IPv4 (0x0800)",
                 "!3 > Internet Protocol Version 4, Src: 0.0.0.0, Dst: 255.255.255.255",
                 "!4 > User Datagram Protocol, Src Port: 68, Dst Port: 67",
                 "> Dynamic Host Configuration Protocol (Discover)"])),
             col(step(card("Разбор", li([
                 "<b>1</b> — тип сообщения: DHCP Discover.",
                 "<b>2</b> — на канальном уровне адрес назначения <b class='mono'>ff:ff:ff:ff:ff:ff</b>.",
                 "<b>3</b> — своего адреса нет: <b class='mono'>0.0.0.0 → 255.255.255.255</b>.",
                 "<b>4</b> — UDP: клиент <b>68</b> → сервер <b>67</b>."]), "ye", "1"))))
    ), bg="b")

    slide("Wireshark: DHCPOFFER", sc(
        head("Wireshark · <em>DHCPOFFER</em>", "Ответ сервера на DISCOVER"),
        grow("g21",
             step(_ws("536  248.257062  10.10.1.1  →  255.255.255.255  DHCP  345  DHCP Offer", [
                 "!2 > Destination: Broadcast (ff:ff:ff:ff:ff:ff)",
                 "!3 > Internet Protocol Version 4, Src: 10.10.1.1, Dst: 255.255.255.255",
                 "  > User Datagram Protocol, Src Port: 67, Dst Port: 68",
                 "  v Dynamic Host Configuration Protocol (Offer)",
                 "      Message type: Boot Reply (2)",
                 "      Transaction ID: 0x225083cc",
                 "      Client IP address: 0.0.0.0",
                 "!4     Your (client) IP address: 10.10.1.13",
                 "      Next server IP address: 10.10.1.1",
                 "!5   > Option: (53) DHCP Message Type (Offer)",
                 "!5   > Option: (54) DHCP Server Identifier (10.10.1.1)",
                 "!5   > Option: (1) Subnet Mask (255.255.255.0)",
                 "!5   > Option: (3) Router   (6) DNS   (51) Lease Time"])),
             col(step(card("Разбор", li([
                 "<b>2</b> — у клиента нет адреса → широковещательный MAC; обработает только автор DISCOVER.",
                 "<b>3</b> — источник — адрес сервера <b class='mono'>10.10.1.1</b>, назначение — 255.255.255.255.",
                 "<b>4</b> — предлагаемый адрес <b class='mono'>10.10.1.13</b> (поле YIADDR).",
                 "<b>5</b> — опции: маска, срок аренды, шлюз по умолчанию и т. д."]), "or", "2"))))
    ), bg="d")

    slide("Wireshark: DHCPREQUEST", sc(
        head("Wireshark · <em class='v'>DHCPREQUEST</em>", "Клиент принимает предложенные параметры"),
        grow("g21",
             step(_ws("631  251.300828  0.0.0.0  →  255.255.255.255  DHCP  382  DHCP Request", [
                 "v Ethernet II, Dst: Broadcast (ff:ff:ff:ff:ff:ff)",
                 "!2   > Source: EltexEnt_1f:f4:80 (e4:5a:d4:1f:f4:80)",
                 "  > Internet Protocol Version 4, Src: 0.0.0.0, Dst: 255.255.255.255",
                 "!3 > User Datagram Protocol, Src Port: 68, Dst Port: 67",
                 "  v Dynamic Host Configuration Protocol (Request)",
                 "      Message type: Boot Request (1)",
                 "      Transaction ID: 0x225083cc",
                 "    > Option: (54) DHCP Server Identifier (10.10.1.1)",
                 "!4   > Option: (50) Requested IP Address (10.10.1.13)",
                 "    > Option: (55) Parameter Request List"])),
             col(step(card("Разбор", li([
                 "<b>1</b> — DHCPREQUEST отправляется от клиента к серверу.",
                 "<b>2</b> — сообщение широковещательное; в опции 54 указан конкретный сервер.",
                 "<b>3</b> — IPv4-адреса ещё нет → источник <b class='mono'>0.0.0.0</b>.",
                 "<b>4</b> — клиент указывает адрес, который запрашивает: <b class='mono'>10.10.1.13</b>."]), "vi", "3"))))
    ), bg="a")

    slide("Wireshark: DHCPACK", sc(
        head("Wireshark · <em>DHCPACK</em>", "Последнее сообщение в получении адреса"),
        grow("g21",
             step(_ws("632  251.324466  10.10.1.1  →  255.255.255.255  DHCP  345  DHCP ACK", [
                 "  > Internet Protocol Version 4, Src: 10.10.1.1, Dst: 255.255.255.255",
                 "  v Dynamic Host Configuration Protocol (ACK)",
                 "      Message type: Boot Reply (2)",
                 "      Transaction ID: 0x225083cc",
                 "!4     Your (client) IP address: 10.10.1.13",
                 "!4     Next server IP address: 10.10.1.1",
                 "!4   > Option: (53) DHCP Message Type (ACK)",
                 "!4   > Option: (1) Subnet Mask (255.255.255.0)",
                 "!4   v Option: (3) Router: 10.10.1.1",
                 "!4   v Option: (51) IP Address Lease Time: (600s) 10 minutes"])),
             col(step(card("Разбор", p(
                 "Сервер высылает <b>DHCPACK</b>, подтверждая, что клиент может использовать адрес "
                 "<b class='mono'>10.10.1.13</b>.",
                 "Обратите внимание: <b>Transaction ID 0x225083cc</b> одинаков во всех четырёх сообщениях — "
                 "так клиент понимает, что это ответы на его запрос.",
                 "Срок аренды — <b>600 с = 10 минут</b>."), "lm", "4"))))
    ), bg="c")

    # -------- RELAY
    slide("Проблема: сервер в другой сети", sc(
        head("Проблема: сервер <em>в другой сети</em>", "Широковещание не проходит через маршрутизатор"),
        grow("g", col(_scene_relay_problem()))
    ), bg="d")

    slide("DHCP Relay — ретранслятор", sc(
        head("DHCP Relay — <em>DHCP-ретранслятор</em>", "Позволяет клиентам в разных подсетях получать IP-адреса с центрального сервера"),
        grow("g", col(_scene_relay()))
    ), bg="a")

    slide("Возможности DHCP Relay", sc(
        head("Что делает <em>ретранслятор</em>", "Служба на маршрутизаторе или L3-коммутаторе"),
        grow("g3",
             step(card("Перенаправление запросов", p(
                 "Ловит широковещательный запрос клиента и пересылает его к DHCP-серверу в другой сети "
                 "<b>одноадресно</b>. Клиенты разных сегментов получают адреса от одного сервера."), "ye", "1")),
             step(card("Идентификация сегмента", p(
                 "Добавляет в сообщение, из какого сегмента пришёл запрос — свой адрес в поле <b>GIADDR</b>. "
                 "По нему сервер выбирает нужный <b>пул</b>."), "or", "2")),
             step(card("Централизация", p(
                 "Изменения конфигурации вносятся <b>в одном месте</b>, а не в каждой подсети отдельно. "
                 "Удобно в крупных и распределённых сетях."), "vi", "3"))),
        step(foot("Как сервер выбирает пул: по GIADDR = 192.168.10.1 → пул сети 192.168.10.0/24.", "note"))
    ), bg="b")

    # -------- настройка
    slide("Настройка DHCP-клиента", sc(
        head("Настройка <em>DHCP-клиента</em>", "Маршрутизатор ESR тоже может получать адрес по DHCP"),
        grow("g2",
             step(card("Команды", cli([
                 "# заходим в настройки интерфейса",
                 "> ESR(config-if-gi)# ip address dhcp",
                 "# (необязательно) адрес DHCP-сервера напрямую",
                 "> ESR(config-if-gi)# ip dhcp server address 192.168.2.10"], "ESR · CLI"), "cy", "1")),
             step(card("Пояснение", li([
                 "<b>ip address dhcp</b> — интерфейс получит адрес у DHCP-сервера.",
                 "<b>ip dhcp server address &lt;ADDR&gt;</b> — указать конкретный сервер.",
                 "Типичный случай — WAN-порт, которому адрес выдаёт провайдер."]), "ye", "?")))
    ), bg="d")

    slide("Настройка DHCP-сервера", sc(
        head("Настройка <em>DHCP-сервера</em>", "Интерфейс → пул → сеть, диапазон, исключения, шлюз"),
        grow("g2",
             step(card("Пример", cli([
                 "ESR# configure",
                 "> ESR(config)# interface gi1/0/1.10",
                 "ESR(config-if-gi)# ip address 192.168.10.10/24",
                 "ESR(config-if-gi)# exit",
                 "> ESR(config)# ip dhcp-server",
                 "> ESR(config)# ip dhcp-server pool DHCP-10",
                 "ESR(config-dhcp-server)# network 192.168.10.0/24",
                 "ESR(config-dhcp-server)# address-range 192.168.10.1-192.168.10.100",
                 "ESR(config-dhcp-server)# excluded-address-range 192.168.10.10",
                 "ESR(config-dhcp-server)# default-router 192.168.10.10",
                 "ESR(config-dhcp-server)# exit"], "ESR · DHCP-сервер"), "cy")),
             col(step(card("Что означает", table(["Команда", "Смысл"], [
                 ["<b>ip dhcp-server</b>", "включить службу"],
                 ["<b>pool DHCP-10</b>", "создать пул с именем"],
                 ["<b>network</b>", "адрес обслуживаемой сети"],
                 ["<b>address-range</b>", "диапазон выдаваемых адресов"],
                 ["<b>excluded-address-range</b>", "не выдавать (адрес самого ESR)"],
                 ["<b>default-router</b>", "шлюз по умолчанию для клиентов"]]), "ye")),
                 step(foot("Дополнительно можно указать DNS-сервер, время аренды и другие опции.", "note"))))
    ), bg="b")

    slide("Настройка DHCP-ретранслятора", sc(
        head("Настройка <em>DHCP-ретранслятора</em>", "Включить relay глобально + указать сервер на интерфейсе клиентов"),
        grow("g2",
             step(card("Пример", cli([
                 "ESR(config)# interface gigabitethernet 1/0/1",
                 "ESR(config-if-gi)# ip address 10.0.0.1/24",
                 "ESR(config)# interface gigabitethernet 1/0/2",
                 "ESR(config-if-gi)# ip address 192.168.0.1/24",
                 "> ESR(config)# ip dhcp-relay",
                 "ESR(config)# interface gigabitethernet 1/0/2",
                 "> ESR(config-if-gi)# ip helper-address 10.0.0.2"], "ESR · DHCP Relay"), "cy")),
             col(_scene_relay_cfg()))
    ), bg="a")

    slide("Проверка DHCP", sc(
        head("Проверка <em>DHCP</em>", "Команды show на ESR"),
        grow("g2",
             col(step(card("Выданные адреса", cli([
                 "> ESR# show ip dhcp binding",
                 "Allocated        MAC address        Binding   Lease expires at",
                 "---------------  -----------------  --------  -----------------------",
                 "! 192.168.1.3      50:46:5d:a5:3f:91  dynamic   Thursday 2014/01/01 12:42:12"], ""), "cy", "1")),
                 step(card("DSCP сообщений сервера", cli(["> ESR# show ip dhcp server dscp", "! DSCP:    32"], ""), "vi", "2"))),
             col(step(card("Настроенные пулы", cli([
                 "> ESR# show ip dhcp server pool lan-pool",
                 "name:                lan-pool",
                 "! network:             192.168.1.0/24",
                 "! address-ranges:      192.168.1.2-192.168.1.254",
                 "default-router:      192.168.1.1",
                 "max lease time:      1:0:0 (day:hour:min)",
                 "default lease time:  0:12:0 (day:hour:min)"], ""), "ye", "3"))))
    ), bg="d")

    slide("Мини-тест: DHCP", sc(
        head("Проверим себя · <em class='y'>DHCP</em>"),
        grow("g2",
             col(step(quiz("Какой IP-адрес источника у DHCPDISCOVER?",
                           ["255.255.255.255", "0.0.0.0", "адрес шлюза", "127.0.0.1"], 1,
                           "У клиента ещё нет адреса — источник 0.0.0.0, назначение 255.255.255.255.")),
                 step(quiz("Какое сообщение клиент шлёт, обнаружив через ARP, что адрес занят?",
                           ["DHCPNAK", "DHCPRELEASE", "DHCPDECLINE", "DHCPOFFER"], 2,
                           "DHCPDECLINE — «нет, спасибо», сервер выдаст другой адрес."))),
             col(step(quiz("Зачем нужен DHCP Relay?",
                           ["Шифровать DHCP-трафик", "Пересылать запросы клиентов к серверу в другой сети",
                            "Хранить таблицу NAT", "Синхронизировать время"], 1,
                           "Широковещание не проходит через маршрутизатор — relay пересылает запрос одноадресно.")),
                 step(quiz("Какое поле заполняет ретранслятор?", ["YIADDR", "CHADDR", "GIADDR", "CIADDR"], 2,
                           "GIADDR — IP relay-агента; по нему сервер выбирает пул."))))
    ), bg="c")


# ======================================================================

def _ws(top, lines):
    """Окно в стиле Wireshark: строка списка + дерево полей с номерами выделений."""
    out = ['<div class="ws"><div class="wsbar"><i></i><i></i><i></i><span>Wireshark · Ethernet</span></div>',
           '<div class="wstop"><b class="wsn">1</b>%s</div><pre class="wsp">' % top]
    for ln in lines:
        if ln.startswith("!"):
            n, rest = ln[1], ln[2:]
            out.append('<span class="wsh"><b class="wsn">%s</b>%s</span>' % (n, rest.replace("<", "&lt;")))
        else:
            out.append('<span>%s</span>' % ln.replace("<", "&lt;"))
    out.append('</pre></div>')
    return "".join(out)


def _scene_fields():
    o = []
    cols = [("DISCOVER", "y"), ("OFFER", "o"), ("REQUEST", "v"), ("ACK", "g")]
    fields = ["IP источника", "IP назначения", "UDP-порты", "YIADDR", "Опция 50", "Опция 54"]
    data = [["0.0.0.0", "10.10.1.1", "0.0.0.0", "10.10.1.1"],
            ["255.255.255.255"] * 4,
            ["68 → 67", "67 → 68", "68 → 67", "67 → 68"],
            ["0.0.0.0", "10.10.1.13", "0.0.0.0", "10.10.1.13"],
            ["—", "—", "10.10.1.13", "—"],
            ["—", "10.10.1.1", "10.10.1.1", "10.10.1.1"]]
    o.append(S.txt(120, 60, "Поле", 17, S.SOFT, 800, "start"))
    for j, (nm, t) in enumerate(cols):
        x = 360 + j * 210
        o.append('<g data-ph="%d">' % (j + 1))
        o.append('<rect x="%d" y="30" width="196" height="44" rx="22" fill="url(#pg)" stroke="%s" stroke-width="2.2" filter="url(#gl)"/>' % (x, S.TONE[t]))
        o.append(S.txt(x + 98, 59, nm, 18, S.TONE[t], 900))
        for i in range(len(fields)):
            y = 100 + i * 66
            o.append(S.box(x, y, 196, 52, S.TONE[t], "rgba(5,18,46,.92)", 9, 1.3))
            o.append(S.txt(x + 98, y + 33, data[i][j], 16, "#fff", 800, mono=True))
        o.append('</g>')
    for i, f in enumerate(fields):
        o.append(S.txt(120, 133 + i * 66, f, 17, "#fff", 800, "start"))
    return scene(S.fig("".join(o), "0 0 1200 500"), [
        "Шесть полей, которые стоит отслеживать в обмене DHCP.",
        "<b>DISCOVER</b>: 0.0.0.0 → 255.255.255.255, порты 68 → 67, адресов ещё нет.",
        "<b>OFFER</b>: источник — сервер 10.10.1.1, в YIADDR — предложенный 10.10.1.13.",
        "<b>REQUEST</b>: снова 0.0.0.0; опция 50 — запрошенный адрес, опция 54 — выбранный сервер.",
        "<b>ACK</b>: сервер подтверждает 10.10.1.13 — клиент настраивает интерфейс.",
    ])


def _scene_relay_problem():
    o = [S.pc(130, 260, "DHCP-клиент", "VLAN 10 · 192.168.10.0/24", 100),
         S.router(600, 250, "Маршрутизатор", "без relay", 120),
         S.server(1060, 250, "DHCP-сервер", "10.0.0.0/24", 120)]
    o.append(S.link(190, 260, 535, 255, S.CY, 3, .6) + S.link(665, 255, 1000, 255, S.CY, 3, .6))
    o.append(S.env(200, 225, 500, 225, "DISCOVER · broadcast", 1, S.YE, False, 220))
    o.append('<g data-ph="2">' + S.txt(600, 160, "✕", 70, S.RD, 900) + S.badge(600, 350, "Широковещание отброшено", S.RD, size=16) + '</g>')
    o.append(S.note(340, 410, ["Broadcast живёт только в своём сегменте:", "маршрутизатор его отбрасывает,",
                               "между VLAN коммутатор его не передаёт."], S.RD, ph=3, w=520))
    return scene(S.fig("".join(o), "0 0 1200 520"), [
        "Клиент и DHCP-сервер находятся в <b>разных сетях</b>.",
        "Клиент шлёт DHCPDISCOVER на широковещательный адрес канального уровня…",
        "…и маршрутизатор его <b>отбрасывает</b>: широковещание не маршрутизируется.",
        "Итог: без специальной службы клиент адрес не получит. Решение — <b>DHCP Relay</b>.",
    ])


def _scene_relay():
    o = [S.pc(110, 270, "Клиент (ПК)", "VLAN 10", 96),
         S.switch(340, 270, "Коммутатор", "VLAN 10", 100),
         S.router(640, 260, "DHCP Relay", "192.168.10.1 · 10.0.0.1", 120),
         S.server(1060, 260, "Центральный", "DHCP-сервер 10.0.0.2", 120)]
    o.append(S.link(160, 270, 290, 270, S.CY, 3, .6) + S.link(390, 270, 575, 265, S.CY, 3, .6)
             + S.link(705, 265, 1000, 260, S.VI, 3, .6))
    o.append('<g data-ph="0">' + S.txt(360, 410, "Подсеть клиента · VLAN 10", 17, S.CY, 800)
             + S.txt(870, 410, "Подсеть DHCP-сервера", 17, S.VI, 800) + '</g>')
    o.append(S.env(160, 225, 560, 225, "DISCOVER · broadcast", 1, S.YE, True, 220))
    o.append(S.mvhdr(640, 80, 640, 80, [("GIADDR", "192.168.10.1", "y"), ("Hops", "0 → 1", "c")], 2, "Relay дописывает", 300))
    o.append(S.env(720, 225, 970, 225, "unicast → 10.0.0.2", 3, S.VI, True, 220))
    o.append(S.badge(1060, 140, "Пул для 192.168.10.0/24", S.GR, ph=4, size=15))
    o.append(S.env(980, 305, 720, 305, "OFFER · unicast", 5, S.OR, True, 190))
    o.append(S.env(560, 305, 170, 305, "OFFER → клиенту", 6, S.OR, True, 190))
    o.append(S.badge(110, 160, "Адрес получен", S.GR, ph=7, size=15))
    return scene(S.fig("".join(o), "0 0 1200 460"), [
        "Клиент в VLAN 10, центральный DHCP-сервер — в другой подсети, между ними <b>DHCP Relay</b>.",
        "Клиент шлёт <b>DISCOVER</b> широковещательно — его ловит интерфейс ретранслятора.",
        "Relay дописывает свой адрес <b>GIADDR = 192.168.10.1</b> и увеличивает Hops.",
        "Запрос уходит серверу <b>одноадресно (unicast)</b>.",
        "Сервер по GIADDR выбирает <b>пул сети 192.168.10.0/24</b>.",
        "OFFER возвращается к ретранслятору…",
        "…и ретранслятор передаёт его клиенту в VLAN 10.",
        "Так же проходят REQUEST и ACK — клиент получил адрес с центрального сервера.",
    ])


def _scene_relay_cfg():
    o = [S.pc(90, 200, "Клиенты", "192.168.0.0/24", 80),
         S.router(420, 190, "ESR", "", 110),
         S.server(760, 190, "DHCP-сервер", "10.0.0.2", 100)]
    o.append(S.link(140, 200, 360, 195, S.CY, 3, .6) + S.link(480, 195, 705, 190, S.VI, 3, .6))
    o.append(S.badge(250, 160, "gi1/0/2 · 192.168.0.1", S.CY, size=13))
    o.append(S.badge(590, 160, "gi1/0/1 · 10.0.0.1", S.VI, size=13))
    o.append(S.badge(420, 330, "ip dhcp-relay  (глобально)", S.YE, ph=1, size=15))
    o.append(S.badge(250, 255, "ip helper-address 10.0.0.2", S.GR, ph=2, size=14))
    o.append(S.env(150, 120, 700, 120, "запрос → 10.0.0.2", 3, S.YE, True, 200))
    return scene(S.fig("".join(o), "0 0 860 380"), [
        "Два интерфейса ESR: к клиентам (gi1/0/2) и к серверу (gi1/0/1).",
        "<b>ip dhcp-relay</b> — включаем ретрансляцию глобально.",
        "<b>ip helper-address</b> — на интерфейсе со стороны клиентов указываем сервер.",
        "Запросы клиентов перенаправляются серверу 10.0.0.2.",
    ])
