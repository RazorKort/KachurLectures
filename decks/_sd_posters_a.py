# -*- coding: utf-8 -*-
"""Нативные плакаты деки 2.5 — статическая маршрутизация (по фото-референсам ph03, ph07, ph08, ph09,
ph11, ph16, ph17 и титул)."""

from _sd_pkit import (t, ml, h, city, frame, panel_head, card, screen, strip, label, bubble, poster_title,
                      band, terminal, wrouter, puck, switch, monitor, laptop, tower, rack, cloud, citycloud,
                      netcloud, ar, cable, xbad, xcross, vgood, vminus, excl, dot, icon, finish, S,
                      INK, RED, CYAN, AMBER, CREAM, CREAM2, GREEN, FT, FB, FM)


def bg(seed=3, sky="dusk", arcs=True, sun=True):
    """Фон плаката во весь кадр."""
    return city(0, 0, 1600, 900, seed, sky, sun=sun, arcs=arcs, dim=.62)


# ======================================================================
#  ТИТУЛ
# ======================================================================

def cover():
    b = [bg(11, "dusk", arcs=False),
         '<rect width="1600" height="900" fill="#0b1c1b" opacity=".25"/>',
         poster_title("Статическая|и динамическая|маршрутизация", None, 50, 40, 92)]
    net = S(wrouter(560, 640, 190, "R1", ants=4), wrouter(930, 520, 190, "R2", ants=4),
            wrouter(1260, 680, 190, "R3", ants=4),
            ar(660, 610, 830, 545, "cream", 7, both=True),
            ar(1030, 545, 1170, 640, "cream", 7, both=True),
            ar(680, 700, 1140, 715, "red", 8, both=True))
    extra = S(ar(990, 470, 1250, 610, "cyan", 6, curve=110, dash=True),
              bubble(1300, 450, "При сбое — новый путь", 22, CREAM, "left", 280),
              citycloud(1460, 820, 230, 120, "Удалённая сеть", 20),
              ar(1340, 735, 1350, 800, "red", 7))
    lead = S(t(90, 420, "Глава 2.5 · Как маршрут попадает в таблицу маршрутизации:", 28, "#e6efe9", "start", 600),
             t(90, 458, "руками администратора или протоколом", 28, "#e6efe9", "start", 600),
             label(150, 520, "ip route", 22, RED, "#fff", True),
             label(310, 520, "суммирование", 22, CREAM),
             label(500, 520, "петли · blackhole", 22, CREAM),
             label(735, 520, "RIP · OSPF · BGP", 22, "#bfe9f1"))
    return finish("".join(b) + lead + net + extra)


# ======================================================================
#  ph09 — СТАТИЧЕСКАЯ И ДИНАМИЧЕСКАЯ
# ======================================================================

def _procons(x, y, w, good, bad):
    """Две колонки: преимущества / ограничения."""
    cw = (w - 16) / 2
    out = []
    for k, (title, rows, mark, hdr) in enumerate((("Преимущества", good, vgood, "#1d3433"),
                                                  ("Ограничения", bad, vminus, "#3a1f1c"))):
        cx = x + k * (cw + 16)
        out.append(frame(cx, y, cw, 270, CREAM))
        out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="52" fill="%s"/>' % (cx + 2, y + 2, cw - 4, hdr))
        out.append(mark(cx + 32, y + 27, 17))
        out.append(h(cx + 60, y + 38, title, 25, CREAM))
        for i, (ic, txt_) in enumerate(rows):
            ry = y + 64 + i * 68
            out.append('<rect x="%.1f" y="%.1f" width="%.1f" height="60" fill="%s" stroke="%s" stroke-width="2"/>'
                       % (cx + 10, ry, cw - 20, CREAM2, INK))
            out.append(icon(cx + 40, ry + 30, ic, .62, INK, False))
            out.append(ml(cx + 72, ry + (24 if "|" in txt_ else 37), txt_, 19, INK, "start", 600))
    return "".join(out)


