# -*- coding: utf-8 -*-
"""Слайды 1–15: введение, пропускная способность, производительность, overhead."""
from _g12_lib import (slide, head, card, ul, res, bub, chain, table, grid, step,
                      bar, ico)


def build():
    # ------------------------------------------------------------ 1. титул
    slide("Титул", "", f'''
<div class="cover">
  <span class="pill">Глава 12 · Компьютерные сети</span>
  <h1>Характеристики<br><em>компьютерных сетей</em></h1>
  <div class="ln"></div>
  <p class="sub" style="font-size:clamp(14px,1.4vw,21px)">
    Пропускная способность и производительность, накладные расходы, доступность,
    надёжность, масштабируемость, безопасность и стоимость сети.</p>
  <div class="meta">
    <span class="pill">30 слайдов</span>
    <span class="pill">2 тренажёра</span>
    <span class="pill">8 вопросов</span>
    <span class="pill">← → шаги · R прогон · Esc содержание</span>
  </div>
</div>''')

    # ------------------------------------------------------------ 2. цели
    slide("Цель лекции",
          head("Цель лекции", "Что вы должны унести с этой главы."),
          grid(3, [
              step(card("Набор характеристик", "01", "net",
                        "<p>Знать основные характеристики компьютерной сети и понимать, "
                        "какую сторону её работы описывает каждая из них.</p>" +
                        ul(["Пропускная способность и производительность",
                            "Доступность и надёжность",
                            "Масштабируемость",
                            "Безопасность и стоимость"]))),
              step(card("Понятийный аппарат", "02", "book",
                        "<p>Различать понятия, которые в быту путают между собой.</p>" +
                        ul(["Теоретический максимум против фактического объёма",
                            "Полезные данные против служебных",
                            "Отказоустойчивость против резервирования"]), dark=True)),
              step(card("Оценка готовой сети", "03", "scale",
                        "<p>Уметь оценить правильность построения сети: соответствует ли "
                        "она заявленным параметрам и требованиям организации.</p>" +
                        res("Характеристики — это язык, на котором заказчик и инженер "
                            "договариваются о том, какая сеть нужна."))),
          ]))

    # ------------------------------------------------------------ 3. зачем
    slide("Зачем оценивать сеть",
          head("Зачем оценивать сеть",
               "В прошлых главах разбирали, как сеть устроена и работает. Теперь — как понять, "
               "что она построена правильно."),
          grid(3, [
              step(card("Что уже известно", "01", "layers",
                        "<p>Технологии локальных сетей, построение и функционирование, "
                        "отправка информации устройствами, уровни взаимодействия.</p>" +
                        "<p>Этого достаточно, чтобы сеть <b>заработала</b>. Но не достаточно, "
                        "чтобы сказать, что она <b>хорошая</b>.</p>")),
              step(card("Какие вопросы остаются", "02", "eye",
                        ul(["Правильно ли построена сеть?",
                            "Соответствует ли она выбранным параметрам?",
                            "Отвечает ли основным требованиям организации?",
                            "Не станет ли она причиной опасности для сотрудников "
                            "и организации в целом?"], "ask"), dark=True)),
              step(card("Что делает инженер", "03", "gear",
                        "<p>При разработке и построении сети нужно учитывать множество "
                        "факторов и параметров.</p>" +
                        ul(["На этапе проектирования — заложить показатели",
                            "В процессе эксплуатации — сверять соответствие",
                            "По результатам — планировать изменения"]) +
                        res("Характеристики сети измеряются не один раз при сдаче, "
                            "а всё время, пока сеть живёт."))),
          ]))

    # ------------------------------------------------------------ 4. элементы
    slide("Элементы и характеристики сети",
          head("Элементы и характеристики сети",
               "Слева — из чего сеть состоит. Справа — что она должна обеспечивать."),
          f'''<div class="g g3" style="align-items:start">
{step(card("Элементы сети — что входит в сеть", icon="pkg", dark=True, body=
     ul(["<b>Устройства</b> — компьютеры, серверы, маршрутизаторы, коммутаторы",
         "<b>Стандарты</b> — правила, обеспечивающие совместимость устройств",
         "<b>Организации</b> — разрабатывают стандарты (IEEE, IETF)",
         "<b>Среды передачи</b> — кабели, оптоволокно, радиоканалы",
         "<b>Протоколы</b> — наборы правил обмена данными",
         "<b>Программное обеспечение</b> — ОС, сетевые службы, приложения"])))}
{step(f'<div class="col" style="align-items:center;justify-content:center;height:100%">{_cloudnet()}</div>')}
{step(card("Характеристики сети — что сеть обеспечивает", icon="chart", body=
     ul(["<b>Топология</b> — структура и способ соединения устройств",
         "<b>Надёжность</b> — стабильная и бесперебойная работа",
         "<b>Масштабируемость</b> — возможность расширения",
         "<b>Доступность</b> — доступ к ресурсам для авторизованных пользователей",
         "<b>Безопасность</b> — защита данных от несанкционированного доступа",
         "<b>Стоимость</b> — затраты на оборудование, внедрение и поддержку",
         "<b>Скорость</b> — производительность и скорость передачи данных"])))}
</div>''')

    # ------------------------------------------------------------ 5. пропускная способность
    slide("Пропускная способность", head(
        'Пропускная способность <em>(bandwidth)</em>',
        "Количество бит, переданных за одну секунду, и производные от этой единицы."),
        f'''
{step(card("Определение", icon="wave", dark=True, body=
     "<p style='font-size:clamp(13px,1.1vw,17px)'><b>Пропускная способность (bandwidth)</b> — "
     "это количество бит, переданных за одну секунду <b>(бит/с)</b>, а также производные "
     "от этой единицы измерения.</p>"))}
<div style="height:14px"></div>
<div class="ladder">
{_lstep("бит/с","(b/s)","Базовая единица измерения","#2f6f63")}
<span class="mul">×1000 ›</span>
{_lstep("кбит/с","(kb/s)","1 кбит/с = 1000 бит/с","#2a7f6f")}
<span class="mul">×1000 ›</span>
{_lstep("Мбит/с","(Mb/s)","1 Мбит/с = 1000 кбит/с","#2d7fa8")}
<span class="mul">×1000 ›</span>
{_lstep("Гбит/с","(Gb/s)","1 Гбит/с = 1000 Мбит/с","#3a5fb8")}
</div>
<div style="height:14px"></div>
<div class="g g32">
{step(card("Что это значит на практике", icon="swap", body=
     "<p>Пропускная способность определяет, <b>сколько данных можно передать за секунду</b> "
     "по каналу связи между отправителем и получателем.</p>" +
     "<p>Это <b>теоретическое, максимально возможное</b> значение. Фактически переданный "
     "объём данных почти всегда меньше — его описывает другая характеристика, "
     "производительность сети.</p>"))}
{step(bub("Чем больше пропускная способность, тем быстрее передаются данные. "
          "Но «быстрее» здесь — про потолок канала, а не про то, что вы реально получите.","dn"))}
</div>''', scen="ladder")

    # ------------------------------------------------------------ 6. Ethernet
    slide("Стандарты Ethernet", head(
        "Стандарты Ethernet",
        "Рост пропускной способности проводных локальных сетей."),
        f'''
{step(table(["Год","Стандарт IEEE","Название","Пропускная способность"], [
  ["1983","802.3","Ethernet","<span class='mono'>10 Мбит/с</span>"],
  ["1995","802.3u","Fast Ethernet","<span class='mono'>100 Мбит/с</span>"],
  ["1998–1999","802.3z / 802.3ab","Gigabit Ethernet","<span class='mono'>1 Гбит/с</span>"],
  ["2002","802.3ae","10 Gigabit Ethernet","<span class='mono'>10 Гбит/с</span>"],
  ["2010","802.3ba","40G / 100G Ethernet","<span class='mono'>40 и 100 Гбит/с</span>"],
  ["2016–2017","802.3bs","200G / 400G Ethernet","<span class='mono'>200 и 400 Гбит/с</span>"],
]))}
<div style="height:14px"></div>
<div class="g g3">
{step(card("Шаг в десять раз", "01", "grow",
     "<p>Каждое следующее поколение Ethernet поднимает потолок примерно на порядок. "
     "Переход с 1 Гбит/с на 10 Гбит/с — один из способов увеличить эффективную "
     "производительность сети.</p>"))}
{step(card("Стандарт ≠ ваша скорость", "02", "alert", dark=True, body=
     "<p>Стандарт задаёт пропускную способность канала. Реально полученная скорость "
     "зависит от нагрузки, качества линии и доли служебного трафика.</p>" +
     res("Гигабитный порт не гарантирует гигабит полезных данных.", bad=True)))}
{step(card("Кабель тоже имеет категорию", "03", "link",
     "<p>Витая пара категории 5e рассчитана на 1 Гбит/с, 6 и 6a — на 10 Гбит/с на "
     "ограниченной длине. Оптика снимает ограничение по расстоянию.</p>" +
     res("Сеть работает по самому слабому звену тракта.")))}
</div>''')

    # ------------------------------------------------------------ 7. производительность
    slide("Производительность сети", head(
        'Производительность сети <em>(network performance)</em>',
        "Пропускная способность не рассматривается без параметра производительности."),
        f'''<div class="g g2">
{step(card("Пропускная способность", "01", "wave",
     "<p>Описывает <b>теоретическое</b> — максимально возможное — значение количества "
     "переданной информации.</p>" +
     "<p>Это свойство канала и оборудования: сколько бит они в принципе способны "
     "пропустить за секунду.</p>" +
     res("Потолок. Он не зависит от того, что именно вы передаёте.")))}
{step(card("Производительность сети", "02", "gauge", dark=True, body=
     "<p><b>Производительность сети (network performance)</b> — это фактический объём "
     "данных, передаваемых между узлами за единицу времени, обычно за 1 секунду.</p>" +
     "<p>Она зависит не только от канала, но и от того, <b>какие данные</b> мы передаём "
     "и <b>как именно</b> они передаются.</p>" +
     res("Факт. Измеряется на работающей сети под реальной нагрузкой.")))}
</div>
<div style="height:14px"></div>
{step(card("Почему это две разные характеристики", icon="bulb", tint=True, body=
     "<p>Производительность сети — <b>не фиксированное значение</b>. Показания меняются "
     "в зависимости от объёма и количества пакетов, проходящих через сеть, от условий "
     "передачи и от множества факторов.</p>" +
     "<p>Поэтому корректно говорить не «скорость сети равна X», а «при такой-то нагрузке "
     "измеренная производительность составила X».</p>"))}''')

    # ------------------------------------------------------------ 8. T = G + O
    slide("Формула T = G + O", head(
        "Из чего складывается производительность сети",
        "Общая производительность состоит из двух составляющих: полезной и служебной."),
        f'''
{step('''<div class="fz"><div class="f">
<span class="t">T</span> <span class="op">=</span> <span class="g">G</span>
<span class="op">+</span> <span class="o">O</span></div>
<div class="cap">T — производительность сети · G — эффективная производительность (goodput)
· O — накладные расходы (overhead)</div></div>''')}
<div style="height:14px"></div>
<div class="g g3">
{step(card("T — производительность сети", icon="gauge", body="<p>Фактическая скорость передачи данных (бит/с). Всё, что реально проходит "
     "через канал, вместе со служебной частью.</p>"))}
{step(card("G — эффективная производительность", icon="check", body="<p><b>Goodput.</b> Полезные данные, которые действительно доходят до получателя "
     "и имеют смысл для приложения.</p>"))}
{step(card("O — накладные расходы", icon="layers", body="<p><b>Overhead.</b> Служебные данные, необходимые для передачи: заголовки, "
     "служебные поля, повторные передачи и т. д.</p>"))}
</div>
<div style="height:14px"></div>
{step(_pipe())}''', scen="pipe")

    # ---------------------------------------------------- 8b. как увеличить G
    slide("Как увеличить G", head(
        "Как увеличить эффективную производительность",
        "Из формулы T = G + O следует, что полезную часть можно поднять двумя путями."),
        f'''<div class="g g2" style="align-items:start">
{step(card("Из формулы следует", icon="bulb", dark=True, body=
     '<div class="fz" style="padding:14px 18px;box-shadow:none"><div class="f" '
     'style="font-size:clamp(20px,2.6vw,34px)"><span class="g">G</span> '
     '<span class="op">=</span> <span class="t">T</span> <span class="op">−</span> '
     '<span class="o">O</span></div></div>'
     "<p style='margin-top:10px'>Увеличить эффективную производительность можно не только "
     "за счёт повышения пропускной способности канала, но и за счёт "
     "<b>уменьшения накладных расходов</b>.</p>" +
     ul(["<b>Увеличить пропускную способность канала</b> — например, перейти "
         "с 1 Гбит/с на 10 Гбит/с. Дорого, требует замены оборудования.",
         "<b>Уменьшить накладные расходы</b> — оптимизировать настройки, использовать "
         "более эффективные протоколы, сократить количество повторных передач. "
         "Дёшево, но требует инженерной работы."]) +
     res("Производительность сети — это баланс между полезными данными "
         "и служебным трафиком.")))}
{step(card("Тренажёр: доля накладных расходов", icon="calc", body=
     "<p>Канал <b>T = 1000 Мбит/с</b>. Подвиньте ползунок — значения G и O "
     "пересчитаются.</p>"
     '<div class="ui"><label for="ovr">Overhead</label>'
     '<input id="ovr" type="range" min="0" max="40" step="1" value="22">'
     '<span class="pill b" id="vP">22 %</span></div>'
     '<div class="g g2" style="margin-top:12px">'
     '<div><div style="font-size:11.5px;color:#5c7d77">G — полезные данные</div>'
     '<div class="big" id="vG" style="color:#1f9b4f">780 Мбит/с</div></div>'
     '<div><div style="font-size:11.5px;color:#5c7d77">O — служебные данные</div>'
     '<div class="big" id="vO" style="color:#2a7cc4">220 Мбит/с</div></div></div>'
     '<div style="margin-top:14px">' + _pipe_mini() + '</div>'))}
</div>''')

    # ------------------------------------------------------------ 9. факторы
    slide("Факторы производительности", head(
        "Факторы, влияющие на производительность сети",
        "Фактическая производительность сети зависит от множества факторов."),
        grid(6, [
            step(card("Качество соединения", "01", "link", dark=True, body=
                 "<p>Состояние кабелей, разъёмов, уровень сигнала Wi-Fi, стабильность "
                 "линии связи.</p>")),
            step(card("Радиочастотные и электромагнитные помехи", "02", "wifi", dark=True, body=
                 "<p>Другие беспроводные сети, бытовые устройства, электромагнитные "
                 "источники создают помехи.</p>")),
            step(card("Приоритет трафика и отбрасывание пакетов", "03", "queue", dark=True, body=
                 "<p>Часть пакетов может быть отброшена на этапе обработки выходных "
                 "очередей порта из-за низкого приоритета.</p>")),
            step(card("Отбрасывание и повторная пересылка", "04", "trash", dark=True, body=
                 "<p>При ошибках передачи данные могут быть отброшены и отправлены "
                 "заново — это увеличивает задержки и снижает полезную скорость.</p>")),
            step(card("Ошибки в формировании данных", "05", "doc", dark=True, body=
                 "<p>Некорректная работа приложений, ошибки при подготовке данных "
                 "к отправке приводят к повторной передаче или потере пакетов.</p>")),
            step(card("Накладные расходы протоколов", "06", "layers", dark=True, body=
                 "<p>Заголовки и служебные поля не несут полезной информации, но занимают "
                 "пропускную способность.</p>" +
                 '<div style="display:flex;gap:5px;margin-top:9px;flex-wrap:wrap">'
                 '<span class="pill b">Заголовок</span>'
                 '<span class="pill g">Полезные данные</span>'
                 '<span class="pill d">Служебные поля</span></div>')),
        ]))

    # ------------------------------------------------------------ 10. нагрузка
    slide("Почему измеренная скорость ниже", head(
        "Почему измеренная скорость может быть ниже?",
        "Показания производительности сети зависят от объёма и количества пакетов, "
        "проходящих через неё."),
        f'''<div class="g g2" style="align-items:start">
{step(card("Небольшая нагрузка", icon="check", body=
     "<p>При низкой нагрузке и передаче небольших пакетов скорость может быть "
     "близка к пропускной способности.</p>"
     '<div style="margin:12px 0 6px;display:flex;justify-content:space-between;'
     'font-size:11.5px;color:#5c7d77"><span>Измеренная скорость</span>'
     '<span class="pill g">≈ пропускной способности</span></div>'
     + bar("92%", "green") +
     '<ul class="ck loadlist" style="margin-top:12px">'
     "<li>Небольшие пакеты данных</li>"
     "<li>Минимальные задержки</li>"
     "<li>Сеть не перегружена</li></ul>", cls="", dark=False).replace(
         '<div class="bar green"><i data-w="92%" style="width:0"></i></div>',
         '<div class="bar green" id="loadA"><i data-w="92%" style="width:0"></i></div>'))}
{step(card("Пиковая нагрузка", icon="alert", dark=True, body=
     "<p>При высоких нагрузках и передаче больших пакетов реальная скорость будет "
     "значительно ниже.</p>"
     '<div style="margin:12px 0 6px;display:flex;justify-content:space-between;'
     'font-size:11.5px;color:#9dc4bc"><span>Измеренная скорость</span>'
     '<span class="pill r">значительно ниже</span></div>'
     + bar("31%", "red") +
     '<ul class="ck minus loadlist" style="margin-top:12px">'
     "<li>Большой объём трафика и крупные пакеты</li>"
     "<li>Отбрасывание пакетов</li>"
     "<li>Повторная пересылка данных</li>"
     "<li>Уменьшение скользящего окна</li>"
     "<li>Снижение скорости для сохранения стабильности</li></ul>").replace(
         '<div class="bar red"><i data-w="31%" style="width:0"></i></div>',
         '<div class="bar red" id="loadB"><i data-w="31%" style="width:0"></i></div>'))}
</div>
<div style="height:14px"></div>
{step(card("Вывод", icon="bulb", tint=True, body=
     "<p>Производительность сети — это <b>не фиксированное значение</b>. "
     "Она зависит от текущей нагрузки, условий передачи и множества факторов. "
     "Поэтому измерение всегда привязано к условиям, в которых оно сделано.</p>"))}''',
        scen="load")

    # ------------------------------------------------------------ 11. кадр Ethernet
    slide("Накладные расходы: преамбула", head(
        'Накладные расходы <em>(overhead)</em>: преамбула',
        "Часть трафика, необходимая для работы сети, но не содержащая полезной информации."),
        f'''
{step(card("Преамбула в Ethernet", "01", "pkg", dark=True, body=
     "<p>Преамбула в заголовке кадра Ethernet состоит из <b>32 байт</b>, представляющих "
     "собой комбинацию нулей и единиц. Они служат для уведомления приёмника о начале "
     "передачи кадра, но не содержат полезной информации.</p>"))}
<div style="height:14px"></div>
{step(_eframe())}
<div style="height:14px"></div>
<div class="g g2">
{step(card("Зачем она нужна", icon="wave", body=
     "<p>Преамбула помогает приёмнику синхронизироваться и понять, что начинается "
     "новый кадр. Без неё приёмник не определит границу кадра в потоке бит.</p>" +
     res("Служебные данные не бесполезны — без них сеть не будет работать. "
         "Но в полезную скорость они не попадают.")))}
{step(card("Накладные расходы — это", icon="layers", tint=True, body=
     "<p>Информация, которая передаётся по сети, но не воспринимается "
     "непосредственно как полезная для конечного пользователя.</p>" +
     ul(["Преамбула и SFD",
         "MAC-адреса получателя и отправителя",
         "Поле типа и контрольная сумма FCS",
         "Межпакетный разрыв",
         "Повторные передачи"])))}
</div>''', scen="frame")

    # ------------------------------------------------------------ 12. IPG
    slide("Межпакетный разрыв (IPG)", head(
        'Межпакетный разрыв <em>(Interpacket Gap)</em>',
        "После каждого кадра нужно дать понять приёмнику, что передача прекращена."),
        f'''<div class="g g32" style="align-items:start">
<div class="col">
{step(card("Как это работает", "02", "clock", dark=True, body=
     "<p>После каждого кадра необходимо дать понять устройству-приёмнику, что передача "
     "прекращена. Для этого используется межпакетный разрыв (interpacket gap) размером "
     "<b>96 бит</b>.</p>"
     "<p>Во время этого интервала в канале нет передачи данных, то есть он находится "
     "в простое, хотя это не несёт полезной информации. Тем не менее, это необходимый "
     "элемент в передаче данных.</p>"))}
{step(_ipg())}
</div>
<div class="col">
{step(card("Сколько это по времени", icon="gauge", body=
     "<p>Время, которое затрачивается на передачу этих 96 бит, зависит от скорости "
     "сетевого адаптера.</p>" +
     table(["Скорость","Длительность IPG"], [
       ["<span class='mono'>10 Мбит/с</span>","<span class='mono'>9,6 мкс</span>"],
       ["<span class='mono'>100 Мбит/с</span>","<span class='mono'>0,96 мкс</span>"],
       ["<span class='mono'>1 Гбит/с</span>","<span class='mono'>96 нс</span>"],
       ["<span class='mono'>10 Гбит/с</span>","<span class='mono'>9,6 нс</span>"],
     ])))}
{step(card("Почему это накладные расходы", icon="alert", tint=True, body=
     "<p>Канал в эти моменты свободен, но передать по нему ничего нельзя. "
     "При большом количестве мелких кадров суммарное время простоя становится "
     "заметной долей секунды.</p>" +
     res("Чем мельче кадры, тем выше доля overhead в общем трафике.", bad=True)))}
</div>
</div>''')

    # ------------------------------------------------------------ 13. TCP
    slide("Повторная передача в TCP", head(
        "Накладные расходы: повторная передача в TCP",
        "Протокол TCP также увеличивает накладные расходы."),
        f'''<div class="g g32" style="align-items:start">
<div class="col">
{step(card("Повторная передача", "03", "refresh", dark=True, body=
     "<p>Протокол TCP постоянно переотправляет сегменты, для которых не получено "
     "подтверждение <b>(ACK)</b> от приёмника.</p>"
     "<p>Это необходимо для обеспечения надёжной доставки данных, но увеличивает объём "
     "служебного трафика в сети.</p>"))}
{step(_tcp())}
</div>
<div class="col">
{step(card("Счётчик служебного трафика", icon="chart", body=
     '<div style="font-size:11.5px;color:#5c7d77">Повторно передано за сеанс</div>'
     '<div class="big"><span id="tCnt">0</span> КБ</div>'
     "<p style='margin-top:8px'>Каждый потерянный сегмент оплачивается дважды: "
     "сам сегмент плюс ожидание таймаута.</p>"))}
{step(card("Зависимость", icon="grow", tint=True, body=
     "<p>Чем больше потеря пакетов или выше нагрузка на сеть, тем больше повторных "
     "передач и, соответственно, накладных расходов.</p>" +
     res("Рост нагрузки → рост потерь → рост повторов → ещё больше нагрузки. "
         "Петля затягивается сама на себе.", bad=True)))}
</div>
</div>''', scen="tcp")

    # ------------------------------------------------------------ 14. тест
    slide("Тест производительности", head(
        "Тест производительности сети",
        "Показывает, с какой скоростью передаются данные в вашей сети."),
        f'''
{step(_speedtest())}
<div style="height:14px"></div>
<div class="g g4">
{step(card("Скачивание (Download)", icon="dl", body=
     "<p><b>Мбит/с.</b> Скорость, с которой данные загружаются из интернета "
     "на ваше устройство.</p>" + res("Загрузка сайтов, файлов, видео.")))}
{step(card("Отправка (Upload)", icon="ul", body=
     "<p><b>Мбит/с.</b> Скорость, с которой данные отправляются с вашего устройства "
     "в интернет.</p>" + res("Отправка файлов, видеозвонки, работа в облаке.")))}
{step(card("Пинг (Ping)", icon="clock", body=
     "<p><b>мс.</b> Время, за которое данные доходят до сервера и возвращаются "
     "обратно. Чем меньше значение, тем быстрее отклик.</p>" +
     res("Особенно важен в онлайн-играх и видеозвонках.")))}
{step(card("Хорошие значения", icon="check", dark=True, body=
     table(["Параметр","Ориентир"], [
       ["Скачивание","<span class='mono'>&gt; 50 Мбит/с</span>"],
       ["Отправка","<span class='mono'>&gt; 50 Мбит/с</span>"],
       ["Пинг","<span class='mono'>&lt; 20 мс</span>"],
     ]) + res("Точные значения зависят от тарифного плана и типа подключения.")))}
</div>''')

    # ------------------------------------------------------------ 15. доступность
    slide("Доступность сети", head(
        'Доступность сети <em>(network availability)</em>',
        "Процентное соотношение времени, в котором сеть фактически использовалась, "
        "к общему времени периода."),
        f'''<div class="g g2" style="align-items:start">
{step(card("Определение", "01", "clock", dark=True, body=
     "<p><b>Доступность сети (network availability)</b> — это процентное соотношение "
     "времени, в котором сеть фактически использовалась <b>(uptime)</b>, к общему "
     "времени периода.</p>"
     "<p>По умолчанию за «время периода» принимают год — <b>365 дней</b>.</p>" +
     res("Время фактического использования вычисляется как общее время периода "
         "за вычетом времени простоя (downtime) — времени, в течение которого "
         "пользователи не могут использовать все сервисы сети.")))}
{step(card("Как считается", "02", "calc", body=
     '<div class="fml" style="margin:14px 0 16px">A = '
     '<span class="frac"><span class="n">t<sub>общ</sub> − t<sub>пр</sub></span>'
     '<span class="d">t<sub>общ</sub></span></span> × 100 %</div>' +
     table(["Обозначение","Что это"], [
       ["<span class='mono'>A</span>","доступность сети, %"],
       ["<span class='mono'>t<sub>общ</sub></span>","общее время периода (например, год)"],
       ["<span class='mono'>t<sub>пр</sub></span>","время простоя сети"],
     ])))}
</div>''')


