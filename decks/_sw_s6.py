# -*- coding: utf-8 -*-
"""Слайды 104–125: режимы работы портов — access, trunk, native VLAN, general, Q-in-Q, MAC-based."""

from _sw_lib import (slide, head, sc, g, grow, col, card, p, li, irow, foot, tags, tag,
                     table, cli, pic, step, scene, task, quiz)
import _sw_svg as S


def build():
    slide("Режимы работы портов", sc(
        head("Режимы работы <em>портов</em>",
             "Порт коммутатора может работать в четырёх режимах."),
        grow("g", pic("port_modes"))
    ))

    slide("Четыре режима порта", sc(
        head("Четыре <em>режима</em> порта",
             "Что каждый из них принимает на входе."),
        grow("g",
             col(step(table(
                 ["Режим", "Что принимает на входе", "Сколько VLAN", "К чему подключается"],
                 [(["<b>access</b> — интерфейс доступа",
                    "только <b>нетегированный</b> трафик",
                    "одна", "оконечные устройства: ПК, принтер, камера"], "hi"),
                  ["<b>trunk</b> — магистральный",
                   "только <b>тегированный</b>, кроме одной native VLAN",
                   "много", "другие коммутаторы и маршрутизаторы"],
                  ["<b>general</b> — полная поддержка 802.1Q",
                   "и <b>тегированный</b>, и <b>нетегированный</b>",
                   "много", "IP-телефоны, точки доступа Wi-Fi"],
                  ["<b>customer</b> — Q-in-Q",
                   "трафик клиента с его собственными тегами",
                   "много", "сети провайдера"]])),
                 step(foot("По умолчанию все порты коммутатора работают в режиме <b>access в VLAN 1</b>."))),
             )
    ))

    # ------------------------------------------------- ACCESS
    slide("Порты доступа", sc(
        head("<em>Порты доступа</em> (access)",
             "Порты, посредством которых оконечные устройства получают доступ в сеть."),
        grow("g2",
             col(step(card("Четыре правила порта доступа", ''.join([
                 irow("<b>1.</b> На входе обрабатывает только <b>нетегированный</b> трафик. "
                      "При поступлении тегированного кадра он будет отброшен.", "", "no"),
                 irow("<b>2.</b> На входе кадр <b>тегируется</b> меткой VLAN, к которой относится порт.", "v", "tag"),
                 irow("<b>3.</b> На выход пропускаются только кадры, тегированные меткой своей VLAN.", "g", "ok"),
                 irow("<b>4.</b> На выходе метка <b>снимается</b>, и устройство получает кадр без тега.", "y", "arrow"),
             ]), "cy"))),
             col(step(card("Почему именно так", p(
                 "Сами оконечные устройства <b>не поддерживают протокол 802.1Q по умолчанию</b> "
                 "и отбрасывают тегированные кадры. Это и обусловливает правила работы порта доступа."), "mg")),
                 step(card("Где видно в выводе", p(
                     "Порты доступа в выводах команды <b>show vlan</b> чаще указываются "
                     "в столбце <b>UnTagged Ports</b>.") +
                     cli([
                         "> switch# show interfaces switchport gigabitethernet 1/0/1",
                         "",
                         "Port : gi1/0/1",
                         "! Port Mode: Access",
                         "Gvrp Status: disabled",
                         "Ingress Filtering: true",
                         "Acceptable Frame Type: admitAll",
                     ]), "lm"))),
             )
    ))

    slide("Сцена: работа порта доступа", sc(
        head("Сцена: <em>работа порта доступа</em>",
             "Вход и выход кадра на порту access VLAN 10."),
        grow("g", col(_scene_access()))
    ))

    slide("Назначение порта в VLAN", sc(
        head("Назначение <em>порта в VLAN</em>",
             "Три шага: выбрать интерфейс — перевести в access — назначить VLAN."),
        grow("g2",
             col(step(card("Один порт", cli([
                 "switch# configure",
                 "> switch(config)# interface gigabitethernet 1/0/1",
                 "> switch(config-if)# switchport mode access",
                 "> switch(config-if)# switchport access vlan 10",
                 "switch(config-if)# exit",
             ]), "cy")),
                 step(card("Сразу несколько портов", cli([
                     "# interface range — диапазон интерфейсов",
                     "> switch(config)# interface range gigabitethernet 1/0/1-4",
                     "> switch(config-if-range)# switchport mode access",
                     "> switch(config-if-range)# switchport access vlan 10",
                     "switch(config-if-range)# exit",
                 ]), "mg"))),
             col(step(card("Проверка результата", cli([
                 "> switch# show vlan",
                 "",
                 "Vlan   Name       Tagged Ports  UnTagged Ports  Created by",
                 "---- ----------- ------------- --------------- ----------",
                 "   1      -                      gi1/0/5-24         D",
                 "!  10     IT                      gi1/0/1-4         S",
                 "   20  Management                                   S",
             ]), "lm")),
                 step(card("Удаление порта из VLAN", cli([
                     "# Два равнозначных способа:",
                     "> switch(config-if)# no switchport access vlan",
                     "# или",
                     "> switch(config-if)# switchport access vlan 1",
                 ]) + foot("При удалении VLAN с порта доступа он автоматически переводится в VLAN по умолчанию.", "note"), "am"))),
             )
    ))

    # ------------------------------------------------- TRUNK
    slide("Магистральные порты", sc(
        head("<em>Магистральные</em> порты (trunk)",
             "А как подключить устройства одной VLAN на разных коммутаторах?"),
        grow("g2",
             col(step(card("Постановка задачи", p(
                 "Порты доступа предназначены для подключения оконечных устройств. А как поступить, "
                 "если необходимо обеспечить подключение нескольких оконечных устройств "
                 "на <b>разных коммутаторах</b> к одной VLAN?",
                 "Для этих целей существуют магистральные порты."), "cy")),
                 step(card("Определение", p(
                     "<b>Магистральные</b> (от англ. trunk — «транковые») порты — порты, предназначенные "
                     "для подключения сетевых устройств и способные принимать и обрабатывать кадры "
                     "с <b>несколькими разрешёнными метками 802.1Q</b>."), "mg"))),
             col(step(card("Основная задача", p(
                 "Обмен <b>тегированным трафиком</b> между сетевыми устройствами для того, "
                 "чтобы устройства в одной VLAN на разных коммутаторах продолжали находиться "
                 "в одном широковещательном домене.") +
                 foot("Один кабель между коммутаторами вместо одного кабеля на каждую VLAN.", "ok"), "lm")),
                 step(card("Где видно", p(
                     "В выводе <b>show vlan</b> транковые порты попадают в столбец "
                     "<b>Tagged Ports</b> — сразу в нескольких строках, по одной на каждую разрешённую VLAN."), "am"))),
             )
    ))

    slide("Сцена: магистральный порт", sc(
        head("Сцена: <em>магистральный порт</em>",
             "Две VLAN едут по одному кабелю между коммутаторами."),
        grow("g", col(_scene_trunk()))
    ))

    slide("Нативная VLAN", sc(
        head("<em>Нативная</em> VLAN",
             "Нетегированный трафик на транковом порту."),
        grow("g2",
             col(step(card("Определение", p(
                 "Транковый порт может принимать на входе нетегированные кадры и помещать их "
                 "в оговорённую VLAN. Такой трафик называется <b>нативным</b> (native), "
                 "а VLAN — <b>нативной</b>.",
                 "На выходе транкового порта идентификатор нативной VLAN удаляется из кадра, "
                 "и далее кадр передаётся в нетегированном виде."), "cy"))),
             col(step(card("Безопасность", p(
                 "По умолчанию нативной является <b>VLAN 1</b>. На практике это может создать "
                 "угрозы безопасности: кадр, принятый на порту доступа в VLAN 1, имеет "
                 "теоретическую возможность быть переданным на все коммутаторы.") +
                 foot("Рекомендуется на транковых портах менять нативную VLAN на резервную, "
                      "не содержащую портов доступа.", "warn"), "rd")),
                 step(card("Где пригодится", p(
                     "Транковый порт с нативной VLAN может применяться для подключения оконечных "
                     "устройств, поддерживающих протокол 802.1Q — например, IP-телефонов."), "am"))),
             )
    ))

    slide("Сцена: native VLAN", sc(
        head("Сцена: <em>нативная VLAN</em>",
             "Поведение кадров на выходе порта доступа и транковых портов."),
        grow("g", col(_scene_native()))
    ))

    slide("Конфигурация транка", sc(
        head("Конфигурация <em>транкового порта</em>",
             "Три этапа: режим — список разрешённых VLAN — нативная VLAN."),
        grow("g2",
             col(step(card("Этапы", ''.join([
                 irow("<b>1.</b> Перевод порта в режим Trunk.", "", "arrow"),
                 irow("<b>2.</b> Конфигурация списка разрешённых VLAN (allowed VLAN).", "v", "tag"),
                 irow("<b>3.</b> Конфигурация нативной VLAN.", "g", "ok"),
             ]) + cli([
                 "# 1. Режим trunk (в режиме конфигурации интерфейса)",
                 "> switch(config-if)# switchport mode trunk",
                 "",
                 "# 2. Добавить VLAN к списку разрешённых",
                 "> switch(config-if)# switchport trunk allowed vlan add 10,20,30-40",
                 "# Удалить VLAN из списка разрешённых",
                 "> switch(config-if)# switchport trunk allowed vlan remove 30",
                 "",
                 "# 3. Нативная VLAN",
                 "> switch(config-if)# switchport trunk native vlan 50",
             ]), "cy"))),
             col(step(card("Пример целиком", p(
                 "На порту Gigabitethernet 1/0/10 нужно разрешить прохождение трафика VLAN 10, 20, "
                 "а также с 30-й по 40-ю. Нетегированные кадры должны помещаться на входе в VLAN 50.") +
                 cli([
                     "switch# configure",
                     "switch(config)# interface Gigabitethernet 1/0/10",
                     "> switch(config-if)# switchport mode trunk",
                     "> switch(config-if)# switchport trunk allowed vlan add 10,20,30-40",
                     "> switch(config-if)# switchport trunk native vlan 50",
                     "switch(config-if)# exit",
                 ]), "lm")),
                 step(foot("Сами VLAN 10, 20, 30–40 и 50 должны быть уже созданы командой <b>vlan num</b>.", "note"))),
             )
    ))

    # ------------------------------------------------- GENERAL
    slide("Режим general", sc(
        head("Интерфейс с полной поддержкой <em>802.1Q</em>",
             "Режим general — и тегированный, и нетегированный трафик."),
        grow("g2",
             col(step(card("Где применяется", p(
                 "Режим <b>General</b> (характерный для оборудования D-Link, Eltex, QTech, "
                 "Huawei/H3C в режиме hybrid) применяется там, где к одному физическому порту "
                 "подключается устройство, генерирующее <b>одновременно и тегированные, "
                 "и нетегированные кадры</b>."), "cy")),
                 step(card("PVID", p(
                     "<b>PVID (Port VLAN ID)</b> — это идентификатор VLAN, который коммутатор назначает "
                     "<b>входящим нетегированным кадрам</b> (untagged frames).",
                     "Это прямой аналог native VLAN, но для режима general."), "mg"))),
             col(step(card("Ключевые сценарии", ''.join([
                 irow("<b>IP-телефоны с транзитным ПК.</b> Нетегированный трафик от компьютера "
                      "через встроенный свитч телефона попадает в Native/PVID VLAN (например, VLAN 10 для данных). "
                      "Голосовой трафик самого телефона передаётся с 802.1Q-тегом (Voice VLAN, например VLAN 20).", "", "net"),
                 irow("<b>Корпоративные точки доступа Wi-Fi.</b> Управление самой точкой идёт без тега "
                      "в Management VLAN, а клиентские SSID — тегированными кадрами в своих VLAN.", "v", "net"),
             ]), "lm")))
             )
    ))

    slide("Команды режима general", sc(
        head("Команды режима <em>general</em>",
             "Два типовых варианта настройки."),
        grow("g2",
             col(step(card("Нетегированная VLAN с PVID", cli([
                 "switch# configure",
                 "switch(config)# interface Gigabitethernet 1/0/10",
                 "> switch(config-if)# switchport mode general",
                 "> switch(config-if)# switchport general pvid 50",
                 "> switch(config-if)# switchport general allowed vlan add 50 untagged",
             ]) + p("Входящие нетегированные кадры попадут в VLAN 50 и на выходе уйдут без тега."), "cy"))),
             col(step(card("Тегированные VLAN", cli([
                 "switch# configure",
                 "switch(config)# interface Gigabitethernet 1/0/10",
                 "> switch(config-if)# switchport mode general",
                 "> switch(config-if)# switchport general allowed vlan add 10,20,30 tagged",
             ]) + p("Эти VLAN будут проходить через порт с меткой 802.1Q."), "mg")),
                 step(foot("Отличие от trunk: в general для <b>каждой</b> VLAN явно указывается, "
                           "уходит ли она с порта <b>tagged</b> или <b>untagged</b>.", "ok"))),
             )
    ))

    slide("Сцена: general и IP-телефон", sc(
        head("Сцена: <em>general</em> и IP-телефон",
             "Один кабель — два вида трафика."),
        grow("g", col(_scene_general()))
    ))

    # ------------------------------------------------- Q-in-Q
    slide("Q-in-Q интерфейс", sc(
        head("<em>Q-in-Q</em> интерфейс (customer)",
             "Добавление внешнего тега провайдера поверх клиентского."),
        grow("g2",
             col(step(card("Что делает функция", p(
                 "Данная функция позволяет на основе сконфигурированных правил фильтрации "
                 "по номерам внутренних VLAN (<b>Customer VLAN</b>):") +
                 li(["производить добавление внешнего <b>SPVLAN</b> (Service Provider’s VLAN)",
                     "подменять Customer VLAN",
                     "запрещать прохождение трафика"]), "cy")),
                 step(card("Пример правила", p(
                     "Пропустить VLAN 20 без изменения; на остальной трафик, приходящий в порт 1, "
                     "добавить метку 25."), "mg"))),
             col(step(card("Две аксиомы снова", p(
                 "<b>1)</b> Тег всегда снимается <b>на выходе</b>, добавляется <b>на входе порта</b>.",
                 "<b>2)</b> Если на входе с тегом произведено действие, то на выходе должно быть "
                 "выполнено обратное действие."), "lm")),
                 step(card("Ограничение", p(
                     "Наличие хотя бы одного правила <b>Selective Q-in-Q</b> на интерфейсе "
                     "запрещает включение функции логирования широковещательного шторма "
                     "на этом интерфейсе."), "am"))),
             )
    ))

    slide("Сцена: Q-in-Q", sc(
        head("Сцена: <em>Q-in-Q</em>",
             "Два клиента с одинаковыми номерами VLAN в сети провайдера."),
        grow("g", col(_scene_qinq()))
    ))

    # ------------------------------------------------- MAC-based
    slide("VLAN на основе MAC-адресов", sc(
        head("VLAN на основе <em>MAC-адресов</em>",
             "Принадлежность определяется не портом, а адресом устройства."),
        grow("g2",
             col(step(card("Правила назначения", p(
                 "Каждый коммутатор поддерживает таблицу с записями соответствий между "
                 "MAC-адресами и ID VLAN.",
                 "После получения от ПК кадра без тега коммутатор анализирует MAC-адрес "
                 "источника кадра, ищет в таблице соответствия ID VLAN и назначает кадр "
                 "соответствующей сети VLAN."), "cy")),
                 step(card("Характеристики", li([
                     "<b>Плюс.</b> Если меняется интерфейс коммутатора, к которому подключён ПК, "
                     "сеть VLAN остаётся неизменной — ведь MAC-адрес ПК не меняется.",
                     "<b>Минус.</b> Вредоносные ПК могут легко подделывать MAC-адреса, "
                     "поэтому этот метод может подвергать сеть рискам безопасности.",
                     "Метод немного сложен, но гибок."]), "am"))),
             col(step(card("Команды", cli([
                 "# Создаём группу MAC-адресов внутри VLAN",
                 "> switch(config)# vlan database",
                 "> switch(config-vlan)# vlan 10",
                 "> switch(config-vlan)# map mac f4:f2:6d:03:42:31 40 macs-group 1",
                 "switch(config-vlan)# exit",
                 "",
                 "# Привязываем группу к порту в режиме general",
                 "switch(config)# interface gigabitethernet 1/0/1",
                 "> switch(config-if)# switchport mode general",
                 "> switch(config-if)# switchport general map macs-group 1 vlan 10",
             ]), "lm"))),
             )
    ))

    slide("Тренажёр: пройдёт ли кадр", sc(
        head("Тренажёр: <em>пройдёт ли кадр</em>",
             "Ответьте «да» или «нет» и проверьте рассуждение."),
        grow("g2",
             col(task("v1", "На порт <b>access VLAN 10</b> пришёл кадр с меткой 802.1Q VID 10. "
                            "Примет ли его порт?",
                      "нет|no",
                      "Порт доступа на входе обрабатывает <b>только нетегированный</b> трафик. "
                      "Любой тегированный кадр отбрасывается — даже если номер VLAN совпадает.",
                      "да / нет"),
                 task("v2", "На транковом порту разрешены VLAN 10 и 20, native VLAN 50. "
                            "В какую VLAN попадёт нетегированный кадр на входе?",
                      "50",
                      "Нетегированный трафик на транке помещается в <b>нативную VLAN</b> — здесь VLAN 50.",
                      "номер VLAN")),
             col(task("v3", "Сколько байт добавляется к кадру на Q-in-Q интерфейсе "
                            "по сравнению с нетегированным кадром?",
                      "8|8 байт",
                      "Два тега 802.1Q по 4 байта = <b>8 байт</b>. Максимальный размер кадра становится 1526 байт.",
                      "байт"),
                 task("v4", "Порт в режиме general с PVID 10 и allowed vlan 20 tagged. "
                            "С какой меткой уйдёт кадр VLAN 20 на выходе?",
                      "20|с тегом 20|tagged 20",
                      "VLAN 20 добавлена как <b>tagged</b> — значит на выходе метка 802.1Q с VID 20 сохраняется. "
                      "А вот кадры VLAN 10 (PVID) уйдут без тега.",
                      "номер VLAN")),
             )
    ))


