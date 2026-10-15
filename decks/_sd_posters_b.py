# -*- coding: utf-8 -*-
"""Нативные плакаты деки 2.5 — динамическая маршрутизация (по фото-референсам ph01, ph02, ph04, ph05,
ph06, ph12, ph13, ph14, ph15)."""

from _sd_pkit import (t, ml, h, city, frame, panel_head, card, screen, strip, label, bubble, poster_title,
                      band, terminal, wrouter, puck, switch, monitor, laptop, tower, rack, cloud, citycloud,
                      netcloud, ar, cable, xbad, xcross, vgood, vminus, excl, dot, icon, finish, S,
                      INK, RED, CYAN, AMBER, CREAM, CREAM2, GREEN, FT, FB, FM)


def bg(seed=3, sky="dusk", arcs=True, sun=True):
    return city(0, 0, 1600, 900, seed, sky, sun=sun, arcs=arcs, dim=.62)


def _cyan_ring(x, y, rx=70):
    return ('<ellipse cx="%.1f" cy="%.1f" rx="%.1f" ry="%.1f" fill="none" stroke="%s" stroke-width="4" '
            'opacity=".8" filter="url(#__U___gl)"/>' % (x, y, rx, rx * .26, CYAN))


# ======================================================================
#  ph01 — ДИНАМИЧЕСКИЕ МАРШРУТЫ
# ======================================================================

def p01():
    b = [bg(101, "dusk", arcs=False),
         poster_title("Динамические маршруты",
                      "Маршрутизаторы обмениваются маршрутами и реагируют на изменения сети.", 40, 24, 92)]
    net = S(wrouter(430, 470, 230, "R1", ants=4), wrouter(790, 330, 230, "R2", ants=4),
            wrouter(1110, 470, 230, "R3", ants=4),
            ar(560, 420, 670, 350, "cream", 8, both=True), ar(910, 350, 1010, 420, "cream", 8, both=True),
            ar(560, 500, 990, 500, "red", 9, both=True))
    alt = S(ar(640, 300, 690, 300, "cyan", 6, curve=0, dash=True),
            ar(920, 290, 1080, 400, "cyan", 6, curve=80, dash=True),
            label(1110, 255, "При сбое — новый путь", 24, "#0f2523", CYAN, w=290, hh=44),
            ar(1240, 480, 1350, 480, "red", 8), citycloud(1450, 470, 220, 140, "Удалённая сеть", 24))
    feats = []
    for i, (ic, txt_) in enumerate((("search", "Обнаружение|сетей"), ("refresh", "Обновление|таблиц"),
                                    ("fork", "Поиск|альтернативного|пути"))):
        x = 30 + i * 520
        feats.append(S(frame(x, 640, 500, 230, CREAM), icon(x + 120, 755, ic, 1.6, CREAM, True, "#163331", 82),
                       ml(x + 220, 745 - (20 if txt_.count("|") == 2 else 0), txt_.upper(), 36, INK, "start", 700, FT,
                          1.08)))
    return finish("".join(b) + net + alt + "".join(feats))


# ======================================================================
#  ph05 — НАЗНАЧЕНИЕ ДИНАМИЧЕСКОЙ МАРШРУТИЗАЦИИ
# ======================================================================

def _q(x, y, n, title, cap, seed):
    return (card(x, y, 760, 355, title, num=n, fs=40) +
            screen(x + 14, y + 80, 732, 210, seed, "teal") +
            strip(x + 14, y + 300, 732, cap, 23, 42))


def p05():
    b = [bg(105, "teal", arcs=True, sun=True),
         poster_title("Назначение динамической маршрутизации",
                      "Для средних и крупных сетей с меняющейся топологией", 30, 14, 60)]
    q1 = S(_q(30, 125, 1, "Обнаружение сетей", "Сведения от соседних маршрутизаторов", 111),
           netcloud(140, 300, 170, 120), wrouter(330, 310, 140, "R1"), _cyan_ring(330, 330, 85),
           wrouter(610, 310, 140, "R2"), _cyan_ring(610, 330, 85), netcloud(720, 290, 120, 100),
           ar(530, 310, 420, 310, "red", 6, dash=True),
           bubble(470, 240, "сеть 10.0.3.0/24", 18, CREAM, "down", 190))
    q2 = S(_q(810, 125, 2, "Обмен маршрутами", "Обновление маршрутной информации", 112),
           netcloud(900, 320, 140, 110), netcloud(1500, 320, 130, 110),
           wrouter(1060, 340, 130), wrouter(1190, 245, 130), wrouter(1330, 340, 130),
           ar(1095, 305, 1150, 270, "red", 5, both=True), ar(1235, 270, 1290, 305, "red", 5, both=True),
           ar(1130, 350, 1260, 350, "red", 5, both=True))
    q3 = S(_q(30, 495, 3, "Выбор пути", "По алгоритму и метрике протокола", 113),
           netcloud(120, 680, 140, 110), netcloud(700, 680, 140, 110),
           wrouter(240, 690, 120), wrouter(420, 610, 110), wrouter(420, 740, 110), wrouter(600, 690, 120),
           ar(280, 670, 375, 615, "cyan", 4, dash=True), ar(465, 615, 560, 670, "cyan", 4, dash=True),
           ar(280, 705, 375, 740, "red", 6), ar(465, 740, 560, 705, "red", 6))
    q4 = S(_q(810, 495, 4, "Реакция на сбой", "Автоматический переход на доступный путь", 114),
           netcloud(900, 680, 140, 110), netcloud(1500, 680, 130, 110),
           wrouter(1020, 690, 120), wrouter(1200, 610, 110), wrouter(1200, 740, 110), wrouter(1380, 690, 120),
           ar(1060, 670, 1155, 615, "cream", 4, dash=True), xcross(1200, 600, 22),
           ar(1060, 705, 1155, 740, "red", 6), ar(1245, 740, 1340, 705, "red", 6))
    return finish("".join(b) + q1 + q2 + q3 + q4)


