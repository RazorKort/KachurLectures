# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, arrow_svg, icon

SLIDES = []   # (ref, label, html)
K = 1920 / 900.0
SVG0 = '<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" viewBox="0 0 1920 1080">'
SVG_OPEN = '<svg viewBox="0 0 24 24">'


def inner_icon(name):
    return icon(name)[len(SVG_OPEN):-len('</svg>')]


def r(v):
    return round(v * K)


def P(l, t, w=None, h=None, ex=""):
    """Стиль из координат миниатюры (900 px) -> холст 1920."""
    s = f"position:absolute;left:{r(l)}px;top:{r(t)}px;"
    if w is not None: s += f"width:{r(w)}px;"
    if h is not None: s += f"height:{r(h)}px;"
    return s + ex


def A(l, t, w=None, h=None, ex=""):
    s = f"position:absolute;left:{l}px;top:{t}px;"
    if w is not None: s += f"width:{w}px;"
    if h is not None: s += f"height:{h}px;"
    return s + ex


def title(txt, top=34, size=64):
    return f'<h1 class="t ab ctr-x" style="top:{top}px;width:1700px;font-size:{size}px">{txt}</h1>'


def circ(svg_inner, size=92):
    return (f'<span style="display:grid;place-items:center;width:{size}px;height:{size}px;border-radius:50%;flex:none;'
            f'background:radial-gradient(circle at 35% 30%,#6ea8ff,#2a6bf2 60%,#1d4fd8);box-shadow:0 8px 20px rgba(42,107,242,.35);'
            f'border:3px solid rgba(255,255,255,.85)"><svg viewBox="0 0 24 24" style="width:{size*0.5:.0f}px;height:{size*0.5:.0f}px;'
            f'fill:none;stroke:#fff;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round">{svg_inner}</svg></span>')


