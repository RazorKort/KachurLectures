# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, arrow_svg, icon

SLIDES = []
SVG0 = '<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" viewBox="0 0 1920 1080">'
NAVY = "var(--navy)"


def ab(l, t, w=None, h=None, extra=""):
    s = f"position:absolute;left:{l}px;top:{t}px;"
    if w: s += f"width:{w}px;"
    if h: s += f"height:{h}px;"
    return s + extra


def ic(n):
    """Путь иконки из библиотеки (без обёртки svg)."""
    return icon(n)[len('<svg viewBox="0 0 24 24">'):-len('</svg>')]


def cico(p, cls=""):
    return f'<span class="ico {cls}"><svg viewBox="0 0 24 24">{p}</svg></span>'


def sv24(p, size=30):
    return (f'<svg viewBox="0 0 24 24" style="width:{size}px;height:{size}px;flex:none;fill:none;stroke:currentColor;'
            f'stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round">{p}</svg>')


TOWER = ('<path d="M12 11v10M8 21l4-10 4 10M7 6a7 7 0 0 0 0 7M17 6a7 7 0 0 1 0 7M9.5 8a3.5 3.5 0 0 0 0 3.5M14.5 8a3.5 3.5 0 0 1 0 3.5"/>'
         '<circle cx="12" cy="9.5" r="1"/>')
HOUSE = '<path d="M4 11l8-7 8 7M6 10v10h12V10M10 20v-6h4v6"/>'
SLIDERS = '<path d="M4 7h10M18 7h2M4 17h2M10 17h10M14 4v6M6 14v6"/>'
ENTER = '<path d="M19 5v8H6M10 9l-4 4 4 4"/>'
PEOPLE = '<circle cx="9" cy="8.5" r="3"/><circle cx="17" cy="9.5" r="2.4"/><path d="M3 20c0-3.3 2.7-5.5 6-5.5s6 2.2 6 5.5M16 14.8c3 0 5 1.8 5 5"/>'
DOC = '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/><path d="M10 12h6M10 16h6"/>'
WRENCH = '<path d="M15 7a4 4 0 0 1-5.3 5.3L5 17l2 2 4.7-4.7A4 4 0 0 0 17 9z"/>'
WARN = '<path d="M12 4l9 16H3z"/><path d="M12 10v5M12 17.6h.01"/>'


def waves(x, y, d=1, col="var(--blue)"):
    out = ""
    for i, r in enumerate((10, 20, 30)):
        out += (f'<path d="M{x + d * i * 14} {y - r} Q{x + d * (i * 14 + r)} {y} {x + d * i * 14} {y + r}" '
                f'stroke="{col}" stroke-width="4" fill="none" stroke-linecap="round"/>')
    return out


def line(s, d):
    return f'<path class="dr" data-s="{s}" pathLength="1" d="{d}" stroke="var(--blue)" stroke-width="3" fill="none"/>'