# ======================================================================
#  ph02 — ХАРАКТЕРИСТИКИ ПРОТОКОЛОВ
# ======================================================================

def _stopwatch(x, y, r=70):
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="#2b3a39" stroke="%s" stroke-width="3"/>'
            '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" stroke="%s" stroke-width="8"/>'
            '<circle cx="%.1f" cy="%.1f" r="%.1f" fill="none" stroke="#9aa7a5" stroke-width="3"/>'
            '<path d="M%.1f %.1f L%.1f %.1f" stroke="%s" stroke-width="7" stroke-linecap="round"/>'
            '<path d="M%.1f %.1f A%.1f %.1f 0 0 1 %.1f %.1f" fill="none" stroke="%s" stroke-width="7"/></g>'
            % (x - 12, y - r - 26, 24, 22, INK, x, y, r, CREAM, INK, x, y, r * .78,
               x, y, x + r * .5, y + r * .45, RED, x, y - r * .78, r * .78, r * .78, x + r * .78, y, RED))


def _chip(x, y, s=1.0, lab="ЦП"):
    w = 110 * s
    pins = "".join('<path d="M%.1f %.1f v-12 M%.1f %.1f v12" stroke="%s" stroke-width="4"/>'
                   % (x - w * .35 + i * w * .14, y - w / 2, x - w * .35 + i * w * .14, y + w / 2, INK)
                   for i in range(6))
    pins += "".join('<path d="M%.1f %.1f h-12 M%.1f %.1f h12" stroke="%s" stroke-width="4"/>'
                    % (x - w / 2, y - w * .35 + i * w * .14, x + w / 2, y - w * .35 + i * w * .14, INK)
                    for i in range(6))
    return ('<g>%s<rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" rx="8" fill="#1b2626" stroke="%s" '
            'stroke-width="4"/><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="none" stroke="%s" '
            'stroke-width="3"/>%s</g>' % (pins, x - w / 2, y - w / 2, w, w, INK, x - w * .3, y - w * .3, w * .6,
                                         w * .6, RED, t(x, y + 12, lab, 32, CREAM, "middle", 700, FT)))


def _ram(x, y, w=200):
    cells = "".join('<rect x="%.1f" y="%.1f" width="%.1f" height="30" fill="#1b2626"/>'
                    % (x - w / 2 + 12 + i * (w - 24) / 6, y - 22, (w - 24) / 6 - 8) for i in range(6))
    pins = "".join('<rect x="%.1f" y="%.1f" width="5" height="12" fill="%s"/>'
                   % (x - w / 2 + 10 + i * 12, y + 26, AMBER) for i in range(int((w - 20) / 12)))
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="62" rx="4" fill="#3b7f5a" stroke="%s" '
            'stroke-width="4"/>%s%s</g>' % (x - w / 2, y - 36, w, INK, cells, pins))


def _fiber(x, y):
    rays = "".join('<path d="M%.1f %.1f q60 %.1f 130 %.1f" stroke="%s" stroke-width="3" fill="none" '
                   'filter="url(#__U___gl)"/>' % (x + 40, y - 12 + i * 6, (i - 2) * 8, (i - 2) * 22, RED)
                   for i in range(5))
    return ('<g><path d="M%.1f %.1f l90 -40 v80 z" fill="#1b2626" stroke="%s" stroke-width="4"/>'
            '<ellipse cx="%.1f" cy="%.1f" rx="16" ry="40" fill="#2b3a39" stroke="%s" stroke-width="4"/>'
            '<circle cx="%.1f" cy="%.1f" r="12" fill="%s" filter="url(#__U___gl)"/>%s</g>'
            % (x - 90, y + 40, INK, x, y, INK, x, y, RED, rays))


