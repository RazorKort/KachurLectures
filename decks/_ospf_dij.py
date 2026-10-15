# -*- coding: utf-8 -*-
"""Блок «Алгоритм Дейкстры и стоимость» в стиле инфографик методички."""

from _ospf_lib import (slide, head, sc, card, step, steps, irow, foot, tag, tags, table,
                       router, arrow, link, pill, txt, ok, ban,
                       blob, cloud_icon, legend, bubble, sparkle,
                       rowc, nrow, tile, split, ill, mini, panel, mark, ICON)

W = 128
POS = {"R1": (175, 225), "R5": (825, 225), "R3": (500, 395), "R2": (175, 575), "R4": (825, 575)}
EDGES = [("R1", "R2", 8), ("R1", "R3", 10), ("R1", "R5", 15), ("R2", "R3", 11),
         ("R2", "R4", 16), ("R3", "R4", 12), ("R3", "R5", 3), ("R4", "R5", 16)]
TONE = {"R1": "p", "R2": "p", "R3": "b", "R4": "b", "R5": "b"}


def anchor(n):
    x, y = POS[n]
    return x, y + W * 0.14


def key(a, b):
    return "".join(sorted([a, b]))


def dgraph(marks, status=None, visited=(), active=None, tree=(), hot=(), anim_edges=(), new_marks=None):
    """Граф методички из роутеров-шайб.
    marks: {'R1': '0'}; status: {'R1': 'посещена'}; tree/hot/anim_edges: множества пар;
    new_marks: {'R4': ('22', 'обновлена')} — появляются анимацией поверх старой метки."""
    status = status or {}
    new_marks = new_marks or {}
    tree = {key(*e) for e in tree}
    hot = {key(*e) for e in hot}
    anim = {key(*e) for e in anim_edges}
    out = [blob(500, 380, 470, 300, "b", None, seed=1.3, dash=True)]
    for a, b, w in EDGES:
        (x1, y1), (x2, y2) = anchor(a), anchor(b)
        k = key(a, b)
        if k in tree:
            out.append('<path d="M%.0f %.0f L%.0f %.0f" stroke="#ffe9a8" stroke-width="22" stroke-linecap="round"/>'
                       '<path d="M%.0f %.0f L%.0f %.0f" stroke="#f2b705" stroke-width="8" stroke-linecap="round"/>'
                       % (x1, y1, x2, y2, x1, y1, x2, y2))
        else:
            out.append(link(x1, y1, x2, y2, 5, "#7d9cc0"))
        if k in hot:
            cls = "dedge go-f" if k in anim else ""
            out.append('<g class="%s"><path d="M%.0f %.0f L%.0f %.0f" stroke="#ff5c9e" stroke-width="9" '
                       'stroke-linecap="round" stroke-dasharray="20 12"/></g>' % (cls, x1, y1, x2, y2))
    for a, b, w in EDGES:
        (x1, y1), (x2, y2) = anchor(a), anchor(b)
        mx, my = (x1 + x2) / 2.0, (y1 + y2) / 2.0
        if x1 == x2:
            mx, my = mx + (-48 if x1 < 500 else 48), my + 30
        out.append('<circle cx="%.0f" cy="%.0f" r="24" fill="#fff" stroke="#7d9cc0" stroke-width="2.6"/>' % (mx, my))
        out.append(txt(mx, my + 8, str(w), fs=22, weight=900))
    for n, (x, y) in POS.items():
        if n == active:
            out.append('<ellipse class="dhalo go-f" cx="%d" cy="%d" rx="96" ry="58" fill="#ffd93d" opacity=".45"/>'
                       % (x, y + 18))
        tone = "g" if n in visited else TONE[n]
        out.append(router(x, y, W, "gr" if n in visited else tone, label=n))
        if n in visited:
            out.append(ok(x + 70, y - 6, 17))
    for n, (x, y) in POS.items():
        v = marks.get(n, "∞")
        st = status.get(n, "не посещена" if n not in visited else "посещена")
        mt = "g" if n in visited else ("y" if n == active or st == "следующая" else ("p" if v != "∞" else "w"))
        out.append(mark(x, y - 130, v, st, mt))
        if n in new_marks:
            nv, ns = new_marks[n]
            out.append('<g class="dlabel go-f">%s</g>' % mark(x, y - 130, nv, ns, "y"))
    return "".join(out)