MASK = '-webkit-mask-image:radial-gradient(ellipse 72% 72% at 50% 50%,#000 78%,transparent 100%);mask-image:radial-gradient(ellipse 72% 72% at 50% 50%,#000 78%,transparent 100%);'
ARR = ('<svg viewBox="0 0 24 12" style="width:30px;height:15px;vertical-align:middle;margin:0 4px">'
       '<path d="M1 6h20M16 1l5 5-5 5" fill="none" stroke="#2a6bf2" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def term(lines, fs=18):
    dots = "".join(f'<i style="width:15px;height:15px;border-radius:50%;background:{c};display:block"></i>'
                   for c in ("#ff5f57", "#febc2e", "#28c840"))
    return (f'<div style="background:#0f1a3a;border-radius:16px;overflow:hidden;box-shadow:0 10px 26px rgba(15,26,58,.35);width:100%;height:100%">'
            f'<div style="display:flex;gap:9px;padding:14px 20px">{dots}</div>'
            f'<pre class="mono" style="color:#eaf0ff;font-size:{fs}px;line-height:27px;padding:2px 20px;margin:0;white-space:pre;font-weight:500">{lines}</pre></div>')


# =====================================================================
# p019  Контекстная подсказка
# =====================================================================
def s019():
    o = [title("Контекстная подсказка", 30)]
    o.append(f'<div class="card solid" data-s="1" style="{A(508, 132, 879, 107)}display:flex;align-items:center;gap:26px;padding:0 30px">'
             f'<span class="ico" style="width:84px;height:84px"><span style="font-size:58px;font-weight:800;color:var(--navy)">?</span></span>'
             f'<div><div style="font-size:31px;font-weight:700;color:var(--navy)">Введите <span style="color:var(--blue);font-weight:800">?</span> в любом месте командной строки</div>'
             f'<div style="font-size:23px;color:var(--dim);margin-top:4px">Символ ? не отображается, нажимать Enter не требуется</div></div></div>')

    def pad(rows, c1):
        return "\n".join(a.ljust(c1) + b for a, b in rows)

    t1 = ("console# ?\n\n" + pad([("backup", "Backup the configurations"), ("boot", "Boot command"),
          ("cd", "Changes current working directory"), ("clear", "Clear configuration"),
          ("clock", "Manages the system clock"), ("configure", "Configures the terminal")], 11))
    t2 = ("console# d?\n\n" + pad([("debug", "Configures trace for Loopback detection"), ("delete", "Delete command"),
          ("dir", "Prints information about directory"), ("disable", "Disables a feature"),
          ("dot1x", "Configures PNAC related information"), ("dump", "Display memory content")], 9))
    t3 = ("console# show interfaces ?\n\n" + pad([("<CR>", "Displays interface status and"), ("", "configuration."),
          ("Fastethernet", "Fast Ethernet interface"), ("Gigabitethernet", "Gigabit ethernet interface"),
          ("advertisement", "Options advertised"), ("capabilities", "Capabilities of the interface"),
          ("combo", "Interfaces combo mode"), ("counters", "Counter related information")], 17))
    t1, t2, t3 = [x.replace("<", "&lt;").replace(">", "&gt;") for x in (t1, t2, t3)]
    cards = [(32, "01", "До начала<br>набора команды", t1, 19, "Показывает команды, доступные в текущем режиме.", 2),
             (658, "02", "После начала<br>набора команды", t2, 18, "Ищет команды по введённой первой букве.", 3),
             (1277, "03", "Просмотр<br>ключей команды", t3, 16, "Показывает доступные ключи и параметры незавершённой команды.", 4)]
    for l, n, ttl, tx, fs, desc, s in cards:
        o.append(f'<div class="card solid" data-s="{s}" style="{A(l, 267, 608, 646)}padding:0">'
                 f'<span class="mono" style="{A(26, 38, 92, 92)}display:grid;place-items:center;border-radius:50%;color:#fff;font-size:40px;font-weight:800;'
                 f'background:radial-gradient(circle at 35% 30%,#6ea8ff,#2a6bf2 60%,#1d4fd8);border:3px solid #fff;box-shadow:0 8px 20px rgba(42,107,242,.35)">{n}</span>'
                 f'<div style="{A(132, 44, 350)}font-size:29px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.15">{ttl}</div>'
                 f'<div style="{A(486, 36)}">{ico("term")}</div>'
                 f'<div style="{A(24, 172, 560, 326)}">{term(tx, fs)}</div>'
                 f'<div class="card" style="{A(24, 516, 560, 104)}padding:0 26px;display:flex;align-items:center;background:rgba(255,255,255,.7)">'
                 f'<p class="b" style="font-size:23px">{desc}</p></div></div>')
    o.append(f'<div class="card solid" data-s="5" style="{A(181, 934, 1558, 115)}display:flex;align-items:center;gap:30px;padding:0 40px">'
             f'{ico("doc")}<span style="width:2px;height:60px;background:var(--line)"></span>'
             f'<p class="b" style="font-size:27px">Контекстная подсказка показывает список команд и параметров, доступных в текущем режиме.</p></div>')
    return "".join(o)


SLIDES.append(("p019", "Контекстная подсказка", s019()))


# =====================================================================
# p020  Режимы командной строки
# =====================================================================
def s020():
    o = [f'<div class="ab" style="{A(43, 40)}font-size:57px;font-weight:800;line-height:1.1;text-transform:uppercase;color:var(--navy)">'
         f'Режимы<br><span style="color:#5a70b8">Командной<br>строки</span></div>',
         f'<p class="b" style="{A(43, 270, 450)}font-size:25px;line-height:1.4;color:var(--navy)">Иерархия режимов CLI<br>на маршрутизаторах ESR</p>']

    def step(top, h, n, ttl, chips, desc, s):
        chip_html = "".join(f'<span class="chip mono" style="font-size:{27 if len(chips)==1 else 19}px;padding:8px 18px">{c}</span>' for c in chips)
        return (f'<div class="card solid" data-s="{s}" style="{A(508, top, 868, h)}padding:0">'
                f'<span class="mono" style="{A(34, 20, 74, 74)}display:grid;place-items:center;border-radius:50%;color:#fff;font-size:30px;font-weight:800;'
                f'background:radial-gradient(circle at 35% 30%,#6ea8ff,#2a6bf2 60%,#1d4fd8);border:3px solid #fff">{n}</span>'
                f'<div style="{A(140, 22)}font-size:32px;font-weight:800;color:var(--navy);text-transform:uppercase">{ttl}</div>'
                f'<div style="{A(140 if len(chips)==1 else 34, 72 if len(chips)==1 else 104)}display:flex;gap:{16 if len(chips)==1 else 14}px;white-space:nowrap">{chip_html}</div>'
                f'<div style="{A(140, h - 56 if len(chips)==1 else h - 38)}font-size:18px;color:var(--dim);white-space:nowrap">{desc}</div></div>')

    o += [step(96, 177, "01", "Пользовательский режим", ["esr&gt;"], "Непривилегированный доступ &bull; только базовые операции &bull; доступно 15 команд", 1),
          step(316, 190, "02", "Привилегированный режим", ["esr#"], "Диагностика и переход к глобальному конфигурированию", 2),
          step(526, 190, "03", "Глобальное конфигурирование", ["esr(config)#"], "Основной режим настройки устройства", 3),
          step(752, 205, "04", "Конфигурирование функционала", ["esr(config-user)#", "esr(config-gre)#", "esr(config-line-ssh)#"],
               "Пользователь &bull; GRE-туннель &bull; линия SSH", 4)]
    o.append(SVG0 + arrow_svg(941, 282, 941, 312, 2) + arrow_svg(941, 508, 941, 522, 3) + arrow_svg(941, 718, 941, 748, 4) + '</svg>')
    rows = [("user", "Логин: <b>admin</b>"), ("lock", "Пароль: <b>password</b>"), ("shield", "Уровень привилегий: <b>15</b>"),
            ("gear", "Пользователя нельзя удалить, но можно настроить")]
    rh = [82, 82, 82, 98]
    ry = [150, 246, 342, 438]
    inner = "".join(
        f'<div class="card solid" data-s="5" style="{A(24, ry[i], 415, rh[i])}--dl:{i*120}ms;padding:0 18px;display:flex;align-items:center;gap:16px;border-radius:18px">'
        f'{ico(n, "sm")}<span style="font-size:{26 if i < 3 else 20}px;color:var(--navy);line-height:1.3">{t}</span></div>'
        for i, (n, t) in enumerate(rows))
    o.append(f'<div class="card" data-s="5" style="{A(1425, 209, 463, 548)}padding:0">'
             f'<div style="{A(30, 26, 400)}font-size:34px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.2">Учётная запись<br>по умолчанию</div>{inner}</div>')
    o.append(f'<div class="note" data-s="6" style="{A(508, 998, 875, 51)}align-items:center;padding:0 22px;font-size:19px;border-radius:14px;gap:10px">'
             f'<span style="color:var(--blue);font-weight:800">i</span> Символ &gt; — непривилегированный режим &nbsp;&bull;&nbsp; Символ # — привилегированный режим</div>')
    return "".join(o)


SLIDES.append(("p020", "Режимы командной строки", s020()))


# =====================================================================
# p021  Коммутаторы агрегации
# =====================================================================
def s021():
    o = [title("Коммутаторы агрегации", 30)]
    feats = [("layers", "L2 и L3", 172), ("server", "Стек до 8 устройств", 310), ("bolt", "Резервирование<br>питания", 440),
             ("wifi", "Front-to-back", 575), ("speed", "1G &bull; 10G &bull; 40G", 740)]
    for i, (ic, t, cx) in enumerate(feats):
        o.append(f'<div data-s="1" style="--dl:{i*90}ms;{A(r(cx) - 150, 150, 300)}text-align:center">'
                 f'<div style="display:flex;justify-content:center">{ico(ic, "hex")}</div>'
                 f'<div style="margin-top:14px;font-size:22px;font-weight:700;color:var(--navy);text-transform:uppercase;line-height:1.25">{t}</div></div>')
    o.append('<div data-s="1" style="' + A(0, 0) + '">' + "".join(
        f'<div style="{A(r(x), 160, 2, 120)}background:var(--line)"></div>' for x in (237, 378, 513, 668)) + '</div>')
    ratio = {"p021_mes3400.jpg": 114 / 448, "p021_mes3300.jpg": 118 / 406, "p021_mes3324.jpg": 118 / 441}
    cards = [(32, 625, "MES3400-48F", "p021_mes3400.jpg", 587, 2,
              [("speed", "48 &times; SFP<br>1G / 10G"), ("gear", "Высокая плотность портов"), ("net", "Для магистральных и агрегационных сегментов")]),
             (666, 594, "MES3300-08F", "p021_mes3300.jpg", 540, 3,
              [("speed", "8 &times; SFP+<br>10G"), ("gear", "Компактное решение"), ("net", "Гибкое развёртывание")]),
             (1269, 619, "MES3324", "p021_mes3324.jpg", 570, 4,
              [("speed", "24 &times; 1G<br>4 &times; 10G"), ("gear", "Универсальная агрегация"), ("net", "Оптимальное соотношение возможностей")])]
    for l, w, name, img, iw, s, fs in cards:
        ih = round(iw * ratio[img])
        top = 40 + (196 - ih) // 2
        items = "".join(f'<div style="display:flex;gap:8px;align-items:center;flex:1;min-width:0">{ico(ic, "sm")}'
                        f'<span style="font-size:15px;line-height:1.2;color:var(--navy)">{t}</span></div>' for ic, t in fs)
        o.append(f'<div class="card" data-s="{s}" style="{A(l, 348, w, 389)}padding:0">'
                 f'<img class="cut ab" src="assets/{img}" alt="{name}" style="{A((w - iw)//2, top, iw)}">'
                 f'<div style="{A(0, 250, w)}text-align:center;font-size:40px;font-weight:700;color:var(--navy);letter-spacing:1px">{name}</div>'
                 f'<div style="{A(16, 306, w - 32)}display:flex;gap:6px">{items}</div></div>')
    o.append(SVG0 + ''.join(
        f'<path class="dr" data-s="5" pathLength="1" d="M{x} 737 L{x} 775 L960 775 L960 843" stroke="rgba(110,150,220,.6)" stroke-width="3" fill="none"/>'
        for x in (344, 963, 1578)) + '</svg>')
    o.append(f'<div data-s="5" style="{A(875, 843, 170, 170)}border-radius:50%;background:radial-gradient(circle at 40% 35%,#fff,#bcd4ff 55%,#8fb4f5);'
             f'box-shadow:0 0 50px rgba(110,168,255,.7),inset 0 0 30px rgba(255,255,255,.8)"></div>')

    def agg(l, ic, ttl, txt, s):
        return (f'<div class="card solid" data-s="{s}" style="{A(l, 821, 555, 224)}display:flex;align-items:center;gap:26px;padding:0 34px">'
                f'{ico(ic, "hex")}<div><div style="font-size:30px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.1">{ttl}</div>'
                f'<p class="b" style="margin-top:10px;font-size:22px">{txt}</p></div></div>')
    o += [agg(224, "stack", "Агрегация 1G", "Доступ и агрегация на скорости 1 Гбит/с", 6),
          agg(1163, "server", "Агрегация 10G / 40G", "Высокая пропускная способность для магистральных соединений", 7)]

    def chev(x):
        return (f'<svg data-s="6" class="ab" style="{A(x, 905, 70, 40)}" viewBox="0 0 70 40"><path d="M6 6l14 14-14 14M30 6l14 14-14 14M54 6l14 14-14 14" '
                f'fill="none" stroke="#6ea8ff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    o += [chev(790), chev(1075)]
    return "".join(o)


SLIDES.append(("p021", "Коммутаторы агрегации", s021()))


# =====================================================================
# p022  Обзор беспроводного оборудования
# =====================================================================
def s022():
    o = [title('Обзор <span class="lt">беспроводного</span> оборудования', 30, 62),
         '<p class="ab ctr-x" style="top:122px;width:1700px;text-align:center;font-size:25px;color:var(--navy)">'
         'Беспроводные технологии расширяют возможности проводной сети и имеют преимущества и недостатки.</p>']
    pros = [("phone", "Мобильный доступ", "Быстрое подключение стационарных и мобильных устройств"),
            ("chart", "Масштабируемость", "Простое добавление пользователей и расширение зоны покрытия"),
            ("expand", "Гибкость", "Подключение в разных местах и в удобное время"),
            ("db", "Сокращение затрат", "Меньше кабелей и оборудования по сравнению с проводной сетью"),
            ("gear", "Быстрая установка", "Одно устройство обеспечивает подключение многих пользователей"),
            ("sun", "Работа в сложных условиях", "Удобное развёртывание в экстренной или неблагоприятной среде")]
    rows = "".join(
        f'<div class="card solid" data-s="2" style="{A(16, 108 + i*101, 516, 92)}--dl:{i*110}ms;padding:0 16px;display:flex;align-items:center;gap:16px;border-radius:16px">'
        f'{ico(ic, "sm")}<div><div style="font-size:22px;font-weight:800;color:var(--navy);text-transform:uppercase">{t}</div>'
        f'<div style="font-size:17px;color:var(--dim);line-height:1.25;margin-top:2px">{d}</div></div></div>'
        for i, (ic, t, d) in enumerate(pros))
    o.append(f'<div class="card" data-s="2" style="{A(17, 181, 548, 725)}padding:0">'
             f'<div style="{A(26, 24)}font-size:40px;font-weight:800;color:var(--navy);text-transform:uppercase">Преимущества</div>{rows}</div>')
    cons = [("bolt", "Помехи", "Сигнал зависит от электромагнитных шумов и других устройств"),
            ("lock", "Безопасность", "Требуются дополнительная защита, шифрование и контроль доступа"),
            ("speed", "Скорость и стабильность", "Радиоканал может уступать проводной сети по скорости и надёжности")]
    rows = "".join(
        f'<div class="card solid" data-s="3" style="{A(16, 104 + i*190, 459, 176)}--dl:{i*150}ms;padding:0 18px;display:flex;align-items:center;gap:18px;border-radius:18px">'
        f'{ico(ic, "hex")}<div><div style="font-size:24px;font-weight:800;color:var(--navy);text-transform:uppercase">{t}</div>'
        f'<div style="font-size:19px;color:var(--dim);line-height:1.3;margin-top:6px">{d}</div></div></div>'
        for i, (ic, t, d) in enumerate(cons))
    o.append(f'<div class="card" data-s="3" style="{A(1408, 181, 491, 683)}padding:0">'
             f'<div style="{A(26, 24)}font-size:40px;font-weight:800;color:var(--navy);text-transform:uppercase">Недостатки</div>{rows}</div>')
    o.append(f'<img class="cut ab" data-s="1" src="assets/p022_wifi_scene.jpg" alt="Wi-Fi: точка доступа и устройства" style="{A(560, 170, 830, None, MASK)}">')

    def bot(l, w, ic, ttl, sub, s):
        return (f'<div class="card solid" data-s="{s}" style="{A(l, 928, w, 122)}display:flex;align-items:center;gap:24px;padding:0 30px">'
                f'{ico(ic, "hex")}<div><div style="font-size:34px;font-weight:800;color:var(--navy);text-transform:uppercase">{ttl}</div>'
                f'<div style="font-size:20px;color:var(--dim);margin-top:4px">{sub}</div></div></div>')
    o += [bot(288, 661, "wifi", "Беспроводная сеть", "Мобильность &bull; гибкость &bull; быстрое развёртывание", 4),
          bot(1035, 629, "cable", "Проводная сеть", "Высокая скорость &bull; стабильность &bull; предсказуемость", 4)]
    o.append(f'<svg data-s="4" class="ab" style="{A(962, 968, 66, 36)}" viewBox="0 0 66 36"><path d="M6 18h54M18 8L6 18l12 10M48 8l12 10-12 10" fill="none" stroke="#7a8fc0" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    return "".join(o)


SLIDES.append(("p022", "Обзор беспроводного оборудования", s022()))


# =====================================================================
# p023  Монтаж в стойку
# =====================================================================
def s023():
    # слайд целиком — исходный визуал из pptx, без пересборки блоками
    return ('<img class="ab" src="assets/p023_full.jpg" alt="Монтаж в стойку" '
            'style="position:absolute;left:0;top:0;width:1920px;height:1080px;object-fit:cover">')


SLIDES.append(("p023", "Монтаж в стойку", s023()))


# =====================================================================
# p024  Команды IP ADDRESS
# =====================================================================
PUR, BLU, GRN, NAVY = "#6b2fb3", "#1f88d9", "#1f9d5b", "#12245e"
PILL = {"cmd": ("#e6dbfb", "#5a2fa8"), "par": ("#d3e8fb", "#1f6fb8"), "kw": ("#d6f3e3", "#1b7a4a")}


def tok(x, y, txt, col):
    return f'<div class="mono" style="{A(r(x), r(y) - 34)}font-size:44px;font-weight:800;color:{col};line-height:68px;white-space:nowrap">{txt}</div>'


def pill(x0, x1, y0, y1, txt, kind, fs=20):
    bg, fg = PILL[kind]
    return (f'<div style="{P(x0, y0, x1 - x0, y1 - y0)}background:{bg};color:{fg};border-radius:12px;display:flex;align-items:center;justify-content:center;'
            f'text-align:center;font-size:{fs}px;font-weight:600;line-height:1.15">{txt}</div>')


def grp(step, inner, arrows=""):
    return (f'<div data-s="{step}" style="{A(0, 0, 1920, 1080)}">{inner}'
            + (SVG0 + arrows + '</svg>' if arrows else '') + '</div>')


def s024():
    o = [title('Команды <span class="lt">IP address</span>', 28, 64)]
    o.append(f'<div class="card" style="{P(18, 72, 864, 146)}padding:0"></div>')
    o.append(f'<div class="card" style="{P(18, 225, 864, 135)}padding:0"></div>')

    def strip(y):
        return f'<div style="{P(30, y, 840, 34)}background:rgba(255,255,255,.9);border-radius:12px"></div>'
    t1 = (f'<div style="{P(38, 78)}font-size:32px;font-weight:800;color:var(--navy);text-transform:uppercase">Настройка <span style="color:var(--blue)">IP-адреса</span></div>'
          + strip(99)
          + tok(112, 115, "ip address", PUR) + tok(258, 115, "&lt;ADDR/LEN&gt;", BLU) + tok(402, 115, "[", NAVY)
          + tok(430, 115, "secondary", GRN) + tok(548, 115, "]", NAVY) + tok(588, 115, "[", NAVY)
          + tok(617, 115, "unit", GRN) + tok(683, 115, "&lt;ID&gt;", BLU) + tok(748, 115, "]", NAVY))
    ar1 = (arrow_svg(r(175), r(131), r(175), r(154), None, PUR) + arrow_svg(r(318), r(131), r(318), r(154), None, BLU)
           + arrow_svg(r(473), r(131), r(473), r(154), None, GRN) + arrow_svg(r(633), r(131), r(633), r(154), None, GRN)
           + arrow_svg(r(711), r(131), r(711), r(154), None, BLU)
           + f'<path class="dr" pathLength="1" d="M{r(406)} {r(134)} L{r(406)} {r(191)} L{r(585)} {r(191)} L{r(585)} {r(134)}" stroke="#2a6bf2" stroke-width="3" fill="none"/>')
    labs1 = (pill(118, 198, 156, 184, "Команда", "cmd") + pill(258, 378, 156, 188, "Обязательный<br>параметр", "par")
             + pill(432, 516, 156, 186, "Ключевое<br>слово", "kw") + pill(593, 650, 156, 186, "Ключевое<br>слово", "kw")
             + pill(678, 745, 156, 184, "Параметр", "par") + pill(490, 675, 199, 216, "Необязательные элементы", "par", 17))
    o += [grp(1, t1, ar1), grp(2, labs1)]
    t2 = (f'<div style="{P(38, 232)}font-size:32px;font-weight:800;color:var(--navy);text-transform:uppercase">Удаление <span style="color:var(--blue)">IP-адреса</span></div>'
          + strip(254)
          + tok(113, 270, "no ip address", PUR) + tok(316, 270, "{", NAVY) + tok(342, 270, "&lt;ADDR/LEN&gt;", BLU)
          + tok(472, 270, "[", NAVY) + tok(497, 270, "unit", GRN) + tok(562, 270, "&lt;ID&gt;", BLU) + tok(625, 270, "]", NAVY)
          + tok(648, 270, "|", NAVY) + tok(690, 270, "all", GRN) + tok(748, 270, "}", NAVY))
    ar2 = (arrow_svg(r(215), r(286), r(215), r(307), None, PUR) + arrow_svg(r(397), r(286), r(397), r(307), None, BLU)
           + arrow_svg(r(513), r(286), r(513), r(307), None, GRN) + arrow_svg(r(590), r(286), r(590), r(307), None, BLU)
           + arrow_svg(r(708), r(286), r(708), r(307), None, GRN)
           + f'<path class="dr" pathLength="1" d="M{r(318)} {r(290)} L{r(318)} {r(340)} L{r(748)} {r(340)} L{r(748)} {r(290)}" stroke="#2a6bf2" stroke-width="3" fill="none"/>')
    labs2 = (pill(165, 268, 309, 328, "Команда", "cmd") + pill(342, 452, 309, 328, "Параметр", "par")
             + pill(476, 548, 303, 331, "Ключевое<br>слово", "kw", 18) + pill(557, 622, 309, 328, "Параметр", "par")
             + pill(668, 748, 303, 331, "Ключевое<br>слово", "kw", 18) + pill(415, 650, 343, 359, "Обязательный выбор одного варианта", "par", 17))
    o += [grp(3, t2, ar2), grp(4, labs2)]
    o.append(f'<div data-s="5" style="{P(30, 369, 330, 24)}font-size:30px;font-weight:800;color:var(--navy);text-transform:uppercase;white-space:nowrap">Параметры и ключевые слова</div>')
    o.append(f'<div data-s="5" style="{P(332, 380, 540, 1.5)}background:var(--blue)"></div>')
    cards = [(20, 223, "doc", "&lt;ADDR/LEN&gt;", BLU, "IP-адрес и длина маски подсети<br>Формат: AAA.BBB.CCC.DDD/EE<br>AAA&ndash;DDD: [0..255]<br>EE: [1..32]"),
             (247, 201, "list", "&lt;ID&gt;", BLU, "Номер юнита<br>Допустимые значения: [1..4]"),
             (452, 211, "gear", "secondary", GRN, "Указывает, что адрес является дополнительным. Без secondary адрес считается основным. Допускается до 7 дополнительных IP-адресов."),
             (667, 218, "layers", "all", GRN, "Удаляет все IP-адреса на интерфейсе.")]
    for i, (x, w, ic, nm, col, tx) in enumerate(cards):
        o.append(f'<div class="card solid" data-s="5" style="{P(x, 392, w, 98)}--dl:{i*120}ms;padding:0 14px;display:flex;gap:14px;align-items:center">'
                 f'{ico(ic, "sm")}<div><div class="mono" style="font-size:25px;font-weight:800;color:{col}">{nm}</div>'
                 f'<div style="font-size:15px;line-height:1.3;color:var(--navy);margin-top:4px">{tx}</div></div></div>')
    return "".join(o)


SLIDES.append(("p024", "Команды IP address", s024()))


# =====================================================================
# p025  Функционал коммутаторов MES
# =====================================================================
def s025():
    o = [title('Функционал коммутаторов <span class="lt">MES</span>', 26, 54),
         '<p class="ab ctr-x" style="top:90px;width:1700px;text-align:center;font-size:24px;color:var(--dim)">Набор функций зависит от модели и версии прошивки.</p>']
    steps = [("globe", "eltex-co.ru"), ("stack", f"Каталог{ARR}Ethernet-коммутаторы MES"),
             ("switch", "Выбрать нужную модель"), ("doc", f"Документы и файлы{ARR}Руководство пользователя / Руководство по эксплуатации")]
    ys = [112, 218, 330, 430]
    hs = [90, 100, 92, 112]
    inner = "".join(
        f'<div data-s="1" style="--dl:{i*120}ms;{A(24, ys[i], 347, hs[i])}display:flex;align-items:center;gap:16px;background:rgba(255,255,255,.6);border-radius:16px;padding:0 16px">'
        f'<span class="badge" style="border-radius:50%;width:44px;height:44px">{i+1}</span>{ico(ic, "sm")}'
        f'<span style="font-size:{22 if i == 0 else 17}px;color:var(--navy);line-height:1.3;{"font-family:var(--mono);" if i == 0 else ""}">{t}</span></div>'
        for i, (ic, t) in enumerate(steps))
    o.append(f'<div class="card" data-s="1" style="{A(11, 139, 395, 548)}padding:0">'
             f'<div style="{A(26, 14)}font-size:26px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.2">Где посмотреть<br>функции модели</div>{inner}</div>')
    cols = [("net", "Интерфейсы и L2", [("Функции интерфейсов", 42), ("Работа с MAC-адресами", 42), ("VLAN", 42), ("L2 Multicast", 42), ("Функции L2", 42), ("Link Aggregation", 42)], 437, 241, 2),
            ("globe", "L3 и IPv6", [("Функции L3", 66), ("L3 Multicast", 66), ("Поддержка IPv6", 66)], 687, 222, 3),
            ("shield", "Безопасность и трафик", [("Функции безопасности", 66), ("ACL &mdash; списки управления доступом", 66), ("QoS и ограничение скорости", 66)], 917, 233, 4),
            ("gear", "Управление", [("Сервисные функции", 66), ("Основные функции управления", 66)], 1158, 206, 5)]
    o.append(f'<div class="card" data-s="2" style="{A(416, 139, 971, 548)}padding:0"><div style="{A(26, 14)}font-size:30px;font-weight:800;color:var(--navy);text-transform:uppercase">Группы функций</div></div>')
    for ic, ttl, its, x, w, s in cols:
        items = "".join(f'<div style="background:rgba(255,255,255,.75);border-radius:12px;height:{h}px;display:flex;align-items:center;padding:0 12px;'
                        f'font-size:17px;line-height:1.25;color:var(--navy);margin-bottom:6px">{t}</div>' for t, h in its)
        o.append(f'<div class="card solid" data-s="{s}" style="{A(x, 215, w, 455)}padding:12px;border-radius:18px">'
                 f'<div style="display:flex;justify-content:center">{ico(ic, "hex")}</div>'
                 f'<div style="text-align:center;font-size:20px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.15;margin:8px 0 14px;height:48px;display:flex;align-items:center;justify-content:center">{ttl}</div>'
                 f'{items}</div>')
    tiles = [("speed", "Пропускная способность", 0, 0, 2), ("arrows", "Неблокируемая матрица", 1, 0, 2),
             ("layers", "Уровень:<br>L2 или L3", 0, 1, 2), ("switch", "Количество и скорость портов", 1, 1, 2),
             ("stack", "Стекирование", 0, 2, 3), ("bolt", "PoE", 1, 2, 3), ("reload", "Резервирование и горячая замена", 2, 2, 3)]
    tl = ""
    for i, (ic, t, c, rw, n) in enumerate(tiles):
        w = 218 if n == 2 else 140
        x = 24 + c * (w + 15)
        tl += (f'<div class="card solid" style="{A(x, 100 + rw*144, w, 130)}--dl:{i*80}ms;padding:8px;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:8px;border-radius:16px;text-align:center" data-s="6">'
               f'<span style="color:var(--blue);display:block"><svg viewBox="0 0 24 24" style="width:40px;height:40px;fill:none;stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round">{inner_icon(ic)}</svg></span>'
               f'<span style="font-size:{18 if n == 2 else 15}px;color:var(--navy);line-height:1.2">{t}</span></div>')
    o.append(f'<div class="card" data-s="6" style="{A(1408, 139, 491, 548)}padding:0">'
             f'<div style="{A(26, 14, 440)}font-size:26px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.2">Ключевые характеристики модели</div>{tl}</div>')
    o.append(f'<div class="ab" data-s="7" style="{A(32, 722)}font-size:34px;font-weight:800;color:var(--navy);text-transform:uppercase">Неблокируемая матрица</div>')
    o.append(f'<img class="cut ab" data-s="7" src="assets/p025_matrix.jpg" alt="Матрица: Ethernet-порты, коммутационная матрица, Uplink-порты" style="{A(58, 783, 1171)}">')
    o.append(f'<div class="ab" data-s="7" style="{A(58, 930, 480)}text-align:center;font-size:23px;color:var(--navy)"><b>Ethernet-порты</b><br>(пользовательские)</div>')
    o.append(f'<div class="ab" data-s="7" style="{A(900, 930, 450)}text-align:center;font-size:23px;color:var(--navy)"><b>Uplink-порты</b><br>(аплинки)</div>')
    o.append(f'<div class="card solid" data-s="8" style="{A(1286, 736, 598, 320)}padding:26px 34px">'
             f'<div style="font-size:35px;font-weight:800;color:var(--navy);line-height:1.3"><span style="color:var(--blue)">&sum;</span> скоростей Ethernet-портов<br>'
             f'<span style="color:var(--blue)">&le;</span> <span style="color:var(--blue)">&sum;</span> скоростей Uplink-портов</div>'
             f'<p class="b" style="margin-top:22px;font-size:25px;color:var(--dim)">Трафик со всех Ethernet-интерфейсов может быть передан через Uplink без внутренней блокировки.</p></div>')
    return "".join(o)


SLIDES.append(("p025", "Функционал коммутаторов MES", s025()))


# =====================================================================
# p026  Системные индикаторы
# =====================================================================
LED = {"off": ("#d5d9e3", "#7f8697", "rgba(120,130,150,0)"), "grn": ("#9cf27a", "#17a52a", "rgba(40,200,60,.45)"),
       "red": ("#ff9a9a", "#d01c1c", "rgba(240,50,50,.45)")}


def led(kind, ring=False):
    a, b, g = LED[kind]
    rg = "0 0 0 7px rgba(60,200,80,.22),0 0 0 14px rgba(60,200,80,.10)," if ring else ""
    return (f'<span style="flex:none;width:50px;height:50px;border-radius:50%;background:radial-gradient(circle at 35% 30%,{a},{b});'
            f'border:3px solid #fff;box-shadow:{rg}0 0 18px {g},0 4px 8px rgba(0,0,0,.2)"></span>')


def ledrow(kind, ttl, txt, top, h, w, s, dl, ring=False):
    return (f'<div class="card solid" data-s="{s}" style="{A(20, top, w, h)}--dl:{dl}ms;padding:0 18px;display:flex;align-items:center;gap:18px;border-radius:16px">'
            f'{led(kind, ring)}<div><div style="font-size:24px;font-weight:800;color:var(--navy)">{ttl}</div>'
            f'<div style="font-size:20px;color:var(--dim);line-height:1.25">{txt}</div></div></div>')


def lcard(l, t, w, h, icon_svg, name, sub, rows, s):
    inner = ""
    for i, row in enumerate(rows):
        k, tt, tx, rt, rh = row[:5]
        ring = len(row) > 5 and row[5]
        inner += ledrow(k, tt, tx, rt, rh, w - 40, s, 120 * (i + 1), ring)
    return (f'<div class="card" data-s="{s}" style="{A(l, t, w, h)}padding:0">'
            f'<div style="{A(22, 18)}display:flex;align-items:center;gap:20px">{circ(icon_svg, 88)}'
            f'<div><div style="font-size:40px;font-weight:800;color:#1f4fb8;line-height:1">{name}</div>'
            f'<div style="font-size:18px;color:var(--dim);margin-top:6px;line-height:1.2">{sub}</div></div></div>{inner}</div>')


def s026():
    o = [f'<div class="ab" style="{A(60, 36)}font-size:84px;font-weight:800;line-height:1.08;text-transform:uppercase;color:var(--navy)">'
         f'Системные<br><span style="color:#4d6fc4">индикаторы</span></div>',
         f'<div class="ab" style="{A(60, 232, 130, 3)}background:linear-gradient(90deg,var(--blue),transparent)"></div>',
         f'<p class="b ab" style="{A(60, 266, 520)}font-size:26px;line-height:1.45;color:var(--navy)">Системные индикаторы отражают текущее состояние устройства. '
         f'Зелёный цвет означает штатную работу, красный &mdash; неисправность, требующую внимания администратора.</p>',
         f'<img class="cut ab" src="assets/p026_device.jpg" alt="Коммутатор MES" style="{A(0, 778, 533)}">']
    o.append(f'<div class="card rose" data-s="6" style="{A(60, 505, 452, 170)}display:flex;align-items:center;gap:18px;padding:0 22px;border-color:#f3a3b8">'
             f'<span style="color:#e23b4f;flex:none"><svg viewBox="0 0 24 24" style="width:64px;height:64px;fill:rgba(226,59,79,.15);stroke:currentColor;stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round"><path d="M12 4l9 16H3z"/><path d="M12 10v5M12 17.6h.01"/></svg></span>'
             f'<p class="b" style="font-size:21px;line-height:1.35">Если индикаторы <b>Alarm</b> и <b>PoE</b> одновременно горят красным, это сигнализирует о критической ошибке PoE.</p></div>')
    bell = '<path d="M6 17V11a6 6 0 0 1 12 0v6l1.5 2h-15z"/><path d="M10 21h4"/>'
    batt = '<rect x="3" y="8" width="16" height="9" rx="2"/><path d="M21 11v3M6 11v3M9.5 11v3M13 11v3"/>'
    pw = '<path d="M12 4v8"/><path d="M7.5 7a7 7 0 1 0 9 0"/>'
    portsvg = '<rect x="3" y="6" width="18" height="12" rx="2"/><path d="M7 10v3M10 10v3M13 10v3M16 10v3"/>'
    lay = '<path d="M12 4l8 4-8 4-8-4z"/><path d="M4 12l8 4 8-4"/><path d="M4 16l8 4 8-4"/>'
    o.append(lcard(725, 64, 548, 456, pw, "Power", "Электропитание",
                   [("off", "Выключен", "Питание выключено.", 130, 98), ("grn", "Зелёный горит", "Питание включено, нормальная работа.", 236, 102),
                    ("grn", "Зелёный мерцает", "Самотестирование при включении питания (POST).", 346, 102, True)], 1))
    o.append(lcard(1301, 64, 567, 456, bell, "Alarm", "Наличие и уровень аварии устройства",
                   [("off", "Не горит", "Нормальная работа устройства.", 140, 112), ("red", "Красный", "Перегрев.", 262, 112)], 2))
    o.append(lcard(544, 538, 437, 454, portsvg, "PoE", "Состояние PoE-портов",
                   [("off", "Выключен", "Потребитель PoE не подключен.", 140, 90), ("grn", "Зелёный", "Подключен потребитель PoE.", 240, 90),
                    ("red", "Красный", "Ошибка PoE на порту.", 340, 90)], 3))
    o.append(lcard(998, 538, 420, 454, lay, "Master", "Признак ведущего устройства при работе в стеке",
                   [("off", "Выключен", "Устройство не является «мастером» в стеке или не задан режим стекирования.", 150, 150),
                    ("grn", "Зелёный", "Устройство является «мастером» в стеке.", 312, 108)], 4))
    o.append(lcard(1444, 538, 429, 454, batt, "Battery", "Индикатор состояния аккумуляторной батареи.",
                   [("off", "Выключен", "АКБ отключена.", 150, 90), ("grn", "Зелёный", "АКБ подключена.", 250, 90),
                    ("red", "Красный", "Низкий уровень заряда АКБ.", 350, 90)], 5))
    return "".join(o)


SLIDES.append(("p026", "Системные индикаторы", s026()))