def p02():
    b = [bg(102, "dusk", arcs=True, sun=False),
         poster_title("Характеристики протоколов|динамической маршрутизации", None, 30, 12, 64)]
    a = S(card(20, 170, 770, 340, "Скорость сходимости", fs=40),
          ml(60, 270, "Как быстро маршрутизаторы|согласуют новые маршруты", 24, INK, "start", 600),
          '<ellipse cx="460" cy="420" rx="290" ry="70" fill="none" stroke="%s" stroke-width="4" '
          'stroke-dasharray="14 10" filter="url(#__U___gl)"/>' % RED,
          wrouter(180, 430, 130), wrouter(630, 330, 120), wrouter(680, 440, 130), _stopwatch(440, 400, 70))
    c = S(card(810, 170, 770, 340, "Масштабируемость", fs=40),
          t(850, 262, "Работа при росте сети", 24, INK, "start", 600),
          wrouter(900, 360, 90), wrouter(1000, 430, 90), wrouter(880, 470, 90),
          cable(930, 370, 980, 420, "red", 3), cable(920, 455, 960, 440, "red", 3),
          '<path d="M1080 420 h50 v-20 l40 35 l-40 35 v-20 h-50 z" fill="%s" stroke="%s" stroke-width="3"/>' % (RED, INK),
          wrouter(1250, 330, 80), wrouter(1360, 300, 80), wrouter(1480, 340, 80), wrouter(1300, 420, 80),
          wrouter(1420, 410, 80), wrouter(1520, 460, 80), wrouter(1250, 480, 80), wrouter(1380, 490, 80),
          cable(1270, 345, 1340, 320, "red", 2.5), cable(1380, 315, 1460, 345, "red", 2.5),
          cable(1260, 345, 1290, 410, "red", 2.5), cable(1320, 430, 1400, 420, "red", 2.5),
          cable(1440, 420, 1510, 455, "red", 2.5), cable(1300, 435, 1260, 470, "red", 2.5),
          cable(1420, 425, 1390, 480, "red", 2.5), cable(1480, 355, 1430, 400, "red", 2.5))
    d = S(card(20, 530, 770, 340, "Потребление ресурсов", fs=40),
          t(60, 622, "ЦП  •  ОЗУ  •  полоса пропускания", 24, INK, "start", 600),
          _chip(140, 740, .95), t(140, 852, "ЦП", 24, INK, "middle", 700),
          _ram(380, 745, 210), t(380, 852, "ОЗУ", 24, INK, "middle", 700),
          _fiber(620, 730), ml(640, 830, "полоса|пропускания", 22, INK, "middle", 700))
    e = S(card(810, 530, 770, 340, "Настройка и обслуживание", fs=40),
          t(850, 622, "Сложность внедрения и поддержки", 24, INK, "start", 600),
          screen(830, 650, 730, 205, 121, "night"),
          frame(870, 680, 300, 150, "#162423", 4, False), icon(950, 755, "gear", 1.2, "#5ec6d8", False),
          '<rect x="1020" y="715" width="120" height="14" fill="%s"/><rect x="1020" y="745" width="100" '
          'height="10" fill="#7d8c89"/><rect x="1020" y="770" width="110" height="10" fill="#7d8c89"/>' % RED,
          rack(1300, 755, 1.4, 6), rack(1400, 760, 1.3, 6), rack(1500, 755, 1.4, 6))
    a = '<g transform="translate(0 -22)">%s</g>' % a
    c = '<g transform="translate(0 -22)">%s</g>' % c
    d = '<g transform="translate(0 -36)">%s</g>' % d
    e = '<g transform="translate(0 -36)">%s</g>' % e
    fin = S(frame(330, 842, 940, 50, CREAM),
            t(800, 875, "— Сравнение помогает выбрать протокол под размер и задачи сети. —", 25, INK, "middle", 700))
    return finish("".join(b) + a + c + d + e + fin)


# ======================================================================
#  ph06 — КЛАССИФИКАЦИЯ ПО ПРИНЦИПУ РАБОТЫ
# ======================================================================

def _doc(x, y, s=1.0):
    return ('<g><rect x="%.1f" y="%.1f" width="%.1f" height="%.1f" fill="%s" stroke="%s" stroke-width="3"/>'
            '<path d="M%.1f %.1f h%.1f M%.1f %.1f h%.1f M%.1f %.1f h%.1f" stroke="%s" stroke-width="2.5"/></g>'
            % (x - 16 * s, y - 20 * s, 32 * s, 40 * s, CREAM, INK, x - 10 * s, y - 10 * s, 20 * s, x - 10 * s, y,
               20 * s, x - 10 * s, y + 10 * s, 16 * s, INK))