# ---------------------------------------------------------------- вспомогательное


def _lstep(u, e, v, color):
    return (f'<div class="stp" style="background:linear-gradient(160deg,{color},'
            f'{color}d9)"><div class="u">{u}</div><div class="e">{e}</div>'
            f'<div class="v">{v}</div></div>')


def _cloudnet():
    return '''<svg viewBox="0 0 300 300" style="width:100%;max-width:300px" aria-hidden="true">
<defs><radialGradient id="cn" cx=".5" cy=".4" r=".7">
<stop offset="0" stop-color="#e8fbf6"/><stop offset="1" stop-color="#9fd8ca"/></radialGradient></defs>
<path d="M78 148c-19 0-34-15-34-34 0-18 14-33 32-34 6-24 28-42 54-42 24 0 45 15 52 36 3-1 6-1 9-1 19 0 34 15 34 34s-15 34-34 34z"
 fill="url(#cn)" stroke="#5fc3ad" stroke-width="1.6"/>
<text x="150" y="98" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="21" font-weight="750" fill="#0a2c28">Компьютерные</text>
<text x="150" y="122" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="21" font-weight="750" fill="#0a2c28">сети</text>
<text x="150" y="141" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" fill="#3f6660">объединяют устройства, людей и данные</text>
<g stroke="#19b89f" stroke-width="1.6" fill="none" opacity=".8">
<path d="M150 150v26M150 176l-54 30M150 176l54 30M96 206h108"/></g>
<g fill="#12423c">
<rect x="62" y="206" width="56" height="34" rx="4"/><rect x="122" y="212" width="56" height="28" rx="4"/>
<rect x="182" y="206" width="56" height="34" rx="4"/></g>
<g fill="#5ee0c8">
<rect x="70" y="214" width="40" height="3" rx="1.5"/><rect x="70" y="221" width="28" height="3" rx="1.5"/>
<rect x="130" y="220" width="40" height="3" rx="1.5"/>
<rect x="190" y="214" width="40" height="3" rx="1.5"/><rect x="190" y="221" width="28" height="3" rx="1.5"/></g>
<g fill="#3f6660" font-family="Segoe UI,sans-serif" font-size="10" text-anchor="middle">
<text x="90" y="256">устройства</text><text x="150" y="256">каналы</text><text x="210" y="256">сервисы</text></g>
</svg>'''


