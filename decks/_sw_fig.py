# -*- coding: utf-8 -*-
"""Картинки из pptx 2.2, которых не было в деке: вставляются слайдами сразу после своей темы (порядок pptx)."""
from _sw_lib import SL, sc, head, grow, b64, _esc

def _figs(names, cap):
    imgs = "".join('<div class="pfig"><img src="%s" alt=""></div>' % b64("fig_" + n) for n in names)
    return '<div class="pfigs n%d">%s</div><div class="piccap">%s</div>' % (len(names), imgs, cap)

def _slide(label, title, names, cap):
    return ('<section class="slide" data-label="%s">%s</section>'
            % (_esc(label), sc(head(title), grow("g", _figs(names, cap)))))

def _info(label, title, name):
    return ('<section class="slide" data-label="%s">%s</section>'
            % (_esc(label), sc(head(title), grow("g", '<div class="pic"><img src="%s" alt=""></div>' % b64(name)))))

# после какого слайда старой деки (номер 1..151) вставить; слайды pptx в скобках
INSERT = [
    (21, [_slide("MAC-адрес: пример", "MAC-адрес — <em>как паспорт</em> сетевой карты", ["s09_1"], "Каждая сетевая карта имеет глобально уникальный MAC-адрес")]),            # pptx 9
    (48, [_slide("show mac address-table", "Таблица коммутации: <em>вывод CLI</em>", ["s20_1"], "switch# show mac address-table")]),          # 20
    (52, [_slide("show mac address-table count", "Заполненность <em>таблицы</em>", ["s21_1"], "switch# show mac address-table count")]),     # 21
    (54, [_info("Способы обработки кадров", "Способы обработки кадров <em>коммутатором</em>", "frame_ways")]),                               # 23
    (72, [_slide("Шторм: схема", "Широковещательный <em>шторм</em>", ["s30_0"], "Кадр бесконечно размножается в петле коммутаторов")]),       # 30
    (74, [_slide("Домен рассылки: схема", "Граница домена — <em>маршрутизатор</em>", ["s32_0"], "Маршрутизатор не пропускает широковещательный ARP-запрос")]),  # 32
    (80, [_slide("show interfaces", "Просмотр <em>портов</em> в CLI", ["s35_1", "s35_0"], "switch# show interfaces status · show interfaces GigabitEthernet 1/0/1")]),  # 35
    (88, [_info("Loopback", "Интерфейсы обратной петли <em>loopback</em>", "loopback"),
          _slide("show ip interfaces", "Интерфейсы L3 в <em>CLI</em>", ["s39_1"], "switch# show ip interfaces — loopback 1, SVI (vlan 1) и физический с IP")]),  # 39
    (92, [_slide("ARP без VLAN", "Без VLAN: <em>ARP-запрос</em> всем", ["s40_0", "s41_0"], "Рис. 2.4.1.1–2.4.1.2 — запрос PC и рассылка на все порты коммутаторов"),
          _slide("ARP с VLAN", "С VLAN: домены <em>разделены</em>", ["s42_0", "s43_0"], "Рис. 2.4.1.3–2.4.1.4 — разделение на домены, рассылка только в своём сегменте")]),  # 40-43
    (96, [_slide("Таблица с VLAN", "Таблица коммутации <em>с VLAN</em>", ["s51_1"], "Рис. 2.4.3.1 — пример таблицы коммутации")]),          # 51
    (99, [_slide("Тегирование: кадр", "Тегирование кадра <em>на порту</em>", ["s47_0", "s48_0"], "Рис. 2.4.2.2 — к кадру добавляется тег 802.1Q"),
          _slide("Растегирование", "Копирование и <em>растегирование</em>", ["s49_0", "s50_0"], "Рис. 2.4.2.3–2.4.2.4 — копии кадра и снятие тега на выходе")]),  # 47-50
    (102, [_slide("show vlan", "Создание и удаление VLAN: <em>show vlan</em>", ["s52_0", "s52_1"], "Результат создания и удаления VLAN на коммутаторе")]),  # 52
    (106, [_slide("Классификация VLAN", "Классификация <em>VLAN</em>", ["s54_1"], "Рис. 2.4.6.1 — по методу создания, тегирования и виду трафика")]),  # 54
    (111, [_slide("Порт доступа в CLI", "Порт доступа: <em>проверка</em>", ["s58_0", "s58_1"], "switch# show interfaces switchport · show vlan"),
           _slide("access vlan 10", "Назначение портов <em>в VLAN 10</em>", ["s59_0", "s59_1", "s59_2", "s60_0"], "interface range · switchport access vlan 10 · show vlan")]),  # 58-60
    (115, [_slide("Native VLAN 20", "Транк с <em>native VLAN 20</em>", ["s65_0"], "Рис. 2.5.4.2.3 — применение транкового порта с нативной VLAN 20")]),  # 65
    (121, [_slide("Q-in-Q: схема", "Q-in-Q: <em>CVLAN и SVLAN</em>", ["s72_0"], "X — любой VLAN, кроме 31; на выходе добавляется внешняя метка SVLAN")]),  # 72
    (122, [_slide("MAC-VLAN: схема", "VLAN на основе <em>MAC-адресов</em>", ["s74_0"], "ПК1 и ПК2 попадают в VLAN 10 по своим MAC-адресам")]),  # 74
    (129, [_slide("Консольный порт", "Консольный <em>порт и кабель</em>", ["s77_1", "s77_0"], "Рис. 2.6.1.1.1 — консольный порт коммутатора и настройки терминала")]),  # 77
    (130, [_slide("SSH: схема", "Подключение <em>по SSH</em>", ["s79_0"], "Рис. 2.6.1.2.1 — подключение к коммутатору по протоколу SSH")]),  # 79
    (132, [_slide("Web: первое подключение", "Начальное подключение <em>по Web</em>", ["s80_1", "s80_0"], "Рис. 2.6.1.3.1–2.6.1.3.2 — схема и окно входа Web-интерфейса"),
           _slide("Web-интерфейс Eltex", "Web-интерфейс <em>MES2324</em>", ["s81_0", "s82_0"], "Рис. 2.6.1.3.3–2.6.1.3.4 — окно конфигурации и подключение в функционирующей сети")]),  # 80-82
    (134, [_slide("Баннеры в CLI", "Баннерные сообщения <em>в CLI</em>", ["s84_0", "s84_1", "s84_2"], "banner login · banner exec — вид при входе и в конфигурации")]),  # 84
    (138, [_slide("Удаление учётной записи", "Учётные записи <em>в CLI</em>", ["s87_0", "s87_1"], "Рис. 2.6.4.2.2 — результат удаления учётной записи")]),  # 87
    (139, [_slide("Повышение привилегий в CLI", "Повышение <em>уровня привилегий</em>", ["s88_0", "s89_0", "s89_1"], "Пользовательский режим · enable · временное повышение с 1 до 15")]),  # 88-89
]

CSS = """
.pfigs{flex:1 1 auto;min-height:0;display:grid;gap:22px;align-items:center;justify-items:center}
.pfigs.n2{grid-template-columns:1fr 1fr}.pfigs.n3,.pfigs.n4{grid-template-columns:1fr 1fr}
.pfig{background:#fff;border-radius:14px;padding:14px;box-shadow:0 0 0 1px rgba(0,229,255,.55),0 0 26px rgba(0,229,255,.28);
  max-width:100%;max-height:100%;display:flex;opacity:0;transform:translateY(14px) scale(.98);animation:pfin .7s ease forwards}
.pfig:nth-child(2){animation-delay:.35s}.pfig:nth-child(3){animation-delay:.7s}.pfig:nth-child(4){animation-delay:1.05s}
.pfig img{max-width:100%;max-height:62vh;object-fit:contain;display:block}
.pfigs.n3 .pfig img,.pfigs.n4 .pfig img{max-height:29vh}
@keyframes pfin{to{opacity:1;transform:none}}
"""

def apply():
    for after, items in sorted(INSERT, key=lambda x: -x[0]):
        SL[after:after] = items