def p06():
    b = [bg(106, "teal", arcs=True, sun=False),
         poster_title("Классификация по принципу работы", None, 30, 18, 70)]

    def col(x, title, cap, proto, seed, body):
        return S(card(x, 120, 500, 690, title, fs=34),
                 screen(x + 14, 190, 472, 390, seed, "dusk" if seed % 2 else "night"),
                 body,
                 t(x + 250, 630, cap, 26, INK, "middle", 700),
                 '<rect x="%d" y="645" width="70" height="5" fill="%s"/>' % (x + 215, RED),
                 frame(x + 40, 680, 420, 100, "#cfe2e2", 4, False),
                 h(x + 250, 748, proto, 46, INK, "middle"))
    dv = (puck(150, 270, 40) + puck(340, 270, 40) + puck(110, 410, 40) + puck(390, 410, 40) +
          puck(250, 500, 40) +
          ar(195, 270, 295, 270, "red", 4, both=True) + ar(130, 315, 115, 365, "red", 4, both=True) +
          ar(375, 315, 390, 365, "red", 4, both=True) + ar(145, 445, 210, 485, "red", 4, both=True) +
          ar(355, 445, 290, 485, "red", 4, both=True) +
          _doc(245, 240, .9) + _doc(90, 340, .9) + _doc(420, 340, .9) + _doc(250, 380, .9) + _doc(400, 470, .9))
    ls = ('<g opacity=".4">%s</g>' % "".join(
        '<path d="M%d 200 V570 M530 %d H980" stroke="%s" stroke-width="1.5"/>' % (540 + i * 40, 200 + i * 40, CYAN)
        for i in range(11)) +
          puck(640, 300, 38) + puck(870, 250, 38) + puck(760, 400, 38) + puck(900, 420, 38) +
          puck(600, 480, 38) + puck(740, 530, 38) +
          cable(680, 300, 830, 255, "red", 4) + cable(660, 320, 730, 390, "red", 4) + cable(800, 400, 865, 415, "red", 4) +
          cable(880, 290, 900, 380, "red", 4) + cable(630, 470, 735, 415, "red", 4) + cable(765, 440, 750, 500, "red", 4) +
          cable(620, 500, 705, 530, "red", 4) + cable(780, 525, 880, 450, "red", 2, glow=False))
    pv = (cloud(1150, 420, 230, 230, "#bfd7ea", 4) + cloud(1400, 410, 220, 230, "#f1c0b5", 4) +
          label(1140, 300, "AS 65001", 18, CREAM) + label(1420, 290, "AS 65002", 18, CREAM) +
          puck(1100, 380, 26) + puck(1180, 440, 26) + puck(1100, 480, 26) +
          cable(1105, 390, 1170, 430, "blue", 3) + cable(1110, 470, 1170, 450, "blue", 3) +
          puck(1290, 440, 24) + puck(1380, 420, 26) + puck(1450, 460, 26) + puck(1400, 500, 26) +
          ar(1205, 440, 1265, 440, "red", 4) + ar(1315, 440, 1355, 425, "red", 4) +
          label(1215, 395, "AS65001", 13, CREAM, INK, True) + label(1290, 395, "AS65010", 13, CREAM, INK, True) +
          label(1370, 370, "AS65002", 13, CREAM, INK, True))
    a = col(30, "Дистанционно-векторные", "Обмен маршрутами с соседями", "RIP", 131, dv)
    c = col(550, "По состоянию канала", "Карта связей и расчёт пути", "OSPF  ·  IS-IS", 132, ls)
    d = col(1070, "По вектору пути", "Путь через автономные системы", "BGP", 133, pv)
    return finish("".join(b) + a + c + d)


# ======================================================================
#  ph04 — КЛАССОВЫЕ И БЕСКЛАССОВЫЕ ПРОТОКОЛЫ
# ======================================================================

def _env(x, y, w, hh, text, red_tail=None, fs=34):
    out = [frame(x, y, w, hh, CREAM, 4, False),
           icon(x + 52, y + hh / 2, "env", .95, INK, False)]
    if red_tail:
        out.append('<text x="%.1f" y="%.1f" font-size="%d" font-weight="700" font-family="%s" fill="%s">%s'
                   '<tspan fill="%s">%s</tspan></text>' % (x + 100, y + hh / 2 + fs * .36, fs, FB, INK, text, RED,
                                                         red_tail))
    else:
        out.append(t(x + 100, y + hh / 2 + fs * .36, text, fs, INK, "start", 700))
    return "".join(out)