def _pipe():
    return '''<div class="c l" style="padding:10px 14px 6px">
<svg class="wide" viewBox="0 0 900 300" style="width:100%" aria-hidden="true">
<defs>
<linearGradient id="pg" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#7ae8a6"/><stop offset=".5" stop-color="#49d67f"/>
 <stop offset="1" stop-color="#2aa85d"/></linearGradient>
<linearGradient id="po" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#86c6fa"/><stop offset=".5" stop-color="#4aa3f0"/>
 <stop offset="1" stop-color="#2a7cc4"/></linearGradient>
</defs>
<text x="440" y="34" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="15"
 font-weight="700" fill="#0a2c28">Общая производительность T</text>
<path d="M120 48 v10 h640 v-10" fill="none" stroke="#5c7d77" stroke-width="1.4"/>
<rect x="18" y="150" width="90" height="80" rx="10" fill="#12423c"/>
<text x="63" y="183" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11.5" fill="#eafaf6">Данные</text>
<text x="63" y="199" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11.5" fill="#eafaf6">для передачи</text>
<rect x="120" y="150" width="640" height="80" rx="6" fill="#dceee9" stroke="#b7d8cf"/>
<rect id="pipeG" x="120" y="150" width="0" height="80" fill="url(#pg)"/>
<rect id="pipeO" x="120" y="150" width="0" height="80" fill="url(#po)"/>
<rect x="120" y="150" width="640" height="80" rx="6" fill="none" stroke="#0d332f" stroke-width="2" opacity=".35"/>
<ellipse cx="120" cy="190" rx="13" ry="40" fill="#0d332f" opacity=".25"/>
<ellipse cx="760" cy="190" rx="13" ry="40" fill="#0d332f" opacity=".18"/>
<rect x="772" y="150" width="110" height="80" rx="10" fill="#12423c"/>
<text x="827" y="183" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11.5" fill="#eafaf6">Полученные</text>
<text x="827" y="199" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11.5" fill="#eafaf6">полезные данные</text>
<g class="brk"><path id="brG" d="M120 250 v8 h500 v-8" fill="none" stroke="#2aa85d" stroke-width="1.6"/>
<text id="labG" x="370" y="276" text-anchor="middle" font-family="Segoe UI,sans-serif"
 font-size="13" font-weight="700" fill="#1f9b4f">G — полезные данные</text>
<text id="labG2" x="370" y="292" text-anchor="middle" font-family="Segoe UI,sans-serif"
 font-size="10.5" fill="#5c7d77">то, что доходит до получателя</text></g>
<g class="brk"><path id="brO" d="M620 250 v8 h140 v-8" fill="none" stroke="#2a7cc4" stroke-width="1.6"/>
<text id="labO" x="690" y="276" text-anchor="middle" font-family="Segoe UI,sans-serif"
 font-size="13" font-weight="700" fill="#2a7cc4">O — накладные расходы</text>
<text id="labO2" x="690" y="292" text-anchor="middle" font-family="Segoe UI,sans-serif"
 font-size="10.5" fill="#5c7d77">служебные данные</text></g>
</svg></div>'''