# ======================================================================
#  СЦЕНЫ
# ======================================================================

def _scene_access():
    o = []
    names = ["1/0/1", "1/0/2", "1/0/3", "1/0/4", "1/0/5", "1/0/6"]
    sw, pts = S.switch(330, 250, 540, 84, 6, "Коммутатор", names=names)
    o.append(sw)
    o.append(S.badge(pts[0][0], 230, "access VLAN 10", S.LM, ph=0))
    o.append(S.pc(120, 150, "ПК", "не знает про 802.1Q", S.CY))
    o.append(S.link(172, 183, 320, 280, S.SOFT, 2.4, .3))

    o.append(S.pkt(210, 200, 320, 268, "Нетегированный кадр", 1, S.SOFT, w=230))
    o.append(S.badge(600, 130, "Правило 1: на входе принимается только нетегированный трафик", S.CY, ph=1, only=True))
    o.append('<g data-ph="2" data-ph-only>%s</g>' % S.frame_strip(
        240, 390, [("DMAC", 6, S.CY), ("SMAC", 6, S.MG), ("802.1Q VID 10", 5, S.LM),
                   ("EtherType", 4, S.AM), ("Данные", 10, S.SOFT), ("FCS1", 3, S.RD)],
        w=720, h=44, cap="Правило 2: кадр тегируется меткой своей VLAN"))
    o.append(S.badge(600, 130, "Правило 2: кадр тегируется меткой VLAN 10", S.LM, ph=2, only=True))

    o.append('<g data-ph="3" data-ph-only>')
    o.append('<circle cx="%g" cy="%g" r="22" fill="rgba(255,77,94,.2)" stroke="%s" stroke-width="2.6"/>'
             % (pts[0][0], pts[0][1] + 10, S.RD))
    o.append('<path d="M%g %gl20 20M%g %gl-20 20" stroke="%s" stroke-width="3.4" stroke-linecap="round"/>'
             % (pts[0][0] - 10, pts[0][1], pts[0][0] + 10, pts[0][1], S.RD))
    o.append("</g>")
    o.append(S.badge(600, 130, "Если бы на вход пришёл тегированный кадр — он был бы отброшен", S.RD, ph=3, only=True))

    o.append(S.badge(pts[3][0], 230, "access VLAN 20", S.MG, ph=4))
    o.append('<g data-ph="4" data-ph-only>')
    o.append('<circle cx="%g" cy="%g" r="20" fill="rgba(255,77,94,.18)" stroke="%s" stroke-width="2.4"/>'
             % (pts[3][0], pts[3][1] + 10, S.RD))
    o.append("</g>")
    o.append(S.arrow(pts[0][0], pts[0][1] + 60, pts[2][0], pts[2][1] + 60, S.LM, 3.2, "ahg", ph=4))
    o.append(S.badge(600, 130, "Правило 3: на выход идут только кадры своей VLAN", S.LM, ph=4, only=True))

    o.append(S.pc(1080, 150, "ПК VLAN 10", col=S.LM))
    o.append(S.arrow(pts[5][0], pts[5][1], 1028, 220, S.LM, 3.4, "ahg", ph=5))
    o.append('<g data-ph="5" data-ph-only>%s</g>' % S.frame_strip(
        300, 400, [("DMAC", 6, S.CY), ("SMAC", 6, S.MG), ("EtherType", 4, S.AM),
                   ("Данные", 10, S.SOFT), ("FCS2", 3, S.RD)],
        w=620, h=44, cap="Правило 4: на выходе метка снимается"))
    o.append(S.badge(600, 130, "Правило 4: на выходе метка снимается, ПК получает обычный кадр", S.LM, ph=5, only=True))

    caps = ["Порт 1/0/1 настроен как access VLAN 10",
            "ПК отправляет нетегированный кадр",
            "Коммутатор добавляет метку VLAN 10",
            "Тегированный кадр на входе был бы отброшен",
            "На порты чужой VLAN кадр не уйдёт",
            "На выходе метка снимается"]
    return scene(S.fig("".join(o)), caps)


