# -*- coding: utf-8 -*-
"""Блок 8: NTP — история, принцип, алгоритм Марзулло, иерархия Stratum, настройка; итоговый тест и задачи."""

from _sw_lib import grow, g, col, card, p, li, foot, tags, tag, table, cli, step, scene, task, quiz
from _nat_lib import slide, sc, head, pill, kv, big
import _nat_svg as S


def build():
    slide("Раздел: NTP", '<div class="sc"><div class="cover">'
          '<p class="kick">Часть 3</p><div class="big">Протокол <em>сетевого времени</em></div>'
          '<div class="orn"><i></i><b></b><i></i></div>'
          '<p class="lead">NTP — Network Time Protocol: единое время для компьютеров, сетей и всего мира</p>'
          '</div></div>', bg="c", cover=True)

    slide("История учёта времени", sc(
        head("Протокол сетевого времени <em>(NTP)</em>", "Единое время для компьютеров, сетей и всего мира"),
        grow("g", col(_scene_time_history()))
    ), bg="a")

    slide("Откуда берётся точное время", sc(
        head("Откуда берётся <em>точное время</em>", "GPS / атомные часы → NTP-серверы → компьютеры и сетевые устройства"),
        grow("g", col(_scene_time_chain()))
    ), bg="d")

    slide("Зачем нужно точное время", sc(
        head("Зачем нужно <em class='y'>точное время</em>?", "Даже небольшое расхождение часов имеет серьёзные последствия"),
        grow("g3",
             step(card("Безопасность и аутентификация", p("Сертификаты и билеты Kerberos проверяют время: разошлись часы — "
                                                         "вход отклонён."), "ye", "🔒")),
             step(card("Журналы событий", p("Чтобы восстановить цепочку событий по логам разных устройств, "
                                            "метки времени должны совпадать."), "or", "≡")),
             step(card("Согласованность данных", p("Репликация баз данных: какая запись новее, решается по времени."), "vi", "⇄")),
             step(card("Финансы", p("Порядок сделок и транзакций фиксируется с точностью до долей секунды."), "lm", "₽")),
             step(card("Телекоммуникации", p("Синхронизация оборудования связи и биллинга."), "cy", "☎")),
             step(card("Научные исследования", p("Совместные измерения в разных точках мира."), "rd", "✦")))
    ), bg="b")

    slide("NTP: общая информация", sc(
        head("NTP: <em>синхронизация времени</em> в сети", "Клиент-серверный протокол, распространяющий точное время от эталонных источников"),
        grow("g2",
             col(step(card("История", li([
                 "Конец <b>1970-х</b> — <b>Дэвид Миллс</b> разрабатывает первую версию.",
                 "Цель — устойчивая точная синхронизация даже при переменных задержках сети.",
                 "Начало <b>2000-х</b> — стабильная версия <b>NTPv4</b>.",
                 "Сегодня — стандарт для Интернета и локальных сетей."]), "ye", "⌚")),
                 step(card("Безопасность", p("Есть аутентификация сообщений между клиентами и серверами — защита от "
                                             "подмены времени. Требует правильной настройки и обновлений."), "rd", "🔒"))),
             col(step(card("Как работает", li([
                 "Клиент обращается к <b>нескольким</b> NTP-серверам («массив источников»).",
                 "Анализирует разницу во времени между ними — <b>джиттер</b> показывает стабильность сервера.",
                 "Использует <b>взвешенное среднее</b> времени от надёжных серверов.",
                 "Транспорт — <b>UDP, порт 123</b>."]), "cy", "⚙")),
                 step(foot("Для жёстких требований к точности применяют <b>PTP</b> (Precision Time Protocol).", "note"))))
    ), bg="a")

    slide("Обмен NTP: четыре метки времени", sc(
        head("Обмен NTP: <em>четыре метки времени</em>", "Как клиент узнаёт задержку и смещение своих часов"),
        grow("g", col(_scene_ntp_exchange()))
    ), bg="d")

    slide("Алгоритм Марзулло", sc(
        head("Алгоритм <em>Марзулло</em> (Marzullo's Algorithm)", "Выбор наиболее достоверного времени из ответов разных серверов"),
        grow("g", col(_scene_marzullo()))
    ), bg="b")

    slide("Марзулло: принцип", sc(
        head("Марзулло: <em>принцип</em>"),
        grow("g2",
             col(step(card("Шаги", li([
                 "Каждый сервер даёт значение времени и <b>погрешность</b> → интервал.",
                 "Ищется интервал, который содержит «правильное» время для <b>наибольшего числа</b> источников.",
                 "Значения за его пределами <b>исключаются</b> — они могли быть искажены.",
                 "Оставшиеся значения <b>усредняются</b>."]), "cy", "1"))),
             col(step(card("Пример", p("10 ± 2 → [8, 12]", "12 ± 1 → [11, 13]", "11 ± 1 → [10, 12]",
                                       "Пересечение всех трёх: <b>[11, 12]</b> → <b>11,5 ± 0,5</b>."), "ye", "Σ")),
                 step(big("Лучшая оценка — наименьший интервал, согласованный с наибольшим числом источников", "y"))))
    ), bg="c")

    slide("Задачи: Марзулло", sc(
        head("Задачи · <em class='y'>алгоритм Марзулло</em>"),
        grow("g2",
             col(step(task("t-m1", "Серверы: <b>20 ± 3</b>, <b>22 ± 2</b>, <b>21 ± 1</b>. Найдите пересечение интервалов [a,b].",
                           "[20,22]|20,22|[20;22]|20-22",
                           "[17,23] ∩ [20,24] ∩ [20,22] = <b>[20, 22]</b> → оценка 21 ± 1.", "[a,b]")),
                 step(task("t-m2", "Для того же примера: итоговая оценка времени (центр интервала)?", "21",
                           "Центр [20, 22] — <b>21</b> (± 1).", "число"))),
             col(step(task("t-m3", "Серверы: <b>10 ± 1</b>, <b>11 ± 1</b>, <b>30 ± 1</b>. Сколько источников попадёт в лучший интервал?",
                           "2", "[9,11] и [10,12] пересекаются в [10,11]; [29,31] — <b>выброс</b>. Ответ: <b>2</b>.", "число")),
                 step(foot("Сервер 30 ± 1 — «врущие часы»: алгоритм его отбросит.", "warn"))))
    ), bg="a")

    slide("Иерархия NTP — Stratum", sc(
        head("Иерархия NTP — <em>Stratum</em>", "Чем меньше номер слоя, тем ближе сервер к эталону"),
        grow("g", col(_scene_stratum()))
    ), bg="d")

    slide("Stratum: уровни", sc(
        head("Stratum: <em>уровни иерархии</em>"),
        grow("g", col(
            pill("0", "Stratum 0 — эталон", "атомные часы, GPS; прямой доступ ограничен, время передаётся в Stratum 1", "y", True),
            pill("1", "Stratum 1 — первичные серверы", "получают время от Stratum 0 по спецустройствам, точные аппаратные часы", "o", True),
            pill("2", "Stratum 2, 3 … 15", "синхронизируются с вышестоящими; серверы локальных сетей, удалённые NTP-серверы", "v", True),
            pill("16", "Stratum 16", "самый низкий уровень — устройство НЕ синхронизировано", "r", True))),
        step(foot("Клиент предпочитает источник с <b>меньшим</b> stratum. Максимум переходов — <b>15</b>.", "note"))
    ), bg="b")

    slide("Задача: какой stratum", sc(
        head("Задача · <em class='y'>какой stratum?</em>"),
        grow("g2",
             col(step(task("t-s1", "Маршрутизатор синхронизируется с сервером Stratum 2. Какой stratum будет у маршрутизатора?",
                           "3", "Каждый переход вниз +1: 2 + 1 = <b>3</b>.", "число")),
                 step(task("t-s2", "Сервер получает время напрямую от GPS-приёмника. Его stratum?", "1",
                           "GPS — Stratum 0, сервер с прямым подключением — <b>Stratum 1</b>.", "число"))),
             col(step(quiz("В выводе show ntp peers: «stratum 16». Что это значит?",
                           ["Самый точный сервер", "Устройство не синхронизировано", "16 источников", "Порт 16"], 1,
                           "Stratum 16 — устройство не синхронизировано.")),
                 step(quiz("Какой источник выберет клиент при прочих равных?",
                           ["Stratum 4", "Stratum 2", "Stratum 3", "Stratum 16"], 1,
                           "Меньший stratum — ближе к эталону, точнее."))))
    ), bg="c")

    slide("Настройка NTP", sc(
        head("Настройка <em>NTP</em> на ESR", "Синхронизировать R1 (192.0.2.10/24) с NTP-сервером 192.0.2.1/24"),
        grow("g2",
             col(_scene_ntp_cfg()),
             col(step(card("Команды", cli([
                 "> ESR(config)# ntp enable",
                 "> ESR(config)# ntp server 192.0.2.1",
                 "ESR(config-ntp)# prefer",
                 "ESR(config-ntp)# minpoll 4"], "ESR · NTP"), "cy")),
                 step(table(["Команда", "Назначение"], [
                     ["<b>ntp enable</b>", "включить синхронизацию с удалёнными серверами"],
                     ["<b>ntp server &lt;ADDR&gt;</b>", "IP-адрес NTP-сервера"],
                     ["<b>minpoll &lt;4..6&gt;</b>", "минимальный интервал опроса"],
                     ["<b>prefer</b>", "предпочтительный сервер"]]))))
    ), bg="a")

    slide("Диагностика NTP", sc(
        head("Диагностика <em>NTP</em>"),
        grow("g2",
             step(card("show ntp configuration", cli([
                 "> esr# show ntp configuration",
                 "NTP status:  Enabled",
                 "NTP mode:    client/server",
                 "NTP DSCP:    46",
                 "Address         VRF  Type    Version  Min poll  Max poll  Prefer",
                 "! 89.109.251.21   1    server  4        6         10        Yes",
                 "89.109.251.22   1    server  4        6         10        No",
                 "46.254.241.74   1    server  4        6         10        No",
                 "212.19.6.218    1    server  4        6         10        No"], ""), "cy", "1")),
             col(step(card("show ntp peers", cli([
                 "> esr# show ntp peers",
                 "! Clock is synchronized, stratum 2, reference is 89.109.251.22",
                 "   remote          refid st t when poll reach delay  offset  jitter",
                 "+ 89.109.251.21    MRS   1  u 51   64   255   44.125 -9.839  12.666",
                 "! * 89.109.251.22    MRS   1  u 42   64   255   40.668  3.964   3.991",
                 "+ 46.254.241.74    MRS   1  u 49   64   255   22.958  2.694   2.254",
                 "- 212.19.6.218     MRS   1  u 38   64   255   66.194 -0.407   4.408"], ""), "ye", "2")),
                 step(foot("<b>*</b> — выбранный источник, <b>+</b> — кандидаты, <b>−</b> — отброшен. "
                           "Серверы Stratum 1 → сам ESR получил <b>stratum 2</b>.", "note"))))
    ), bg="d")

    # -------- итог
    slide("Итоговый тест", sc(
        head("Итоговый <em class='y'>тест</em>", 'Правильных ответов: <span class="score">0 / 0</span>'),
        grow("g2",
             col(step(quiz("Какой порт и протокол у DHCP-сервера?", ["TCP 67", "UDP 67", "UDP 123", "UDP 68"], 1,
                           "Сервер — UDP 67, клиент — UDP 68.")),
                 step(quiz("Когда клиент впервые пытается продлить аренду?", ["25 %", "50 % (T0)", "87,5 % (T1)", "100 %"], 1,
                           "T0 = 50 % — одноадресный DHCPREQUEST.")),
                 step(quiz("Адрес 192.168.1.10 внутреннего ПК, видимый изнутри, — это…",
                           ["Inside global", "Outside local", "Inside local", "Outside global"], 2, "Inside local.")),
                 step(quiz("Какой NAT позволяет многим узлам выходить через ОДИН публичный адрес?",
                           ["Статический", "Динамический", "NAPT / PAT", "DNAT"], 2, "NAPT различает узлы по портам."))),
             col(step(quiz("Что меняет Destination NAT?", ["Адрес источника", "Адрес назначения", "MAC-адрес", "TTL"], 1,
                           "DNAT переписывает адрес (и иногда порт) назначения.")),
                 step(quiz("Зачем на ESR зоны TRUST и UNTRUST при настройке NAT?",
                           ["Для DHCP", "Для политики безопасности (zone-pair)", "Для NTP", "Не нужны"], 1,
                           "Правила zone-pair разрешают трафик между зонами.")),
                 step(quiz("Что делает Proxy ARP?", ["Шифрует ARP", "Отвечает на ARP за узел другого сегмента",
                                                     "Выдаёт IP-адреса", "Синхронизирует время"], 1, "Маршрутизатор отвечает своим MAC.")),
                 step(quiz("Stratum 0 — это…", ["Не синхронизированное устройство", "Эталон: атомные часы, GPS",
                                                "Любой клиент", "Маршрутизатор"], 1, "Самые точные источники времени."))))
    ), bg="b")

    slide("Комплексная задача", sc(
        head("Комплексная <em class='y'>задача</em>", "Офис: 40 ПК в 192.168.10.0/24, сервер DHCP в 10.0.0.0/24, один публичный адрес 1.1.1.1"),
        grow("g2",
             col(step(task("t-c1", "Какая служба нужна на маршрутизаторе, чтобы ПК получили адреса от сервера в 10.0.0.0/24?",
                           "dhcp relay|dhcp-relay|relay|ретранслятор|dhcp-ретранслятор",
                           "Сервер в другой сети → <b>DHCP Relay</b> (ip dhcp-relay + ip helper-address).", "служба")),
                 step(task("t-c2", "Какой тип NAT выпустит все 40 ПК в Интернет через 1.1.1.1?",
                           "napt|pat|snat|source nat|napt/pat",
                           "Один адрес на много узлов — <b>NAPT (PAT)</b>, разновидность Source NAT.", "тип NAT"))),
             col(step(task("t-c3", "Веб-сервер 192.168.10.5 нужно открыть снаружи на 1.1.1.1:80. Какой NAT?",
                           "dnat|destination nat|проброс|port forwarding",
                           "Входящий запрос → <b>Destination NAT</b> (проброс порта 80).", "тип NAT")),
                 step(task("t-c4", "Аренда — 1 сутки (1440 мин). Через сколько минут ПК попробует её продлить?",
                           "720", "T0 = 50 % · 1440 = <b>720 минут</b>.", "минуты"))))
    ), bg="c")

    slide("Итоги главы", sc(
        head("Итоги <em>главы</em>"),
        grow("g3",
             step(card("DHCP", li(["DORA: Discover → Offer → Request → Ack", "ARP-проверка и DHCPDECLINE",
                                   "аренда: T0 = 50 %, T1 = 87,5 %", "Relay для сервера в другой сети"], "lm"), "ye", "1")),
             step(card("NAT", li(["4 адреса: inside/outside × local/global", "SNAT: статический, динамический, NAPT",
                                  "DNAT и проброс портов", "зоны и правила на ESR, Proxy ARP"], "lm"), "or", "2")),
             step(card("NTP", li(["UDP 123, клиент-сервер", "алгоритм Марзулло", "Stratum 0 … 15, 16 — нет синхр.",
                                  "ntp enable / ntp server / prefer"], "lm"), "vi", "3"))),
        step(big("Спасибо за внимание!"))
    ), bg="a")