def p04():
    b = ['<rect width="1600" height="900" fill="#0d1d1d"/>', city(0, 0, 1600, 900, 104, "teal", sun=False, dim=.7),
         frame(16, 16, 1568, 92, "#0f2523"), poster_title("Классовые и бесклассовые протоколы", None, 30, 24, 66)]

    def side(x, title, seed):
        return (card(x, 125, 770, 520) + panel_head(x, 125, title, 52) +
                screen(x + 14, 205, 742, 300, seed, "teal") +
                '<rect x="%d" y="515" width="742" height="115" fill="%s" stroke="%s" stroke-width="3"/>'
                % (x + 14, CREAM, INK) +
                '<path d="M%d 515v115M%d 515v115" stroke="%s" stroke-width="3"/>' % (x + 260, x + 510, INK))
    L = S(side(20, "Классовые", 141),
          wrouter(170, 420, 250), ar(260, 290, 380, 300, "red", 9),
          _env(390, 250, 340, 90, "192.168.1.0"),
          frame(470, 380, 250, 60, CREAM, 3, False), t(595, 422, "255.255.255.0", 30, INK, "middle", 700),
          '<circle cx="595" cy="410" r="62" fill="none" stroke="%s" stroke-width="10"/>'
          '<path d="M552 367 L638 453" stroke="%s" stroke-width="10"/>' % (RED, RED),
          t(157, 580, "Маска не передаётся", 23, INK, "middle", 700),
          t(405, 580, "RIPv1  •  IGRP", 25, INK, "middle", 700),
          ml(655, 568, "Нет поддержки|VLSM и CIDR", 23, INK, "middle", 700))
    R = S(side(810, "Бесклассовые", 142),
          wrouter(960, 420, 250), ar(1050, 290, 1170, 300, "red", 9),
          _env(1180, 250, 360, 90, "192.168.1.0", "/24"),
          '<path d="M1500 340 L1500 380 L1430 395 Z" fill="%s" opacity=".5"/>' % RED,
          label(1450, 370, "/24", 22, RED, "#fff", w=60, hh=36),
          frame(1180, 400, 360, 74, "#f7cfca", 4, False),
          t(1290, 450, "192.168.1.0", 30, INK, "middle", 700),
          '<rect x="1410" y="410" width="120" height="54" fill="%s"/>' % RED,
          t(1470, 450, "/24", 32, "#fff", "middle", 700, FT),
          t(947, 580, "Префикс передаётся", 23, INK, "middle", 700),
          t(1195, 580, "RIPv2 • OSPFv2 • IS-IS", 23, INK, "middle", 700),
          ml(1445, 568, "Поддержка|VLSM и CIDR", 23, INK, "middle", 700))
    v6 = S(frame(20, 665, 770, 140, CREAM), '<rect x="44" y="700" width="12" height="70" fill="%s"/>' % RED,
           ml(74, 740, "IPv6: длина префикса|передаётся", 30, INK, "start", 700, FT),
           _env(420, 690, 350, 90, "2001:db8::", "/64", 32))
    ec = S(frame(810, 665, 770, 140, CREAM), '<rect x="834" y="700" width="12" height="70" fill="%s"/>' % RED,
           ml(864, 728, "ECMP: несколько путей|равной стоимости", 30, INK, "start", 700, FT),
           puck(1240, 735, 44), ar(1290, 720, 1430, 705, "red", 6, curve=20), ar(1290, 750, 1430, 765, "red", 6,
                                                                                   curve=-20),
           cloud(1500, 735, 140, 100, CREAM2, 4))
    return finish("".join(b) + L + R + v6 + ec)


# ======================================================================
#  ph12, ph13 — ИСТОРИЯ ПРОТОКОЛОВ
# ======================================================================

def _yearcard(x, y, year, name, cap, seed, body, circle=True):
    out = [frame(x, y, 270, 260, CREAM), screen(x + 12, y + 90, 246, 120 if cap else 160, seed, "dusk", sun=True)]
    if circle:
        out.append('<circle cx="%d" cy="%d" r="44" fill="%s" stroke="%s" stroke-width="4"/>' % (x + 46, y + 44, RED, INK))
        out.append(t(x + 46, y + 56, year, 30 if len(year) <= 4 else 22, "#fff", "middle", 700, FT))
        out.append(t(x + 175, y + 64, name, 46, INK, "middle", 700, FT))
    else:
        out.append(t(x + 20, y + 44, year, 42, RED, "start", 700, FT))
        out.append(t(x + 20, y + 82, name, 34, INK, "start", 700, FT))
    out.append(body)
    if cap:
        out.append(strip(x + 12, y + 210, 246, cap.split("|")[0], 17, 40) if "|" not in cap else
                   '<rect x="%d" y="%d" width="246" height="40" fill="%s" stroke="%s" stroke-width="3"/>'
                   % (x + 12, y + 210, CREAM, INK) + ml(x + 135, y + 226, cap, 15, INK, "middle", 700, FB, 1.1))
    return "".join(out)


def _arrowbox(x, y):
    return ('<path d="M%d %d h18 v-16 l26 28 l-26 28 v-16 h-18 z" fill="%s" stroke="%s" stroke-width="3"/>'
            % (x, y - 12, RED, INK))


