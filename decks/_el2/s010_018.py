# -*- coding: utf-8 -*-
"""Слайды по референсам p010, p012, p013, p014, p015, p017, p018.
Координаты новых слайдов — в системе картинки-оригинала, приведённой к 1497x842 (как в _el2cmp), S = 1920/1497.
CROPS — список вырезок из оригинала pptx (генерируются отдельно в _el2assets)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, arrow_svg

SLIDES = []
CROPS = []
S = 1920 / 1497
NV = "#1b2a6b"          # тёмно-синий заголовков оригинала
LB = "#6c84d4"          # светло-синий второго слова заголовка
WIDE = "font-family:var(--f);font-weight:800;"


def q(v):
    return round(v * S)


def B(x0, y0, x1=None, y1=None, ex=""):
    s = f"position:absolute;left:{q(x0)}px;top:{q(y0)}px;"
    if x1 is not None: s += f"width:{q(x1) - q(x0)}px;"
    if y1 is not None: s += f"height:{q(y1) - q(y0)}px;"
    return s + ex


def cut(n, name, x0, y0, x1, y1, mode="f", ds=None, ex="", alt=""):
    """вырезка из слайда pptx n, ставится ровно на то же место"""
    CROPS.append((n, name, x0, y0, x1, y1, mode))
    st = f' data-s="{ds}"' if ds else ""
    return f'<img class="ab"{st} src="assets/{name}" alt="{alt}" style="{B(x0, y0, x1, y1)}{ex}">'


def G(ds, *parts, dl=0):
    return (f'<div data-s="{ds}" style="position:absolute;left:0;top:0;width:1920px;height:1080px;--dl:{dl}ms">'
            + "".join(parts) + '</div>')


def box(x0, y0, x1, y1, ex=""):
    return f'<div class="card" style="{B(x0, y0, x1, y1)}padding:0;border-radius:24px;{ex}"></div>'


def tx(x0, y0, html, fs, ex="", x1=None):
    return f'<div style="{B(x0, y0, x1)}font-size:{fs}px;line-height:1.2;color:{NV};{ex}">{html}</div>'


def hd(x0, y0, html, fs, ex="", x1=None):
    """заголовок блока широким жирным шрифтом, как в оригинале"""
    return tx(x0, y0, html, fs, f"{WIDE}text-transform:uppercase;line-height:1.12;{ex}", x1)


def ab(l, t, w=None, extra=""):
    s = f"position:absolute;left:{l}px;top:{t}px;"
    if w: s += f"width:{w}px;"
    return s + extra


def layer(*parts):
    return ('<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" '
            'viewBox="0 0 1920 1080">' + "".join(parts) + '</svg>')


def tile(l, t, w, icn, text, s, dl=0, h=150, fs=18):
    return (f'<div class="card" data-s="{s}" style="{ab(l, t, w)}height:{h}px;padding:16px;text-align:center;--dl:{dl}ms">'
            f'<div style="display:flex;justify-content:center">{ico(icn, "sm")}</div>'
            f'<div style="margin-top:10px;font-size:{fs}px;font-weight:700;color:var(--navy);'
            f'text-transform:uppercase;line-height:1.25">{text}</div></div>')


# ======================================================= модели MES (p010) — pptx 39
def pill(x0, y0, x1, y1, txt, fs=30):
    return (f'<div style="{B(x0, y0, x1, y1)}display:grid;place-items:center;border-radius:40px;'
            f'background:linear-gradient(180deg,#fff,#eef2fd);box-shadow:0 4px 12px rgba(90,110,190,.16),inset 0 1px 0 #fff;'
            f'{WIDE}font-size:{fs}px;color:{NV}">{txt}</div>')


def mes_models():
    o = [hd(0, 30, 'Модели MES и их характеристики', 64, "text-align:center;white-space:nowrap;letter-spacing:-.5px", 1497),
         hd(0, 92, 'Коммутаторы доступа', 38, f"text-align:center;color:#4a63c8;font-weight:700", 1497)]
    feats = [(123, 152, 194, 224, "p010_ic_compact.png", 223, "Компактные<br>размеры"),
             (434, 152, 503, 224, "p010_ic_temp.png", 533, "Расширенный<br>температурный<br>диапазон"),
             (757, 152, 827, 224, "p010_ic_shield.png", 852, "Надёжность и<br>отказоустойчивость"),
             (1113, 152, 1183, 224, "p010_ic_bolt.png", 1210, "Безопасность и<br>защита от скачков")]
    f = [box(100, 140, 1398, 236)]
    for i, (a, b, c, d, nm, tx0, t) in enumerate(feats):
        f.append(cut(39, nm, a - 3, b - 3, c + 3, d + 3, "w"))
        f.append(hd(tx0, (b + d) / 2 - (13 if "<br>" in t and t.count("<br>") == 1 else 21), t, 21, "font-weight:600;line-height:1.25"))
    f += [f'<div style="{B(x, 170, x + 1.5, 212)}background:rgba(140,160,215,.45)"></div>' for x in (403, 727, 1083)]
    o.append(G(1, *f))
    devs = [((28, 258, 505, 488), (42, 296, 490, 405), "mes1428", "MES1428", (167, 432, 373, 474)),
            ((520, 258, 977, 488), (543, 292, 950, 407), "mes2300-08", "MES2300-08", (634, 432, 862, 474)),
            ((992, 258, 1470, 488), (1010, 290, 1455, 405), "mes2420b-24d", "MES2420B-24D", (1093, 432, 1367, 474)),
            ((66, 505, 741, 772), (95, 530, 712, 692), "mes2408", "MES2408", (284, 720, 508, 762)),
            ((758, 505, 1435, 772), (785, 530, 1408, 694), "mes2408b", "MES2408B", (986, 720, 1210, 762))]
    for i, (c, im, f_, nm, p) in enumerate(devs):
        o.append(G(2 + i, box(*c),
                   f'<img class="ab" src="assets/dev/{f_}.webp" alt="{nm}" style="{B(*im)}'
                   f'filter:drop-shadow(0 10px 14px rgba(80,95,170,.22))">',
                   pill(*p, nm)))
    return "".join(o)


SLIDES.append(("p010", "Модели MES: коммутаторы доступа", mes_models()))


# ======================================================= функционал ESR (p012)
def esr_functions():
    o = ['<h1 class="t ab ctr-x" style="top:26px;width:1820px;font-size:56px">Основной функционал маршрутизаторов ESR</h1>',
         '<div class="sub n ab ctr-x" style="top:96px;font-size:21px">'
         'Возможности зависят от модели, версии ПО и установленных лицензий</div>']

    steps = [("globe", "eltex-co.ru"), ("doc", "Каталог, маршрутизаторы ESR"), ("router", "Выбрать нужную модель"),
             ("list", "Документы и файлы"), ("doc", "Руководство по эксплуатации или Справочник команд CLI")]
    o.append(f'<div class="card" data-s="1" style="{ab(70, 150, 380)}height:620px">'
             '<div class="ch sm">Где посмотреть функции модели</div>'
             + "".join(f'<div style="display:flex;gap:14px;align-items:center;margin-bottom:22px">'
                       f'<span class="badge o" style="width:38px;height:38px;font-size:20px">{i + 1}</span>'
                       f'{ico(icn, "sm")}<p class="b sm" style="flex:1">{t}</p></div>'
                       for i, (icn, t) in enumerate(steps)) + '</div>')

    groups = [("net", "Интерфейсы и VLAN", ["Сетевые интерфейсы", "VLAN"]),
              ("arrows", "Коммутация и маршрутизация", ["L2, LAG/LACP", "RIP, OSPF, IS-IS, BGP"]),
              ("lock", "Туннели и VPN", ["MPLS, GRE, DMVPN", "IPsec, OpenVPN", "WireGuard, PPTP, L2TP"]),
              ("gear", "Сетевые сервисы", ["NAT и DHCP", "QoS"]),
              ("shield", "Безопасность", ["ACL и Firewall", "IPS/IDS", "Защита от DoS/DDoS"]),
              ("chart", "Резервирование и мониторинг", ["VRRP, MultiWAN, кластер 1+1", "SNMP, Syslog, NetFlow", "Zabbix и SLA"])]
    o.append(f'<div class="ch sm ab" style="left:490px;top:150px">Основные группы функций</div>')
    for i, (icn, title, items) in enumerate(groups):
        l = 490 + (i % 3) * 300
        t = 200 + (i // 3) * 290
        o.append(f'<div class="card" data-s="{2 + i}" style="{ab(l, t, 280)}height:260px;padding:18px 20px;text-align:center">'
                 f'<div style="display:flex;justify-content:center">{ico(icn, "sm")}</div>'
                 f'<div style="margin-top:10px;font-size:18px;font-weight:800;color:var(--navy);text-transform:uppercase;'
                 f'line-height:1.2">{title}</div>'
                 + "".join(f'<p class="b sm dim" style="margin-top:10px;font-size:17px">{x}</p>' for x in items)
                 + '</div>')

    crit = [("speed", "Количество и скорость портов"), ("chart", "Производительность маршрутизации"),
            ("shield", "Производительность Firewall и VPN"), ("stack", "Поддерживаемые протоколы"),
            ("lock", "Безопасность"), ("reload", "Резервирование")]
    o.append('<div class="ch sm ab" style="left:1420px;top:150px">Ключевые критерии выбора</div>')
    for i, (icn, t) in enumerate(crit):
        o.append(tile(1420 + (i % 2) * 230, 200 + (i // 2) * 200, 210, icn, t, 8 + i // 2, dl=(i % 2) * 80, h=180, fs=16))

    o.append(f'<img class="ph ab" data-s="11" src="assets/p012_scene.jpg" style="{ab(70, 800, 1780)}">')
    return "".join(o)


SLIDES.append(("p012", "Основной функционал маршрутизаторов ESR", esr_functions()))


# ======================================================= внешние точки доступа (p013) — pptx 72
def outdoor_ap():
    o = [hd(0, 26, f'Внешние точки доступа <span style="color:{LB}">Eltex</span>', 62,
            "text-align:center;white-space:nowrap;letter-spacing:-.5px", 1497),
         tx(0, 87, 'Надёжные беспроводные сети в любых условиях', 21,
            f"text-align:center;letter-spacing:6.5px;text-transform:uppercase;font-family:var(--f);font-weight:600;color:#5d6aa0", 1497),
         f'<div style="{B(330, 96, 388, 97.2)}background:#8d9bc8"></div>',
         f'<div style="{B(1110, 96, 1167, 97.2)}background:#8d9bc8"></div>',
         tx(1350, 26, 'Связь<br>образование<br>развитие', 16,
            "text-transform:uppercase;letter-spacing:3px;line-height:1.55;font-family:var(--f);font-weight:600;color:#8a93b8")]
    devs = [((68, 130, 402, 498), '<img class="ab" src="assets/dev/wop-30li.webp" alt="WOP-30LI" style="' + B(114, 145, 342) + '">', "WOP-30LI", 235),
            ((417, 130, 755, 498), cut(72, "p013_wop12ac.png", 458, 138, 718, 462, "f", alt="WOP-12ac"), "WOP-12ac", 586),
            ((770, 130, 1078, 498), '<img class="ab" src="assets/dev/wop-50l.webp" alt="WOP-50L" style="' + B(838, 140, 1003) + '">', "WOP-50L", 921),
            ((1093, 130, 1426, 498), '<img class="ab" src="assets/dev/wop-3l-ex.webp" alt="WOP-3L-EX" style="' + B(1180, 140, 1331) + '">', "WOP-3L-EX", 1257)]
    for i, (c, img, nm, cx) in enumerate(devs):
        o.append(G(1 + i, box(*c), img, hd(cx - 150, 458, nm, 34, "text-align:center;text-transform:none", cx + 150)))
    caps = [(369, "p013_hx_wifi.png", "2,4 и 5 ГГц"), (552, "p013_hx_poe.png", "PoE"), (736, "p013_hx_wpa.png", "WPA2/WPA3"),
            (931, "p013_hx_vlan.png", "VLAN и<br>несколько SSID"), (1122, "p013_hx_roam.png", "Бесшовный<br>роуминг"),
            (1328, "p013_hx_mgmt.png", "Централизованное<br>управление")]
    c = [box(33, 513, 1463, 658), hd(63, 558, "Общие<br>возможности", 29)]
    c += [f'<div style="{B(x, 548, x + 1.5, 625)}background:rgba(140,160,215,.45)"></div>' for x in (275, 461, 643, 832, 1028, 1220)]
    for i, (cx, nm, t) in enumerate(caps):
        c.append(cut(72, nm, cx - 42, 520, cx + 42, 610, "w"))
        c.append(tx(cx - 110, 606 if "<br>" in t else 614, t, 22, "text-align:center;font-weight:600;line-height:1.05", cx + 110))
    o.append(G(5, *c))
    apps = [(232, 548, 246, 300, 318, "p013_sc_park", "Парки и стадионы"), (540, 848, 545, 600, 610, "p013_sc_dir", "Направленное покрытие"),
            (838, 1148, 840, 895, 905, "p013_sc_ind", "Промышленные объекты"), (1140, 1458, 1145, 1200, 1212, "p013_sc_ex", "Взрывоопасные зоны")]
    a = [box(33, 672, 1463, 812), hd(63, 715, "Сферы<br>применения", 29)]
    for x0, x1, i0, i1, t0, nm, t in apps:
        a.append(cut(72, nm + ".png", x0, 674, x1, 772, "f"))
        a.append(cut(72, nm + "_i.png", i0, 748, i1, 802, "w"))
        a.append(tx(t0, 777, t, 22, "font-weight:600;white-space:nowrap"))
    o.append(G(6, *a))
    return "".join(o)


SLIDES.append(("p013", "Внешние точки доступа Eltex", outdoor_ap()))


# ======================================================= индикаторы интерфейсов (p014) — pptx 16
def indicators():
    o = [tx(60, 14, 'Индикаторы<br><span style="color:#6f87d8">интерфейсов</span>', 86,
            f"{WIDE}text-transform:uppercase;line-height:1;letter-spacing:-1.5px;white-space:nowrap"),
         tx(63, 160, 'Маршрутизаторы имеют несколько интерфейсов, которые используются<br>для подключения к нескольким сетям. '
                     'Каждый интерфейс является участником<br>отдельной IP-сети. Для каждого интерфейса необходимо настроить IP-адрес<br>'
                     'и маску подсети соответствующей сети.', 21, "line-height:1.22;color:#2c3768;white-space:nowrap;letter-spacing:-.3px"),
         '<img class="ab" src="assets/dev/esr-3150.webp" alt="ESR-3150" style="' + B(705, 38, 1497) + 'filter:drop-shadow(0 14px 20px rgba(80,95,170,.25))">']
    c1 = [box(37, 258, 465, 648), hd(77, 276, "Разъем RJ-45", 33),
          hd(95, 318, "LINK/ACT", 25), hd(313, 318, "SPEED", 25),
          cut(16, "p014_rj45.png", 100, 345, 390, 568, "w", alt="Разъём RJ-45"),
          tx(37, 581, "Расположение индикаторов<br>разъема RJ-45", 25, "text-align:center;line-height:1.15;color:#2c3768", 465)]
    c2 = [box(478, 258, 845, 648), hd(506, 270, "Индикаторы<br>оптических интерфейсов", 28),
          cut(16, "p014_sfp.png", 560, 328, 748, 560, "w", alt="Оптический интерфейс"),
          hd(562, 563, "RX/ACT", 21), hd(683, 563, "TX/ACT", 21),
          tx(478, 592, "Расположение индикаторов<br>оптических интерфейсов", 25, "text-align:center;line-height:1.15;color:#2c3768", 845)]
    rows = [("Выключен", "Выключен", "Порт выключен или<br>соединение не установлено"),
            ("Выключен", "Горит постоянно", "Установлено соединение<br>на скорости 10/100 Мбит/с"),
            ("Горит постоянно", "Горит постоянно", "Установлено соединение<br>на скорости 1000 Мбит/с"),
            ("X", "Мигание", "Идёт передача данных")]
    hs = [61, 61, 61, 55]
    tr = "".join(f'<tr style="height:{q(h)}px"><td style="text-align:center;font-weight:700">{a}</td>'
                 f'<td style="text-align:center;font-weight:700;border-left:1px solid rgba(160,170,210,.35)">{b}</td>'
                 f'<td style="border-left:1px solid rgba(160,170,210,.35)">{c}</td></tr>' for (a, b, c), h in zip(rows, hs))
    th = "color:#fff;text-align:center;font-weight:600;padding:6px 10px;line-height:1.1;font-size:21px"
    c3 = [box(858, 262, 1485, 648), hd(884, 284, "Состояние интерфейса", 33),
          f'<table class="tbl" style="{B(876, 327, 1467)}font-size:20px;border-radius:10px;table-layout:fixed">'
          f'<colgroup><col style="width:{q(147)}px"><col style="width:{q(160)}px"><col></colgroup>'
          f'<thead><tr style="height:{q(57)}px"><th style="{th};background:linear-gradient(180deg,#f2bd5c,#e19a3e)">Индикатор<br>SPEED</th>'
          f'<th style="{th};background:linear-gradient(180deg,#4fc0b8,#2f9fa8)">Индикатор<br>LINK/ACT</th>'
          f'<th style="{th};background:linear-gradient(90deg,#4f78d8,#3d60c8)">Состояние интерфейса</th></tr></thead>'
          f'<tbody style="color:{NV}">{tr}</tbody></table>']
    tri = lambda c1_, c2_: (f'<svg viewBox="0 0 44 40" style="width:{q(44)}px;height:{q(40)}px"><defs><linearGradient id="g{c1_[1:]}" x1="0" y1="0" x2="0" y2="1">'
                            f'<stop offset="0" stop-color="{c1_}"/><stop offset="1" stop-color="{c2_}"/></linearGradient></defs>'
                            f'<polygon points="22,37 3,4 41,4" fill="url(#g{c1_[1:]})" stroke="#24476b" stroke-width="2.4" stroke-linejoin="round"/></svg>')
    c4 = [box(45, 660, 965, 800), f'<div style="{B(500, 675, 501.3, 785)}background:rgba(140,160,215,.45)"></div>',
          f'<div style="{B(88, 684)}">{tri("#5fd36c", "#16843a")}</div>',
          tx(163, 676, '<b style="font-size:30px">RX/ACT</b> <b style="font-size:24px;font-weight:600">(приём)</b>', 30, WIDE),
          tx(163, 706, "Индикатор загорается или мигает<br>при наличии оптического сигнала<br>на приёмном интерфейсе (RX).<br>Мигание указывает на приём данных.", 21, "line-height:1.2;color:#2c3768"),
          f'<div style="{B(552, 684)}">{tri("#ffb24a", "#e0641c")}</div>',
          tx(631, 676, '<b style="font-size:30px">TX/ACT</b> <b style="font-size:24px;font-weight:600">(передача)</b>', 30, WIDE),
          tx(631, 706, "Индикатор загорается или мигает<br>при наличии оптического сигнала<br>на передающем интерфейсе (TX).<br>Мигание указывает на передачу данных.", 21, "line-height:1.2;color:#2c3768")]
    o += [G(1, *c1), G(2, *c2), G(3, *c3), G(4, *c4), cut(16, "p014_fiber.png", 1100, 638, 1497, 805, "f", ds=4, alt="Оптический коннектор")]
    return "".join(o)


SLIDES.append(("p014", "Индикаторы интерфейсов", indicators()))


# ======================================================= MES1428 задняя панель (p015)
def mes1428_back():
    o = ['<div class="ab" style="left:96px;top:56px"><div class="big">MES1428</div>'
         '<div class="kick" style="margin-top:6px">Задняя панель</div></div>',
         f'<img class="cut ab" src="assets/p015_mes1428_back.jpg" style="{ab(190, 320, 1540)}">']

    def call(l, n, title, txt, icn, s):
        return (f'<div class="card" data-s="{s}" style="{ab(l, 650, 520)}display:flex;gap:18px;align-items:flex-start">'
                f'<span class="badge">{n}</span><div style="flex:1">'
                f'<div style="font-size:24px;font-weight:800;color:var(--navy);text-transform:uppercase">{title}</div>'
                f'<div style="display:flex;gap:16px;align-items:center;margin-top:12px">{ico(icn, "sm")}'
                f'<p class="b sm dim">{txt}</p></div></div></div>')

    o += [call(330, 2, "Вентиляционные отверстия", "Обеспечивают теплообмен и охлаждение компонентов", "fan", 1),
          call(1070, 1, "Клемма заземления", "Подключение корпуса устройства к контуру защитного заземления", "ground", 2)]
    o.append(layer(
        '<path class="dr" data-s="1" pathLength="1" d="M420 520 L420 600 L590 600 L590 650" stroke="var(--blue)" stroke-width="4" fill="none"/>',
        '<path class="dr" data-s="1" pathLength="1" d="M1240 520 L1240 600 L590 600" stroke="var(--blue)" stroke-width="4" fill="none"/>',
        '<path class="dr" data-s="2" pathLength="1" d="M1650 520 L1650 600 L1330 600 L1330 650" stroke="var(--blue)" stroke-width="4" fill="none"/>'))

    others = [("power", "Разъём питания переменного тока"), ("bolt", "Разъём аккумуляторной батареи"),
              ("fan", "Вентиляторные модули")]
    o.append(f'<div class="card" data-s="3" style="{ab(620, 850, 900)}height:190px;padding:20px 30px">'
             '<div style="text-align:center;font-size:26px;font-weight:800;color:var(--navy);text-transform:uppercase;'
             'margin-bottom:16px">На других моделях</div>'
             + "".join(f'<div class="ab" style="left:{40 + i * 290}px;top:76px;width:260px;text-align:center">'
                       f'<div style="display:flex;justify-content:center">{ico(icn, "sm")}</div>'
                       f'<p class="b sm dim" style="margin-top:8px">{t}</p></div>'
                       for i, (icn, t) in enumerate(others)) + '</div>')
    return "".join(o)


SLIDES.append(("p015", "MES1428: задняя панель", mes1428_back()))


# ======================================================= WOP-12ac (p017) — pptx 73
def wop12ac():
    o = [tx(90, 52, 'WOP-12ac', 160, f"{WIDE}letter-spacing:-5px;line-height:1;white-space:nowrap"),
         hd(98, 180, 'Внешняя точка доступа', 54, "color:#5a6db0;font-weight:700;white-space:nowrap"),
         f'<div style="{B(78, 237, 700, 238.2)}background:linear-gradient(90deg,#7d8fc8,rgba(125,143,200,.15))"></div>',
         f'<div style="{B(75, 234, 81, 240)}border-radius:50%;background:#4a5fb0"></div>',
         cut(73, "p017_wop12ac.png", 875, 22, 1372, 660, "f", alt="WOP-12ac")]
    tiles = [((47, 268, 266, 433), (98, 288, 214, 374), "2,4 и 5 ГГц"),
             ((282, 268, 502, 433), (333, 284, 450, 364), "До 1300 + 450<br>Мбит/с"),
             ((517, 268, 742, 433), (580, 288, 680, 368), "PoE+ · IEEE 802.3at"),
             ((47, 450, 266, 615), (98, 468, 214, 542), "До 64 устройств<br>в кластере"),
             ((282, 450, 502, 615), (312, 474, 468, 540), "Бесшовный<br>роуминг"),
             ((517, 450, 742, 615), (558, 466, 702, 556), "От −40 до +65 °C")]
    for i, (c, ic, t) in enumerate(tiles):
        two = "<br>" in t
        ty = (c[1] + 108) if two else (c[1] + 117)
        o.append(G(1 + i // 3, box(*c, "border-radius:20px"), cut(73, f"p017_ic{i + 1}.png", *ic, "wf"),
                   hd(c[0], ty, t, 25, "text-align:center;font-weight:600;line-height:1.2", c[2]), dl=(i % 3) * 110))
    apps = [((72, 640, 445, 772), (106, 752, 170, 818), 190, "Парки"),
            ((462, 648, 855, 772), (516, 754, 582, 818), 598, "Стадионы"),
            ((882, 652, 1290, 786), (896, 754, 960, 818), 975, "Промышленные объекты")]
    a = [f'<div style="{B(50, 636, 870, 637.2)}background:linear-gradient(90deg,#7d8fc8,rgba(125,143,200,.1))"></div>',
         f'<div style="{B(48, 633, 54, 639)}border-radius:50%;background:#4a5fb0"></div>']
    a += [f'<div style="{B(x, 668, x + 1.3, 806)}background:rgba(140,160,215,.5)"></div>' for x in (455, 868)]
    for i, (sc, ic, t0, t) in enumerate(apps):
        a.append(G(3, cut(73, f"p017_sc{i + 1}.png", *sc, "f"), cut(73, f"p017_sci{i + 1}.png", *ic, "w"),
                   hd(t0, 774, t, 25, "font-weight:600;white-space:nowrap"), dl=i * 130))
    o += a
    return "".join(o)


SLIDES.append(("p017", "WOP-12ac: внешняя точка доступа", wop12ac()))


# ======================================================= справка в CLI MES (p018) — pptx 60
def help_mes():
    o = [hd(0, 82, 'Справка в командной строке MES', 72, "text-align:center;white-space:nowrap;letter-spacing:-1px", 1497)]
    cards = [((40, 180, 505, 676), "01", "Контекстная<br>подсказка", (186, 312, 372, 470), "p018_q.png",
              "Показывает доступные<br>команды и параметры<br>в текущем режиме.", 127),
             ((519, 180, 975, 676), "02", "Проверка<br>синтаксиса", (610, 312, 886, 474), "p018_term.png",
              "Помогает обнаружить<br>ошибку в введённой<br>команде.", 596),
             ((989, 180, 1457, 676), "03", "Горячие<br>клавиши", (1050, 330, 1398, 472), "p018_keys.png",
              "Ускоряют ввод,<br>редактирование и работу<br>с командами.", 1086)]
    for i, (c, n, t, ic, nm, d, dx) in enumerate(cards):
        bx = c[0] + 38 if i == 0 else c[0] + 31
        o.append(G(1 + i, box(*c, "border-radius:26px"),
                   f'<div style="{B(bx, 207, bx + 92, 296)}display:grid;place-items:center;border-radius:14px;'
                   f'background:linear-gradient(160deg,#5b8cf0,#2a55d0 70%,#2148b8);box-shadow:inset 0 2px 0 rgba(255,255,255,.4),0 8px 18px rgba(42,80,200,.35);'
                   f'{WIDE}font-size:54px;color:#fff">{n}</div>',
                   hd(bx + 117, 209, t, 41, "letter-spacing:-.5px;line-height:1.16"),
                   cut(60, nm, *ic, "f"),
                   tx(dx, 480, d, 34, "line-height:1.24;color:#1d2c6e")))
    return "".join(o)


SLIDES.append(("p018", "Справка в командной строке MES", help_mes()))