# ---------------------------------------------------------------- p035
def p035():
    o = ['<h1 class="t ab ctr-x" style="top:18px;width:1700px;font-size:58px">Устройства беспроводной сети</h1>']

    def dev(l, t, h, n, kind, model, img, ibox, pill, picn, desc, chips, s):
        x = [f'<div class="card" data-s="{s}" style="{ab(l, t, 920, h)}padding:0">',
             f'<span class="badge" style="{ab(34, 30)}width:62px;height:62px;font-size:32px;border-radius:50%">{n}</span>',
             f'<div style="{ab(122, 22)}font-size:24px;font-weight:700;color:{NAVY};text-transform:uppercase">{kind}</div>',
             f'<div class="mono" style="{ab(122, 52)}font-size:42px;font-weight:800;color:var(--blue)">{model}</div>']
        ix, iy, iw, ih = ibox
        x.append(f'<img src="assets/{img}" alt="{model}" style="{ab(ix, iy, iw, ih)}object-fit:contain">')
        x.append(f'<div style="{ab(520, 92)}display:flex;align-items:center;gap:12px">{cico(picn, "sm")}'
                 f'<span class="tag" style="font-size:20px;padding:8px 22px;border-radius:22px;background:rgba(150,185,250,.35)">{pill}</span></div>')
        x.append(f'<p class="b sm" style="{ab(520, 150, 385)}font-size:19px;line-height:1.2">{desc}</p>')
        cw = 287
        for i, (icn, tx) in enumerate(chips):
            x.append(f'<div style="{ab(20 + i * (cw + 10), h - 66, cw, 54)}display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.9);'
                     f'border:1.5px solid var(--line);border-radius:14px;padding:0 12px"><span style="color:var(--blue);display:flex">{sv24(icn)}</span>'
                     f'<span style="font-size:17px;font-weight:600;color:{NAVY};line-height:1.0">{tx}</span></div>')
        x.append('</div>')
        return "".join(x)

    o.append(dev(60, 88, 362, "01", "Контроллер беспроводного доступа", "WLC-3350", "dev/wlc-3350.webp", (30, 118, 470, 120),
                 "Управление сетью", ic("gear"),
                 "Управляет сотнями точек доступа, выполняет мониторинг, анализирует трафик и время сессий, задаёт индивидуальные настройки Wi-Fi.",
                 [(ic("net"), "Централизованное управление"), (ic("chart"), "Статистика"), (ic("reload"), "Бесшовный роуминг")], 1))
    o.append(dev(1000, 88, 362, "02", "Беспроводная точка доступа", "WEP-3L", "p035_wep3l2.png", (60, 106, 300, 160),
                 "Подключение клиентов", ic("wifi"),
                 "Подключает смартфоны, планшеты и другие беспроводные устройства к проводной сети.",
                 [(ic("wifi"), "Wi-Fi"), (PEOPLE, "Мобильные клиенты"), (ic("link"), "Проводная сеть")], 2))
    o.append(dev(60, 462, 362, "03", "Базовая станция БШПД", "WOP-3ax-LR6", "dev/wop-3ax-lr6.webp", (100, 108, 150, 175),
                 "Широкополосный доступ", TOWER,
                 "Организует беспроводную сеть широкополосного доступа и поддерживает сервисы Triple Play: интернет, телевидение и голос.",
                 [(ic("shield"), "Наружная установка"), (TOWER, "Секторные антенны"), (ic("sun"), "Разные климатические условия")], 3))
    o.append(dev(1000, 462, 362, "04", "Абонентская станция", "WB-2P-LR5", "dev/wb-2p-lr5.webp", (90, 108, 200, 175),
                 "Подключение абонента", TOWER,
                 "Принимает сигнал базовой станции и обеспечивает подключение удалённого абонента к сети.",
                 [(TOWER, "Направленная связь"), (HOUSE, "Удалённый объект"), (ic("speed"), "Широкополосный канал")], 4))

    o.append(f'<div class="card" data-s="5" style="{ab(60, 834, 1820, 236)}padding:0"></div>')
    o.append(f'<div data-s="5" style="{ab(90, 842)}font-size:26px;font-weight:800;color:{NAVY};text-transform:uppercase">Схема работы сети</div>')

    def lab(cx, t1, t2, s, w):
        return (f'<div data-s="{s}" style="{ab(cx - w // 2, 950, w)}text-align:center;font-size:16px;font-weight:700;color:{NAVY};text-transform:uppercase;line-height:1.25">'
                f'{t1}<br><span class="mono" style="color:var(--blue);font-size:18px">{t2}</span></div>')

    o.append(f'<img data-s="5" src="assets/dev/wlc-3350.webp" alt="WLC-3350" style="{ab(111, 890, 240)}">')
    o.append(f'<img data-s="6" src="assets/p035_wep3l2.png" alt="WEP-3L" style="{ab(464, 872, 130)}">')
    o.append(f'<img data-s="7" src="assets/p035_clients.jpg" alt="Клиенты" style="{ab(736, 870, 224)}">')
    o.append(f'<img data-s="8" src="assets/dev/wop-3ax-lr6.webp" alt="WOP-3ax-LR6" style="{ab(1170, 852, 60)}">')
    o.append(f'<img data-s="9" src="assets/dev/wb-2p-lr5.webp" alt="WB-2P-LR5" style="{ab(1505, 852, 66)}">')
    o += [lab(231, "Контроллер WLC", "WLC-3350", 5, 280), lab(530, "Точки доступа WAP", "WEP-3L", 6, 260),
          lab(848, "Клиенты", "&nbsp;", 7, 200), lab(1200, "Базовая станция БШПД", "WOP-3ax-LR6", 8, 280),
          lab(1546, "Абонентская станция", "WB-2P-LR5", 9, 260)]
    sv = [SVG0, line(6, "M352 905 L474 905"),
          f'<g data-s="6">{waves(612, 900, 1)}</g>',
          '<path data-s="8" d="M1035 850 L1035 990" stroke="rgba(110,150,220,.5)" stroke-width="2"/>',
          f'<g data-s="9">{waves(1300, 900, 1)}{waves(1450, 900, -1)}<path d="M1362 900H1388M1362 900l8-6M1362 900l8 6M1388 900l-8-6M1388 900l-8 6" stroke="var(--blue)" stroke-width="3" fill="none"/></g>',
          '</svg>']
    o.append("".join(sv))
    o.append(f'<div class="note" data-s="10" style="{ab(400, 1012, 1120, 50)}align-items:center;padding:0 20px;font-size:18px;gap:14px">'
             f'<span style="color:var(--blue);display:flex">{sv24(ic("info"))}</span>'
             f'Точки доступа с поддержкой LTE могут подключаться к сети оператора через активную SIM-карту.</div>')
    return "".join(o)