def _eframe():
    F = [("Преамбула","32 байта","srv","#49d67f"),("SFD","1 байт","srv","#49d67f"),
         ("MAC получателя","6 байт","srv","#8fb8b0"),("MAC отправителя","6 байт","srv","#8fb8b0"),
         ("Тип","2 байта","srv","#8fb8b0"),("Полезные данные","46 – 1500 байт","use","#19b89f"),
         ("FCS","4 байта","srv","#8fb8b0")]
    cells = "".join(
        f'<div class="fld" data-k="{k}" style="flex:{3 if k=="use" else 1} 1 90px;'
        f'border-radius:12px;padding:10px 11px;background:{c}22;border:1.4px solid {c};'
        f'min-width:88px">'
        f'<div style="font:700 12px Segoe UI,sans-serif;color:#0a2c28;line-height:1.2">{n}</div>'
        f'<div style="font:600 10.5px Consolas,monospace;color:#3f6660;margin-top:3px">{b}</div>'
        + ('<div style="font:600 10px Consolas,monospace;color:#1f9b4f;margin-top:5px">'
           '10101010 … 10101011</div>' if n == "Преамбула" else '')
        + '</div>'
        for n, b, k, c in F)
    return f'''<div class="c l">
<div style="display:flex;gap:7px;flex-wrap:wrap;align-items:stretch">{cells}</div>
<div style="display:flex;gap:7px;margin-top:9px;font-size:11px;color:#5c7d77">
<div style="flex:2;border-top:1.4px solid #b7d8cf;padding-top:5px">Служебные данные (накладные расходы)</div>
<div style="flex:3;border-top:1.4px solid #19b89f;padding-top:5px;color:#0e8d78">Полезная информация</div>
</div>
<div id="ovShare" style="margin-top:12px;display:flex;gap:10px;align-items:center;flex-wrap:wrap">
<span class="pill b">Минимальный кадр: 64 байта данных + 26 байт служебных</span>
<span class="pill r">доля overhead ≈ 29 %</span>
<span class="pill g">Кадр 1500 байт: доля overhead ≈ 2 %</span>
</div></div>'''