# ======================================================================

def _scene_time_history():
    o = []
    items = [("Ранние компьютеры", "Время вели операторы вручную,", "внешние часы", "y"),
             ("1950–1960-е", "ОС получили системные", "вызовы для работы со временем", "o"),
             ("Рост сетей", "Компьютерам понадобилась", "синхронизация часов", "v"),
             ("NTP", "Сетевой протокол", "синхронизации времени", "g"),
             ("Сегодня", "GPS и атомные часы — точное", "время по всему миру", "c")]
    for i, (t, a, b, tone) in enumerate(items):
        x = 20 + i * 236
        c = S.TONE[tone]
        o.append('<g data-ph="%d">' % (i + 1))
        o.append('<rect x="%d" y="30" width="220" height="44" rx="22" fill="url(#pg)" stroke="%s" stroke-width="2.2" filter="url(#gl)"/>' % (x, c))
        o.append('<circle cx="%d" cy="52" r="16" fill="%s"/>' % (x + 22, c) + S.txt(x + 22, 58, str(i + 1), 16, "#0b1630", 900))
        o.append(S.txt(x + 46, 59, t, 17, c, 900, "start"))
        o.append(S.box(x, 90, 220, 230, c, "rgba(5,18,46,.92)", 12, 1.5))
        o.append(_clock_icon(x + 110, 175, i, c))
        o.append(S.txt(x + 110, 270, a, 13.5, S.SOFT, 700) + S.txt(x + 110, 292, b, 13.5, S.SOFT, 700))
        o.append('</g>')
        if i < 4:
            o.append('<path d="M%d 205h16" stroke="%s" stroke-width="3" marker-end="url(#mk%s)" data-ph="%d"/>' % (x + 222, c, tone, i + 2))
    o.append('<g data-ph="6">' + S.box(120, 360, 960, 90, S.CY, "rgba(5,18,46,.92)", 14, 2)
             + S.txt(600, 398, "Точность учёта времени стала критически важной:", 19, "#fff", 900)
             + S.txt(600, 428, "финансы · телекоммуникации · безопасность · научные исследования", 16, S.YE, 800) + '</g>')
    return scene(S.fig("".join(o), "0 0 1200 470"), [
        "История учёта времени на компьютерах насчитывает много десятилетий.",
        "<b>Ранние компьютеры</b>: встроенных часов нет, временем управляют операторы вручную.",
        "<b>1950–1960-е</b>: первые ОС с системными вызовами для работы со временем.",
        "<b>Рост сетей</b>: понадобилась точная синхронизация между компьютерами.",
        "<b>NTP</b> — стандарт синхронизации времени в компьютерных сетях.",
        "<b>Сегодня</b>: глобальные серверы времени, GPS и атомные часы.",
        "Точное время критично во многих областях.",
    ])