def calc(text, res, keep=False):
    return ('<div class="calc dcalc go-f%s"><span class="ar">&#10140;</span><span>%s</span><span class="r">%s</span></div>'
            % (" keep" if keep else "", text, res))


def marks_table(rows):
    return table(["Вершина", "Метка", "Через", "Статус"],
                 [(r, "hi") if r[3] == "следующая" else r for r in rows])


def step_slide(label, title, sub, gargs, calcs, rows, fin):
    slide(label, sc(
        head(title, sub),
        split(
            ill("0 0 1000 680", dgraph(**gargs)),
            panel("route", "Проверяем соседей", "".join(calcs), "y") +
            step(panel("doc", "Таблица меток", marks_table(rows), "b")) +
            '<div class="dfin go-f">' + rowc("ok", "Итог шага", fin, "g") + '</div>',
            "56fr 44fr")
    ), scen="dij")


def build():
    # ------------------------------------------------------------ 1. алгоритм: принцип
    slide("Алгоритм Дейкстры", sc(
        head("Алгоритм Дейкстры", "Как маршрутизатор строит дерево кратчайших путей SPF. Эдсгер Дейкстра, 1959 год."),
        split(
            steps(
                nrow("1", "Старт", mini("0 0 80 64", '<circle cx="40" cy="32" r="22" fill="#ff5c9e"/>'
                     + txt(40, 40, "0", fs=22, color="#fff", weight=900)),
                     "Корень — сам маршрутизатор: его метка <b>0</b>, у всех остальных вершин <b>∞</b>.", "p"),
                nrow("2", "Выбор", mini("0 0 80 64", '<circle cx="40" cy="32" r="22" fill="#ffd93d"/>'
                     + '<path d="M30 32 l8 8 l14 -16" stroke="#121212" stroke-width="5" fill="none"/>'),
                     "Берём непосещённую вершину с <b>наименьшей</b> меткой.", "y"),
                nrow("3", "Пересчёт", mini("0 0 80 64", txt(40, 40, "8+11", fs=18, weight=900)),
                     "Для каждого непосещённого соседа: <b>метка + вес ребра</b>. Меньше текущей метки — заменяем.", "b"),
                nrow("4", "Отметка", mini("0 0 80 64", '<circle cx="40" cy="32" r="22" fill="#3fc47c"/>'
                     + '<path d="M30 32 l8 8 l14 -16" stroke="#fff" stroke-width="5" fill="none"/>'),
                     "Все соседи проверены — вершина <b>посещена</b>, её метка окончательная.", "g"),
                nrow("5", "Повтор", mini("0 0 80 64", '<path d="M18 32 a22 22 0 1 1 8 17" stroke="#9b7bf0" '
                     'stroke-width="5" fill="none"/><path d="M14 46 l12 4 l2 -12" stroke="#9b7bf0" stroke-width="5" fill="none"/>'),
                     "Шаги 2–4 повторяются, пока не будут посещены все вершины.", "v")),
            ill("0 0 1000 680", dgraph({"R1": "0"}, {"R1": "корень"}, active="R1")),
            "46fr 54fr"),
        step(foot("<b>Правило обновления метки:</b> метка соседа меняется, только если новый путь <b>короче</b> текущего. "
                  "Метка никогда не растёт — поэтому в дереве SPF не бывает петель.", "note"))
    ))

    # ------------------------------------------------------------ 2. граф задачи
    slide("Граф задачи", sc(
        head("Исходные данные", "Пять маршрутизаторов, восемь каналов. Вес ребра — стоимость канала. Считаем пути от R1."),
        split(
            ill("0 0 1000 680", dgraph({"R1": "0"}, {"R1": "корень"})),
            panel("doc", "Веса рёбер",
                  table(["Канал", "Вес", "Канал", "Вес"],
                        [["R1 — R2", ("8", "c"), "R2 — R4", ("16", "c")],
                         ["R1 — R3", ("10", "c"), "R3 — R4", ("12", "c")],
                         ["R1 — R5", ("15", "c"), "R3 — R5", ("3", "c")],
                         ["R2 — R3", ("11", "c"), "R4 — R5", ("16", "c")]]), "b") +
            step(panel("star", "Начальные метки",
                       '<p>Корень R1 получает метку <b>0</b>. Расстояние до остальных пока неизвестно — '
                       'их метки равны <b>∞</b>.</p>' +
                       tags(tag("R1 = 0", "g"), tag("R2 = ∞", "w"), tag("R3 = ∞", "w"), tag("R4 = ∞", "w"),
                            tag("R5 = ∞", "w")), "p")) +
            step(rowc("bulb", "Граф = сеть",
                      "Вершины — маршрутизаторы, рёбра — каналы, вес — стоимость канала OSPF.", "y")),
            "56fr 44fr")
    ))

    # ------------------------------------------------------------ 3–7. шаги
    step_slide("Дейкстра: шаг 1", "Дейкстра: первый шаг", "Стартуем из R1 и обновляем метки его соседей R2, R3, R5.",
               dict(marks={"R1": "0"}, status={"R1": "текущая"}, active="R1",
                    hot=[("R1", "R2"), ("R1", "R3"), ("R1", "R5")],
                    anim_edges=[("R1", "R2"), ("R1", "R3"), ("R1", "R5")],
                    new_marks={"R2": ("8", "следующая"), "R3": ("10", "обновлена"), "R5": ("15", "обновлена")}),
               [calc("<b>R2:</b> 0 + 8 = 8 &lt; ∞", "8"), calc("<b>R3:</b> 0 + 10 = 10 &lt; ∞", "10"),
                calc("<b>R5:</b> 0 + 15 = 15 &lt; ∞", "15")],
               [["R1", "0", "—", "посещена"], ["R2", "8", "R1", "следующая"], ["R3", "10", "R1", "не посещена"],
                ["R4", "∞", "—", "не посещена"], ["R5", "15", "R1", "не посещена"]],
               "Соседи R1 проверены — помечаем <b>R1 посещённой</b>. Следующая вершина — <b>R2</b>: её метка 8 минимальна.")

    step_slide("Дейкстра: шаг 2", "Дейкстра: второй шаг", "Раскрываем R2 с меткой 8. Соседи: R1 (посещена), R3, R4.",
               dict(marks={"R1": "0", "R2": "8", "R3": "10", "R5": "15"}, status={"R2": "текущая"},
                    visited=["R1"], active="R2", tree=[("R1", "R2")],
                    hot=[("R2", "R3"), ("R2", "R4")], anim_edges=[("R2", "R3"), ("R2", "R4")],
                    new_marks={"R4": ("24", "обновлена"), "R3": ("10", "следующая")}),
               [calc("<b>R3:</b> 8 + 11 = 19 ≥ 10 — оставляем", "10", True),
                calc("<b>R4:</b> 8 + 16 = 24 &lt; ∞", "24")],
               [["R1", "0", "—", "посещена"], ["R2", "8", "R1", "посещена"], ["R3", "10", "R1", "следующая"],
                ["R4", "24", "R2", "не посещена"], ["R5", "15", "R1", "не посещена"]],
               "Путь до R3 через R2 длиннее известного — метка 10 остаётся. R2 посещена, следующая — <b>R3</b> (10).")

    step_slide("Дейкстра: шаг 3", "Дейкстра: третий шаг", "Раскрываем R3 с меткой 10. Непосещённые соседи: R4 и R5.",
               dict(marks={"R1": "0", "R2": "8", "R3": "10", "R4": "24", "R5": "15"}, status={"R3": "текущая"},
                    visited=["R1", "R2"], active="R3", tree=[("R1", "R2"), ("R1", "R3")],
                    hot=[("R3", "R4"), ("R3", "R5")], anim_edges=[("R3", "R4"), ("R3", "R5")],
                    new_marks={"R4": ("22", "обновлена"), "R5": ("13", "следующая")}),
               [calc("<b>R4:</b> 10 + 12 = 22 &lt; 24", "22"), calc("<b>R5:</b> 10 + 3 = 13 &lt; 15", "13")],
               [["R1", "0", "—", "посещена"], ["R2", "8", "R1", "посещена"], ["R3", "10", "R1", "посещена"],
                ["R4", "22", "R3", "не посещена"], ["R5", "13", "R3", "следующая"]],
               "Обе метки улучшились. R3 посещена, следующая — <b>R5</b> с меткой 13.")

    step_slide("Дейкстра: шаг 4", "Дейкстра: четвёртый шаг", "Раскрываем R5 с меткой 13. Непосещённый сосед один — R4.",
               dict(marks={"R1": "0", "R2": "8", "R3": "10", "R4": "22", "R5": "13"}, status={"R5": "текущая"},
                    visited=["R1", "R2", "R3"], active="R5", tree=[("R1", "R2"), ("R1", "R3"), ("R3", "R5")],
                    hot=[("R4", "R5")], anim_edges=[("R4", "R5")],
                    new_marks={"R4": ("22", "следующая")}),
               [calc("<b>R4:</b> 13 + 16 = 29 ≥ 22 — оставляем", "22", True)],
               [["R1", "0", "—", "посещена"], ["R2", "8", "R1", "посещена"], ["R3", "10", "R1", "посещена"],
                ["R4", "22", "R3", "следующая"], ["R5", "13", "R3", "посещена"]],
               "R5 посещена. Осталась <b>R4</b> с меткой 22.")

    step_slide("Дейкстра: шаг 5", "Дейкстра: пятый шаг", "Раскрываем R4 с меткой 22. Все её соседи уже посещены.",
               dict(marks={"R1": "0", "R2": "8", "R3": "10", "R4": "22", "R5": "13"}, status={"R4": "текущая"},
                    visited=["R1", "R2", "R3", "R5"], active="R4",
                    tree=[("R1", "R2"), ("R1", "R3"), ("R3", "R5"), ("R3", "R4")]),
               [calc("<b>R2, R3, R5</b> — уже посещены, пересчёт не нужен", "—", True)],
               [["R1", "0", "—", "посещена"], ["R2", "8", "R1", "посещена"], ["R3", "10", "R1", "посещена"],
                ["R4", "22", "R3", "посещена"], ["R5", "13", "R3", "посещена"]],
               "Все вершины посещены — <b>алгоритм завершён</b>. В методичке шаги 4 и 5 идут в порядке R4 → R5; "
               "по правилу минимальной метки корректнее R5 (13), затем R4 (22). Итог тот же.")

    # ------------------------------------------------------------ 8. дерево SPF и итог
    tree_svg = (blob(500, 380, 470, 300, "b", None, seed=1.3) +
                "".join('<path class="sdrop fade30" d="M%.0f %.0f L%.0f %.0f" stroke="#7d9cc0" stroke-width="5" '
                        'stroke-linecap="round"/>' % (anchor(a) + anchor(b))
                        for a, b, w in EDGES if key(a, b) not in {"R1R2", "R1R3", "R3R5", "R3R4"}) +
                "".join('<path class="sgrow dash" style="--L:420" d="M%.0f %.0f L%.0f %.0f" stroke="#f2b705" '
                        'stroke-width="12" stroke-linecap="round"/>' % (anchor(a) + anchor(b))
                        for a, b in (("R1", "R2"), ("R1", "R3"), ("R3", "R5"), ("R3", "R4"))) +
                "".join(router(x, y, W, "p" if n == "R1" else "gr", label=n) for n, (x, y) in POS.items()) +
                "".join('<g class="snode go-f">%s</g>' % mark(POS[n][0], POS[n][1] - 104, v, s, "g" if n != "R1" else "p")
                        for n, v, s in (("R1", "0", "корень"), ("R2", "8", "R1 → R2"), ("R3", "10", "R1 → R3"),
                                        ("R5", "13", "R1 → R3 → R5"), ("R4", "22", "R1 → R3 → R4"))))
    slide("Дерево SPF", sc(
        head("Результат: дерево кратчайших путей", "Из корня прорастают только рёбра кратчайших путей, остальные связи бледнеют."),
        split(
            ill("0 0 1000 680", tree_svg),
            panel("tree", "Кратчайшие пути от R1",
                  table(["Куда", "Стоимость", "Путь", "Следующий переход"],
                        [["R2", ("8", "c"), "R1 → R2", ("R2", "c")],
                         ["R3", ("10", "c"), "R1 → R3", ("R3", "c")],
                         ["R5", ("13", "c"), "R1 → R3 → R5", ("R3", "c")],
                         ["R4", ("22", "c"), "R1 → R3 → R4", ("R3", "c")]]), "y") +
            step(rowc("doc", "В таблицу маршрутизации",
                      "Записывается не вся цепочка, а <b>стоимость</b> и <b>следующий переход</b>: «до R4 — через R3, cost 22».", "b")) +
            step(rowc("stop", "Отброшено",
                      "Связи R1–R5, R2–R3, R2–R4, R4–R5 существуют физически, но через них путь длиннее.", "p")) +
            step(rowc("swap", "У каждого своё дерево",
                      "LSDB в области одна, но каждый маршрутизатор ставит в корень себя.", "g")),
            "56fr 44fr")
    ), scen="spf")

    # ------------------------------------------------------------ 9. стоимость (как r04)
    Wc = 150
    rr = {"R1": (150, 250), "R2": (500, 250), "R3": (850, 250)}
    ex = (cloud_icon(330, 90, .9) + cloud_icon(720, 80, .8) + sparkle(960, 60) +
          link(150, 271, 850, 271, 8, "#7d9cc0") +
          "".join(router(x, y, Wc, "b" if n == "R2" else "p", label=n) for n, (x, y) in rr.items()) +
          '<rect x="60" y="40" width="180" height="70" rx="16" fill="#ffd3e4"/>' +
          txt(150, 70, "Сеть", fs=22, weight=800) + txt(150, 98, "назначения", fs=22, weight=800) +
          link(150, 110, 150, 180, 3, "#121212") +
          '<g class="cmk go-f"><circle cx="325" cy="271" r="38" fill="#fff" stroke="#7d9cc0" stroke-width="3"/>' +
          txt(325, 283, "10", fs=32, weight=900) + txt(325, 340, "10 Мбит/с", fs=18, color="#56606b") + '</g>' +
          '<g class="cmk go-f"><circle cx="675" cy="271" r="38" fill="#fff" stroke="#7d9cc0" stroke-width="3"/>' +
          txt(675, 283, "64", fs=32, weight=900) + txt(675, 340, "1,544 Мбит/с", fs=18, color="#56606b") + '</g>' +
          '<rect x="40" y="390" width="920" height="170" rx="24" fill="#fde7f0"/>' +
          txt(500, 432, "Стоимость маршрута = сумма стоимостей интерфейсов", fs=24, weight=800) +
          '<rect x="250" y="452" width="500" height="86" rx="20" fill="#ffe9a8"/>' +
          '<g class="cterm go-f">' + txt(330, 515, "10", fs=52, weight=900) + '</g>' +
          '<g class="cterm go-f">' + txt(395, 515, "+", fs=52, weight=900) + txt(450, 515, "1", fs=52, weight=900) + '</g>' +
          '<g class="cterm go-f">' + txt(505, 515, "+", fs=52, weight=900) + txt(575, 515, "64", fs=52, weight=900) + '</g>' +
          '<g class="ctot go-f">' + txt(645, 515, "=", fs=52, weight=900) + txt(705, 515, "75", fs=52, weight=900, color="#d8276f") + '</g>')
    formula = (
        '<div style="display:grid;grid-template-columns:auto auto 1fr;align-items:center;gap:16px;'
        'background:#fff;border-radius:20px;padding:16px">'
        '<div style="background:#ffd3e4;border-radius:18px;padding:16px 20px;font:800 clamp(18px,1.6vw,32px)/1.15 var(--f);'
        'text-align:center">Стоимость<br>интерфейса</div>'
        '<div class="big">=</div>'
        '<div style="display:flex;flex-direction:column;gap:8px">'
        '<div style="background:#c7e2fb;border-radius:14px;padding:10px;text-align:center;font:800 clamp(15px,1.3vw,26px)/1.2 var(--f)">'
        'эталонная пропускная способность</div>'
        '<div style="height:4px;background:#121212;border-radius:2px"></div>'
        '<div style="background:#ffe9a8;border-radius:14px;padding:10px;text-align:center;font:800 clamp(15px,1.3vw,26px)/1.2 var(--f)">'
        'пропускная способность интерфейса</div></div></div>')
    slide("Стоимость OSPF", sc(
        head("Стоимость OSPF", "Метрика выбора кратчайшего маршрута."),
        '<div class="row2 fill" style="grid-template-rows:minmax(0,1fr)">' +
        panel("gear", "Формула расчёта стоимости интерфейса OSPF",
              formula +
              rowc("bulb", "Эталон по умолчанию",
                   "Эталонная пропускная способность — <b>100 Мбит/с</b>. Её можно изменить, но одинаково на всех маршрутизаторах.", "y") +
              rowc("net", "У каждого интерфейса своя стоимость",
                   "Стоимость зависит от пропускной способности. Дробь округляется вниз, минимум — 1.", "b"), "p") +
        panel("tree", "Пример расчёта стоимости маршрута", ill("0 0 1000 580", ex), "b") +
        '</div>'
    ), scen="cost")

    # ------------------------------------------------------------ 10. таблица стоимостей
    slide("Стоимость: значения", sc(
        head("Стоимость для типовых скоростей", "Считаем по формуле 100 Мбит/с ÷ скорость интерфейса."),
        split(
            panel("doc", "Таблица значений",
                  table(["Скорость интерфейса", "Расчёт", "cost"],
                        [["64 кбит/с", "100 ÷ 0,064 = 1562,5", ("1562", "c")],
                         ["1,544 Мбит/с (T1)", "100 ÷ 1,544 = 64,7", ("64", "c")],
                         ["2 Мбит/с (E1)", "100 ÷ 2", ("50", "c")],
                         ["10 Мбит/с", "100 ÷ 10", ("10", "c")],
                         ["100 Мбит/с", "100 ÷ 100", ("1", "c")],
                         ["1 Гбит/с", "100 ÷ 1000 = 0,1 → минимум", ("1", "c")],
                         ["10 Гбит/с", "100 ÷ 10000 = 0,01 → минимум", ("1", "c")]]), "y"),
            steps(rowc("stop", "Проблема быстрых каналов",
                       "При 100 Мбит/с и выше стоимость по формуле равна <b>1</b>: гигабит и сотка становятся неразличимы.", "p"),
                  rowc("gear", "Решение 1 — поднять эталон",
                       "Эталонную полосу увеличивают (например, до 10 Гбит/с) — <b>одинаково на всех</b> маршрутизаторах сети.", "b"),
                  rowc("key", "Решение 2 — задать вручную",
                       "Команда <b>ip ospf cost</b> на интерфейсе. Нужна, когда в сети оборудование разных вендоров.", "g"),
                  rowc("sum", "Стоимость маршрута",
                       "Сумма стоимостей всех <b>исходящих</b> интерфейсов на пути от маршрутизатора до сети назначения.", "y")),
            "52fr 48fr")
    ))

    # ------------------------------------------------------------ 11. ECMP
    Wm = 120
    em = {"R1": (130, 330), "R2": (480, 150), "R3": (480, 510), "R4": (830, 330)}
    ecmp = (blob(480, 340, 440, 280, "p", None, seed=.4) +
            '<path d="M130 347 L480 167 L830 347" stroke="#ffe9a8" stroke-width="22" fill="none" stroke-linecap="round"/>'
            '<path d="M130 347 L480 527 L830 347" stroke="#c7e2fb" stroke-width="22" fill="none" stroke-linecap="round"/>' +
            link(130, 347, 480, 167, 5, "#7d9cc0") + link(480, 167, 830, 347, 5, "#7d9cc0") +
            link(130, 347, 480, 527, 5, "#7d9cc0") + link(480, 527, 830, 347, 5, "#7d9cc0") +
            "".join(router(x, y, Wm, "b" if n in ("R2", "R3") else "p", label=n) for n, (x, y) in em.items()) +
            "".join('<circle cx="%d" cy="%d" r="28" fill="#fff" stroke="#7d9cc0" stroke-width="3"/>%s'
                    % (x, y, txt(x, y + 9, "10", fs=24, weight=900)) for x, y in ((300, 250), (660, 250), (300, 440), (660, 440))) +
            bubble(480, 600, "10 + 10 = 20  и  10 + 10 = 20 — трафик делится", "y", 18))
    slide("Равные стоимости", sc(
        head("Равноценные маршруты — ECMP", "Если у двух путей одинаковая стоимость, OSPF использует оба."),
        split(
            ill("0 0 960 680", ecmp),
            steps(rowc("swap", "Equal Cost Multi-Path",
                       "Маршрутизатор ставит в таблицу <b>оба</b> следующих перехода и распределяет между ними трафик.", "b"),
                  rowc("gear", "Сколько путей",
                       "Команда <b>maximum-paths</b> от 1 до 32, по умолчанию 16. Отрицательная форма отключает ECMP.", "y"),
                  rowc("key", "Как выбрать один путь",
                       "Изменить стоимость интерфейса командой <b>ip ospf cost</b>: меньшее значение — предпочтительнее.", "p")),
            "56fr 44fr")
    ))