SLIDES.append(("p035", "Устройства беспроводной сети", p035()))


# ---------------------------------------------------------------- p036
def shield(kind, dark=False):
    c1, c2 = ("#cfe0ff", "#8fb4f5") if not dark else ("#a9c8ff", "#4f86ec")
    extra = ""
    if kind == 10:
        extra = ('<circle cx="128" cy="112" r="20" fill="#fff" stroke="#4a7ae0" stroke-width="3"/>'
                 '<circle cx="128" cy="112" r="7" fill="none" stroke="#4a7ae0" stroke-width="3"/>'
                 '<path d="M128 86v10M128 128v10M102 112h10M144 112h10M110 94l7 7M139 123l7 7M146 94l-7 7M117 123l-7 7" stroke="#4a7ae0" stroke-width="4"/>')
    if kind == 15:
        extra = '<path d="M98 138l6-24 12 12 12-18 12 18 12-12 6 24z" fill="#ffd36b" stroke="#fff" stroke-width="2"/>'
    return (f'<svg viewBox="0 0 180 200" style="width:200px;height:222px"><defs><linearGradient id="sg{kind}" x1="0" y1="0" x2="1" y2="1">'
            f'<stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>'
            f'<ellipse cx="90" cy="178" rx="70" ry="14" fill="rgba(255,255,255,.7)" stroke="#9db8ee"/>'
            f'<path d="M90 12l62 24v50c0 38-26 62-62 78-36-16-62-40-62-78V36z" fill="url(#sg{kind})" stroke="#fff" stroke-width="3"/>'
            f'<text x="50" y="108" font-family="var(--mono)" font-size="40" font-weight="800" fill="{"#fff" if dark else "#1d3d93"}">&gt;_</text>{extra}</svg>')


def p036():
    o = [f'<div class="ab" style="left:178px;top:50px;font-size:78px;font-weight:800;color:{NAVY};text-transform:uppercase;line-height:1.05;letter-spacing:.5px">Режимы командной строки</div>',
         '<div class="ab" style="left:180px;top:150px;font-size:60px;font-weight:800;color:#6f8fc9;text-transform:uppercase;line-height:1">Уровни привилегий</div>']
    sv = [SVG0,
          '<g data-s="1"><path class="dr" pathLength="1" d="M360 300 C700 300 1000 250 1410 170" stroke="var(--blue)" stroke-width="3" fill="none"/>'
          '<circle cx="363" cy="299" r="9" fill="#fff" stroke="var(--blue)" stroke-width="4"/><circle cx="950" cy="248" r="9" fill="#fff" stroke="var(--blue)" stroke-width="4"/>'
          '<circle cx="1420" cy="168" r="9" fill="#fff" stroke="var(--blue)" stroke-width="4"/></g>',
          arrow_svg(640, 455, 690, 475, 2, w=8), arrow_svg(1240, 395, 1290, 375, 3, w=8), '</svg>']

    def lvl(l, t, w, h, num, s, dark, body):
        bg = ("background:linear-gradient(135deg,#3f78e8,#1a3b9a);border-color:#8fb4ff;box-shadow:0 0 40px rgba(60,120,255,.45);" if dark else "")
        col = "#fff" if dark else NAVY
        return (f'<div class="card solid" data-s="{s}" style="{ab(l, t, w, h)}padding:0;border-radius:30px;{bg}">'
                f'<div style="{ab(36, 34)}font-size:36px;font-weight:800;color:{col};text-transform:uppercase;display:flex;align-items:baseline;gap:14px">'
                f'Уровень<span style="font-size:{86 if num != 1 else 80}px;line-height:.9;color:{"#fff" if dark else "var(--blue)"}">{num}</span></div>{body}</div>')

    def pill(t, l, tp, w, dark=False):
        return (f'<div style="{ab(l, tp, w, 50)}border-radius:25px;display:grid;place-items:center;font-size:21px;font-weight:600;'
                f'background:{"rgba(255,255,255,.25)" if dark else "rgba(150,185,250,.4)"};color:{"#fff" if dark else NAVY}">{t}</div>')

    sc = lambda k, d=False, z=.8, l=10, t=110: (f'<div style="{ab(l, t, 200)}transform:scale({z});transform-origin:left top">{shield(k, d)}</div>')
    b1 = (sc(1) + f'<div style="{ab(190, 140, 340)}"><div style="font-size:32px;font-weight:800;color:{NAVY}">Мониторинг</div>'
          f'<p class="b" style="margin-top:8px;font-size:23px;color:{NAVY}">Доступен только мониторинг устройства</p></div>'
          + pill("Минимальные права", 54, 320, 440))
    o.append(lvl(81, 316, 553, 400, 1, 1, False, b1))
    b10 = (sc(10, l=10, t=100) + f'<div style="{ab(190, 120, 340)}"><div style="font-size:32px;font-weight:800;color:{NAVY}">Конфигурирование</div>'
           f'<p class="b" style="margin-top:6px;font-size:22px;color:{NAVY}">Доступна настройка устройства</p></div>'
           f'<div style="{ab(24, 280, 500)}background:rgba(255,255,255,.7);border:1.5px solid var(--line);border-radius:16px;padding:12px 18px;font-size:19px;line-height:1.35;color:{NAVY}">'
           f'<b>Недоступно:</b><ul style="margin:4px 0 0 20px"><li>создание пользователей</li><li>перезагрузка устройства</li><li>загрузка программного обеспечения</li></ul></div>')
    o.append(lvl(683, 252, 554, 463, 10, 2, False, b10))
    b15 = (sc(15, True, .85) + f'<div style="{ab(220, 130, 300)}"><div style="font-size:34px;font-weight:800;color:#fff">Полный доступ</div>'
           f'<p class="b" style="margin-top:8px;font-size:22px;color:#fff">Нет ограничений</p></div>' + pill("Максимальные права", 80, 400, 380, True))
    o.append(lvl(1283, 192, 520, 500, 15, 3, True, b15))
    o.append("".join(sv))

    o.append(f'<div class="card" data-s="4" style="{ab(64, 736, 1790, 320)}padding:0;border-radius:30px"></div>')
    o.append(f'<div data-s="4" style="{ab(96, 770)}font-size:42px;font-weight:800;color:{NAVY};text-transform:uppercase">Переход между уровнями</div>')

    def tr(l, up, title, cmd, s):
        d = "M35 4L4 42h20v54h22V42h20z" if up else "M35 96L4 58h20V4h22v54h20z"
        return (f'<div data-s="{s}" style="{ab(0, 0)}">'
                f'<div class="card solid" style="{ab(l - 30, 836, 840, 175)}padding:0;border-radius:20px"></div>'
                f'<svg style="{ab(l, 880, 70, 100)}" viewBox="0 0 70 100"><path d="{d}" fill="var(--blue)"/></svg>'
                f'<div style="{ab(l + 90, 848, 700)}white-space:nowrap;font-size:26px;font-weight:700;color:{NAVY}">{title}</div>'
                f'<div class="mono" style="{ab(l + 90, 892, 610)}background:#16254f;color:#eaf2ff;border-radius:14px;padding:14px 26px;font-size:27px;line-height:1.35">{cmd}</div></div>')

    o.append(tr(126, True, "Получение 15-го уровня", "esr&gt; enable<br>esr#", 4))
    o.append(tr(1028, False, "Возвращение на первоначальный уровень", "esr# disable<br>esr&gt;", 5))
    return "".join(o)