def _clock_icon(x, y, k, c):
    if k == 3:
        return S.server(x, y, "", "", 80)
    if k == 4:
        return S.globe(x, y, 46)
    o = '<circle cx="%g" cy="%g" r="44" fill="rgba(10,40,90,.7)" stroke="%s" stroke-width="3" filter="url(#gl)"/>' % (x, y, c)
    for a in range(12):
        import math
        xa, ya = x + 36 * math.sin(math.radians(a * 30)), y - 36 * math.cos(math.radians(a * 30))
        o += '<circle cx="%.1f" cy="%.1f" r="2.4" fill="%s"/>' % (xa, ya, c)
    o += '<path d="M%g %gV%g M%g %gL%g %g" stroke="#fff" stroke-width="4" stroke-linecap="round"/>' % (x, y, y - 28, x, y, x + 18, y + 10)
    return o


def _scene_time_chain():
    o = []
    o.append(S.chip(40, 20, "0", "GPS / атомные часы", "y", 300))
    o.append(S.globe(130, 200, 60) + S.txt(130, 300, "GPS-спутники", 16, "#fff", 800))
    o.append(_clock_icon(290, 200, 0, S.YE) + S.txt(290, 300, "Атомные часы", 16, "#fff", 800))
    o.append('<g data-ph="1">' + S.chip(450, 20, "1", "NTP-серверы", "o", 260)
             + S.server(510, 200, "Stratum 1", "", 100) + S.server(660, 200, "Stratum 2", "", 90) + '</g>')
    o.append('<path d="M360 200H450" stroke="%s" stroke-width="4" marker-end="url(#mko)" class="flow" data-ph="1"/>' % S.OR)
    o.append('<g data-ph="2">' + S.chip(800, 20, "2", "Компьютеры и устройства", "v", 360))
    devs = [("Компьютеры", 100), ("Серверы", 180), ("Маршрутизаторы", 260), ("Смартфоны", 340)]
    for nm, y in devs:
        o.append(S.pc(880, y, "", "", 50) + S.txt(920, y + 6, nm, 15, "#fff", 800, "start"))
        o.append('<path d="M715 200L845 %d" stroke="%s" stroke-width="2.4" marker-end="url(#mkv)" class="flow"/>' % (y, S.VI))
    o.append('</g>')
    o.append(S.badge(600, 440, "Транспорт NTP — UDP, порт 123", S.CY, ph=3, size=17))
    return scene(S.fig("".join(o), "0 0 1200 480"), [
        "Эталон времени — <b>GPS</b> и <b>атомные часы</b>.",
        "От них время получают <b>NTP-серверы</b> верхнего уровня и передают ниже.",
        "Компьютеры, серверы, маршрутизаторы, смартфоны синхронизируются с NTP-серверами.",
        "Обмен идёт по <b>UDP, порт 123</b>.",
    ])