def _scene_trunk():
    o = []
    sw1, p1 = S.switch(80, 250, 400, 80, 5, "SW1", names=["1/0/1", "1/0/2", "1/0/3", "1/0/4", "trunk"])
    sw2, p2 = S.switch(720, 250, 400, 80, 5, "SW2", names=["trunk", "1/0/2", "1/0/3", "1/0/4", "1/0/5"])
    o.append(sw1)
    o.append(sw2)
    o.append(S.link(p1[4][0], p1[4][1] + 10, p2[0][0], p2[0][1] + 10, S.AM, 5, .6))
    o.append(S.badge(600, 250, "Магистраль (trunk)", S.AM, ph=0))

    o.append(S.pc(110, 70, "ПК-A", "VLAN 10", S.LM))
    o.append(S.pc(330, 70, "ПК-B", "VLAN 20", S.MG))
    o.append(S.pc(880, 70, "ПК-C", "VLAN 10", S.LM))
    o.append(S.pc(1090, 70, "ПК-D", "VLAN 20", S.MG))
    o.append(S.link(110, 170, p1[0][0], p1[0][1], S.LM, 2.2, .3))
    o.append(S.link(330, 170, p1[1][0], p1[1][1], S.MG, 2.2, .3))
    o.append(S.link(880, 170, p2[2][0], p2[2][1], S.LM, 2.2, .3))
    o.append(S.link(1090, 170, p2[4][0], p2[4][1], S.MG, 2.2, .3))

    o.append(S.pkt(170, 180, p1[0][0], p1[0][1], "Кадр без тега", 1, S.LM, w=170))
    o.append(S.badge(600, 160, "ПК-A (VLAN 10) отправляет кадр ПК-C", S.LM, ph=1, only=True))
    o.append(S.badge(600, 160, "На порту access добавлен тег VLAN 10", S.LM, ph=2, only=True))
    o.append(S.pkt(p1[0][0], 330, p1[4][0], 330, "802.1Q VID 10", 2, S.LM, w=160))
    o.append(S.pkt(p1[4][0], 290, p2[0][0], 290, "802.1Q VID 10", 3, S.LM, w=160))
    o.append(S.badge(600, 160, "По магистрали кадр идёт <b>с тегом</b> — иначе SW2 не узнает его VLAN", S.AM, ph=3, only=True))
    o.append(S.arrow(p2[0][0], p2[0][1] + 50, p2[2][0], p2[2][1] + 50, S.LM, 3.2, "ahg", ph=4))
    o.append(S.badge(600, 160, "SW2 по метке понял: это VLAN 10 → на порт ПК-C", S.LM, ph=4, only=True))
    o.append(S.arrow(p2[2][0], p2[2][1], 880, 170, S.LM, 3.4, "ahg", ph=5))
    o.append(S.note(240, 420, [
        "На выходе порта доступа метка снимается — ПК-C получает обычный кадр.",
        "ПК-B и ПК-D в VLAN 20 живут своей жизнью по тому же кабелю,",
        "и два широковещательных домена не смешиваются."], S.LM, ph=5, w=720, only=True))

    caps = ["Два коммутатора, между ними один кабель — магистраль",
            "ПК-A из VLAN 10 отправляет кадр",
            "Порт доступа добавляет метку VLAN 10",
            "По магистрали кадр идёт тегированным",
            "SW2 читает метку и выбирает порт своей VLAN",
            "На выходе метка снимается"]
    return scene(S.fig("".join(o)), caps)