SLIDES.append(("p036", "Режимы командной строки: уровни привилегий", p036()))


# ---------------------------------------------------------------- p037
def p037():
    o = [f'<img class="ab" src="assets/p037_rack.jpg" alt="Стойка с сетевым оборудованием" style="{ab(120, 110, 440)}border-radius:6px;box-shadow:var(--sh)">',
         f'<img class="ab" data-s="1" src="assets/p037_stack.jpg" alt="Коммутаторы и маршрутизаторы Eltex" '
         f'style="{ab(720, 280, 900)}-webkit-mask-image:radial-gradient(ellipse 72% 72% at 50% 50%,#000 62%,transparent 100%);mask-image:radial-gradient(ellipse 72% 72% at 50% 50%,#000 62%,transparent 100%)">',
         f'<div class="ab" style="left:790px;top:70px;font-size:78px;font-weight:800;line-height:1.05;text-transform:uppercase;color:{NAVY}">Сетевое<br><span style="color:#5b73b8">оборудование</span></div>']
    for i, (n, t) in enumerate([("net", "Коммутаторы"), ("router", "Маршрутизаторы"), ("server", "Сетевые устройства")]):
        o.append(f'<div data-s="{2 + i}" style="{ab(1560, 150 + i * 100, 330)}display:flex;align-items:center;gap:18px">'
                 f'<span class="ico" style="background:#5a73c0;color:#fff;border-radius:50%;border:none">'
                 f'<svg viewBox="0 0 24 24">{ic(n)}</svg></span>'
                 f'<span style="font-size:18px;font-weight:700;color:#5b73b8;letter-spacing:1px;text-transform:uppercase">{t}</span></div>')
    return "".join(o)


SLIDES.append(("p037", "Сетевое оборудование", p037()))


