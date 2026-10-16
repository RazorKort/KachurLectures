# -*- coding: utf-8 -*-
"""Блок 7: Destination NAT и проброс портов, настройка SNAT/DNAT на ESR, проверка NAT, Proxy ARP."""

from _sw_lib import grow, g, col, card, p, li, foot, tags, tag, table, cli, step, scene, task, quiz
from _nat_lib import slide, sc, head, pill, kv, big
import _nat_svg as S


def build():
    slide("Destination NAT (DNAT)", sc(
        head("Destination NAT <em class='v'>(DNAT)</em> — входящая трансляция",
             "Запросы на публичный адрес перенаправляются на ресурс внутри локальной сети"),
        grow("g", col(_scene_dnat()))
    ), bg="a")

    slide("DNAT: пять этапов", sc(
        head("Принцип работы <em class='v'>DNAT</em>"),
        grow("g", col(
            pill("1", "Входящий запрос", "из внешней сети на публичный адрес устройства с DNAT", "v", True),
            pill("2", "Перехват запроса", "адрес назначения совпадает с общедоступным IP", "o", True),
            pill("3", "Преобразование назначения", "по правилам: публичный → локальный адрес (иногда и порт)", "y", True),
            pill("4", "Перенаправление внутрь", "запрос доставлен целевому серверу в LAN", "g", True),
            pill("5", "Ответное сообщение", "обратно: локальный источник → публичный, ответ уходит внешнему клиенту", "c", True))),
        step(foot("Внутренние адреса не раскрываются: веб, почта, VPN доступны извне, а сеть изолирована.", "ok"))
    ), bg="d")

    slide("Port Forwarding", sc(
        head("Проброс портов — <em>Port Forwarding</em>", "Один публичный адрес, разные порты — разные серверы"),
        grow("g", col(_scene_portfwd()))
    ), bg="b")

    slide("Задача: проброс портов", sc(
        head("Задача · <em class='y'>куда уйдёт запрос?</em>"),
        grow("g2",
             step(card("Правила DNAT на 203.0.113.1", table(["Внешний порт", "Внутренний адрес:порт"], [
                 ["<span class='mono'>:80</span>", "<span class='mono'>10.10.10.2:80</span> — веб"],
                 ["<span class='mono'>:25</span>", "<span class='mono'>10.10.10.3:25</span> — почта"],
                 ["<span class='mono'>:2222</span>", "<span class='mono'>10.10.10.4:22</span> — SSH"]]), "vi", "⇄")),
             col(step(task("t-d1", "Запрос на <b class='mono'>203.0.113.1:25</b>. Какой внутренний адрес получит пакет?",
                           "10.10.10.3", "Порт 25 → почтовый сервер <b>10.10.10.3</b>.", "IP-адрес")),
                 step(task("t-d2", "На какой порт сервера 10.10.10.4 придёт запрос к <b class='mono'>203.0.113.1:2222</b>?",
                           "22", "DNAT меняет и порт: 2222 → <b>22</b> (SSH).", "порт")),
                 step(task("t-d3", "Запрос на <b class='mono'>203.0.113.1:443</b> — дойдёт ли он до какого-нибудь сервера? (да/нет)",
                           "нет", "Правила для 443 нет — пакет не подходит под DNAT и <b>отбрасывается</b>.", "да / нет"))))
    ), bg="c")

    # -------- настройка SNAT
    slide("Настройка SNAT: задача", sc(
        head("Настройка <em class='y'>Source NAT</em> на ESR",
             "Доступ сети 192.168.1.0/24 в публичную сеть через адрес 1.1.1.1"),
        grow("g", col(_scene_cfg_snat()))
    ), bg="a")

    slide("SNAT: зоны и интерфейсы", sc(
        head("SNAT · шаги 1–3: <em>зоны, интерфейсы, профили</em>"),
        grow("g2",
             col(step(card("1. Зоны TRUST и UNTRUST", cli([
                 "ESR# configure",
                 "> ESR(config)# security zone UNTRUST",
                 "ESR(config-zone)# exit",
                 "> ESR(config)# security zone TRUST",
                 "ESR(config-zone)# exit"], ""), "ye", "1")),
                 step(card("3. Профили адресов", cli([
                     "> ESR(config)# object-group network LOCAL_NET",
                     "ESR(config-object-group-network)# ip address-range 192.168.1.1-192.168.1.254",
                     "ESR(config-object-group-network)# exit",
                     "> ESR(config)# object-group network WAN_NET",
                     "ESR(config-object-group-network)# ip address-range 1.1.1.1",
                     "ESR(config-object-group-network)# exit"], ""), "vi", "3"))),
             col(step(card("2. Зоны и адреса на интерфейсах", cli([
                 "> ESR(config)# interface gigabitethernet 1/0/1",
                 "ESR(config-if-gi)# security-zone TRUST",
                 "ESR(config-if-gi)# ip address 192.168.1.1/24",
                 "ESR(config-if-gi)# exit",
                 "> ESR(config)# interface tengigabitethernet 1/0/2",
                 "ESR(config-if-te)# ip address 1.1.1.1/29",
                 "ESR(config-if-te)# security-zone UNTRUST",
                 "ESR(config-if-te)# exit"], ""), "or", "2")),
                 step(foot("TRUST — сегмент LAN, UNTRUST — сегмент WAN.", "note"))))
    ), bg="d")

    slide("SNAT: правила и пул", sc(
        head("SNAT · шаги 4–7: <em>правила, пул, ruleset, маршрут</em>"),
        grow("g2",
             col(step(card("4. Пара зон TRUST → UNTRUST", cli([
                 "> ESR(config)# security zone-pair TRUST UNTRUST",
                 "ESR(config-zone-pair)# rule 1",
                 "ESR(config-zone-pair-rule)# match source-address LOCAL_NET",
                 "ESR(config-zone-pair-rule)# action permit",
                 "ESR(config-zone-pair-rule)# enable",
                 "ESR(config-zone-pair-rule)# exit"], ""), "ye", "4")),
                 step(card("5. Пул публичных адресов", cli([
                     "> ESR(config)# nat source",
                     "ESR(config-snat)# pool WAN_ADDRESS",
                     "ESR(config-snat-pool)# ip address-range 1.1.1.1",
                     "ESR(config-snat-pool)# exit"], ""), "or", "5"))),
             col(step(card("6. Набор правил SNAT", cli([
                 "> ESR(config-snat)# ruleset SNAT",
                 "ESR(config-snat-ruleset)# to zone UNTRUST",
                 "ESR(config-snat-ruleset)# rule 1",
                 "ESR(config-snat-rule)# match source-address LOCAL_NET",
                 "! ESR(config-snat-rule)# action source-nat pool WAN_ADDRESS",
                 "ESR(config-snat-rule)# enable",
                 "ESR(config-snat-rule)# exit"], ""), "vi", "6")),
                 step(card("7. Маршрут по умолчанию", cli(["> ESR(config)# ip route 0.0.0.0/0 1.1.1.254"], ""), "lm", "7")),
                 step(foot("<b>persistent</b> — один внутренний адрес всегда в один внешний (нужно для STUN).", "note"))))
    ), bg="b")

    # -------- настройка DNAT
    slide("Настройка DNAT: задача", sc(
        head("Настройка <em class='v'>Destination NAT</em> на ESR",
             "FTP-сервер 192.168.1.100 должен быть доступен извне по адресу 1.1.1.1, порт 21"),
        grow("g", col(_scene_cfg_dnat()))
    ), bg="c")

    slide("DNAT: профили", sc(
        head("DNAT · шаги 1–3: <em>зоны, интерфейсы, профили</em>"),
        grow("g2",
             col(step(card("1–2. Зоны и интерфейсы", cli([
                 "ESR(config)# security zone UNTRUST",
                 "ESR(config)# security zone TRUST",
                 "ESR(config)# interface gigabitethernet 1/0/1",
                 "ESR(config-if-gi)# security-zone TRUST",
                 "ESR(config-if-gi)# ip address 192.168.1.1/24",
                 "ESR(config)# interface tengigabitethernet 1/0/2",
                 "ESR(config-if-te)# ip address 1.1.1.1/29",
                 "ESR(config-if-te)# security-zone UNTRUST"], "так же, как для SNAT"), "ye", "1"))),
             col(step(card("3. Профили адресов и портов", cli([
                 "> ESR(config)# object-group network WAN_IP",
                 "ESR(config-object-group-network)# ip address 1.1.1.1",
                 "> ESR(config)# object-group network SERVER_IP",
                 "ESR(config-object-group-network)# ip address 192.168.1.100",
                 "> ESR(config)# object-group service FTP_PORT",
                 "ESR(config-object-group-service)# port 21"], ""), "vi", "3")),
                 step(table(["Профиль", "Что хранит"], [["WAN_IP", "адрес публичной сети"],
                                                        ["SERVER_IP", "адрес сервера в LAN"],
                                                        ["FTP_PORT", "порт 21"]]))))
    ), bg="d")

    slide("DNAT: правила", sc(
        head("DNAT · шаги 5–6: <em>ruleset и пара зон</em>"),
        grow("g2",
             step(card("5. Набор правил DNAT", cli([
                 "> ESR(config-dnat)# ruleset DNAT",
                 "ESR(config-dnat-ruleset)# from zone UNTRUST",
                 "ESR(config-dnat-ruleset)# rule 1",
                 "ESR(config-dnat-rule)# match destination-address WAN_IP",
                 "ESR(config-dnat-rule)# match protocol tcp",
                 "ESR(config-dnat-rule)# match destination-port FTP_PORT",
                 "! ESR(config-dnat-rule)# action destination-nat pool SERVER_POOL",
                 "ESR(config-dnat-rule)# enable"], ""), "vi", "5")),
             col(step(card("6. Пара зон UNTRUST → TRUST", cli([
                 "> ESR(config)# security zone-pair UNTRUST TRUST",
                 "ESR(config-zone-pair)# rule 1",
                 "ESR(config-zone-pair-rule)# match destination-address SERVER_IP",
                 "! ESR(config-zone-pair-rule)# match destination-nat",
                 "ESR(config-zone-pair-rule)# action permit",
                 "ESR(config-zone-pair-rule)# enable"], ""), "or", "6")),
                 step(foot("Пропускается только трафик к SERVER_IP, <b>прошедший DNAT</b>. "
                           "Пул SERVER_POOL (адрес и порт сервера) создаётся в разделе <b>nat destination</b>.", "note"))))
    ), bg="a")

    slide("Проверка NAT", sc(
        head("Проверка <em>NAT</em>", "Команды show ip nat …"),
        grow("g2",
             col(step(card("Активные трансляции", cli([
                 "> ESR# show ip nat translations",
                 "Prot  Inside source      Inside dest.     Outside source     Outside dest.",
                 "----  -----------------  ---------------  -----------------  --------------",
                 "! tcp   203.0.113.2:54825  192.0.2.100:80   203.0.113.2:54825  203.0.2.1:80"], ""), "cy", "1")),
                 step(p("Статические трансляции присутствуют всегда; во время активного сеанса видно и адрес внешнего устройства."))),
             col(step(card("Пулы", cli(["> ESR# show ip nat destination pools",
                                         "Name         IP           Port  Description",
                                         "! SERVER_POOL  192.0.2.100  80    --"], ""), "ye", "2")),
                 step(card("Наборы правил", cli(["> ESR# show ip nat destination rulesets",
                                                  "Name  From            Description",
                                                  "! DNAT  zone 'UNTRUST'  --"], ""), "vi", "3"))))
    ), bg="b")

    # -------- Proxy ARP
    slide("NAT Proxy ARP", sc(
        head("NAT <em>Proxy ARP</em>", "Маршрутизатор отвечает на ARP-запросы за узел из другого сегмента"),
        grow("g", col(_scene_proxy_arp()))
    ), bg="d")

    slide("Proxy ARP: суть и проверка", sc(
        head("Proxy ARP: <em>суть и проверка</em>"),
        grow("g2",
             step(card("Принцип", p(
                 "Маршрутизатор с несколькими интерфейсами (физическими или виртуальными: туннель, VLAN-сабинтерфейс) "
                 "отвечает на ARP-запросы в одном сегменте <b>ARP-ответами узла из другого сегмента</b>.",
                 "Узлы первой сети считают, что этот узел рядом, и шлют ему трафик <b>локально</b> — без MAC шлюза. "
                 "Маршрутизатор «слышит» трафик для транслируемого MAC и передаёт его в другой сегмент.",
                 "Для NAT это помогает пакетам, вернувшимся из внешней сети, найти MAC назначения."), "cy", "i")),
             col(step(card("Проверка", cli([
                 "> vESR-2# show ip nat proxy-arp",
                 "Interface    IP address range",
                 "-----------  --------------------------",
                 "! gi1/0/1      100.0.1.100-100.0.1.249"], ""), "ye", "✓")),
                 step(foot("Адреса пула NAT 100.0.1.100–249 «живут» на gi1/0/1: на ARP о них отвечает маршрутизатор.", "note"))))
    ), bg="a")