def _scene_native():
    o = []
    sw, pts = S.switch(300, 250, 600, 84, 6, "Коммутатор",
                       names=["access", "trunk A", "trunk B", "1/0/4", "1/0/5", "1/0/6"])
    o.append(sw)
    o.append(S.badge(pts[0][0], 226, "access VLAN 10", S.LM, ph=0))
    o.append(S.badge(pts[1][0], 226, "trunk: 10, 20 · native 30", S.AM, ph=0))
    o.append(S.badge(pts[2][0] + 60, 226, "trunk: 10, 20 · native 30", S.MG, ph=0))

    rows = [
        ("Кадр VLAN 10", pts[0][0], S.LM, "без тега", 1),
        ("Кадр VLAN 10", pts[1][0], S.LM, "с тегом VID 10", 2),
        ("Кадр VLAN 20", pts[1][0], S.MG, "с тегом VID 20", 3),
        ("Кадр VLAN 30", pts[1][0], S.AM, "без тега (native)", 4),
    ]
    for (lbl, x, c, out, ph) in rows:
        o.append(S.pkt(x, 400, x, 340, lbl, ph, c, w=170, sub=out))
    o.append(S.badge(600, 150, "На выходе порта доступа VLAN 10 метка всегда снимается", S.LM, ph=1, only=True))
    o.append(S.badge(600, 150, "На транке кадр VLAN 10 уходит с меткой VID 10", S.LM, ph=2, only=True))
    o.append(S.badge(600, 150, "Кадр VLAN 20 тоже уходит с меткой VID 20", S.MG, ph=3, only=True))
    o.append(S.badge(600, 150, "А вот кадр нативной VLAN 30 уходит БЕЗ метки", S.AM, ph=4, only=True))
    o.append(S.note(230, 440, [
        "На входе транкового порта нетегированный кадр помещается в native VLAN,",
        "на выходе идентификатор native VLAN удаляется из кадра.",
        "Значит native VLAN должна совпадать на обоих концах магистрали!"], S.AM, ph=5, w=740, only=True))
    o.append(S.badge(600, 150, "Рекомендация: не держать native VLAN равной 1", S.RD, ph=5, only=True))

    caps = ["Порт доступа и два транка с native VLAN 30",
            "Выход кадра VLAN 10 с порта доступа",
            "Выход кадра VLAN 10 с транка",
            "Выход кадра VLAN 20 с транка",
            "Выход кадра нативной VLAN 30",
            "Главное правило и риск безопасности"]
    return scene(S.fig("".join(o)), caps)