def p09():
    b = [bg(5, "dusk"), poster_title("Статическая и динамическая маршрутизация", None, 40, 22, 54)]
    L = [card(30, 110, 760, 720),
         panel_head(30, 110, "Статическая", 46),
         t(70, 210, "Администратор задаёт маршрут", 26, INK, "start", 600),
         screen(48, 232, 724, 230, 21, "dusk", sun=True)]
    Ls = S(netcloud(140, 330, 170, 110, "Сеть А", "192.168.1.0/24", 15),
           wrouter(330, 330, 120, "R1"), wrouter(560, 330, 120, "R2"),
           netcloud(690, 330, 150, 110, "Сеть Б", "192.168.2.0/24", 15),
           cable(225, 335, 270, 335), cable(390, 335, 500, 335), cable(620, 335, 640, 335),
           label(330, 430, "ip route 192.168.2.0/24|via 10.0.0.2", 15, CREAM, INK, True))
    Lc = S(_procons(48, 480, 724,
                    [("gear", "Нет служебного обмена|маршрутами"), ("target", "Путь задан явно"),
                     ("tree", "Подходит для небольших|сетей")],
                    [("wrench", "Изменения вносят вручную"), ("warn", "Ошибки конфигурации"),
                     ("chart", "Сложно поддерживать|при росте сети")]))
    R = [card(810, 110, 760, 720),
         panel_head(810, 110, "Динамическая", 46),
         t(850, 210, "Маршрутизаторы обмениваются маршрутами", 26, INK, "start", 600),
         screen(828, 232, 724, 230, 22, "dusk", sun=True)]
    Rs = S(netcloud(920, 330, 150, 110, "Сеть А", "192.168.1.0/24", 15),
           wrouter(1080, 370, 110), wrouter(1190, 280, 110), wrouter(1310, 370, 110),
           netcloud(1460, 330, 150, 110, "Сеть В", "192.168.2.0/24", 15),
           ar(1110, 340, 1160, 300, "red", 5, both=True), ar(1220, 300, 1280, 340, "red", 5, both=True),
           ar(1140, 380, 1250, 380, "red", 5, both=True),
           cable(1000, 340, 1030, 360), cable(1370, 360, 1390, 345))
    Rc = S(_procons(828, 480, 724,
                    [("gear", "Автоматическое|обнаружение сетей"), ("cycle", "Поиск пути после сбоя"),
                     ("tree", "Удобнее для крупных|сетей")],
                    [("wrench", "Нужна настройка|протокола"), ("db", "Доп. нагрузка на ЦП,|память и сеть"),
                     ("shield", "Требуются меры защиты|обмена")]))
    fin = S(band(250, 842, 1100, "Оба подхода можно использовать вместе", 30, 50))
    return finish("".join(b) + "".join(L) + "".join(R) + Ls + Rs + Lc + Rc + fin)


# ======================================================================
#  ph08 — СТАТИЧЕСКИЕ МАРШРУТЫ (обзор)
# ======================================================================