def p12():
    b = [bg(112, "dusk", arcs=True, sun=True), poster_title("История протоколов|маршрутизации", None, 30, 14, 84),
         ml(1560, 52, "ОТ ПЕРВЫХ|МАРШРУТОВ|К СОВРЕМЕННЫМ|СЕТЯМ", 17, CREAM, "end", 700)]
    xs = [20, 335, 650, 965, 1280]
    items = [
        ("1984", "EGP", "Между автономными|системами",
         '<path d="M80 340 Q150 250 220 330" fill="none" stroke="%s" stroke-width="4" filter="url(#__U___gl)"/>' % RED +
         dot(80, 340, 8) + dot(220, 330, 8)),
        ("1980-е", "IGRP", "Внутри автономной|системы",
         puck(470, 325, 24) + puck(410, 375, 24) + puck(530, 375, 24) + puck(470, 405, 22) +
         cable(450, 340, 420, 360, "red", 3) + cable(490, 340, 520, 360, "red", 3)),
        ("1988", "RIP", "Обмен маршрутами|между соседями",
         puck(785, 315, 24) + puck(725, 370, 24) + puck(845, 370, 24) + puck(785, 405, 22) +
         ar(765, 325, 740, 350, "red", 3, both=True) + ar(805, 325, 830, 350, "red", 3, both=True)),
        ("1993", "RIPv2", "Поддержка бесклассовой|адресации",
         puck(1100, 380, 30) + ar(1100, 345, 1100, 305, "red", 4) + ar(1060, 370, 1010, 350, "red", 4) +
         ar(1140, 370, 1190, 350, "red", 4) + ar(1070, 395, 1020, 410, "red", 4) + ar(1130, 395, 1180, 410, "red", 4)),
        ("1997", "RIPng", "Маршрутизация IPv6",
         '<circle cx="1415" cy="350" r="56" fill="none" stroke="%s" stroke-width="3"/>' % CREAM +
         t(1415, 362, "IPv6", 34, CREAM, "middle", 700, FT) + puck(1415, 400, 28)),
    ]
    cards = []
    for i, (yr, nm, cap, body) in enumerate(items):
        cards.append(S(_yearcard(xs[i], 250, yr, nm, cap, 150 + i,
                                 '<g transform="translate(0 42)">%s</g>' % body)))
        if i < 4:
            cards.append(S(_arrowbox(xs[i] + 274, 400)))
    foot = S(frame(20, 760, 470, 110, "#0f2523"), icon(90, 815, "books", 1.2, CREAM, False),
             h(150, 805, "Основа RIP:", 30, CREAM), t(150, 845, "алгоритм Беллмана — Форда", 26, CREAM, "start", 600),
             frame(1180, 760, 400, 110, "#0f2523"), icon(1240, 815, "gear", 1.2, RED, False),
             h(1300, 805, "ESR:", 30, CREAM), t(1300, 845, "RIPv2 и RIPng", 26, CREAM, "start", 600))
    return finish("".join(b) + "".join(cards) + foot)