def _ipg():
    return '''<div class="c l" style="padding:12px 14px 8px">
<svg class="wide" viewBox="0 0 620 180" style="width:100%" aria-hidden="true">
<rect x="20" y="58" width="130" height="62" rx="9" fill="#12423c"/>
<text x="85" y="84" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="12.5" font-weight="700" fill="#eafaf6">Кадр 1</text>
<text x="85" y="102" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" fill="#9dc4bc">(данные)</text>
<rect x="470" y="58" width="130" height="62" rx="9" fill="#12423c"/>
<text x="535" y="84" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="12.5" font-weight="700" fill="#eafaf6">Кадр 2</text>
<text x="535" y="102" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" fill="#9dc4bc">(данные)</text>
<line x1="150" y1="89" x2="470" y2="89" stroke="#b7d8cf" stroke-width="2" stroke-dasharray="7 7"/>
<path d="M160 89h300" stroke="#19b89f" stroke-width="1.6" marker-start="url(#ar)" marker-end="url(#ar)" opacity="0"/>
<defs><marker id="ar" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto">
<path d="M0 4h8M4 0l4 4-4 4" stroke="#0a2c28" stroke-width="1.4" fill="none"/></marker></defs>
<path d="M165 46h290" stroke="#0a2c28" stroke-width="1.4" marker-start="url(#ar)" marker-end="url(#ar)"/>
<text x="310" y="26" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="13" font-weight="750" fill="#0a2c28">Межпакетный разрыв</text>
<text x="310" y="40" text-anchor="middle" font-family="Consolas,monospace" font-size="14" font-weight="800" fill="#0e8d78">96 бит</text>
<text x="310" y="137" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="12" fill="#3f6660">Канал в простое</text>
<text x="310" y="153" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11" fill="#5c7d77">(нет передачи данных)</text>
<text x="85" y="140" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10.5" fill="#5c7d77">время →</text>
</svg></div>'''