def p08():
    b = [bg(8, "dusk"),
         poster_title("Статические маршруты", "ФИКСИРОВАННЫЕ ПРАВИЛА ПЕРЕДАЧИ ПАКЕТОВ В СЕТИ", 40, 26, 80, ".2em")]
    net = S(frame(40, 220, 300, 230, "#173332"), label(190, 250, "Сеть А|192.0.2.0/24", 22),
            switch(190, 390, 120), monitor(100, 330, .8), monitor(190, 320, .8), monitor(290, 330, .8),
            tower(310, 400, .8), cable(125, 345, 170, 385), cable(250, 345, 220, 385),
            frame(830, 220, 300, 230, "#173332"), label(980, 250, "Сеть В|198.51.100.0/24", 22),
            switch(980, 390, 120), monitor(890, 330, .8), monitor(980, 320, .8), monitor(1080, 330, .8),
            wrouter(470, 410, 150, "R1"), wrouter(700, 410, 150, "R2"),
            ar(255, 395, 390, 410, "red", 6), ar(550, 410, 620, 410, "red", 6),
            ar(780, 410, 910, 395, "red", 6),
            label(585, 360, "IP", 16, RED, "#fff", True))
    rec = S(card(40, 490, 1090, 280, "Запись маршрута", fs=40),
            '<rect x="62" y="570" width="1046" height="56" fill="#cfe6ea" stroke="%s" stroke-width="3"/>' % INK,
            t(236, 607, "Сеть назначения:", 23, INK, "middle", 700),
            t(585, 607, "Следующий узел:", 23, INK, "middle", 700),
            t(934, 607, "Выходной интерфейс:", 23, INK, "middle", 700),
            '<rect x="62" y="626" width="1046" height="120" fill="%s" stroke="%s" stroke-width="3"/>' % (CREAM, INK),
            '<path d="M411 570v176M760 570v176" stroke="%s" stroke-width="3"/>' % INK,
            icon(125, 686, "graph", 1.35, "#1f6f88", False), t(270, 698, "192.0.2.0/24", 32, INK, "middle", 700, FT),
            puck(480, 690, 34), t(640, 698, "10.0.0.2", 32, INK, "middle", 700, FT),
            icon(835, 686, "port", 1.35, INK, False), t(990, 698, "Gi1/0/1", 32, INK, "middle", 700, FT))
    side = [S(card(1160, 30, 410, 240, "Напрямую подключённые", num=1, fs=26),
              screen(1180, 100, 370, 110, 31, "dusk"), switch(1260, 160, 120),
              ar(1325, 160, 1440, 160, "red", 5), citycloud(1490, 150, 100, 60),
              t(1365, 245, "Сеть на активном интерфейсе", 21, INK, "middle", 700)),
            S(card(1160, 290, 410, 300, "Удалённые", num=2, fs=26),
              frame(1180, 350, 370, 105, "#cfe6ea", 3, False), icon(1232, 402, "docgear", 1.3, INK, False),
              ml(1290, 393, "Статические:|задаёт администратор", 21, INK, "start", 700),
              frame(1180, 465, 370, 105, "#cfe6ea", 3, False), icon(1232, 517, "net", 1.3, RED, False),
              ml(1290, 508, "Динамические:|добавляет протокол", 21, INK, "start", 700)),
            S(card(1160, 610, 410, 230, "Маршрут по умолчанию", num=3, fs=26),
              screen(1180, 680, 370, 85, 33, "dusk"), icon(1222, 722, "globe", 1.1, CREAM, False),
              ar(1260, 722, 1320, 722, "red", 5), wrouter(1380, 728, 100),
              ar(1435, 715, 1530, 690, "red", 4), ar(1435, 725, 1535, 725, "red", 4),
              ar(1435, 735, 1530, 760, "red", 4),
              ml(1365, 795, "0.0.0.0/0:|если точного направления нет", 19, INK, "middle", 700))]
    note = S(frame(40, 800, 1090, 64, "#0f2523"), excl(80, 832, 22),
             t(120, 840, "При совпадении нескольких маршрутов сначала выбирают наиболее длинный префикс.",
               24, CREAM, "start", 600))
    return finish("".join(b) + net + rec + "".join(side) + note)


# ======================================================================
#  ph16 — КАК ПОЯВЛЯЮТСЯ МАРШРУТЫ
# ======================================================================

