# -*- coding: utf-8 -*-
"""Слайды по референсам p004, p005, p007, p008."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, icon, arrow_svg

SLIDES = []


def ab(l, t, w=None, extra=""):
    s = f"position:absolute;left:{l}px;top:{t}px;"
    if w: s += f"width:{w}px;"
    return s + extra


def layer(*parts):
    return ('<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" '
            'viewBox="0 0 1920 1080">' + "".join(parts) + '</svg>')


# ======================================================= стекирование (p004)
def li(name, txt, l, t, w, fs=21):
    s = icon(name).replace("<svg ", '<svg style="width:30px;height:30px;fill:none;stroke:var(--blue);stroke-width:1.8;flex:none" ')
    return (f'<div class="ab" style="left:{l}px;top:{t}px;width:{w}px;display:flex;gap:16px;align-items:center">'
            f'{s}<span style="font-size:{fs}px;color:var(--navy);white-space:nowrap">{txt}</span></div>')


def stacking():
    o = ['<h1 class="t ab ctr-x" style="top:18px;width:1700px;font-size:52px">Стекирование и производительность коммутаторов</h1>']
    H = 'font-size:34px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.1'
    # --- как работает стек
    o.append(f'<div class="card" data-s="1" style="{ab(38, 92, 1040)}height:325px"></div>')
    o.append(f'<div class="ab" data-s="1" style="left:82px;top:106px;{H}">Как работает стек</div>')
    o.append('<img class="ab" data-s="1" src="assets/p004_stackfull.jpg" '
             'style="left:200px;top:150px;width:440px;mix-blend-mode:multiply">')
    for i in range(4):
        o.append(f'<div class="ab" data-s="1" style="left:56px;top:{186 + i * 50}px;font-size:16px;color:var(--navy)">'
                 f'Коммутатор {i + 1}</div>')
    o.append('<div class="ab" data-s="1" style="left:650px;top:244px;font-size:16px;color:var(--navy);line-height:1.2">'
             'Стековое<br>соединение<br>(SFP)</div>')
    feats = ["До 8 физических<br>устройств", "1 логический<br>коммутатор", "Общее управление<br>и больше портов"]
    for i, t in enumerate(feats):
        o.append(f'<img class="ab" data-s="2" src="assets/p004_f{i + 1}.png" style="left:782px;top:{128 + i * 92}px;width:80px;'
                 f'--dl:{i * 90}ms">'
                 f'<div class="ab" data-s="2" style="left:876px;top:{136 + i * 92}px;width:200px;font-size:21px;font-weight:700;'
                 f'color:var(--navy);line-height:1.2;--dl:{i * 90}ms">{t}</div>')
    # --- uplink
    o.append(f'<div class="card" data-s="3" style="{ab(1092, 102, 790)}height:325px;padding:16px 26px">'
             f'<div style="{H}">Uplink-интерфейс</div>'
             '<p class="b" style="font-size:21px;line-height:1.3;margin-top:6px">Высокоскоростной интерфейс для подключения '
             'к вышестоящему коммутатору или маршрутизатору.</p>'
             '<p class="b" style="font-size:21px;line-height:1.3;margin-top:4px">Благодаря SFP-модулям может использовать '
             'разные типы соединений.</p>'
             '<div style="margin-top:6px;padding:4px 0;border-radius:8px;background:rgba(200,215,245,.55);text-align:center;'
             'font-size:21px;color:var(--navy)">E1 <span style="color:var(--blue)">&#9679;</span> 10 Gigabit Ethernet '
             '<span style="color:var(--blue)">&#9679;</span> оптоволокно</div></div>')
    for i, (img, lab, val) in enumerate([("p004_eth.png", "Ethernet-порт:", "100 Мбит/с"), ("p004_upl.png", "Uplink:", "1 Гбит/с")]):
        x = 1135 + i * 410
        o.append(f'<div class="ab" data-s="3" style="left:{x}px;top:340px;display:flex;gap:18px;align-items:center">'
                 f'<img src="assets/{img}" style="width:100px">'
                 f'<div><div style="font-size:21px;color:var(--navy)">{lab}</div>'
                 f'<div style="font-size:34px;font-weight:800;color:var(--blue);white-space:nowrap">{val}</div></div></div>')
    o.append('<div class="ab" data-s="3" style="left:1488px;top:345px;width:2px;height:80px;background:var(--line)"></div>')
    # --- два варианта
    o.append(f'<div class="card" data-s="4" style="{ab(38, 430, 1844)}height:485px"></div>')
    o.append(f'<div class="ab" data-s="4" style="left:82px;top:440px;{H}">Два варианта на 48 абонентов</div>')
    o.append(f'<div class="card solid" data-s="4" style="{ab(56, 482, 588)}height:420px"></div>')
    o.append(f'<div class="ab" data-s="4" style="left:104px;top:492px;{H};font-size:30px">Стек: 2 × 24 порта</div>')
    o.append('<img class="ab" data-s="4" src="assets/p004_two2.jpg" style="left:100px;top:532px;width:520px;mix-blend-mode:multiply">')
    L = [("server", "2 × 1 RU = 2 RU"), ("power", "2 розетки 220 В"), ("switch", "48 абонентских портов"),
         ("speed", "48 × 100 Мбит/с = 4,8 Гбит/с"), ("db", "Стоимость: 2 × 150 = 300 единиц"),
         ("chart", "Стоимость порта: 300 ÷ 48 = 6,25 единицы")]
    for i, (n, t) in enumerate(L):
        o.append(f'<div data-s="4" class="ab" style="left:0;top:0">{li(n, t, 96, 668 + i * 37, 540)}</div>')

    rows = [("Место в стойке", "2 RU", "1 RU", True), ("Питание", "2 розетки", "1 розетка", True),
            ("Порты", "48", "48", False), ("Пропускная<br>способность портов", "4,8 Гбит/с", "4,8 Гбит/с", False),
            ("Стоимость", "300", "250", False), ("Цена порта", "6,25", "5,21", True)]
    td = "padding:7px 10px;font-size:19px;border-bottom:1px solid rgba(150,175,225,.35);color:var(--navy)"
    tr = "".join(f'<tr><td style="{td};line-height:1.15">{a}</td><td style="{td};text-align:center;white-space:nowrap">{b}</td>'
                 f'<td style="{td};text-align:center;white-space:nowrap;{"background:#bdf0ea;font-weight:700" if hl else ""}">{c}</td></tr>'
                 for a, b, c, hl in rows)
    th = "padding:9px 10px;font-size:19px;font-weight:600;color:#fff;text-align:center"
    o.append(f'<div class="ab" data-s="5" style="left:668px;top:446px;width:580px;text-align:center;font-size:27px;font-weight:800;'
             f'color:var(--navy);text-transform:uppercase">Сравнение параметров</div>')
    o.append(f'<table class="ab" data-s="5" style="left:676px;top:492px;width:568px;border-collapse:collapse;background:rgba(255,255,255,.85);'
             f'border-radius:10px;overflow:hidden"><tr style="background:linear-gradient(90deg,#8fa6dc,#6f8bd0)">'
             f'<th style="{th}">Показатель</th><th style="{th}">Стек 2 × 24</th><th style="{th};background:#5d7bc9">Один × 48</th></tr>'
             f'{tr}</table>')
    o.append('<div class="ab" data-s="5" style="left:690px;top:858px;display:flex;gap:16px;align-items:center">'
             '<span style="width:56px;height:28px;border-radius:6px;background:#bdf0ea;display:block"></span>'
             '<span style="font-size:19px;color:var(--navy)">Лучший результат по данному показателю</span></div>')

    o.append(f'<div class="card solid" data-s="6" style="{ab(1282, 482, 584)}height:420px"></div>')
    o.append(f'<div class="ab" data-s="6" style="left:1320px;top:492px;{H};font-size:30px">Один коммутатор: 48 портов</div>')
    o.append('<img class="ab" data-s="6" src="assets/p004_one2.jpg" style="left:1312px;top:548px;width:540px;mix-blend-mode:multiply">')
    R = [("server", "1 RU"), ("power", "1 розетка 220 В"), ("switch", "48 абонентских портов"),
         ("speed", "48 × 100 Мбит/с = 4,8 Гбит/с"), ("db", "Стоимость: 250 единиц"),
         ("chart", "Стоимость порта: 250 ÷ 48 = 5,21 единицы")]
    for i, (n, t) in enumerate(R):
        o.append(f'<div data-s="6" class="ab" style="left:0;top:0">{li(n, t, 1320, 668 + i * 37, 540)}</div>')

    # --- две скорости
    o.append(f'<div class="card" data-s="7" style="{ab(38, 928, 1844)}height:138px"></div>')
    o.append(f'<div class="ab" data-s="7" style="left:82px;top:938px;{H}">Две разные скорости</div>')
    for i, (img, t, d) in enumerate([("p004_sp1.png", "Скорость пересылки",
                                      "Производительность всего коммутатора: объём данных, обрабатываемых за секунду."),
                                     ("p004_sp2.png", "Скорость порта",
                                      "Скорость передачи данных каждого Ethernet-порта: 100 Мбит/с, 1, 10 или 100 Гбит/с.")]):
        x, cw = [(470, 650), (1150, 715)][i]
        o.append(f'<div class="card solid" data-s="7" style="{ab(x, 942, cw)}height:112px;padding:8px 16px;display:flex;gap:16px;'
                 f'align-items:center;--dl:{i * 120}ms"><img src="assets/{img}" style="width:92px">'
                 f'<div><div style="font-size:22px;font-weight:800;color:var(--navy);text-transform:uppercase">{t}</div>'
                 f'<div style="font-size:18px;color:var(--navy);line-height:1.25;margin-top:2px">{d}</div></div></div>')
    o.append('<div class="ab" data-s="7" style="left:1136px;top:960px;width:2px;height:80px;background:var(--line)"></div>')
    return "".join(o)


SLIDES.append(("p004", "Стекирование и производительность коммутаторов", stacking()))


# ======================================================= ESR-200 задняя панель (p005)
def esr200_back():
    o = ['<div class="ab" style="left:96px;top:56px"><div class="big">ESR-200</div>'
         '<div class="kick" style="margin-top:6px">Задняя панель</div></div>',
         f'<img class="cut ab" src="assets/esr200_back.jpg" style="{ab(190, 330, 1540)}">']

    def call(l, n, title, txt, icn, s):
        return (f'<div class="card" data-s="{s}" style="{ab(l, 700, 520)}display:flex;gap:18px;align-items:flex-start">'
                f'<span class="badge">{n}</span><div style="flex:1">'
                f'<div style="font-size:25px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.2">{title}</div>'
                f'<div style="display:flex;gap:16px;align-items:center;margin-top:14px">{ico(icn, "sm")}'
                f'<p class="b sm dim">{txt}</p></div></div></div>')

    o += [call(170, 1, "Клемма для заземления устройства",
               "Используется для подключения маршрутизатора к контуру заземления.", "ground", 1),
          call(950, 2, "Вентиляционный модуль",
               "Обеспечивает эффективное охлаждение устройства и стабильную работу системы.", "fan", 2)]
    o.append(layer(
        '<path class="dr" data-s="1" pathLength="1" d="M250 560 L250 640 L430 640 L430 700" stroke="var(--blue)" stroke-width="4" fill="none"/>',
        '<path class="dr" data-s="2" pathLength="1" d="M1060 560 L1060 640 L1210 640 L1210 700" stroke="var(--blue)" stroke-width="4" fill="none"/>',
        '<path class="dr" data-s="2" pathLength="1" d="M1270 560 L1270 640 L1210 640" stroke="var(--blue)" stroke-width="4" fill="none"/>'))
    return "".join(o)


SLIDES.append(("p005", "ESR-200: задняя панель", esr200_back()))


# ======================================================= MES2424P задняя панель (p007)
MASK = ("-webkit-mask-image:radial-gradient(ellipse 62% 80% at 50% 50%,#000 86%,transparent 100%);"
        "mask-image:radial-gradient(ellipse 62% 80% at 50% 50%,#000 86%,transparent 100%)")


def mes2424p_back():
    o = ['<div class="ab" style="left:82px;top:58px;font-size:96px;font-weight:900;color:#132a8a;line-height:1;'
         'letter-spacing:-1px">MES2424P</div>',
         '<div class="ab" style="left:84px;top:162px;font-size:44px;font-weight:800;color:#6f86d6;text-transform:uppercase;'
         'line-height:1">Задняя панель</div>',
         f'<img class="ab" src="assets/dev/mes2424p-back.webp" style="{ab(210, 250, 1500)}filter:drop-shadow(0 14px 22px rgba(60,80,150,.25))">']

    def call(l, w, n, title, img, txt, s):
        return (f'<div class="card solid" data-s="{s}" style="{ab(l, 750, w)}height:172px;padding:0"></div>'
                f'<div class="ab" data-s="{s}" style="left:{l - 4}px;top:742px;width:84px;height:84px;background:#3f63d8;color:#fff;'
                f'font-size:46px;font-weight:800;display:grid;place-items:center;'
                f'clip-path:polygon(25% 0,75% 0,100% 50%,75% 100%,25% 100%,0 50%)">{n}</div>'
                f'<div class="ab" data-s="{s}" style="left:{l + 100}px;top:768px;font-size:27px;font-weight:800;color:#1c3db8;'
                f'text-transform:uppercase">{title}</div>'
                f'<img class="ab" data-s="{s}" src="assets/{img}" style="left:{l + 96}px;top:818px;width:88px">'
                f'<div class="ab" data-s="{s}" style="left:{l + 210}px;top:836px;width:{w - 230}px;font-size:21px;color:var(--navy);'
                f'line-height:1.25">{txt}</div>')

    o.append(call(800, 500, 1, "Вентиляторы", "p007_fan.png", "Охлаждение устройства", 1))
    o.append(call(1342, 500, 2, "Клемма заземления", "p007_gnd.png", "Клемма для заземления устройства", 2))
    st = 'stroke="#1f47c9" stroke-width="4" fill="none" stroke-linejoin="round"'
    o.append(layer(
        f'<path class="dr" data-s="1" pathLength="1" d="M824 573 L824 698 L1280 698 L1280 573" {st}/>',
        f'<path class="dr" data-s="1" pathLength="1" d="M1052 698 L1052 748" {st}/>',
        '<g data-s="1"><circle cx="824" cy="573" r="7" fill="#1f47c9"/><circle cx="1280" cy="573" r="7" fill="#1f47c9"/>'
        '<circle cx="1052" cy="746" r="7" fill="#1f47c9"/></g>',
        f'<path class="dr" data-s="2" pathLength="1" d="M1639 600 L1639 746" {st}/>',
        '<g data-s="2"><circle cx="1639" cy="600" r="7" fill="#1f47c9"/><circle cx="1639" cy="746" r="7" fill="#1f47c9"/></g>'))
    return "".join(o)


SLIDES.append(("p007", "MES2424P: задняя панель", mes2424p_back()))


# ======================================================= коммутаторы ЦОД (p008)
def dc_switches():
    o = ['<h1 class="t ab ctr-x" style="top:36px;width:1700px;font-size:58px">Коммутаторы центра обработки данных</h1>',
         '<div class="ab ctr-x" style="top:110px;font-size:46px;font-weight:800;color:#6f86d6;letter-spacing:2px">ЦОД</div>']

    tags = ["1G · 10G · 40G · 100G", "Top-of-rack", "End-of-row", "Неблокируемая<br>матрица", "EVPN / VXLAN",
            "Минимальная<br>задержка"]
    for i, t in enumerate(tags):
        cx = round([183, 407, 632, 858, 1083, 1312][i] * 1.2826)
        o.append(f'<img class="ab" data-s="1" src="assets/p008_i{i + 1}.png" style="left:{cx - 62}px;top:178px;width:124px;'
                 f'--dl:{i * 70}ms">'
                 f'<div class="ab" data-s="1" style="left:{cx - 150}px;top:308px;width:300px;text-align:center;font-size:21px;'
                 f'font-weight:700;color:var(--navy);text-transform:uppercase;line-height:1.2;--dl:{i * 70}ms">{t}</div>')
        if i:
            o.append(f'<div class="ab" data-s="1" style="left:{cx - 144}px;top:200px;width:2px;height:150px;'
                     f'background:var(--line)"></div>')

    for i, (img, name) in enumerate([("dev/mes5600-24.webp", "MES5600-24"), ("dev/mes5400-24.webp", "MES5400-24"),
                                     ("dev/mes5410-48.webp", "MES5410-48")]):
        l = [18, 657, 1276][i]
        w = [624, 605, 625][i]
        o.append(f'<div class="card" data-s="{2 + i}" style="{ab(l, 380, w)}height:292px;padding:0"></div>'
                 f'<img class="ab" data-s="{2 + i}" src="assets/{img}" style="left:{l + w // 2 - 250}px;top:398px;width:500px;height:190px;'
                 f'object-fit:contain;filter:drop-shadow(0 10px 16px rgba(60,80,150,.25))">'
                 f'<div class="ab" data-s="{2 + i}" style="left:{l}px;top:600px;width:{w}px;text-align:center;font-size:34px;'
                 f'font-weight:800;color:#1c3a9c">{name}</div>'
                 f'<div class="ab" data-s="{2 + i}" style="left:{l + w // 2 - 40}px;top:650px;width:80px;height:3px;'
                 f'background:#6f8ee0"></div>')

    o.append(f'<img class="ab" data-s="5" src="assets/p008_scene.jpg" style="{ab(26, 680, 1282)}'
             f'-webkit-mask-image:linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent);'
             f'mask-image:linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent)">')
    for i, t in enumerate(["Front-to-back", "Резервирование<br>питания", "Горячая<br>замена", "Мониторинг<br>оборудования"]):
        l, t0 = 1332 + (i % 2) * 274, 720 + (i // 2) * 136
        o.append(f'<div class="card solid" data-s="6" style="{ab(l, t0, 258)}height:118px;padding:0 14px;display:flex;gap:14px;'
                 f'align-items:center;--dl:{i * 80}ms"><img src="assets/p008_f{i + 1}.png" style="width:66px;flex:none">'
                 f'<div style="font-size:19px;font-weight:700;color:var(--navy);text-transform:uppercase;line-height:1.2">{t}</div></div>')
    return "".join(o)


SLIDES.append(("p008", "Коммутаторы центра обработки данных", dc_switches()))