def _tcp():
    return '''<div class="c l" style="padding:12px 14px 8px">
<svg class="wide" viewBox="0 0 620 230" style="width:100%" aria-hidden="true">
<rect x="14" y="78" width="118" height="72" rx="10" fill="#12423c"/>
<text x="73" y="112" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="12" font-weight="700" fill="#eafaf6">Отправитель</text>
<text x="73" y="128" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10.5" fill="#9dc4bc">(клиент)</text>
<rect x="488" y="78" width="118" height="72" rx="10" fill="#12423c"/>
<text x="547" y="112" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="12" font-weight="700" fill="#eafaf6">Получатель</text>
<text x="547" y="128" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="10.5" fill="#9dc4bc">(сервер)</text>
<defs>
<marker id="agr" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
<path d="M0 0l9 4.5L0 9z" fill="#2aa85d"/></marker>
<marker id="abl" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto">
<path d="M0 0l9 4.5L0 9z" fill="#2a7cc4"/></marker></defs>
<g id="tSeg"><path d="M140 52h336" stroke="#2aa85d" stroke-width="2.4" marker-end="url(#agr)"/>
<text x="308" y="40" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="12" font-weight="700" fill="#1f9b4f">Сегмент данных</text></g>
<g id="tAck"><path d="M476 104H146" stroke="#ef5a5a" stroke-width="2.4" stroke-dasharray="8 6"/>
<path d="M300 94l16 16M316 94l-16 16" stroke="#ef5a5a" stroke-width="3" stroke-linecap="round"/>
<text x="308" y="88" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="12" font-weight="700" fill="#d13c3c">ACK не получен</text></g>
<g id="tTo"><rect x="206" y="132" width="204" height="26" rx="8" fill="#fde8e8" stroke="#ef5a5a"/>
<text x="308" y="149" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11.5" fill="#c23434">Истёк таймаут ожидания</text></g>
<g id="tRe"><path d="M140 186h336" stroke="#2a7cc4" stroke-width="2.4" stroke-dasharray="9 6" marker-end="url(#abl)"/>
<text x="308" y="208" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="12" font-weight="700" fill="#2a7cc4">Повторная отправка того же сегмента</text></g>
</svg></div>'''