def p16():
    b = [bg(16, "dusk"), poster_title("Как появляются|маршруты", None, 40, 20, 74),
         ml(1560, 50, "РАЗНЫЕ|ИСТОЧНИКИ —|ОДНА ТАБЛИЦА|МАРШРУТИЗАЦИИ", 17, CREAM, "end", 700)]
    p1 = S(card(30, 200, 500, 290, "Напрямую подключённая|сеть", num=1, fs=28),
           t(70, 300, "IP-адрес и префикс на активном интерфейсе", 19, INK, "start", 600),
           screen(46, 318, 468, 150, 41, "dusk"),
           laptop(110, 380, 1.0), switch(250, 380, 120), cable(150, 385, 190, 385),
           label(360, 345, "192.168.1.0/24", 20, CREAM, INK, True),
           label(280, 440, "ip address 192.168.1.1 255.255.255.0", 16, CREAM, INK, True))
    p2 = S(card(550, 200, 500, 290, "Статический маршрут", num=2, fs=28),
           t(590, 268, "Администратор задаёт путь вручную", 20, INK, "start", 600),
           label(1010, 255, "S", 26, "#1a2a29", "#fff", w=46, hh=46),
           screen(566, 290, 468, 180, 42, "dusk"),
           frame(586, 305, 300, 72, "#0b1716", 3, False),
           t(600, 333, "ip route 10.10.10.0 255.255.255.0", 15, "#e9e2cf", "start", 600, FM),
           t(600, 358, "192.0.2.1", 15, "#e9e2cf", "start", 600, FM),
           switch(800, 430, 110), label(960, 410, "Изменяется|вручную", 17, "#cfe6ea"))
    p3 = S(card(1070, 200, 500, 290, "Динамический маршрут", num=3, fs=28),
           t(1110, 268, "Протоколы обмениваются сведениями о сетях", 19, INK, "start", 600),
           screen(1086, 290, 468, 180, 43, "dusk"),
           label(1270, 320, "RIP  •  OSPF  •  IS-IS  •  BGP", 19, CREAM, INK),
           label(1520, 320, "R", 24, "#1a2a29", "#fff", w=44, hh=40),
           puck(1160, 410, 34), puck(1300, 380, 34), puck(1400, 440, 34), citycloud(1500, 400, 90, 60),
           ar(1195, 400, 1265, 385, "red", 4, both=True, dash=True), ar(1335, 390, 1370, 425, "red", 4, both=True,
                                                                        dash=True))
    core = S(wrouter(800, 572, 250, "Маршрутизатор", ants=4, labfs=24),
             ar(530, 470, 660, 560, "red", 6), ar(800, 470, 800, 520, "red", 6),
             ar(1070, 470, 940, 560, "red", 6))
    tb = S(card(30, 690, 1540, 200, "Таблица маршрутизации", fs=34))
    cols = [(60, 160, "Источник"), (220, 420, "Сеть назначения"), (640, 420, "Маска префикса"),
            (1060, 260, "Следующий узел"), (1320, 240, "Интерфейс")]
    rows = [("C", "192.168.1.0", "255.255.255.0", "—", "GigabitEthernet0/0", "#bfe0ea"),
            ("S", "10.10.10.0", "255.255.255.0", "192.0.2.1", "—", "#f6dfae"),
            ("R", "172.16.0.0", "255.255.0.0", "203.0.113.1", "GigabitEthernet0/1", "#bfe0ea")]
    tbl = ['<rect x="56" y="752" width="1488" height="34" fill="#cfe6ea" stroke="%s" stroke-width="2.5"/>' % INK]
    for (x, w, n) in cols:
        tbl.append(t(x + w / 2, 776, n, 19, INK, "middle", 700))
    for i, r in enumerate(rows):
        y = 786 + i * 32
        tbl.append('<rect x="56" y="%d" width="1488" height="32" fill="%s" stroke="%s" stroke-width="2"/>'
                   % (y, CREAM, INK))
        tbl.append('<rect x="56" y="%d" width="164" height="32" fill="%s" stroke="%s" stroke-width="2"/>'
                   % (y, r[5], INK))
        for k, (x, w, n) in enumerate(cols):
            tbl.append(t(x + w / 2, y + 23, r[k], 19, INK, "middle", 700 if k == 0 else 500, FB if k == 0 else FM))
    for (x, w, n) in cols[1:]:
        tbl.append('<path d="M%d 752V882" stroke="%s" stroke-width="2"/>' % (x, INK))
    tbs = S("".join(tbl))
    return finish("".join(b) + p1 + p2 + p3 + core + tb + tbs)


