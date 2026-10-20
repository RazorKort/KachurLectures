# -*- coding: utf-8 -*-
"""Слайды по референсам p075-p082."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, arrow_svg, icon

SLIDES = []


def px(v):
    return round(v * 1920 / 900)


def py(v):
    return round(v * 1080 / 506)


def pz(v):
    return round(v * 1080 / 600)


def R(x0, y0, x1, y1, fy=py):
    return (f"position:absolute;left:{px(x0)}px;top:{fy(y0)}px;"
            f"width:{px(x1) - px(x0)}px;height:{fy(y1) - fy(y0)}px;")


def layer(*parts):
    return ('<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" '
            'viewBox="0 0 1920 1080">' + "".join(parts) + '</svg>')


def led(color, size=44):
    g = {"g": ("#d4ffdc", "#31d05a", "#15993c", "60,200,100"),
         "r": ("#ffd6d6", "#f0494b", "#b92024", "240,70,75")}[color]
    return (f'<span style="display:block;flex:none;width:{size}px;height:{size}px;border-radius:50%;'
            f'background:radial-gradient(circle at 35% 30%,{g[0]},{g[1]} 55%,{g[2]});'
            f'box-shadow:0 0 0 {size // 4}px rgba({g[3]},.16),0 0 22px rgba({g[3]},.45)"></span>')


def dot(color):
    c = {"g": "#34c759", "o": "#ff9f1a", "gr": "#9aa6bd", "r": "#f0494b", "b": "#2a6bf2"}[color]
    return f'<i style="display:block;flex:none;width:10px;height:10px;border-radius:50%;background:{c};margin-top:7px"></i>'


def bl(color, text, fs=15):
    return (f'<div style="display:flex;gap:8px;align-items:flex-start;font-size:{fs}px;line-height:1.3;'
            f'color:var(--ink)">{dot(color)}<span>{text}</span></div>')


HEAD = 'font-weight:800;color:var(--navy);text-transform:uppercase;'


def IM(name, l, t, w, s=None, extra=""):
    ds = f' data-s="{s}"' if s else ""
    return f'<img class="ab"{ds} src="assets/{name}" alt="" style="left:{l}px;top:{t}px;width:{w}px;{extra}">'


def BX(l, t, w, h, inner, s=None, cls="card", extra=""):
    ds = f' data-s="{s}"' if s else ""
    return f'<div class="{cls} ab"{ds} style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;padding:0;{extra}">{inner}</div>'


def TX(l, t, w, html, fs=20, extra=""):
    return f'<div class="ab" style="left:{l}px;top:{t}px;width:{w}px;font-size:{fs}px;line-height:1.25;color:var(--ink);{extra}">{html}</div>'




# ======================================================= p075 справочник CLI MES
def p075():
    o = ['<h1 class="t ab ctr-x" style="top:34px;width:1700px">Справочник команд CLI</h1>',
         '<div class="ab ctr-x" style="top:128px;display:flex;gap:26px;align-items:center;font-size:25px;'
         'font-weight:700;color:var(--blue);letter-spacing:4px;text-transform:uppercase;white-space:nowrap">'
         '<span style="width:90px;height:2px;background:var(--blue)"></span>'
         'Руководство по эксплуатации MES<span style="width:90px;height:2px;background:var(--blue)"></span></div>']
    o.append(f'<div class="card" data-s="1" style="{R(55, 98, 347, 418)}padding:0;overflow:hidden">'
             '<img src="assets/p075_cover.jpg" style="display:block;width:100%;height:100%;object-fit:cover"></div>')
    pdf = '<img class="ab" src="assets/p075_i_pdf.png" alt="PDF" style="left:40px;top:40px;width:128px">'
    items = [("server", "Назначение оборудования"), ("doc", "Технические характеристики"),
             ("gear", "Начальная настройка"), ("chart", "Конфигурация и мониторинг"),
             ("reload", "Обновление программного обеспечения")]
    lst = "".join(f'<div class="ab" style="left:28px;top:{300 + i * 78}px;width:560px;display:flex;gap:26px;'
                  f'align-items:center"><img src="assets/p075_i{i + 1}.png" style="width:72px"><p class="b" style="font-size:24px">{t}</p></div>'
                  for i, (ic, t) in enumerate(items))
    o.append(f'<div class="card" style="{R(368, 98, 878, 418)}padding:0">'
             f'<div class="ab" data-s="2" style="left:0;top:0;width:100%;height:290px">{pdf}'
             f'<div class="ab" style="left:200px;top:40px;{HEAD}font-size:44px;white-space:nowrap">Руководство по эксплуатации</div>'
             '<div class="tag ab" style="left:190px;top:100px;font-size:21px;padding:6px 20px;font-weight:600">Версия ПО 10.4.5</div>'
             '<p class="b ab" style="left:190px;top:150px;width:800px;font-size:23px">Официальный документ Элтекс для настройки и '
             'эксплуатации коммутаторов серии MES.</p></div>'
             '<div class="ab" style="left:28px;top:272px;width:1030px;height:2px;background:var(--line)"></div>'
             f'<div class="ab" data-s="3" style="left:0;top:0;width:100%;height:100%">{lst}</div>'
             f'<div class="card solid ab" data-s="4" style="left:640px;top:296px;width:448px;height:322px;padding:24px 26px">'
             f'<div style="display:flex;gap:20px;align-items:center"><img src="assets/p075_i_term.png" style="width:84px">'
             f'<div style="{HEAD}font-size:29px;line-height:1.1">Синтаксис<br>команд CLI</div></div>'
             '<p class="b sm" style="margin-top:14px;font-size:20px">Команды, параметры, ключевые слова и примеры настройки.</p>'
             '<div style="display:flex;gap:18px;align-items:center;margin-top:16px">'
             '<span class="chip key" style="font-size:26px;padding:14px 22px;min-width:150px">CTRL</span>'
             '<span style="font-size:26px;color:var(--dim)">+</span>'
             '<span class="chip key" style="font-size:26px;padding:14px 26px;min-width:100px">F</span></div>'
             '<p class="b sm" style="margin-top:12px;font-size:20px">Поиск команды в документе</p></div></div>')
    o.append(f'<div class="card" data-s="5" style="{R(115, 437, 785, 485)}display:flex;align-items:center;gap:22px;'
             f'padding:0 0 0 54px"><img src="assets/p075_i_doc.png" style="width:52px"><span class="mono" style="font-size:26px;font-weight:800;color:var(--navy)">PDF</span>'
             '<span style="width:2px;height:60px;background:var(--line)"></span>'
             f'<img src="assets/p075_i_link.png" style="width:44px">'
             '<span style="font-size:26px;color:var(--navy)">eltex.ru/storage/upload_center/files/60/MES_Series_user_manual_10.4.5.pdf</span></div>')
    return "".join(o)


SLIDES.append(("p075", "Справочник команд CLI: руководство MES", p075()))


# ======================================================= p076 радиоинтерфейсы
def p076():
    o = ['<h1 class="t left ab" style="left:72px;top:26px;width:1700px;font-size:76px">Настройка радиоинтерфейсов</h1>',
         '<img class="ph ab" data-s="1" src="assets/p076_webui.jpg" alt="Web-интерфейс точки доступа" style="left:38px;top:132px;width:1056px;height:712px;object-fit:cover;object-position:top;border-radius:22px;box-shadow:0 14px 38px rgba(26,52,120,.16)">']

    def pill(x, y, txt, light=False):
        bg = "#5b86e6" if light else "#19c0e8"
        return (f'<span class="ab" style="left:{x}px;top:{y}px;width:118px;height:52px;display:grid;place-items:center;background:{bg};color:#fff;'
                f'border-radius:8px;font-size:24px;font-weight:600">{txt}</span>')

    def rowbox(x, y, w, h, inner):
        return BX(x, y, w, h, inner, None, "card solid", "border-radius:10px")

    def head(icon, title):
        return IM(icon, 14, 10, 84) + TX(112, 26, 500, f'<span style="{HEAD}font-size:36px">{title}</span>')
    o.append(BX(1122, 135, 748, 205, head("p076_i1.png", "Режим работы")
                + rowbox(110, 66, 618, 60, pill(6, 4, "2,4 ГГц") + TX(140, 16, 470, "802.11ax; 802.11b/g/n; 802.11b/g/n/ax", 23))
                + rowbox(110, 130, 618, 60, pill(6, 4, "5 ГГц", True) + TX(140, 16, 470, "802.11ax; 802.11a/n/ac; 802.11a/n/ac/ax", 23)), 2))
    o.append(BX(1122, 362, 748, 238, head("p076_i2.png", "Выбор канала")
                + rowbox(110, 72, 618, 76, IM("p076_ok.png", 14, 10, 54) + TX(84, 8, 520, "<b>Автоматический</b> — точка выбирает наименее загруженный канал", 21))
                + rowbox(110, 156, 618, 66, IM("p076_gear.png", 14, 6, 54) + TX(84, 18, 520, "<b>Статический</b> — канал задаётся вручную", 21)), 3))
    o.append(BX(1122, 622, 748, 225, head("p076_i3.png", "Доступные каналы")
                + rowbox(110, 76, 618, 62, pill(6, 5, "2,4 ГГц") + TX(140, 16, 470, "1 – 13 &nbsp;|&nbsp; Оптимальные: 1, 6 и 11", 23))
                + rowbox(110, 146, 618, 62, pill(6, 5, "5 ГГц", True) + TX(140, 16, 470, "36 – 64, 132 – 144, 149 – 165", 23)), 4))

    def small(l, w, icon, title, body, vis, vl, vt, vw, s, bl=130, bt=76, bw=None):
        return BX(l, 870, w, 185, IM(icon, 16, 14, 82) + TX(124, 26, w - 130, f'<span style="{HEAD}font-size:25px">{title}</span>')
                  + TX(bl, bt, bw or (w - 140), body, 21) + IM(vis, vl, vt, vw), s, "card", "border-radius:18px")
    o.append(small(49, 426, "p076_b1.png", "Ширина канала", "20 или 40 МГц", "p076_v1.png", 130, 112, 260, 5))
    o.append(small(488, 459, "p076_b2.png", "Основной канал", "<b>Upper</b> — верхний<br><b>Lower</b> — нижний", "p076_v2.png", 316, 70, 130, 6, bw=190))
    o.append(small(960, 396, "p076_b3.png", "Мощность сигнала", "от 6 до 16 дБм", "p076_v3.png", 248, 64, 128, 7, bw=120))
    o.append(small(1369, 502, "p076_b4.png", "Глобальная изоляция", "Изолирует трафик клиентов разных VAP и радиоинтерфейсов",
                   "p076_v4.png", 18, 90, 162, 8, bl=196, bt=74, bw=296))
    return "".join(o)


SLIDES.append(("p076", "Настройка радиоинтерфейсов", p076()))


# ======================================================= p077 системные индикаторы
def p077():
    o = ['<img class="ab" data-s="1" src="assets/p077_mes2424p.png" alt="Коммутатор MES2424P" style="left:-150px;top:800px;width:700px;filter:drop-shadow(0 14px 20px rgba(30,60,130,.25))">',
         '<div class="ab" style="left:56px;top:38px;font-size:96px;font-weight:900;line-height:1;text-transform:uppercase;color:#13256e">Системные</div>',
         '<div class="ab" style="left:56px;top:124px;font-size:96px;font-weight:900;line-height:1;text-transform:uppercase;'
         'background:linear-gradient(90deg,#3b6fe0,#7aa2f2);-webkit-background-clip:text;background-clip:text;color:transparent">Индикаторы</div>',
         '<div class="ab" style="left:62px;top:228px;width:72px;height:4px;border-radius:2px;background:#3d72e8"></div>',
         '<p class="ab" style="left:60px;top:258px;width:540px;font-size:29px;line-height:1.24;color:#2a3558">Системные индикаторы отражают текущее состояние устройства. '
         'Зелёный цвет означает штатную работу, красный — неисправность, требующую внимания администратора.</p>']
    o.append(BX(51, 504, 458, 166, IM("p077_i_warn.png", 18, 34, 98)
                + TX(130, 22, 315, 'Если индикаторы <b>Alarm</b> и <b>PoE</b> одновременно горят красным, это сигнализирует о критической ошибке PoE.', 21, "color:#5a1a24;line-height:1.2"),
                8, "card rose", "background:linear-gradient(158deg,rgba(255,240,242,.97),rgba(252,214,220,.92));border:2px solid rgba(240,120,130,.45);border-radius:18px"))
    LED = {"off": ("p077_led_off.png", 56), "g": ("p077_led_g.png", 60), "gb": ("p077_led_gb.png", 84), "r": ("p077_led_r.png", 64)}

    def row(l, t, w, h, led, title, desc, fs=20):
        img, iw = LED[led]
        return BX(l, t, w, h, IM(img, 52 - iw // 2, (h - iw) // 2, iw)
                  + TX(110, 0, w - 120, f'<div style="display:flex;flex-direction:column;justify-content:center;height:{h}px">'
                       f'<b style="font-size:24px;color:var(--navy)">{title}</b><span style="font-size:{fs}px;line-height:1.15">{desc}</span></div>'),
                  None, "card solid", "border-radius:12px")

    def card(l, t, w, h, icon, title, sub, rows, s, tf=42, sf=21):
        inner = (IM(icon, 18, 14, 108) + TX(150, 26, w - 160, f'<div style="font-size:{tf}px;font-weight:800;color:var(--navy);line-height:1">{title}</div>'
                 f'<div style="font-size:{sf}px;color:#3a5aa8;margin-top:6px;line-height:1.15">{sub}</div>'))
        inner += "".join(row(r[0] - l, r[1] - t, r[2], r[3], *r[4:]) for r in rows)
        return BX(l, t, w, h, inner, s, "card", "border-radius:22px")
    o.append(card(725, 62, 549, 451, "p077_i_power.png", "Power", "Электропитание",
                  [(747, 201, 506, 84, "off", "Выключен", "Питание выключено."),
                   (747, 291, 506, 103, "g", "Зелёный горит", "Питание включено,<br>нормальная работа."),
                   (747, 400, 506, 103, "gb", "Зелёный мерцает", "Самотестирование<br>при включении питания (POST).")], 1))
    o.append(card(1302, 62, 565, 451, "p077_i_alarm.png", "Alarm", "Наличие и уровень аварии устройства",
                  [(1321, 212, 526, 119, "off", "Не горит", "Нормальная работа устройства."),
                   (1321, 337, 526, 122, "r", "Красный", "Перегрев.")], 2))
    o.append(card(539, 541, 436, 447, "p077_i_poe.png", "PoE", "Состояние PoE-портов",
                  [(554, 690, 408, 82, "off", "Выключен", "Потребитель PoE не подключен."),
                   (554, 780, 408, 82, "g", "Зелёный", "Подключен потребитель PoE."),
                   (554, 870, 408, 95, "r", "Красный", "Ошибка PoE на порту.")], 3))
    o.append(card(998, 541, 426, 447, "p077_i_master.png", "Master", "Признак ведущего устройства при работе в стеке",
                  [(1012, 690, 398, 144, "off", "Выключен", "Устройство не является «мастером» в стеке или не задан режим стекирования."),
                   (1012, 840, 398, 125, "g", "Зелёный", "Устройство является «мастером» в стеке.")], 4))
    o.append(card(1443, 541, 428, 447, "p077_i_batt.png", "Battery", "Индикатор состояния аккумуляторной батареи.",
                  [(1460, 690, 397, 82, "off", "Выключен", "АКБ отключена."),
                   (1460, 780, 397, 82, "g", "Зелёный", "АКБ подключена."),
                   (1460, 870, 397, 95, "r", "Красный", "Низкий уровень заряда АКБ.")], 5))
    return "".join(o)


SLIDES.append(("p077", "Системные индикаторы", p077()))



# ======================================================= p078 установка в стойку
def p078():
    o = ['<h1 class="t ab ctr-x" style="top:26px;width:1700px;font-size:60px">Установка коммутаторов <span class="lt">MES</span> в стойку</h1>']
    steps = [(25, 318, "1.", "Установить кронштейны", "p078_step1.jpg",
              "Кронштейны и винты входят в комплект поставки. Закрепите кронштейны на корпусе устройства."),
             (330, 590, "2.", "Разместить в стойке", "p078_step2.jpg",
              "Совместите отверстия кронштейнов с направляющими стойки."),
             (598, 878, "3.", "Закрепить устройство", "p078_step3.jpg", "Надёжно закрепите устройство с обеих сторон.")]
    for i, (x0, x1, n, t, img, txt) in enumerate(steps):
        w = px(x1) - px(x0)
        o.append(f'<div class="card" data-s="{1 + i}" style="{R(x0, 80, x1, 265)}padding:0;overflow:hidden">'
                 f'<div style="height:78px;background:linear-gradient(90deg,#d9e6fb,#eef4ff);display:flex;align-items:center;gap:16px;padding:0 14px">'
                 f'<span style="display:grid;place-items:center;min-width:92px;height:62px;background:#1f55c8;color:#fff;'
                 f'font-size:44px;font-weight:800;border-radius:12px">{n}</span>'
                 f'<span style="{HEAD}font-size:30px;white-space:nowrap">{t}</span></div>'
                 f'<img class="ab" src="assets/{img}" style="left:10px;top:92px;width:{w - 20}px;height:206px;'
                 f'object-fit:contain"></div>'
                 + f'<p class="b ab" data-s="{1 + i}" style="left:{px(x0) + 28}px;top:{py(224)}px;width:{w - 56}px;font-size:21px">{txt}</p>')
    o.append(layer(*[f'<path data-s="{s}" d="M{x} 340 L{x + 34} 366 L{x} 392Z" fill="#2a6bf2"/>' for x, s in ((680, 2), (1252, 3))]))
    o.append('<div class="ab ctr-x" data-s="4" style="top:572px;display:flex;gap:24px;align-items:center;white-space:nowrap">'
             '<span style="width:460px;height:2px;background:var(--line)"></span>'
             f'<span style="{HEAD}font-size:34px">Требования безопасности</span>'
             '<span style="width:460px;height:2px;background:var(--line)"></span></div>')

    def bcard(x0, x1, s):
        return f'<div class="card" data-s="{s}" style="{R(x0, 305, x1, 492)}padding:0;overflow:hidden">'

    SOFT = "-webkit-mask-image:radial-gradient(ellipse closest-side,#000 78%,transparent);mask-image:radial-gradient(ellipse closest-side,#000 78%,transparent)"
    o.append(bcard(15, 315, 4) +
             '<img class="ab" src="assets/p078_i_warn.png" style="left:18px;top:8px;width:92px">'
             f'<span class="ab" style="left:120px;top:24px;{HEAD}font-size:28px;white-space:nowrap">Не перекрывать вентиляцию</span>'
             f'<img class="ab" src="assets/p078_vent.jpg" style="left:44px;top:70px;width:540px;{SOFT}">'
             '<p class="b ab" style="left:36px;top:236px;width:580px;font-size:19px;line-height:1.3">Не закрывайте вентиляционные отверстия<br>и вентиляторы посторонними предметами.</p>'
             '<div class="ab" style="left:24px;top:300px;width:586px;background:#fde4e6;border-radius:12px;padding:8px 14px;'
             'display:flex;gap:14px;align-items:center;font-size:18px;line-height:1.25;color:#c5313a">'
             '<img src="assets/p078_i_temp.png" style="width:30px">'
             'Перекрытие потока воздуха вызывает перегрев<br>и нарушение работы.</div></div>')
    o.append(bcard(320, 590, 5) +
             '<img class="ab" src="assets/p078_i_gear.png" style="left:16px;top:8px;width:88px">'
             f'<span class="ab" style="left:128px;top:24px;{HEAD}font-size:28px;white-space:nowrap">Вертикальная установка</span>'
             f'<img class="ab" src="assets/p078_vert.jpg" style="left:30px;top:60px;width:272px;{SOFT}">'
             '<p class="b ab" style="left:350px;top:92px;width:230px;font-size:19px;line-height:1.3">Модели <b>MES3710P</b> и <b>MES3708P</b> '
             'устанавливаются вертикально.<br><br>Боковые панели обеспечивают теплоотвод.</p></div>')
    o.append(bcard(598, 878, 6) +
             '<img class="ab" src="assets/p078_i_power.png" style="left:12px;top:8px;width:88px">'
             f'<span class="ab" style="left:120px;top:24px;{HEAD}font-size:28px;white-space:nowrap">Подключение питания</span>'
             f'<img class="ab" src="assets/p078_tools.jpg" style="left:0;top:80px;width:597px;{SOFT}">'
             '<p class="b ab" style="left:28px;top:292px;width:560px;font-size:19px;line-height:1.3">Электропитание должен подключать<br>квалифицированный специалист.</p></div>')
    return "".join(o)


SLIDES.append(("p078", "Установка коммутаторов MES в стойку", p078()))


# ======================================================= p079 MES1428 передняя панель
def p079():
    o = ['<div class="ab" style="left:75px;top:20px"><div style="font-size:70px;font-weight:800;color:var(--navy);'
         'text-transform:uppercase;line-height:1">Конструктивное исполнение</div>'
         '<div style="font-size:26px;font-weight:700;color:var(--blue);text-transform:uppercase;margin-top:10px">Передняя панель MES1428</div></div>',
         '<img class="ab" src="assets/p079_front.jpg" style="left:58px;top:497px;width:1786px;filter:drop-shadow(0 16px 26px rgba(30,60,130,.18))">']

    def box(x0, y0, x1, y1, n, title, body, s):
        return (f'<div class="card" data-s="{s}" style="{R(x0, y0, x1, y1)}padding:0">'
                f'<span class="badge ab" style="left:14px;top:12px;width:62px;height:62px;font-size:40px;border-radius:14px;font-family:var(--f)">{n}</span>'
                f'<div class="ab" style="left:98px;top:20px;{HEAD}font-size:{26 if len(title) < 20 else 22}px;white-space:nowrap">{title}</div>{body}</div>')

    def img(name, left, top, w):
        return f'<img class="ab" src="assets/{name}" style="left:{left}px;top:{top}px;width:{w}px">'

    def txt(left, top, w, t):
        return f'<p class="b ab" style="left:{left}px;top:{top}px;width:{w}px;font-size:21px;line-height:1.35">{t}</p>'

    o.append(box(42, 108, 285, 188, 1, "Разъём питания",
                 img("p079_ic_plug.jpg", 24, 102, 62) + txt(120, 98, 380, "Подключение к источнику переменного тока"), 1))
    o.append(box(315, 108, 565, 188, 3, "Консольный интерфейс",
                 img("p079_ic_con.jpg", 24, 100, 76) + txt(124, 104, 340, "Локальное управление устройством"), 3))
    o.append(box(598, 108, 855, 188, 5, "Ethernet-интерфейсы",
                 img("p079_ic_eth.jpg", 24, 100, 76) + txt(124, 104, 420, "Порты 10/100BASE-TX (RJ-45)"), 5))
    o.append(box(35, 372, 290, 472, 2, "Индикаторы",
                 '<div class="ab" style="left:36px;top:96px;width:480px;font-size:21px;line-height:1.35">'
                 + bl("b", "<b>Power</b> — индикатор питания устройства", 21)
                 + '<div style="height:8px"></div>' + bl("b", "<b>Alarm</b> — индикатор перегрева", 21) + '</div>', 2))
    o.append(box(315, 372, 565, 472, 4, "Функциональная кнопка F",
                 '<span class="ab" style="left:30px;top:106px;width:60px;height:60px;border-radius:50%;background:#1f55c8;'
                 'box-shadow:0 0 0 7px #fff inset,0 0 0 3px #1f55c8;border:0"><i style="position:absolute;inset:18px;border-radius:50%;background:#1f55c8"></i></span>'
                 + txt(116, 90, 380, "Менее 10 секунд — перезагрузка<br>Более 10 секунд — перезагрузка и сброс настроек"), 4))
    o.append(box(598, 372, 855, 472, 6, "Combo-порты",
                 img("p079_ic_combo.jpg", 24, 102, 76) + txt(124, 98, 420, "Порты 10/100/1000BASE-T (RJ-45)"), 6))

    def ln(path, s, dots=()):
        d = "".join(f'<circle data-s="{s}" cx="{px(cx)}" cy="{py(cy)}" r="7" fill="#2a6bf2"/>' for cx, cy in dots)
        return f'<path class="dr" data-s="{s}" pathLength="1" d="{path}" stroke="var(--blue)" stroke-width="3" fill="none"/>' + d

    P = lambda *pts: "M" + " L".join(f"{px(x)} {py(y)}" for x, y in pts)
    o.append(layer(
        ln(P((95, 188), (95, 262)), 1, [(95, 262)]),
        ln(P((320, 142), (320, 200), (228, 262), (228, 286)), 3, [(320, 142), (228, 286)]),
        ln(P((355, 244), (355, 236), (548, 236), (548, 244)), 5),
        ln(P((452, 236), (452, 210), (620, 210), (620, 188)), 5, [(620, 188)]),
        ln(P((180, 372), (180, 326)), 2, [(180, 326)]),
        ln(P((263, 372), (263, 326)), 4, [(263, 326)]),
        ln(P((700, 346), (700, 354), (840, 354), (840, 346)), 6),
        ln(P((765, 354), (765, 372)), 6, [(765, 372)])))
    return "".join(o)


SLIDES.append(("p079", "Конструктивное исполнение: передняя панель MES1428", p079()))


# ======================================================= p080 точки доступа outdoor
def p080():
    o = ['<img class="ab" data-s="1" src="assets/p080_scene.jpg" alt="Схема уличной сети Wi-Fi" style="left:0;top:0;width:1920px;'
         '-webkit-mask-image:linear-gradient(to bottom,#000 90%,transparent 100%);mask-image:linear-gradient(to bottom,#000 90%,transparent 100%)">',
         '<div class="ab" style="left:20px;top:40px;width:1080px;height:150px;background:#eef3fd;-webkit-mask-image:radial-gradient(closest-side,#000 80%,transparent);mask-image:radial-gradient(closest-side,#000 80%,transparent)"></div>',
         '<h1 class="t left ab" style="left:62px;top:66px;width:1200px;font-size:84px">Точки доступа: <span class="lt">Outdoor</span></h1>']
    for i, (l, w, t) in enumerate([(28, 594, "Уличное покрытие"), (641, 564, "Питание PoE"), (1223, 662, "Централизованное управление")]):
        o.append(f'<div class="card" data-s="{2 + i}" style="position:absolute;left:{l}px;top:876px;width:{w}px;height:160px;display:flex;gap:30px;align-items:center;padding:0 30px">'
                 f'<img src="assets/p080_i{i + 1}.png" alt="" style="width:110px"><span style="{HEAD}font-size:32px;line-height:1.15">{t}</span></div>')
    return "".join(o)


SLIDES.append(("p080", "Точки доступа: Outdoor", p080()))


# ======================================================= p081 устройство коммутаторов MES
def p081():
    o = [IM("p081_board_r.jpg", 609, 0, 674, 1, "-webkit-mask-image:linear-gradient(90deg,transparent,#000 4%);mask-image:linear-gradient(90deg,transparent,#000 4%)"),
         IM("p081_board_l.jpg", 488, 256, 123, 1, "-webkit-mask-image:linear-gradient(90deg,transparent,#000 25%);mask-image:linear-gradient(90deg,transparent,#000 25%)"),
         '<div class="ab" style="left:56px;top:66px;font-size:80px;font-weight:800;line-height:1;text-transform:uppercase;color:#1b2f86">Устройство</div>',
         '<div class="ab" style="left:56px;top:152px;font-size:58px;font-weight:800;line-height:1;text-transform:uppercase;color:#1b2f86;letter-spacing:-.5px">Коммутаторов-MES</div>',
         '<div class="ab" style="left:58px;top:226px;font-size:30px;font-weight:600;color:#5d6fa8;text-transform:uppercase">Конструктивное исполнение</div>']
    # справа сверху
    o.append(BX(1302, 28, 581, 128, IM("p081_i_sw.png", 12, 16, 116)
                + TX(146, 14, 420, "<b>Коммутатор</b> — специализированный компьютер с процессором, памятью, операционной системой и сетевыми интерфейсами.", 21, "line-height:1.2"), 2))
    o.append(BX(1286, 162, 366, 136, IM("p081_i_chip.png", 4, 18, 84)
                + TX(92, 10, 268, f'<div style="{HEAD}font-size:25px">Чип коммутации</div>'
                     '<div style="font-size:15px;margin-top:6px;line-height:1.25">Быстро обрабатывает и пересылает кадры по простому алгоритму.</div>'), 2))
    o.append(BX(1662, 162, 228, 136, TX(14, 8, 210, f'<div style="{HEAD}font-size:19px">Уровни работы</div>'
                '<div style="margin-top:4px;font-size:17px;white-space:nowrap"><b style="font-size:24px;color:var(--navy)">L2</b> — коммутация</div>'
                '<div style="margin-top:0;font-size:17px;line-height:1.1;white-space:nowrap"><b style="font-size:24px;color:var(--navy)">L3</b> — коммутация<br><span style="margin-left:40px">и маршрутизация</span></div>'), 3))
    o.append(BX(1302, 308, 581, 108, IM("p081_i_gear.png", 22, 22, 68)
                + TX(104, 12, 470, "<b>ОС на базе Linux:</b><br>инициализация системы, управление, функции коммутации и маршрутизации.", 20, "line-height:1.2"), 3))
    # ОЗУ
    def mi(l, w, icon_, t, d):
        return BX(l, 545, w, 128, IM(icon_, 8, 12, 46)
                  + TX(58, 10, w - 62, f'<div style="font-size:19px;font-weight:700;color:var(--navy);white-space:nowrap;letter-spacing:-.4px">{t}</div>'
                       f'<div style="font-size:16px;color:var(--dim);margin-top:2px">{d}</div>'), None, "card solid", "border-radius:14px")
    ram = (IM("p081_i_ram.png", 20, 22, 78) + TX(118, 26, 480, f'<span style="{HEAD}font-size:33px">Оперативная память (ОЗУ)</span>')
           + IM("p081_i_bolt.png", 612, 12, 44) + TX(664, 8, 262, '<b style="color:var(--navy);font-size:19px">Энергозависимая</b>'
           '<div style="font-size:15px;color:var(--dim);margin-top:2px">Данные сохраняются только при наличии электропитания</div>'))
    o.append(BX(26, 427, 930, 499, ram, 4))
    o.append(f'<div data-s="4">' + mi(49, 218, "p081_i_doc.png", "running-config", "текущая конфигурация")
             + mi(276, 201, "p081_i_layers.png", "Буфер обмена", "временное хранение пакетов")
             + mi(490, 224, "p081_i_arp.png", "Таблица ARP", "соответствия IP- и MAC-адресов")
             + mi(727, 207, "p081_i_route.png", "Таблица<br>маршрутизации", "") + '</div>')
    for l, w, lab, img, iw in ((49, 409, "DDR3", "p081_ddr3.png", 208), (477, 446, "DDR4", "p081_ddr4.png", 229)):
        o.append(BX(l, 686, w, 118, TX(32, 40, 120, f'<b style="font-size:28px;color:var(--navy)">{lab}</b>')
                    + IM(img, 140, 6, iw), 4, "card solid", "border-radius:14px"))
    o.append(BX(49, 827, 881, 84, IM("p081_i_warn.png", 30, 10, 64)
                + TX(120, 26, 740, '<b style="font-size:26px;color:#d0263a">При отключении питания содержимое ОЗУ теряется.</b>'),
                5, "card rose", "background:rgba(255,226,232,.92);border-radius:16px"))
    # ПЗУ
    rom = (IM("p081_i_db.png", 26, 18, 62) + TX(120, 26, 470, f'<span style="{HEAD}font-size:33px">Постоянная память (ПЗУ)</span>')
           + IM("p081_i_shield.png", 604, 12, 50) + TX(662, 8, 256, '<b style="color:var(--navy);font-size:19px">Энергонезависимая</b>'
           '<div style="font-size:15px;color:var(--dim);margin-top:2px">Данные сохраняются после отключения питания</div>')
           + BX(20, 122, 887, 57, IM("p081_i_doc2.png", 26, 6, 46)
                + TX(100, 14, 780, "Загрузочные инструкции &bull; POST &bull; конфигурации &bull; прошивки", 22), None, "card solid", "border-radius:12px"))
    o.append(BX(968, 427, 928, 499, rom, 6))
    spi_b = ["U-Boot и переменные окружения", "Factory-параметры: S/N, MAC, HW rev.", "Параметры инициализации<br>DDR-памяти"]
    nand_b = ["startup-config — /mnt/config", "Образы firmware — image-1 / image-2", "Дополнительные данные — /mnt/data",
              "Критические журналы — /mnt/critlog", "Boot-лицензия"]

    def mem(l, w, icon_, title, bullets, img, il, it, iw, top, gap=6):
        lst = "".join(bl("b", b, 19) for b in bullets)
        return BX(l, 614, w, 304, IM(icon_, 18, 14, 60) + TX(96, 26, w - 110, f'<span style="{HEAD}font-size:28px">{title}</span>')
                  + IM(img, il, it, iw) + TX(24, top, w - 40, f'<div style="display:flex;flex-direction:column;gap:{gap}px">{lst}</div>'),
                  7, "card solid", "border-radius:16px")
    o.append(mem(988, 436, "p081_i_chip2.png", "SPI NOR Flash", spi_b, "p081_spi.png", 272, 192, 150, 84))
    o.append(mem(1439, 440, "p081_i_chip3.png", "NAND Flash", nand_b, "p081_nand.png", 276, 206, 150, 66, 1))

    def pw(l, w, icon_, col, label, txt, ricon, lw, s):
        arrow = f'<svg class="ab" style="left:{lw}px;top:30px" width="60" height="34" viewBox="0 0 60 34"><path d="M2 17 H44" stroke="#3d72e8" stroke-width="5"/><path d="M36 4 L58 17 L36 30Z" fill="#3d72e8"/></svg>'
        return BX(l, 947, w, 98, IM(icon_, 14, 10, 80) + TX(110, 32, 300, f'<span style="{HEAD}font-size:24px;color:{col}">{label}</span>')
                  + arrow + BX(lw + 74, 10, w - lw - 94, 78, TX(16, 14, w - lw - 186, txt, 20) + IM(ricon, w - lw - 178, 14, 76), None, "card solid", "border-radius:12px"),
                  s, "card", "border-radius:18px")
    o.append(pw(38, 905, "p081_i_on.png", "#1d8a46", "Питание включено", "<b>ОЗУ</b> хранит рабочие данные", "p081_i_ram2.png", 374, 8))
    o.append(pw(981, 904, "p081_i_off.png", "#d0263a", "Питание выключено", "ПЗУ сохраняет загрузочные<br>файлы и конфигурации", "p081_i_db2.png", 390, 8))
    return "".join(o)


SLIDES.append(("p081", "Устройство коммутаторов MES", p081()))


# ======================================================= p082 WB-2P-LR5
def p082():
    o = ['<img class="ab" data-s="1" src="assets/p082_scene.jpg" alt="WB-2P-LR5 и WOP-2ac-LR5" style="left:0;top:0;width:1920px;'
         '-webkit-mask-image:linear-gradient(to bottom,#000 93%,transparent);mask-image:linear-gradient(to bottom,#000 93%,transparent)">']
    tiles = ["5 ГГц ·<br>IEEE 802.11a/n/ac", "MIMO 2×2", "Мощность<br>до 28 дБм", "Антенна<br>12 дБ", "PoE-инжектор<br>24 В", "Кнопка Reset<br>на инжекторе"]
    xs = [603, 813, 1018, 1219, 1421, 1635]
    for i, (x, tt) in enumerate(zip(xs, tiles)):
        o.append(f'<div class="card solid" data-s="2" style="position:absolute;left:{x}px;top:64px;width:200px;height:180px;padding:12px 6px;'
                 f'text-align:center;border-radius:16px;--dl:{i * 70}ms"><img src="assets/p082_t{i + 1}.png" alt="" style="width:78px">'
                 f'<div style="margin-top:4px;font-size:19px;font-weight:700;color:var(--navy);text-transform:uppercase;line-height:1.2">{tt}</div></div>')
    for i, (l, w, tt) in enumerate([(32, 616, "Дальняя беспроводная связь"), (667, 590, "Доступ к домашней сети"), (1274, 612, "Фиксированный ШПД")]):
        o.append(BX(l, 806, w, 240, IM(f"p082_art{i + 1}.jpg", 0, 98, w, None, "border-radius:0 0 22px 22px;height:142px;object-fit:cover")
                    + IM(f"p082_c{i + 1}.png", 22, 10, 80) + TX(124, 36, w - 130, f'<span style="{HEAD}font-size:25px">{tt}</span>'),
                    3 + i, "card", "border-radius:22px;overflow:hidden"))
    return "".join(o)


SLIDES.append(("p082", "WB-2P-LR5: абонентская станция и базовая станция", p082()))