# ---------------------------------------------------------------- p038
def p038():
    o = [f'<div class="ab" style="left:75px;top:30px"><div class="big" style="font-size:90px">ESR-3300</div>'
         f'<div class="kick" style="margin-top:4px;font-size:34px;color:#7fa0e0">Передняя панель</div></div>',
         f'<img class="cut ab" src="assets/p038_front.jpg" alt="ESR-3300, передняя панель" style="{ab(107, 462, 1700)}">']

    def card(l, t, w, h, n, title, img, iw, ih, txt, s, fs=17, ty=78):
        return (f'<div class="card solid" data-s="{s}" style="{ab(l, t, w, h)}padding:0;border-radius:20px">'
                f'<span class="badge" style="{ab(14, 14)}">{n}</span>'
                f'<div style="{ab(76, 20)}font-size:26px;font-weight:800;color:{NAVY}">{title}</div>'
                f'<img src="assets/{img}" alt="{title}" style="{ab(18, 90, iw, ih)}object-fit:contain">'
                f'<p class="b sm" style="{ab(iw + 36, ty, w - iw - 54)}font-size:{fs}px;line-height:1.4">{txt}</p></div>')

    o.append(card(107, 213, 490, 182, 1, "2.5GE [1 ... 4]", "p038_sfp.jpg", 130, 122, '4 порта <span class="mono">1000BASE-X/10GBASE-R/25GBASE-R</span>.', 1))
    o.append(card(618, 213, 470, 182, 2, "40/100GE [1 ... 4]", "p038_qsfp.jpg", 170, 50, '4 порта Ethernet <span class="mono">40GBASE-R (QSFP+)/100GBASE-R (QSFP28)</span>.', 2))
    o.append(card(1109, 213, 331, 182, 3, "USB", "p038_usb.jpg", 76, 100, "Порт USB 3.0 для подключения USB-устройств.", 3))
    o.append(card(1461, 213, 341, 182, 4, "microSD", "p038_microsd.jpg", 100, 52, "Разъем для установки microSD-карт памяти.", 4))
    o.append(card(85, 725, 360, 260, 5, "Console", "p038_rj45.jpg", 110, 80, "Консольный порт RS-232 (RJ-45) для локального управления устройством.", 5, 16, 74))
    o.append(card(459, 725, 384, 260, 6, "OOB", "p038_oob.jpg", 100, 80, "Ethernet-интерфейс для удаленного доступа и управления, в том числе для резервного доступа через вторичный загрузчик U-Boot.", 6, 16, 74))
    o.append(f'<div class="card solid" data-s="7" style="{ab(853, 725, 469, 325)}padding:0;border-radius:20px">'
             f'<span class="badge" style="{ab(14, 14)}">7</span><div class="mono" style="{ab(76, 18)}font-size:30px;font-weight:800;color:{NAVY}">F</div>'
             f'<img src="assets/p038_fbtn.jpg" alt="Кнопка F" style="{ab(24, 100, 90, 70)}object-fit:contain">'
             f'<p class="b sm" style="{ab(130, 74, 320)}font-size:16px;line-height:1.4">Функциональная кнопка для перезагрузки устройства и сброса к заводским настройкам:<br>'
             f'удержание менее 10 секунд — перезагрузка устройства;<br>удержание более 10 секунд — перезагрузка и сброс к заводским настройкам.</p></div>')
    rows = [("Status", "текущее состояние устройства."), ("Alarm", "наличие и уровень аварии."), ("User", "пользовательские сценарии."),
            ("Flash", "активность обмена с microSD/USB Flash."), ("Power", "питание устройства."), ("Master", "работа в failover-режимах."),
            ("Fan", "состояние вентиляторов."), ("RPS", "резервный источник питания.")]
    li = "".join(f'<div style="display:flex;gap:10px;align-items:center;font-size:17px;line-height:1.55"><i style="width:14px;height:14px;border-radius:50%;background:#3f5f9f;flex:none"></i>'
                 f'<b style="width:68px;color:{NAVY}">{a}</b><span>— {b}</span></div>' for a, b in rows)
    o.append(f'<div class="card solid" data-s="8" style="{ab(1344, 735, 520, 320)}padding:0;border-radius:20px">'
             f'<span class="badge" style="{ab(14, 14)}">8</span><div style="{ab(76, 20)}font-size:26px;font-weight:800;color:{NAVY}">Индикаторы состояния</div>'
             f'<div style="{ab(24, 78, 480)}">{li}</div></div>')
    o.append("".join([SVG0, line(1, "M640 395 V440 M575 480 V445 H706 V480"), line(2, "M885 395 V530"),
                      line(3, "M1169 395 V430 H1078 V560"), line(4, "M1290 395 V450 H1169 V600"),
                      line(5, "M265 725 V700 H1250 V676"), line(6, "M650 725 V712 H1268 V676"),
                      line(7, "M1088 725 V690 H1327 V676"), line(8, "M1514 735 V676"), '</svg>']))
    return "".join(o)


SLIDES.append(("p038", "ESR-3300: передняя панель", p038()))