# ======================================================================
#  ph11 — НАЗНАЧЕНИЕ СТАТИЧЕСКОЙ МАРШРУТИЗАЦИИ
# ======================================================================

def _cpanel(x, y, w, hh, title, cap, seed):
    return (card(x, y, w, hh, title, fs=32) +
            screen(x + 14, y + 66, w - 28, hh - 130, seed, "teal") +
            strip(x + 14, y + hh - 56, w - 28, cap, 21, 42))


def p11():
    b = [bg(12, "teal", arcs=False, sun=True),
         poster_title("Назначение статической маршрутизации", None, 40, 24, 62)]
    a = S(_cpanel(30, 120, 500, 360, "Тупиковая сеть", "Путь к сети с одним выходом", 51),
          '<rect x="60" y="200" width="200" height="200" fill="#4a8a8a" opacity=".4" stroke="%s" '
          'stroke-width="3" stroke-dasharray="10 7"/>' % CREAM,
          monitor(110, 245, .7), laptop(100, 330, .6), tower(110, 380, .6), switch(190, 310, 90),
          cable(130, 255, 170, 300), cable(130, 335, 160, 315),
          ar(240, 310, 360, 310, "red", 5), puck(420, 305, 46))
    c = S(_cpanel(550, 120, 500, 360, "Суммаризация", "Несколько сетей — один общий префикс", 52),
          citycloud(640, 230, 120, 64), citycloud(640, 305, 120, 64), citycloud(640, 380, 120, 64),
          ar(705, 230, 830, 300, "red", 4), ar(705, 305, 830, 305, "red", 4), ar(705, 380, 830, 312, "red", 4),
          puck(910, 300, 46))
    d = S(_cpanel(1070, 120, 500, 360, "Небольшая сеть", "Простая таблица маршрутизации", 53),
          monitor(1140, 220, .7), monitor(1240, 220, .7), switch(1190, 300, 90), laptop(1140, 380, .6),
          monitor(1250, 380, .6), cable(1150, 240, 1180, 290), cable(1230, 240, 1200, 290),
          cable(1180, 310, 1150, 365), cable(1200, 310, 1240, 365),
          ar(1245, 300, 1350, 300, "red", 5), puck(1430, 300, 46))
    e = S(_cpanel(30, 500, 750, 380, "Маршрут по умолчанию", "0.0.0.0/0, если нет более точного совпадения", 54),
          monitor(110, 610, .7), monitor(230, 610, .7), switch(170, 680, 90), laptop(110, 760, .6),
          laptop(240, 760, .6), cable(120, 630, 150, 670), cable(220, 630, 190, 670),
          ar(220, 680, 330, 680, "red", 5), puck(410, 675, 48),
          ar(470, 675, 590, 675, "red", 6), cloud(670, 670, 170, 110, CREAM2, 4))
    f = S(_cpanel(800, 500, 770, 380, "Резервный маршрут", "Другой путь при отказе основного", 55),
          monitor(880, 610, .7), monitor(990, 610, .7), switch(935, 690, 90), laptop(880, 770, .6),
          cable(890, 630, 920, 680), cable(980, 630, 950, 680),
          puck(1100, 690, 44),
          ar(1140, 670, 1320, 615, "red", 4, dash=True), xcross(1230, 640, 14),
          puck(1380, 610, 38), cloud(1500, 600, 120, 76, CREAM2, 4),
          ar(1140, 705, 1320, 760, "red", 6), puck(1380, 765, 38), cloud(1500, 755, 120, 76, CREAM2, 4))
    return finish("".join(b) + a + c + d + e + f)


