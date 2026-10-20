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
    o = ['<h1 class="t ab" style="left:76px;top:26px;font-size:80px;text-align:left;white-space:nowrap">Обзор коммутаторов MES</h1>',
         TAG]
    # официальный рендер на прозрачном фоне вместо размытого кропа 896px из pptx
    o.append('<img class="ab" src="assets/dev/mes1428.webp" alt="Коммутатор MES1428" style="left:77px;top:324px;width:1229px;'
             'filter:drop-shadow(0 16px 26px rgba(110,100,165,.24))">')
    o.append(icard(T(45, 75, 318, 170), "cpu", "Коммутатор",
                   "Специализированный компьютер для быстрого приёма, обработки и пересылки данных.", 1, "card solid", 29, 22))
    chip = (f'<div style="display:flex;gap:22px;align-items:center;height:100%">{mi("cpu", "")}'
            f'<div style="flex:1"><div style="font-size:25px;font-weight:800;color:#fff;text-transform:uppercase;line-height:1.1">'
            f'Чип коммутации</div><p style="font-size:20px;line-height:1.35;color:#e8eeff;margin-top:8px">'
            f'Высокоскоростная обработка и передача трафика</p></div></div>')
    o.append(card(T(400, 86, 610, 152, "background:linear-gradient(135deg,#5876f2,#3a4ed0);border-color:rgba(255,255,255,.4);"
                                       "box-shadow:0 0 44px rgba(70,100,255,.55);"), chip, 2, "card", pad="18px 24px"))
    o.append(layer('<g data-s="2"><path class="dr" pathLength="1" d="M853 240 L800 240 L738 366" stroke="#5a86f0" stroke-width="3" fill="none"/>'
                   '<circle class="hd" cx="738" cy="368" r="9" fill="#bcd3ff" stroke="#4d7cf0" stroke-width="3"/></g>'))
    o.append(icard(T(650, 63, 885, 140), "route3", "Основная функция",
                   "Подключение конечных пользователей и устройств к сети.", 3, "card", 26, 21, ics="hex", pad="18px 22px"))
    lst = ('<ul style="list-style:none;font-size:20px;line-height:1.4;margin-top:6px">'
           + "".join(f'<li style="display:flex;gap:10px"><span style="color:var(--blue)">&#8226;</span>{t}</li>'
                     for t in ["крупные предприятия", "малый и средний бизнес", "сети операторов связи"]) + '</ul>')
    o.append(card(T(650, 150, 885, 226), f'<div style="display:flex;gap:22px;align-items:center;height:100%">'
                  f'{mi("building", "hex")}<div style="flex:1">{H("Где используются", 26)}{lst}</div></div>',
                  4, "card", pad="16px 22px"))
    o.append(icard(T(650, 233, 885, 320), "globe", "Роль в сети",
                   "Коммутаторы работают в разных сегментах сети и решают задачи доступа, агрегации и передачи данных.",
                   4, "card", 26, 20, ics="hex", pad="16px 22px"))
    o.append('<div class="ab ctr-x" data-s="5" style="top:688px;width:900px;text-align:center">'
             '<div style="display:flex;align-items:center;gap:24px"><span style="flex:1;height:3px;background:linear-gradient(90deg,transparent,#7aa3f0)"></span>'
             + H("Как выбрать коммутатор", 46, "var(--navy)", "white-space:nowrap") +
             '<span style="flex:1;height:3px;background:linear-gradient(270deg,transparent,#7aa3f0)"></span></div></div>')
    sel = [(15, 225, "port", "Количество портов", "Сколько абонентов и устройств нужно подключить"),
           (232, 446, "speed", "Скорость передачи", "Требуемая пропускная способность"),
           (456, 670, "net", "Сегмент сети", "Доступ, агрегация или операторская сеть"),
           (679, 885, "gear", "Возможности модели", "Функции, характеристики и назначение")]
    for i, (x0, x1, ic, ti, tx) in enumerate(sel):
        o.append(icard(T(x0, 350, x1, 412), ic, ti, tx, 6, "card", 21, 18, dl=i * 120, gap=18, pad="14px 18px"))
    bar = (f'<div style="display:flex;align-items:center;height:100%;gap:26px">'
           f'<div style="flex:1;display:flex;gap:24px;align-items:center;padding-left:20px">{mi("route3", "sm")}'
           f'<p class="b" style="font-size:24px"><b>Маршрутизатор</b> выбирает путь между сетями</p></div>'
           f'<span style="width:2px;height:70px;background:var(--line)"></span>'
           f'<div style="flex:1;display:flex;gap:24px;align-items:center;padding-left:20px">{mi("bidir", "sm")}'
           f'<p class="b" style="font-size:24px">Коммутатор быстро передаёт данные внутри сетевого сегмента</p></div></div>')
    o.append(card(T(15, 435, 842, 487), bar, 7, "card solid", pad="0 20px"))
    return "".join(o)