def _scene_ntp_exchange():
    o = [S.pc(200, 90, "NTP-клиент", "", 80), S.server(1000, 90, "NTP-сервер", "", 80)]
    o.append('<path d="M200 150V470" stroke="#5fb8ff" stroke-width="2" stroke-dasharray="6 6" opacity=".6"/>')
    o.append('<path d="M1000 150V470" stroke="#5fb8ff" stroke-width="2" stroke-dasharray="6 6" opacity=".6"/>')
    o.append('<g data-ph="1"><path d="M200 190L992 260" stroke="%s" stroke-width="3.4" marker-end="url(#mky)"/>' % S.YE
             + S.txt(150, 196, "t1", 20, S.YE, 900) + S.txt(1050, 266, "t2", 20, S.YE, 900)
             + S.txt(600, 205, "запрос (метка t1)", 16, S.YE, 800) + '</g>')
    o.append('<g data-ph="2"><path d="M1000 300L208 380" stroke="%s" stroke-width="3.4" marker-end="url(#mkg)"/>' % S.GR
             + S.txt(1050, 306, "t3", 20, S.GR, 900) + S.txt(150, 386, "t4", 20, S.GR, 900)
             + S.txt(600, 330, "ответ (t1, t2, t3)", 16, S.GR, 800) + '</g>')
    o.append('<g data-ph="3">' + S.box(330, 400, 540, 100, S.CY, "rgba(5,18,46,.95)", 12, 2)
             + S.txt(600, 436, "задержка δ = (t4 − t1) − (t3 − t2)", 19, "#fff", 800, mono=True)
             + S.txt(600, 474, "смещение θ = ((t2 − t1) + (t3 − t4)) / 2", 19, S.YE, 800, mono=True) + '</g>')
    return scene(S.fig("".join(o), "0 0 1200 510"), [
        "Клиент и сервер обмениваются одним запросом и одним ответом.",
        "Клиент отправляет запрос в момент <b>t1</b> (по своим часам); сервер принимает в <b>t2</b>.",
        "Сервер отвечает в <b>t3</b>; клиент получает ответ в <b>t4</b>.",
        "По четырём меткам клиент вычисляет <b>задержку</b> сети и <b>смещение</b> своих часов.",
    ])