# ======================================================================

def _scene_dnat():
    o = [S.router(110, 240, "R1", "198.51.100.1", 90), S.cloud(400, 230, "Интернет", 1.0),
         S.router(720, 240, "R2 · DNAT", "", 110), S.server(1080, 240, "Сервер", "10.10.10.2", 100)]
    o.append(S.link(155, 240, 310, 235, S.CY, 3, .5) + S.link(490, 235, 660, 240, S.CY, 3, .5)
             + S.link(780, 240, 1025, 240, S.CY, 3, .5))
    o.append(S.badge(600, 280, "203.0.113.1", S.OR, size=13) + S.badge(870, 280, "10.10.10.1", S.CY, size=13))
    o.append(S.mvhdr(250, 330, 480, 330, [("SrcIP", "198.51.100.1:53314", "c"), ("DstIP", "203.0.113.1:80", "o")], 1, "Запрос из Интернета", 320, False))
    o.append('<g data-ph="2">' + S.box(580, 40, 280, 100, S.VI, "rgba(5,18,46,.96)", 12, 2)
             + S.txt(720, 66, "Таблица правил", 16, S.VI, 900)
             + S.txt(650, 92, "outside destination", 12, S.SOFT, 700) + S.txt(800, 92, "IP", 12, S.SOFT, 700)
             + S.txt(650, 120, "203.0.113.1:80", 14, S.OR, 800, mono=True) + S.txt(800, 120, "10.10.10.2:80", 14, S.YE, 800, mono=True)
             + '</g>')
    o.append(S.mvhdr(770, 330, 960, 330, [("SrcIP", "198.51.100.1:53314", "c"), ("DstIP", "10.10.10.2:80", "y")], 3, "После DNAT", 320, False))
    o.append(S.env(1030, 200, 160, 200, "ответ: src 203.0.113.1:80", 4, S.GR, True, 260))
    return scene(S.fig("".join(o), "0 0 1200 480"), [
        "Клиент R1 (198.51.100.1) в Интернете, сервер 10.10.10.2 спрятан за R2 с DNAT.",
        "Запрос на публичный <b>203.0.113.1:80</b>.",
        "R2 проверяет <b>таблицу правил</b>: 203.0.113.1:80 → 10.10.10.2:80.",
        "Адрес <b>назначения</b> заменён — запрос доставлен серверу 10.10.10.2.",
        "Ответ: R2 делает обратную замену источника на 203.0.113.1 — клиент не знает о внутреннем адресе.",
    ])


