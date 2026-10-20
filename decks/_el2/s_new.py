# -*- coding: utf-8 -*-
"""Новые слайды: p059a (pptx 32, commit/confirm), p083 (pptx 83, доп. настройки VAP), p084 (pptx 84, Minimal Signal)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import arrow_svg  # noqa: F401  (формат KIT)

SLIDES = []
K = 1920 / 1672          # пересчёт px оригинала (1672x941) в холст 1920x1080


def k(v):
    return round(v * K)


def box(x0, y0, x1, y1, extra=""):
    return f"position:absolute;left:{k(x0)}px;top:{k(y0)}px;width:{k(x1 - x0)}px;height:{k(y1 - y0)}px;{extra}"


def div(x0, y0, x1, y1, inner, s=None, cls="", extra="", dl=0):
    st = box(x0, y0, x1, y1, extra) + (f"--dl:{dl}ms;" if dl and s else "")
    d = f' data-s="{s}"' if s else ""
    c = f' class="{cls}"' if cls else ""
    return f'<div{c}{d} style="{st}">{inner}</div>'


def img(name, x0, y0, x1, s=None, extra="", dl=0):
    d = f' data-s="{s}"' if s else ""
    dls = f"--dl:{dl}ms;" if dl and s else ""
    blend = "mix-blend-mode:multiply;" if name.endswith(".png") else ""
    return (f'<img class="ab"{d} src="assets/{name}" alt="" '
            f'style="left:{k(x0)}px;top:{k(y0)}px;width:{k(x1 - x0)}px;{blend}{dls}{extra}">')


def layer(*parts):
    return ('<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" '
            'viewBox="0 0 1920 1080">' + "".join(parts) + '</svg>')


def fat_arrow(x, y0, y1, s, col="#4d6cf0", dl=0):
    """Толстая вертикальная стрелка (вниз, если y1>y0) в координатах оригинала."""
    X, Y0, Y1 = k(x), k(y0), k(y1)
    dn = 1 if Y1 > Y0 else -1
    tip = Y1
    base = Y1 - dn * 26
    st = f' style="--dl:{dl}ms"' if dl else ""
    return (f'<g data-s="{s}"{st}><path d="M{X - 8} {Y0} L{X + 8} {Y0} L{X + 8} {base} L{X + 20} {base} '
            f'L{X} {tip} L{X - 20} {base} L{X - 8} {base} Z" fill="{col}" opacity=".92"/></g>')


def thin_arrow(x, y0, y1, s, dl=0):
    X, Y0, Y1 = k(x), k(y0), k(y1)
    st = f' style="--dl:{dl}ms"' if dl else ""
    return (f'<g data-s="{s}"{st}><path d="M{X} {Y0} V{Y1 - 12}" stroke="#4d6cf0" stroke-width="5"/>'
            f'<path d="M{X - 11} {Y1 - 16} L{X} {Y1} L{X + 11} {Y1 - 16} Z" fill="#4d6cf0"/></g>')


MONO = "font-family:var(--fm,ui-monospace,Consolas,monospace);font-weight:700;color:var(--navy)"
CARD = "background:rgba(255,255,255,.62);border:1.5px solid rgba(160,180,240,.55);border-radius:14px;box-shadow:0 8px 22px rgba(90,110,190,.12);"


# ======================================================= p059a commit / confirm (pptx 32)
def commit_confirm():
    o = ['<h1 class="t ab" style="left:300px;top:22px;width:1300px;font-size:76px;text-align:center">'
         'Механизм <span style="text-transform:uppercase">commit</span> и '
         '<span style="text-transform:uppercase">confirm</span></h1>',
         layer(f'<path d="M{k(360)} {k(100)} H{k(1285)}" stroke="#8fa8f0" stroke-width="2"/>'
               f'<rect x="{k(822)}" y="{k(94)}" width="12" height="12" transform="rotate(45 {k(828)} {k(100)})" fill="#5a86f0"/>')]
    # верхний ряд источников
    src = [(48, 320, "p032_ico_cmd.png", '<span style="font-weight:700;font-size:23px;color:var(--navy);line-height:1.2">Команды<br>конфигурации</span>'),
           (340, 626, "p032_ico_doc.png", f'<span style="{MONO};font-size:24px">default-config</span>'),
           (645, 914, "p032_ico_doc.png", f'<span style="{MONO};font-size:24px">factory-config</span>'),
           (930, 1226, "p032_ico_doc.png", '<span style="font-weight:700;font-size:21px;color:var(--navy);line-height:1.2">Файл конфигурации<br>с удалённого сервера</span>')]
    for i, (x0, x1, ic, txt) in enumerate(src):
        inner = (f'<div style="display:flex;align-items:center;gap:14px;height:100%;padding:0 14px;white-space:nowrap">'
                 f'<img src="assets/{ic}" alt="" style="width:{k(44)}px;mix-blend-mode:multiply">{txt}</div>')
        o.append(div(x0, 127, x1, 210, inner, 1, extra=CARD, dl=i * 100))
    arr = [thin_arrow(x, 212, 252, 1, dl=300) for x in (202, 484, 784, 1074)]

    def band(y0, y1, name, desc, bg, bd):
        inner = (f'<div style="position:absolute;left:{k(300)}px;top:{k(16)}px;display:flex;gap:{k(30)}px;align-items:center">'
                 f'<img src="assets/p032_doc_big.png" alt="" style="width:{k(62)}px">'
                 f'<div><div style="{MONO};font-size:40px;line-height:1.1">{name}</div>'
                 f'<div style="font-size:22px;color:var(--ink);margin-top:6px">{desc}</div></div></div>')
        return box(117, y0, 1157, y1, f"background:{bg};border:2px solid {bd};border-radius:14px;"
                   "box-shadow:0 10px 26px rgba(90,110,190,.14);"), inner

    st, inner = band(256, 357, "candidate-config", "Подготовленные, но ещё не применённые изменения",
                     "linear-gradient(90deg,rgba(214,200,255,.75),rgba(236,230,255,.7))", "#b9a6f2")
    o.append(f'<div data-s="2" style="{st}">{inner}</div>')
    st, inner = band(443, 546, "running-config", "Текущая активная конфигурация",
                     "linear-gradient(90deg,rgba(200,240,226,.8),rgba(228,248,240,.75))", "#7ccfaa")
    inner += (f'<img src="assets/p032_check.png" alt="" style="position:absolute;left:{k(745)}px;top:{k(18)}px;width:{k(70)}px">'
              f'<div style="position:absolute;left:{k(842)}px;top:{k(14)}px;white-space:nowrap"><div style="{MONO};font-size:29px">confirm</div>'
              '<div style="font-size:18px;line-height:1.3;color:var(--ink)">Подтвердить<br>применённые изменения</div></div>')
    o.append(f'<div data-s="3" style="{st}">{inner}</div>')
    st, inner = band(634, 733, "restore-config", "Копия конфигурации для возможного восстановления",
                     "linear-gradient(90deg,rgba(208,222,255,.8),rgba(232,240,255,.75))", "#97b2f2")
    o.append(f'<div data-s="5" style="{st}">{inner}</div>')

    arr += [fat_arrow(390, 358, 441, 3), fat_arrow(785, 441, 358, 4), fat_arrow(390, 548, 632, 5),
            fat_arrow(785, 632, 548, 6)]
    o.append(layer(*arr))
    lab = "font-size:20px;line-height:1.25;color:var(--ink)"
    o.append(div(240, 378, 380, 420, f'<div style="{MONO};font-size:36px;text-align:right">commit</div>', 3))
    o.append(div(418, 385, 700, 415, f'<div style="font-size:21px;color:var(--ink)">Применить изменения</div>', 3))
    o.append(div(812, 370, 1200, 430,
                 f'<div style="display:flex;gap:16px;align-items:center"><span style="{MONO};font-size:35px">rollback</span>'
                 f'<span style="width:2px;height:62px;background:var(--navy)"></span>'
                 f'<span style="{lab}">Удалить предварительно<br>внесённые изменения<br>из candidate-config</span></div>', 4))
    o.append(div(190, 568, 380, 616, f'<div style="font-size:21px;line-height:1.2;color:var(--navy)">Создание точки<br>восстановления</div>', 5))
    o.append(div(812, 565, 1210, 630,
                 f'<div style="display:flex;gap:16px;align-items:center"><span style="{MONO};font-size:35px">restore</span>'
                 f'<span style="width:2px;height:62px;background:var(--navy)"></span>'
                 f'<span style="{lab};white-space:nowrap">Отменить неподтверждённые<br>изменения без ожидания<br>таймера</span></div>', 6))
    # строка процесса
    ar = '<svg width="40" height="16" viewBox="0 0 40 16"><path d="M2 8H36M28 2L37 8L28 14" stroke="var(--navy)" stroke-width="2.4" fill="none"/></svg>'
    flow = (f'<div style="display:flex;align-items:center;justify-content:space-around;height:100%;font-size:22px;color:var(--navy)">'
            f'<span style="display:flex;gap:18px;align-items:center"><img src="assets/p032_ico_doc.png" alt="" style="width:38px">'
            f'<span style="{MONO};font-size:25px">commit</span></span>{ar}'
            f'<span style="display:flex;gap:16px;align-items:center"><img src="assets/p032_clock.png" alt="" style="width:46px">'
            f'ожидание <span style="{MONO};font-size:25px">confirm</span></span>{ar}'
            f'<span style="display:flex;gap:16px;align-items:center"><img src="assets/p032_okmini.png" alt="" style="width:46px">'
            f'<span style="{MONO};font-size:25px">confirm</span> или <span style="{MONO};font-size:25px">restore</span></span></div>')
    o.append(div(160, 750, 1138, 812, flow, 7, extra=CARD))
    info = (f'<div style="display:flex;align-items:center;gap:26px;height:100%;padding:0 26px">'
            f'<img src="assets/p032_info.png" alt="" style="width:{k(52)}px">'
            f'<span style="font-size:23px;color:var(--ink)"><span style="{MONO};font-size:27px">candidate-config</span>'
            f' — конфигурационный файл, изменения из которого применяются после команды '
            f'<span style="{MONO};font-size:27px">commit</span>.</span></div>')
    o.append(div(47, 836, 1423, 907, info, 8, extra=CARD))
    # правая колонка
    side = [(145, 290, "p032_sq_commit.png", "commit", "Применяет изменения<br>из candidate-config"),
            (307, 450, "p032_sq_confirm.png", "confirm", "Подтверждает<br>применённые изменения"),
            (466, 618, "p032_sq_restore.png", "restore", "Отменяет неподтверждённые<br>изменения без ожидания<br>таймера"),
            (634, 773, "p032_sq_rollback.png", "rollback", "Удаляет подготовленные<br>изменения из candidate-config")]
    steps = (3, 3, 6, 4)
    for (y0, y1, ic, name, txt), s in zip(side, steps):
        inner = (f'<div style="display:flex;align-items:center;gap:16px;height:100%;padding:0 10px;white-space:nowrap">'
                 f'<img src="assets/{ic}" alt="" style="width:{k(78)}px">'
                 f'<div><div style="{MONO};font-size:37px;line-height:1.1">{name}</div>'
                 f'<div style="font-size:20px;line-height:1.3;color:var(--ink);margin-top:6px">{txt}</div></div></div>')
        o.append(div(1262, y0, 1641, y1, inner, s, extra=CARD))
    return "".join(o)


SLIDES.append(("p059a", "Механизм commit и confirm", commit_confirm()))


# ======================================================= p083 доп. настройки VAP (pptx 83)
def H(txt, sz=30, col="var(--navy)"):
    return (f'<div style="font-family:var(--fh);font-size:{sz}px;font-weight:700;color:{col};'
            f'text-transform:uppercase;line-height:1.1">{txt}</div>')


def P(txt, sz=21):
    return f'<p style="font-size:{sz}px;line-height:1.35;color:var(--ink);margin-top:10px">{txt}</p>'


def vap_extra():
    o = ['<h1 class="t ab" style="left:68px;top:18px;width:1100px;font-size:66px;text-align:left;white-space:nowrap">'
         'Дополнительные настройки VAP</h1>',
         img("p083_web.jpg", 42, 122, 757, 1, "border-radius:14px;box-shadow:0 14px 34px rgba(90,110,190,.22);")]
    o.append(div(785, 112, 1188, 325, "", 2, extra=CARD))
    o.append(img("p083_ssid.png", 800, 130, 892, 2))
    o.append(div(906, 128, 1180, 320, H("Вещание SSID") + P("Включает отображение имени беспроводной сети в эфире."), 2))
    o.append(div(1203, 112, 1642, 325, "", 3, extra=CARD))
    o.append(img("p083_wifi.png", 1215, 125, 1305, 3))
    o.append(div(1314, 120, 1640, 245, H("Band Steering") +
                 '<p style="font-size:19px;line-height:1.16;letter-spacing:-.3px;color:var(--ink);margin-top:4px">Переводит совместимых клиентов '
                 'в сеть 5 ГГц. На обоих радиоинтерфейсах должны быть одинаковый SSID и включён Band Steer.</p>', 3))
    o.append(img("p083_band.png", 1285, 262, 1600, 3, dl=250))
    o.append(div(785, 340, 1195, 505, "", 4, extra=CARD))
    o.append(img("p083_tree.png", 798, 355, 892, 4))
    o.append(div(895, 348, 1194, 504, H("VLAN Trunk и General Mode", 24) +
                 '<p style="font-size:18.5px;line-height:1.18;letter-spacing:-.3px;color:var(--ink);margin-top:5px">VLAN Trunk передаёт клиенту '
                 'тегированный трафик.<br>General Mode разрешает одновременно тегированный и нетегированный трафик.</p>', 4))
    o.append(div(1210, 340, 1642, 505, "", 5, extra=CARD))
    o.append(img("p083_tag.png", 1222, 355, 1310, 5))
    o.append(div(1326, 352, 1636, 500, H("General VLAN ID", 28) +
                 '<p style="font-size:20px;line-height:1.22;letter-spacing:-.2px;color:var(--ink);margin-top:8px">Для указанного VLAN метка снимается при передаче клиенту. Обратный нетегированный трафик получает этот VLAN ID.</p>', 5))
    o.append(div(785, 520, 1642, 650, "", 6, extra=CARD))
    o.append(img("p083_iso.png", 788, 535, 905, 6))
    o.append(div(915, 528, 1350, 648, H("Изоляция и роуминг", 28) +
                 '<p style="font-size:19px;line-height:1.18;letter-spacing:-.3px;color:var(--ink);margin-top:6px">Изоляция блокирует обмен между клиентами одной VAP. 802.11k/v помогает выбирать соседнюю точку доступа.</p>', 6))
    o.append(img("p083_roam.png", 1360, 536, 1632, 6, dl=250))
    o.append(div(785, 668, 1642, 892, "", 7, extra=CARD))
    o.append(div(803, 680, 1150, 715, H("Приоритет трафика WMM", 29), 7))
    o.append(div(800, 733, 965, 872, "", 7, extra=CARD))
    o.append(img("p083_dscp.png", 812, 748, 860, 7))
    o.append(div(870, 742, 962, 868, H("DSCP", 27, "var(--navy)") +
                 '<p style="font-size:17px;line-height:1.25;color:var(--ink);margin-top:4px">приоритет из заголовка IP-пакета</p>', 7))
    o.append(div(972, 733, 1140, 872, "", 7, extra=CARD, dl=120))
    o.append(img("p083_8021p.png", 980, 745, 1036, 7, dl=120))
    o.append(div(1045, 742, 1138, 868, H('<span style="text-transform:none">802.1p</span>', 26, "var(--navy)") +
                 '<p style="font-size:17px;line-height:1.25;color:var(--ink);margin-top:4px">приоритет CoS из VLAN-тега</p>', 7, dl=120))
    o.append(div(1154, 715, 1156, 872, "", 8, extra="background:var(--line);"))
    o.append(div(1175, 708, 1600, 735, '<div style="font-size:19px;font-weight:600;color:var(--navy)">Четыре очереди трафика (WMM)</div>', 8))
    o.append(img("p083_wmm.png", 1160, 735, 1642, 8))
    return "".join(o)


SLIDES.append(("p083", "Дополнительные настройки VAP", vap_extra()))


# ======================================================= p084 Minimal Signal (pptx 84)
def min_signal():
    o = ['<h1 class="t ab" style="left:150px;top:18px;width:1300px;font-size:74px;text-align:left;white-space:nowrap">'
         'Minimal Signal <span class="lt">и безопасность VAP</span></h1>',
         img("p084_web.jpg", 38, 114, 926, 1, "border-radius:16px;box-shadow:0 14px 34px rgba(90,110,190,.22);")]
    rows = [(118, 240, "p084_c1.png", "Minimal Signal", "Отключает клиента при длительно<br>низком уровне сигнала.", "p084_wifix.png", (1488, 128, 1614)),
            (256, 378, "p084_c2.png", "Минимальный уровень", "Если сигнал ниже −75 дБм,<br>клиент отключается от VAP.", "p084_lvl.png", (1478, 266, 1632)),
            (394, 552, "p084_c3.png", "Порог роуминга", "При снижении сигнала до −70&nbsp;дБм клиент переключается на другую точку доступа.", "p084_roam.png", (1362, 396, 1628)),
            (568, 688, "p084_c4.png", "Интервал", "10 секунд до принятия<br>решения об отключении.", "p084_timer.png", (1432, 580, 1612))]
    cy = {0: 124, 1: 262, 2: 402, 3: 572}
    for i, (y0, y1, ic, ti, tx, pic, (px0, py0, px1)) in enumerate(rows):
        s = i + 2
        o.append(div(948, y0, 1642, y1, "", s, extra=CARD))
        o.append(img(ic, 958, cy[i], 1064, s))
        o.append(div(1082, y0 + 18, 1360 if i == 2 else 1440, y1 - 6, H(ti, 31) +
                     f'<p style="font-size:20px;line-height:1.25;letter-spacing:-.3px;color:var(--ink);margin-top:8px">{tx}</p>', s))
        o.append(img(pic, px0, py0, px1, s, dl=200))
    o.append(div(98, 715, 1585, 900, "", 6, extra=CARD))
    o.append(div(122, 728, 700, 770, H("Режимы безопасности", 37), 6))
    modes = [(118, 312, "p084_s1.png", "Выключено", "Без шифрования"),
             (323, 548, "p084_s2.png", "WPA / WPA2 / WPA3", "Защита по ключу<br>длиной 8–63 символа"),
             (558, 777, "p084_s3.png", "WPA-Enterprise", "Авторизация<br>через RADIUS"),
             (787, 1005, "p084_s4.png", "WPA2-Enterprise", "Централизованная<br>проверка пользователя")]
    for i, (x0, x1, ic, ti, tx) in enumerate(modes):
        inner = (f'<div style="display:flex;align-items:center;gap:8px;height:100%;padding:0 6px;letter-spacing:-.3px">'
                 f'<img src="assets/{ic}" alt="" style="width:{k(54)}px;flex:none;mix-blend-mode:multiply">'
                 f'<div><div style="font-family:var(--fh);font-size:19px;font-weight:700;color:var(--navy);'
                 f'text-transform:uppercase;line-height:1.1;white-space:nowrap">{ti}</div>'
                 f'<div style="font-size:16px;line-height:1.12;color:var(--ink);margin-top:3px">{tx}</div></div></div>')
        o.append(div(x0, 776, x1, 886, inner, 7, extra=CARD, dl=i * 110))
    o.append(div(1016, 745, 1018, 885, "", 8, extra="background:var(--line);"))
    o.append(img("p084_scheme.png", 1025, 740, 1570, 8))
    return "".join(o)


SLIDES.append(("p084", "Minimal Signal и безопасность VAP", min_signal()))
