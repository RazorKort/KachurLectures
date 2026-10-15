# -*- coding: utf-8 -*-
"""Слайды 72–85: интерфейсы коммутатора — L2, L3, физические с IP, SVI, loopback."""

from _sw_lib import (slide, head, sc, g, grow, col, card, p, li, irow, foot, tags, tag,
                     table, cli, pic, step, scene, task)
import _sw_svg as S


def build():
    slide("Интерфейсы коммутатора", sc(
        head("Интерфейсы <em>коммутатора</em>",
             "Делятся на интерфейсы уровня L2 и интерфейсы уровня L3."),
        grow("g", pic("if_overview"))
    ))

    slide("L2 или L3: в чём разница", sc(
        head("<em>L2</em> или <em class=\"v\">L3</em>: в чём разница",
             "До какого места интерфейс разбирает пришедший кадр."),
        grow("g", col(_scene_l2l3()))
    ))

    slide("Интерфейсы уровня L2", sc(
        head("Интерфейсы уровня <em>L2</em>",
             "Они же «порты коммутатора» (switchport)."),
        grow("g", pic("if_l2"))
    ))

    slide("Функции и состояния порта", sc(
        head("Функции и <em>состояния</em> порта",
             "Три действия и два состояния."),
        grow("g2",
             col(step(card("Что делает порт L2", ''.join([
                 irow("<b>Получение кадра</b> — из провода в буфер порта.", "", "arrow"),
                 irow("<b>Оценка целостности</b> — проверка поля FCS.", "g", "ok"),
                 irow("<b>Отправка кадра</b> — с пересчётом контрольной суммы.", "v", "split"),
             ]) + p("Порт L2 обрабатывает информацию <b>от начала кадра до поля EtherType включительно</b>, "
                    "а также поле FCS."), "cy"))),
             col(step(card("Два состояния", table(
                 ["Состояние", "Когда", "Что значит"],
                 [(["<b>up</b>", "кабель подключён, на том конце работающее устройство",
                    "порт готов передавать данные"], "hi"),
                  ["<b>down</b>", "нет кабеля, нет сигнала или порт выключен административно",
                   "порт не участвует в передаче"]]), "mg")),
                 step(card("Режим по умолчанию", p(
                     "По умолчанию все физические интерфейсы коммутатора находятся в режиме <b>switchport</b>.",
                     "Интерфейсы маршрутизатора, наоборот, по умолчанию работают в режиме "
                     "<b>routerport</b>, то есть как интерфейс L3, но могут быть переведены в switchport."), "lm"))),
             )
    ))

    slide("show interfaces status", sc(
        head("<em>show interfaces status</em>",
             "Состояние всех портов одной командой."),
        grow("g", pic("if_l2_show"))
    ))

    slide("Команды просмотра портов", sc(
        head("Команды <em>просмотра</em> портов",
             "От общей картины к параметрам одного порта."),
        grow("g2",
             col(step(card("Состояние всех портов", cli([
                 "> switch# show interfaces status",
                 "",
                 "                                             Flow Link    Back  Mdix",
                 "Port   Type         Duplex  Speed Neg   ctrl State  Pressure Mode",
                 "------ ------------ ------  ----- ----- ---- ------ -------- ----",
                 "! gi1/0/1 1G-Copper  Full   1000  Enabled Off  Up    Disabled  Off",
                 "gi1/0/2 1G-Copper  Full   1000  Enabled Off  Up    Disabled  Off",
                 "gi1/0/3 1G-Copper    --     --     --    --  Down     --      --",
             ]), "cy"))),
             col(step(card("Параметры одного порта", cli([
                 "> switch# show interfaces GigabitEthernet 1/0/1",
                 "",
                 "gi1/0/1 is up (connected)",
                 "  Hardware is Gigabit Ethernet",
                 "  MAC address is a8:f9:4b:aa:00:01",
                 "  Full-duplex, 1000Mbps, link type is auto",
                 "  Input packets 184920, output packets 97431",
                 "! CRC errors 0, collisions 0",
             ]), "mg")),
                 step(foot("Счётчик <b>CRC errors</b> — тот самый показатель отброшенных по FCS кадров. "
                           "Если он растёт — проверьте кабель и разъёмы.", "note"))),
             )
    ))

    slide("Интерфейсы уровня L3", sc(
        head("Интерфейсы уровня <em>L3</em>",
             "Умеют смотреть в IP-заголовок."),
        grow("g", pic("if_l3"))
    ))

    slide("Функции интерфейса L3", sc(
        head("Функции интерфейса <em>L3</em>",
             "Пять задач, которых нет у порта L2."),
        grow("g2",
             col(step(card("Что умеет интерфейс L3", ''.join([
                 irow("<b>Декапсуляция</b> кадра до уровня L3.", "", "doc"),
                 irow("<b>Фильтрация и отбрасывание</b> трафика посредством ACL.", "v", "shield"),
                 irow("<b>Маршрутизация</b> трафика по таблице маршрутизации.", "g", "net"),
                 irow("<b>Обработка управляющего трафика</b>, предназначенного самому коммутатору.", "y", "gear"),
                 irow("<b>Инкапсуляция</b> трафика L3 для отправки в нужный порт уровня L2.", "r", "arrow"),
             ]), "cy"))),
             col(step(card("Три вида интерфейсов L3", table(
                 ["Вид", "Где живёт", "Для чего"],
                 [["<b>Физический с IP</b>", "обычный порт, переведённый в L3",
                   "точка-точка с маршрутизатором"],
                  ["<b>SVI</b>", "виртуальный, привязан к VLAN",
                   "шлюз для узлов своей VLAN"],
                  ["<b>Loopback</b>", "существует только в памяти",
                   "идентификатор устройства"]]), "mg"))),
             )
    ))

    slide("Физический интерфейс с IP", sc(
        head("Физические интерфейсы с <em>IP-адресами</em>",
             "Когда порт перестаёт быть switchport."),
        grow("g", pic("phys_ip"))
    ))

    slide("Что меняется после IP", sc(
        head("Что меняется после <em>установки IP</em>",
             "Порт начинает вести себя как интерфейс маршрутизатора."),
        grow("g2",
             col(step(card("Новое поведение", li([
                 "отсылает кадры с <b>собственным MAC-адресом</b> в поле Source MAC",
                 "принимает только <b>адресованные ему</b> кадры",
                 "<b>декапсулирует</b> входящие кадры до уровня L3 для принятия решений по маршрутизации",
                 "<b>инкапсулирует</b> исходящие пакеты L3 в кадры L2"]), "cy"))),
             col(step(card("Команды", cli([
                 "switch# configure",
                 "switch(config)# interface gigabitethernet 1/0/24",
                 "> switch(config-if)# no switchport",
                 "> switch(config-if)# ip address 10.0.0.1 /30",
                 "switch(config-if)# exit",
                 "",
                 "switch# show ip interfaces",
             ]), "mg")),
                 step(foot("Возможность установки IP-адреса на физический порт доступна не на всех моделях — "
                           "это признак многоуровневого коммутатора.", "note"))),
             )
    ))

    slide("Интерфейсы SVI", sc(
        head("Интерфейсы <em>SVI</em>",
             "Switching Virtual Interface — виртуальный интерфейс коммутатора."),
        grow("g", pic("svi"))
    ))

    slide("SVI: правила", sc(
        head("<em>SVI</em>: правила работы",
             "Один SVI — одна VLAN."),
        grow("g2",
             col(step(card("Определение", p(
                 "Интерфейсы SVI — это виртуальные интерфейсы, привязанные к определённой виртуальной сети (VLAN).",
                 "Имена интерфейсов совпадают с номером виртуальной сети, например <b>VLAN 10</b> или <b>VLAN 20</b>.",
                 "Через определённый SVI проходит трафик всех портов соответствующей ему VLAN на данном коммутаторе."), "cy")),
                 step(card("Условие состояния UP", p(
                     "Эти интерфейсы активны (находятся в состоянии up) только если в соответствующей VLAN "
                     "есть <b>хотя бы один активный порт</b> — доступа или магистральный."), "lm"))),
             col(step(card("Настройка SVI", cli([
                 "switch# configure",
                 "> switch(config)# vlan 10",
                 "switch(config-vlan)# name IT",
                 "switch(config-vlan)# exit",
                 "> switch(config)# interface vlan 10",
                 "> switch(config-if)# ip address 192.168.10.1 /24",
                 "switch(config-if)# exit",
             ]), "mg")),
                 step(card("Зачем нужен SVI", li([
                     "<b>Шлюз по умолчанию</b> для узлов своей VLAN.",
                     "<b>Управление коммутатором</b> по SSH или Web.",
                     "<b>Сетевые сервисы</b>: DHCP relay, VRRP, маршрутизация между VLAN."], "lm"), "am"))),
             )
    ))

    slide("Сцена: когда SVI поднимается", sc(
        head("Когда <em>SVI</em> поднимается",
             "Условие UP проверяется по активным портам VLAN."),
        grow("g", col(_scene_svi()))
    ))

    slide("Интерфейсы loopback", sc(
        head("Интерфейсы <em>обратной петли</em>",
             "Loopback — «сеть в себе» с префиксом /32."),
        grow("g2",
             col(step(card("Свойства", li([
                 "создаются <b>пользователем</b> и всегда находятся в состоянии <b>up</b>",
                 "IP-адреса имеют длину префикса <b>/32</b>, то есть являются «сетью в себе»",
                 "не зависят от состояния физических портов"]), "cy")),
                 step(card("Где применяются", li([
                     "идентификатор устройства в протоколах динамической маршрутизации (Router ID в OSPF)",
                     "интерфейсы тестовых сетей",
                     "адрес для управления, который не пропадёт при обрыве одного кабеля"], "lm"), "lm"))),
             col(step(card("Команды", cli([
                 "switch# configure",
                 "> switch(config)# interface loopback 1",
                 "> switch(config-if)# ip address 10.255.255.1 /32",
                 "switch(config-if)# exit",
                 "",
                 "> switch# show ip interfaces",
                 "",
                 "IP Address     I/F        Type      Status",
                 "-------------- ---------- --------- --------",
                 "! 10.255.255.1/32 loopback1  Static    Valid",
                 "192.168.10.1/24 vlan 10    Static    Valid",
             ]), "mg"))),
             )
    ))

    slide("Сводка типов интерфейсов", sc(
        head("Сводка <em>типов интерфейсов</em>",
             "Одна таблица на весь блок."),
        grow("g",
             col(step(table(
                 ["Интерфейс", "Уровень", "Есть ли IP", "Состояние up, если", "Зачем"],
                 [["<b>switchport</b> (физический)", "L2", "нет",
                   "подключён кабель и есть сигнал", "приём и пересылка кадров"],
                  ["<b>физический с IP</b>", "L3", "да",
                   "подключён кабель и есть сигнал", "стык точка-точка"],
                  (["<b>SVI</b> (interface vlan N)", "L3", "да",
                    "в VLAN есть хотя бы один активный порт", "шлюз VLAN и управление"], "hi"),
                  ["<b>loopback</b>", "L3", "да, /32",
                   "<b>всегда</b>", "идентификатор устройства"]])),
                 step(foot("Граница широковещательного домена — любой из интерфейсов уровня L3, "
                           "потому что именно на нём кадр декапсулируется до пакета.", "ok"))),
             )
    ))