def p13():
    b = ['<rect width="1600" height="900" fill="#173533"/>', city(0, 520, 1600, 380, 113, "night", sun=False, dim=.6),
         poster_title("История протоколов|маршрутизации", None, 30, 14, 84)]
    xs = [20, 335, 650, 965, 1280]

    def tri(cx, cy, r=22):
        return (puck(cx, cy - 30, r) + puck(cx - 70, cy + 20, r) + puck(cx + 70, cy + 20, r) +
                cable(cx - 20, cy - 20, cx - 55, cy + 10, "red", 3) + cable(cx + 20, cy - 20, cx + 55, cy + 10, "red", 3))
    globe = ('<circle cx="1100" cy="380" r="62" fill="#1b2a2a" stroke="%s" stroke-width="3"/>' % INK +
             '<path d="M1038 380h124M1100 318c25 20 25 104 0 124M1100 318c-25 20-25 104 0 124M1048 350h104M1048 410h104" '
             'stroke="%s" stroke-width="2.5" fill="none" filter="url(#__U___gl)"/>' % RED +
             dot(1070, 350, 6) + dot(1135, 400, 6) + dot(1120, 335, 6))
    items = [("1989", "OSPF", tri(150, 380)), ("1991", "OSPFv2", tri(465, 380)),
             ("1992", "IS-IS", tri(780, 380) + puck(780, 410, 20) + cable(780, 365, 780, 395, "red", 3)),
             ("1994", "BGPv4", globe), ("1999", "OSPFv3", tri(1410, 380))]
    cards = []
    for i, (yr, nm, body) in enumerate(items):
        cards.append(S(_yearcard(xs[i], 180, yr, nm, None, 160 + i, body, circle=False)))
        if i < 4:
            cards.append(S(_arrowbox(xs[i] + 274, 320)))
    tags_ = S(frame(20, 465, 770, 56, CREAM), '<rect x="34" y="476" width="10" height="34" fill="%s"/>' % RED,
              h(60, 505, "OSPF и IS-IS — внутри автономной системы", 28, INK),
              frame(810, 465, 770, 56, CREAM), '<rect x="824" y="476" width="10" height="34" fill="%s"/>' % RED,
              h(850, 505, "BGP — между автономными системами", 28, INK))
    as1 = (cloud(420, 720, 520, 260, "#2b4746", 4) + h(380, 640, "AS 1", 36, CREAM, "middle") +
           puck(300, 760, 32) + puck(420, 700, 32) + puck(400, 820, 32) + puck(540, 770, 32) +
           cable(330, 750, 390, 710, "red", 3) + cable(330, 770, 370, 810, "red", 3) +
           cable(450, 710, 510, 760, "red", 3) + cable(430, 820, 510, 780, "red", 3) + cable(420, 735, 405, 795, "red", 3))
    as2 = (cloud(1180, 720, 520, 260, "#2b4746", 4) + h(1140, 640, "AS 2", 36, CREAM, "middle") +
           puck(1050, 770, 32) + puck(1180, 700, 32) + puck(1160, 820, 32) + puck(1300, 770, 32) +
           cable(1080, 760, 1150, 710, "red", 3) + cable(1080, 780, 1130, 815, "red", 3) +
           cable(1210, 710, 1270, 760, "red", 3) + cable(1190, 820, 1270, 780, "red", 3))
    link_ = cable(640, 740, 960, 740, "red", 5) + dot(640, 740, 10) + dot(960, 740, 10)
    nb = (frame(40, 650, 230, 76, CREAM, 3, False),
          '<rect x="50" y="660" width="8" height="56" fill="%s"/>' % RED,
          ml(70, 682, "Алгоритм Дейкстры|→ кратчайший путь", 20, INK, "start", 700),
          ar(270, 700, 290, 745, "cream", 3),
          frame(1340, 600, 240, 110, CREAM, 3, False),
          '<rect x="1350" y="612" width="8" height="86" fill="%s"/>' % RED,
          ml(1370, 632, "IPv6:|OSPFv3,|расширения BGP, IS-IS", 19, INK, "start", 700),
          ar(1340, 680, 1320, 750, "cream", 3))
    return finish("".join(b) + "".join(cards) + tags_ + S(as1, as2, link_) + S(*nb))


# ======================================================================
#  ph14 — ПЛАВАЮЩИЙ ДИНАМИЧЕСКИЙ МАРШРУТ
# ======================================================================

def p14():
    b = [bg(114, "dusk", arcs=False, sun=True), poster_title("Плавающий динамический маршрут", None, 30, 14, 76)]
    rip = S(frame(30, 125, 470, 330, CREAM), t(60, 185, "RIP · preference 100", 38, INK, "start", 700, FT),
            screen(46, 205, 438, 234, 171, "dusk", sun=True),
            puck(240, 345, 68, tone="blue"))
    ospf = S(frame(830, 125, 470, 330, CREAM),
             '<text x="860" y="185" font-size="38" font-weight="700" font-family="%s" fill="%s">OSPF · preference '
             '<tspan fill="%s">5</tspan></text>' % (FT, INK, RED),
             screen(846, 205, 438, 234, 172, "dusk", sun=True),
             puck(1060, 345, 68, tone="red"))
    box = S(frame(1320, 125, 260, 270, CREAM), ml(1450, 170, "До настройки:|OSPF 150", 26, INK, "middle", 700, FT),
            frame(1350, 225, 200, 54, CREAM2, 3, False), t(1450, 262, "150", 32, INK, "middle", 700, FT),
            '<path d="M1450 285 v30" stroke="%s" stroke-width="10"/><path d="M1430 310 l20 22 l20 -22 z" fill="%s"/>'
            % (RED, RED),
            frame(1350, 330, 200, 54, RED, 3, False), t(1450, 367, "5", 34, "#fff", "middle", 700, FT))
    mid = S(cloud(665, 205, 290, 160, CREAM2, 4), ml(665, 222, "Удалённая сеть|192.168.10.0/24", 22, INK, "middle", 700),
            ar(500, 340, 640, 290, "blue", 6, curve=40, dash=True),
            ar(830, 340, 700, 290, "red", 7, curve=40))
    r1 = S(wrouter(665, 575, 300, "R1", ants=4, labfs=26),
           cable(560, 545, 470, 440, "blue", 4, True), cable(770, 545, 900, 440, "red", 5),
           ar(1300, 470, 1180, 450, "red", 8, curve=-30),
           label(1270, 520, "Выбран: меньшее preference", 26, RED, "#fff"))
    term = S(terminal(30, 705, 760, 115, ["R1(config)# ip protocols ospf preference 5"], 26),
             terminal(810, 705, 760, 115, ["R1#  show ip route all"], 26))
    fin = S(frame(30, 835, 1540, 56, CREAM), '<rect x="50" y="846" width="10" height="34" fill="%s"/>' % RED,
            h(80, 875, "Для маршрутов к одной сети предпочтительнее источник с меньшим preference.", 30, INK))
    return finish("".join(b) + rip + ospf + box + mid + r1 + term + fin)