# ======================================================================
#  ph03 — ЧЕТЫРЕ ТИПА СТАТИЧЕСКИХ МАРШРУТОВ
# ======================================================================

def _type(x, y, title, sub, seed):
    return (city(x, y, 780, 440, seed, "dusk", sun=(seed % 2 == 1), arcs=False, dim=.7) +
            '<rect x="%d" y="%d" width="780" height="440" fill="none" stroke="%s" stroke-width="5"/>' % (x, y, INK) +
            '<rect x="%d" y="%d" width="20" height="78" fill="%s"/>' % (x + 22, y + 20, RED) +
            '<text x="%d" y="%d" font-size="60" font-weight="700" fill="%s" font-family="%s" '
            'style="paint-order:stroke" stroke="#0a1615" stroke-width="5">%s</text>'
            % (x + 58, y + 86, CREAM, FT, title.upper()) +
            label(x + 58 + len(sub) * 11.5 / 2 + 14, y + 140, sub, 23, CREAM, INK))


def p03():
    a = S(_type(15, 12, "Обычный статический", "Путь к конкретной сети", 61),
          citycloud(120, 330, 180, 110, "10.0.0.0/24", 20), wrouter(300, 330, 140, "R1"),
          wrouter(520, 330, 140, "R2"), citycloud(690, 330, 170, 110, "192.0.2.0/24", 20, red=True),
          cable(215, 335, 230, 335, "cyan", 4), ar(372, 335, 450, 335, "red", 6), ar(592, 335, 600, 335, "red", 6))
    c = S(_type(805, 12, "По умолчанию", "0.0.0.0/0 — если нет более точного маршрута", 62),
          citycloud(910, 330, 180, 110, "10.0.0.0/24", 20), wrouter(1080, 330, 130, "R1"),
          wrouter(1270, 330, 130, "R2"),
          ar(1145, 335, 1205, 335, "red", 6), ar(1335, 320, 1440, 200, "red", 5), ar(1340, 335, 1440, 305, "red", 5),
          ar(1335, 350, 1440, 410, "red", 5),
          citycloud(1510, 180, 110, 70, q=True), citycloud(1510, 300, 110, 70, q=True),
          citycloud(1510, 420, 110, 70, q=True))
    d = S(_type(15, 458, "Суммарный", "Несколько сетей — один общий маршрут", 63),
          citycloud(115, 680, 170, 100, "10.0.0.0/24", 19), citycloud(115, 820, 170, 100, "10.0.1.0/24", 19),
          '<path d="M205 680H240V820H205M240 750H260" fill="none" stroke="%s" stroke-width="5" '
          'filter="url(#__U___gl)"/>' % RED,
          label(350, 750, "10.0.0.0/23", 26, CREAM, INK),
          ar(445, 750, 500, 750, "red", 6), wrouter(570, 755, 130, "R1"), ar(640, 755, 660, 755, "red", 6),
          citycloud(720, 750, 130, 90, "10.0.2.0/24", 17))
    e = S(_type(805, 458, "Плавающий", "Резерв с меньшим приоритетом", 64),
          citycloud(900, 760, 170, 100, "10.0.0.0/24", 19), wrouter(1050, 765, 120, "R1"),
          wrouter(1250, 660, 110, "R2"), wrouter(1250, 830, 110, "R3"),
          ar(1112, 750, 1190, 670, "red", 5), cable(1310, 665, 1400, 700, "cream", 3, True, False),
          xcross(1340, 640, 12),
          ar(1112, 780, 1190, 830, "red", 4, dash=True), ar(1310, 830, 1410, 790, "red", 6),
          citycloud(1490, 760, 160, 100, "203.0.113.0/24", 18))
    return finish('<rect width="1600" height="900" fill="#0d1d1d"/>' + a + c + d + e)