# ======================================================================
#  СЦЕНЫ
# ======================================================================

def _scene_l2l3():
    o = []
    o.append(S.frame_strip(80, 90, [("Preamble", 4, S.SOFT), ("DMAC", 5, S.CY), ("SMAC", 5, S.MG),
                                    ("EtherType", 4, S.AM), ("IP-заголовок", 9, S.LM),
                                    ("Данные", 10, S.SOFT), ("FCS", 3, S.RD)],
                           w=1040, h=52, cap="Пришедший кадр"))
    # граница чтения L2
    o.append('<g data-ph="1">')
    o.append('<rect x="78" y="84" width="630" height="64" rx="10" fill="none" stroke="%s" stroke-width="3.4" filter="url(#gl)"/>' % S.CY)
    o.append(S.txt(392, 174, "Порт L2 читает до EtherType включительно — и ещё FCS", 14, S.CY, 800))
    o.append("</g>")
    o.append('<g data-ph="2">')
    o.append('<rect x="78" y="84" width="1044" height="64" rx="10" fill="none" stroke="%s" stroke-width="3.4" filter="url(#gl)"/>' % S.MG)
    o.append(S.txt(600, 200, "Интерфейс L3 идёт глубже: читает Source IP и Destination IP", 14, S.MG, 800))
    o.append("</g>")

    o.append('<g data-ph="3">')
    o.append(S.box(90, 250, 500, 250, S.CY))
    o.append(S.txt(340, 284, "Интерфейс L2 — порт коммутатора", 17, S.CY, 800))
    for i, t in enumerate(["Смотрит на DMAC и SMAC",
                           "Ищет в таблице коммутации",
                           "Выбирает выходной порт",
                           "О сетях и IP ничего не знает",
                           "Называется switchport"]):
        o.append(S.txt(118, 322 + i * 34, "• " + t, 14, S.SOFT, 600, "start"))
    o.append("</g>")

    o.append('<g data-ph="4">')
    o.append(S.box(620, 250, 500, 250, S.MG))
    o.append(S.txt(870, 284, "Интерфейс L3", 17, S.MG, 800))
    for i, t in enumerate(["Декапсулирует кадр до пакета",
                           "Читает Source IP и Destination IP",
                           "Применяет ACL и маршрутизацию",
                           "Принимает управляющий трафик",
                           "Здесь заканчивается broadcast-домен"]):
        o.append(S.txt(648, 322 + i * 34, "• " + t, 14, S.SOFT, 600, "start"))
    o.append("</g>")

    caps = ["Кадр пришёл на интерфейс",
            "Граница чтения у порта L2",
            "Граница чтения у интерфейса L3",
            "Что делает интерфейс L2",
            "Что делает интерфейс L3"]
    return scene(S.fig("".join(o)), caps)