def _scene_general():
    o = []
    sw, pts = S.switch(420, 280, 420, 84, 4, "Коммутатор",
                       names=["general", "1/0/2", "1/0/3", "uplink"])
    o.append(sw)
    o.append(S.badge(pts[0][0], 256, "general · PVID 10 · allowed 20 tagged", S.AM, ph=0))

    o.append(S.box(90, 120, 230, 130, S.CY))
    o.append(S.txt(205, 152, "IP-телефон", 16, S.CY, 800))
    o.append(S.txt(205, 180, "голос — VLAN 20 (tagged)", 12.5, S.MG, 700))
    o.append(S.txt(205, 204, "встроенный свитч", 12, S.SOFT, 600))
    o.append(S.txt(205, 228, "транзит ПК — без тега", 12.5, S.LM, 700))
    o.append(S.pc(110, 380, "ПК", "VLAN 10", S.LM))
    o.append(S.link(110, 380, 205, 250, S.SOFT, 2.4, .3))
    o.append(S.link(320, 185, 410, 300, S.SOFT, 2.6, .35))

    o.append(S.pkt(180, 330, 400, 300, "Кадр ПК — без тега", 1, S.LM, w=200))
    o.append(S.badge(630, 170, "Нетегированный кадр ПК попадает в PVID = VLAN 10", S.LM, ph=1, only=True))
    o.append(S.pkt(320, 200, 400, 290, "Голос — 802.1Q VID 20", 2, S.MG, w=220))
    o.append(S.badge(630, 170, "Голосовой кадр приходит с тегом VID 20 и пропускается", S.MG, ph=2, only=True))
    o.append(S.note(230, 430, [
        "Один физический порт обслуживает два разных широковещательных домена:",
        "данные в VLAN 10 и голос в VLAN 20.",
        "Ни access, ни trunk так сделать не могут: access не примет тег,",
        "а trunk на выходе отдаст с тегом всё, кроме одной native VLAN."], S.AM, ph=3, w=760, only=True))
    o.append(S.arrow(pts[3][0], pts[3][1] + 40, 1080, 340, S.AM, 3.4, "aha", ph=4))
    o.append(S.box(980, 300, 190, 80, S.AM))
    o.append(S.txt(1075, 332, "Ядро сети", 14, S.AM, 800))
    o.append(S.txt(1075, 356, "VLAN 10 и 20", 12.5, S.SOFT, 600))
    o.append(S.badge(630, 170, "Дальше оба потока идут по магистрали тегированными", S.AM, ph=4, only=True))

    caps = ["Порт general: PVID 10 и разрешённая VLAN 20 tagged",
            "Компьютер шлёт кадр без тега",
            "Телефон шлёт голос с тегом",
            "Почему нужен именно general",
            "В ядро сети оба потока уходят тегированными"]
    return scene(S.fig("".join(o)), caps)