def _speedtest():
    return '''<div class="c d" style="padding:20px 24px">
<div class="g g4" style="align-items:center">
<div style="text-align:center">
  <div style="width:56px;height:56px;margin:0 auto 9px;border-radius:50%;display:grid;
   place-items:center;background:rgba(94,224,200,.12);border:1px solid rgba(94,224,200,.45)">
  <svg viewBox="0 0 24 24" style="width:26px;height:26px;stroke:#5ee0c8;fill:none;stroke-width:1.5">
  <circle cx="12" cy="12" r="8.6"/><path d="M3.4 12h17.2M12 3.4a14 14 0 0 1 0 17.2 14 14 0 0 1 0-17.2"/></svg></div>
  <div style="font:700 13px Segoe UI,sans-serif;color:#eafaf6">Проверка завершена</div>
  <div style="font-size:11px;color:#9dc4bc;margin-top:3px">Соединение стабильное</div>
</div>
<div style="text-align:center;border-left:1px solid rgba(94,224,200,.18)">
  <div style="font:700 11.5px Segoe UI,sans-serif;color:#9dc4bc;letter-spacing:.08em">СКАЧИВАНИЕ</div>
  <div style="font:800 clamp(28px,4vw,52px)/1 Consolas,monospace;color:#fff;margin:6px 0">83.49</div>
  <div style="font-size:12px;color:#5ee0c8;font-weight:700">Мбит/с</div>
</div>
<div style="text-align:center;border-left:1px solid rgba(94,224,200,.18)">
  <div style="font:700 11.5px Segoe UI,sans-serif;color:#9dc4bc;letter-spacing:.08em">ОТПРАВКА</div>
  <div style="font:800 clamp(28px,4vw,52px)/1 Consolas,monospace;color:#fff;margin:6px 0">84.94</div>
  <div style="font-size:12px;color:#9b7fe0;font-weight:700">Мбит/с</div>
</div>
<div style="text-align:center;border-left:1px solid rgba(94,224,200,.18)">
  <div style="font:700 11.5px Segoe UI,sans-serif;color:#9dc4bc;letter-spacing:.08em">PING</div>
  <div style="font:800 clamp(28px,4vw,52px)/1 Consolas,monospace;color:#fff;margin:6px 0">3</div>
  <div style="font-size:12px;color:#e8a33d;font-weight:700">мс</div>
  <div style="font-size:10.5px;color:#9dc4bc;margin-top:7px">при скачивании 7 мс · при отправке 9 мс</div>
</div>
</div></div>'''