def _scene_portfwd():
    o = [S.pc(100, 250, "Клиент", "198.51.100.9", 90), S.router(450, 240, "NAT", "203.0.113.1", 110)]
    srv = [(130, "Веб", "10.10.10.2", ":80", "y"), (260, "Почта", "10.10.10.3", ":25", "o"), (390, "SSH", "10.10.10.4", ":22", "v")]
    for (y, nm, ip, pt, t) in srv:
        o.append(S.server(1050, y, nm, ip + pt, 70) + S.link(505, 240, 1010, y, S.TONE[t], 2.5, .55))
    o.append(S.link(145, 250, 390, 245, S.CY, 3, .5))
    for i, (y, nm, ip, pt, t) in enumerate(srv):
        ext = {":22": ":2222"}.get(pt, pt)
        o.append(S.env(170, 210, 390, 210, "→ 203.0.113.1" + ext, 1 + i * 2, S.TONE[t], True, 210))
        o.append(S.env(520, 240, 960, y - 30, ip + pt, 2 + i * 2, S.TONE[t], True, 170))
    return scene(S.fig("".join(o), "0 0 1200 480"), [
        "За одним публичным адресом 203.0.113.1 — три сервера.",
        "Запрос на порт <b>80</b>…", "…уходит на веб-сервер 10.10.10.2:80.",
        "Запрос на порт <b>25</b>…", "…уходит на почтовый сервер 10.10.10.3:25.",
        "Запрос на порт <b>2222</b>…", "…уходит на SSH 10.10.10.4:<b>22</b> — порт тоже преобразован.",
    ])