def _scene_marzullo():
    o = []
    X0, SC = 140, 140          # x = X0 + (v-8)*SC
    def x(v):
        return X0 + (v - 8) * SC
    for v in range(8, 15):
        o.append('<path d="M%g 40V430" stroke="#5fb8ff" stroke-dasharray="4 6" opacity=".35"/>' % x(v))
        o.append(S.txt(x(v), 465, str(v), 18, "#fff", 800))
    rows = [("[8, 12]", 8, 12, 10, "10 ± 2", 1), ("[10, 12]", 10, 12, 11, "11 ± 1", 2), ("[11, 13]", 11, 13, 12, "12 ± 1", 3)]
    for i, (lab, a, b, m, txt, ph) in enumerate(rows):
        y = 90 + i * 80
        o.append('<g data-ph="%d">' % ph)
        o.append(S.txt(70, y + 6, lab, 17, S.SOFT, 800, mono=True))
        o.append('<path d="M%g %dH%g" stroke="%s" stroke-width="8" stroke-linecap="round" filter="url(#gl)"/>' % (x(a), y, x(b), S.BL))
        o.append('<circle cx="%g" cy="%d" r="9" fill="%s"/>' % (x(m), y, S.RD))
        o.append(S.txt(x(b) + 20, y + 6, txt, 18, S.YE, 900, "start"))
        o.append('</g>')
    o.append('<g data-ph="4"><rect x="%g" y="50" width="%g" height="230" fill="rgba(255,210,63,.14)" stroke="%s" stroke-dasharray="6 5"/></g>'
             % (x(11), x(12) - x(11), S.YE))
    o.append('<g data-ph="5"><path d="M%g 300V340" stroke="%s" stroke-width="4" marker-end="url(#mkb)"/>' % (x(11.5), S.BL)
             + S.txt(70, 386, "[11, 12]", 17, S.SOFT, 800, mono=True)
             + '<path d="M%g 380H%g" stroke="%s" stroke-width="10" stroke-linecap="round" filter="url(#gl)"/>' % (x(11), x(12), S.RD)
             + '<circle cx="%g" cy="380" r="10" fill="#fff"/>' % x(11.5)
             + S.txt(x(12) + 24, 388, "11,5 ± 0,5", 22, S.GR, 900, "start") + '</g>')
    return scene(S.fig("".join(o), "0 0 1200 490"), [
        "Ось времени. Каждый NTP-сервер сообщает значение и погрешность.",
        "Сервер 1: <b>10 ± 2</b> → интервал [8, 12].",
        "Сервер 2: <b>11 ± 1</b> → интервал [10, 12].",
        "Сервер 3: <b>12 ± 1</b> → интервал [11, 13].",
        "Ищем область, где пересекаются интервалы <b>всех трёх</b> источников.",
        "Пересечение <b>[11, 12]</b> → лучшая оценка <b>11,5 ± 0,5</b>.",
    ])