def _scene_svi():
    o = []
    names = ["1/0/1", "1/0/2", "1/0/3", "1/0/4", "1/0/5", "1/0/6", "1/0/7", "1/0/8"]
    sw, pts = S.switch(300, 290, 600, 86, 8, "Коммутатор L3", names=names)
    o.append(sw)
    o.append('<rect x="316" y="358" width="280" height="4" rx="2" fill="%s" opacity=".8"/>' % S.CY)
    o.append(S.txt(456, 392, "VLAN 10 · порты 1/0/1–1/0/4", 13, S.CY, 800))
    o.append('<rect x="610" y="358" width="280" height="4" rx="2" fill="%s" opacity=".8"/>' % S.MG)
    o.append(S.txt(750, 392, "VLAN 20 · порты 1/0/5–1/0/8", 13, S.MG, 800))

    o.append(S.box(260, 110, 320, 90, S.CY))
    o.append(S.txt(420, 142, "SVI VLAN 10", 17, S.CY, 800))
    o.append(S.txt(420, 170, "192.168.10.1/24", 14, S.INK, 700, mono=True))
    o.append(S.box(620, 110, 320, 90, S.MG))
    o.append(S.txt(780, 142, "SVI VLAN 20", 17, S.MG, 800))
    o.append(S.txt(780, 170, "192.168.20.1/24", 14, S.INK, 700, mono=True))
    o.append(S.link(420, 200, 420, 290, S.CY, 2.6, .5, dash=True))
    o.append(S.link(780, 200, 780, 290, S.MG, 2.6, .5, dash=True))

    o.append(S.badge(420, 232, "SVI DOWN", S.RD, ph=0, only=True))
    o.append(S.badge(780, 232, "SVI DOWN", S.RD, ph=0, only=True))
    o.append(S.note(300, 440, ["Ни один порт не подключён: оба SVI в состоянии down,",
                               "хотя IP-адреса на них уже настроены."], S.RD, ph=0, w=600, only=True))

    o.append('<g data-ph="1"><circle cx="%g" cy="%g" r="16" fill="rgba(157,252,90,.3)" stroke="%s" stroke-width="2.4"/></g>'
             % (pts[0][0], pts[0][1] + 10, S.LM))
    o.append(S.badge(420, 232, "SVI UP", S.LM, ph=1))
    o.append(S.badge(780, 232, "SVI DOWN", S.RD, ph=1, only=True))
    o.append(S.note(300, 440, ["В VLAN 10 появился один активный порт 1/0/1 — этого достаточно:",
                               "SVI VLAN 10 перешёл в состояние up и стал шлюзом для своей сети."], S.LM, ph=1, w=640, only=True))

    o.append('<g data-ph="2"><circle cx="%g" cy="%g" r="16" fill="rgba(196,92,255,.3)" stroke="%s" stroke-width="2.4"/></g>'
             % (pts[4][0], pts[4][1] + 10, S.MG))
    o.append(S.badge(780, 232, "SVI UP", S.LM, ph=2))
    o.append(S.note(300, 440, ["В VLAN 20 тоже появился активный порт — оба шлюза работают."], S.LM, ph=2, w=640, only=True))

    o.append(S.pc(120, 420, "ПК VLAN 10", "192.168.10.100", S.CY))
    o.append(S.arrow(180, 450, 320, 400, S.CY, 3, "ah", ph=3))
    o.append(S.arrow(420, 290, 420, 210, S.CY, 3, "ah", ph=3))
    o.append(S.box(980, 400, 200, 80, S.LM))
    o.append(S.txt(1080, 432, "Другая сеть", 14, S.LM, 800))
    o.append(S.txt(1080, 456, "например 8.8.8.8", 12, S.SOFT, 600))
    o.append(S.arrow(580, 155, 980, 420, S.LM, 3.2, "ahg", ph=4))
    o.append(S.note(300, 500, ["Пакет уходит на шлюз 192.168.10.1 (SVI VLAN 10),",
                               "там декапсулируется и маршрутизируется дальше."], S.LM, ph=4, w=640, only=True))

    caps = ["Активных портов нет — оба SVI в down",
            "Поднялся порт 1/0/1 → SVI VLAN 10 стал up",
            "Поднялся порт 1/0/5 → SVI VLAN 20 стал up",
            "ПК отправляет трафик на свой шлюз",
            "Шлюз маршрутизирует пакет в другую сеть"]
    return scene(S.fig("".join(o)), caps)