# ---------------------------------------------------------------- p039 / p041
def err_slide(title, cols, steps_title, note):
    o = [f'<h1 class="t ab ctr-x" style="top:30px;width:1800px;font-size:60px">{title}</h1>']
    themes = [("rgba(255,243,225,.8)", "#f0a83a"), ("rgba(253,236,244,.8)", "#e8809f"), ("rgba(232,244,255,.85)", "#6ec0f2")]
    mids = [DOC, ic("gear"), SLIDERS]
    wcols = ["linear-gradient(135deg,#ffcf6a,#f08a12)", "linear-gradient(135deg,#ff7a95,#d6264f)", "linear-gradient(135deg,#ff7a95,#d6264f)"]
    for i, (hd, sub, cause, ex, fix) in enumerate(cols):
        bg, bd = themes[i]
        l = 36 + i * 622
        box = (f'border:1.5px solid var(--line);border-radius:16px;background:rgba(255,255,255,.75);display:flex;gap:16px;align-items:center;padding:0 18px')
        o.append(
            f'<div class="card" data-s="{i + 1}" style="{ab(l, 154, 604, 640)}padding:0;border-radius:28px;background:{bg};border:2px solid {bd}">'
            f'<div style="{ab(26, 30, 110, 110)}border-radius:50%;background:{wcols[i]};display:grid;place-items:center;box-shadow:0 8px 22px rgba(0,0,0,.18)">'
            f'<svg viewBox="0 0 24 24" style="width:66px;height:66px;fill:none;stroke:#fff;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round">{WARN}</svg></div>'
            f'<div style="{ab(160, 44, 440)}white-space:nowrap;letter-spacing:-.5px;font-size:31px;font-weight:800;color:{NAVY};text-transform:uppercase;line-height:1">{hd}</div>'
            f'<div style="{ab(160, 90, 440)}white-space:nowrap;font-size:25px;font-weight:700;color:#7a90c4">{sub}</div>'
            f'<div style="{ab(18, 162, 568, 128)}{box}">{cico(mids[i])}<div><div style="font-size:24px;font-weight:800;color:{NAVY}">Причина:</div>'
            f'<p class="b sm" style="font-size:20px;line-height:1.3">{cause}</p></div></div>'
            f'<div style="{ab(18, 306)}font-size:23px;font-weight:800;color:{NAVY}">Пример в командной строке:</div>'
            f'<div class="mono" style="{ab(18, 346, 568, 124)}background:#16254f;color:#eaf2ff;border-radius:14px;padding:14px 20px;font-size:21px;line-height:1.35;white-space:pre">{ex}</div>'
            f'<div style="{ab(18, 486, 568, 138)}{box}">{cico(WRENCH)}<div><div style="font-size:24px;font-weight:800;color:{NAVY}">Что исправить:</div>'
            f'<p class="b sm" style="font-size:20px;line-height:1.3">{fix}</p></div></div></div>')
    o.append(f'<div class="card" data-s="4" style="{ab(36, 812, 1848, 250)}padding:0;border-radius:28px"></div>')
    o.append(f'<div data-s="4" style="{ab(96, 830)}font-size:40px;font-weight:800;color:{NAVY};text-transform:uppercase">{steps_title}</div>')
    icons = [(DOC, "Ввод команды"), (ENTER, "Нажатие Enter"), ('<circle cx="11" cy="11" r="6"/><path d="M15.5 15.5L20 20"/>', "Анализ слева направо"),
             (ic("gear"), "Проверка синтаксиса"), (ic("check"), "Выполнение или сообщение об ошибке")]
    xs = [239, 608, 960, 1295, 1660]
    for k, ((p, tx), cx) in enumerate(zip(icons, xs)):
        o.append(f'<div data-s="5" style="--dl:{k * 140}ms;{ab(cx - 130, 880, 260)}text-align:center">'
                 f'<div style="display:inline-block">{cico(p, "hex")}</div>'
                 f'<div style="font-size:21px;font-weight:600;color:{NAVY};margin-top:8px;line-height:1.15"><b>{k + 1}.</b> {tx}</div></div>')
    sv = [SVG0] + [f'<g data-s="5" style="--dl:{k * 140 + 100}ms"><path d="M{a} 918H{a + 60}M{a + 50} 910l10 8-10 8" stroke="var(--blue)" stroke-width="3" fill="none"/></g>'
                   for k, a in enumerate([365, 722, 1090, 1430])] + ['</svg>']
    o.append("".join(sv))
    o.append(f'<div class="note" data-s="6" style="{ab(380, 1008, 1160, 50)}align-items:center;padding:0 20px;font-size:19px;gap:14px">'
             f'<span style="color:var(--blue);display:flex">{sv24(ic("info"))}</span>{note}</div>')
    return "".join(o)