# ======================================================================
#  ph07 — ПЕТЛЯ ИЗ-ЗА СУММАРНОГО МАРШРУТА
# ======================================================================

def p07():
    b = ['<rect width="1600" height="900" fill="#0d1d1d"/>',
         frame(10, 10, 1580, 90, "#0f2523"), city(14, 14, 1572, 82, 71, "dusk", sun=True, dim=.5),
         poster_title("Петля из-за суммарного маршрута", None, 30, 20, 64)]
    top = [city(10, 110, 1580, 330, 72, "teal", sun=False, dim=.78),
           '<rect x="10" y="110" width="1580" height="330" fill="none" stroke="%s" stroke-width="5"/>' % INK,
           '<rect x="34" y="128" width="16" height="56" fill="%s"/>' % CYAN,
           h(64, 178, "Правильная доставка", 54, CREAM)]
    topS = S(monitor(100, 360, 1.4), frame(110, 222, 180, 110, CREAM),
             ml(200, 252, "Пакет|назначение:", 20, INK, "middle", 600), t(200, 318, "10.1.1.25", 28, INK, "middle", 700, FT),
             ar(220, 370, 400, 370, "cyan", 8), wrouter(500, 370, 200, "ESR-A", ants=4),
             label(780, 300, "10.1.0.0/16", 30, CREAM, INK, True),
             ar(610, 370, 940, 370, "cyan", 8), wrouter(1050, 370, 200, "ESR-B", ants=4),
             bubble(1040, 225, "На ESR-B:|/24 точнее /0", 25, CREAM, "down", 230),
             ar(1160, 370, 1330, 370, "cyan", 8), rack(1400, 360, 1.3, 6), rack(1480, 370, 1.1, 5),
             label(1450, 220, "Сеть|10.1.1.0/24", 22, CREAM))
    bot = [city(10, 450, 1580, 340, 73, "red", sun=True, dim=.8),
           '<rect x="10" y="450" width="1580" height="340" fill="none" stroke="%s" stroke-width="5"/>' % INK,
           '<rect x="34" y="468" width="16" height="56" fill="%s"/>' % RED,
           h(64, 518, "Петля маршрутизации", 54, CREAM)]
    botS = S(monitor(100, 700, 1.4), frame(110, 568, 180, 110, CREAM),
             ml(200, 598, "Пакет|назначение:", 20, INK, "middle", 600),
             t(200, 664, "10.1.20.5", 28, RED, "middle", 700, FT),
             wrouter(500, 700, 200, "ESR-A", ants=4), wrouter(1050, 700, 200, "ESR-B", ants=4),
             ar(600, 660, 950, 660, "red", 8, curve=50), ar(950, 740, 600, 740, "red", 8, curve=-50),
             label(780, 585, "10.1.0.0/16 → 12.1.1.1", 26, CREAM, INK, True),
             label(780, 772, "0.0.0.0/0 → 12.1.1.2", 26, CREAM, INK, True),
             cable(1160, 680, 1300, 620, "red", 4, True), cloud(1400, 590, 230, 140, CREAM2, 4),
             xcross(1400, 565, 26), label(1400, 650, "10.1.20.0/24|отсутствует", 22, CREAM, RED))
    fin = S(frame(10, 800, 1580, 90, CREAM), excl(70, 845, 30),
            '<text x="120" y="860" font-size="40" font-weight="700" font-family="%s" fill="%s">'
            '<tspan fill="%s">TTL</tspan> уменьшается на каждом переходе: при <tspan fill="%s">TTL = 0</tspan> '
            'пакет отбрасывается</text>' % (FT, INK, RED, RED))
    return finish("".join(b) + "".join(top) + topS + "".join(bot) + botS + fin)


# ======================================================================
#  ph17 — КАК РАЗОРВАТЬ ПЕТЛЮ НА ESR-B
# ======================================================================

