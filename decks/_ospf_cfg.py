# -*- coding: utf-8 -*-
"""Блок «Настройка OSPF на ESR»: процесс, область, интерфейс, параметры, таймеры, проверка."""

from _ospf_lib import (slide, head, sc, step, steps, foot, tag, tags, table, cli,
                       router, link, pill, txt, blob, bubble, rowc, split, ill, panel, chain)


def cfg(label, title, sub, lines, rows, typ=True, ratio="54fr 46fr", scen="type"):
    slide(label, sc(
        head(title, sub),
        split(panel("pc", "Командная строка ESR", cli(lines, typ=typ), "b"), steps(*rows), ratio)
    ), scen=scen if typ else None)


def build():
    slide("Настройка: порядок", sc(
        head("Настройка OSPF: порядок действий", "Пять шагов — от процесса до проверки соседства."),
        step(chain([("router ospf", ""), ("area + enable", "b"), ("enable процесса", "y"),
                    ("интерфейс: ip ospf", ""), ("commit · confirm", "g")])),
        '<div class="row3 fill">' + steps(
            rowc("gear", "Процесс глобально", "Создаём процесс OSPF, задаём router-id, создаём и включаем область.", "p"),
            rowc("net", "Привязка к интерфейсу", "На интерфейсе указываем instance, area, тип сети и включаем ip ospf.", "b"),
            rowc("eye", "Проверка", "show ip ospf neighbor — соседство Full; show ip route — маршруты O.", "g")) + '</div>'
    ))

    cfg("Настройка: процесс", "Создание процесса OSPF", "Процесс создаётся в режиме глобальной конфигурации, номер от 1 до 65535.",
        [("esr(config)#", "router ospf 100", "номер процесса 1–65535"),
         ("esr(config-ospf)#", "router-id 1.1.1.1", "идентификатор в формате IPv4"),
         ("esr(config-ospf)#", "area 0.0.0.0", "создаём область"),
         ("esr(config-ospf-area)#", "enable", "включаем область"),
         ("esr(config-ospf-area)#", "exit", ""),
         ("esr(config-ospf)#", "enable", "включаем процесс"),
         ("esr(config-ospf)#", "do commit", ""),
         ("esr(config-ospf)#", "do confirm", "после проверки")],
        [rowc("doc", "Номер процесса", "Локальный: на разных маршрутизаторах может отличаться, но в одной сети лучше одинаковый.", "b"),
         rowc("key", "router-id вручную", "Обычно — адрес отдельного Loopback. Сменить потом можно только перезапуском процесса.", "p"),
         rowc("stop", "Порядок включения", "Пока ни одна area не включена, процесс OSPF не включится.", "y")])

    cfg("Настройка: тип области", "Тип области и параметры процесса", "Если область не backbone и не standard — тип задаётся явно.",
        [("esr(config-ospf)#", "area 0.0.0.2", ""),
         ("esr(config-ospf-area)#", "area-type stub", "totally-stub / nssa / totally-nssa"),
         ("esr(config-ospf-area)#", "enable", ""),
         ("esr(config-ospf)#", "preference 90", "по умолчанию 150; у RIP — 100"),
         ("esr(config-ospf)#", "opaque-lsa disable", "отключить Opaque LSA"),
         ("esr(config-ospf)#", "maximum-paths 4", "ECMP: 1–32, по умолчанию 16")],
        [rowc("star", "preference", "Чтобы OSPF был предпочтительнее RIP (100), ставим значение меньше 100.", "b"),
         rowc("stop", "opaque-lsa disable", "Сосед узнает, что Opaque LSA не поддерживаются. Форма no — вернуть по умолчанию.", "v"),
         rowc("swap", "maximum-paths", "Сколько равноценных маршрутов ставить в таблицу. Форма no отключает ECMP.", "g")])

    cfg("Настройка: интерфейс", "Включение OSPF на интерфейсе", "Интерфейс, смотрящий в сторону соседа, привязываем к процессу и области.",
        [("esr(config)#", "interface gigabitethernet 1/0/1", ""),
         ("esr(config-if-gi)#", "ip address 203.0.113.1/30", ""),
         ("esr(config-if-gi)#", "ip ospf instance 100", "номер процесса"),
         ("esr(config-if-gi)#", "ip ospf area 8.0.0.0", "без area — попадёт в 0.0.0.0"),
         ("esr(config-if-gi)#", "ip ospf network-type point-to-point", ""),
         ("esr(config-if-gi)#", "ip ospf", "включаем OSPF на интерфейсе"),
         ("esr(config-if-gi)#", "do commit", "")],
        [rowc("bulb", "Area по умолчанию", "Не указали area — интерфейс окажется в backbone 0.0.0.0.", "y"),
         rowc("shield", "Firewall", "Разрешите в зоне безопасности протокол 89 (protocol-id 0x59) и правила между зонами.", "p"),
         rowc("ok", "Результат", "После commit/confirm OSPF начнёт рассылать Hello.", "g")])

    slide("Минимальная конфигурация", sc(
        head("Минимальная конфигурация двух маршрутизаторов", "Процесс 100, область 8.0.0.0, тип сети point-to-point."),
        '<div class="row2" style="flex:0 0 auto">' +
        ill("0 0 1000 180", blob(500, 95, 470, 80, "b", None, seed=.5) + link(260, 100, 740, 100, 6, "#7d9cc0") +
            router(260, 80, 160, "p", label="R1") + router(740, 80, 160, "b", label="R2") +
            pill(500, 60, "203.0.113.0/30", "w", 18, h=36)) +
        rowc("ok", "Совпадают", "Процесс (по соглашению), область, тип сети, маска. Различаются router-id и адреса.", "g") + '</div>',
        '<div class="row2 fill">' + steps(
            panel("pc", "R1", cli([("esr(config)#", "router ospf 100"), ("esr(config-ospf)#", "router-id 1.1.1.1"),
                                   ("esr(config-ospf)#", "area 8.0.0.0"), ("esr(config-ospf-area)#", "enable"),
                                   ("esr(config-ospf)#", "enable"), ("esr(config)#", "interface gi1/0/1"),
                                   ("esr(config-if-gi)#", "ip address 203.0.113.1/30"),
                                   ("esr(config-if-gi)#", "ip ospf instance 100"), ("esr(config-if-gi)#", "ip ospf area 8.0.0.0"),
                                   ("esr(config-if-gi)#", "ip ospf network-type point-to-point"), ("esr(config-if-gi)#", "ip ospf")]), "p"),
            panel("pc", "R2", cli([("esr(config)#", "router ospf 100"), ("esr(config-ospf)#", "router-id 2.2.2.2"),
                                   ("esr(config-ospf)#", "area 8.0.0.0"), ("esr(config-ospf-area)#", "enable"),
                                   ("esr(config-ospf)#", "enable"), ("esr(config)#", "interface gi1/0/1"),
                                   ("esr(config-if-gi)#", "ip address 203.0.113.2/30"),
                                   ("esr(config-if-gi)#", "ip ospf instance 100"), ("esr(config-if-gi)#", "ip ospf area 8.0.0.0"),
                                   ("esr(config-if-gi)#", "ip ospf network-type point-to-point"), ("esr(config-if-gi)#", "ip ospf")]), "b")) + '</div>'
    ))

    cfg("Аутентификация и cost", "Аутентификация, стоимость, приоритет", "Дополнительные параметры интерфейса.",
        [("esr(config-if-gi)#", "ip ospf authentication algorithm md5", ""),
         ("esr(config-if-gi)#", "ip ospf authentication key ascii-text Pa$$word1", "8–16 символов"),
         ("esr(config-if-gi)#", "ip ospf cost 10", "стоимость вручную"),
         ("esr(config-if-gi)#", "ip ospf priority 200", "0–255; 0 — не участвует в выборе DR"),
         ("esr(config-if-gi)#", "ip ospf mtu-ignore", "не сверять MTU")],
        [rowc("lock", "Аутентификация", "Пароли у соседей не совпали — соседство не установится.", "p"),
         rowc("sum", "Стоимость", "Задают вручную при разных вендорах. Меньше cost — предпочтительнее путь.", "y"),
         rowc("star", "Приоритет", "Выше — больше шансов стать DR; 0 — никогда.", "b")], typ=False)

    cfg("Таймеры", "Таймеры OSPF", "Настраиваются на интерфейсе в сторону соседа и должны совпадать.",
        [("esr(config-if-gi)#", "ip ospf hello-interval 10", "по умолчанию 10 с"),
         ("esr(config-if-gi)#", "ip ospf dead-interval 40", "по умолчанию 40 с"),
         ("esr(config-if-gi)#", "ip ospf poll-interval 120", "Hello для NBMA"),
         ("esr(config-if-gi)#", "ip ospf retransmit-interval 5", "повтор LSU без подтверждения")],
        [rowc("clock", "Dead = 4 × Hello", "10/40 с по умолчанию, для NBMA — 30/120 с.", "b"),
         rowc("ok", "Только ESR и нет NBMA", "Значения по умолчанию можно не трогать.", "g"),
         rowc("bolt", "Нужна быстрая реакция", "Настраивайте BFD, а не уменьшайте таймеры до предела.", "y")], typ=False)

    cfg("Проверка конфигурации", "Проверка конфигурации", "Что включить и что смотреть, когда соседство не поднимается.",
        [("esr(config-ospf)#", "log-adjacency-changes", "изменения смежности в консоль"),
         ("esr#", "show ip ospf", "процесс"), ("esr#", "show ip ospf interface", "роли, cost, таймеры"),
         ("esr#", "show ip ospf neighbor", "состояния соседей"), ("esr#", "show ip ospf database", "LSDB"),
         ("esr#", "show ip route", "таблица маршрутизации")],
        [rowc("stop", "Маски, таймеры, тип сети", "Не совпадают маска подсети, Hello/Dead или тип сети OSPF.", "p"),
         rowc("stop", "Забыли применить", "Нет commit/confirm или enable в области/процессе.", "y"),
         rowc("stop", "Межсетевой экран", "Не отключён и не настроен — Hello не проходят.", "b"),
         rowc("stop", "Анонсирование", "Неправильно настроены анонсирование и фильтрация.", "v")], typ=False)