SLIDES.append(("p039", "Проверка синтаксиса команд MES", err_slide(
    "Проверка синтаксиса команд MES",
    [("Incomplete command", "Незаконченная команда", "Введены не все ключевые слова или параметры.", "console#\nconsole#set\n% Incomplete command.",
      "После команды set необходимо указать ключевое слово, например date, и требуемые параметры."),
     ("Ambiguous command", "Неоднозначная команда", "Команда не может быть однозначно распознана.", "console#\nconsole#d\n% Ambiguous Command",
      "Буквы d недостаточно: с неё начинается несколько доступных команд. Введите больше букв для однозначного выбора."),
     ("Invalid input detected", "Обнаружен недопустимый ввод", "В одном из параметров команды допущена ошибка.",
      "console#\nconsole#set cli prompt ops\n                          ^\n% Invalid input detected at '^' marker.",
      "Символ ^ указывает место ошибки. Вместо ops необходимо использовать параметр on или off.")],
    "Как проверяется команда", "Если команда распознана, она выполняется, затем командная строка ожидает следующий ввод.")))


# ---------------------------------------------------------------- p040
def p040():
    o = [f'<div class="ab" style="left:75px;top:24px"><div class="big" style="font-size:92px">ESR-200</div>'
         f'<div class="kick" style="margin-top:2px;font-size:28px;color:#7fa0e0;letter-spacing:4px">Передняя панель</div></div>',
         f'<img class="cut ab" src="assets/p040_front.jpg" alt="ESR-200, передняя панель" style="{ab(107, 469, 1699)}">']

    def card(l, t, w, h, n, title, s, inner):
        return (f'<div class="card solid" data-s="{s}" style="{ab(l, t, w, h)}padding:0;border-radius:20px">'
                f'<span class="badge" style="{ab(14, 14)}">{n}</span>'
                f'<div style="{ab(74, 18)}white-space:nowrap;font-size:23px;font-weight:800;color:{NAVY}">{title}</div>{inner}</div>')

    t = lambda l, tp, w, x: f'<div class="b sm" style="{ab(l, tp, w)}font-size:17px;line-height:1.38">{x}</div>'
    img = lambda f, l, tp, w, h: f'<img src="assets/{f}" alt="" style="{ab(l, tp, w, h)}object-fit:contain">'
    o.append(card(60, 188, 458, 277, 1, "Слот для SD-карты", 1,
                  img("p040_sd.jpg", 16, 76, 90, 122) + t(120, 68, 326, "Имеется у всех, кроме младших моделей (ESR-10/12V/12VF/14VF). Может хранить образ системы, файлы журнала, файлы настройки, резервные копии конфигурации и любые другие файлы, необходимые для работы системы.")))
    o.append(card(644, 181, 486, 256, 3, "Сетевые интерфейсы", 3,
                  img("p040_rj45.jpg", 18, 90, 130, 80) + t(166, 68, 308, "Медные и комбинированные. Комбинированный интерфейс может использоваться как для медных соединений, так и для оптоволоконных, но только с использованием модулей SFP/SFP+/QSFP/QSFP+.")))
    pts = "".join(f'<div style="display:flex;gap:10px;align-items:center;margin-bottom:12px"><i style="width:18px;height:18px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#6c8be0,#1a2f7a)"></i><b style="font-size:18px;color:{NAVY}">{x}</b></div>'
                  for x in ["Power", "Status", "Alarm", "Fan"])
    o.append(card(1158, 181, 538, 235, 4, "Индикаторы состояния", 4,
                  f'<div style="{ab(26, 74)}">{pts}</div>' + t(190, 70, 330, "Отображают состояние:<ul style='margin:4px 0 0 18px'><li>электропитание;</li><li>текущее состояние устройства;</li><li>наличие и уровень аварии устройства;</li><li>состояние вентиляторов.</li></ul>")))
    o.append(card(273, 757, 350, 235, 2, "USB-разъёмы", 2,
                  img("p040_usbs.jpg", 18, 80, 90, 84) + t(120, 70, 220, "Два USB-разъёма для подключения flash-карт и 3G/4G модемов.")))
    o.append(card(710, 736, 427, 314, 5, "Функциональная кнопка F", 5,
                  img("p040_fbtn.jpg", 16, 84, 78, 46) + t(106, 66, 306, "Используется для перезагрузки устройства и сброса к заводским настройкам:<br>удержание менее 10 секунд — перезагрузка устройства;<br>удержание более 10 секунд — перезагрузка и сброс к заводским настройкам.")))
    o.append(card(1163, 764, 362, 228, 6, "Консольный интерфейс", 6,
                  img("p040_console.jpg", 16, 84, 100, 66) + t(130, 76, 218, "Используется для локального управления устройством.")))
    o.append(card(1551, 757, 309, 224, 7, "Разъём питания", 7,
                  img("p040_plug.jpg", 14, 84, 80, 74) + t(106, 74, 190, "Для подключения к источнику электропитания переменного тока.")))
    o.append("".join([SVG0, line(1, "M213 465 V640"), line(2, "M437 757 V700"), line(3, "M680 437 V460 H1070 V437 M885 437 V470"),
                      line(4, "M1237 416 V570"), line(5, "M1286 736 V640"), line(6, "M1387 764 V690"), line(7, "M1685 757 V660"), '</svg>']))
    return "".join(o)