def _pipe_mini():
    return '''<svg class="wide" viewBox="0 0 600 110" style="width:100%" aria-hidden="true">
<defs>
<linearGradient id="pg2" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#7ae8a6"/><stop offset=".5" stop-color="#49d67f"/>
 <stop offset="1" stop-color="#2aa85d"/></linearGradient>
<linearGradient id="po2" x1="0" y1="0" x2="0" y2="1">
 <stop offset="0" stop-color="#86c6fa"/><stop offset=".5" stop-color="#4aa3f0"/>
 <stop offset="1" stop-color="#2a7cc4"/></linearGradient>
</defs>
<rect x="20" y="26" width="560" height="54" rx="6" fill="#dceee9" stroke="#b7d8cf"/>
<rect id="mpG" x="20" y="26" width="437" height="54" fill="url(#pg2)"/>
<rect id="mpO" x="457" y="26" width="123" height="54" fill="url(#po2)"/>
<rect x="20" y="26" width="560" height="54" rx="6" fill="none" stroke="#0d332f" stroke-width="1.8" opacity=".3"/>
<text id="mlG" x="238" y="100" text-anchor="middle" font-family="Segoe UI,sans-serif"
 font-size="13" font-weight="700" fill="#1f9b4f">G</text>
<text id="mlO" x="518" y="100" text-anchor="middle" font-family="Segoe UI,sans-serif"
 font-size="13" font-weight="700" fill="#2a7cc4">O</text>
<text x="300" y="18" text-anchor="middle" font-family="Segoe UI,sans-serif" font-size="11"
 fill="#5c7d77">T = 1000 Мбит/с</text>
</svg>'''