# ======================================================================
#  ph15 — RIB → ВЫБОР → FIB
# ======================================================================

def _pslant(x, y, w, hh, seed):
    """Скошенная кремовая панель с городом внутри."""
    return (city(x, y, w, hh, seed, "dusk", sun=False, dim=.45) +
            '<path d="M%d %d h%d l-30 %d h-%d z" fill="%s" opacity=".9" stroke="%s" stroke-width="4"/>'
            % (x + 20, y + 10, w - 20, hh - 20, w - 50, CREAM, INK))


def p15():
    b = [bg(115, "dusk", arcs=False, sun=True), poster_title("Динамические маршруты", None, 30, 14, 84)]
    rib = S(_pslant(20, 120, 520, 330, 181), h(270, 185, "RIB", 56, INK, "middle"),
            t(270, 222, "Все известные маршруты", 24, INK, "middle", 600),
            puck(90, 360, 32), puck(450, 360, 32),
            '<path d="M120 345 Q270 250 420 345" fill="none" stroke="%s" stroke-width="5"/>' % RED,
            '<path d="M120 360 H420" fill="none" stroke="%s" stroke-width="5"/>' % "#4aa3d6",
            '<path d="M120 375 Q270 460 420 375" fill="none" stroke="%s" stroke-width="5"/>' % GREEN,
            puck(270, 300, 24), puck(220, 360, 22), puck(320, 360, 22), puck(270, 415, 24))
    sel = S(ar(545, 290, 590, 290, "red", 14),
            _pslant(570, 120, 460, 330, 182), h(800, 185, "Выбор лучших", 44, INK, "middle"),
            ar(620, 270, 680, 290, "red", 5), ar(620, 310, 680, 310, "blue", 5), ar(620, 350, 680, 330, "green", 5),
            icon(745, 310, "gear", 2.6, INK, False),
            frame(830, 255, 150, 44, CREAM, 3, False), t(905, 284, "Preference", 21, INK, "middle", 700),
            frame(830, 340, 150, 44, CREAM, 3, False), t(905, 369, "Cost", 21, INK, "middle", 700),
            '<path d="M790 300 h30 v-23 h10 M790 320 h30 v42 h10" fill="none" stroke="%s" stroke-width="3"/>' % INK)
    fib = S(ar(1035, 290, 1080, 290, "red", 14),
            _pslant(1060, 120, 420, 330, 183), h(1270, 185, "FIB", 56, INK, "middle"),
            t(1270, 222, "Маршруты для пересылки", 22, INK, "middle", 600),
            puck(1130, 340, 30), puck(1270, 340, 26), puck(1400, 340, 30),
            cable(1160, 340, 1245, 340, "red", 5), cable(1295, 340, 1370, 340, "red", 5),
            ar(1450, 300, 1500, 300, "red", 14),
            '<path d="M1505 250 h65 l15 15 v80 h-80 z" fill="%s" stroke="%s" stroke-width="3"/>' % (CREAM, INK),
            ml(1545, 290, "IP-|пакет", 22, INK, "middle", 700, FT))
    topo = S(frame(20, 470, 1560, 270, "#173332"), city(24, 474, 1552, 262, 184, "teal", sun=False, dim=.7),
             label(240, 510, "Изменение топологии", 28, CREAM),
             puck(110, 640, 40), puck(560, 640, 40), puck(260, 580, 24), xcross(400, 580, 22), puck(260, 690, 24),
             puck(400, 690, 24),
             '<path d="M150 630 L240 585 M280 580 H380" stroke="#6f8d88" stroke-width="4" stroke-dasharray="10 8"/>',
             '<path d="M150 650 L240 685 H380 L520 650" stroke="%s" stroke-width="5" fill="none" '
             'filter="url(#__U___gl)"/>' % RED,
             '<path d="M640 620 h40 v-20 l40 38 l-40 38 v-20 h-40 z" fill="%s" stroke="%s" stroke-width="3"/>' % (RED, INK),
             label(1060, 510, "Новый лучший путь", 28, CREAM),
             puck(830, 640, 40), puck(1360, 640, 40), puck(1000, 580, 24), puck(1180, 580, 24),
             puck(1000, 690, 24), puck(1180, 690, 24),
             '<path d="M870 630 L975 585 H1155 L1320 630" stroke="#6f8d88" stroke-width="4" fill="none" '
             'stroke-dasharray="10 8"/>',
             '<path d="M870 650 L975 685 H1155 L1320 650" stroke="%s" stroke-width="5" fill="none" '
             'filter="url(#__U___gl)"/>' % RED)
    term = S(terminal(20, 760, 1560, 125, [("ESR# ", "config"), ("ESR(config)# ", "router ?")], 26))
    return finish("".join(b) + rib + sel + fib + topo + term)
