# -*- coding: utf-8 -*-
"""Слайды по референсам p019–p026 (pptx 62, 20, 41, 65, 15, 26, 44, 17).
Координаты — в системе картинки-оригинала, приведённой к 1497x842 (как в _el2cmp), S = 1920/1497.
CROPS — вырезки из оригинала pptx (иконки, фото, иллюстрации); текст — живой HTML."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, arrow_svg

SLIDES = []   # (ref, label, html)
CROPS = []
S = 1920 / 1497
NV = "#1b2a6b"          # тёмно-синий текста оригинала
LB = "#6c84d4"          # светло-синий второго слова заголовков
BL = "#3a6fd8"          # синий акцент
WIDE = "font-family:var(--f);font-weight:800;"
COND = "font-family:var(--fh);font-weight:700;"
SVG0 = '<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" viewBox="0 0 1920 1080">'


def q(v):
    return round(v * S)


def B(x0, y0, x1=None, y1=None, ex=""):
    s = f"position:absolute;left:{q(x0)}px;top:{q(y0)}px;"
    if x1 is not None: s += f"width:{q(x1) - q(x0)}px;"
    if y1 is not None: s += f"height:{q(y1) - q(y0)}px;"
    return s + ex


def cut(n, name, x0, y0, x1, y1, mode="f", ds=None, ex="", alt="", nat=False):
    """вырезка из слайда pptx n, ставится ровно на то же место (nat — без растяжения по высоте)"""
    CROPS.append((n, name, x0, y0, x1, y1, mode))
    st = f' data-s="{ds}"' if ds else ""
    return f'<img class="ab"{st} src="assets/{name}" alt="{alt}" style="{B(x0, y0, x1, None if nat else y1)}{ex}">'


def G(ds, *parts, dl=0):
    return (f'<div data-s="{ds}" style="position:absolute;left:0;top:0;width:1920px;height:1080px;--dl:{dl}ms">'
            + "".join(parts) + '</div>')


def box(x0, y0, x1, y1, ex=""):
    return f'<div class="card" style="{B(x0, y0, x1, y1)}padding:0;border-radius:22px;{ex}"></div>'


def tx(x0, y0, html, fs, ex="", x1=None):
    return f'<div style="{B(x0, y0, x1)}font-size:{fs}px;line-height:1.2;color:{NV};{ex}">{html}</div>'


def hd(x0, y0, html, fs, ex="", x1=None):
    """заголовок широким жирным шрифтом, как в оригинале"""
    return tx(x0, y0, html, fs, f"{WIDE}text-transform:uppercase;line-height:1.12;{ex}", x1)


def ch(x0, y0, html, fs, ex="", x1=None):
    """заголовок узким шрифтом (там, где он узкий в оригинале)"""
    return tx(x0, y0, html, fs, f"{COND}text-transform:uppercase;line-height:1.08;{ex}", x1)


def vline(x, y0, y1, col="rgba(140,160,215,.45)"):
    return f'<div style="{B(x, y0, x + 1.3, y1)}background:{col}"></div>'


def hline(x0, x1, y, col="rgba(140,160,215,.55)"):
    return f'<div style="{B(x0, y, x1, y + 1.3)}background:{col}"></div>'


def path(d, ds=None, col="#2f55c8", w=3):
    st = f' data-s="{ds}"' if ds else ""
    pts = []
    for tok in d.split():
        pts.append(tok if tok[0].isalpha() else str(q(float(tok))))
    return f'<path class="dr"{st} pathLength="1" d="{" ".join(pts)}" stroke="{col}" stroke-width="{w}" fill="none"/>'


def arr(x1, y1, x2, y2, col="#3a6fd8", w=3):
    return arrow_svg(q(x1), q(y1), q(x2), q(y2), None, col, w)


# =====================================================================
# p019  Контекстная подсказка — pptx 62
# =====================================================================
def term_html(x0, y0, x1, y1, lines):
    dots = "".join(f'<i style="width:{q(10)}px;height:{q(10)}px;border-radius:50%;background:{c};display:block"></i>'
                   for c in ("#ff5f57", "#febc2e", "#28c840"))
    body = "\n".join(lines).replace("<", "&lt;").replace(">", "&gt;")
    return (f'<div style="{B(x0, y0, x1, y1)}background:linear-gradient(180deg,#151b2c,#06090f);border-radius:10px;overflow:hidden;'
            f'box-shadow:0 10px 24px rgba(15,26,58,.35)">'
            f'<div style="display:flex;gap:{q(6)}px;padding:{q(12)}px {q(14)}px {q(10)}px;background:#1d2436">{dots}</div>'
            f'<pre class="mono" style="color:#eef2ff;font-size:21px;line-height:{q(21.5)}px;padding:{q(8)}px {q(14)}px;margin:0;'
            f'white-space:pre;letter-spacing:-1.3px;font-weight:500">{body}</pre></div>')


def s019():
    o = [ch(0, 20, 'Контекстная подсказка', 86, "text-align:center;white-space:nowrap", 1497)]
    o.append(G(1, box(412, 100, 1080, 192, "border-radius:18px"),
               cut(62, "p019_q.png", 433, 104, 524, 190, "w"),
               tx(543, 110, f'Введите <span style="color:{BL};font-size:44px">?</span> в любом месте командной строки', 33,
                  f"{COND}white-space:nowrap;line-height:1.1"),
               tx(543, 150, 'Символ ? не отображается, нажимать Enter не требуется', 25, "white-space:nowrap;color:#33407a")))

    def pad(rows, c1):
        return [a.ljust(c1) + b for a, b in rows]
    t1 = ["console# ?", ""] + pad([("backup", "Backup the configurations"), ("boot", "Boot command"),
                                    ("cd", "Changes current working directory"), ("clear", "Clear configuration"),
                                    ("clock", "Manages the system clock"), ("configure", "Configures the terminal")], 10)
    t2 = ["console# d?", ""] + pad([("debug", "Configures trace for Loopback detection"), ("delete", "Delete command"),
                                     ("dir", "Prints information about directory"), ("disable", "Disables a feature"),
                                     ("dot1x", "Configures PNAC related information"), ("dump", "Display memory content")], 9)
    t3 = ["console# show interfaces ?", ""] + pad([("<CR>", "Displays interface status and"), ("", "configuration."),
                                                    ("Fastethernet", "Fast Ethernet interface"), ("Gigabitethernet", "Gigabit ethernet interface"),
                                                    ("advertisement", "Options advertised"), ("capabilities", "Capabilities of the interface"),
                                                    ("combo", "Interfaces combo mode"), ("counters", "Counter related information")], 16)
    t3 = t3[:1] + t3[2:]
    cards = [((22, 208, 500, 708), (36, 232, 120, 316), (378, 220, 482, 332), "До начала<br>набора команды", t1,
              (38, 340, 482, 596), (38, 610, 482, 692), "Показывает команды, доступные<br>в текущем режиме."),
             ((512, 208, 980, 708), (527, 232, 611, 316), (859, 220, 963, 332), "После начала<br>набора команды", t2,
              (528, 340, 966, 596), (528, 610, 966, 692), "Ищет команды по введённой<br>первой букве."),
             ((992, 208, 1475, 708), (1007, 232, 1091, 316), (1355, 220, 1459, 332), "Просмотр<br>ключей команды", t3,
              (1007, 340, 1460, 596), (1007, 610, 1460, 692), "Показывает доступные ключи и параметры<br>незавершённой команды.")]
    for i, (c, bd, hx, t, tl, tm, ds_, d) in enumerate(cards):
        o.append(G(2 + i, box(*c, "border-radius:18px"), cut(62, f"p019_n{i + 1}.png", *bd, "w"),
                   cut(62, f"p019_hx{i + 1}.png", *hx, "w"),
                   ch(bd[2] + 18, 243, t, 35, "line-height:1.1;white-space:nowrap"),
                   term_html(*tm, tl),
                   f'<div style="{B(*ds_)}border-radius:14px;background:rgba(255,255,255,.75);box-shadow:0 4px 12px rgba(110,120,190,.12)"></div>',
                   tx(ds_[0] + 27, ds_[1] + 17, d, 25, "line-height:1.3;white-space:nowrap")))
    o.append(G(5, box(140, 727, 1355, 815, "border-radius:18px"), cut(62, "p019_doc.png", 194, 732, 274, 811, "w"),
               vline(298, 745, 798),
               tx(334, 758, 'Контекстная подсказка показывает список команд и параметров, доступных в текущем режиме.', 27,
                  "font-weight:600;white-space:nowrap;letter-spacing:-.3px")))
    return "".join(o)


SLIDES.append(("p019", "Контекстная подсказка", s019()))


# =====================================================================
# p020  Режимы командной строки — pptx 20
# =====================================================================
def s020():
    o = [tx(30, 26, f'Режимы<br><span style="color:{LB}">Командной<br>строки</span>', 70,
            f"{WIDE}text-transform:uppercase;line-height:1.03;letter-spacing:-1.5px;white-space:nowrap"),
         tx(32, 208, 'Иерархия режимов CLI<br>на маршрутизаторах ESR', 27, "line-height:1.27;color:#38447a")]
    steps = [((395, 55, 1078, 212), "01", "Пользовательский режим", ["esr&gt;"], "Непривилегированный доступ &nbsp;&bull;&nbsp; только базовые операции &nbsp;&bull;&nbsp; доступно 15 команд"),
             ((395, 245, 1078, 400), "02", "Привилегированный режим", ["esr#"], "Диагностика и переход к глобальному конфигурированию"),
             ((395, 433, 1078, 587), "03", "Глобальное конфигурирование", ["esr(config)#"], "Основной режим настройки устройства"),
             ((395, 615, 1078, 760), "04", "Конфигурирование функционала", ["esr(config-user)#", "esr(config-gre)#", "esr(config-line-ssh)#"],
              "Пользователь &nbsp;&bull;&nbsp; GRE-туннель &nbsp;&bull;&nbsp; линия SSH")]
    for i, (c, n, t, chips, d) in enumerate(steps):
        y = c[1]
        p = [box(*c, "border-radius:16px"), cut(20, f"p020_n{i + 1}.png", 412, y + 18, 494, y + 92, "w"),
             hd(513, y + 25, t, 31, "white-space:nowrap")]
        if len(chips) == 1:
            p.append(f'<div class="mono" style="{B(515, y + 63, 781, y + 107)}display:flex;align-items:center;padding-left:{q(30)}px;'
                     f'background:linear-gradient(180deg,#e9ecfa,#dfe3f6);border-radius:8px;box-shadow:inset 0 1px 0 #fff,0 2px 6px rgba(100,110,180,.15);'
                     f'font-size:33px;color:{NV}">{chips[0]}</div>')
            p.append(tx(513, y + 118, d, 21, "font-family:var(--fh);font-weight:500;white-space:nowrap;color:#2e3a6e;letter-spacing:-.4px"))
        else:
            xs = [(515, 677), (692, 854), (868, 1055)]
            for (a, b), cp in zip(xs, chips):
                p.append(f'<div class="mono" style="{B(a, y + 61, b, y + 101)}display:grid;place-items:center;'
                         f'background:linear-gradient(180deg,#f2f3fc,#e3e6f6);border-radius:8px;box-shadow:inset 0 1px 0 #fff,0 2px 6px rgba(100,110,180,.15);'
                         f'font-size:21px;font-weight:700;color:{NV};letter-spacing:-1.6px;white-space:nowrap">{cp}</div>')
            p.append(tx(513, y + 111, d, 21, "font-family:var(--fh);font-weight:500;white-space:nowrap;color:#2e3a6e"))
        o.append(G(i + 1, *p))
    o.append(SVG0 + "".join(path(f"M 423 {a} L 423 {b}", None, "rgba(120,140,200,.5)", 2) for a, b in ((212, 245), (400, 433), (587, 615)))
             + arr(737, 212, 737, 247, "#5b7fd0", 6) + arr(737, 400, 737, 435, "#5b7fd0", 6) + arr(737, 587, 737, 617, "#5b7fd0", 6) + '</svg>')
    rows = [("p020_i1.png", (272, 336), "Логин: <b style='font-size:30px'>admin</b>"), ("p020_i2.png", (342, 406), "Пароль: <b style='font-size:30px'>password</b>"),
            ("p020_i3.png", (412, 476), "Уровень привилегий: <b style='font-size:30px'>15</b>"),
            ("p020_i4.png", (483, 557), "Пользователя нельзя<br>удалить, но можно настроить")]
    r = [box(1108, 165, 1475, 608, "border-radius:20px"), hd(1140, 190, "Учётная запись<br>по умолчанию", 33, "line-height:1.15")]
    for i, (nm, (a, b), t) in enumerate(rows):
        r.append(f'<div style="{B(1130, a, 1453, b)}border-radius:10px;background:rgba(255,255,255,.72);box-shadow:0 3px 10px rgba(110,120,190,.12)"></div>')
        r.append(cut(20, nm, 1140, (a + b) / 2 - 21, 1184, (a + b) / 2 + 21, "w"))
        r.append(tx(1197, (a + b) / 2 - (14 if i < 3 else 26), t, 25 if i < 3 else 23, "white-space:nowrap;line-height:1.25"))
    o.append(G(5, *r))
    o.append(G(6, f'<div style="{B(397, 778, 1077, 820)}border-radius:12px;background:rgba(255,255,255,.7);box-shadow:0 3px 10px rgba(110,120,190,.12)"></div>',
               f'<div style="{B(426, 789, 448, 811)}border-radius:50%;background:#7088d0;color:#fff;display:grid;place-items:center;font-size:21px;font-weight:800;font-family:serif">i</div>',
               tx(470, 788, 'Символ <b>&gt;</b> — непривилегированный режим &nbsp;&nbsp;&bull;&nbsp;&nbsp; Символ <b>#</b> — привилегированный режим', 21,
                  "font-family:var(--fh);font-weight:500;white-space:nowrap;color:#2e3a6e")))
    return "".join(o)


SLIDES.append(("p020", "Режимы командной строки", s020()))


# =====================================================================
# p021  Коммутаторы агрегации — pptx 41
# =====================================================================
def s021():
    o = [hd(0, 38, 'Коммутаторы агрегации', 76, "text-align:center;white-space:nowrap;letter-spacing:-1px;line-height:1", 1497)]
    feats = [(287, "L2 и L3"), (515, "Стек до 8 устройств"), (746, "Резервирование<br>питания"), (977, "Front-to-back"),
             (1208, "1G &nbsp;&bull;&nbsp; 10G &nbsp;&bull;&nbsp; 40G")]
    f = [vline(x, 150, 218) for x in (392, 630, 866, 1096)]
    for i, (cx, t) in enumerate(feats):
        f.append(cut(41, f"p021_hx{i + 1}.png", cx - 47, 120, cx + 47, 218, "w"))
        f.append(hd(cx - 120, 216 if "<br>" in t else 222, t, 24, "text-align:center;font-weight:700;line-height:1.08", cx + 120))
    o.append(G(1, *f))
    cards = [((22, 272, 508, 577), (34, 296, 494, 420), "mes3400-48f", "MES3400-48F", 265, (120, 160, 370, 410),
              [((35, 488, 172, 553), "48 × SFP", "1G / 10G"), ((175, 488, 325, 553), None, "Высокая<br>плотность портов"),
               ((330, 488, 497, 553), None, "Для магистральных<br>и агрегационных<br>сегментов")]),
             ((518, 272, 977, 577), (538, 302, 956, 416), "mes3300-08f", "MES3300-08F", 748, (600, 640, 865, 905),
              [((531, 488, 665, 553), "8 × SFP+", "10G"), ((670, 488, 808, 553), None, "Компактное<br>решение"),
               ((813, 488, 965, 553), None, "Гибкое<br>развертывание")]),
             ((988, 272, 1475, 577), (1002, 300, 1458, 420), "mes3324f", "MES3324", 1227, (1080, 1120, 1325, 1365),
              [((1001, 488, 1140, 553), "24 × 1G", "4 × 10G"), ((1146, 488, 1296, 553), None, "Универсальная<br>агрегация"),
               ((1301, 488, 1463, 553), None, "Оптимальное<br>соотношение<br>возможностей")])]
    for i, (c, im, f_, nm, cx, ln, subs) in enumerate(cards):
        p = [box(*c, "border-radius:18px"),
             (cut(41, "p021_mes3324.png", *im, "f", alt=nm) if f_ == "mes3324f" else f'<img class="ab" src="assets/dev/{f_}.webp" alt="{nm}" style="{B(*im)}filter:drop-shadow(0 10px 14px rgba(80,95,170,.22))">'),
             hline(ln[0], ln[1], 455, "rgba(110,130,200,.6)"), hline(ln[2], ln[3], 455, "rgba(110,130,200,.6)"),
             hd(cx - 160, 437, nm, 38, "text-align:center;font-weight:700;text-transform:none", cx + 160)]
        for j, (sb, b1, t) in enumerate(subs):
            p.append(f'<div style="{B(*sb)}border-radius:8px;background:rgba(255,255,255,.6);box-shadow:0 2px 8px rgba(110,120,190,.10)"></div>')
            p.append(cut(41, f"p021_c{i + 1}{j + 1}.png", sb[0] + 8, sb[1] + 12, sb[0] + 52, sb[1] + 53, "w"))
            if b1:
                p.append(tx(sb[0] + 58, sb[1] + 13, f'<b style="font-size:22px">{b1}</b><br>{t}', 21, "line-height:1.1;white-space:nowrap;font-family:var(--fh);font-weight:500"))
            else:
                k = t.count("<br>")
                p.append(tx(sb[0] + 56, sb[1] + 32 - 8.5 * (k + 1), t, 21, "line-height:1.0;white-space:nowrap;font-family:var(--fh);font-weight:500;letter-spacing:-.9px"))
        o.append(G(2 + i, *p))
    o.append(G(5, SVG0 + path("M 263 577 L 263 605 L 640 605 L 668 632", None, "rgba(140,165,225,.75)", 3)
               + path("M 748 577 L 748 625", None, "rgba(140,165,225,.75)", 3)
               + path("M 1232 577 L 1232 605 L 856 605 L 828 632", None, "rgba(140,165,225,.75)", 3) + '</svg>',
               cut(41, "p021_globe.png", 662, 615, 834, 782, "f")))

    def agg(c, icn, ttl, txt, x0):
        return [box(*c, "border-radius:18px"), cut(41, icn, c[0] + 12, c[1] + 14, c[0] + 104, c[1] + 116, "w"),
                hd(x0, c[1] + 28, ttl, 34, "white-space:nowrap"), tx(x0, c[1] + 68, txt, 23, "line-height:1.3;white-space:nowrap")]
    o.append(G(6, *agg((178, 640, 558, 772), "p021_ag1.png", "Агрегация 1G", "Доступ и агрегация<br>на скорости 1 Гбит/с", 306),
               cut(41, "p021_chev1.png", 588, 684, 645, 724, "w")))
    o.append(G(7, cut(41, "p021_chev2.png", 840, 684, 897, 724, "w"),
               *agg((922, 640, 1340, 772), "p021_ag2.png", "Агрегация 10G / 40G", "Высокая пропускная способность<br>для магистральных соединений", 1043)))
    return "".join(o)


SLIDES.append(("p021", "Коммутаторы агрегации", s021()))


# =====================================================================
# p022  Обзор беспроводного оборудования — pptx 65
# =====================================================================
def s022():
    o = [hd(0, 30, f'Обзор <span style="color:#7d8fc9">беспроводного оборудования</span>', 64,
            "text-align:center;white-space:nowrap;letter-spacing:-1.5px;line-height:1", 1497),
         tx(0, 101, 'Беспроводные технологии расширяют возможности проводной сети и имеют преимущества и недостатки.', 26,
            "text-align:center;white-space:nowrap;color:#2e3a6e", 1497)]
    o.append(cut(65, "p022_scene.png", 446, 128, 1094, 708, "f", ds=1, alt="Wi-Fi: точка доступа и устройства"))
    pros = [("Мобильный доступ", "Быстрое подключение стационарных<br>и мобильных устройств"),
            ("Масштабируемость", "Простое добавление пользователей<br>и расширение зоны покрытия"),
            ("Гибкость", "Подключение в разных местах<br>и в удобное время"),
            ("Сокращение затрат", "Меньше кабелей и оборудования<br>по сравнению с проводной сетью"),
            ("Быстрая установка", "Одно устройство обеспечивает<br>подключение многих пользователей"),
            ("Работа в сложных условиях", "Удобное развёртывание в экстренной<br>или неблагоприятной среде")]
    ys = [(213, 297), (299, 378), (380, 460), (462, 541), (543, 622), (625, 706)]
    p = [box(15, 143, 442, 710, "border-radius:18px"), hd(40, 162, "Преимущества", 41)]
    for i, ((t, d), (a, b)) in enumerate(zip(pros, ys)):
        p.append(f'<div style="{B(37, a, 424, b - 2)}border-radius:10px;background:rgba(255,255,255,.55)"></div>')
        p.append(cut(65, f"p022_p{i + 1}.png", 44, a + 4, 118, b - 6, "w"))
        p.append(hd(137, a + 14, t, 22, "white-space:nowrap"))
        p.append(tx(137, a + 34, d, 21, "line-height:1.12;white-space:nowrap;letter-spacing:-.6px;color:#2e3a6e"))
    o.append(G(2, *p))
    cons = [("Помехи", "Сигнал зависит от<br>электромагнитных шумов<br>и других устройств"),
            ("Безопасность", "Требуются дополнительная<br>защита, шифрование<br>и контроль доступа"),
            ("Скорость и стабильность", "Радиоканал может уступать<br>проводной сети по скорости<br>и надёжности")]
    ys = [(226, 367), (375, 518), (526, 668)]
    m = [box(1098, 143, 1480, 702, "border-radius:18px"), hd(1120, 162, "Недостатки", 41)]
    for i, ((t, d), (a, b)) in enumerate(zip(cons, ys)):
        m.append(f'<div style="{B(1115, a, 1462, b)}border-radius:12px;background:rgba(255,255,255,.6);box-shadow:0 2px 8px rgba(110,120,190,.10)"></div>')
        m.append(cut(65, f"p022_c{i + 1}.png", 1120, a + 22, 1210, b - 22, "w"))
        m.append(hd(1227, a + 30, t, 23, "white-space:nowrap;letter-spacing:-.4px"))
        m.append(tx(1227, a + 60, d, 21, "line-height:1.2;white-space:nowrap;color:#2e3a6e"))
    o.append(G(3, *m))
    o.append(G(4, box(223, 710, 1268, 820, "border-radius:18px"),
               cut(65, "p022_wl.png", 268, 718, 356, 812, "w"), hd(378, 734, "Беспроводная сеть", 32, "white-space:nowrap"),
               tx(378, 771, "Мобильность &bull; гибкость &bull; быстрое развёртывание", 21, "white-space:nowrap;font-family:var(--fh);font-weight:500"),
               vline(748, 718, 812), cut(65, "p022_arr.png", 718, 745, 780, 778, "w"),
               cut(65, "p022_wd.png", 844, 718, 932, 812, "w"), hd(955, 734, "Проводная сеть", 32, "white-space:nowrap"),
               tx(955, 771, "Высокая скорость &bull; стабильность &bull; предсказуемость", 21,
                  "white-space:nowrap;font-family:var(--fh);font-weight:500;letter-spacing:-.3px")))
    return "".join(o)


SLIDES.append(("p022", "Обзор беспроводного оборудования", s022()))


# =====================================================================
# p023  Монтаж в стойку — pptx 15
# =====================================================================
def s023():
    # по требованию координатора — оригинал pptx 15 целиком, плавное появление
    return ('<img class="ab" data-s="1" src="assets/p015_full.jpg" alt="Монтаж в стойку" '
            'style="left:0;top:0;width:1920px;height:1080px;object-fit:cover;transition:opacity 900ms ease">')


SLIDES.append(("p023", "Монтаж в стойку", s023()))


# =====================================================================
# p024  Команды IP ADDRESS — pptx 26
# =====================================================================
PUR, TBL, GRN = "#7a2fc0", "#1f8fd8", "#1f9d4f"
PILL = {"cmd": ("#e9defb", "#5a2fa8"), "par": ("#d6ecfb", "#1f6fb8"), "kw": ("#d8f3e2", "#1b7a4a")}


def tok(x, yc, txt, col):
    return f'<div class="mono" style="{B(x, yc - 22)}font-size:44px;font-weight:700;color:{col};line-height:{q(44)}px;white-space:nowrap">{txt}</div>'


def pill(x0, y0, x1, y1, txt, kind, fs=23):
    bg, fg = PILL[kind]
    return (f'<div style="{B(x0, y0, x1, y1)}background:{bg};color:{fg};border-radius:8px;display:flex;align-items:center;justify-content:center;'
            f'text-align:center;font-size:{fs}px;font-weight:600;line-height:1.05;box-shadow:0 2px 6px rgba(100,110,180,.10)">{txt}</div>')


def s024():
    o = [ch(0, 22, f'Команды <span style="color:{BL}">IP address</span>', 86, "text-align:center;white-space:nowrap", 1497)]
    strip = lambda y0, y1: f'<div style="{B(52, y0, 1445, y1)}background:rgba(255,255,255,.92);border-radius:10px;box-shadow:0 2px 8px rgba(110,120,190,.10)"></div>'
    r1 = [box(30, 115, 1468, 362, "border-radius:18px"),
          hd(65, 125, f'Настройка <span style="color:{BL}">IP-адреса</span>', 35, "white-space:nowrap"),
          strip(167, 215),
          tok(187, 191, "ip address", PUR), tok(430, 191, "&lt;ADDR/LEN&gt;", TBL), tok(668, 191, "[", NV),
          tok(717, 191, "secondary", GRN), tok(918, 191, "]", NV), tok(975, 191, "[", NV),
          tok(1027, 191, "unit", GRN), tok(1137, 191, "&lt;ID&gt;", TBL), tok(1243, 191, "]", NV)]
    a1 = (SVG0 + arr(288, 214, 288, 258, PUR) + arr(529, 214, 529, 258, TBL) + arr(801, 214, 801, 258, GRN)
          + arr(1055, 214, 1055, 258, GRN) + arr(1182, 214, 1182, 258, TBL)
          + path("M 676 222 L 676 320 L 1255 320 L 1255 222", None, "#2f55c8", 3) + path("M 928 222 L 928 320", None, "#2f55c8", 3)
          + arr(968, 320, 968, 334, "#2f55c8") + '</svg>')
    l1 = [pill(197, 262, 380, 308, "Команда", "cmd"), pill(427, 262, 630, 310, "Обязательный<br>параметр", "par"),
          pill(723, 262, 880, 308, "Ключевое<br>слово", "kw"), pill(985, 262, 1120, 308, "Ключевое<br>слово", "kw"),
          pill(1126, 262, 1242, 308, "Параметр", "par"), pill(815, 335, 1120, 357, "Необязательные элементы", "par", 21)]
    r2 = [box(30, 375, 1468, 598, "border-radius:18px"),
          hd(65, 385, f'Удаление <span style="color:{BL}">IP-адреса</span>', 35, "white-space:nowrap"),
          strip(425, 473),
          tok(240, 450, "no ip address", PUR), tok(520, 450, "{", NV), tok(568, 450, "&lt;ADDR/LEN&gt;", TBL),
          tok(787, 450, "[", NV), tok(830, 450, "unit", GRN), tok(933, 450, "&lt;ID&gt;", TBL), tok(1035, 450, "]", NV),
          tok(1092, 450, "|", NV), tok(1148, 450, "all", GRN), tok(1243, 450, "}", NV)]
    a2 = (SVG0 + arr(358, 472, 358, 503, PUR) + arr(658, 472, 658, 503, TBL) + arr(853, 472, 853, 503, GRN)
          + arr(985, 472, 985, 503, TBL) + arr(1175, 472, 1175, 503, GRN)
          + path("M 530 478 L 530 556 L 1252 556 L 1252 478", None, "#2f55c8", 3) + arr(887, 556, 887, 570, "#2f55c8") + '</svg>')
    l2 = [pill(275, 505, 446, 548, "Команда", "cmd"), pill(568, 505, 750, 548, "Параметр", "par"),
          pill(790, 505, 915, 548, "Ключевое<br>слово", "kw"), pill(927, 505, 1047, 548, "Параметр", "par"),
          pill(1112, 505, 1238, 548, "Ключевое<br>слово", "kw"), pill(693, 572, 1082, 596, "Обязательный выбор одного варианта", "par", 21)]
    o += [G(1, *r1), G(2, a1, *l1), G(3, *r2), G(4, a2, *l2)]
    p = [f'<div style="{B(33, 627, 41, 635)}border-radius:50%;background:{BL}"></div>',
         hd(52, 612, "Параметры и ключевые слова", 37, "white-space:nowrap;letter-spacing:-.5px"),
         f'<div style="{B(565, 627, 573, 635)}border-radius:50%;background:{BL}"></div>', hline(575, 1462, 631, "rgba(70,110,210,.6)")]
    cards = [((33, 656, 400, 815), (44, 664, 132, 760), 150, 670, "&lt;ADDR/LEN&gt;", TBL,
              "IP-адрес и длина маски подсети<br>Формат: AAA.BBB.CCC.DDD/EE<br>AAA–DDD: [0..255]<br>EE: [1..32]", 21),
             ((410, 656, 745, 815), (420, 664, 510, 760), 530, 670, "&lt;ID&gt;", TBL,
              "<span style='font-size:24px'>Номер юнита</span><br>Допустимые значения: [1..4]", 21),
             ((752, 656, 1108, 815), (760, 664, 850, 760), 868, 664, "secondary", GRN,
              "Указывает, что адрес является<br>дополнительным.<br>Без secondary адрес считается<br>основным.<br>Допускается до 7 дополнительных<br>IP-адресов.", 21),
             ((1116, 656, 1465, 815), (1126, 664, 1216, 760), 1233, 670, "all", GRN, "Удаляет все IP-адреса<br>на интерфейсе.", 24)]
    for i, (c, ic, x, y, nm, col, d, fs) in enumerate(cards):
        lh = 1.0 if i == 2 else 1.25
        p.append(G(5, box(*c, "border-radius:14px"), cut(26, f"p024_ic{i + 1}.png", *ic, "w"),
                   tx(x, y - 4, nm, 34, f"{WIDE}font-weight:700;color:{col};white-space:nowrap"),
                   tx(x, y + (30 if i == 2 else 36), d, fs, f"line-height:{lh};white-space:nowrap;color:#26336a;font-family:var(--fh);font-weight:500"),
                   dl=i * 120))
    o.append(G(5, *p[:4]))
    o += p[4:]
    return "".join(o)


SLIDES.append(("p024", "Команды IP address", s024()))


# =====================================================================
# p025  Функционал коммутаторов MES — pptx 44
# =====================================================================
def s025():
    o = [hd(0, 13, 'Функционал коммутаторов <span style="font-size:64px">MES</span>', 56, "text-align:center;white-space:nowrap;letter-spacing:-.8px;line-height:1", 1497),
         tx(0, 62, 'Набор функций зависит от модели и версии прошивки.', 26, "text-align:center;white-space:nowrap;color:#3e4a80", 1497)]
    # --- где посмотреть
    st = [(215, "<b class='mono' style='font-size:23px'>eltex-co.ru</b>", 203),
          (306, "Каталог &rarr;<br>Ethernet-коммутаторы<br>MES", 286),
          (403, "Выбрать нужную<br>модель", 392),
          (490, "<b>Документы и файлы &rarr;</b><br>Руководство пользователя /<br>Руководство по эксплуатации", 470)]
    a = [box(25, 108, 316, 540, "border-radius:18px"), hd(43, 120, "Где посмотреть<br>функции модели", 29, "line-height:1.12"),
         vline(52, 215, 490, "rgba(110,130,200,.55)")]
    for i, (yc, t, ty) in enumerate(st):
        a.append(f'<div style="{B(40, yc - 13, 66, yc + 13)}border-radius:50%;display:grid;place-items:center;'
                 f'background:linear-gradient(160deg,#6f8fe0,#3d5cc0);color:#fff;font-size:21px;font-weight:800">{i + 1}</div>')
        a.append(cut(44, f"p025_w{i + 1}.png", 72, yc - 34, 138, yc + 34, "w"))
        a.append(tx(146, ty, t, 21, "line-height:1.08;white-space:nowrap;letter-spacing:-1px;font-family:var(--fh);font-weight:500;font-size:21px"))
        if i < 3:
            a.append(f'<div style="{B(103, yc + 36, 109, yc + 56)}color:#5a6ea8;font-size:21px;line-height:1">&darr;</div>')
    o.append(G(1, *a))
    # --- группы функций
    cols = [((338, 158, 525, 525), 431, "Интерфейсы и L2", 238,
             [((345, 278, 518, 306), "Функции интерфейсов"), ((345, 312, 518, 340), "Работа с MAC-адресами"), ((345, 348, 518, 376), "VLAN"),
              ((345, 385, 518, 413), "L2 Multicast"), ((345, 422, 518, 450), "Функции L2"), ((345, 460, 518, 494), "Link Aggregation")]),
            ((532, 158, 712, 525), 620, "L3 и IPv6", 238,
             [((538, 290, 705, 332), "Функции L3"), ((538, 342, 705, 384), "L3 Multicast"), ((538, 397, 705, 440), "Поддержка IPv6")]),
            ((718, 158, 897, 525), 805, "Безопасность<br>и трафик", 236,
             [((722, 290, 890, 332), "Функции безопасности"), ((722, 340, 890, 385), "ACL — списки<br>управления доступом"),
              ((722, 396, 890, 452), "QoS и ограничение<br>скорости")]),
            ((903, 158, 1082, 525), 992, "Управление", 238,
             [((908, 290, 1075, 335), "Сервисные функции"), ((908, 340, 1075, 395), "Основные функции<br>управления")])]
    o.append(G(2, box(325, 108, 1090, 540, "border-radius:18px"), hd(345, 120, "Группы функций", 29)))
    for i, (c, cx, t, ty, items) in enumerate(cols):
        g = [f'<div style="{B(*c)}border-radius:12px;background:rgba(255,255,255,.5);box-shadow:0 2px 8px rgba(110,120,190,.10)"></div>',
             cut(44, f"p025_g{i + 1}.png", cx - 36, 162, cx + 36, 234, "w"),
             hd(c[0], ty, t, 23, "text-align:center;line-height:1.05", c[2])]
        for j, (b, it) in enumerate(items):
            g.append(f'<div style="{B(*b)}border-radius:8px;background:rgba(255,255,255,.65)"></div>')
            g.append(cut(44, f"p025_g{i + 1}{j + 1}.png", b[0] + 3, (b[1] + b[3]) / 2 - 15, b[0] + 37, (b[1] + b[3]) / 2 + 15, "w"))
            k = it.count("<br>")
            g.append(tx(b[0] + 44, (b[1] + b[3]) / 2 - 10.5 - 8 * k, it, 21,
                        "line-height:.98;white-space:nowrap;letter-spacing:-.9px;font-family:var(--fh);font-weight:500"))
        o.append(G(3 + i, *g, dl=0))
    # --- ключевые характеристики
    tiles = [((1110, 182, 1283, 290), "Пропускная<br>способность"), ((1290, 182, 1465, 290), "Неблокируемая<br>матрица"),
             ((1110, 297, 1283, 408), "Уровень:<br>L2 или L3"), ((1290, 297, 1465, 408), "Количество<br>и скорость портов"),
             ((1110, 415, 1220, 527), "Стекирование"), ((1226, 415, 1336, 527), "PoE"), ((1342, 415, 1465, 527), "Резервирование<br>и горячая замена")]
    k = [box(1100, 108, 1475, 540, "border-radius:18px"), hd(1127, 120, "Ключевые характеристики<br>модели", 27, "line-height:1.1;white-space:nowrap")]
    for i, (c, t) in enumerate(tiles):
        cx = (c[0] + c[2]) / 2
        small = i >= 4
        k.append(f'<div style="{B(*c)}border-radius:10px;background:rgba(255,255,255,.6);box-shadow:0 2px 8px rgba(110,120,190,.10)"></div>')
        k.append(cut(44, f"p025_k{i + 1}.png", cx - 32, c[1] + 6, cx + 32, c[1] + 62, "w"))
        k.append(tx(c[0] - 6, c[1] + (64 if "<br>" in t else 72), t, 21 if small else 23,
                    "text-align:center;line-height:1.08;white-space:nowrap;letter-spacing:-.4px" + (";font-family:var(--fh);font-weight:500" if small else ""), c[2] + 6))
    o.append(G(7, *k))
    # --- неблокируемая матрица
    o.append(G(8, box(25, 548, 1475, 808, "border-radius:18px"), hd(42, 559, "Неблокируемая матрица", 32, "white-space:nowrap"),
               cut(44, "p025_mx.png", 45, 596, 968, 724, "f", alt="Ethernet-порты, коммутационная матрица, Uplink-порты"),
               cut(44, "p025_mx2.png", 455, 720, 662, 766, "w"),
               tx(60, 722, "<b>Ethernet-порты</b><br>(пользовательские)", 23, "text-align:center;line-height:1.15", 305),
               tx(790, 727, "<b>Uplink-порты</b><br>(аплинки)", 23, "text-align:center;line-height:1.15", 980)))
    o.append(G(9, f'<div style="{B(1003, 572, 1462, 790)}border-radius:14px;background:rgba(255,255,255,.6);box-shadow:0 2px 8px rgba(110,120,190,.10)"></div>',
               tx(1018, 584, '<span style="font-size:46px">&sum;</span> скоростей Ethernet-портов<br>'
                             '<span style="font-size:42px">&le;</span><span style="font-size:46px">&sum;</span> скоростей Uplink-портов', 37,
                  f"{WIDE}font-weight:700;line-height:1.12;white-space:nowrap;letter-spacing:-.6px"),
               hline(1022, 1442, 678, "rgba(120,140,200,.4)"),
               tx(1038, 690, 'Трафик со всех Ethernet-интерфейсов<br>может быть передан через Uplink<br>без внутренней блокировки.', 28,
                  "line-height:1.24;white-space:nowrap;color:#26336a")))
    return "".join(o)


SLIDES.append(("p025", "Функционал коммутаторов MES", s025()))


# =====================================================================
# p026  Системные индикаторы — pptx 17
# =====================================================================
DOT = {"g": "radial-gradient(circle at 35% 30%,#a8f59a,#22a83a 70%)", "o": "radial-gradient(circle at 35% 30%,#ffd28a,#f08a18 70%)",
       "r": "radial-gradient(circle at 35% 30%,#ff9a9a,#d81e2a 70%)", "x": "radial-gradient(circle at 35% 30%,#eef0f8,#a9b0c8 70%)"}


def dot(k):
    return (f'<i style="flex:none;width:{q(11)}px;height:{q(11)}px;border-radius:50%;background:{DOT[k]};margin-top:4px;'
            f'box-shadow:0 1px 3px rgba(0,0,0,.25)"></i>')


def led_rows(n, rows, x0, x1, xs, lx, led_w, name_fs):
    """rows: (y0, y1, led_name, name, desc, [(dot, text)...]) — таблица индикаторов"""
    h = []
    for i, (y0, y1, led, nm, ds_, items) in enumerate(rows):
        right = ("".join(f'<div style="display:flex;gap:9px;align-items:flex-start;margin:1px 0">{dot(k) if k else ""}<span>{t}</span></div>'
                         for k, t in items) if items else '<div style="text-align:center;width:100%">-</div>')
        h.append(f'<div style="display:grid;grid-template-columns:{q(xs - x0)}px 1fr;min-height:{q(y1 - y0)}px;border-radius:10px;'
                 f'background:rgba(255,255,255,.62);box-shadow:0 2px 8px rgba(110,120,190,.10);margin-bottom:{q(5)}px;overflow:hidden">'
                 f'<div style="position:relative;display:flex;align-items:center;padding:3px 4px 3px {q(lx - x0)}px;border-right:1px solid rgba(160,170,210,.35)">'
                 f'<img src="assets/{led}" alt="" style="position:absolute;left:{q(4)}px;top:50%;width:{q(led_w)}px;transform:translateY(-50%)">'
                 f'<div><div style="{WIDE}font-size:{name_fs}px;line-height:1.05">{nm}</div>'
                 f'<div style="font-size:21px;line-height:1.0;color:#4a5584;font-family:var(--fh);font-weight:500">{ds_}</div></div></div>'
                 f'<div style="display:flex;flex-direction:column;justify-content:center;padding:3px 6px 3px 12px;font-size:21px;line-height:1.0;'
                 f'font-family:var(--fh);font-weight:500;color:#26336a">{right}</div></div>')
    return f'<div style="{B(x0, rows[0][0], x1)}">{"".join(h)}</div>'


def s026():
    o = [tx(38, 28, f'Системные<br><span style="color:#6f87d8">индикаторы</span>', 74,
            f"{WIDE}text-transform:uppercase;line-height:1.05;letter-spacing:-1.5px;white-space:nowrap"),
         f'<div style="{B(42, 147, 92, 149)}background:{BL}"></div>',
         tx(42, 160, 'Системные индикаторы средних<br>моделей содержат индикаторы:<br><b>Status, Alarm, Power</b> и <b>FAN</b>.<br>'
                     'Эти индикаторы отражают текущее<br>состояние устройства.<br><br>'
                     'В младших моделях не все из этих<br>индикаторов используются,<br>зависит от конкретной модели.<br><br>'
                     'Системные индикаторы старших<br>моделей, в отличии от средних,<br>имеют не 4, а 8 значений индикаторов.<br>'
                     'К имеющимся <b>Status, Alarm, Power</b><br>и <b>FAN</b> добавляются ещё:<br><b>VPN, Mastr, RPS</b> и <b>Flash</b>.', 23,
            "line-height:1.13;white-space:nowrap;letter-spacing:-.3px;color:#26336a"),
         '<img class="ab" src="assets/dev/esr-200.webp" alt="ESR-200" style="' + B(0, 585, 600) + 'filter:drop-shadow(0 14px 20px rgba(80,95,170,.25))">']
    # leds
    leds = {"g": "p026_led_g.png", "r": "p026_led_r.png", "b": "p026_led_b.png"}
    CROPS.extend([(17, "p026_led_g.png", 541, 151, 599, 199, "w"), (17, "p026_led_r.png", 541, 244, 599, 292, "w"),
                  (17, "p026_led_b.png", 988, 442, 1044, 490, "w")])
    mid = [(138, 215, leds["g"], "Status", "Текущее состояние<br>устройства", [("g", "Работает нормально."), ("o", "Состояние загрузки ПО.")]),
           (224, 312, leds["r"], "Alarm", "Наличие и уровень<br>аварии устройства", [("x", "Выключен"), ("", "Устройство работает<br>в безаварийном режиме.")]),
           (320, 477, leds["g"], "Power", "Электропитание", [("g", "Основной источник<br>питания в норме."),
                                                             ("o", "Неработоспособность<br>основного источника питания,<br>авария или отсутствие<br>первичной сети."),
                                                             ("x", "Отказ внутренних<br>источников питания.")]),
           (486, 563, leds["g"], "FAN", "Состояние<br>вентиляторов", [("x", "Все вентиляторы исправны."), ("r", "Отказ одного/нескольких<br>вентиляторов.")])]
    o.append(G(1, box(522, 55, 950, 600, "border-radius:18px"), hd(545, 66, "Средние модели", 31, "white-space:nowrap"),
               tx(545, 96, "4 основных индикатора", 23, "color:#5a6aa8;white-space:nowrap"),
               cut(17, "p026_mid_dev.png", 785, 85, 940, 130, "w"),
               led_rows(17, mid, 533, 937, 740, 613, 60, 23)))
    old = [(137, 190, leds["g"], "Status", "Текущее состояние<br>устройства", [("g", "Работает нормально."), ("o", "Состояние загрузки ПО.")]),
           (197, 252, leds["r"], "Alarm", "Наличие и уровень<br>аварии устройства", [("x", "Выключен"), ("", "Устройство работает<br>в безаварийном режиме.")]),
           (260, 370, leds["g"], "Power", "Электропитание", [("g", "Основной источник питания<br>в норме."),
                                                             ("o", "Неработоспособность основного<br>источника питания, авария или<br>отсутствие первичной сети."),
                                                             ("x", "Отказ внутренних источников<br>питания.")]),
           (378, 433, leds["g"], "FAN", "Состояние вентиляторов", [("x", "Все вентиляторы исправны."), ("r", "Отказ одного/нескольких<br>вентиляторов.")]),
           (440, 490, leds["b"], "VPN", "Наличие активных<br>VPN-сессий.", None),
           (497, 548, leds["b"], "Mastr", "Работа устройства<br>в failover-режимах.", None),
           (555, 662, leds["b"], "RPS", "Режим работы<br>резервного источника<br>питания.", [("g", "Резервный источник питания<br>установлен и исправен."),
                                                                                         ("r", "Отсутствие первичного питания<br>резервного источника или его<br>неисправность."),
                                                                                         ("x", "Резервный источник не установлен.")]),
           (670, 740, leds["b"], "Flash", "Активность обмена<br>с накопителем:<br>SD-картой/USB Flash.", [("g", "Выполнение операций чтение<br>и записи по команде «copy».")])]
    o.append(G(2, box(968, 55, 1478, 832, "border-radius:18px"), hd(997, 66, "Старшие модели", 31, "white-space:nowrap"),
               tx(997, 96, "8 индикаторов", 23, "color:#5a6aa8;white-space:nowrap"),
               cut(17, "p026_old_dev.png", 1262, 60, 1450, 132, "w"),
               led_rows(17, old, 978, 1460, 1200, 1058, 54, 22)))
    o.append(G(3, box(493, 705, 855, 802, "border-radius:16px"),
               tx(510, 712, "&ldquo;", 72, f"{WIDE}color:#5a73c8;line-height:1"),
               tx(562, 716, 'Индикаторы помогают быстро<br>оценить состояние устройства<br>и своевременно выявить возможные<br>неисправности.', 21,
                  "line-height:1.08;white-space:nowrap;letter-spacing:-.4px;color:#26336a")))
    return "".join(o)


SLIDES.append(("p026", "Системные индикаторы", s026()))