SLIDES.append(("p040", "ESR-200: передняя панель", p040()))

SLIDES.append(("p041", "Ошибки в командной строке ESR", err_slide(
    "Ошибки в командной строке ESR",
    [("Incompleted command", "Незаконченная команда", "Введены не все ключевые слова или параметры.", "esr# set\nSyntax error: Incompleted command",
      "Дополнить команду: set date и указать необходимые параметры."),
     ("Unknown command", "Неизвестная команда", "Командная строка не распознала введённую команду.", "esr# s\nSyntax error: Unknown command",
      "Проверить написание и ввести полное имя команды."),
     ("Illegal parameter", "Недопустимый параметр", "Введено значение, которое команда не может принять.", "esr# set date 22:44:33 15 1\nSyntax error: Illegal parameter",
      "Вместо 1 указать название месяца, например January.")],
    "Как обрабатывается команда", "Если команда распознана, она выполняется, затем командная строка ожидает следующий ввод ESR.")))


# ---------------------------------------------------------------- p042
def p042():
    fade = ("-webkit-mask-image:linear-gradient(to right,transparent,#000 18%,#000 82%,transparent);"
            "mask-image:linear-gradient(to right,transparent,#000 18%,#000 82%,transparent)")
    o = [f'<img class="ab" src="assets/p042_land.jpg" alt="" style="{ab(1060, 230, 300, 760)}object-fit:cover;{fade}">',
         f'<img class="ab" data-s="1" src="assets/dev/wop-2ac-lr5.webp" alt="WOP-2ac-LR5 SYNC" style="{ab(1330, 56, 324, 832)}object-fit:contain">',
         f'<div class="ab" style="left:75px;top:56px;font-size:88px;font-weight:800;color:{NAVY};line-height:1;letter-spacing:-1px">WOP-2ac-LR5 SYNC</div>',
         '<div class="ab" style="left:78px;top:158px;font-size:48px;font-weight:800;color:#6f8fc9;text-transform:uppercase;letter-spacing:1px">Базовая станция БШПД</div>']
    cells = ["5 ГГц · IEEE 802.11a/n/ac", "До 867 Мбит/с", "MIMO 2×2", "До 30 клиентов", "Мощность до 28 дБм", "От −45 до +65 °C"]
    for i, tx in enumerate(cells):
        l = 64 if i % 2 == 0 else 509
        w = 421 if i % 2 == 0 else 389
        o.append(f'<div class="card solid" data-s="{i + 2}" style="{ab(l, 285 + (i // 2) * 119, w, 101)}padding:0 14px;display:flex;align-items:center;gap:18px;border-radius:18px">'
                 f'<img src="assets/p042_i{i + 1}.png" alt="" style="width:86px;height:89px;flex:none;mix-blend-mode:multiply">'
                 f'<span style="white-space:nowrap;font-size:24px;font-weight:700;color:{NAVY};text-transform:uppercase;line-height:1.1">{tx}</span></div>')
    o.append(f'<div class="card solid" data-s="8" style="{ab(64, 649, 834, 155)}padding:0 22px;display:flex;align-items:center;gap:22px;border-radius:20px">'
             f'<img src="assets/p042_i7.png" alt="" style="width:180px;height:137px;flex:none;mix-blend-mode:multiply">'
             f'<div style="border-left:2px solid var(--line);padding-left:24px"><div style="font-size:30px;font-weight:800;color:{NAVY};text-transform:uppercase">Межсекторная синхронизация</div>'
             f'<div style="font-size:21px;color:var(--dim);text-transform:uppercase;margin-top:8px;line-height:1.25">Эффективная работа при ограниченном<br>частотном ресурсе</div></div></div>')
    for k, (f, lab, l, w) in enumerate([("p042_house2.jpg", "Частная застройка", 51, 302), ("p042_tower2.jpg", "Удалённые объекты", 408, 317),
                                        ("p042_tv2.jpg", "Triple Play", 763, 314)]):
        o.append(f'<div class="ab" data-s="{9 + k}" style="{ab(l, 823, w)}text-align:center"><img src="assets/{f}" alt="{lab}" '
                 f'style="width:{w}px;height:{round(w * 151 / 262 if k < 2 else w * 134 / 273)}px;display:block;mix-blend-mode:multiply;object-fit:cover">'
                 f'<div style="font-size:21px;font-weight:600;color:{NAVY};text-transform:uppercase;margin-top:12px">{lab}</div></div>')
    return "".join(o)


SLIDES.append(("p042", "WOP-2ac-LR5 SYNC: базовая станция БШПД", p042()))
SLIDES.sort(key=lambda x: x[0])