def p17():
    b = ['<rect width="1600" height="900" fill="#0d1d1d"/>',
         city(0, 0, 1600, 470, 81, "teal", sun=False, dim=.75),
         poster_title("Как разорвать петлю на ESR-B", None, 30, 10, 70)]
    pref = S(frame(40, 120, 800, 62, CREAM),
             t(60, 162, "Самый длинный подходящий префикс:", 27, INK, "start", 700),
             label(560, 151, "/24", 26, "#bfe9f1", INK, True), t(612, 162, "→", 28, INK),
             label(665, 151, "/16", 26, "#f7b3a8", INK, True), t(717, 162, "→", 28, INK),
             label(770, 151, "/0", 26, "#f6dfae", INK, True))
    cli = S(terminal(900, 95, 420, 135, ["ip route 10.1.0.0/16 blackhole", "do commit", "do confirm"], 20))
    net = S(wrouter(260, 350, 230, "ESR-A", ants=4), cable(380, 355, 560, 335, "cream", 4, glow=False),
            cloud(680, 320, 250, 140, CREAM2, 4), ml(680, 315, "WAN /|другая сеть", 24, INK, "middle", 700),
            cable(800, 335, 945, 355, "cream", 4, glow=False),
            wrouter(1060, 350, 230, "ESR-B", ants=4),
            ar(1180, 345, 1380, 330, "cyan", 8), rack(1440, 340, 1.2, 6), rack(1520, 350, 1.0, 5),
            label(1480, 220, "Сеть|10.1.1.0/24", 22, CREAM))
    bh = S(xbad(935, 452, 24),
           label(840, 452, "blackhole|10.1.0.0/16", 18, "#f7cfca", RED),
           ar(1150, 400, 1350, 430, "amber", 7, curve=-30),
           cloud(1460, 425, 210, 100, CREAM, 4), ml(1460, 420, "По умолчанию|0.0.0.0/0", 21, INK, "middle", 700))
    hdr = S(frame(20, 480, 1560, 340, "#173332"),
            label(160, 512, "Куда идёт пакет", 23, CREAM, INK, w=260, hh=44),
            label(700, 512, "Подходящий маршрут на ESR-B", 23, CREAM, INK, w=560, hh=44),
            label(1240, 512, "Результат", 23, CREAM, INK, w=470, hh=44))

    def row(y, addr, mid, midfill, res, col, end):
        return S(frame(30, y, 1540, 86, "#21403e", 3, False),
                 laptop(85, y + 40, .9), label(225, y + 43, addr, 34, CREAM, INK, False, w=200, hh=60),
                 ar(345, y + 43, 400, y + 43, col, 7),
                 label(700, y + 43, mid, 30, midfill, INK, False, w=520, hh=62),
                 ar(975, y + 43, 1020, y + 43, col, 7),
                 label(1240, y + 43, res, 27, CREAM, INK, False, w=420, hh=62), end)
    r1 = row(545, "10.1.1.25", "Сеть 10.1.1.0/24", "#bfe9f1", "Доставить в сеть", "cyan",
             rack(1510, 588, .8, 4))
    r2 = row(640, "10.1.20.5", "10.1.0.0/16  blackhole", "#f7c6be", "Отбросить на ESR-B", "red",
             xbad(1510, 683, 30))
    r3 = row(735, "8.8.8.8", "0.0.0.0/0", "#f6dfae", "По маршруту по умолчанию", "amber",
             cloud(1510, 778, 90, 56, CREAM, 3))
    fin = S(frame(20, 836, 1560, 54, "#0f2523"),
            t(50, 872, "Проверка:", 24, CREAM, "start", 700), label(270, 863, "show ip route", 21, "#0b1716", "#e9e2cf",
                                                                     True),
            t(440, 872, "|    blackhole: без уведомления отправителю", 24, CREAM, "start", 600))
    return finish("".join(b) + pref + cli + net + bh + hdr + r1 + r2 + r3 + fin)