def _scene_stratum():
    o = []
    bands = [(0, "#2ad4ff", 3), (1, "#6cf08a", 3), (2, "#6cf08a", 4), (3, "#6cf08a", 6)]
    pos = {}
    for lvl, col_, n in bands:
        y = 20 + lvl * 120
        o.append('<g data-ph="%d">' % lvl)
        o.append('<rect x="20" y="%d" width="1160" height="104" rx="14" fill="%s" opacity=".12" stroke="%s" stroke-opacity=".5"/>' % (y, col_, col_))
        o.append(S.txt(60, y + 64, str(lvl), 40, col_, 900))
        o.append(S.txt(60, y + 92, "stratum", 12, S.SOFT, 700))
        pts = []
        for k in range(n):
            xx = 200 + (k + .5) * (960.0 / n)
            pts.append(xx)
            if lvl == 0:
                o.append(_clock_icon(xx, y + 52, 0, S.YE).replace('r="44"', 'r="34"'))
            else:
                o.append(S.server(xx, y + 48, "", "", 64))
        pos[lvl] = (y, pts)
        if lvl > 0:
            py, pp = pos[lvl - 1]
            for k, xx in enumerate(pts):
                src = pp[min(len(pp) - 1, k * len(pp) // n)]
                o.append('<path d="M%g %dL%g %d" stroke="%s" stroke-width="2.6" marker-end="url(#mk%s)" class="flow"/>'
                         % (src, py + 90, xx, y + 12, S.YE if lvl == 1 else S.RD, "y" if lvl == 1 else "r"))
            for k in range(len(pts) - 1):
                if (k + lvl) % 2 == 0:
                    o.append('<path d="M%g %dH%g" stroke="%s" stroke-width="2" stroke-dasharray="5 4" opacity=".8"/>'
                             % (pts[k] + 34, y + 52, pts[k + 1] - 34, S.RD))
        o.append('</g>')
    o.append(S.badge(1000, 70, "эталон: атомные часы, GPS", S.YE, ph=0, size=14))
    o.append(S.badge(1000, 445, "пиры одного уровня сверяются друг с другом", S.RD, ph=4, size=14))
    return scene(S.fig("".join(o), "0 0 1200 500"), [
        "<b>Stratum 0</b> — эталонные часы: атомные, GPS.",
        "<b>Stratum 1</b> — серверы, подключённые к эталону напрямую.",
        "<b>Stratum 2</b> — синхронизируются с Stratum 1 и между собой.",
        "<b>Stratum 3</b> — ещё на уровень ниже; точность снижается с ростом номера.",
        "Серверы одного уровня — пиры: обмениваются временем для надёжности (красные пунктиры).",
    ])


def _scene_ntp_cfg():
    o = [S.router(170, 190, "R1", "NTP-клиент", 120), S.router(720, 190, "NTP", "NTP-сервер", 120, col=S.GR)]
    o.append(S.link(235, 190, 655, 190, S.CY, 4, .7))
    o.append(S.badge(300, 150, "192.0.2.10/24", S.CY, size=15) + S.badge(600, 150, "192.0.2.1/24", S.GR, size=15))
    o.append(S.env(250, 230, 640, 230, "NTP-запрос · UDP 123", 1, S.YE, True, 220))
    o.append(S.env(640, 260, 250, 260, "время сервера", 2, S.GR, True, 180))
    o.append(S.badge(170, 330, "Clock is synchronized ✓", S.GR, ph=3, size=15))
    return scene(S.fig("".join(o), "0 0 880 380"), [
        "Топология для настройки NTP: R1 — клиент, сервер 192.0.2.1.",
        "После <b>ntp enable</b> и <b>ntp server 192.0.2.1</b> R1 опрашивает сервер.",
        "Сервер возвращает метки времени.",
        "Часы R1 синхронизированы.",
    ])
