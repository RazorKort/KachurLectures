# -*- coding: utf-8 -*-
"""Блок 4: удалённое управление (telnet/ssh), дата и время, баннеры, команды show."""

from _r23_lib import (slide, head, sc, g, col, card, step, steps, irow, foot, tag, tags,
                      table, cli, imgcard, fig, arrow, link, pill, txt, circ_num,
                      router, switch, pc, server, cloudfig, laptop, packet, netlabel,
                      okmark, ban, shieldfig)


def build():
    # ------------------------------------------------------------------ 48
    slide("Удалённое управление", sc(
        head("Удалённое управление <em>маршрутизатором</em>",
             "Прямой доступ консольным проводом есть не всегда — устройство может стоять в другом городе."),
        g("g2",
          step(card("Telnet", (
              "<p>Протокол удалённого терминального управления. Данные передаются "
              "<b>в открытом (незашифрованном) виде</b>.</p>"
              + irow("stop", "Злоумышленник, перехватив трафик, увидит <b>пароль открытым текстом</b>", "r")
              + irow("warn", "На сегодняшний день считается <b>небезопасным</b>", "a")
              + irow("ok", "Прост и всегда под рукой — но только в изолированной лаборатории", "")
          ), num="1", tone="red")),
          step(card("SSH", (
              "<p>Secure Shell — тот же терминальный доступ, но передача данных идёт "
              "<b>в зашифрованном виде</b>.</p>"
              + irow("lock", "Пароль и команды защищены от перехвата", "g")
              + irow("shield", "Поддерживается маршрутизаторами ESR", "g")
              + irow("star", "<b>Рекомендуемый</b> способ удалённого доступа", "")
          ), num="2", tone="grn")),
          ),
        step(foot("Маршрутизаторы ESR поддерживают работу и с telnet, и с ssh. Выбор очевиден: "
                  "там, где есть сеть общего пользования, используют только <b>ssh</b>.", "warn")),
    ))

    # ------------------------------------------------------------------ 49
    slide("Почему telnet опасен", sc(
        head("Что видит <em>перехватчик трафика</em>",
             "Один и тот же пароль в двух протоколах."),
        step(card(None, fig("0 0 1040 290",
            '<g class="sq go-f">'
            + laptop(90, 70, w=74, label="Инженер")
            + arrow(135, 70, 420, 70, tone="r", w=5)
            + router(500, 70, w=110, label="R1")
            + '<rect x="190" y="20" width="200" height="32" rx="10" fill="#ffe6ec"/>'
            + txt(290, 42, "admin / P@ssw0rd!", fs=14, color="#b11c3d", mono=True)
            + txt(640, 60, "telnet — открытый текст", fs=15, color="#b11c3d", anchor="start")
            + txt(640, 82, "пароль читается как есть", fs=13, color="#5d5682", anchor="start", weight=600)
            + '</g>'
            + '<g class="sq go-f">'
            + laptop(90, 200, w=74, label="Инженер")
            + arrow(135, 200, 420, 200, tone="g", w=5)
            + router(500, 200, w=110, label="R1")
            + '<rect x="190" y="150" width="200" height="32" rx="10" fill="#e1f7ee"/>'
            + txt(290, 172, "8f3a…c1d9 (шифр)", fs=14, color="#0c7a49", mono=True)
            + txt(640, 190, "ssh — зашифрованный канал", fs=15, color="#0c7a49", anchor="start")
            + txt(640, 212, "перехват бесполезен", fs=13, color="#5d5682", anchor="start", weight=600)
            + '</g>'
            + '<g class="sq pop">' + shieldfig(960, 200, w=52, tone="g") + '</g>'
            + '<g class="sq pop">'
            + '<circle cx="290" cy="110" r="18" fill="#f0486b"/>'
            + txt(290, 116, "!", fs=20, color="#fff", weight=900)
            + '</g>'
        ), tone="w")),
        step(foot("Если злоумышленник заполучит и проанализирует трафик telnet, он получит "
                  "пароль, переданный открытым текстом — и полный доступ к устройству.", "warn")),
    ), scen="sq")

    # ------------------------------------------------------------------ 50
    slide("Настройка SSH-сервера", sc(
        head("Поднимаем <em>SSH-сервер</em> на ESR",
             "Одна команда в глобальной конфигурации плюс обязательные commit и confirm."),
        g("g2",
          step(card("Команда", cli([
              ("esr-200#", "configure"),
              ("esr-200(config)#", "ip ssh server"),
              ("esr-200(config)#", "exit"),
              ("esr-200#", "commit"),
              ("esr-200#", "confirm"),
          ], typ=True) + "<p style='margin-top:8px'>Синтаксис: <span class='kv'>[no] ip ssh server "
                         "[ vrf &lt;имя&gt; ]</span></p>", num="1", tone="dark")),
          col(
            step(card("То же для telnet", "<p>Аналогичным образом вместо ssh-сервера можно "
                      "настроить telnet-сервер командой <span class='kv'>ip telnet server</span> "
                      "и подключаться по telnet — но недостатки этого протокола описаны выше.</p>",
                      num="2", tone="vio")),
            step(card("Проверка доступности", (
                irow("term", "<b>PuTTY</b> — графический ssh-клиент для Windows", "")
                + irow("cpu", "Встроенный клиент <span class='kv'>ssh</span> в Linux и Windows 10+", "c2")
                + irow("link", "Любое приложение, умеющее подключаться к ssh-серверам", "m")
            ), num="3", tone="cya")),
          ),
          ),
    ), scen="type")

    # ------------------------------------------------------------------ 51
    slide("Подключение по SSH", sc(
        head("Подключаемся <em>ssh-клиентом</em>",
             "Синтаксис консольного клиента проще, чем заполнение полей в графическом приложении."),
        g("g2",
          step(card("Синтаксис и сеанс", cli([
              ("//", "ssh <имя учётной записи>@<ip-адрес интерфейса маршрутизатора>"),
              "",
              ("user@user-PC:~$", "ssh admin@172.16.100.12"),
              "(admin@172.16.100.12) Password: ********",
              "",
              (">>", "esr-200#"),
          ], typ=True), num="1", tone="dark")),
          col(
            step(card("Что происходит по шагам", (
                irow("arr", "Клиент устанавливает соединение с <b>ssh-сервером</b> устройства", "")
                + irow("key", "Маршрутизатор запрашивает <b>пароль</b> учётной записи", "c2")
                + irow("eye", "Символы пароля <b>экранируются</b> — длину не подсмотреть", "m")
                + irow("ok", "При верном пароле открывается консоль управления", "g")
            ), num="2", tone="vio")),
            step(foot("Если адрес пингуется, а соединение отклоняется — на устройстве просто "
                      "не поднят ssh-сервер или настройка не подтверждена командой confirm.", "note")),
          ),
          ),
    ), scen="type")

    # ------------------------------------------------------------------ 52
    slide("Дата и время", sc(
        head("Настройка <em>даты и времени</em>",
             "Без верного времени журналы событий бесполезны: непонятно, что и когда произошло."),
        g("g2",
          step(card("Установка вручную", cli([
              ("esr-200#", "set date 17:23:55 09 October 2023"),
              "2023-10-09T10:23:17+00:00 %TIME-I-INFO: System time was",
              "changed by user admin  Mon Oct 9 17:23:55 UTC 2023",
              "",
              ("esr-200#", "show date"),
              (">>", "\"Monday 17:27:46 UTC October 09 2023\""),
          ], typ=True), num="1", tone="dark")),
          step(card("Синтаксис set date", table(
              ["Поле", "Формат", "Допустимые значения"],
              [[("&lt;TIME&gt;", "mono"), ("HH:MM:SS", "mono"), "HH 0–23, MM 0–59, SS 0–59"],
               [("&lt;DAY&gt;", "mono"), "день месяца", "1–31"],
               [("&lt;MONTH&gt;", "mono"), "название месяца", "January … December"],
               [("&lt;YEAR&gt;", "mono"), "год", "2001–2037"]]
          ) + "<p style='margin-top:8px'>Полный вид: <span class='kv'>set date &lt;TIME&gt; "
              "[&lt;DAY&gt; &lt;MONTH&gt; [&lt;YEAR&gt;]]</span>. Команда выполняется "
              "<b>из привилегированного режима</b>.</p>", num="2", tone="vio")),
          ),
        step(foot("Просмотр текущих даты и времени — командой <span class='kv'>show date</span> "
                  "из привилегированного режима.", "")),
    ), scen="type")

    # ------------------------------------------------------------------ 53
    slide("Часовой пояс", sc(
        head("Настройка <em>часового пояса</em>",
             "Сдвиг в часах относительно Greenwich Mean Time: от gmt −12 до gmt +12."),
        g("g2",
          step(card("Команда", cli([
              ("esr-200#", "configure"),
              ("esr-200(config)#", "clock timezone gmt +7"),
              ("esr-200(config)#", "exit"),
              ("esr-200#", "commit"),
              ("esr-200#", "confirm"),
              "",
              ("esr-200#", "show date"),
              (">>", "\"Tuesday 00:53:22 GMT+7 October 10 2023\""),
          ], typ=True), num="1", tone="dark")),
          col(
            step(card("Важная деталь", (
                "<p>Если в конфигурации ничего не изменилось, устройство честно ответит:</p>"
                + cli([("!!", "Nothing to commit in configuration."),
                       ("!!", "You must commit some changes first.")])
                + "<p style='margin-top:8px'>Это не ошибка — просто новых изменений нет.</p>"
            ), num="2", tone="vio")),
            step(card("Зачем это нужно", (
                irow("clock", "Метки времени в <b>журналах событий</b> совпадут с реальностью", "")
                + irow("shield", "Корректная работа <b>сертификатов</b> и защищённых сессий", "c2")
                + irow("chart", "Совпадение времени на всех устройствах при разборе аварий", "m")
            ), num="3", tone="cya")),
          ),
          ),
    ), scen="type")

    # ------------------------------------------------------------------ 54
    slide("Синхронизация по NTP", sc(
        head("Время можно <em>не вводить вручную</em>",
             "Маршрутизаторы ESR умеют получать настройки даты и времени с ntp-сервера."),
        step(card(None, fig("0 0 1000 250",
            server(120, 110, w=66, label="NTP-сервер", sub="эталонное время")
            + cloudfig(400, 106, 190, 96, "Сеть", None, "cb", fs=16)
            + router(720, 110, w=120, label="R1")
            + switch(900, 110, w=92, label="SW1")
            + arrow(170, 110, 300, 110, tone="c", w=4.5, cls="sq go-f")
            + arrow(500, 110, 650, 110, tone="c", w=4.5, cls="sq go-f")
            + arrow(780, 110, 850, 110, tone="c", w=4.5, cls="sq go-f")
            + '<g class="sq go-f">'
            + pill(500, 196, "все устройства сети живут по одному времени", "cb", fs=14.5, h=30)
            + '</g>'
        ), tone="w")),
        g("g2",
          step(card("Ручная установка", "<p>Подходит для одного устройства в лаборатории. "
                    "На большой сети время быстро разъедется.</p>", num="1", tone="amb")),
          step(card("Синхронизация NTP", "<p>Все устройства берут время у одного источника. "
                    "Это единственный рабочий вариант для реальной сети.</p>", num="2", tone="grn")),
          ),
    ), scen="sq")

    # ------------------------------------------------------------------ 55
    slide("Баннерные сообщения", sc(
        head("<em>Баннерные</em> сообщения",
             "Текст, который видит каждый подключившийся к оборудованию."),
        g("g2",
          step(card("Два типа баннеров", (
              table(["Команда", "Когда выводится"],
                    [[("banner login", "mono"), "перед авторизацией"],
                     [("banner exec", "mono"), "после успешной авторизации"]])
              + "<p style='margin-top:8px'>Снять баннер: <span class='kv'>no banner login</span> "
                "или <span class='kv'>no banner exec</span>.</p>"
              + irow("warn", "При написании баннеров <b>не допускаются пробелы</b>", "a")
              + irow("gear", "Настраиваются из режима глобальной конфигурации", "")
          ), num="1", tone="vio")),
          step(card("Что туда пишут", (
              irow("hello", "Приветствие: «Добро пожаловать!»", "")
              + irow("warn", "Предупреждение: обдумывайте действия при настройке", "a")
              + irow("cal", "Расписание технических работ и возможных простоев", "c2")
              + irow("user", "Контакты ответственного инженера", "m")
          ), num="2", tone="cya")),
          ),
        step(card("Настройка", cli([
            ("esr-200#", "configure"),
            ("esr-200(config)#", "banner login Router-esr-200"),
            ("esr-200(config)#", "banner exec Connect_Router_esr_200"),
            ("esr-200(config)#", "exit"),
            ("esr-200#", "commit"),
            ("esr-200#", "confirm"),
        ], typ=True), tone="dark")),
    ), scen="type")

    # ------------------------------------------------------------------ 56
    slide("Баннеры глазами пользователя", sc(
        head("Что увидит <em>подключающийся</em>",
             "Сначала banner login, после ввода пароля — banner exec."),
        g("g2",
          step(card("Сеанс подключения", cli([
              ("user@user-PC:~$", "ssh admin@172.16.100.12"),
              "",
              (">>", "Router-esr-200"),
              ("//", "— это banner login, до ввода пароля"),
              "",
              "(admin@172.16.100.12) Password: ********",
              "",
              (">>", "Connect_Router_esr-200"),
              ("//", "— это banner exec, после авторизации"),
              "",
              ("esr-200#", ""),
          ]), num="1", tone="dark")),
          col(
            step(card("Зачем это на практике", (
                irow("eye", "Инженер сразу видит, <b>к какому устройству</b> подключается", "")
                + irow("shield", "Юридическое предупреждение о недопустимости доступа", "g")
                + irow("flag", "Отметка о плановых работах — коллега не полезет настраивать", "m")
            ), num="2", tone="vio")),
            step(foot("Не забывайте: после ввода настроек их нужно <b>применить и подтвердить</b> "
                      "командами commit и confirm.", "note")),
          ),
          ),
    ))

    # ------------------------------------------------------------------ 57
    slide("Команда show", sc(
        head("Проверка соединения: <em>команда show</em>",
             "Основная команда для просмотра информации, выполняется из привилегированного режима."),
        g("g2",
          step(card("Список опций по знаку «?»", cli([
              ("esr-200#", "show ?"),
              "aaa                Show aaa information",
              "alarm              Show alarm information",
              "archive            Show archive information",
              "arp                Show the entries in the ARP cache",
              "bfd                Show BFD",
              "bgp                Show BGP information",
              "bootvar            Show boot parameters",
              "candidate-config   Show the candidate configuration",
              "…",
          ]), num="1", tone="dark")),
          step(card("Самые частые команды", table(
              ["Команда", "Что показывает"],
              [[("show running-config", "mono"), "текущие настройки устройства"],
               [("show interfaces status", "mono"), "состояние всех интерфейсов"],
               [("show arp", "mono"), "содержимое кэша ARP-таблицы"],
               ([("show ip route", "mono"), "таблицу маршрутизации с лучшими маршрутами"], "hi"),
               [("show version", "mono"), "версию программного обеспечения"],
               [("show date", "mono"), "текущие дату и время"]]
          ) + "<p style='margin-top:8px'>У команды <span class='kv'>show ip route</span> есть "
              "ключ <span class='kv'>all</span> — он выводит <b>все</b> маршруты, а не только "
              "лучшие.</p>", num="2", tone="vio")),
          ),
        step(foot("Знак вопроса <span class='kv'>?</span> работает в любом месте команды и "
                  "показывает допустимые продолжения — это встроенная справка CLI.", "")),
    ))

    # ------------------------------------------------------------------ 58
    slide("Разбор вывода интерфейсов", sc(
        head("<em>show interfaces status</em> подробно",
             "Команда выводит информацию обо всех интерфейсах: физических и виртуальных."),
        g("g21",
          step(card("Фильтр по типу интерфейса", cli([
              ("esr-200#", "show interfaces status ?"),
              "bridge                Show bridge interface's state",
              "e1                    Show e1 interface's state",
              "fortygigabitethernet  Show fortygigabitethernet state",
              "gigabitethernet       Show gigabitethernet state",
              "loopback              Show loopback interface's state",
              "modem                 Show modem interface's state",
              "multilink             Show multilink interface's state",
              "port-channel          Show port-channel state",
              "tengigabitethernet    Show tengigabitethernet state",
          ]), num="1", tone="dark")),
          col(
            step(card("Что ещё показывает команда", (
                irow("box", "Размер окна и <b>MTU</b> интерфейса", "")
                + irow("link", "<b>MAC-адреса</b> интерфейсов", "c2")
                + irow("clock", "Время <b>последнего изменения</b> состояния", "m")
                + irow("eye", "И физические, и виртуальные интерфейсы", "g")
            ), num="2", tone="vio")),
            step(card("Один интерфейс", cli([
                ("esr-200#", "show interfaces status gigabitethernet 1/0/1"),
                "",
                "Interface               gi1/0/1",
                "Administrative state    Up",
                (">>", "Link state              Up"),
                "Speed                   1000M",
                "Duplex                  full-duplex",
                "MTU                     1500",
                "MAC address             a8:f9:4b:00:11:22",
            ]), num="3", tone="dark")),
          ),
          ),
    ))

    # ------------------------------------------------------------------ 59
    slide("Практикум · порядок команд", sc(
        head("Практикум: <em>соберите настройку интерфейса</em>",
             "Нажимайте команды в том порядке, в каком их вводят на маршрутизаторе."),
        '<div id="cfgsim" style="display:flex;flex-direction:column;gap:12px;flex:1 1 auto;min-height:0">'
        + card("Доступные команды", '<div id="cfpool" class="g g4"></div>', tone="vio")
        + card("Ваша последовательность", '<div id="cfout"></div>', tone="w")
        + card(None, '<div class="note" id="cfnote"></div>'
               '<div class="ui" style="margin-top:8px">'
               '<button id="cfreset" class="pri">Заново</button>'
               '<span class="stat"><span>собрано <b id="cfcnt">0 / 7</b></span></span></div>', tone="w")
        + '</div>',
    ))