def _scene_qinq():
    o = []
    o.append(S.box(430, 240, 340, 90, S.AM))
    o.append(S.txt(600, 276, "Сеть провайдера", 17, S.AM, 800))
    o.append(S.txt(600, 302, "SPVLAN 25 и SPVLAN 26", 13, S.SOFT, 700))
    o.append(S.box(80, 110, 260, 90, S.CY))
    o.append(S.txt(210, 146, "Клиент А", 16, S.CY, 800))
    o.append(S.txt(210, 172, "свои VLAN 10, 20", 13, S.SOFT, 700))
    o.append(S.box(80, 380, 260, 90, S.MG))
    o.append(S.txt(210, 416, "Клиент Б", 16, S.MG, 800))
    o.append(S.txt(210, 442, "тоже VLAN 10, 20", 13, S.SOFT, 700))
    o.append(S.link(340, 155, 430, 265, S.CY, 2.6, .4))
    o.append(S.link(340, 425, 430, 305, S.MG, 2.6, .4))
    o.append(S.box(860, 110, 260, 90, S.CY))
    o.append(S.txt(990, 146, "Филиал А", 16, S.CY, 800))
    o.append(S.box(860, 380, 260, 90, S.MG))
    o.append(S.txt(990, 416, "Филиал Б", 16, S.MG, 800))
    o.append(S.link(770, 265, 860, 155, S.CY, 2.6, .4))
    o.append(S.link(770, 305, 860, 425, S.MG, 2.6, .4))

    o.append(S.badge(600, 60, "Проблема: у обоих клиентов одинаковые номера VLAN", S.RD, ph=0))
    o.append('<g data-ph="1" data-ph-only>%s</g>' % S.frame_strip(
        260, 486, [("DMAC", 6, S.CY), ("SMAC", 6, S.MG), ("C-TAG VID 10", 5, S.CY),
                   ("EtherType", 4, S.LM), ("Данные", 9, S.SOFT), ("FCS", 3, S.RD)],
        w=680, h=42, cap="Кадр клиента А с его собственным тегом"))
    o.append(S.badge(600, 60, "Кадр клиента приходит с его Customer VLAN", S.CY, ph=1, only=True))
    o.append('<g data-ph="2" data-ph-only>%s</g>' % S.frame_strip(
        210, 486, [("DMAC", 6, S.CY), ("SMAC", 6, S.MG), ("S-TAG VID 25", 5, S.AM),
                   ("C-TAG VID 10", 5, S.CY), ("EtherType", 4, S.LM),
                   ("Данные", 9, S.SOFT), ("FCS", 3, S.RD)],
        w=780, h=42, cap="Провайдер добавил внешний тег SPVLAN 25 поверх клиентского"))
    o.append(S.badge(600, 60, "На входе customer-порта добавляется внешний тег SPVLAN 25", S.AM, ph=2, only=True))
    o.append(S.badge(600, 60, "Внутри сети провайдера клиенты разделены по SPVLAN", S.LM, ph=3, only=True))
    o.append('<g data-ph="3">')
    o.append(S.badge(600, 200, "Клиент А → SPVLAN 25", S.CY))
    o.append(S.badge(600, 370, "Клиент Б → SPVLAN 26", S.MG))
    o.append("</g>")
    o.append('<g data-ph="4" data-ph-only>%s</g>' % S.frame_strip(
        260, 486, [("DMAC", 6, S.CY), ("SMAC", 6, S.MG), ("C-TAG VID 10", 5, S.CY),
                   ("EtherType", 4, S.LM), ("Данные", 9, S.SOFT), ("FCS", 3, S.RD)],
        w=680, h=42, cap="На выходе внешний тег снимается — клиент получает свой кадр"))
    o.append(S.badge(600, 60, "Аксиома 2: добавили на входе — сняли на выходе", S.LM, ph=4, only=True))

    caps = ["Два клиента с одинаковыми номерами VLAN",
            "Кадр клиента с его Customer VLAN",
            "Добавляется внешний тег SPVLAN",
            "Внутри сети провайдера клиенты разделены",
            "На выходе внешний тег снимается"]
    return scene(S.fig("".join(o)), caps)
