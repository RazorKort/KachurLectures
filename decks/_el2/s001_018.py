# -*- coding: utf-8 -*-
"""Слайды по референсам p001-p018 (режимы CLI, документация, горячие клавиши, панели)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, arrow_svg

SLIDES = []


def ab(l, t, w=None, extra=""):
    s = f"position:absolute;left:{l}px;top:{t}px;"
    if w: s += f"width:{w}px;"
    return s + extra


def layer(*parts):
    return ('<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" '
            'viewBox="0 0 1920 1080">' + "".join(parts) + '</svg>')


def svg_lbl(x, y, t, s, anchor="middle"):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" data-s="{s}" font-family="var(--mono)" '
            f'font-size="27" font-weight="600" fill="var(--navy)">{t}</text>')


# ======================================================= режимы CLI (p001/p016)
def modes(title, prompts, fn_cmd, cards, warn=None):
    o = [f'<h1 class="t ab ctr-x" style="top:18px;width:1700px;font-size:72px">{title}</h1>']
    MB = "mix-blend-mode:multiply"
    BL = "#1d3fae"

    def box(top, h, w, name, cmd, cls, s):
        return (f'<div class="card {cls} ab" data-s="{s}" style="{ab(336, top, w)}height:{h}px;padding:16px 20px;text-align:center">'
                f'<div style="font-size:35px;font-weight:800;color:#141c3c;text-transform:uppercase;line-height:1.15">{name}</div>'
                f'<div style="display:inline-block;margin-top:6px;padding:2px 60px;border-radius:8px;border:1.5px solid rgba(120,150,210,.45);'
                f'background:rgba(255,255,255,.5);font-family:var(--mono);font-weight:600;font-size:36px;color:{BL}">{cmd}</div></div>')

    names = ["Пользовательский режим", "Привилегированный режим",
             "Режим глобального конфигурирования", "Режим конфигурирования функционала"]
    geo = [(115, 151, 904), (359, 150, 904), (607, 146, 790), (857, 152, 904)]
    for i, (name, cmd, cls, (t, h, w)) in enumerate(zip(names, prompts, ["solid", "cream", "mint", "solid"], geo)):
        o.append(box(t, h, w, name, cmd, cls, 1 + i * 2))

    tops = [156, 369, 605] if warn else [156, 423, 664]
    hs = [190, 211, 184] if warn else [244, 216, 188]
    for j, (cmd, txt) in enumerate(cards):
        o.append(f'<div class="card ab" data-s="{2 + j * 3}" style="{ab(1312, tops[j], 561)}height:{hs[j]}px;display:flex;gap:22px;'
                 f'align-items:flex-start;padding:22px 24px"><img src="assets/p024_term.png" style="width:88px;flex:none;{MB}"><div>'
                 f'<div class="mono" style="font-size:38px;font-weight:700;color:{BL};line-height:1.1">{cmd}</div>'
                 f'<p class="b" style="margin-top:8px;font-size:25px;line-height:1.3;color:#141c3c">{txt}</p></div></div>')
    if warn:
        o.append(f'<div class="card ab" data-s="8" style="{ab(1312, 818, 561)}height:191px;display:flex;gap:30px;'
                 f'align-items:center;padding:22px 30px"><img src="assets/p024_warn.png" style="width:96px;flex:none;{MB}">'
                 f'<p class="b" style="font-size:25px;line-height:1.35;color:#141c3c">{warn}</p></div>')

    def lbl(x, y, t, s, anchor):
        return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" data-s="{s}" font-family="var(--mono)" '
                f'font-size="30" font-weight="700" fill="{BL}">{t}</text>')

    def arr(x, y1, y2, s):
        d = -1 if y2 < y1 else 1
        return (f'<path class="dr" data-s="{s}" pathLength="1" d="M{x} {y1} L{x} {y2 - d * 22}" stroke="#1f4fe0" stroke-width="7" fill="none"/>'
                f'<polygon class="hd" data-s="{s}" points="{x - 16},{y2 - d * 26} {x + 16},{y2 - d * 26} {x},{y2}" fill="#1f4fe0"/>')

    parts = []
    for (y0, y1, down, s_down, s_up) in [(268, 357, "enable", 2, 3), (511, 605, "config", 4, 5), (755, 855, fn_cmd, 6, 7)]:
        parts += [arr(607, y0, y1, s_down), lbl(573, (y0 + y1) / 2 + 10, down, s_down, "end"),
                  arr(945, y1, y0, s_up), lbl(981, (y0 + y1) / 2 + 10, "exit", s_up, "start")]
    parts += [arr(1161, 855, 512, 8), lbl(1183, 692, "end", 8, "start")]
    o.append(layer(*parts))
    return "".join(o)


SLIDES.append(("p001", "Навигация между режимами (ESR)", modes(
    "Навигация между режимами",
    ["esr&gt;", "esr#", "esr(config)#", "esr(config-if-gi)#"], "int gi &lt;num&gt;",
    [("enable", "переход из пользовательского<br>режима в привилегированный"),
     ("exit", "выход на один уровень назад;<br>в привилегированном режиме<br>закрывает сеанс"),
     ("end", "переход из любого режима<br>сразу в привилегированный")],
    warn="Для команды <b class=\"mono\" style=\"color:#1d3fae\">enable</b><br>необходимо назначить<br>пароль")))

SLIDES.append(("p016", "Переключение между режимами (MES)", modes(
    "Переключение между режимами",
    ["console&gt;", "console#", "console(config)#", "console(config-if)#"], "int vlan &lt;num&gt;",
    [("enable", "Переход из пользовательского<br>режима в привилегированный.<br>Для команды необходимо<br>назначить пароль."),
     ("exit", "Выход на один уровень назад.<br>В привилегированном режиме<br>закрывает сеанс."),
     ("end", "Переход из любого режима<br>сразу в привилегированный.")])))


# ======================================================= документация (p002)
def docs():
    MB = "mix-blend-mode:multiply"
    N = "color:#1a2457"
    o = ['<div class="ab" style="left:703px;top:38px;width:513px;height:56px;border-radius:30px;background:rgba(255,255,255,.7);'
         'border:2px solid rgba(150,170,230,.5);display:grid;place-items:center;font-size:27px;color:#1a2457">Официальные материалы Элтекс</div>',
         '<div class="ab" style="left:480px;top:64px;width:200px;height:2px;background:#5a74c8"></div>',
         '<div class="ab" style="left:1240px;top:64px;width:200px;height:2px;background:#5a74c8"></div>',
         '<h1 class="t ab ctr-x" style="top:112px;width:1800px;font-size:76px">Документация для маршрутизаторов <span class="lt">ESR</span></h1>']

    def img(src, l, t, w, s):
        return f'<img class="ab" data-s="{s}" src="assets/{src}" style="left:{l}px;top:{t}px;width:{w}px;{MB}">'

    def common(cl, cover, cov_l, pill_l, url_l, url_w, url, s):
        return (f'<div class="card ab" data-s="{s}" style="left:{cl}px;top:231px;width:898px;height:737px"></div>'
                f'<img class="ph ab" data-s="{s}" src="assets/{cover}" style="left:{cov_l}px;top:276px;width:368px">'
                f'<div class="card solid ab" data-s="{s}" style="left:{pill_l}px;top:814px;width:323px;height:58px;border-radius:30px;'
                f'display:flex;gap:18px;align-items:center;justify-content:center;padding:0">'
                f'<img src="assets/p027_doc.png" style="height:40px;{MB}"><b style="font-size:27px;{N}">PDF • бесплатно</b></div>'
                f'<div class="card solid ab" data-s="{s}" style="left:{url_l}px;top:887px;width:{url_w}px;height:58px;border-radius:14px;'
                f'display:flex;gap:14px;align-items:center;padding:0 20px">'
                f'<img src="assets/p027_link.png" style="height:28px;{MB}">'
                f'<span class="mono" style="font-size:20px;{N};white-space:nowrap;letter-spacing:-1.6px">{url}</span></div>')

    T = f'font-size:42px;font-weight:800;text-transform:uppercase;line-height:1.12;{N}'
    VER = ('background:rgba(200,215,250,.8);border-radius:20px;padding:4px 20px;font-size:25px;font-weight:700;color:#2a47b0')
    # левая карточка
    o.append(common(51, "p002_cli_cover.jpg", 103, 340, 92, 828, "eltex.ru/storage/upload_center/files/16/ESR-Series_CLI_1.40.pdf", 1))
    o.append(img("p027_pdf1.png", 525, 283, 92, 1))
    o.append(f'<div class="ab" data-s="1" style="left:645px;top:285px;{T}">Справочник<br>команд CLI</div>')
    o.append(f'<div class="ab" data-s="1" style="left:648px;top:389px;{VER}">Версия 1.40</div>')
    o.append('<div class="ab" data-s="1" style="left:526px;top:446px;width:391px;height:2px;background:rgba(120,140,200,.35)"></div>')
    for i, t in enumerate(["Полный синтаксис команд", "Параметры и ключевые слова", "Значения по умолчанию"]):
        o.append(img(f"p027_f{i + 1}.png", 524, 464 + i * 57, 58, 2))
        o.append(f'<div class="ab" data-s="2" style="left:600px;top:{472 + i * 57}px;font-size:23px;letter-spacing:-.4px;white-space:nowrap;{N};--dl:{i * 100}ms">{t}</div>')
    o.append(img("p027_keys.png", 563, 646, 312, 3))
    o.append(f'<div class="ab" data-s="3" style="left:560px;top:748px;width:330px;text-align:center;font-size:27px;{N}">Поиск по документу</div>')
    # правая карточка
    o.append(common(971, "p002_man_cover.jpg", 1013, 1257, 1000, 836,
                    "eltex.ru/storage/upload_center/files/52/ESR-Series_User_manual_1.40.pdf", 4))
    o.append(img("p027_pdf2.png", 1407, 284, 82, 4))
    o.append(f'<div class="ab" data-s="4" style="left:1513px;top:292px;{T}">Руководство<br>по эксплуатации</div>')
    o.append(f'<div class="ab" data-s="4" style="left:1517px;top:398px;{VER}">Версия 1.40</div>')
    o.append('<div class="ab" data-s="4" style="left:1411px;top:472px;width:425px;height:2px;background:rgba(120,140,200,.35)"></div>')
    for i, (ic, t) in enumerate([("p027_g.png", "Минимальные настройки<br>технологий и протоколов"),
                                 ("p027_d.png", "Пошаговые примеры<br>конфигурации")]):
        o.append(img(ic, 1408, 494 + i * 116, 82, 5))
        o.append(f'<div class="ab" data-s="5" style="left:1513px;top:{510 + i * 116}px;font-size:27px;line-height:1.3;{N};--dl:{i * 120}ms">{t}</div>')
    return "".join(o)


SLIDES.append(("p002", "Документация для маршрутизаторов ESR", docs()))


# ======================================================= горячие клавиши MES (p003)
def hotkeys_mes():
    MB = "mix-blend-mode:multiply"
    N = "color:#1a2457"
    o = ['<h1 class="t ab ctr-x" style="top:28px;width:1800px;font-size:72px">Горячие клавиши и быстрые команды MES</h1>',
         '<div class="card ab" style="left:23px;top:139px;width:1875px;height:573px"></div>',
         '<div class="ab" style="left:52px;top:166px;width:4px;height:44px;background:#3a5bd0"></div>',
         f'<div class="ab" style="left:80px;top:152px;font-size:52px;font-weight:800;text-transform:uppercase;{N}">Горячие клавиши</div>']
    left = ["Вернуться к началу строки.", "Вернуться к концу строки.", "Продвинуться вперёд на один символ.",
            "Продвинуться назад на один символ.", "Удалить данный символ.", "Удалить начало строки до символа."]
    right = ["Удалить конец строки до символа.", "Удалить предыдущее слово.", "Переместить предыдущий символ.",
             "Перейти к предыдущей строке в истории команд.", "Перейти к следующей строке в истории команд.",
             "Возврат к корневому режиму CLI."]
    ys = [260, 340, 418, 498, 577, 655]

    def row(l, w, kimg, kw, sep, tx, y, txt, s, dl):
        return (f'<div data-s="{s}" style="--dl:{dl}ms"><div class="card solid ab" style="left:{l}px;top:{y - 35}px;width:{w}px;height:70px;'
                f'border-radius:12px;padding:0"></div>'
                f'<img class="ab" src="assets/{kimg}" style="left:{l + 4}px;top:{y - 40}px;width:{kw}px;{MB}">'
                f'<div class="ab" style="left:{sep}px;top:{y - 20}px;width:2px;height:40px;background:rgba(120,140,200,.35)"></div>'
                f'<div class="ab" style="left:{tx}px;top:{y - 16}px;font-size:24px;letter-spacing:-.3px;white-space:nowrap;{N}">{txt}</div></div>')

    for i, t in enumerate(left):
        o.append(row(58, 885, f"p064_kL{i + 1}.png", 300, 372, 405, ys[i], t, 1, i * 70))
    for i, t in enumerate(right):
        o.append(row(977, 885, f"p064_kR{i + 1}.png", 257, 1280, 1311, ys[i], t, 2, i * 70))

    def head(l, t, icon, title, col, s):
        return (f'<img class="ab" data-s="{s}" src="assets/{icon}" style="left:{l}px;top:{t}px;width:84px;{MB}">'
                f'<div class="ab" data-s="{s}" style="left:{l + 98}px;top:{t + 16}px;font-size:37px;font-weight:800;'
                f'text-transform:uppercase;color:{col};white-space:nowrap">{title}</div>')

    IN = 'background:rgba(255,255,255,.65);border:1.5px solid rgba(150,165,215,.4);border-radius:10px'
    o.append('<div class="card ab" data-s="3" style="left:28px;top:729px;width:620px;height:316px"></div>')
    o.append(head(44, 740, "p064_gear.png", "Привилегированный режим", "#1a2457", 3))
    o.append(f'<div class="ab" data-s="3" style="left:60px;top:818px;font-size:25px;line-height:1.15;{N}">Команды диагностики, мониторинга и очистки<br>'
             'процессов выполняются из<br>привилегированного режима.</div>')
    o.append(f'<div class="ab" data-s="3" style="left:54px;top:914px;width:574px;height:112px;{IN}"></div>')
    o.append(f'<div class="ab" data-s="3" style="left:74px;top:920px;font-size:22px;font-weight:700;{N}">Примеры команд:</div>')
    for x, w, c in [(74, 105, "ping"), (192, 163, "traceroute"), (368, 112, "show"), (492, 117, "clear")]:
        o.append(f'<div class="ab mono" data-s="3" style="left:{x}px;top:959px;width:{w}px;height:52px;border-radius:10px;'
                 f'background:linear-gradient(180deg,#f2f7ff,#d7e5fb);border:1.5px solid #b9cdf0;box-shadow:0 3px 8px rgba(80,110,190,.2);'
                 f'display:grid;place-items:center;font-size:26px;font-weight:700;color:#1d3fae">{c}</div>')
    o.append('<div class="card ab" data-s="4" style="left:667px;top:729px;width:612px;height:316px"></div>')
    o.append(head(691, 740, "p064_term.png", "Ключ do", "#1a2457", 4))
    o.append(f'<div class="ab" data-s="4" style="left:712px;top:815px;font-size:25px;line-height:1.15;{N}">Ключ <b style="color:#1d3fae">do</b> '
             'ставится перед командой<br>и позволяет выполнить привилегированную<br>команду из любого режима.</div>')
    o.append(f'<div class="ab" data-s="4" style="left:695px;top:917px;width:559px;height:109px;{IN}"></div>')
    o.append(f'<div class="ab" data-s="4" style="left:714px;top:922px;font-size:22px;font-weight:700;{N}">Примеры:</div>')
    o.append(f'<div class="ab mono" data-s="4" style="left:712px;top:952px;font-size:23px;line-height:1.35;{N};white-space:nowrap">'
             'console(config)# <b style="color:#1d3fae">do show interfaces</b><br>'
             'console(config-if)# <b style="color:#1d3fae">do ping 10.0.0.1</b></div>')
    o.append('<div class="card ab" data-s="5" style="left:1298px;top:729px;width:598px;height:316px"></div>')
    o.append(head(1323, 740, "p064_warn.png", "Исключение", "#b0174f", 5))
    o.append('<div class="ab" data-s="5" style="left:1327px;top:827px;width:546px;height:161px;border-radius:12px;'
             'background:linear-gradient(180deg,#fdf0f6,#f7e3ef);border:1.5px solid #efc6da"></div>')
    o.append(f'<div class="ab" data-s="5" style="left:1351px;top:852px;font-size:25px;line-height:1.3;{N}">Команды '
             '<b class="mono" style="color:#c2185b">dir</b> и <b class="mono" style="color:#c2185b">copy</b> не работают<br>'
             'с ключом <b style="color:#c2185b">do</b>. Они выполняются только<br>из привилегированного режима.</div>')
    return "".join(o)


SLIDES.append(("p003", "Горячие клавиши и быстрые команды MES", hotkeys_mes()))


# ======================================================= горячие клавиши ESR (p006)
def hotkeys_esr():
    MB = "mix-blend-mode:multiply"
    N = "color:#1a2457"
    o = ['<h1 class="t ab ctr-x" style="top:28px;width:1800px;font-size:74px">Горячие клавиши и быстрые команды ESR</h1>']

    def panel(l, t, w, h, title, col, s):
        return (f'<div class="card ab" data-s="{s}" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px"></div>'
                f'<div class="ab" data-s="{s}" style="left:{l + 26}px;top:{t + 32}px;width:4px;height:42px;background:{col}"></div>'
                f'<div class="ab" data-s="{s}" style="left:{l + 50}px;top:{t + 20}px;font-size:50px;font-weight:800;'
                f'text-transform:uppercase;color:{col};white-space:nowrap">{title}</div>')

    BOX = 'background:rgba(255,255,255,.7);border:1.5px solid rgba(160,150,220,.45);border-radius:10px'
    P = "color:#4a2fa8"
    o.append(panel(23, 144, 924, 431, "Сокращение команд", "#4a2fa8", 1))
    for l, w, hd, code, top in [(54, 374, "Полная команда", f'esr(config)# <b style="{P}">interface<br>gigabitethernet 1/0/1</b>', 312),
                                (522, 391, "Сокращённая команда", f'esr(config)# <b style="{P}">int gi 1/0/1</b>', 333)]:
        o.append(f'<div class="ab" data-s="1" style="left:{l}px;top:250px;width:{w}px;height:148px;{BOX}"></div>'
                 f'<div class="ab" data-s="1" style="left:{l + 26}px;top:260px;font-size:25px;font-weight:700;{P}">{hd}</div>'
                 f'<div class="ab mono" data-s="1" style="left:{l + 26}px;top:{top}px;font-size:24px;letter-spacing:-.6px;line-height:1.2;{N};white-space:nowrap">{code}</div>')
    o.append(f'<img class="ab" data-s="1" src="assets/p031_arr.png" style="left:438px;top:290px;width:78px;{MB}">')
    o.append(f'<div class="ab" data-s="1" style="left:56px;top:436px;width:857px;height:100px;{BOX}"></div>')
    o.append(f'<img class="ab" data-s="1" src="assets/p031_info.png" style="left:74px;top:448px;width:78px;{MB}">')
    o.append(f'<div class="ab" data-s="1" style="left:164px;top:452px;font-size:26px;line-height:1.25;{N}">Сокращение допустимо, '
             'если командная строка<br>однозначно распознаёт команду.</div>')
    o.append(panel(968, 144, 928, 431, "Горячие клавиши", "#1f3f9a", 2))
    keys = [(200, 230, 1293, "Завершает частично набранную команду<br>или ключевое слово"),
            (257, 230, 1293, "Выход из режима конфигурации в привилегированный<br>режим; аналог команды <b>end</b>"),
            (312, 230, 1293, "Прерывает текущую команду"),
            (365, 319, 1366, "Листает историю команд вперёд"),
            (415, 319, 1366, "Листает историю команд назад")]
    for i, (c, w, tx, t) in enumerate(keys):
        y = int(c * 1.2826)
        dy = 27 if "<br>" in t else 14
        o.append(f'<div data-s="2" style="--dl:{i * 90}ms"><img class="ab" src="assets/p031_k{i + 1}.png" '
                 f'style="left:1010px;top:{y - 38}px;width:{w}px;{MB}">'
                 f'<div class="ab" style="left:{tx}px;top:{y - dy}px;font-size:20px;letter-spacing:-.6px;line-height:1.2;white-space:nowrap;{N}">{t}</div></div>')
    DK = ('background:#13214f;border-radius:6px;border:2px solid #3c5bb5;display:flex;align-items:center;padding-left:18px;'
          'font-family:var(--mono);font-size:29px;color:#fff;white-space:nowrap')
    o.append(panel(23, 590, 924, 366, "История команд", "#1a2457", 3))
    o.append(f'<div class="ab" data-s="3" style="left:54px;top:682px;width:532px;height:57px;{DK}">esr#&nbsp;<b style="color:#8fd0ff">show history</b></div>')
    o.append(f'<div class="ab" data-s="3" style="left:54px;top:748px;font-size:22px;line-height:1.3;{N}">Показывает список ранее '
             'выполненных команд.<br>По умолчанию хранится 50 команд.</div>')
    o.append(f'<div class="ab" data-s="3" style="left:54px;top:825px;width:532px;height:60px;{DK};font-size:22px;letter-spacing:-.8px">'
             'esr(config)#&nbsp;<b style="color:#8fd0ff">history size [10-1000]</b></div>')
    o.append(f'<div class="ab" data-s="3" style="left:54px;top:896px;font-size:22px;{N}">Изменяет размер буфера истории.</div>')
    o.append(f'<div class="ab" data-s="3" style="left:618px;top:682px;width:293px;height:235px;{BOX}"></div>')
    o.append(f'<div class="ab" data-s="3" style="left:638px;top:698px;font-size:21px;font-weight:700;{N}">Пример вывода:</div>')
    o.append(f'<div class="ab mono" data-s="3" style="left:650px;top:742px;font-size:23px;line-height:33px;{N};white-space:nowrap">'
             '1&nbsp;&nbsp;<b>config</b><br>2&nbsp;&nbsp;<b>int gi 1/0/1</b><br>3&nbsp;&nbsp;<b>end</b><br>4&nbsp;&nbsp;<b>show history</b></div>')
    TL = "#0f5a6e"
    o.append(panel(968, 590, 928, 366, "Ключ do", TL, 4))
    o.append(f'<div class="ab" data-s="4" style="left:1004px;top:682px;width:477px;height:57px;{DK};background:#0d2f4a">'
             '<b style="color:#6fe0ff">do</b>&nbsp;&lt;команда&gt;</div>')
    o.append(f'<div class="ab" data-s="4" style="left:1006px;top:750px;font-size:20px;letter-spacing:-.6px;line-height:1.3;{N}">Позволяет запускать '
             'команды привилегированного<br>режима из любого режима.</div>')
    o.append(f'<div class="ab" data-s="4" style="left:1000px;top:817px;width:481px;height:113px;{BOX}"></div>')
    o.append(f'<div class="ab" data-s="4" style="left:1020px;top:823px;font-size:21px;font-weight:700;{N}">Примеры:</div>')
    o.append(f'<div class="ab mono" data-s="4" style="left:1016px;top:856px;font-size:20px;line-height:1.35;{N};white-space:nowrap;letter-spacing:-.5px">'
             f'esr(config)# <b style="color:{TL}">do show interfaces</b><br>esr(config-if-gi)# <b style="color:{TL}">do ping 10.0.0.1</b></div>')
    o.append(f'<div class="ab" data-s="5" style="left:1507px;top:680px;width:359px;height:246px;{BOX}"></div>')
    o.append(f'<div class="ab" data-s="5" style="left:1520px;top:695px;font-size:20px;font-weight:700;color:{TL};white-space:nowrap">'
             'Часто используемые команды:</div>')
    for i, (k, v) in enumerate([("Диагностика:", "ping, traceroute"), ("Мониторинг:", "show"), ("Очистка процессов:", "clear")]):
        o.append(f'<div class="ab" data-s="5" style="left:1520px;top:{750 + i * 62}px;font-size:20px;white-space:nowrap;letter-spacing:-.4px;{N}">'
                 f'{k} <b class="mono" style="color:#0d7a86">{v}</b></div>')
    o.append('<div class="card ab" data-s="6" style="left:212px;top:968px;width:1507px;height:86px"></div>')
    o.append(f'<img class="ab" data-s="6" src="assets/p031_warn.png" style="left:232px;top:978px;width:67px;{MB}">')
    o.append('<div class="ab" data-s="6" style="left:314px;top:984px;font-size:44px;font-weight:800;text-transform:uppercase;color:#b0174f">'
             'Исключение</div>')
    o.append('<div class="ab" data-s="6" style="left:596px;top:986px;width:2px;height:50px;background:rgba(120,140,200,.4)"></div>')
    o.append(f'<div class="ab" data-s="6" style="left:620px;top:996px;font-size:21px;white-space:nowrap;letter-spacing:-.3px;{N}">Команды '
             '<b class="mono" style="color:#c2185b">dir</b> и <b class="mono" style="color:#c2185b">copy</b> не работают с ключом '
             '<b class="mono" style="color:#c2185b">do</b> и выполняются только из привилегированного режима.</div>')
    return "".join(o)


SLIDES.append(("p006", "Горячие клавиши и быстрые команды ESR", hotkeys_esr()))


# ======================================================= контекстная подсказка (p009)
def context_help():
    MB = "mix-blend-mode:multiply"
    N = "color:#1a2457"
    o = ['<h1 class="t ab ctr-x" style="top:22px;width:1700px;font-size:80px">Контекстная подсказка в CLI</h1>',
         '<div class="card ab" style="left:532px;top:126px;width:856px;height:114px"></div>',
         f'<img class="ab" src="assets/p029_q.png" style="left:562px;top:128px;width:113px;{MB}">',
         f'<div class="ab" style="left:699px;top:138px;font-size:32px;font-weight:700;{N}">Введите <span style="font-size:44px">?</span>'
         f' в любом месте командной строки</div>',
         f'<div class="ab" style="left:699px;top:192px;font-size:24px;{N}">Символ не отображается и Enter нажимать не требуется</div>']
    M = f"font-family:var(--mono);{N}"

    def rows(l, t, items, c2, lh, fs=20):
        h = ""
        for i, (a_, b_) in enumerate(items):
            h += f'<div class="ab" style="left:{l}px;top:{t + i * lh}px;font-size:{fs}px;white-space:nowrap;{M}">{a_}</div>'
            if b_:
                h += (f'<div class="ab" style="left:{l + c2}px;top:{t + i * lh}px;font-size:{fs}px;white-space:nowrap;{N}">'
                      f'—&nbsp; {b_}</div>')
        return h

    def card(l, t, w, h, k, title, cmd, cw, note, box_h, body, s, nfs=24):
        return (f'<div data-s="{s}"><div class="card ab" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px"></div>'
                f'<img class="ab" src="assets/p029_h{k}.png" style="left:{l + 28}px;top:{t + 18}px;width:146px;{MB}">'
                f'<div class="ab" style="left:{l + 201}px;top:{t + 24}px;font-size:36px;font-weight:800;text-transform:uppercase;{N}">{title}</div>'
                f'<div class="ab" style="left:{l + 201}px;top:{t + 72}px;width:{cw}px;height:57px;background:#13214f;border-radius:6px;'
                f'border:2px solid #3c5bb5;display:flex;align-items:center;padding-left:24px;font-family:var(--mono);'
                f'font-size:29px;color:#fff;white-space:nowrap;letter-spacing:.5px">{cmd}</div>'
                f'<div class="ab" style="left:{l + 201}px;top:{t + 140}px;font-size:{nfs}px;white-space:nowrap;letter-spacing:{'-1.1px' if nfs < 24 else '-.4px'};{N}">{note}</div>'
                f'<div class="card solid ab" style="left:{l + 30}px;top:{t + 183}px;width:{w - 60}px;height:{box_h}px;border-radius:12px"></div>'
                f'{body}</div>')

    o.append(card(32, 253, 920, 341, 1, "Список доступных команд", "esr# ?", 209,
                  "Показывает команды, доступные в текущем режиме.", 137,
                  rows(81, 446, [("boot", "загрузка"), ("clear", "очистка"), ("commit", "применить изменения"),
                                 ("configure", "режим конфигурации")], 137, 28)
                  + rows(517, 446, [("show", "системная информация"), ("ssh", "SSH-клиент"), ("traceroute", "поиск маршрута")], 134, 28), 1))
    o.append(card(971, 253, 914, 341, 2, "Поиск по первой букве", "esr# d?", 248,
                  "Показывает команды, начинающиеся с введённой буквы.", 137,
                  rows(1026, 446, [("debug", ""), ("delete", ""), ("dir", ""), ("disable", "")], 0, 28), 2))
    o.append(card(32, 609, 920, 327, 3, "Подсказка по продолжению команды", "esr# show interfaces ?", 481,
                  "Показывает доступные ключевые слова и параметры.", 122,
                  rows(82, 802, [("bridge", ""), ("counters", ""), ("description", ""), ("port-channel", "")], 0, 26)
                  + rows(489, 802, [("sfp", ""), ("status", ""), ("switch-port", "")], 0, 26), 3))
    o.append(card(971, 609, 914, 327, 4, "Поиск созданных объектов", "esr(config)# object-group service ?", 655,
                  "Показывает текстовые переменные и объекты, созданные в системе.", 122,
                  rows(1026, 810, [("any", "зарезервировано"), ("object1", "созданный объект"), ("obtest", "созданный объект")], 119, 29),
                  4, nfs=22))

    o.append('<div class="card ab" data-s="5" style="left:113px;top:952px;width:1696px;height:93px"></div>')
    o.append(f'<div class="ab" data-s="5" style="left:186px;top:976px;font-size:36px;font-weight:800;text-transform:uppercase;{N}">'
             'Как использовать</div>')
    for i, (x, tx, t) in enumerate([(545, 632, "1. Введите начало команды"), (965, 1056, "2. Добавьте ?"),
                                    (1279, 1379, "3. Выберите вариант из списка")]):
        o.append(f'<img class="ab" data-s="{6 + i}" src="assets/p029_b{i + 1}.png" style="left:{x}px;top:959px;width:76px;{MB}">'
                 f'<div class="ab" data-s="{6 + i}" style="left:{tx}px;top:983px;font-size:20px;font-weight:600;{N}">{t}</div>')
    o.append(layer(*[f'<polygon data-s="{6 + i}" points="{x},985 {x + 14},998 {x},1011" fill="#7d97da"/>' for i, x in enumerate([925, 1235])]))
    return "".join(o)


SLIDES.append(("p009", "Контекстная подсказка в CLI", context_help()))


# ======================================================= параметры commit (p011)
def commit_params():
    MB = "mix-blend-mode:multiply"
    N = "color:#1a2457"
    o = ['<h1 class="t ab ctr-x" style="top:36px;width:1700px;font-size:72px">Дополнительные параметры commit</h1>',
         '<div class="ab mono" data-s="1" style="left:709px;top:128px;width:501px;height:94px;border-radius:10px;background:#13214f;'
         'border:3px solid #9fb6e8;box-shadow:0 10px 24px rgba(20,40,100,.3);display:grid;place-items:center;font-size:42px;'
         'color:#b7dcff;letter-spacing:2px">esr# commit ?</div>']
    o.append(layer(f'<path class="dr" data-s="1" pathLength="1" d="M709 176 H570 Q552 176 552 194 V232" stroke="#5a74c8" stroke-width="3" fill="none"/>',
                   f'<path class="dr" data-s="1" pathLength="1" d="M1210 176 H1351 Q1369 176 1369 194 V232" stroke="#5a74c8" stroke-width="3" fill="none"/>',
                   '<polygon class="hd" data-s="1" points="540,232 564,232 552,252" fill="#5a74c8"/>',
                   '<polygon class="hd" data-s="1" points="1357,232 1381,232 1369,252" fill="#5a74c8"/>'))
    NUM = ('font-size:104px;font-weight:800;line-height:1;background:linear-gradient(180deg,#9fb3e6,#4a64b8);'
           '-webkit-background-clip:text;background-clip:text;color:transparent')
    BOX = 'background:rgba(255,255,255,.75);border:1.5px solid rgba(150,165,215,.45);border-radius:8px'

    def block(dx, n, title, cmd, icon, icw, txt, pill, pw, val, s):
        return (f'<div data-s="{s}"><div class="card ab" style="left:{51 + dx}px;top:263px;width:{892 if not dx else 889}px;height:523px"></div>'
                f'<div class="ab" style="left:{113 + dx}px;top:292px;{NUM}">{n}</div>'
                f'<div class="ab" style="left:{276 + dx}px;top:305px;width:2px;height:80px;background:rgba(120,140,200,.4)"></div>'
                f'<div class="ab" style="left:{312 + dx}px;top:312px;font-size:40px;font-weight:800;text-transform:uppercase;{N};white-space:nowrap">{title}</div>'
                f'<div class="ab mono" style="left:{353 + dx}px;top:389px;width:{545 if not dx else 560}px;height:82px;{BOX};display:flex;align-items:center;'
                f'padding-left:22px;font-size:38px;font-weight:700;{N};white-space:nowrap">{cmd}</div>'
                f'<img class="ab" src="assets/{icon}" style="left:{(118 if not dx else 1022)}px;top:{461}px;width:{icw}px;{MB}">'
                f'<div class="ab" style="left:{378 + dx}px;top:492px;font-size:31px;line-height:1.25;{N}">{txt}</div>'
                f'<div class="ab" style="left:{380 + dx}px;top:587px;width:{pw}px;height:52px;background:#d6f1fa;border-radius:6px;'
                f'display:grid;place-items:center;font-size:30px;{N}">{pill}</div>'
                f'<div class="ab mono" style="left:{380 + dx}px;top:664px;width:{518 if not dx else 517}px;height:84px;{BOX};display:flex;align-items:center;'
                f'padding-left:28px;font-size:32px;{N}">{val}</div></div>')

    o.append(block(0, "01", "Комментарий", "commit comment", "p034_doc.png", 210,
                   "Добавляет комментарий к<br>резервной копии конфигурации", "До 31 символа", 269, "WORD(1-31)", 2))
    o.append(block(926, "02", "Таймер подтверждения", "commit confirm-timeout", "p034_clock.png", 220,
                   "Задаёт время ожидания<br>команды confirm", "От 120 до 86400 секунд", 421, "120-86400", 3))
    for i, (l, t, w, h, txt, sub) in enumerate([(167, 825, 417, 98, "commit", ""), (690, 818, 535, 112, "ожидание confirm", "Идёт защитный интервал"),
                                                (1334, 825, 419, 98, "confirm", "")]):
        clip = ("polygon(0 0,88% 0,100% 50%,88% 100%,0 100%)" if i == 0 else
                "polygon(6% 0,94% 0,100% 50%,94% 100%,6% 100%,0 50%)" if i == 1 else
                "polygon(0 0,100% 0,100% 100%,0 100%,6% 50%)")
        bg = "linear-gradient(180deg,#eef6ff,#d9ecfb)" if i == 1 else "linear-gradient(180deg,#f7f9ff,#e7ecfa)"
        o.append(f'<div class="ab" data-s="{4 + i}" style="left:{l}px;top:{t}px;width:{w}px;height:{h}px;clip-path:{clip};background:{bg};'
                 f'display:flex;flex-direction:column;align-items:center;justify-content:center">'
                 f'<div class="mono" style="font-size:40px;font-weight:600;{N}">{txt}</div>'
                 + (f'<div style="font-size:21px;color:#5a6890">{sub}</div>' if sub else "") + '</div>')
    o.append(layer(arrow_svg(590, 876, 682, 876, 5), arrow_svg(1231, 876, 1323, 876, 6)))
    return "".join(o)


SLIDES.append(("p011", "Дополнительные параметры commit", commit_params()))
