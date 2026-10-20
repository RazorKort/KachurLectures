# -*- coding: utf-8 -*-
"""Слайды по референсам p043-p050 (обзор MES, WEP-3ax, режимы CLI, INDOOR, индикаторы, Wi-Fi, характеристики, стекирование)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, icon, arrow_svg

SLIDES = []
K = 1920 / 900

LOC = {
    "cpu": '<rect x="7" y="7" width="10" height="10" rx="2"/><rect x="10" y="10" width="4" height="4"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>',
    "port": '<rect x="3" y="6" width="18" height="12" rx="2.5"/><path d="M7 18v-4h10v4M9 11v3M12 11v3M15 11v3"/>',
    "route3": '<path d="M12 20v-8M12 12L6 6M12 12l6-6M6 6h4M6 6v4M18 6h-4M18 6v4"/>',
    "bidir": '<path d="M3 12h18M3 12l4-4M3 12l4 4M21 12l-4-4M21 12l-4 4"/>',
    "house": '<path d="M4 11l8-7 8 7"/><path d="M6 10v10h12V10"/><path d="M10 20v-6h4v6"/>',
    "building": '<rect x="5" y="3" width="10" height="18" rx="1"/><path d="M15 9h4v12h-4M8 7h4M8 11h4M8 15h4"/>',
    "bank": '<path d="M3 9l9-5 9 5z"/><path d="M5 10v8M9.5 10v8M14.5 10v8M19 10v8M3 20h18"/>',
    "people": '<circle cx="12" cy="7" r="2.5"/><circle cx="5" cy="9" r="2"/><circle cx="19" cy="9" r="2"/><path d="M7 20c0-3 2-5 5-5s5 2 5 5"/><path d="M2 18c0-2 1.2-3.4 3-3.6M22 18c0-2-1.2-3.4-3-3.6"/>',
    "flask": '<path d="M9 3h6M10 3v6l-5 9a2 2 0 0 0 1.8 3h10.4a2 2 0 0 0 1.8-3l-5-9V3"/><path d="M7.5 15h9"/>',
    "hotel": '<rect x="5" y="4" width="14" height="17" rx="1"/><path d="M9 8h2M13 8h2M9 12h2M13 12h2M10 21v-4h4v4"/>',
    "pin": '<path d="M12 21s-6-5.5-6-11a6 6 0 0 1 12 0c0 5.5-6 11-6 11z"/><circle cx="12" cy="10" r="2.3"/>',
    "users": '<circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.4"/><path d="M3 20c0-3.5 2.7-6 6-6s6 2.5 6 6M16 14.5c3 0 5 2 5 5"/>',
    "star": '<path d="M12 3l8 3v5.5c0 4.5-3.2 7.5-8 9.5-4.8-2-8-5-8-9.5V6z"/><path d="M12 8.5l1.4 2.8 3.1.4-2.3 2.1.6 3.1-2.8-1.6-2.8 1.6.6-3.1-2.3-2.1 3.1-.4z"/>',
    "pie": '<circle cx="12" cy="12" r="8.5"/><path d="M12 3.5V12l7.2 4.3M12 12l-6 5"/>',
    "antenna": '<circle cx="12" cy="11" r="1.6"/><path d="M8.5 7.5a5 5 0 0 0 0 7M15.5 7.5a5 5 0 0 1 0 7M5.5 4.5a9 9 0 0 0 0 13M18.5 4.5a9 9 0 0 1 0 13M12 12.6V21"/>',
    "layers3": '<path d="M12 3l9 4.5-9 4.5-9-4.5z"/><path d="M3 12l9 4.5 9-4.5M3 16.5L12 21l9-4.5"/>',
}


def mi(name, cls=""):
    if ".png" in name or ".jpg" in name:   # вырезка из оригинала: "файл.png:ширина"
        f, _, w = name.partition(":")
        return (f'<img src="assets/{f}" alt="" style="width:{w or 96}px;flex:none;'
                f'mix-blend-mode:multiply">')
    if name in LOC:
        return f'<span class="ico {cls}"><svg viewBox="0 0 24 24">{LOC[name]}</svg></span>'
    return ico(name, cls)


def T(x0, y0, x1, y1, extra=""):
    return (f"position:absolute;left:{round(x0*K)}px;top:{round(y0*K)}px;"
            f"width:{round((x1-x0)*K)}px;height:{round((y1-y0)*K)}px;{extra}")


def layer(*parts):
    return ('<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" '
            'viewBox="0 0 1920 1080">' + "".join(parts) + '</svg>')


def feather(px=50, sides="ltrb"):
    """Мягкие края вставки (маска), чтобы кроп не выделялся прямоугольником на фоне."""
    g = {"l": "to right", "r": "to left", "t": "to bottom", "b": "to top"}
    layers = ",".join(f"linear-gradient({g[c]},transparent 0,#000 {px}px)" for c in sides)
    return (f"-webkit-mask-image:{layers};mask-image:{layers};"
            "-webkit-mask-composite:source-in;mask-composite:intersect;")


def H(txt, sz=28, col="var(--navy)", extra=""):
    return (f'<div style="font-size:{sz}px;font-weight:800;color:{col};text-transform:uppercase;'
            f'line-height:1.12;{extra}">{txt}</div>')


def card(box, inner, s=None, cls="card", dl=0, pad=None, extra=""):
    st = box + (f"padding:{pad};" if pad else "") + extra
    d = f' data-s="{s}"' if s else ""
    if dl and s: st += f"--dl:{dl}ms;"
    return f'<div class="{cls}"{d} style="{st}">{inner}</div>'


def icard(box, icn, title, body, s=None, cls="card", tsz=27, bsz=21, dl=0, ics="", gap=22, pad="22px 26px"):
    inner = (f'<div style="display:flex;gap:{gap}px;align-items:center;height:100%">{mi(icn, ics)}'
             f'<div style="flex:1">{H(title, tsz)}<p class="b" style="font-size:{bsz}px;margin-top:8px;'
             f'color:var(--ink)">{body}</p></div></div>')
    return card(box, inner, s, cls, dl, pad)


TAG = ('<div class="ab" style="left:1726px;top:20px;width:170px;font-size:14px;line-height:1.4;color:#98a8d0;'
       'letter-spacing:1.2px;text-transform:uppercase;text-align:center">Надёжные сети для знаний и развития</div>')


# ======================================================= p043 Обзор коммутаторов MES
def p043():
    o = ['<h1 class="t ab" style="left:76px;top:22px;font-size:102px;line-height:1;text-align:left;white-space:nowrap">Обзор коммутаторов MES</h1>',
         TAG]
    # официальный рендер на прозрачном фоне вместо размытого кропа 896px из pptx
    o.append('<img class="ab" src="assets/dev/mes1428.webp" alt="Коммутатор MES1428" style="left:77px;top:324px;width:1229px;'
             'filter:drop-shadow(0 16px 26px rgba(110,100,165,.24))">')
    o.append(icard(T(45, 75, 318, 170), "p035_i_sw.png:138", "Коммутатор",
                   "Специализированный компьютер для быстрого приёма, обработки и пересылки данных.", 1, "card solid", 29, 22))
    chip = (f'<div style="display:flex;gap:22px;align-items:center;height:100%">{mi("p035_i_chip.png:92", "")}'
            f'<div style="flex:1"><div style="font-size:25px;font-weight:800;color:#fff;text-transform:uppercase;line-height:1.1">'
            f'Чип коммутации</div><p style="font-size:20px;line-height:1.35;color:#e8eeff;margin-top:8px">'
            f'Высокоскоростная обработка и передача трафика</p></div></div>')
    o.append(card(T(400, 86, 610, 152, "background:linear-gradient(135deg,#5876f2,#3a4ed0);border-color:rgba(255,255,255,.4);"
                                       "box-shadow:0 0 44px rgba(70,100,255,.55);"), chip, 2, "card", pad="18px 24px"))
    o.append(layer('<g data-s="2"><path class="dr" pathLength="1" d="M853 240 L800 240 L738 366" stroke="#5a86f0" stroke-width="3" fill="none"/>'
                   '<circle class="hd" cx="738" cy="368" r="9" fill="#bcd3ff" stroke="#4d7cf0" stroke-width="3"/></g>'))
    o.append(icard(T(650, 63, 885, 140), "p035_i_func.png:108", "Основная функция",
                   "Подключение конечных пользователей и устройств к сети.", 3, "card", 26, 21, ics="hex", pad="18px 22px"))
    lst = ('<ul style="list-style:none;font-size:20px;line-height:1.4;margin-top:6px">'
           + "".join(f'<li style="display:flex;gap:10px"><span style="color:var(--blue)">&#8226;</span>{t}</li>'
                     for t in ["крупные предприятия", "малый и средний бизнес", "сети операторов связи"]) + '</ul>')
    o.append(card(T(650, 150, 885, 226), f'<div style="display:flex;gap:22px;align-items:center;height:100%">'
                  f'{mi("p035_i_bld.png:108", "")}<div style="flex:1">{H("Где используются", 26)}{lst}</div></div>',
                  4, "card", pad="16px 22px"))
    o.append(icard(T(650, 233, 885, 320), "p035_i_globe.png:108", "Роль в сети",
                   "Коммутаторы работают в разных сегментах сети и решают задачи доступа, агрегации и передачи данных.",
                   4, "card", 26, 20, ics="hex", pad="16px 22px"))
    o.append('<div class="ab ctr-x" data-s="5" style="top:688px;width:900px;text-align:center">'
             '<div style="display:flex;align-items:center;gap:24px"><span style="flex:1;height:3px;background:linear-gradient(90deg,transparent,#7aa3f0)"></span>'
             + H("Как выбрать коммутатор", 46, "var(--navy)", "white-space:nowrap") +
             '<span style="flex:1;height:3px;background:linear-gradient(270deg,transparent,#7aa3f0)"></span></div></div>')
    sel = [(15, 225, "p035_i_ports.png:106", "Количество портов", "Сколько абонентов и устройств нужно подключить"),
           (232, 446, "p035_i_speed.png:106", "Скорость передачи", "Требуемая пропускная способность"),
           (456, 670, "p035_i_seg.png:106", "Сегмент сети", "Доступ, агрегация или операторская сеть"),
           (679, 885, "p035_i_gear.png:106", "Возможности модели", "Функции, характеристики и назначение")]
    for i, (x0, x1, ic, ti, tx) in enumerate(sel):
        o.append(icard(T(x0, 350, x1, 412), ic, ti, tx, 6, "card", 21, 18, dl=i * 120, gap=18, pad="14px 18px"))
    bar = (f'<div style="display:flex;align-items:center;height:100%;gap:26px">'
           f'<div style="flex:1;display:flex;gap:24px;align-items:center;padding-left:20px">{mi("p035_i_route.png:104", "")}'
           f'<p class="b" style="font-size:24px"><b>Маршрутизатор</b> выбирает путь между сетями</p></div>'
           f'<span style="width:2px;height:70px;background:var(--line)"></span>'
           f'<div style="flex:1;display:flex;gap:24px;align-items:center;padding-left:20px">{mi("p035_i_bidir.png:118", "")}'
           f'<p class="b" style="font-size:24px">Коммутатор быстро передаёт данные внутри сетевого сегмента</p></div></div>')
    o.append(card(T(15, 435, 842, 487), bar, 7, "card solid", pad="0 20px"))
    return "".join(o)


SLIDES.append(("p043", "Обзор коммутаторов MES", p043()))


# ======================================================= p044 WEP-3ax
def p044():
    o = ['<h1 class="t ab ctr-x" style="top:44px;width:1700px;font-size:58px">Беспроводная точка доступа '
         '<span style="text-transform:none">WEP-3ax</span></h1>',
         '<img class="ab" src="assets/p070_wep3ax_scene.jpg" alt="Точка доступа WEP-3ax" style="left:0px;top:124px;width:941px;'+feather(60)+'">']
    # официальное фото Eltex поверх точки доступа из сцены (устройства вокруг — вырезка)
    o.append('<img class="ab" src="assets/dev/wep-3ax.webp" alt="WEP-3ax" style="left:170px;top:200px;width:662px;'
             'filter:drop-shadow(0 18px 26px rgba(90,110,190,.28))">')
    wifi_in = icon("wifi")[len('<svg viewBox="0 0 24 24">'):-6]
    wifi6 = ('<div class="ab" style="left:30px;top:30px;width:150px;text-align:center">'
             '<svg viewBox="0 0 24 24" style="width:100px;height:80px;fill:none;stroke:var(--blue);stroke-width:2.4;stroke-linecap:round">'
             + wifi_in +
             '</svg><div style="margin-top:-4px;display:inline-block;background:var(--blue);color:#fff;border-radius:10px;'
             'padding:2px 14px;font-weight:800;font-size:24px">Wi-Fi 6</div></div>'
             '<div class="ab" style="left:210px;top:44px;font-size:42px;font-weight:800;color:var(--navy)">WI-FI 6</div>'
             f'<div class="ab" style="left:28px;top:182px">{mi("speed", "")}</div>'
             '<div class="ab" style="left:128px;top:170px;width:300px;font-size:21px;line-height:1.55;color:var(--ink)">'
             'IEEE 802.11ax<br>574 Мбит/с — 2,4 ГГц<br>1201 Мбит/с — 5 ГГц</div>')
    o.append(card(T(453, 65, 655, 212), f'<div style="position:relative;height:100%">{wifi6}</div>', 1, "card", pad="0"))

    def row(icn, txt, last=False):
        bd = "" if last else "border-bottom:1.5px solid var(--line);"
        return (f'<div style="display:flex;gap:18px;align-items:center;padding:11px 0;{bd}">'
                f'<span style="color:var(--blue);width:44px;flex:none">{mi(icn, "sm")}</span>'
                f'<span style="font-size:21px;line-height:1.3">{txt}</span></div>')
    o.append(card(T(665, 65, 880, 212),
                  f'<div style="display:flex;gap:16px;align-items:center;margin-bottom:6px">{mi("gear", "sm")}{H("Преимущества", 28)}</div>'
                  + row("users", "MU-MIMO 2×2") + row("wifi", "Бесшовный роуминг") + row("antenna", "Внутренние всенаправленные антенны", True),
                  2, "card", pad="18px 22px"))
    sec = (f'<div style="display:flex;gap:16px;align-items:center;margin-bottom:8px">{mi("lock", "sm")}{H("Безопасность", 29)}</div>'
           f'<div style="display:flex;gap:16px;align-items:flex-start;padding:8px 0;border-bottom:1.5px solid var(--line)">'
           f'<span style="width:44px;flex:none">{mi("shield", "sm")}</span><div><b class="mono" style="font-size:21px">WPA3</b>'
           f'<p class="b" style="font-size:19px;margin-top:4px">Современная аутентификация и шифрование</p></div></div>'
           f'<div style="display:flex;gap:16px;align-items:center;padding:8px 0"><span style="width:44px;flex:none">{mi("server", "sm")}</span>'
           f'<p class="b" style="font-size:19px">Совместимость с предыдущими стандартами</p></div>')
    o.append(card(T(453, 218, 655, 362), sec, 3, "card", pad="16px 22px"))
    pw = (f'<div style="display:flex;gap:16px;align-items:center;margin-bottom:10px">{mi("bolt", "sm")}{H("Питание", 29)}</div>'
          f'<div style="display:flex;gap:16px;align-items:center;padding:8px 0;border-bottom:1.5px solid var(--line)">'
          f'<span style="width:44px;flex:none">{mi("wrench", "sm")}</span><b class="mono" style="font-size:21px">PoE+ (IEEE 802.3at)</b></div>'
          f'<div style="display:flex;gap:16px;align-items:center;padding:8px 0"><span style="width:44px;flex:none">{mi("wrench", "sm")}</span>'
          f'<p class="b" style="font-size:19px">Простая установка без отдельной линии питания</p></div>')
    o.append(card(T(665, 218, 880, 362), pw, 4, "card", pad="16px 22px"))

    def col(icn, txt, last=False):
        bd = "" if last else "border-right:1.5px solid var(--line);"
        return (f'<div style="flex:1;display:flex;gap:14px;align-items:center;padding:0 16px;{bd}">'
                f'<span style="color:var(--blue);width:48px;flex:none">{mi(icn, "sm")}</span>'
                f'<span style="font-size:19px;line-height:1.3">{txt}</span></div>')
    sc = (f'<div style="display:flex;gap:18px;align-items:center;margin-bottom:20px">{mi("net", "sm")}{H("Масштабируемость", 32)}</div>'
          '<div style="display:flex">' + col("chart", "Расширение зоны покрытия") + col("users", "Больше подключённых устройств")
          + col("db", "Стабильная работа при высоком трафике", True) + '</div>')
    o.append(card(T(15, 370, 445, 490), sc, 5, "card", pad="20px 22px"))
    where = [("building", "Офисы"), ("bank", "госучреждения"), ("people", "конференц-залы"), ("flask", "лаборатории"), ("hotel", "гостиницы")]
    wh = (f'<div style="display:flex;gap:18px;align-items:center;margin-bottom:16px">{mi("pin", "sm")}{H("Где используется", 32)}</div>'
          '<div style="display:flex;align-items:flex-start;justify-content:space-between">'
          + "".join(f'<div style="flex:1;text-align:center"><div style="color:var(--navy);display:flex;justify-content:center">'
                    f'<span class="ico" style="background:none;border:none;width:60px;height:60px">'
                    f'<svg viewBox="0 0 24 24" style="width:50px;height:50px">{LOC[ic]}</svg></span></div>'
                    f'<div style="font-size:18px;margin-top:8px">{t}</div></div>' for ic, t in where) + '</div>')
    o.append(card(T(453, 370, 885, 490), wh, 6, "card", pad="20px 22px"))
    return "".join(o)


SLIDES.append(("p044", "Беспроводная точка доступа WEP-3ax", p044()))


# ======================================================= p045 Режимы командной строки
def p045():
    o = ['<div class="ab" style="left:48px;top:34px;width:470px">'
         '<h1 class="t" style="font-size:76px;text-align:left;line-height:1">Режимы</h1>'
         '<h1 class="t" style="font-size:72px;text-align:left;line-height:1;color:#6f8fe0">Командной<br>строки</h1></div>',
         '<div class="ab" style="left:48px;top:270px;width:210px;height:3px;background:linear-gradient(90deg,#4a76e8,transparent)"></div>',
         '<img class="ab" src="assets/p055_globe.jpg" alt="" style="left:0;top:295px;width:500px;'
         '-webkit-mask-image:radial-gradient(ellipse 62% 62% at 45% 50%,#000 55%,transparent 100%);'
         'mask-image:radial-gradient(ellipse 62% 62% at 45% 50%,#000 55%,transparent 100%)">']
    steps = [(33, 120, "01", "p055_i1.png:100", "Пользовательский режим", "console&gt;",
              "Непривилегированный доступ &#8226; базовые операции &#8226; ограниченный набор команд"),
             (140, 232, "02", "p055_i2.png:100", "Привилегированный режим", "console#",
              "Диагностика и переход к глобальному конфигурированию"),
             (262, 350, "03", "p055_i3.png:100", "Глобальное конфигурирование", "console(config)#",
              "Настройка параметров устройства и переход к режимам функций"),
             (372, 460, "04", "p055_i4.png:100", "Конфигурирование функционала", None,
              "Интерфейсы &#8226; VLAN &#8226; протоколы &#8226; списки &#8226; линии &#8226; пользователи")]
    for i, (y0, y1, n, ic, title, cmd, desc) in enumerate(steps):
        if cmd:
            mid = (f'<div class="chip mono" style="font-size:27px;padding:8px 36px;margin-top:6px;'
                   f'background:rgba(255,255,255,.95)">{cmd}</div>')
        else:
            mid = ('<div style="display:flex;gap:10px;margin-top:6px;transform:scale(.78);transform-origin:left center;width:128%">' + "".join(
                f'<span class="chip mono" style="font-size:15px;padding:8px 10px;white-space:nowrap">{c}</span>'
                for c in ["console(config-if)#", "console(config-vlan)#", "console(config-line)#"]) + '</div>')
        inner = (f'<div style="display:flex;gap:20px;align-items:center;height:100%">'
                 f'<span style="width:60px;height:60px;border-radius:50%;background:linear-gradient(135deg,#7f9cf0,#4a68d8);'
                 f'color:#fff;display:grid;place-items:center;font-weight:800;font-size:25px;flex:none;'
                 f'box-shadow:0 6px 14px rgba(60,90,200,.3)">{n}</span>{mi(ic, "")}'
                 f'<div style="flex:1;min-width:0">{H(title, 27)}{mid}'
                 f'<p class="b" style="font-size:18px;margin-top:10px;color:var(--dim)">{desc}</p></div></div>')
        o.append(card(T(240, y0, 650, y1), inner, i + 1, "card", pad="12px 22px"))
    ar = []
    for i, y in enumerate([121, 233, 352]):
        ar.append(arrow_svg(960, round(y * K) + 4, 960, round((y + 17) * K), i + 2, w=7))
    o.append(layer(*ar))
    acc = [("p055_user.png:52", "Логин: <b>admin</b>"), ("p055_lock.png:52", "Пароль: <b>admin</b>"),
           ("p055_star.png:52", "Уровень привилегий: <b>15</b>"), ("p055_gear.png:52", "Пользователя нельзя удалить, но можно настроить")]
    rows = "".join(f'<div class="card solid" style="display:flex;gap:16px;align-items:center;padding:12px 16px;margin-top:14px">'
                   f'<span style="color:var(--blue);width:44px;flex:none">{mi(ic, "sm")}</span>'
                   f'<span style="font-size:22px;line-height:1.3">{t}</span></div>' for ic, t in acc)
    o.append(card(T(668, 98, 885, 350), H("Учётная запись по умолчанию", 30, extra="margin-bottom:6px;line-height:1.2") + rows,
                  5, "card", pad="22px 24px"))
    note = (f'<div style="display:flex;gap:22px;align-items:center;height:100%">{mi("p055_info.png:40", "")}'
            f'<span style="font-size:17px;white-space:nowrap">Символ <b class="mono">&gt;</b> — непривилегированный режим</span>'
            f'<span style="font-size:17px;margin-left:16px;white-space:nowrap">Символ <b class="mono">#</b> — привилегированный режим</span></div>')
    o.append(card(T(235, 466, 650, 497), note, 6, "card solid", pad="0 18px"))
    return "".join(o)


SLIDES.append(("p045", "Режимы командной строки", p045()))


# ======================================================= p046 Точки доступа: INDOOR
def p046():
    D = lambda v: round(v * 1920 / 1497)   # координаты верхней половины compare (1497x842)
    o = [f'<img class="ab" data-s="2" src="assets/p068_scene.jpg" alt="Схема офиса с точками доступа WEP-30L" '
         f'style="left:{D(40)}px;top:{D(135)}px;width:{D(1452)}px;{feather(40)}">',
         f'<img class="ab" data-s="2" src="assets/p068_top.jpg" alt="" style="left:{D(800)}px;top:{D(22)}px;width:{D(540)}px;{feather(30, "ltr")}">',
         f'<h1 class="t ab" style="left:{D(48)}px;top:{D(58)}px;font-size:88px;line-height:1;text-align:left;white-space:nowrap">'
         'Точки доступа: <span class="lt">INDOOR</span></h1>',
         f'<div class="ab" data-s="1" style="left:{D(45)}px;top:{D(143)}px;width:{D(452)}px;height:{D(104)}px;padding:14px 26px;'
         'background:#f7f9ff;border:1.5px solid #c9d4f2;border-radius:10px;font-size:22px;line-height:1.35;color:var(--ink)">'
         'Точки доступа делятся на модели для помещений — INDOOR — и модели для уличной установки — OUTDOOR.</div>']
    cards = [(20, 494, "p068_i1.png", 48, "Внутри помещений", "Установка в офисах, учебных корпусах, гостиницах и общественных зданиях."),
             (503, 958, "p068_i2.png", 528, "Единая сеть", "Несколько точек доступа обеспечивают общую зону Wi-Fi."),
             (968, 1475, "p068_i3.png", 993, "Централизованные сервисы", "DHCP выдаёт IP-адреса, RADIUS выполняет аутентификацию.")]
    for i, (x0, x1, im, ix, ti, tx) in enumerate(cards):
        s = f' data-s="{3 + i}"'
        o.append(f'<div class="card ab"{s} style="left:{D(x0)}px;top:{D(667)}px;width:{D(x1 - x0)}px;height:{D(141)}px"></div>')
        o.append(f'<img class="ab"{s} src="assets/{im}" alt="" style="left:{D(ix)}px;top:{D(688)}px;width:{D(92)}px">')
        o.append(f'<div class="ab"{s} style="left:{D(ix + 110)}px;top:{D(695)}px;width:{D(x1 - ix - 122)}px">' + H(ti, 29)
                 + f'<p style="font-size:20px;line-height:1.3;color:var(--ink);margin-top:10px">{tx}</p></div>')
    return "".join(o)


SLIDES.append(("p046", "Точки доступа: INDOOR", p046()))


# ======================================================= p047 Индикаторы интерфейсов
def p047():
    o = ['<div class="ab" style="left:76px;top:28px;width:760px"><h1 class="t" style="font-size:86px;text-align:left;line-height:.98">Индикаторы</h1>'
         '<h1 class="t" style="font-size:86px;text-align:left;line-height:.98;color:#4a76e8">интерфейсов</h1></div>',
         '<img class="ab" src="assets/dev/mes2424.webp" alt="Коммутатор MES2424" style="left:814px;top:4px;width:1084px;'
         'filter:drop-shadow(0 16px 24px rgba(60,80,160,.3))">',
         '<p class="b ab" data-s="1" style="left:80px;top:206px;width:760px;font-size:22px;line-height:1.3">'
         'Индикаторы показывают состояние и активность соответствующего интерфейса.</p>',
         '<p class="b ab" data-s="1" style="left:80px;top:264px;width:760px;font-size:22px;line-height:1.3">'
         'Медные интерфейсы Gigabit Ethernet имеют два светодиода: <b style="color:#2f9d3a">LINK/ACT</b> — зелёный, '
         '<b style="color:#e8891a">SPEED</b> — янтарный.</p>']
    # RJ-45
    rj = (H("Разъём RJ-45", 36, extra="padding:0 0 0 4px")
          + '<div class="ab" style="left:57px;top:92px;width:200px;text-align:center;font-size:22px;font-weight:800;color:#2f9d3a">LINK/ACT</div>'
          '<div class="ab" style="left:334px;top:92px;width:160px;text-align:center;font-size:22px;font-weight:800;color:#e8891a">SPEED</div>'
          '<img class="ab" src="assets/p051_rj45.png" alt="Разъём RJ-45" style="left:106px;top:149px;width:356px">'
          '<div class="ab" style="left:20px;top:410px;width:520px;text-align:center;font-size:21px;line-height:1.35">'
          'Расположение индикаторов у разъёма RJ-45</div>')
    lines = ('<path d="M157 124 L157 200" stroke="#1f3a8a" stroke-width="3" fill="none"/>'
             '<path d="M414 124 L414 200" stroke="#1f3a8a" stroke-width="3" fill="none"/>')
    rj += f'<svg class="ab" style="left:0;top:0;width:560px;height:500px;overflow:visible" viewBox="0 0 560 500">{lines}</svg>'
    o.append(card(T(15, 163, 278, 400), rj, 2, "card", pad="22px 24px"))
    # SFP
    sfp = (H("Индикаторы<br><span style=\"font-size:22px\">оптических интерфейсов</span>", 33, extra="line-height:1.15")
           + '<img class="ab" src="assets/p047_sfp.jpg" alt="Разъём SFP" style="left:0;top:178px;width:207px">'
           '<div class="ab" style="left:232px;top:150px;width:210px;font-size:16px;line-height:1.35;color:var(--dim)">'
           '<b>LNK</b> — соединение / активность</div>'
           '<div class="ab mono" style="left:240px;top:232px;font-size:20px;font-weight:700;color:var(--navy);display:flex;gap:12px;align-items:center">'
           '<i style="width:18px;height:18px;border-radius:50%;background:#43c24a;box-shadow:0 0 10px #43c24a;display:block"></i>LNK</div>'
           '<div class="ab mono" style="left:240px;top:280px;font-size:20px;font-weight:700;color:var(--navy);display:flex;gap:12px;align-items:center">'
           '<i style="width:18px;height:18px;border-radius:50%;background:#43c24a;box-shadow:0 0 10px #43c24a;display:block"></i>SPD</div>'
           '<div class="ab" style="left:240px;top:326px;width:150px;font-size:16px;line-height:1.35;color:var(--dim)">'
           '<b>SPD</b> — скорость</div>'
           '<div class="ab" style="left:20px;top:410px;width:420px;text-align:center;font-size:21px">Внешний вид разъёма SFP</div>')
    o.append(card(T(285, 163, 500, 400), f'<div style="position:relative;height:100%">{sfp}</div>', 3, "card", pad="22px 24px"))

    def th(txt, bg):
        return (f'<th style="background:{bg};color:#fff;font-weight:600;font-size:21px;padding:14px 12px;text-align:center;'
                f'line-height:1.2">{txt}</th>')

    def tr(a, b, c):
        td = 'style="padding:15px 14px;text-align:center;font-size:20px;line-height:1.3;border-bottom:1.5px solid rgba(150,180,230,.4);background:rgba(255,255,255,.72)"'
        return f'<tr><td {td}>{a}</td><td {td}>{b}</td><td {td}>{c}</td></tr>'

    tbl = (f'<table style="width:100%;border-collapse:separate;border-spacing:0;margin-top:18px;border-radius:14px;overflow:hidden">'
           f'<tr>{th("Индикатор<br>SPEED", "linear-gradient(180deg,#f3a244,#e8891a)")}'
           f'{th("Индикатор<br>LINK/ACT", "linear-gradient(180deg,#3fc9a6,#27a98c)")}'
           f'{th("Состояние интерфейса", "linear-gradient(180deg,#5b8cf0,#3a6ce0)")}</tr>'
           + tr("Выключен", "Выключен", "Порт выключен или соединение не установлено")
           + tr("Выключен", "Горит постоянно", "Установлено соединение на скорости 10/100 Мбит/с")
           + tr("Горит постоянно", "Горит постоянно", "Установлено соединение на скорости 1000 Мбит/с")
           + tr("X", "<b>Мигание</b>", "Идёт передача данных") + '</table>')
    o.append(card(T(510, 163, 880, 397), H("Состояние интерфейса", 34, extra="line-height:1.1") + tbl, 4, "card", pad="22px 26px"))
    o.append('<img class="ab" src="assets/p047_cable.jpg" alt="" style="left:1421px;top:864px;width:499px;z-index:3;pointer-events:none">')
    return "".join(o)


SLIDES.append(("p047", "Индикаторы интерфейсов", p047()))


# ======================================================= p048 Технологии Wi-Fi
def p048():
    D = lambda v: round(v * 1920 / 1497)   # координаты верхней половины compare (1497x842)
    o = [f'<h1 class="t ab ctr-x" style="top:{D(28)}px;width:1600px;font-size:84px;line-height:1">Технологии Wi-Fi</h1>']
    cards = [(25, 115, 743, 398, "Бесшовный роуминг", "Устройство автоматически переключается между точками доступа без разрыва соединения.",
              "802.11r/k/v", "p067_roam.jpg", (338, 192, 738), 270, 322),
             (755, 115, 1473, 398, "MIMO", "Несколько антенн передают несколько потоков данных одному устройству.",
              "Выше скорость и стабильность", "p067_mimo.jpg", (1010, 128, 1466), 240, 322),
             (25, 410, 743, 677, "MU-MIMO", "Точка доступа одновременно передаёт данные нескольким устройствам.",
              "Меньше ожидания для клиентов", "p067_mumimo.jpg", (318, 413, 738), 260, 603),
             (755, 410, 1473, 677, "OFDMA", "Канал делится на части, которые одновременно распределяются между клиентами.",
              "Эффективнее при высокой нагрузке", "p067_ofdma.jpg", (1008, 423, 1462), 210, 620)]
    for i, (x0, y0, x1, y1, ti, tx, tg, im, (ix0, iy0, ix1), tw, tgy) in enumerate(cards):
        s = f' data-s="{i + 1}"'
        o.append(f'<div class="card ab"{s} style="left:{D(x0)}px;top:{D(y0)}px;width:{D(x1 - x0)}px;height:{D(y1 - y0)}px"></div>')
        o.append(f'<img class="ab"{s} src="assets/{im}" alt="" style="left:{D(ix0)}px;top:{D(iy0)}px;width:{D(ix1 - ix0)}px;'
                 f'mix-blend-mode:multiply;{feather(26)}">')
        o.append(f'<div class="ab"{s} style="left:{D(x0 + 37)}px;top:{D(y0 + 38)}px;width:{D(tw)}px">'
                 + H(ti, 44, extra="white-space:nowrap") +
                 f'<p style="font-size:21px;line-height:1.35;color:var(--ink);margin-top:16px">{tx}</p></div>')
        o.append(f'<div class="ab"{s} style="left:{D(x0 + 37)}px;top:{D(tgy)}px;padding:6px 18px;border:1.5px solid #b9c6ec;'
                 f'border-radius:10px;background:rgba(255,255,255,.85);font-size:{19 if i < 3 else 15}px;font-weight:600;color:var(--navy)">{tg}</div>')

    def it(img, key, txt, last=False):
        bd = "" if last else "border-right:2px solid var(--line);"
        return (f'<div style="flex:1;display:flex;gap:22px;align-items:center;padding:0 22px;{bd}">'
                f'<img src="assets/{img}" alt="" style="width:{D(88)}px;flex:none">'
                f'<p style="font-size:22px;line-height:1.3;color:var(--ink)"><b style="color:var(--navy)">{key}</b> — {txt}</p></div>')
    bar = ('<div style="display:flex;align-items:center;height:100%">'
           + it("p067_i1.png", "MIMO", "несколько потоков одному клиенту")
           + it("p067_i2.png", "MU-MIMO", "потоки нескольким клиентам")
           + it("p067_i3.png", "OFDMA", "разделение канала между клиентами", True) + '</div>')
    o.append(f'<div class="card ab" data-s="5" style="left:{D(62)}px;top:{D(698)}px;width:{D(1378)}px;height:{D(102)}px;padding:0 20px">{bar}</div>')
    return "".join(o)


SLIDES.append(("p048", "Технологии Wi-Fi", p048()))


# ======================================================= p049 Основные характеристики коммутаторов
def p049():
    D = lambda v: round(v * 1920 / 1497)   # координаты верхней половины compare (1497x842)
    o = ['<h1 class="t ab ctr-x" style="top:36px;width:1700px;font-size:76px;line-height:1">Основные характеристики</h1>',
         '<h1 class="t ab ctr-x" style="top:112px;width:1700px;font-size:76px;line-height:1;color:#7f9ad8">коммутаторов</h1>']
    P = "font-size:20px;line-height:1.3;color:var(--ink);margin-top:10px"

    def cell(x0, y0, x1, y1, im, ix0, iy0, ix1, tx0, ty0, title, txt, s, dl, extra=""):
        o.append(f'<div class="card ab" data-s="{s}" style="left:{D(x0)}px;top:{D(y0)}px;width:{D(x1 - x0)}px;'
                 f'height:{D(y1 - y0)}px;--dl:{dl}ms"></div>')
        o.append(f'<img class="ab" data-s="{s}" src="assets/{im}" alt="" style="left:{D(ix0)}px;top:{D(iy0)}px;'
                 f'width:{D(ix1 - ix0)}px;mix-blend-mode:multiply;--dl:{dl}ms">')
        o.append(f'<div class="ab" data-s="{s}" style="left:{D(tx0)}px;top:{D(ty0)}px;width:{D(x1 - tx0) - 14}px;--dl:{dl}ms">'
                 f'{H(title, 23)}<p style="{P}">{txt}</p>{extra}</div>')
    xs = [(28, 385), (396, 743), (755, 1102), (1114, 1468)]
    r1 = [("p036_types.png", 45, 200, 188, 192, "Тип коммутатора", "Фиксированный &#8226; модульный &#8226; стекируемый.", ""),
          ("p036_rack.png", 412, 185, 556, 563, "Монтажная единица", "1U (RU) = 4,445&nbsp;см = 1,75&nbsp;дюйма.", ""),
          ("p036_ports.png", 765, 205, 892, 903, "Плотность портов", "Количество портов в 1U или стойке.",
           '<p style="font-size:16px;line-height:1.25;color:var(--dim);margin-top:6px">Учитываются абонентские порты, uplink и питание.</p>'),
          ("p036_coins.png", 1122, 198, 1258, 1262, "Стоимость порта", "Цена устройства ÷ количество портов.", "")]
    for i, ((x0, x1), (im, a, b, c, tx, ti, txt, ex)) in enumerate(zip(xs, r1)):
        cell(x0, 172, x1, 345, im, a, b, c, tx, 200, ti, txt, 1, i * 110, ex)
    r2 = [("p036_speed.png", 38, 388, 188, 195, "Скорость пересылки", "Объём данных, обрабатываемых за секунду."),
          ("p036_shield.png", 412, 378, 552, 565, "Надёжность", "Непрерывность доступа к сети."),
          ("p036_poe.png", 758, 378, 897, 925, "PoE", "Питание оконечных устройств по кабелю передачи данных."),
          ("p036_growth.png", 1128, 383, 1248, 1265, "Масштабируемость", "Подключение новых пользователей через свободные порты.")]
    for i, ((x0, x1), (im, a, b, c, tx, ti, txt)) in enumerate(zip(xs, r2)):
        cell(x0, 357, x1, 532, im, a, b, c, tx, 386, ti.replace("PoE", '<span style="text-transform:none">PoE</span>'), txt, 2, i * 110)
    o.append(f'<div class="ab ctr-x" data-s="3" style="top:{D(550)}px;width:900px;display:flex;align-items:center;gap:18px">'
             '<span style="flex:1;height:2px;background:linear-gradient(90deg,transparent,#8fa3d8)"></span>'
             + H("Типы коммутаторов", 40, extra="white-space:nowrap") +
             '<span style="flex:1;height:2px;background:linear-gradient(270deg,transparent,#8fa3d8)"></span></div>')
    shadow = "filter:drop-shadow(0 12px 18px rgba(90,100,170,.25))"
    pics = [f'<img class="ab" src="assets/dev/mes2424.webp" alt="MES2424" style="left:{D(165)}px;top:{D(628)}px;width:{D(300)}px;{shadow}">',
            f'<img class="ab" src="assets/p036_modular.png" alt="" style="left:{D(570)}px;top:{D(612)}px;width:{D(355)}px;mix-blend-mode:multiply">',
            f'<img class="ab" src="assets/dev/mes3324f.webp" alt="MES3324F" style="left:1383px;top:778px;width:260px;{shadow}">'
            f'<img class="ab" src="assets/dev/mes3324f.webp" alt="MES3324F" style="left:1383px;top:845px;width:260px;{shadow}">']
    r3 = [(113, 520, "Фиксированный", "Тип и количество интерфейсов изменить нельзя."),
          (530, 966, "Модульный", "Порты добавляются платами расширения. Гибче, но дороже."),
          (977, 1384, "Стекируемый", "Несколько устройств работают как одно логическое.")]
    for i, (x0, x1, ti, tx) in enumerate(r3):
        o.append(f'<div class="ab" data-s="{4 + i}" style="left:0;top:0;width:1920px;height:1080px;pointer-events:none">'
                 f'<div class="card ab" style="left:{D(x0)}px;top:{D(600)}px;width:{D(x1 - x0)}px;height:{D(212)}px"></div>'
                 f'{pics[i]}<div class="ab" style="left:{D(x0) + 20}px;top:{D(718)}px;width:{D(x1 - x0) - 40}px;text-align:center">'
                 f'{H(ti, 26)}<p style="font-size:19px;line-height:1.3;color:var(--ink);margin-top:6px">{tx}</p></div></div>')
    return "".join(o)


SLIDES.append(("p049", "Основные характеристики коммутаторов", p049()))


# ======================================================= p050 Стекирование и плотность портов
LOC_CHECK = icon('check')[len('<svg viewBox="0 0 24 24">'):-6]


def _rows(items, fs):
    out = ""
    bd = "border-bottom:1.5px solid rgba(150,180,230,.35);"
    for k, v, hl in items:
        h = (f'<span style="display:inline-block;background:#dcf1e4;color:#1f8a54;font-weight:700;border-radius:8px;'
             f'padding:3px 8px;font-size:12px;line-height:1.2">{hl}</span>') if hl else ""
        out += (f'<tr><td style="padding:6px 8px;font-size:{fs}px;line-height:1.2;{bd}">{k}:</td>'
                f'<td style="padding:6px 6px;font-size:{fs}px;font-weight:700;line-height:1.2;{bd}">{v}</td>'
                f'<td style="padding:3px 6px;text-align:right;width:28%;{bd}">{h}</td></tr>')
    return ('<table style="border-collapse:separate;border-spacing:0;background:rgba(255,255,255,.8);border-radius:10px;'
            'overflow:hidden;width:100%">' + out + '</table>')


def p050():
    o = ['<h1 class="t ab ctr-x" style="top:22px;width:1700px;font-size:60px">Стекирование и плотность портов</h1>']
    sh = "filter:drop-shadow(0 10px 16px rgba(90,100,170,.25))"
    ok = ('<span style="color:var(--blue);width:36px;flex:none"><svg viewBox="0 0 24 24" style="width:34px;height:34px;fill:none;'
          'stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round">' + LOC_CHECK + '</svg></span>')
    lst = "".join(f'<div style="display:flex;gap:10px;align-items:center;margin-bottom:18px">{ok}'
                  f'<span style="font-size:20px;line-height:1.2">{t}</span></div>'
                  for t in ["до 8 устройств в одном стеке", "больше доступных портов",
                            "единое логическое управление", "короткий путь между устройствами"])
    sw = lambda l, t, w, s="": f'<img class="ab"{s} src="assets/dev/mes2424.webp" alt="MES2424" style="left:{l}px;top:{t}px;width:{w}px;{sh}">'
    lab = "font-size:22px;font-weight:800;color:var(--navy);text-align:center"
    o.append('<div class="card ab" data-s="1" style="left:20px;top:110px;width:1260px;height:420px"></div>')
    o.append('<div class="ab" data-s="1" style="left:50px;top:132px">' + H("Стекирование коммутаторов", 38) + '</div>')
    o.append(f'<div class="ab" data-s="1" style="left:50px;top:196px;width:440px;{lab}">2 физических устройства</div>')
    o.append(sw(50, 236, 400, ' data-s="1"'))
    o.append('<div class="ab" data-s="1" style="left:60px;top:344px;font-size:18px;color:var(--dim)">Коммутатор 1 · 24 порта + 2 Uplink/SFP</div>')
    o.append(sw(50, 384, 400, ' data-s="1"'))
    o.append('<div class="ab" data-s="1" style="left:60px;top:492px;font-size:18px;color:var(--dim)">Коммутатор 2 · 24 порта + 2 Uplink/SFP</div>')
    o.append('<svg class="ab" data-s="2" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" viewBox="0 0 1920 1080">'
             '<path d="M452 290 C540 300 540 440 452 440" stroke="#6a60e8" stroke-width="4" fill="none"/>'
             '<path d="M460 280 L446 290 L462 300 Z" fill="#6a60e8"/><path d="M460 430 L446 440 L462 450 Z" fill="#6a60e8"/>'
             '<path d="M572 368 H608" stroke="#3a6ce0" stroke-width="16"/><path d="M604 342 L640 368 L604 394 Z" fill="#3a6ce0"/></svg>')
    o.append('<div class="ab" data-s="2" style="left:470px;top:196px;width:175px;font-size:16px;line-height:1.25">Uplink 1 первого — Uplink 2 второго</div>')
    o.append('<div class="ab" data-s="2" style="left:470px;top:462px;width:175px;font-size:16px;line-height:1.25">Uplink 1 второго — Uplink 2 первого</div>')
    o.append(f'<div class="ab" data-s="3" style="left:650px;top:196px;width:400px;{lab}">1 логический коммутатор</div>')
    o.append('<div class="ab" data-s="3" style="left:650px;top:240px;width:400px;height:250px;border:3px solid #7d8cf0;border-radius:20px;'
             'box-shadow:0 0 28px rgba(110,120,240,.35);background:rgba(255,255,255,.45)"></div>')
    o.append(sw(670, 268, 360, ' data-s="3"') + sw(670, 370, 360, ' data-s="3"'))
    o.append(f'<div class="ab" data-s="4" style="left:1068px;top:200px;width:200px">{lst}</div>')

    ul = ('<div class="chip" style="font-size:20px;padding:8px 14px;margin-top:14px;font-family:var(--f);font-weight:500;'
          'justify-content:center;gap:12px;width:100%">E1 <span style="color:var(--blue)">&#8226;</span> 10 Gigabit Ethernet '
          '<span style="color:var(--blue)">&#8226;</span> оптоволокно</div>')

    def mini(img, lb, val):
        return ('<div class="card solid" style="flex:1;display:flex;gap:12px;align-items:center;padding:10px 14px">'
                f'<img src="assets/{img}" alt="" style="width:64px;border-radius:10px"><div>'
                f'<div style="font-size:18px">{lb}</div><div class="mono" style="font-size:22px;font-weight:800;color:var(--blue);'
                f'white-space:nowrap">{val}</div></div></div>')
    B = (H("Uplink-интерфейс", 34, extra="margin-bottom:10px")
         + '<p class="b" style="font-size:20px;line-height:1.35">Высокоскоростной интерфейс для подключения к вышестоящему '
           'коммутатору или маршрутизатору.</p><p class="b" style="font-size:20px;line-height:1.35;margin-top:8px">'
           'Благодаря SFP-модулям может использовать разные типы соединений.</p>' + ul
         + '<div style="display:flex;gap:14px;margin-top:14px">' + mini("p050_ethport.jpg", "Ethernet-порт:", "100 Мбит/с")
         + mini("p050_uplink.jpg", "Uplink:", "1 Гбит/с") + '</div>')
    o.append(f'<div class="card ab" data-s="5" style="left:1300px;top:110px;width:600px;height:420px;padding:22px 26px">{B}</div>')

    o.append('<div class="ab" data-s="6" style="left:40px;top:548px">' + H("Два способа получить 48 портов", 40) + '</div>')
    left_rows = [("Место в стойке", "2 RU", ""), ("Розетки 220 В", "2", ""), ("Абонентские порты", "2 × 24 = 48", ""),
                 ("Скорость портов", "48 × 100 Мбит/с = 4,8 Гбит/с", ""), ("Условная стоимость", "300 единиц", ""),
                 ("Стоимость порта", "300 ÷ 48 = 6,25", "")]
    right_rows = [("Место в стойке", "1 RU", "−1 RU"), ("Розетки 220 В", "1", "−1 розетка"),
                  ("Абонентские порты", "1 × 48 = 48", ""), ("Скорость портов", "48 × 100 Мбит/с = 4,8 Гбит/с", ""),
                  ("Условная стоимость", "250 единиц", "−50 единиц"), ("Стоимость порта", "250 ÷ 48 = 5,21", "−1,04 за порт")]
    for i, (x, title, pic, rows) in enumerate([
            (20, "2 × 24-портовых коммутатора", sw(44, 700, 300) + sw(44, 790, 300), left_rows),
            (970, "1 × 48-портовый коммутатор",
             f'<img class="ab" src="assets/dev/mes2300b-48.png" alt="MES2300B-48" style="left:994px;top:720px;width:300px;{sh}">', right_rows)]):
        s = f' data-s="{7 + i}"'
        o.append(f'<div class="card ab"{s} style="left:{x}px;top:610px;width:930px;height:300px"></div>')
        o.append(f'<div class="ab"{s} style="left:{x + 24}px;top:626px">' + H(title, 27) + '</div>')
        o.append(f'<div class="ab"{s} style="left:0;top:0;width:1920px;height:1080px;pointer-events:none">{pic}</div>')
        o.append(f'<div class="ab"{s} style="left:{x + 330}px;top:668px;width:585px;{"white-space:nowrap" if i == 0 else ""}">{_rows(rows, 17)}</div>')
    o.append(icard("position:absolute;left:20px;top:926px;width:840px;height:136px;", "layers3", "Плотность портов",
                   "Количество портов в ограниченном пространстве. Высокая плотность экономит место и энергоресурсы.",
                   9, "card", 25, 18, gap=18, pad="10px 20px"))
    o.append(icard("position:absolute;left:880px;top:926px;width:1020px;height:136px;", "speed", "Скорость",
                   "Производительность — объём данных, обрабатываемых за секунду. "
                   "Скорости Ethernet-портов: 100 Мбит/с, 1, 10 и 100 Гбит/с.",
                   9, "card", 25, 18, gap=18, pad="10px 20px", dl=120))
    return "".join(o)


SLIDES.append(("p050", "Стекирование и плотность портов", p050()))