def _scene_cfg_snat():
    o = [S.pc(120, 230, "LAN", "192.168.1.0/24", 90), S.router(520, 220, "ESR", "SNAT", 120),
         S.cloud(900, 210, "Интернет", 1.0)]
    o.append(S.link(170, 230, 455, 225, S.GR, 3, .6) + S.link(585, 225, 810, 215, S.RD, 3, .6))
    o.append(S.badge(310, 280, "gi1/0/1 · 192.168.1.1/24", S.GR, size=14))
    o.append(S.badge(700, 280, "te1/0/2 · 1.1.1.1/29", S.RD, size=14))
    steps = [("1", "Зоны TRUST / UNTRUST", "y"), ("2", "Зоны и IP на интерфейсах", "o"), ("3", "object-group LOCAL_NET, WAN_NET", "v"),
             ("4", "zone-pair TRUST → UNTRUST", "g"), ("5", "nat source · pool WAN_ADDRESS", "c"),
             ("6", "ruleset SNAT · action source-nat", "y"), ("7", "ip route 0.0.0.0/0 1.1.1.254", "o")]
    for i, (n, t, tone) in enumerate(steps):
        x = 40 + (i % 4) * 285
        y = 340 + (i // 4) * 60
        o.append(S.chip(x, y, n, t, tone, 270, i + 1))
    o.append('<g data-ph="1"><rect x="30" y="120" width="360" height="200" rx="14" fill="none" stroke="%s" stroke-dasharray="8 6"/>'
             '%s</g>' % (S.GR, S.txt(50, 145, "TRUST", 16, S.GR, 900, "start")))
    o.append('<g data-ph="1"><rect x="650" y="120" width="520" height="200" rx="14" fill="none" stroke="%s" stroke-dasharray="8 6"/>'
             '%s</g>' % (S.RD, S.txt(1150, 145, "UNTRUST", 16, S.RD, 900, "end")))
    return scene(S.fig("".join(o), "0 0 1200 470"), [
        "Задача: пользователи 192.168.1.0/24 выходят в публичную сеть через 1.1.1.1.",
        "<b>1</b> Создаём зоны: TRUST (LAN) и UNTRUST (WAN).",
        "<b>2</b> Назначаем зоны и IP-адреса интерфейсам.",
        "<b>3</b> Профили адресов: LOCAL_NET — кому можно в Интернет, WAN_NET — публичный адрес.",
        "<b>4</b> Пара зон TRUST → UNTRUST: разрешаем трафик от LOCAL_NET.",
        "<b>5</b> Сервис SNAT: пул WAN_ADDRESS = 1.1.1.1.",
        "<b>6</b> Набор правил SNAT: в зону UNTRUST, источник LOCAL_NET → source-nat.",
        "<b>7</b> Маршрут по умолчанию через шлюз WAN-сети 1.1.1.254.",
    ])


def _scene_cfg_dnat():
    o = [S.cloud(140, 210, "Интернет", 1.0), S.router(520, 220, "ESR", "DNAT", 120),
         S.server(950, 220, "FTP-сервер", "192.168.1.100", 110)]
    o.append(S.link(230, 215, 455, 220, S.RD, 3, .6) + S.link(585, 220, 890, 220, S.GR, 3, .6))
    o.append(S.badge(340, 280, "1.1.1.1 : 21", S.OR, size=15))
    o.append(S.env(230, 170, 450, 170, "dst 1.1.1.1:21", 1, S.OR, True, 170))
    o.append(S.badge(520, 90, "match WAN_IP · tcp · FTP_PORT", S.VI, ph=2, size=15))
    o.append(S.env(590, 170, 880, 170, "dst 192.168.1.100:21", 3, S.YE, True, 220))
    o.append(S.badge(740, 300, "zone-pair UNTRUST→TRUST: match destination-nat", S.GR, ph=4, size=14))
    return scene(S.fig("".join(o), "0 0 1200 380"), [
        "Сервер 192.168.1.100 в зоне TRUST, клиенты — в Интернете (UNTRUST).",
        "Клиент подключается к <b>1.1.1.1:21</b>.",
        "ESR проверяет правило: адрес WAN_IP, протокол tcp, порт FTP_PORT.",
        "Назначение заменено на <b>192.168.1.100:21</b>.",
        "Пара зон пропускает только трафик, прошедший DNAT, к SERVER_IP.",
    ])


def _scene_proxy_arp():
    o = [S.pc(120, 230, "Узел A", "100.0.1.10", 90), S.router(600, 220, "Маршрутизатор", "Proxy ARP · gi1/0/1", 120),
         S.pc(1080, 230, "Узел B", "100.0.1.150 (за NAT)", 90)]
    o.append('<rect x="20" y="110" width="470" height="230" rx="14" fill="none" stroke="#5fb8ff" stroke-dasharray="7 6"/>')
    o.append(S.txt(40, 136, "Сегмент 1", 15, S.CY, 800, "start"))
    o.append('<rect x="710" y="110" width="470" height="230" rx="14" fill="none" stroke="#b077ff" stroke-dasharray="7 6"/>')
    o.append(S.txt(1160, 136, "Сегмент 2", 15, S.VI, 800, "end"))
    o.append(S.link(170, 230, 535, 225, S.CY, 3, .5) + S.link(665, 225, 1030, 230, S.VI, 3, .5))
    o.append(S.env(180, 190, 520, 190, "ARP: кто 100.0.1.150?", 1, S.BL, True, 220))
    o.append(S.env(520, 270, 180, 270, "ARP-ответ: MAC маршрутизатора", 2, S.YE, True, 290))
    o.append(S.badge(120, 400, "A считает B соседом", S.YE, ph=2, size=15))
    o.append(S.env(180, 190, 520, 190, "кадр для 100.0.1.150", 3, S.GR, True, 220))
    o.append(S.env(680, 190, 1010, 190, "передан в сегмент 2", 4, S.GR, True, 210))
    return scene(S.fig("".join(o), "0 0 1200 460"), [
        "Узлы A и B в разных канальных сегментах, между ними маршрутизатор.",
        "A шлёт ARP-запрос: «у кого 100.0.1.150?» — B в другом сегменте его не услышит.",
        "Маршрутизатор отвечает <b>за B</b> своим MAC-адресом.",
        "A отправляет кадр «локально» — на MAC маршрутизатора.",
        "Маршрутизатор передаёт трафик узлу B в другой сегмент.",
    ])