SLIDES.append(("p043", "Обзор коммутаторов MES", p043()))


# ======================================================= p044 WEP-3ax
def p044():
    o = ['<h1 class="t ab ctr-x" style="top:44px;width:1700px;font-size:58px">Беспроводная точка доступа '
         '<span style="text-transform:none">WEP-3ax</span></h1>',
         '<img class="cut ab" src="assets/p044_ap_scene.jpg" alt="Точка доступа WEP-3ax" style="left:38px;top:130px;width:902px;'+feather(70)+'">']
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
         '<h1 class="t" style="font-size:68px;text-align:left;line-height:1.1">Режимы</h1>'
         '<h1 class="t" style="font-size:54px;text-align:left;line-height:1.38;color:#6f8fe0">Командной<br>строки</h1></div>',
         '<div class="ab" style="left:48px;top:262px;width:210px;height:3px;background:linear-gradient(90deg,#4a76e8,transparent)"></div>',
         '<img class="ab" src="assets/p045_globe.jpg" alt="" style="left:0;top:340px;width:440px;'
         '-webkit-mask-image:radial-gradient(ellipse 62% 62% at 45% 50%,#000 55%,transparent 100%);'
         'mask-image:radial-gradient(ellipse 62% 62% at 45% 50%,#000 55%,transparent 100%)">']
    steps = [(33, 120, "01", "term", "Пользовательский режим", "console&gt;",
              "Непривилегированный доступ &#8226; базовые операции &#8226; ограниченный набор команд"),
             (140, 232, "02", "key", "Привилегированный режим", "console#",
              "Диагностика и переход к глобальному конфигурированию"),
             (262, 350, "03", "gear", "Глобальное конфигурирование", "console(config)#",
              "Настройка параметров устройства и переход к режимам функций"),
             (372, 460, "04", "net", "Конфигурирование функционала", None,
              "Интерфейсы &#8226; VLAN &#8226; протоколы &#8226; списки &#8226; линии &#8226; пользователи")]
    for i, (y0, y1, n, ic, title, cmd, desc) in enumerate(steps):
        if cmd:
            mid = (f'<div class="chip mono" style="font-size:27px;padding:8px 36px;margin-top:6px;'
                   f'background:rgba(255,255,255,.95)">{cmd}</div>')
        else:
            mid = ('<div style="display:flex;gap:10px;margin-top:6px">' + "".join(
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
    acc = [("user", "Логин: <b>admin</b>"), ("lock", "Пароль: <b>admin</b>"),
           ("star", "Уровень привилегий: <b>15</b>"), ("gear", "Пользователя нельзя удалить, но можно настроить")]
    rows = "".join(f'<div class="card solid" style="display:flex;gap:16px;align-items:center;padding:12px 16px;margin-top:14px">'
                   f'<span style="color:var(--blue);width:44px;flex:none">{mi(ic, "sm")}</span>'
                   f'<span style="font-size:22px;line-height:1.3">{t}</span></div>' for ic, t in acc)
    o.append(card(T(668, 98, 885, 350), H("Учётная запись по умолчанию", 30, extra="margin-bottom:6px;line-height:1.2") + rows,
                  5, "card", pad="22px 24px"))
    note = (f'<div style="display:flex;gap:22px;align-items:center;height:100%">{mi("info", "sm")}'
            f'<span style="font-size:17px;white-space:nowrap">Символ <b class="mono">&gt;</b> — непривилегированный режим</span>'
            f'<span style="font-size:17px;margin-left:16px;white-space:nowrap">Символ <b class="mono">#</b> — привилегированный режим</span></div>')
    o.append(card(T(235, 466, 650, 497), note, 6, "card solid", pad="0 18px"))
    return "".join(o)


SLIDES.append(("p045", "Режимы командной строки", p045()))


# ======================================================= p046 Точки доступа: INDOOR
def p046():
    o = ['<h1 class="t ab" style="left:56px;top:86px;font-size:64px;text-align:left;white-space:nowrap">'
         'Точки доступа: <span class="lt">INDOOR</span></h1>']
    o.append('<img class="ab" data-s="2" src="assets/p046_office_l.jpg" alt="" style="left:58px;top:324px;width:594px;'+feather(40,"lt")+'">')
    o.append('<img class="ab" data-s="3" src="assets/p046_office_m.jpg" alt="" style="left:653px;top:184px;width:365px;'+feather(40,"t")+'">')
    o.append('<img class="ab" data-s="3" src="assets/p046_office_r.jpg" alt="Схема помещения с точками доступа" style="left:1018px;top:32px;width:891px;'+feather(40,"t")+'">')
    o.append(card(T(28, 85, 300, 148),
                  '<p class="b" style="font-size:25px;line-height:1.4">Точки доступа делятся на модели для помещений — '
                  '<b>INDOOR</b> — и модели для уличной установки — <b>OUTDOOR</b>.</p>', 1, "card solid", pad="14px 24px"))
    cards = [(8, 298, "house", "Внутри помещений", "Установка в офисах, учебных корпусах, гостиницах и общественных зданиях."),
             (303, 578, "wifi", "Единая сеть", "Несколько точек доступа обеспечивают общую зону Wi-Fi."),
             (583, 885, "server", "Централизованные сервисы", "DHCP выдаёт IP-адреса, RADIUS выполняет аутентификацию.")]
    for i, (x0, x1, ic, ti, tx) in enumerate(cards):
        o.append(icard(T(x0, 400, x1, 493), ic, ti, tx, 4 + i, "card", 26, 20, ics="hex", gap=20, pad="16px 24px"))
    return "".join(o)


SLIDES.append(("p046", "Точки доступа: INDOOR", p046()))


# ======================================================= p047 Индикаторы интерфейсов
def p047():
    o = ['<div class="ab" style="left:76px;top:28px;width:760px"><h1 class="t" style="font-size:76px;text-align:left;line-height:1.1">Индикаторы</h1>'
         '<h1 class="t" style="font-size:76px;text-align:left;line-height:1.1;color:#4a76e8">интерфейсов</h1></div>',
         '<img class="cut ab" src="assets/p047_switch.jpg" alt="Коммутатор MES" style="left:806px;top:108px;width:1094px;'
         + feather(30, "lb") + '">',
         '<p class="b ab" data-s="1" style="left:80px;top:205px;width:700px;font-size:20px;line-height:1.4">'
         'Индикаторы показывают состояние и активность соответствующего интерфейса.</p>',
         '<p class="b ab" data-s="1" style="left:80px;top:262px;width:700px;font-size:20px;line-height:1.4">'
         'Медные интерфейсы Gigabit Ethernet имеют два светодиода: <b style="color:#2f9d3a">LINK/ACT</b> — зелёный, '
         '<b style="color:#e8891a">SPEED</b> — янтарный.</p>']
    # RJ-45
    rj = (H("Разъём RJ-45", 36, extra="padding:0 0 0 4px")
          + '<div class="ab" style="left:24px;top:98px;width:200px;text-align:center;font-size:22px;font-weight:800;color:#2f9d3a">LINK/ACT</div>'
          '<div class="ab" style="left:300px;top:98px;width:160px;text-align:center;font-size:22px;font-weight:800;color:#e8891a">SPEED</div>'
          '<img class="ab" src="assets/p047_rj45.jpg" alt="Разъём RJ-45" style="left:102px;top:160px;width:384px">'
          '<div class="ab" style="left:20px;top:410px;width:520px;text-align:center;font-size:21px;line-height:1.35">'
          'Расположение индикаторов у разъёма RJ-45</div>')
    lines = ('<path d="M124 128 L124 190" stroke="#2f9d3a" stroke-width="3" fill="none"/><circle cx="124" cy="196" r="6" fill="#2f9d3a"/>'
             '<path d="M380 128 L380 190" stroke="#e8891a" stroke-width="3" fill="none"/><circle cx="380" cy="196" r="6" fill="#e8891a"/>')
    rj += f'<svg class="ab" style="left:0;top:0;width:560px;height:500px;overflow:visible" viewBox="0 0 560 500">{lines}</svg>'
    o.append(card(T(15, 163, 278, 400), rj, 2, "card", pad="22px 24px"))
    # SFP
    sfp = (H("Индикаторы<br><span style=\"font-size:22px\">оптических интерфейсов</span>", 33, extra="line-height:1.15")
           + '<img class="ab" src="assets/p047_sfp.jpg" alt="Разъём SFP" style="left:0;top:178px;width:207px">'
           '<div class="ab" style="left:240px;top:150px;width:150px;font-size:16px;line-height:1.35;color:var(--dim)">'
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
    o = ['<h1 class="t ab ctr-x" style="top:50px;width:1600px;font-size:66px">Технологии Wi-Fi</h1>']

    def box(x0, y0, x1, y1, title, txt, tagtxt, img, imgbox, s, twd):
        inner = (H(title, 40, extra="line-height:1.1") +
                 f'<p class="b" style="font-size:21px;line-height:1.45;margin-top:18px;width:{twd}px">{txt}</p>'
                 f'<div class="tag" style="position:absolute;left:34px;bottom:30px;font-size:16px;padding:5px 15px;'
                 f'font-weight:500;background:rgba(255,255,255,.85)">{tagtxt}</div>'
                 f'<img class="ab" src="assets/{img}" alt="" style="{imgbox};{feather(22)}">')
        return card(T(x0, y0, x1, y1, "overflow:hidden;"), f'<div style="position:relative;height:100%">{inner}</div>', s, "card", pad="26px 34px")

    o.append(box(15, 68, 445, 240, "Бесшовный роуминг",
                 "Устройство автоматически переключается между точками доступа без разрыва соединения.", "802.11r/k/v",
                 "p048_roam.jpg", "left:376px;top:72px;width:497px", 1, 340))
    o.append(box(455, 68, 885, 240, "MIMO",
                 "Несколько антенн передают несколько потоков данных одному устройству.", "Выше скорость и стабильность",
                 "p048_mimo.jpg", "left:386px;top:12px;width:508px", 2, 300))
    o.append(box(15, 248, 445, 405, "MU-MIMO",
                 "Точка доступа одновременно передаёт данные нескольким устройствам.", "Меньше ожидания для клиентов",
                 "p048_mumimo.jpg", "left:352px;top:-15px;width:542px", 3, 330))
    o.append(box(455, 248, 885, 405, "OFDMA",
                 "Канал делится на части, которые одновременно распределяются между клиентами.", "Эффективнее при высокой нагрузке",
                 "p048_ofdma.jpg", "left:292px;top:-11px;width:580px", 4, 281))

    def it(icn, key, txt, last=False):
        bd = "" if last else "border-right:2px solid var(--line);"
        return (f'<div style="flex:1;display:flex;gap:24px;align-items:center;padding:0 26px;{bd}">'
                f'<span style="color:#6f8fe0;width:84px;flex:none">{mi(icn, "")}</span>'
                f'<p class="b" style="font-size:23px;line-height:1.35"><b>{key}</b> — {txt}</p></div>')
    bar = ('<div style="display:flex;align-items:center;height:100%">'
           + it("layers3", "MIMO", "несколько потоков одному клиенту")
           + it("users", "MU-MIMO", "потоки нескольким клиентам")
           + it("pie", "OFDMA", "разделение канала между клиентами", True) + '</div>')
    o.append(card(T(15, 415, 885, 490), bar, 5, "card solid", pad="0 20px"))
    return "".join(o)


SLIDES.append(("p048", "Технологии Wi-Fi", p048()))


# ======================================================= p049 Основные характеристики коммутаторов
def p049():
    o = ['<h1 class="t ab ctr-x" style="top:36px;width:1700px;font-size:62px;line-height:1.1">Основные характеристики</h1>',
         '<h1 class="t ab ctr-x" style="top:118px;width:1700px;font-size:62px;line-height:1.1;color:#7f9ad8">коммутаторов</h1>']

    def c1(box, img, iw, ix, title, txt, s, extra="", dl=0, tsz=24):
        inner = (f'<img class="ab" src="assets/{img}" alt="" style="left:{ix}px;top:50%;transform:translateY(-50%);width:{iw}px;{feather(10)}">'
                 f'<div class="ab" style="left:{ix + iw + 18}px;right:14px;top:50%;transform:translateY(-50%)">'
                 f'{H(title, tsz)}<p class="b" style="font-size:20px;line-height:1.4;margin-top:10px">{txt}</p>{extra}</div>')
        return card(box, f'<div style="position:relative;height:100%">{inner}</div>', s, "card", dl, "0")

    r1 = [(18, 232, "p049_types.jpg", 150, 12, "Тип коммутатора", "Фиксированный &#8226; модульный &#8226; стекируемый.", ""),
          (240, 450, "p049_rack.jpg", 100, 14, "Монтажная единица", "1U (RU) = 4,445 см = 1,75 дюйма.", ""),
          (458, 660, "p049_ports.jpg", 150, 14, "Плотность портов", "Количество портов в 1U или стойке.",
           '<p class="b dim" style="font-size:16px;margin-top:8px;line-height:1.3">Учитываются абонентские порты, uplink и питание.</p>'),
          (668, 882, "p049_coins.jpg", 110, 14, "Стоимость порта", "Цена устройства ÷ количество портов.", "")]
    for i, (x0, x1, im, iw, ix, ti, tx, ex) in enumerate(r1):
        w = round((x1 - x0) * K)
        o.append(c1(T(x0, 103, x1, 208), im, iw, ix, ti, tx, 1, ex, dl=i * 110, tsz=22))
    r2 = [(18, 232, "p049_speed.jpg", 130, 12, "Скорость<br>пересылки", "Объём данных, обрабатываемых за секунду."),
          (240, 450, "p049_shield.jpg", 120, 10, "Надёжность", "Непрерывность доступа к сети."),
          (458, 660, "p049_poe.jpg", 130, 8, "PoE", "Питание оконечных устройств по кабелю передачи данных."),
          (668, 882, "p049_growth.jpg", 120, 12, "Масштабируемость", "Подключение новых пользователей через свободные порты.")]
    for i, (x0, x1, im, iw, ix, ti, tx) in enumerate(r2):
        o.append(c1(T(x0, 215, x1, 320), im, iw, ix, ti, tx, 2, "", dl=i * 110, tsz=22))
    o.append('<div class="ab ctr-x" data-s="3" style="top:706px;width:900px;text-align:center">'
             + H("Типы коммутаторов", 36, extra="letter-spacing:1px") + '</div>')
    r3 = [(68, 308, "p049_fixed.jpg", 360, "Фиксированный", "Тип и количество интерфейсов изменить нельзя."),
          (318, 578, "p049_modular.jpg", 380, "Модульный", "Порты добавляются платами расширения. Гибче, но дороже."),
          (586, 846, "p049_stack.jpg", 350, "Стекируемый", "Несколько устройств работают как одно логическое.")]
    for i, (x0, x1, im, iw, ti, tx) in enumerate(r3):
        w = round((x1 - x0) * K)
        inner = (f'<img class="ab" src="assets/{im}" alt="" style="left:{(w - iw) // 2}px;top:14px;width:{iw}px;{feather(10)}">'
                 f'<div class="ab" style="left:20px;right:20px;top:156px;text-align:center">{H(ti, 24)}'
                 f'<p class="b" style="font-size:18px;line-height:1.35;margin-top:6px">{tx}</p></div>')
        o.append(card(T(x0, 360, x1, 495), f'<div style="position:relative;height:100%">{inner}</div>', 4 + i, "card", pad="0"))
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
            'overflow:hidden;width:100%;table-layout:fixed">' + out + '</table>')


def p050():
    o = ['<h1 class="t ab ctr-x" style="top:22px;width:1700px;font-size:56px">Стекирование и плотность портов</h1>']
    ok = ('<span style="color:var(--blue);width:36px;flex:none"><svg viewBox="0 0 24 24" style="width:34px;height:34px;fill:none;'
          'stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round">' + LOC_CHECK + '</svg></span>')
    lst = "".join(f'<div style="display:flex;gap:10px;align-items:center;margin-bottom:22px">{ok}'
                  f'<span style="font-size:18px;line-height:1.25">{t}</span></div>'
                  for t in ["до 8 устройств в одном стеке", "больше доступных портов",
                            "единое логическое управление", "короткий путь между устройствами"])
    ar = ('<svg width="20" height="14" viewBox="0 0 20 14" style="vertical-align:middle;margin:0 4px">'
          '<path d="M1 7H17M11 2l6 5-6 5" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>')
    A = (H("Стекирование коммутаторов", 38, extra="line-height:1.1")
         + '<div class="ab" style="left:17px;top:82px;width:358px;text-align:center;font-size:22px;font-weight:800;color:var(--navy)">2 физических устройства</div>'
           '<img class="ab" src="assets/p050_sw1.jpg" alt="" style="left:17px;top:117px;width:358px">'
           '<img class="ab" src="assets/p050_sw2.jpg" alt="" style="left:17px;top:277px;width:358px">'
           '<div class="ab" style="left:30px;top:215px;width:340px;font-size:15px;color:var(--ink)">Коммутатор 1 (24 порта + 2 Uplink/SFP)</div>'
           '<div class="ab" style="left:398px;top:98px;width:220px;font-size:15px;line-height:1.3">Uplink 1 первого<br>'
         + ar + 'Uplink 2 второго</div>'
           '<div class="ab" style="left:421px;top:296px;width:220px;font-size:15px;line-height:1.3">Uplink 1 второго<br>'
         + ar + 'Uplink 2 первого</div>'
           '<svg class="ab" style="left:0;top:0;width:1207px;height:378px;overflow:visible" viewBox="0 0 1207 378">'
           '<path d="M372 180 C470 140 500 215 440 235 C400 248 390 255 376 270 M376 270 C420 262 470 258 440 235" '
           'stroke="#6a60e8" stroke-width="4" fill="none" stroke-linecap="round" opacity="0"/>'
           '<path d="M392 168 C486 140 506 220 440 252 C420 262 400 266 380 264" stroke="#6a60e8" stroke-width="4" fill="none" stroke-linecap="round"/>'
           '<path d="M392 160 L384 178 L404 178 Z" fill="#6a60e8"/>'
           '<path d="M372 264 L392 254 L394 274 Z" fill="#6a60e8"/>'
           '<path d="M520 236 L550 236" stroke="#3a6ce0" stroke-width="16"/>'
           '<path d="M548 212 L588 236 L548 260 Z" fill="#3a6ce0"/></svg>'
           '<div class="ab" style="left:586px;top:84px;width:400px;text-align:center;font-size:22px;font-weight:800;color:var(--navy);white-space:nowrap">1 логический коммутатор</div>'
           '<img class="ab" src="assets/p050_logical.jpg" alt="" style="left:586px;top:127px;width:400px;border-radius:18px">'
           f'<div class="ab" style="left:1002px;top:92px;width:205px">{lst}</div>')
    o.append(card(T(8, 52, 598, 250), f'<div style="position:relative;height:100%">{A}</div>', 1, "card", pad="22px 26px"))

    ul = ('<div class="chip" style="font-size:20px;padding:10px 18px;margin-top:16px;font-family:var(--f);font-weight:500;'
          'justify-content:center;gap:14px;width:100%">E1 <span style="color:var(--blue)">&#8226;</span> 10 Gigabit Ethernet '
          '<span style="color:var(--blue)">&#8226;</span> оптоволокно</div>')

    def mini(img, lab, val):
        return ('<div class="card solid" style="flex:1;display:flex;gap:12px;align-items:center;padding:10px 14px">'
                f'<img src="assets/{img}" alt="" style="width:70px;border-radius:10px"><div>'
                f'<div style="font-size:17px">{lab}</div><div class="mono" style="font-size:22px;font-weight:800;color:var(--blue);'
                f'white-space:nowrap">{val}</div></div></div>')
    minis = ('<div style="display:flex;gap:16px;margin-top:16px">' + mini("p050_ethport.jpg", "Ethernet-порт:", "100 Мбит/с")
             + mini("p050_uplink.jpg", "Uplink:", "1 Гбит/с") + '</div>')
    B = (H("Uplink-интерфейс", 34, extra="line-height:1.1;margin-bottom:12px")
         + '<p class="b" style="font-size:20px;line-height:1.4">Высокоскоростной интерфейс для подключения к вышестоящему '
           'коммутатору или маршрутизатору.</p>'
           '<p class="b" style="font-size:20px;line-height:1.4;margin-top:10px">Благодаря SFP-модулям может использовать разные '
           'типы соединений.</p>' + ul + minis)
    o.append(card(T(612, 52, 885, 250), B, 2, "card", pad="22px 26px"))

    o.append('<div class="ab" data-s="3" style="left:56px;top:550px">' + H("Два способа получить 48 портов", 42, extra="letter-spacing:.5px") + '</div>')

    left_rows = [("Место в стойке", "2 RU", ""), ("Розетки 220 В", "2", ""), ("Абонентские порты", "2 × 24 = 48", ""),
                 ("Суммарная скорость портов", "48 × 100 Мбит/с = 4,8 Гбит/с", ""), ("Условная стоимость", "300 единиц", ""),
                 ("Стоимость порта", "300 ÷ 48 = 6,25 единицы", "")]
    right_rows = [("Место в стойке", "1 RU", "−1 RU"), ("Розетки 220 В", "1", "−1 розетка"),
                  ("Абонентские порты", "1 × 48 = 48", ""), ("Суммарная скорость портов", "48 × 100 Мбит/с = 4,8 Гбит/с", ""),
                  ("Условная стоимость", "250 единиц", "−50 единиц"), ("Стоимость порта", "250 ÷ 48 = 5,21 единицы", "−1,04 за порт")]
    L = (H("2 × 24-портовых коммутатора", 27, extra="margin-bottom:10px")
         + '<img class="ab" src="assets/p050_24x2.jpg" alt="" style="left:6px;top:69px;width:297px">'
         + '<div style="margin-left:312px">' + _rows(left_rows, 16) + '</div>')
    o.append(card(T(18, 292, 440, 428), f'<div style="position:relative;height:100%">{L}</div>', 3, "card", pad="16px 22px"))
    R = (H("1 × 48-портовый коммутатор", 27, extra="margin-bottom:10px")
         + '<img class="ab" src="assets/p050_48.jpg" alt="" style="left:6px;top:133px;width:299px">'
         + '<div style="margin-left:312px">' + _rows(right_rows, 14) + '</div>')
    o.append(card(T(450, 292, 885, 428), f'<div style="position:relative;height:100%">{R}</div>', 4, "card", pad="16px 22px"))

    o.append(icard(T(15, 432, 408, 492), "layers3", "Плотность портов",
                   "Количество портов в ограниченном пространстве. Высокая плотность экономит место и энергоресурсы.",
                   5, "card", 25, 17, gap=18, pad="10px 20px"))
    o.append(icard(T(420, 432, 885, 492), "speed", "Скорость",
                   "Производительность коммутатора — объём данных, обрабатываемых за секунду.<br>"
                   "Скорости Ethernet-портов: 100 Мбит/с, 1, 10 и 100 Гбит/с",
                   5, "card", 25, 17, gap=18, pad="10px 20px", dl=120))
    return "".join(o)


SLIDES.append(("p050", "Стекирование и плотность портов", p050()))
