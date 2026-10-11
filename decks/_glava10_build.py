# -*- coding: utf-8 -*-
# Сборка decks/glava10-kanalnyi.html — Глава 10. Канальный уровень
import math, json, pathlib, zipfile, io, base64, re
from PIL import Image

HERE = pathlib.Path(__file__).parent
OUT = HERE / "glava10-kanalnyi.html"
PPTX = pathlib.Path(r"C:/Users/anank/Downloads/10.pptx")
CATS = pathlib.Path(r"D:/1111")

MEDIA = HERE / "_glava10_media.json"   # кеш картинок на случай, если 10.pptx недоступен
_z = zipfile.ZipFile(PPTX) if PPTX.exists() else None
_cache = json.loads(MEDIA.read_text(encoding="utf-8")) if MEDIA.exists() else {}

def img64(name, w=1300, q=70):
    im = Image.open(io.BytesIO(_z.read("ppt/media/" + name))).convert("RGB")
    im.thumbnail((w, w))
    b = io.BytesIO(); im.save(b, "WEBP", quality=q, method=6)
    return "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()

def cat64(name, w=360):
    im = Image.open(CATS / name).convert("RGBA"); im.thumbnail((w, w))
    b = io.BytesIO(); im.save(b, "WEBP", quality=80, method=6)
    return "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()

def photo(name, cap=""):
    c = f'<figcaption>{cap}</figcaption>' if cap else ""
    src = img64(name) if _z else _cache[cap]
    return f'<figure class="card ph"><img src="{src}" alt="{cap or "Иллюстрация"}" loading="lazy">{c}</figure>'

# ---------------------------------------------------------------- scenes
SCENES = {}

def track(n, keys, default):
    out, v = [], default
    for i in range(n + 1):
        if i in keys: v = keys[i]
        out.append(v)
    return out

def scene(name, n, els, waits=None):
    spec = {"n": n, "w": [(waits or {}).get(i, 1100) for i in range(n + 1)], "e": {}}
    for eid, tr in els.items():
        e = {}
        if "p" in tr: e["p"] = track(n, tr["p"], (0, 0))
        if "o" in tr: e["o"] = track(n, tr["o"], 1)
        if "c" in tr: e["c"] = track(n, tr["c"], "")
        if "t" in tr: e["t"] = track(n, tr["t"], "")
        spec["e"][eid] = e
    SCENES[name] = spec
    return f'data-scene="{name}"'

def svg(vb, body):
    return f'<svg class="dg" viewBox="{vb}" role="img">{body}</svg>'

def pc(x, y, label="", col="o"):
    s = (f'<g class="pc {col}" transform="translate({x} {y})"><rect x="-34" y="-40" width="68" height="46" rx="6" class="pcb"/>'
         f'<rect x="-27" y="-33" width="54" height="32" rx="2" class="pcs"/><path d="M-8 6h16l4 10h-24z" class="pcb"/>'
         f'<rect x="-36" y="18" width="72" height="9" rx="3" class="pcb"/></g>')
    if label: s += f'<text class="nl" x="{x}" y="{y+50}" text-anchor="middle">{label}</text>'
    return s

def box(x, y, w, h, label, cls="bx", tcls="bxt", eid=None, extra=""):
    ida = f' data-id="{eid}"' if eid else ""
    return (f'<g class="an"{ida} {extra}><rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="10"/>'
            f'<text class="{tcls}" x="{x+w/2}" y="{y+h/2+7}" text-anchor="middle">{label}</text></g>')

def wave(x1, x2, y, amp=14, per=34):
    n = max(2, int(abs(x2 - x1) / per * 2)); d = f"M{x1} {y}"; step = (x2 - x1) / n
    for i in range(n):
        cx = x1 + step * (i + .5); ex = x1 + step * (i + 1); cy = y + (amp if i % 2 == 0 else -amp) * 2
        d += f" Q{cx:.1f} {cy:.1f} {ex:.1f} {y}"
    return d

def cap(eid, x, y, cls="cap"):
    return f'<text class="{cls} an" data-id="{eid}" x="{x}" y="{y}" text-anchor="middle"></text>'

def star(cx, cy, r1=46, r2=20, n=12):
    pts = []
    for i in range(n * 2):
        r = r1 if i % 2 == 0 else r2; a = math.pi * i / n
        pts.append(f"{cx+r*math.cos(a):.1f},{cy+r*math.sin(a):.1f}")
    return " ".join(pts)

def arrow(x1, y1, x2, y2, col, step, label="", w=900):
    dx, dy = x2 - x1, y2 - y1; L = math.hypot(dx, dy); ux, uy = dx / L, dy / L
    ex, ey = x2 - ux * 12, y2 - uy * 12; nx, ny = -uy, ux; bx, by = x2 - ux * 20, y2 - uy * 20
    lab = ""
    if label:
        mx, my = (x1 + x2) / 2, (y1 + y2) / 2; ang = math.degrees(math.atan2(dy, dx))
        if dx < 0: ang += 180
        lab = f'<text class="lbl" x="{mx:.1f}" y="{my-12:.1f}" text-anchor="middle" transform="rotate({ang:.1f} {mx:.1f} {my:.1f})">{label}</text>'
    return (f'<g class="arr {col}" data-s="{step}" data-w="{w}"><path class="draw" pathLength="1" d="M{x1} {y1}L{ex:.1f} {ey:.1f}"/>'
            f'<polygon class="head" points="{x2},{y2} {bx+nx*8:.1f},{by+ny*8:.1f} {bx-nx*8:.1f},{by-ny*8:.1f}"/>{lab}</g>')

# ---- sublayers (slide 5)
sl = ""
LAY = [("L3", "Сетевой уровень", 60), ("LLC", "Подуровень LLC", 150), ("MAC", "Подуровень MAC", 240), ("L1", "Физический уровень", 330)]
for i, (k, t, y) in enumerate(LAY):
    col = ["vio", "o", "o", "am"][i]
    sl += f'<rect class="lay {col}" x="40" y="{y}" width="380" height="70" rx="14"/><text class="layk" x="70" y="{y+44}">{k}</text><text class="layt" x="150" y="{y+43}">{t}</text>'
sl += ('<g class="an" data-id="tok" style="--md:900ms"><rect class="tokb" x="-120" y="-26" width="240" height="52" rx="12"/>'
       '<text class="tokt" y="8" text-anchor="middle" data-id="tokt"></text></g>')
sl += cap("scap", 250, 440)
SUBL = svg("0 0 700 460", sl)
Y = {"L1": 365, "MAC": 275, "LLC": 185, "L3": 95}
SUBL_SC = scene("subl", 9, {
    "tok": {"p": {0: (560, Y["L1"]), 2: (560, Y["MAC"]), 3: (560, Y["LLC"]), 4: (560, Y["L3"]), 5: (560, Y["L3"]), 6: (560, Y["LLC"]), 7: (560, Y["MAC"]), 8: (560, Y["L1"])},
            "o": {0: 0, 1: 1}},
    "tokt": {"t": {1: "сигнал среды", 2: "кадр: проверка", 3: "пакет", 4: "пакет", 5: "пакет", 6: "кадр", 7: "кадр + FCS", 8: "0 и 1", 9: "сигнал среды"}},
    "scap": {"t": {1: "Приём: сигнал на физическом уровне", 2: "MAC: формирует кадр и проверяет целостность", 3: "LLC: преобразует кадр в пакет",
                   4: "L3: дальнейшая обработка пакета", 5: "Передача: L3 отдаёт пакет на LLC", 6: "LLC: инкапсуляция данных в кадр",
                   7: "MAC: пересчёт FCS и добавление в концевик", 8: "MAC отдаёт кадр как последовательность нулей и единиц", 9: "L1 преобразует биты в сигнал среды"}},
}, {1: 900, 2: 1100, 3: 1100, 4: 1100, 5: 900, 6: 1100, 7: 1100, 8: 1100, 9: 1100})

# ---- collision (slides 7, 14)
def collision(name):
    b = pc(80, 200, "Рабочая станция") + pc(820, 200, "Рабочая станция", "v")
    b += f'<path class="dr wo an" data-id="wl" pathLength="1" d="{wave(130, 450, 180)}"/>'
    b += f'<path class="dr wv an" data-id="wr" pathLength="1" d="{wave(770, 450, 180)}"/>'
    b += f'<g class="an" data-id="bst"><polygon class="burst" points="{star(450,180)}"/><polygon class="burst2" points="{star(450,180,24,10)}"/></g>'
    b += '<text class="lblo an" data-id="lla" x="250" y="110" text-anchor="middle"></text>'
    b += '<text class="lblv an" data-id="llb" x="650" y="110" text-anchor="middle"></text>'
    b += cap("ccap", 450, 320)
    sc = scene(name, 4, {
        "wl": {"c": {0: "", 1: "on", 4: "on lost"}}, "wr": {"c": {0: "", 2: "on", 4: "on lost"}},
        "lla": {"t": {1: "кадр А →"}}, "llb": {"t": {2: "← кадр Б"}},
        "bst": {"o": {0: 0, 3: 1}},
        "ccap": {"t": {1: "Станция слева начинает передачу в общую среду",
                       2: "В тот же момент начинает передавать станция справа",
                       3: "Сигналы встречаются в середине канала: коллизия",
                       4: "Оба кадра искажены — данные теряются, нужна повторная передача"}},
    }, {1: 1000, 2: 1000, 3: 900, 4: 1100})
    return svg("0 0 900 340", b), sc

COL7, COL7_SC = collision("col7")
COL14, COL14_SC = collision("col14")

# ---- full duplex (15)
fd = pc(80, 200, "Узел А") + pc(820, 200, "Узел Б", "v")
fd += f'<path class="dr wo an" data-id="fa" pathLength="1" d="{wave(130, 770, 150, 10)}"/>'
fd += f'<path class="dr wv an" data-id="fb" pathLength="1" d="{wave(770, 130, 215, 10)}"/>'
fd += '<text class="lblo" x="450" y="112" text-anchor="middle">передача А – Б</text><text class="lblv" x="450" y="275" text-anchor="middle">передача Б – А</text>'
fd += cap("fcap", 450, 325)
FDX = svg("0 0 900 340", fd)
FDX_SC = scene("fdx", 2, {"fa": {"c": {0: "", 1: "on"}}, "fb": {"c": {0: "", 1: "on"}},
                          "fcap": {"t": {1: "Приём и передача одновременно", 2: "Коллизий нет: домен коллизий заканчивается на порту коммутатора"}}},
               {1: 1200, 2: 900})

# ---- polling (16)
po = ('<rect class="node o" x="40" y="20" width="220" height="60" rx="12"/><text class="nodet" x="150" y="57" text-anchor="middle">Контролирующее устройство</text>'
      '<rect class="node o" x="470" y="20" width="130" height="60" rx="12"/><text class="nodet" x="535" y="57" text-anchor="middle">Узел 1</text>'
      '<rect class="node v" x="680" y="20" width="130" height="60" rx="12"/><text class="nodet" x="745" y="57" text-anchor="middle">Узел 2</text>'
      '<line class="ll" x1="150" y1="80" x2="150" y2="420"/><line class="ll" x1="535" y1="80" x2="535" y2="420"/><line class="ll" x1="745" y1="80" x2="745" y2="420"/>')
po += arrow(150, 120, 535, 160, "c-o", 1, "опрос")
po += arrow(535, 185, 150, 225, "c-v", 2, "отказ")
po += arrow(150, 250, 745, 290, "c-o", 3, "опрос")
po += arrow(745, 315, 150, 355, "c-v", 4, "информация")
po += arrow(150, 375, 745, 410, "c-o", 5, "подтверждение")
POLL = svg("0 0 850 430", po)

# ---- token ring (17)
def token_ring(name):
    tr = '<circle class="ring" cx="450" cy="230" r="160"/>'
    POS = []
    for i in range(6):
        a = -math.pi / 2 + i * math.pi / 3; x, y = 450 + 160 * math.cos(a), 230 + 160 * math.sin(a); POS.append((x, y))
        tr += f'<g class="an" data-id="n{i}">' + pc(round(x), round(y) + 18) + '</g>'
    tr += '<g class="an" data-id="tk" style="--md:800ms"><circle class="tkc" r="22"/><text class="tkt" y="7" text-anchor="middle">T</text></g>'
    tr += cap("tcap", 450, 458)
    _tk = {"tk": {"p": {}}, "tcap": {"t": {}}}
    for i in range(6): _tk[f"n{i}"] = {"c": {}}
    for k in range(8):
        j = k % 6; x, y = POS[j]; cx, cy = 450 + (x - 450) * .62, 230 + (y - 230) * .62
        _tk["tk"]["p"][k] = (round(cx), round(cy))
        for i in range(6): _tk[f"n{i}"]["c"][k] = "hot" if i == j else ""
        _tk["tcap"]["t"][k] = f"Метка у узла {j+1}: только он может передавать"
    return svg("0 0 900 490", tr), scene(name, 7, _tk, {i: 1000 for i in range(8)})

TOK, TOK_SC = token_ring("tok")

# ---- reservation (18)
def reservation(name):
    rs = '<line class="tl" x1="40" y1="250" x2="860" y2="250"/><polygon class="tlh" points="870,250 852,241 852,259"/><text class="nl" x="840" y="290">время</text>'
    COLS = ["v", "o", "g", "v", "o", "g"]
    for i in range(6):
        x = 70 + i * 130
        rs += (f'<g class="an slot" data-id="s{i}"><rect class="slotb" x="{x}" y="120" width="110" height="110" rx="12"/>'
               f'<text class="slt" x="{x+55}" y="100" text-anchor="middle">УЗЕЛ {i%3+1}</text></g>' + pc(x + 55, 190, "", COLS[i]))
    rs += '<g class="an" data-id="mk" style="--md:1000ms"><line class="mkl" x1="0" y1="110" x2="0" y2="262"/><circle class="mkc" cy="250" r="8"/></g>'
    rs += cap("rcap", 450, 300)
    _rs = {"mk": {"p": {0: (70, 0)}}, "rcap": {"t": {}}}
    for i in range(6): _rs[f"s{i}"] = {"c": {0: ""}}
    for k in range(1, 7):
        _rs["mk"]["p"][k] = (70 + (k - 1) * 130 + 110, 0)
        for i in range(6): _rs[f"s{i}"]["c"][k] = "on" if i == k - 1 else ""
        _rs["rcap"]["t"][k] = f"Слот {k}: канал занят узлом {(k-1)%3+1}, остальные молчат"
    return svg("0 0 900 330", rs), scene(name, 6, _rs, {i: 1100 for i in range(7)})

RES, RES_SC = reservation("res")

# ---- 8a. резервирование времени: расписание слотов
def reservation8(name):
    RY = [70, 160, 250]; X0, W, GAP = 230, 112, 125
    g = ""
    for i, y in enumerate(RY):
        g += f'<text class="nl" x="30" y="{y+44}">Узел {i+1}</text>'
    for sN in range(6):
        x = X0 + sN * GAP
        g += f'<text class="slt" x="{x+W/2}" y="48" text-anchor="middle">СЛОТ {sN+1}</text>'
        for i, y in enumerate(RY):
            g += f'<rect class="cellb an" data-id="c{sN}_{i}" x="{x}" y="{y}" width="{W}" height="70" rx="10"/>'
        own = sN % 3; oy = RY[own]
        if sN == 3:
            g += (f'<g class="an" data-id="k{sN}" style="--md:500ms"><rect class="padb" x="{x+10}" y="{oy+16}" width="{W-20}" height="38" rx="8"/>'
                  f'<text class="bxt xs" x="{x+W/2}" y="{oy+41}" text-anchor="middle">нет данных</text></g>')
        else:
            col = ["o", "v", "g"][own]
            g += (f'<g class="an" data-id="k{sN}" style="--md:500ms"><rect class="frb {col}" x="{x+10}" y="{oy+16}" width="{W-20}" height="38" rx="8"/>'
                  f'<text class="bxt xs" x="{x+W/2}" y="{oy+41}" text-anchor="middle">кадр</text></g>')
    XE = X0 + 5 * GAP + W
    g += (f'<line class="tl" x1="{X0}" y1="345" x2="{XE+20}" y2="345"/>'
          f'<polygon class="tlh" points="{XE+32},345 {XE+14},336 {XE+14},354"/>'
          f'<text class="nl" x="{XE+10}" y="382" text-anchor="end">время</text>')
    g += cap("rscap", 520, 398)
    els = {"rscap": {"t": {}}}
    for sN in range(6):
        els[f"k{sN}"] = {"o": {0: 0}}
        for i in range(3): els[f"c{sN}_{i}"] = {"c": {0: ""}}
    CAPS = ["Слот 1 закреплён за узлом 1: передаёт только он, узлы 2 и 3 молчат",
            "Слот 2 — очередь узла 2, узлы 1 и 3 ждут своего промежутка",
            "Слот 3 — передаёт узел 3, расписание известно заранее",
            "Слот 4 снова у узла 1, но данных нет — канал простаивает впустую",
            "Слот 5 — узел 2 передаёт в свой промежуток",
            "Слот 6 — узел 3 передаёт, круг завершён",
            "Расписание повторяется: коллизии невозможны, но пустые слоты теряют полосу"]
    for k in range(1, 7):
        sN = k - 1; own = sN % 3
        for t in range(6):
            for i in range(3):
                els[f"c{t}_{i}"]["c"][k] = ("on" if i == own else "mute") if t == sN else ""
            els[f"k{t}"]["o"][k] = 1 if t <= sN else 0
        els["rscap"]["t"][k] = CAPS[sN]
    for t in range(6):
        for i in range(3): els[f"c{t}_{i}"]["c"][7] = ""
    els["rscap"]["t"][7] = CAPS[6]
    return svg("0 0 1000 412", g), scene(name, 7, els, {i: 1250 for i in range(8)})

# ---- 8b. селективный метод: опрос и разрешение
def selective(name):
    g = ('<rect class="node o" x="40" y="165" width="250" height="100" rx="14"/>'
         '<text class="nodet" x="165" y="202" text-anchor="middle">Управляющее</text>'
         '<text class="nodet" x="165" y="232" text-anchor="middle">устройство</text>')
    NY = [70, 215, 360]
    for i, y in enumerate(NY):
        g += f'<path class="ll" fill="none" d="M290 215 C 440 215, 500 {y}, 640 {y}"/>'
        g += f'<g class="an" data-id="u{i}">' + pc(730, y, f"Узел {i+1}", ["o", "v", "g"][i]) + '</g>'
    g += ('<g class="an" data-id="pm" style="--md:900ms"><rect class="frb o" x="-92" y="-21" width="184" height="42" rx="10"/>'
          '<text class="bxt sm" y="7" text-anchor="middle" data-id="pmt"></text></g>')
    g += cap("scap8", 470, 455)
    HOME = (360, 215)
    els = {"pm": {"p": {0: HOME}, "o": {0: 0, 1: 1}}, "pmt": {"t": {}}, "scap8": {"t": {}}}
    for i in range(3): els[f"u{i}"] = {"c": {0: ""}}
    SEQ = [(0, "опрос \u2192", "Контроллер спрашивает узел 1: есть что передавать?", True),
           (0, "\u2190 нет данных", "Узел 1 отвечает «нечего» и в среду не выходит", False),
           (1, "опрос \u2192", "Контроллер переходит к узлу 2", True),
           (1, "\u2190 кадр узла 2", "Узел 2 получил разрешение и передаёт свой кадр", False),
           (2, "опрос \u2192", "Очередь узла 3", True),
           (2, "\u2190 кадр узла 3", "Узел 3 передаёт, остальные молчат — коллизий нет", False)]
    for k, (jj, txt, capt, out) in enumerate(SEQ, 1):
        els["pm"]["p"][k] = (610, NY[jj]) if out else HOME
        els["pmt"]["t"][k] = txt
        for i in range(3): els[f"u{i}"]["c"][k] = ("hot" if i == jj else "wait")
        els["scap8"]["t"][k] = capt
    els["pm"]["o"][7] = 0
    for i in range(3): els[f"u{i}"]["c"][7] = ""
    els["scap8"]["t"][7] = "Без разрешения контроллера никто не выходит в среду — но всё зависит от него"
    return svg("0 0 960 475", g), scene(name, 7, els, {i: 1200 for i in range(8)})

# ---- 8c. случайный доступ: слушаем среду, ловим коллизию
def randacc(name):
    g = '<line class="medl an" data-id="med" x1="60" y1="300" x2="840" y2="300"/><text class="nl" x="450" y="348" text-anchor="middle">общая среда (радиоканал)</text>'
    X = [180, 450, 720]
    for i, x in enumerate(X):
        g += f'<line class="ll" x1="{x}" y1="240" x2="{x}" y2="300"/>'
        g += f'<g class="an" data-id="r{i}">' + pc(x, 200, f"Узел {i+1}", ["o", "v", "g"][i]) + '</g>'
    for n, col in (("rp", "o"), ("rq", "g")):
        g += (f'<g class="an" data-id="{n}" style="--md:900ms"><rect class="frb {col}" x="-62" y="-19" width="124" height="38" rx="10"/>'
              f'<text class="bxt xs" y="6" text-anchor="middle" data-id="{n}t"></text></g>')
    g += f'<g class="an" data-id="rb"><polygon class="burst" points="{star(450,300,30,13)}"/><polygon class="burst2" points="{star(450,300,16,7)}"/></g>'
    g += cap("rcap8", 450, 395)
    els = {"rp": {"p": {0: (450, 300)}, "o": {0: 0}}, "rpt": {"t": {}},
           "rq": {"p": {0: (720, 300)}, "o": {0: 0}}, "rqt": {"t": {}},
           "rb": {"o": {0: 0}}, "med": {"c": {0: ""}}, "rcap8": {"t": {}}}
    for i in range(3): els[f"r{i}"] = {"c": {0: ""}}
    els["r1"]["c"].update({1: "hot", 2: "hot", 3: "hot", 4: "", 5: "", 6: ""})
    els["r0"]["c"].update({3: "wait", 4: "hot", 5: "hot", 6: "wait"})
    els["r2"]["c"].update({5: "hot", 6: "wait"})
    els["rp"]["o"].update({2: 1, 4: 1, 6: 0})
    els["rp"]["p"].update({1: (450, 300), 2: (450, 300), 3: (640, 300), 4: (180, 300), 5: (330, 300)})
    els["rpt"]["t"].update({2: "кадр узла 2", 3: "кадр узла 2", 4: "кадр узла 1", 5: "кадр узла 1"})
    els["rq"]["o"].update({5: 1, 6: 0})
    els["rq"]["p"].update({5: (580, 300)})
    els["rqt"]["t"].update({5: "кадр узла 3"})
    els["rb"]["o"].update({5: 1, 6: 0})
    els["med"]["c"].update({2: "busy", 3: "busy", 4: "busy", 5: "busy", 6: ""})
    els["rcap8"]["t"] = {1: "Узел 2 прослушивает несущую: среда свободна",
                         2: "Раз свободна — узел 2 сразу занимает канал",
                         3: "Узел 1 хочет передать, но слышит занятую среду и ждёт",
                         4: "Канал освободился — узел 1 передаёт свой кадр",
                         5: "Узлы 1 и 3 начали одновременно: оба слышали тишину — коллизия",
                         6: "Оба ждут случайное время и повторяют попытку: так работают CSMA/CD и CSMA/CA"}
    return svg("0 0 900 415", g), scene(name, 6, els, {1: 1200, 2: 1200, 3: 1300, 4: 1200, 5: 1500, 6: 1600})

# ---- 8d. передача токена
def token8(name):
    CX, CY, R = 450, 240, 155
    POS = []
    g = f'<circle class="ring" cx="{CX}" cy="{CY}" r="{R}"/>'
    for i in range(6):
        a = -math.pi / 2 + i * math.pi / 3
        x, y = CX + R * math.cos(a), CY + R * math.sin(a); POS.append((x, y))
        g += f'<g class="an" data-id="n{i}">' + pc(round(x), round(y) + 16, f"Узел {i+1}") + '</g>'
    g += '<g class="an" data-id="tk" style="--md:800ms"><circle class="tkc" r="22"/><text class="tkt" y="7" text-anchor="middle">T</text></g>'
    g += ('<g class="an" data-id="fr" style="--md:900ms"><rect class="frb v" x="-52" y="-18" width="104" height="36" rx="9"/>'
          '<text class="bxt xs" y="6" text-anchor="middle">кадр</text></g>')
    g += cap("tcap8", CX, 492)
    def inner(jj, f=.56): return (round(CX + (POS[jj][0] - CX) * f), round(CY + (POS[jj][1] - CY) * f))
    def outer(jj, f=1.42): return (round(CX + (POS[jj][0] - CX) * f), round(CY + (POS[jj][1] - CY) * f))
    els = {"tk": {"p": {0: inner(0)}, "o": {0: 0, 1: 1}}, "fr": {"p": {0: outer(1)}, "o": {0: 0}}, "tcap8": {"t": {}}}
    for i in range(6): els[f"n{i}"] = {"c": {0: ""}}
    STEPS = [(0, None, 0, "Токен пришёл к узлу 1, но передавать ему нечего"),
             (1, None, 0, "Узел 1 сразу отдаёт токен дальше — узлу 2"),
             (1, 1, 1, "У узла 2 есть данные: владея токеном, он выпускает кадр в кольцо"),
             (1, 2, 1, "Кадр идёт по кольцу, промежуточные узлы только ретранслируют его"),
             (1, 4, 1, "Узел 5 — получатель: он копирует кадр себе"),
             (2, None, 0, "Узел 2 закончил и отпустил токен — метка ушла к узлу 3"),
             (2, None, 0, "Передавать может только владелец токена, поэтому коллизий нет вовсе")]
    for k, (holder, fj, fo, capt) in enumerate(STEPS, 1):
        els["tk"]["p"][k] = inner(holder)
        els["fr"]["o"][k] = fo
        if fj is not None: els["fr"]["p"][k] = outer(fj)
        for i in range(6):
            els[f"n{i}"]["c"][k] = "hot" if i == holder else ("rx" if (fj == 4 and i == 4) else "")
        els["tcap8"]["t"][k] = capt
    return svg("0 0 900 512", g), scene(name, 7, els, {i: 1300 for i in range(8)})

SEL8, SEL8_SC = selective("sel8")
RND8, RND8_SC = randacc("rnd8")
RES8, RES8_SC = reservation8("res8")
TOK8, TOK8_SC = token8("tok8")

# ---- CSMA/CD and CSMA/CA flow (20, 21)
def flow(name, items, order, caps):
    h = '<div class="flow">' + "".join(
        f'<div class="fb an" data-id="b{i}"><span class="badge b{i%5}">{i+1:02d}</span><span>{t}</span></div>' for i, t in enumerate(items)) + '</div>'
    h += '<p class="fcap" data-id="fc"></p>'
    n = len(order)
    els = {f"b{i}": {"c": {0: ""}} for i in range(len(items))}
    els["fc"] = {"t": {0: ""}}
    for k, j in enumerate(order, 1):
        for i in range(len(items)): els[f"b{i}"]["c"][k] = "hot" if i == j else ("done" if i in order[:k] else "")
        els["fc"]["t"][k] = caps[k - 1]
    return f'<div class="card flowcard" {scene(name, n, els, {i: 1300 for i in range(n+1)})}>{h}</div>'

CD = flow("cd", ["Попытка передачи", "Коллизия", "Ожидание случайного промежутка времени", "Повторение с шага №1", "Завершение процесса передачи данных"],
          [0, 1, 2, 3, 0, 4],
          ["Устройство пытается передать кадр", "Обнаружена коллизия", "Ожидание случайного промежутка: равноправный доступ к среде",
           "Повторение с шага №1", "Новая попытка передачи", "Коллизии нет: передача завершена"])
CA = flow("ca", ["Устройство прослушивает среду", "Среда свободна: отправка сигнала затора (jam signal)", "Ожидание другого сигнала затора",
                 "Получен чужой сигнал: режим ожидания, повтор при освобождении", "Сигнала нет: передача кадра", "После передачи: ожидание и повтор процедуры"],
          [0, 1, 2, 3, 0, 1, 2, 4, 5],
          ["Станция прослушивает среду", "Среда свободна: станция предупреждает «коллег» сигналом затора", "Станция ждёт сигнал затора от другой станции",
           "Сигнал получен: режим ожидания", "Канал освободился: повтор", "Снова сигнал затора", "Ожидание…", "Сигнал затора не пришёл: передача кадра",
           "Кадр передан: ожидание и повтор процедуры"])

# ---- framing fixed (10) and variable (11)
fx = ""
for i, (x, bits) in enumerate(((60, "1001101010111010101"), (330, "1001010101110101111"), (600, "0101111000"))):
    col = ["o", "v", "pk"][i]
    fx += (f'<g class="an" data-id="fr{i}"><text class="fl" x="{x+120}" y="70" text-anchor="middle">КАДР {i+1}</text>'
           f'<rect class="frb {col}" x="{x}" y="90" width="240" height="60" rx="10"/>'
           f'<text class="bits" x="{x+14}" y="128">{bits}</text>'
           f'<text class="nl sm" x="{x+120}" y="185" text-anchor="middle">X байт</text></g>')
fx += '<g class="an" data-id="pad"><rect class="padb" x="760" y="96" width="74" height="48" rx="6"/><text class="bits pad" x="768" y="128">101110</text></g>'
fx += cap("xcap", 450, 245)
FIX = svg("0 0 900 270", fx)
FIX_SC = scene("fix", 4, {"fr0": {"o": {0: 0, 1: 1}}, "fr1": {"o": {0: 0, 2: 1}}, "fr2": {"o": {0: 0, 3: 1}}, "pad": {"o": {0: 0, 4: 1}},
                          "xcap": {"t": {1: "Каждые X байт в потоке – отдельный кадр", 3: "Флаги для разделения не нужны",
                                         4: "Данных не хватает: добавленные байты не несут информации"}}}, {1: 900, 2: 900, 3: 900, 4: 1200})

vr = ('<g class="an" data-id="m1"><text class="fl" x="40" y="40">МЕТОД 1: ПОЛЕ ДЛИНЫ</text>'
      '<rect class="frb v" x="40" y="60" width="140" height="56" rx="10"/><text class="bxt" x="110" y="95" text-anchor="middle">длина</text>'
      '<rect class="frb o" x="186" y="60" width="240" height="56" rx="10"/><text class="bxt" x="306" y="95" text-anchor="middle">данные</text></g>'
      '<g class="an" data-id="m2"><text class="fl" x="480" y="40">МЕТОД 2: ФЛАГ В КОНЦЕ</text>'
      '<rect class="frb o" x="480" y="60" width="240" height="56" rx="10"/><text class="bxt" x="600" y="95" text-anchor="middle">данные</text>'
      '<rect class="frb pk" x="726" y="60" width="130" height="56" rx="10"/><text class="bxt" x="791" y="95" text-anchor="middle">флаг</text></g>'
      '<g class="an" data-id="st1"><text class="nl" x="40" y="190">Данные совпадают с флагом:</text><text class="bits big" x="360" y="190">01111110</text></g>'
      '<g class="an" data-id="st2"><text class="nl" x="40" y="250">Экранированные данные:</text><text class="bits big" x="360" y="250">011111<tspan class="ins">0</tspan>10</text></g>')
vr += cap("vcap", 450, 300)
VAR = svg("0 0 900 320", vr)
VAR_SC = scene("var", 4, {"m1": {"o": {0: 0, 1: 1}}, "m2": {"o": {0: 0, 2: 1}}, "st1": {"o": {0: 0, 3: 1}}, "st2": {"o": {0: 0, 4: 1}},
                          "vcap": {"t": {3: "Последние биты данных совпадают с битами флага", 4: "Добавляется специальная последовательность бит"}}},
              {1: 900, 2: 900, 3: 1200, 4: 1200})

# ---- generic frame (23)
gf = (box(40, 60, 230, 80, "ЗАГОЛОВОК", "frb o", "bxt", "g0") + box(280, 60, 330, 80, "ИНФОРМАЦИЯ", "frb g", "bxt", "g1") +
      box(620, 60, 230, 80, "КОНЦЕВИК", "frb v", "bxt", "g2"))
gf += ('<g class="an" data-id="gs"><text class="nl sm" x="155" y="175" text-anchor="middle">разделитель начала кадра</text><text class="nl sm" x="155" y="198" text-anchor="middle">Destination / Source MAC, тип</text></g>'
       '<g class="an" data-id="gi"><text class="nl sm" x="445" y="175" text-anchor="middle">пакет уровня L3</text></g>'
       '<g class="an" data-id="gt"><text class="nl sm" x="735" y="175" text-anchor="middle">FCS</text><text class="nl sm" x="735" y="198" text-anchor="middle">разделитель конца кадра</text></g>')
GEN = svg("0 0 900 220", gf)
GEN_SC = scene("gen", 3, {"g0": {"o": {0: 0, 1: 1}, "p": {0: (-30, 0), 1: (0, 0)}}, "gs": {"o": {0: 0, 1: 1}},
                          "g1": {"o": {0: 0, 2: 1}, "p": {0: (-30, 0), 2: (0, 0)}}, "gi": {"o": {0: 0, 2: 1}},
                          "g2": {"o": {0: 0, 3: 1}, "p": {0: (-30, 0), 3: (0, 0)}}, "gt": {"o": {0: 0, 3: 1}}}, {1: 800, 2: 800, 3: 800})

# ---- FCS check (25)
fc = pc(90, 250, "Получатель")
fc += ('<g class="an" data-id="fk" style="--md:1100ms"><rect class="frb o" x="0" y="0" width="150" height="46" rx="8"/><text class="bxt sm" x="54" y="30" text-anchor="middle">данные</text>'
       '<rect class="frb v" x="104" y="0" width="46" height="46" rx="8"/><text class="bxt sm" x="127" y="30" text-anchor="middle">FCS</text></g>')
fc += box(220, 220, 200, 60, "вычисление суммы", "bx", "bxt sm", "c1") + box(450, 220, 200, 60, "сравнение", "bx", "bxt sm", "c2")
fc += box(690, 160, 190, 56, "кадр принят", "okb", "bxt sm", "ok") + box(690, 290, 190, 56, "кадр отбрасывается", "nob", "bxt sm", "no")
fc += box(220, 380, 200, 50, "кадр потерян", "bx", "bxt sm", "r1") + box(450, 380, 210, 50, "TCP не получает ACK", "bx", "bxt sm", "r2") + box(690, 380, 190, 50, "TCP шлёт снова", "okb", "bxt sm", "r3")
fc += cap("fcc", 450, 40)
FCS = svg("0 0 900 450", fc)
FCS_SC = scene("fcs", 9, {
    "fk": {"p": {0: (560, 60), 1: (200, 60), 5: (560, 60), 6: (200, 60)}, "o": {0: 0, 1: 1, 4: 0, 5: 1}},
    "c1": {"c": {0: "", 2: "hot", 3: "", 7: "hot", 8: ""}}, "c2": {"c": {0: "", 3: "hot", 4: "", 8: "hot", 9: ""}},
    "ok": {"o": {0: .25, 4: 1, 5: .25}}, "no": {"o": {0: .25, 9: 1}},
    "r1": {"o": {0: .25, 9: 1}}, "r2": {"o": {0: .25, 9: 1}}, "r3": {"o": {0: .25, 9: 1}},
    "fcc": {"t": {1: "Кадр приходит на устройство-получатель", 2: "Получатель вычисляет контрольную сумму", 3: "Сравнивает с суммой в концевике",
                  4: "Совпадает: кадр принят", 5: "Второй кадр повреждён помехами", 7: "Вычисление контрольной суммы", 8: "Сравнение",
                  9: "Не совпадает: кадр отбрасывается, TCP отправит сегмент снова"}},
}, {1: 1300, 2: 900, 3: 900, 4: 1200, 5: 1300, 6: 1300, 7: 900, 8: 900, 9: 1500})

# ---- 802.11 To DS / From DS / bridge (37-39)
def phone(x, y):
    return f'<g transform="translate({x} {y})"><rect class="phb" x="-22" y="-40" width="44" height="80" rx="9"/><rect class="pcs" x="-16" y="-31" width="32" height="56" rx="3"/></g>'

def ap(x, y, label):
    return (f'<g transform="translate({x} {y})"><rect class="apb" x="-44" y="-26" width="88" height="52" rx="12"/>'
            f'<path class="apw" d="M-14 -8a20 20 0 0 1 28 0M-22 -16a32 32 0 0 1 44 0"/><circle class="apd" cy="4" r="4"/></g>'
            f'<text class="nl" x="{x}" y="{y+52}" text-anchor="middle">{label}</text>')

def sw(x, y, label):
    return (f'<g transform="translate({x} {y})"><rect class="swb" x="-60" y="-24" width="120" height="48" rx="10"/>'
            + "".join(f'<rect class="swp" x="{-46+i*20}" y="-6" width="12" height="12" rx="2"/>' for i in range(5)) + '</g>'
            f'<text class="nl" x="{x}" y="{y+50}" text-anchor="middle">{label}</text>')

def router(x, y, label):
    return (f'<g transform="translate({x} {y})"><path class="rtb" d="M-50 -10v26a50 16 0 0 0 100 0v-26z"/><ellipse class="rtt" cy="-10" rx="50" ry="16"/>'
            f'<path class="rta" d="M-18 -10h36M0 -18v16"/></g><text class="nl" x="{x}" y="{y+52}" text-anchor="middle">{label}</text>')

def server(x, y, label):
    return (f'<g transform="translate({x} {y})"><rect class="apb" x="-26" y="-42" width="52" height="84" rx="8"/>'
            f'<path class="apw" d="M-14 -22h28M-14 -8h28"/></g><text class="nl" x="{x}" y="{y+62}" text-anchor="middle">{label}</text>')

DEVS = {
    "phone": ("Смартфон", "192.168.1.10", "AA-11-11-11-11-11"),
    "AP": ("AP", "192.168.1.2", "AA-22-22-22-22-22"),
    "SW1": ("SW1", "192.168.1.3", "AA-33-33-33-33-33"),
    "R1": ("R1", "192.168.1.1", "AA-44-44-44-44-44"),
    "Server": ("Server", "10.0.0.10", "AA-55-55-55-55-55"),
    "AP1": ("AP1", "10.0.0.2", "AA-66-66-66-66-66"),
    "AP2": ("AP2", "10.0.0.3", "AA-77-77-77-77-77"),
    "PC1": ("PC1", "10.0.0.20", "AA-88-88-88-88-88"),
}

def devtag(key, x, y, below=True):
    name, ip, mac = DEVS[key]
    yy = y + 78 if below else y - 92
    return (f'<g class="an halo" data-id="h_{key}"><rect class="halob" x="{x-92}" y="{y-58}" width="184" height="{186 if below else 190}" rx="14" transform="translate(0 {0 if below else -60})"/></g>'
            f'<text class="adr" x="{x}" y="{yy}" text-anchor="middle">IP {ip}</text>'
            f'<text class="adr mac" x="{x}" y="{yy+18}" text-anchor="middle">MAC {mac}</text>')

def wifi_scene(name, devices, tags, hops, flags, addrs, caps, travel):
    """addrs: [(dev_key, role, how)]; travel: [text per hop]"""
    b = ""
    for (x1, y1), (x2, y2), kind in hops:
        b += f'<line class="{"wl" if kind == "r" else "cl"}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'
    b += "".join(devtag(k, x, y, bl) for k, x, y, bl in tags)
    b += devices
    b += '<g class="an" data-id="env" style="--md:1000ms"><rect class="envb" x="-24" y="-16" width="48" height="32" rx="4"/><path class="envl" d="M-24 -16l24 18 24-18"/></g>'
    na = len(addrs); fw = 150 if na == 4 else 190
    x = (900 - (2 * 58 + na * fw + (na + 1) * 6)) / 2
    Y0 = 400
    for i, f in enumerate(("ToDS", "FromDS")):
        b += (f'<rect class="fcell" x="{x}" y="{Y0}" width="58" height="34" rx="6"/><text class="fct" x="{x+29}" y="{Y0+22}" text-anchor="middle">{f}</text>'
              f'<rect class="fval an" data-id="fv{i}" x="{x}" y="{Y0+40}" width="58" height="52" rx="6"/><text class="fvt" x="{x+29}" y="{Y0+74}" text-anchor="middle" data-id="ft{i}"></text>')
        x += 64
    for i, (key, role, how) in enumerate(addrs):
        b += (f'<rect class="acell" x="{x}" y="{Y0}" width="{fw}" height="34" rx="6"/><text class="fct" x="{x+fw/2}" y="{Y0+22}" text-anchor="middle">MAC-адрес {i+1}</text>'
              f'<rect class="aval an" data-id="av{i}" x="{x}" y="{Y0+40}" width="{fw}" height="52" rx="6"/>'
              f'<text class="avt mono" x="{x+fw/2}" y="{Y0+62}" text-anchor="middle" data-id="at{i}"></text><text class="avr" x="{x+fw/2}" y="{Y0+82}" text-anchor="middle" data-id="ar{i}"></text>')
        x += fw + 6
    b += '<rect class="howb" x="20" y="508" width="860" height="56" rx="12"/>' + cap("wcap", 450, 543, "how")
    route = [h[0] for h in hops] + [hops[-1][1]]
    n = 2 + na + len(hops)
    els = {"env": {"p": {0: route[0]}, "o": {0: 0}}, "wcap": {"t": {}}}
    for k, *_ in tags: els[f"h_{k}"] = {"o": {0: 0}}
    for i in range(2):
        els[f"ft{i}"] = {"t": {0: "", 1: str(flags[i])}}; els[f"fv{i}"] = {"c": {0: "", 1: "on"}}
    els["wcap"]["t"][1] = caps
    for i, (key, role, how) in enumerate(addrs):
        st = 2 + i
        els[f"at{i}"] = {"t": {0: "", st: DEVS[key][2]}}; els[f"ar{i}"] = {"t": {0: "", st: role}}; els[f"av{i}"] = {"c": {0: "", st: "on"}}
        els[f"h_{key}"]["o"][st] = 1; els[f"h_{key}"]["o"][st + 1] = 0
        els["wcap"]["t"][st] = f"Адрес {i+1} = {DEVS[key][0]} ({DEVS[key][2]}): {how}"
    k = 2 + na
    els["env"]["o"][k] = 1
    for j in range(len(hops)):
        els["env"]["p"][k + j + 1] = route[j + 1]
        els["wcap"]["t"][k + j + 1] = travel[j]
    return svg("0 0 900 580", b), scene(name, n, els, {i: 1800 for i in range(n + 1)})

TODS_DEV = phone(90, 150) + ap(280, 250, "AP") + sw(560, 250, "SW1") + router(790, 120, "R1")
TODS, TODS_SC = wifi_scene("tods", TODS_DEV, [("phone", 90, 150, False), ("AP", 280, 250, True), ("SW1", 560, 250, True), ("R1", 790, 120, False)],
    [((90, 150), (280, 250), "r"), ((280, 250), (560, 250), "c"), ((560, 250), (790, 120), "c")], (1, 0),
    [("AP", "Receiver Address", "приёмник – точка доступа, к которой подключён смартфон"),
     ("phone", "Source / Transmitter", "смартфон и создал кадр, и передаёт его в эфир"),
     ("R1", "Destination Address", "назначение – R1, шлюз во внешнюю сеть")],
    "To DS = 1, From DS = 0: кадр идёт от устройства к системе распределения",
    ["Смартфон передаёт кадр по радио на AP", "AP пересылает кадр через систему распределения на SW1", "SW1 доставляет кадр маршрутизатору R1"])
FROMDS_DEV = phone(90, 150) + ap(280, 250, "AP") + sw(560, 250, "SW1") + router(790, 120, "R1")
FROMDS, FROMDS_SC = wifi_scene("fromds", FROMDS_DEV, [("phone", 90, 150, False), ("AP", 280, 250, True), ("SW1", 560, 250, True), ("R1", 790, 120, False)],
    [((790, 120), (560, 250), "c"), ((560, 250), (280, 250), "c"), ((280, 250), (90, 150), "r")], (0, 1),
    [("phone", "Destination / Receiver", "смартфон – и получатель, и приёмник радиосигнала"),
     ("AP", "Transmitter Address", "передатчик в эфир – точка доступа"),
     ("R1", "Source Address", "источник кадра – маршрутизатор R1")],
    "To DS = 0, From DS = 1: кадр идёт от системы распределения к устройству",
    ["R1 отправляет кадр в сторону SW1", "SW1 передаёт кадр точке доступа", "AP передаёт кадр по радио смартфону"])
BR_DEV = server(90, 200, "Server") + ap(340, 200, "AP1") + ap(590, 200, "AP2") + pc(820, 215, "PC1")
BRIDGE, BRIDGE_SC = wifi_scene("bridge", BR_DEV, [("Server", 90, 200, True), ("AP1", 340, 200, True), ("AP2", 590, 200, True), ("PC1", 820, 200, True)],
    [((90, 200), (340, 200), "c"), ((340, 200), (590, 200), "r"), ((590, 200), (820, 200), "c")], (1, 1),
    [("AP2", "Receiver", "приёмник по радио – точка доступа получателя"),
     ("AP1", "Transmitter", "передатчик по радио – точка доступа отправителя"),
     ("PC1", "Destination", "конечный получатель – компьютер PC1"),
     ("Server", "Source", "отправитель кадра – сервер")],
    "To DS = 1, From DS = 1: точки доступа в режиме моста, задействованы 4 адреса",
    ["Сервер отправляет кадр на AP1", "AP1 передаёт кадр по радио на AP2", "AP2 доставляет кадр компьютеру PC1"])

# ---- wireless bridge principle (36)
bw = ('<circle class="zone o" cx="250" cy="200" r="170"/><circle class="zone v" cx="650" cy="200" r="170"/>'
      '<text class="nl sm" x="150" y="50" text-anchor="middle">зона покрытия AP-1</text><text class="nl sm" x="750" y="50" text-anchor="middle">зона покрытия AP-2</text>')
bw += pc(90, 215, "PC-1") + ap(330, 200, "AP-1") + ap(570, 200, "AP-2") + pc(810, 215, "PC-2", "v")
bw += f'<path class="dr wo an" data-id="b1" pathLength="1" d="{wave(125, 290, 190, 8, 22)}"/>'
bw += f'<path class="dr wo an" data-id="b2" pathLength="1" d="{wave(375, 525, 190, 8, 22)}"/>'
bw += f'<path class="dr wv an" data-id="b3" pathLength="1" d="{wave(615, 775, 190, 8, 22)}"/>'
bw += '<g class="an" data-id="mst"><rect class="bx" x="400" y="110" width="100" height="36" rx="8"/><text class="bxt sm" x="450" y="134" text-anchor="middle">мост</text></g>'
bw += cap("bcap", 450, 400)
BRW = svg("0 0 900 420", bw)
BRW_SC = scene("brw", 4, {"b1": {"c": {0: "", 1: "on"}}, "mst": {"o": {0: 0, 2: 1}}, "b2": {"c": {0: "", 2: "on"}}, "b3": {"c": {0: "", 3: "on"}},
                          "bcap": {"t": {1: "PC-1 передаёт данные на AP-1", 2: "AP-1 в режиме моста передаёт их на AP-2",
                                         3: "AP-2 отправляет данные на PC-2", 4: "PC-2 вне зоны AP-1, но данные дошли"}}}, {1: 1000, 2: 1100, 3: 1000, 4: 900})

# ---- media change (40)
md = ""
NODES = [(60, "PC-1"), (270, "Коммутатор"), (480, "Маршрутизатор"), (690, "Точка доступа"), (880, "PC-2")]
SEG = [("медный кабель", "Ethernet кадр", "cl"), ("медный кабель", "Ethernet кадр", "cl"), ("оптическое волокно", "Ethernet кадр", "ol"), ("радиоволны", "802.11 кадр", "wl")]
for i, (lab, fr, cls) in enumerate(SEG):
    x1, x2 = NODES[i][0] + 45, NODES[i + 1][0] - 45
    md += f'<line class="{cls}" x1="{x1}" y1="220" x2="{x2}" y2="220"/><text class="nl sm" x="{(x1+x2)/2}" y="260" text-anchor="middle">{lab}</text>'
md += pc(60, 235, "PC-1") + sw(270, 220, "Коммутатор") + router(480, 215, "Маршрутизатор") + ap(690, 220, "Точка доступа") + pc(880, 235, "PC-2", "v")
md += ('<g class="an" data-id="mf" style="--md:1100ms"><rect class="frb o" x="-70" y="-22" width="140" height="44" rx="10"/>'
       '<text class="bxt sm" y="7" text-anchor="middle" data-id="mft"></text></g>')
md += cap("mcap", 450, 330)
MED = svg("0 0 940 350", md)
_m = {"mf": {"p": {0: (60, 140)}, "o": {0: 0, 1: 1}}, "mft": {"t": {}}, "mcap": {"t": {}}}
for i, (lab, fr, cls) in enumerate(SEG):
    k = i + 1
    _m["mf"]["p"][k] = ((NODES[i][0] + NODES[i + 1][0]) / 2, 140)
    _m["mft"]["t"][k] = fr; _m["mcap"]["t"][k] = f"{lab}: {fr}"
_m["mf"]["p"][5] = (880, 140); _m["mcap"]["t"][5] = "Пакет тот же, а формат кадра меняется в зависимости от среды"
MED_SC = scene("med", 5, _m, {i: 1300 for i in range(6)})


# ---- CSMA/CD: слушаем среду, ловим коллизию, ждём случайный интервал
def csma_cd(name):
    X = [180, 480, 780]
    g = '<line class="medl an" data-id="cdm" x1="60" y1="300" x2="900" y2="300"/><text class="nl" x="480" y="346" text-anchor="middle">общая среда (один сегмент Ethernet)</text>'
    for i, x in enumerate(X):
        g += f'<line class="ll" x1="{x}" y1="242" x2="{x}" y2="300"/>'
        g += f'<g class="an" data-id="s{i}">' + pc(x, 200, f"Узел {i+1}", ["o", "v", "g"][i]) + '</g>'
        g += f'<text class="tag an" data-id="t{i}" x="{x}" y="118" text-anchor="middle"></text>'
    for n, col in (("fa", "o"), ("fb", "g")):
        g += (f'<g class="an" data-id="{n}" style="--md:900ms"><rect class="frb {col}" x="-58" y="-19" width="116" height="38" rx="10"/>'
              f'<text class="bxt xs" y="6" text-anchor="middle" data-id="{n}t"></text></g>')
    g += f'<g class="an" data-id="cb"><polygon class="burst" points="{star(480,300,30,13)}"/><polygon class="burst2" points="{star(480,300,16,7)}"/></g>'
    g += cap("cdcap", 480, 398)
    els = {"fa": {"p": {0: (180, 300)}, "o": {0: 0}}, "fat": {"t": {}},
           "fb": {"p": {0: (780, 300)}, "o": {0: 0}}, "fbt": {"t": {}},
           "cb": {"o": {0: 0}}, "cdm": {"c": {0: ""}}, "cdcap": {"t": {}}}
    for i in range(3):
        els[f"s{i}"] = {"c": {0: ""}}; els[f"t{i}"] = {"t": {0: ""}}
    T = [  # шаг: (класс узлов, подписи-бейджи, позиции кадров, видимость, вспышка, среда, подпись)
        (["hot", "", ""], ["слушаю среду", "", ""], None, (0, 0), 0, "", "Узел 1 прослушивает несущую: в среде тишина"),
        (["hot", "", ""], ["передаю", "", ""], ((330, 300), None), (1, 0), 0, "busy", "Среда свободна — узел 1 начинает передачу"),
        (["hot", "", "hot"], ["передаю", "", "тоже слышал тишину"], ((380, 300), (620, 300)), (1, 1), 0, "busy", "Узел 3 слышал ту же тишину и начинает передавать"),
        (["hot", "", "hot"], ["коллизия!", "", "коллизия!"], ((440, 300), (560, 300)), (1, 1), 1, "busy", "Сигналы сталкиваются: обе станции слышат искажение — это и есть обнаружение коллизии (CD)"),
        (["wait", "", "wait"], ["jam-сигнал", "", "jam-сигнал"], None, (0, 0), 1, "busy", "Обе шлют короткий jam-сигнал и прекращают передачу"),
        (["wait", "", "wait"], ["жду 2 слота", "", "жду 5 слотов"], None, (0, 0), 0, "", "Каждая отсчитывает свой случайный интервал — поэтому доступ остаётся равноправным"),
        (["hot", "", "wait"], ["передаю", "", "ещё жду"], ((600, 300), None), (1, 0), 0, "busy", "Узел 1 дождался первым и передал кадр уже без коллизии"),
    ]
    for k, (cls, tags, fp, vis, burst, med, capt) in enumerate(T, 1):
        for i in range(3):
            els[f"s{i}"]["c"][k] = cls[i]; els[f"t{i}"]["t"][k] = tags[i]
        if fp:
            if fp[0]: els["fa"]["p"][k] = fp[0]
            if fp[1]: els["fb"]["p"][k] = fp[1]
        els["fa"]["o"][k], els["fb"]["o"][k] = vis
        els["fat"]["t"][k] = "кадр узла 1"; els["fbt"]["t"][k] = "кадр узла 3"
        els["cb"]["o"][k] = burst; els["cdm"]["c"][k] = med
        els["cdcap"]["t"][k] = capt
    els["fa"]["p"][7] = (480, 300)
    return svg("0 0 960 415", g), scene(name, 7, els, {4: 1500, 5: 1400, 6: 1500, 7: 1500})

# ---- CSMA/CA: слушаем эфир, выжидаем DIFS и backoff, получаем ACK
def csma_ca(name):
    g = ap(480, 90, "Точка доступа")
    g += '<line class="medl an" data-id="cam" x1="80" y1="250" x2="880" y2="250"/><text class="nl" x="480" y="296" text-anchor="middle">радиоэфир: коллизию здесь не услышать</text>'
    STA = [(190, "Станция А", "o"), (770, "Станция Б", "v")]
    for i, (x, lab, col) in enumerate(STA):
        g += f'<line class="ll" x1="{x}" y1="250" x2="{x}" y2="322"/>'
        g += f'<g class="an" data-id="a{i}">' + pc(x, 390, lab, col) + '</g>'
        g += f'<text class="tag an" data-id="g{i}" x="{x}" y="335" text-anchor="middle"></text>'
    g += ('<g class="an" data-id="cf" style="--md:900ms"><rect class="frb o" x="-62" y="-19" width="124" height="38" rx="10"/>'
          '<text class="bxt xs" y="6" text-anchor="middle" data-id="cft"></text></g>')
    g += cap("cacap", 480, 462)
    els = {"cf": {"p": {0: (480, 250)}, "o": {0: 0}}, "cft": {"t": {}}, "cam": {"c": {0: ""}}, "cacap": {"t": {}}}
    for i in range(2):
        els[f"a{i}"] = {"c": {0: ""}}; els[f"g{i}"] = {"t": {0: ""}}
    T = [(["wait", "wait"], ["слушаю: занято", "слушаю: занято"], (640, 250), 1, "чужой кадр", "busy",
          "Станция А слушает эфир: идёт чужая передача, канал занят"),
         (["wait", "wait"], ["жду DIFS", "жду DIFS"], (480, 250), 0, "", "",
          "Канал освободился, но сразу никто не передаёт: все выжидают паузу DIFS"),
         (["hot", "wait"], ["счётчик 3", "счётчик 5"], (480, 250), 0, "", "",
          "Дальше каждая станция отсчитывает случайный backoff — у А 3 слота, у Б 5"),
         (["hot", "wait"], ["счётчик 0 — передаю", "замерла на 2"], (330, 180), 1, "кадр станции А", "busy",
          "У А счётчик дошёл до нуля — она передаёт, а Б замораживает свой счётчик"),
         (["hot", "wait"], ["жду ACK", "замерла на 2"], (330, 180), 1, "ACK", "busy",
          "Точка доступа отвечает ACK: кадр принят, иначе А повторила бы передачу"),
         (["wait", "hot"], ["готово", "досчитала — передаю"], (640, 180), 1, "кадр станции Б", "busy",
          "Б досчитывает оставшиеся 2 слота и передаёт следующей — очередь честная"),
         (["", ""], ["", ""], (480, 250), 0, "", "",
          "Коллизия предотвращается заранее: в эфире её нельзя обнаружить, как в кабеле")]
    for k, (cls, tags, fp, vis, ftxt, med, capt) in enumerate(T, 1):
        for i in range(2):
            els[f"a{i}"]["c"][k] = cls[i]; els[f"g{i}"]["t"][k] = tags[i]
        els["cf"]["p"][k] = fp; els["cf"]["o"][k] = vis; els["cft"]["t"][k] = ftxt
        els["cam"]["c"][k] = med; els["cacap"]["t"][k] = capt
    return svg("0 0 960 480", g), scene(name, 7, els, {i: 1500 for i in range(8)})

CDV, CDV_SC = csma_cd("cdv")
CAV, CAV_SC = csma_ca("cav")

# ---------------------------------------------------------------- html helpers
BCOL = ["b0", "b1", "b2", "b3", "b4"]

def badges(items, cls=""):
    return f'<ol class="bl {cls}">' + "".join(
        f'<li><span class="badge {BCOL[i%5]}">{i+1:02d}</span><div>{t}</div></li>' for i, t in enumerate(items)) + '</ol>'

def strip(fields, step=True):
    s = '<div class="strip">'
    for i, (name, size, col) in enumerate(fields):
        st = f' data-s="1" style="--dl:{i*110}ms;flex:{max(1, len(name)/7):.1f}"' if step else ""
        s += f'<div class="fs {col}"{st}><span class="fsz mono">{size}</span><b>{name}</b></div>'
    return s + '</div>'

def p(*paras, cls="p"):
    return "".join(f'<p class="{cls}">{t}</p>' for t in paras)

def two(left, right, cls="two"):
    return f'<div class="{cls}"><div class="txt">{left}</div><div class="vis">{right}</div></div>'

def dgcard(svgc, sc):
    return f'<div class="card dgc" {sc}>{svgc}</div>'

S = []
def slide(label, t1, t2, body, cls=""):
    S.append((label, t1, t2, body, cls))

CAT = {k: cat64(v) for k, v in (("a", "cat.png"), ("b", "cat-1.png"), ("c", "cat-2.png"), ("d", "cat-3.png"))}

# ---------------------------------------------------------------- slides (по 10.pptx)
slide("Титул", "", "", f"""
<div class="title">
  <div class="kick">Глава 10</div>
  <h1>Канальный<br><span class="o2">уровень</span></h1>
  <p class="lead">Кадры, подуровни LLC и MAC, коллизии и методы доступа к среде, кадры Ethernet, PPP и 802.11</p>
  <p class="authors">Ананко Софья Михайловна<br>Качур Анна Юрьевна</p>
  <img class="cat tcat" src="{CAT['d']}" alt="">
</div>""", "tslide")

slide("Цель главы", "Цель", "главы", badges([
    "Информация, передаваемая на канальном уровне;", "Функции канального уровня модели OSI;", "Подуровни канального уровня и их задачи;",
    "Понятие коллизии, способы их минимизации;", "Отличие функционирования канального уровня в проводных и беспроводных сетях."], "big")
    + f'<img class="cat scat" src="{CAT["b"]}" alt="">')

slide("Функции", "Функции", "канального уровня", two(
    p("Канальный уровень является вторым в модели OSI. Его функции включают: выделение границ кадра, передачу сообщений по каналам связи, обнаружение и коррекцию ошибок, аппаратную адресацию. Кроме того, канальный уровень отвечает за контроль потока и контроль среды доступа."),
    badges(["<b>Контроль потока</b> заключается в мониторинге соединения и использовании разных метрик с целью определить, успевает ли принимающее устройство обработать передаваемый трафик. Он применяется для предотвращения переполнения буфера принимающего устройства и потери данных.",
            "<b>Контроль доступа</b> заключается в распределении доступа к среде передачи данных между всеми подключенными к ней устройствами так, чтобы минимизировать вероятность коллизий в сети."])))

slide("Подуровни", "Подуровни", "канального уровня модели OSI", two(
    p("Канальный уровень включает два подуровня:") + badges(["Подуровень логического управления каналом (<b>Logical Link Control – LLC</b>)", "Подуровень управления доступом к среде (<b>Media Access Control – MAC</b>)"], "big"),
    photo("image1.png", "Модель OSI")))

slide("Подуровни: работа", "Подуровни", "приём и передача", two(
    p("Когда на устройство приходят сигналы из среды передачи, они сперва попадают на физический уровень, где происходит преобразование сигналов в нули и единицы. Затем эта последовательность поступает на МАС-подуровень, где из нее формируется кадр и проверяется целостность данного кадра. Далее кадр передается на подуровень LLC, который преобразовывает кадр в пакет. На сетевом уровне осуществляется дальнейшая обработка пакета.",
      "В обратную сторону процесс аналогичен. L3 передает пакет на LLC-подуровень, где происходит инкапсуляция данных в кадр с дальнейшей отправкой на подуровень МАС. Там происходит пересчет контрольной суммы кадра (FCS) и добавление её в концевик кадра. Затем МАС-подуровень отдает кадр на физический уровень в виде последовательности нулей и единиц, а физический уровень преобразует их в сигнал среды.", cls="p sm"),
    dgcard(SUBL, SUBL_SC)))

slide("Связь L1 и L2", "Связь", "физического и канального уровней", two(
    p("Канальный уровень очень тесно связан с физическим уровнем, и некоторые технологии, например, <b>Ethernet</b>, <b>Bluetooth</b> или <b>Wi-Fi</b>, работают на обоих уровнях сразу.",
      "Не случайно в стеке протоколов TCP/IP оба эти уровня объединены в один уровень – <b>доступа к каналу</b>."),
    photo("image4.png", "Ethernet, Bluetooth и Wi-Fi на двух уровнях")))

slide("Управление доступом", "Управление доступом", "к среде передачи данных", two(
    p("При передаче информации по одному каналу данных из разных источников в противоположных направлениях возникает риск взаимного перекрытия сигналов, что может привести к потере данных. Такое явление называется <b>коллизией</b> (от англ. collision – столкновение). Для беспроводных сетей также характерно снижение качества связи, если плохо организовано управление доступом к среде.",
      "Основными методами контроля доступа являются <b>CSMA/CD</b> (множественный доступ с прослушиванием несущей и обнаружением коллизий) для сетей Ethernet и <b>CSMA/CA</b> (множественный доступ с прослушиванием несущей и избежанием коллизий) для беспроводных сетей.", cls="p sm"),
    dgcard(COL7, COL7_SC)))

slide("01 Резервирование времени", "Резервирование", "времени (time reservation)", two(
    p("<b>Резервирование времени</b> (time reservation): каждый узел может пользоваться каналом связи только в отведённый ему промежуток времени.",
      "Время в канале заранее делится на равные слоты, и каждый слот закреплён за конкретным узлом. Пока идёт чужой слот, узел молчит, даже если среда физически свободна. Коллизии при этом невозможны в принципе, но часть пропускной способности теряется: слот «простаивает», если его владельцу нечего передавать.", cls="p sm"),
    dgcard(RES8, RES8_SC)))

slide("02 Селективный метод", "Селективный", "метод (selective method)", two(
    p("<b>Селективный метод</b> (selective method): управляющее устройство сообщает узлам, когда они могут передавать информацию.",
      "Право на передачу раздаёт один выделенный узел-контроллер: он по очереди опрашивает устройства и выдаёт разрешение. Узел без разрешения в среду не выходит, поэтому коллизий нет. Минус — зависимость всей сети от управляющего устройства и накладные расходы на опрос.", cls="p sm"),
    dgcard(SEL8, SEL8_SC)))

slide("03 Случайный доступ", "Метод", "случайного доступа (random access)", two(
    p("<b>Метод случайного доступа</b> (random access methods): устройство само отслеживает состояние среды и пользуется ею при первой возможности. Применяется в Wi-Fi.",
      "Узел прослушивает несущую: если среда свободна — передаёт сразу, если занята — ждёт её освобождения. Централизованного арбитра нет, поэтому метод прост и хорошо масштабируется, но два узла могут начать передачу одновременно — отсюда коллизии и механизмы CSMA/CD и CSMA/CA.", cls="p sm"),
    dgcard(RND8, RND8_SC)))

slide("04 Передача токена", "Передача", "токена (web token)", two(
    p("<b>Передача токена</b> (web token): использовался в топологии Token Ring. Только обладатель токена мог передавать информацию, остальные устройства только принимали.",
      "Специальная метка-токен ходит по кольцу от узла к узлу. Получив её, устройство либо передаёт кадр, либо сразу отдаёт токен дальше. Доступ получается строго честным и без коллизий, но в современных сетях метод практически не используется — его вытеснил коммутируемый Ethernet с полным дуплексом.", cls="p sm"),
    dgcard(TOK8, TOK8_SC)))

slide("Форматирование", "Форматирование", "данных для передачи", p(
    "Одной из функций канального уровня является подготовка кадров к отправке по среде на физическом уровне. В среде вся информация передается в виде импульсов, соответствующих битам. Поэтому принимающему устройству крайне необходимо понимать, с какого именно бита начинается блок информации, предназначенный именно ему, а также сколько бит нужно принять, и какой из принятых бит что означает.",
    "Передающему же устройству необходимо правильно выбрать метод форматирования, чтобы с большей вероятностью принимающее устройство получило переданную информацию на физическом уровне и сформировало из нее кадры. Для этого есть два основных способа.", cls="p lg")
    + '<div class="g2 mt"><div class="card pill"><span class="badge b0">01</span><b>Фиксированная длина</b></div><div class="card pill"><span class="badge b1">02</span><b>Варьирующаяся длина</b></div></div>')

slide("Фиксированная длина", "Форматирование", "фиксированной длины", two(
    p("Форматирование фиксированной длины означает, что каждый кадр имеет одинаковый размер <b class='mono'>X</b> и каждые X байт в потоке представляют собой отдельный кадр. Это позволяет избежать необходимости использования флагов для разделения кадров.",
      "Но, если данные на третьем уровне не достаточны, чтобы заполнить X байт, необходимо добавить последовательности байт, которые не несут никакой информации."),
    dgcard(FIX, FIX_SC)))

slide("Варьирующаяся длина", "Форматирование", "варьирующейся длины", two(
    p("Форматирование варьирующейся длины подразумевает отсутствие фиксированного размера кадров, поэтому необходимо добавлять разграничители. Для этого существуют два метода: включение поля, в котором будет записана длина кадра, или установка флага в конце кадра.",
      "Однако возникают проблемы, если последние биты информативной части кадра совпадают с битами флага. Эта проблема может быть решена путем добавления специальной последовательности бит в данные."),
    dgcard(VAR, VAR_SC)))

slide("Пример: Ethernet", "Пример", "кадр Ethernet 802.3", p("Для примера формата кадра различных технологий можно привести формат кадра Ethernet стандарта 802.3. В таком формате длина полезной нагрузки может изменяться от <b class='mono'>46</b> до <b class='mono'>1500</b> байт.", cls="p lg")
    + strip([("Преамбула", "8 байт", "o"), ("MAC-адрес назначения", "6 байт", "v"), ("MAC-адрес источника", "6 байт", "g"), ("Ether Type", "2 байта", "am"), ("Полезная нагрузка", "46 – 1500 байт", "o"), ("Контр. сумма (FCS)", "4 байта", "pk")]))

slide("Пример: ATM", "Пример", "кадр фиксированной длины ATM", two(
    p("В качестве примера формата кадра фиксированной длины можно упомянуть устаревшую технологию <b>АТМ</b> (Asynchronous Transfer Mode) – асинхронный способ передачи данных.",
      "В ней первые <b class='mono'>5</b> байт составляют заголовок, а полезная нагрузка будет заключена в <b class='mono'>48</b> байтах. В случае если данных не хватит для полного заполнения поля, оно будет дополнено холостой нагрузкой в виде нулей."),
    '<div class="card atm"><div class="atmt mono">1 октет (8 бит)</div>'
    '<div class="fs o big" data-s="1"><b>ЗАГОЛОВОК</b><span class="fsz mono">5 байт</span></div>'
    '<div class="fs v big" data-s="2" style="flex:4"><b>ПОЛЕЗНАЯ НАГРУЗКА</b><span class="fsz mono">48 байт</span></div>'
    '<div class="fs pk big" data-s="3"><b>холостая нагрузка</b><span class="fsz mono">0000…</span></div></div>'))

slide("Полудуплекс", "Доступ к среде", "полудуплексная передача", two(
    p("<b>Полудуплекс</b> (Half Duplex, HDX) предполагает, что в определенный момент времени только один узел может передавать информацию, иначе возникнут коллизии в канале передачи. На протяжении всей истории локальных сетей коллизии стали главным «противником» успешной передачи данных. Они возникают в случае, когда два или более устройства начинают передачу данных одновременно в одной и той же среде.",
      "В первых версиях протокола Ethernet, разработанных для сетей на основе коаксиального кабеля, была возможна передача только от одного устройства всем остальным: в коаксиальном кабеле предусмотрен всего один электрический контур.", cls="p sm"),
    dgcard(COL14, COL14_SC)))

slide("Полный дуплекс", "Доступ к среде", "полнодуплексная передача", two(
    p("Решил данную проблему <b>коммутатор</b>, который пришёл на замену концентратору. Единый домен коллизии сети сократился до небольших доменов, которые заканчивались на портах коммутатора. Устройства, подключенные к одному коммутатору, могут передавать данные одновременно вообще без риска коллизии. Этот вариант был назван «полным дуплексом», а первый стал называться полудуплексом.",
      "<b>Полный дуплекс</b> (Full Duplex, FDX) позволяет обоим устройствам одновременно выполнять прием и передачу данных в канале связи. В сетях с полудуплексным соединением используется метод CSMA/CD для снижения воздействия коллизий.", cls="p sm"),
    dgcard(FDX, FDX_SC)))

slide("Опрос", "Контролируемый доступ", "опрос", two(
    p("При контролируемом доступе узлы опрашивают друг друга, чтобы определить, кто имеет право на отправку. Это позволяет отправлять сообщения только одному узлу за раз, чтобы избежать коллизий. Существует три метода контроля доступа.",
      "<b>Опрос</b>: контролирующее устройство опрашивает узлы по очереди, нужно ли им что-либо отправить."),
    '<div class="card dgc">' + POLL + '</div>'))

slide("Передача метки", "Контролируемый доступ", "передача метки", two(
    p("<b>Передача метки</b>: узлы передают друг другу метку, обладатель которой имеет право пользоваться каналом связи.", "Чаще всего используется в кольцевых топологиях.", cls="p lg"),
    dgcard(TOK, TOK_SC)))

slide("Резервация", "Контролируемый доступ", "резервация", two(
    p("<b>Резервация</b>: узлы резервируют временной слот, в течение которого они могут отправлять информацию.", "Каждый узел может пользоваться каналом связи только в отведённый ему промежуток времени.", cls="p lg"),
    dgcard(RES, RES_SC)))

slide("Коллизии", "Коллизии", "и методы работы с ними", p(
    "Коллизии представляют одну из главных угроз эффективной передаче данных в единой среде с общим доступом.",
    "Одним из первых методов «работы» с коллизиями был протокол <b>CSMA/CD</b> (Carrier Sense Multiple Access with Collision Detection – множественный доступ с контролем несущей и обнаружением коллизий). CSMA/CD определяет порядок действий, которые должно предпринять устройство в результате обнаружения коллизии. В упрощенном виде CSMA/CD работает пошагово.", cls="p lg")
    + f'<img class="cat scat" src="{CAT["c"]}" alt="">')

slide("CSMA/CD", "CSMA/CD", "пошагово", two(
    p("Важно объяснить, почему устройство ожидает именно <b>случайный</b> промежуток времени. Все устройства в сети конкурируют за среду передачи данных; использование определённых моментов времени привело бы к монополизации среды конкретным узлом. Случайность момента времени обеспечивает равноправный доступ к среде.",
      "С появлением коммутаторов и кабелей из более чем одной пары проводников значение CSMA/CD снизилось. Однако с развитием беспроводных сетей проблема коллизий вновь стала актуальной, что привело к появлению протокола CSMA/CA.", cls="p sm"),
    dgcard(CDV, CDV_SC)))

slide("CSMA/CD: шаги", "CSMA/CD", "алгоритм по шагам", two(
    p("Станция не ждёт разрешения и не резервирует время: она просто слушает среду и передаёт, когда та свободна. Коллизия здесь — штатная ситуация, которую протокол умеет распознать и отработать.",
      "Обнаружив искажение сигнала, обе станции обрывают передачу, подают jam-сигнал и расходятся по случайным интервалам ожидания — поэтому среду не монополизирует ни один узел.", cls="p sm"),
    CD))

slide("CSMA/CA", "CSMA/CA", "предотвращение коллизий", two(
    p("<b>CSMA/CA</b> (Carrier-Sense Multiple Access with Collision Avoidance) – множественный доступ с контролем несущей и предотвращением коллизий. Похож на своего предшественника, но концептуально от него отличается.",
      "Вместо реагирования на коллизию, CSMA/CA стремится ее избежать, «работая» на упреждение. Устройство в терминах этого протокола называется <b>станцией</b>."),
    dgcard(CAV, CAV_SC)))

slide("CSMA/CA: шаги", "CSMA/CA", "алгоритм по шагам", two(
    p("Радиостанция не слышит эфир в момент собственной передачи, поэтому обнаружить коллизию, как в кабеле, она не может. Единственный выход — не допустить её: выждать паузу, отсчитать случайный backoff и только потом выйти в эфир.",
      "Подтверждением служит кадр ACK от получателя: если его нет, станция считает кадр потерянным и повторяет попытку.", cls="p sm"),
    CA))

slide("CSMA/CD и CSMA/CA", "Сравнение", "CSMA/CD и CSMA/CA", p("Принципиальное отличие между этими протоколами заключается в их подходе к управлению коллизиями. Протокол CSMA/CD функционирует подобно <b>пожарной бригаде</b>, которая отправляется тушить пожар, тогда как протокол CSMA/CA действует как <b>нормативная система пожарной безопасности</b>, направленная на предотвращение возникновения пожара.", cls="p lg")
    + '<div class="tw card"><table class="tbl"><thead><tr><th>CSMA/CD</th><th>CSMA/CA</th></tr></thead><tbody>'
    + "".join(f'<tr data-s="{i+1}"><td>{a}</td><td>{b}</td></tr>' for i, (a, b) in enumerate([
        ("Используется в проводных сетях", "Используется в беспроводных сетях"), ("Начинает работать после коллизии", "Работает до коллизии"),
        ("Сокращает время восстановления работоспособности сети", "Снижает вероятность коллизии"), ("Возобновляет передачу после устранения коллизии", "Запрашивает разрешение на отправку")]))
    + '</tbody></table></div>')

slide("Кадр: структура", "Кадр", "канала передачи данных", p("Типичный кадр канального уровня состоит из трех элементов: заголовок, информация и концевик.", cls="p lg") + dgcard(GEN, GEN_SC))

slide("Кадр: заголовок", "Кадр", "заголовок, информация, концевик", '<div class="g3">'
    + '<article class="card fc"><span class="badge b0">01</span><h3>Заголовок (header)</h3><p>«Управляющая информация» – первоначальные инструкции, как с этим кадром обращаться:</p><ul class="dl"><li><b>Разделитель начала кадра</b> (start frame delimiter) – дать понять принимающему устройству, что начинается передача.</li><li><b>Destination MAC и Source MAC</b> – могут не быть обязательными для некоторых протоколов.</li><li><b>Тип передаваемых данных</b> – какому протоколу L3 передать данные.</li></ul></article>'
    + '<article class="card fc"><span class="badge b1">02</span><h3>Информация</h3><p>Пакет уровня L3, вложенный в кадр.</p></article>'
    + '<article class="card fc"><span class="badge b2">03</span><h3>Концевик (trailer)</h3><ul class="dl"><li><b>Поле контроля правильности передачи</b>: на кадр может повлиять что угодно – от включенной за стеной микроволновки до скачков напряжения. Например, поле FCS в кадре Ethernet рассчитывает передающее устройство, а затем принимающее; если значения совпадают, кадр принят корректно, иначе отбрасывается.</li><li><b>Разделитель конца кадра</b> – необязателен, так как иногда длина кадра указывается в заголовке.</li></ul></article></div>')

slide("Адресация L2", "Адресация", "канального уровня", two(
    p("Наиболее популярным методом адресации на канальном уровне являются <b>MAC-адреса</b> (подробно – в главе 4). Помимо стандартного 48-битового адреса существует еще 64-битный, разработанный для работы совместно с IPv6.",
      "MAC-адрес не является единственным вариантом. В протоколе <b>PPP</b> поле адреса занимает всего 1 байт и выглядит как 8 единиц (<span class='mono'>0хFF</span>), являясь широковещательным адресом: в одном канале не может одновременно существовать более 2 устройств, поэтому кадр будет получен исключительно одним соседним устройством."),
    photo("image20.png", "Адресация Ethernet и PPP")))

slide("Концевик кадра", "Концевик", "кадра", two(
    p("Концевик кадра включает в себя контрольную сумму кадра, используемую для обнаружения ошибок при передаче, и флаг, обозначающий конец отдельного кадра.",
      "Если контрольная сумма, вычисленная устройством при получении кадра, не совпадает с суммой, содержащейся в концевике, кадр отбрасывается. В большинстве случаев пропажа кадра не остается незамеченной протоколами верхних уровней. Если протокол TCP не получит подтверждения получения сегмента, он отправит его снова."),
    dgcard(FCS, FCS_SC)))

slide("Ethernet 802.3", "Кадр", "Ethernet 802.3", two(
    p("На сегодня стандарт <b>Ethernet</b> является самым распространенным стандартом для построения локальных сетей в мире.",
      "Стандарт IEEE 802.3 был впервые опубликован в <b class='mono'>1983</b> году, но первая экспериментальная реализация протокола Ethernet создана была в <b class='mono'>1973</b> году.", cls="p lg"),
    photo("image22.png", "Формат кадра Ethernet II (Ethernet DIX v2.0)")))

slide("Поля Ethernet II", "Поля кадра", "Ethernet II", strip([("Преамбула", "8 байт", "o"), ("MAC назначения", "6 байт", "v"), ("MAC источника", "6 байт", "g"), ("EtherType", "2 байта", "am"), ("Полезная нагрузка", "46 – 1500 байт", "o"), ("FCS", "4 байта", "pk")])
    + '<div class="g3 mt">' + "".join(f'<article class="card fc"><span class="badge {BCOL[i%5]}">{i+1:02d}</span><h3>{h}</h3><p>{t}</p></article>' for i, (h, t) in enumerate([
        ("Преамбула (Preamble), 8 байт", "Последовательность чередующихся нулей и единиц длиной 64 бита. «Дает понять» соседям по сети о начале передачи кадра."),
        ("MAC-адрес назначения, 6 байт", "Адрес получателя. Предшествует адресу источника, чтобы коммутатор или маршрутизатор мог скорее сравнить его со своим и решить, обрабатывать кадр или сразу отбросить."),
        ("MAC-адрес источника, 6 байт", "Адрес устройства-отправителя."),
        ("EtherType, 2 байта", "Код протокола, инкапсулированного в поле «полезная нагрузка». Номера – на странице IANA IEEE 802 Numbers."),
        ("Полезная нагрузка, 46 – 1500 байт", "Пакет уровня L3 или данные протоколов уровня L2, например, протокола ARP."),
        ("Контрольная сумма, 4 байта", "Обнаружение ошибок: если значение отличается от вычисленного получателем, кадр отбрасывается.")])) + '</div>', "tight")

slide("Ethernet 802.3: поля", "Кадр", "IEEE 802.3: дополнительные поля", p("В 1983 году был выпущен официальный стандарт Ethernet – IEEE 802.3, принятый ISO в качестве официального стандарта для систем Ethernet.")
    + strip([("Преамбула", "7 байт", "o"), ("SFD", "1 байт", "pk"), ("MAC назначения", "6 байт", "v"), ("MAC источника", "6 байт", "g"), ("802.1Q", "4 байта", "gr"), ("EtherType", "2 байта", "am"), ("Полезная нагрузка", "46 – 1500 байт", "o"), ("FCS", "4 байта", "pk"), ("IPG", "12 байт", "am")])
    + '<div class="g3 mt">' + "".join(f'<article class="card fc"><span class="badge {BCOL[i%5]}">{i+1:02d}</span><h3>{h}</h3><p>{t}</p></article>' for i, (h, t) in enumerate([
        ("SFD, 1 байт", "Разделитель начала кадра (Start Frame Delimiter). Указывает на начало кадра, отделяет преамбулу от начала передачи самого кадра."),
        ("802.1Q (опционально), 4 байта", "Тег приоритетности кадра (802.1p) и идентификатор виртуальной локальной сети (VLAN), к которой он относится."),
        ("IPG, 12 байт", "Межпакетный интервал (InterPacket Gap): пауза в микро- или наносекундах для подготовки приемника к приему следующего кадра.")])) + '</div>')

slide("Кадр PPP", "Кадр", "Point-to-Point (PPP)", p("Протокол «точка-точка» используется для установления соединения между двумя узлами напрямую.")
    + strip([("Флаг", "1 байт", "pk"), ("Адрес", "1 байт", "v"), ("Управление", "1 байт", "g"), ("Протокол", "2 байта", "am"), ("Данные", "до 1494 байт", "o"), ("FCS", "2 – 4 байта", "pk"), ("Флаг", "1 байт", "pk")])
    + '<div class="g3 mt">' + "".join(f'<article class="card fc"><span class="badge {BCOL[i%5]}">{i+1:02d}</span><h3>{h}</h3><p>{t}</p></article>' for i, (h, t) in enumerate([
        ("Флаг, 1 байт", "Метки начала и конца кадра (<span class='mono'>01111110</span>)."),
        ("Адрес, 1 байт", "PPP не использует уникальные адреса узлов: поле всегда содержит <span class='mono'>11111111</span>. В обмене участвует только два устройства."),
        ("Управление, 1 байт", "Зарезервировано для будущих изменений. Должно содержать <span class='mono'>00000011</span>, иначе кадр будет отброшен."),
        ("Протокол, 2 байта", "Идентификатор протокола, инкапсулированного в кадре."),
        ("Данные, до 1494 байт", "Информация, инкапсулированная в кадре, переменной длины."),
        ("FCS, 2 – 4 байта", "Обнаружение ошибок при передаче кадра.")])) + '</div>', "tight")

slide("Кадр 802.11", "Беспроводной", "кадр 802.11", p("Строение кадра стандарта 802.11 гораздо более сложное, нежели строение кадра Ethernet. Это обусловлено сложностью передачи информации в беспроводной среде, а также наличием промежуточного сетевого устройства (точки доступа). В стандарте 802.11 определено 4 типа кадров:")
    + '<div class="g2">' + "".join(f'<article class="card fc" data-s="{i+1}"><span class="badge {BCOL[i%5]}">{i+1:02d}</span><h3>{h}</h3><p>{t}</p></article>' for i, (h, t) in enumerate([
        ("Data frames", "Кадры, содержащие данные. Предназначены для передачи данных от передатчика к приемнику."),
        ("Management frames", "Служебные кадры. Используются для управления базовыми станциями."),
        ("Control frames", "Управляющие кадры. При нормальном обмене данными между станциями происходит передача кадров с данными."),
        ("Extension Frames", "Расширенные кадры. Добавлены в стандарт 802.11ad, который определяет использование Wi-Fi на частоте 60 ГГц.")])) + '</div>')

F80211 = [("FC", "2", "o"), ("Duration / ID", "2", "am"), ("MAC-адрес 1", "6", "v"), ("MAC-адрес 2", "6", "v"), ("MAC-адрес 3", "6", "v"), ("Seq Control", "2", "g"),
          ("MAC-адрес 4", "6", "v"), ("QoS Control", "2", "gr"), ("HT Control", "4", "gr"), ("Frame Body", "0 – 2304", "o"), ("FCS", "4", "pk")]
slide("Поля 802.11", "Структура", "кадра IEEE 802.11", strip(F80211) + p("Размеры полей указаны в байтах.", cls="p sm dimp")
    + '<div class="g3 mt">' + "".join(f'<article class="card fc"><span class="badge {BCOL[i%5]}">{i+1:02d}</span><h3>{h}</h3><p>{t}</p></article>' for i, (h, t) in enumerate([
        ("Frame Control", "Содержит 11 подполей, определяющих параметры соединения."),
        ("Duration/Id, 2 байта", "Зависит от типа и подтипа кадра и QoS. «Длительность» – как долго будет занята среда (мкс); в определенных случаях – идентификатор."),
        ("MAC-адреса 1 – 4, по 6 байт", "MAC-адреса узлов, используемых для передачи и приема данных."),
        ("Sequence Control", "Два подполя – порядковый номер (12 бит) и номер фрагмента (4 бита)."),
        ("QoS Control, 2 байта", "Категория или поток трафика и другая информация, связанная с качеством обслуживания."),
        ("HT Control, 4 байта", "Оптимизация передачи: состояние канала для адаптивного изменения скорости."),
        ("Frame Body, 0 – 2304 байт", "Передаваемые данные, инкапсулированные в кадр."),
        ("FCS", "Контрольная сумма для обнаружения ошибок при передаче кадра.")])) + '</div>', "tight")

FC_SUB = [("Version", "2", "o"), ("Type", "2", "am"), ("Subtype", "4", "am"), ("To DS", "1", "v"), ("From DS", "1", "v"), ("MF", "1", "g"),
          ("Retry", "1", "g"), ("PM", "1", "gr"), ("More Data", "1", "gr"), ("PF", "1", "pk"), ("+HTC", "1", "pk")]
slide("Frame Control 1", "Поле", "«Управление кадром»: часть 1", strip(FC_SUB) + p("Размеры подполей указаны в битах.", cls="p sm dimp")
    + '<div class="g3 mt">' + "".join(f'<article class="card fc"><span class="badge {BCOL[i%5]}">{i+1:02d}</span><h3>{h}</h3><p>{t}</p></article>' for i, (h, t) in enumerate([
        ("Version, 2 бита", "Версия протокола может принимать значения 00 и 01."),
        ("Type, 2 бита", "Тип кадра: управляющий, служебный, кадр с данными, расширенный."),
        ("Subtype, 4 бита", "Подтип поля Type: RTS, CTS, ACK и др."),
        ("To DS, 1 бит", "Трафик передается от оконечного устройства к системе распределения."),
        ("From DS, 1 бит", "Трафик передается от системы распределения к оконечному устройству.")])) + '</div>')

slide("Frame Control 2", "Поле", "«Управление кадром»: часть 2", strip(FC_SUB) + '<div class="g3 mt">' + "".join(f'<article class="card fc"><span class="badge {BCOL[i%5]}">{i+1:02d}</span><h3>{h}</h3><p>{t}</p></article>' for i, (h, t) in enumerate([
        ("More Fragments, 1 бит", "За этим кадром следует еще один, содержащий фрагмент того же пакета. Работает в связке с Sequence Control."),
        ("Retry, 1 бит", "Кадр пересылается повторно: получение прошлого не было подтверждено."),
        ("Pwr Mgmt, 1 бит", "Отправитель включил режим экономии энергии (1) или выключил (0)."),
        ("More Data, 1 бит", "У отправителя это не последний кадр в пересылаемой серии."),
        ("Protected Frame, 1 бит", "В теле кадра используется шифрование."),
        ("+HTC, 1 бит", "«1»: передатчик способен принимать VHT-вариант поля HT Control.")])) + '</div>')

slide("Sequence Control", "Поле", "Sequence Control", two(
    p("Следующее поле – контроль порядка (Sequence control). В нем находится два подполя:") + badges([
        "<b>Номер фрагмента</b> (Fragment Number). Когда кадр необходимо разделить на более мелкие составляющие, каждой из них присваивается свой номер, по которым последовательность собирается обратно в единый кадр.",
        "<b>Порядковый номер</b> (Sequence Number). Используется для нумерации передаваемых кадров, позволяет точно идентифицировать каждый кадр в процессе передачи."]),
    '<div class="card atm"><div class="atmt mono">Sequence Control, 2 байта</div><div class="rowf"><div class="fs am big" data-s="1"><b>FN</b><span class="fsz mono">4 бита</span></div>'
    '<div class="fs g big" data-s="2" style="flex:3"><b>Sequence Number</b><span class="fsz mono">12 бит</span></div></div></div>'))

slide("Система распределения", "Система", "распределения (Distribution System)", two(
    p("Под данным определением понимается одно или несколько устройств, с помощью которых несколько точек доступа объединяются в одну общую сеть. На рисунке роль системы распределения выполняет коммутатор <b>SW-1</b>.",
      "Когда точки доступа находятся в обоюдной зоне покрытия, то есть «достают» друг до друга, общую сеть можно реализовать без дополнительного устройства, соединив точки доступа в режиме <b>беспроводного моста</b>."),
    photo("image28.png", "Пример системы распределения")))

slide("Беспроводной мост", "Беспроводной", "мост", two(
    p("<b>Беспроводной мост</b> – это режим точки доступа, в котором она выполняет функцию передачи сигнала через себя до другой точки доступа.",
      "Компьютеру PC-1 необходимо передать данные на компьютер PC-2. Зоны покрытия точки доступа АР-1 не хватает для передачи данных на такое расстояние. Но благодаря режиму моста PC-1 передает данные на АР-1, затем данные отправляются на АР-2 и уже после нее достигают узла назначения РС-2."),
    dgcard(BRW, BRW_SC)))

slide("To DS", "To DS", "от устройства к системе распределения", two(
    p("Система из маршрутизатора R1, коммутатора SW1, точки доступа AP и смартфона. Мы хотим передать кадр со смартфона во внешнюю сеть.",
      "В поле <b>To DS</b> ставится 1, флаг <b>From DS</b> остается 0. Первым адресом ставится МАС-адрес точки доступа как адрес приемника (Receiver Address). Далее – МАС-адрес смартфона как источника (Source Address) и передатчика (Transmitter Address). Третьим адресом будет МАС-адрес маршрутизатора R1 как адрес назначения (Destination Address).", cls="p sm"),
    dgcard(TODS, TODS_SC)))

slide("From DS", "From DS", "от системы распределения к устройству", two(
    p("Аналогичная схема, но отправка кадра происходит от системы распределения к устройству.",
      "Во флаге <b>From DS</b> ставим 1, флаг <b>To DS</b> остается 0. Первым адресом ставится МАС-адрес смартфона как получателя (Destination Address) и приемника (Receiver Address). Вторым – адрес точки доступа как передатчика (Transmitter Address). Третьим – МАС-адрес маршрутизатора как адрес источника (Source Address).", cls="p sm"),
    dgcard(FROMDS, FROMDS_SC)))

slide("To DS + From DS", "To DS, From DS", "беспроводной мост", two(
    p("Когда в обоих флагах To DS и From DS стоят 1, узлы передачи и приема связаны между собой точками доступа в режиме моста. В кадре будут задействованы <b>четыре</b> различных МАС-адреса.",
      "Сервер отправляет кадр: его MAC-адрес отправителя указывается в <b>четвертом</b> поле адреса; MAC-адрес компьютера получателя – в <b>третьем</b>. MAC-адрес точки доступа отправителя как передатчика – во <b>втором</b> поле, а точки доступа получателя как приемника – в <b>первом</b>.", cls="p sm"),
    dgcard(BRIDGE, BRIDGE_SC)))

slide("Форматы для сред", "Форматы кадров", "для различных сред передачи", two(
    p("На канальном уровне данные инкапсулируются в кадр (L2), который может содержать пакет (L3). При передаче через различные среды каждый новый кадр, созданный для пересылки пакета, имеет свой формат, адаптированный под особенности конкретной среды.",
      "Для медных кабелей часто используется Ethernet, формат кадра которого отличен от формата 802.11 для радиоволн. Кроме того, для связи двух устройств может применяться протокол PPP, в котором отсутствует адресация передающего и принимающего устройств.", cls="p sm"),
    dgcard(MED, MED_SC)))

slide("Ethernet: история", "Протокол", "Ethernet", two(
    p("<b>Ethernet</b> – семейство технологий, отвечающих за передачу данных по кабелю в компьютерных сетях. Днем появления Ethernet считается <b>22 мая 1973</b> года: Роберт Меткалф (Robert Metcalfe) и Дэвид Боггс (David Boggs) опубликовали описание экспериментальной сети, построенной в Исследовательском центре Xerox. Передача данных осуществлялась по толстому коаксиальному кабелю со скоростью 2,94 Мбит/с. Имя Ethernet – сокращение от The Ether Network (Эфирная сеть).",
      "В 1983 году IEEE выпустил официальный стандарт Ethernet – IEEE 802.3. Ethernet функционирует на физическом и канальном уровнях: на физическом определяются типы среды, методы кодирования, разъемы; на канальном – формат кадров и протоколы управления доступом к среде.", cls="p sm"),
    badges(["Ethernet – 10 Мб/с", "Fast Ethernet – 100 Мб/с", "Gigabit Ethernet – 1 Гб/с", "10G Ethernet – 10 Гб/с", "40GbE и 100GbE – 40 и 100 Гб/с", "400GbE – 400 Гб/с"], "sm")))

slide("Ethernet: таблица", "Протокол", "Ethernet: модификации", p("В качестве передающей среды используется коаксиальный кабель, витая пара и оптический кабель.")
    + '<div class="tw card"><table class="tbl"><thead><tr><th>Технология</th><th>Модификация</th><th>Скорость</th><th>Кабель</th></tr></thead><tbody>'
    + "".join(f'<tr data-s="{i+1}"><td>{a}</td><td class="mono">{b}</td><td class="mono">{c}</td><td>{d}</td></tr>' for i, (a, b, c, d) in enumerate([
        ("Ethernet", "10Base-5", "10 Мбит/с", "Толстый коаксиальный"), ("Ethernet", "10Base-2", "10 Мбит/с", "Тонкий коаксиальный"),
        ("Ethernet", "10Base-T", "10 Мбит/с", "Витая пара"), ("Ethernet", "10Base-F", "10 Мбит/с", "Оптоволоконный"),
        ("Fast Ethernet", "100Base-T", "100 Мбит/с", "Витая пара"), ("Fast Ethernet", "100Base-FX", "100 Мбит/с", "Оптоволоконный"),
        ("Gigabit Ethernet", "1000Base-T", "1 Гбит/с", "Витая пара категории 5e"), ("10G Ethernet", "10GBase-T", "10 Гбит/с", "Витая пара категории 6 и оптоволоконный")]))
    + '</tbody></table></div>', "tight")

slide("Стандарты", "Стандарты", "канального уровня", two(
    p("Наиболее распространёнными стандартами канального уровня являются стандарты <b>IEEE 802.x</b>.",
      "Только 802.2 описывает программную реализацию функций канального уровня, все остальные – варианты реализации подуровня MAC, аппаратную часть уровня.",
      "При реализации канального уровня используются только стандарты, утвержденные международными организациями (ISO, IEEE, ITU), а не, например, RFC IETF."),
    '<div class="stds">' + "".join(f'<div class="card std" data-s="1" style="--dl:{i*90}ms"><b class="mono">{a}</b><span>{b}</span></div>' for i, (a, b) in enumerate([
        ("802.2", "Logical Link Control (LLC)"), ("802.3", "Ethernet"), ("802.4", "Token Bus"), ("802.5", "Token Ring"),
        ("802.11", "Wireless LAN"), ("802.15", "WPAN (Bluetooth)"), ("802.16", "WMAN")])) + '</div>'))

# ---------------------------------------------------------------- trainers & quiz
slide("Тренажёр: доступ", "Тренажёр", "CSMA/CD или CSMA/CA", '<div class="two"><div class="card trn">'
    '<div class="tq" id="t1-q"></div><div class="opts" id="t1-o"></div><div class="tres" id="t1-r" aria-live="polite"></div>'
    '<div class="trow"><button class="btn" id="t1-nx" type="button">Следующее утверждение</button><span class="mono dimp" id="t1-sc">0 / 0</span></div></div>'
    f'<div class="catbox"><img class="cat" src="{CAT["a"]}" alt=""></div></div>')

slide("Тренажёр: адреса 802.11", "Тренажёр", "адреса в кадре 802.11", '<div class="two"><div class="card trn">'
    '<div class="tq" id="t2-q"></div><div class="opts col" id="t2-o"></div><div class="tres" id="t2-r" aria-live="polite"></div>'
    '<div class="trow"><button class="btn" id="t2-nx" type="button">Новый вопрос</button><span class="mono dimp" id="t2-sc">0 / 0</span></div></div>'
    '<div class="card trn"><div class="tq" id="t3-q"></div><div class="opts" id="t3-o"></div><div class="tres" id="t3-r" aria-live="polite"></div>'
    '<button class="btn" id="t3-nx" type="button">Другое поле</button></div></div>')

QUIZ = [
    {"q": "Какие два подуровня включает канальный уровень?", "o": ["LLC и MAC", "MAC и IP", "LLC и TCP", "PHY и MAC"], "a": 0,
     "e": "Подуровень логического управления каналом (LLC) и подуровень управления доступом к среде (MAC)."},
    {"q": "На каком подуровне пересчитывается контрольная сумма кадра (FCS) при передаче?", "o": ["LLC", "MAC", "Сетевом", "Физическом"], "a": 1,
     "e": "На подуровне МАС происходит пересчет FCS и добавление её в концевик кадра."},
    {"q": "Какой метод доступа используется в беспроводных сетях?", "o": ["CSMA/CD", "CSMA/CA", "Передача токена", "Полный дуплекс"], "a": 1,
     "e": "CSMA/CA – для беспроводных сетей, CSMA/CD – для сетей Ethernet."},
    {"q": "Почему в CSMA/CD устройство ждёт именно случайный промежуток времени?", "o": ["Так быстрее", "Чтобы обеспечить равноправный доступ к среде", "Так требует IEEE", "Чтобы пересчитать FCS"], "a": 1,
     "e": "Определённые моменты времени привели бы к монополизации среды конкретным узлом. Случайность обеспечивает равноправный доступ."},
    {"q": "Сколько байт заголовка и полезной нагрузки в кадре ATM?", "o": ["5 и 48", "8 и 46", "14 и 1500", "1 и 1494"], "a": 0,
     "e": "Первые 5 байт составляют заголовок, полезная нагрузка – 48 байт; недостающее дополняется нулями."},
    {"q": "Что содержит поле «Адрес» в кадре PPP?", "o": ["MAC-адрес получателя", "11111111 – широковещательный адрес", "IP-адрес", "00000011"], "a": 1,
     "e": "PPP не использует уникальные адреса узлов: поле всегда содержит 11111111. 00000011 – поле «Управление»."},
    {"q": "Кадр 802.11 от смартфона во внешнюю сеть. Какие значения флагов?", "o": ["To DS = 0, From DS = 1", "To DS = 1, From DS = 0", "To DS = 1, From DS = 1", "To DS = 0, From DS = 0"], "a": 1,
     "e": "От устройства к системе распределения: To DS = 1, From DS = 0."},
    {"q": "Что происходит с кадром, если контрольная сумма не совпала?", "o": ["Кадр исправляется", "Кадр отбрасывается, TCP отправит сегмент снова", "Кадр пересылается дальше", "Отправляется Time Exceeded"], "a": 1,
     "e": "Кадр отбрасывается. Если TCP не получит подтверждения получения сегмента, он отправит его снова."},
]
slide("Проверь себя", "Проверь", "себя", '<div class="two quizrow"><div class="card quiz">'
    '<div class="qtop mono"><span id="qz-n">1 / 8</span><span id="qz-sc">верно: 0</span></div><div class="tq" id="qz-q"></div>'
    '<div class="opts col" id="qz-o"></div><div class="tres" id="qz-e" aria-live="polite"></div>'
    '<div class="trow"><button class="btn" id="qz-pv" type="button">Предыдущий</button><button class="btn pri" id="qz-nx" type="button">Следующий вопрос</button></div></div>'
    f'<div class="catbox"><img class="cat" src="{CAT["c"]}" alt=""></div></div>')

# ---------------------------------------------------------------- CSS
CSS = r"""
:root{--paper:#fbf9f7;--card:#fff;--line:#e7e4e0;--ink:#14161c;--dim:#5c6270;
  --orange:#f2600c;--amber:#f6a623;--violet:#6f52a8;--green:#6f9e55;--grey:#7a8291;--pinkish:#e0527a;
  --f:"Golos Text","Inter","Manrope","Segoe UI",system-ui,sans-serif;--mono:"JetBrains Mono","Cascadia Mono","Consolas",ui-monospace,monospace;
  --r:16px;--ez:cubic-bezier(.22,.7,.3,1);color-scheme:light}
*{box-sizing:border-box;margin:0;padding:0}
html{font-size:clamp(14px,min(1.02vw,1.86vh),28px)}
html,body{height:100%;overflow:hidden;background:var(--paper);color:var(--ink);font-family:var(--f)}
.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}
#deco{position:fixed;inset:0;z-index:0;pointer-events:none;width:100%;height:100%}
#prog{position:fixed;left:0;top:0;height:4px;width:100%;z-index:30;background:var(--line)}
#prog i{display:block;height:100%;width:0;background:var(--orange);transition:width .3s var(--ez)}
.slide{position:fixed;inset:0;z-index:1;display:none}.slide.on{display:block}
.sc{height:100%;overflow-y:auto;overflow-x:hidden;display:flex;flex-direction:column;padding:clamp(20px,6vh,72px) clamp(16px,6vw,130px) calc(5rem + 12px);scrollbar-width:thin}
.tight .sc{padding-top:clamp(14px,4vh,44px)}
.wrap{margin:auto;width:100%;max-width:100rem;position:relative}
.sh{margin-bottom:1.3rem}
h2{font-size:2.4rem;line-height:1.02;font-weight:900;text-transform:uppercase;letter-spacing:-.01em}
h2 .o2{display:block;color:var(--orange)}
.tight h2{font-size:2rem}
h3{font-size:1.08rem;font-weight:800;margin:.5rem 0 .4rem;line-height:1.25}
.p{font-size:1.18rem;line-height:1.55;margin-bottom:.9rem;max-width:66ch}
.p.lg{font-size:1.4rem;max-width:none}.p.sm{font-size:1.02rem;margin-bottom:.7rem}
.dimp{color:var(--dim)}
.mt{margin-top:1rem}
.two{display:grid;grid-template-columns:minmax(0,1fr);gap:1.4rem 2.6rem;align-items:center}
.g2,.g3{display:grid;grid-template-columns:minmax(0,1fr);gap:1rem}
.card{background:var(--card);border:1.5px solid var(--line);border-radius:var(--r)}
.dgc{padding:1rem 1.2rem}
.dg{display:block;width:100%;height:auto;max-height:66vh;overflow:visible}
.ph{padding:.6rem;margin:0}.ph img{display:block;width:100%;height:auto;max-height:64vh;object-fit:contain;border-radius:10px}
.ph figcaption{font-size:.85rem;color:var(--dim);padding:.5rem .3rem 0}
/* badges */
.badge{flex:none;display:inline-grid;place-items:center;min-width:2.3em;height:1.9em;padding:0 .35em;border-radius:6px;color:#fff;font-weight:800;font-family:var(--mono);font-size:.85em}
.b0{background:var(--orange)}.b1{background:var(--amber)}.b2{background:var(--violet)}.b3{background:var(--green)}.b4{background:var(--grey)}
.bl{list-style:none;display:flex;flex-direction:column;gap:.9rem}
.bl li{display:flex;gap:.9rem;align-items:flex-start;font-size:1.15rem;line-height:1.45}
.bl.big li{font-size:1.5rem;align-items:center}.bl.sm li{font-size:1rem}
.fc{padding:1.1rem 1.2rem}.fc p,.fc li{font-size:.98rem;line-height:1.45}
.dl{padding-left:1.1rem;display:flex;flex-direction:column;gap:.4rem;margin-top:.4rem}
.pill{display:flex;gap:1rem;align-items:center;padding:1rem 1.2rem;font-size:1.3rem}
/* strips */
.strip{display:flex;gap:.35rem;flex-wrap:wrap}
.fs{flex:1;min-width:6.5rem;display:flex;flex-direction:column;gap:.25rem;padding:.6rem .7rem;border-radius:10px;border:2px solid var(--c);background:color-mix(in srgb,var(--c) 12%,#fff)}
.fs b{font-size:.92rem;line-height:1.2}.fsz{font-size:.78rem;color:var(--dim)}
.fs.big{padding:1rem 1.2rem}.fs.big b{font-size:1.2rem}
.o{--c:var(--orange)}.am{--c:var(--amber)}.v{--c:var(--violet)}.g{--c:var(--green)}.gr{--c:var(--grey)}.pk{--c:var(--pinkish)}
.atm{padding:1.2rem;display:flex;flex-direction:column;gap:.6rem}.atmt{color:var(--dim);font-size:.9rem}
.rowf{display:flex;gap:.5rem}
.stds{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:.7rem}
.std{padding:.9rem 1rem;display:flex;flex-direction:column;gap:.2rem}.std b{color:var(--orange);font-size:1.4rem}
/* tables */
.tw{overflow-x:auto}.tbl{width:100%;border-collapse:collapse;font-size:1.05rem}
.tbl th,.tbl td{text-align:left;padding:.6rem 1rem;border-bottom:1px solid var(--line)}
.tbl thead th{background:var(--ink);color:#fff;font-weight:800;text-transform:uppercase;font-size:.9rem;letter-spacing:.04em}
/* flow */
.flowcard{padding:1.2rem}
.flow{display:flex;flex-direction:column;gap:.55rem}
.fb{display:flex;gap:.8rem;align-items:center;padding:.65rem .9rem;border:2px solid var(--line);border-radius:12px;font-size:1.05rem;transition:border-color .28s,background .28s,opacity .28s}
.fb.hot{border-color:var(--orange);background:#fff1e8}
.fb.done{opacity:.75}
.fcap{margin-top:.8rem;min-height:1.6em;font-weight:700;font-size:1.1rem;color:var(--orange)}
/* reveal engine */
[data-s]{opacity:0;transform:translateY(10px);transition:opacity 280ms var(--ez) var(--dl,0ms),transform 280ms var(--ez) var(--dl,0ms)}
[data-s].in{opacity:1;transform:none}
tr[data-s],svg [data-s]{transform:none}
.arr[data-s]{opacity:1}
.arr .draw{fill:none;stroke:var(--c);stroke-width:3.5;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset 700ms linear}
.arr.in .draw{stroke-dashoffset:0}
.arr .head{fill:var(--c);opacity:0;transition:opacity 90ms linear 650ms}.arr.in .head{opacity:1}
.arr .lbl{fill:var(--c);font-size:20px;font-weight:800;opacity:0;transition:opacity 280ms var(--ez) 600ms;text-transform:uppercase}.arr.in .lbl{opacity:1}
.c-o{--c:var(--orange)}.c-v{--c:var(--violet)}
.an{transition:transform var(--md,1000ms) cubic-bezier(.45,.05,.35,1) var(--dl,0ms),opacity 280ms var(--ez)}
.dr{fill:none;stroke-width:4;stroke-linecap:round;stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset 900ms linear}
.dr.on{stroke-dashoffset:0}.wo{stroke:var(--orange)}.wv{stroke:var(--violet)}
.ni,.ni *{transition:none!important}
.flash{animation:fl 700ms var(--ez) 1}@keyframes fl{0%{opacity:.2}100%{opacity:1}}
/* svg */
.dg text{font-family:var(--f);fill:var(--ink);font-size:20px}
.dg .nl{font-size:17px;font-weight:700}.dg .nl.sm{font-size:15px;font-weight:600;fill:var(--dim)}
.dg .cap{font-size:21px;font-weight:800;fill:var(--orange)}
.pcb{fill:#fff;stroke:var(--ink);stroke-width:3}.pc.o .pcs{fill:var(--orange)}.pc.v .pcs{fill:var(--violet)}.pc.g .pcs{fill:var(--green)}.pcs{fill:var(--orange)}
.hot .pcb{stroke:var(--orange);stroke-width:5}
.medl{stroke:var(--grey);stroke-width:6;stroke-linecap:round;transition:stroke 400ms}.medl.busy{stroke:var(--orange)}
.wait .pcb{stroke:var(--grey);stroke-width:3;opacity:.55}
.cellb{fill:#fff;stroke:#e3ddd4;stroke-width:2;transition:fill 300ms,stroke 300ms,opacity 300ms}
.cellb.on{fill:#fff1e8;stroke:var(--orange);stroke-width:3}.cellb.mute{opacity:.35}
.rx .pcb{stroke:var(--violet);stroke-width:5}
.dg .bxt.xs{font-size:17px}
.dg .tag{font-size:19px;font-weight:800;fill:var(--ink);opacity:.85}
.burst{fill:var(--orange)}.burst2{fill:#ffd23f}
.an[data-id="bst"]{transform-origin:450px 180px;animation:bpulse 900ms ease-in-out infinite}
@keyframes bpulse{0%,100%{transform:scale(1)}50%{transform:scale(1.14)}}
.dr.lost{opacity:.3}
.lblo{fill:var(--orange)!important;font-weight:800}.lblv{fill:var(--violet)!important;font-weight:800}
.lay{stroke-width:2}.lay.o{fill:#fff1e8;stroke:var(--orange)}.lay.vio{fill:#efeaf7;stroke:var(--violet)}.lay.am{fill:#fff6e6;stroke:var(--amber)}
.dg .layk{font-family:var(--mono);font-weight:900;font-size:26px}.dg .layt{font-size:19px;font-weight:600}
.tokb{fill:var(--ink)}.dg .tokt{fill:#fff;font-weight:800;font-size:19px}
.node{stroke-width:2.5}.node.o{fill:#fff1e8;stroke:var(--orange)}.node.v{fill:#efeaf7;stroke:var(--violet)}
.dg .nodet{font-weight:800;font-size:17px}
.ll{fill:none;stroke:var(--grey);stroke-width:2;stroke-dasharray:6 7}
.ring{fill:none;stroke:var(--violet);stroke-width:3;stroke-dasharray:10 8}
.tkc{fill:var(--orange);stroke:#fff;stroke-width:3}.dg .tkt{fill:#fff;font-weight:900;font-size:20px}
.tl,.mkl{stroke:var(--violet);stroke-width:4}.tlh{fill:var(--violet)}.mkc{fill:var(--orange)}.mkl{stroke:var(--orange);stroke-width:3}
.slotb{fill:#fff;stroke:var(--line);stroke-width:2;transition:fill .28s,stroke .28s}
.slot.on .slotb{fill:#fff1e8;stroke:var(--orange)}
.dg .slt{font-size:15px;font-weight:800}
.frb{stroke-width:2.5}.frb.o{fill:#fff1e8;stroke:var(--orange)}.frb.v{fill:#efeaf7;stroke:var(--violet)}.frb.pk{fill:#fde9ef;stroke:var(--pinkish)}.frb.g{fill:#eef5ea;stroke:var(--green)}
.dg .bits{font-family:var(--mono);font-size:18px;font-weight:700}.dg .bits.big{font-size:28px}.dg .ins{fill:var(--orange);font-weight:900}
.padb{fill:#fde9ef;stroke:var(--pinkish);stroke-width:2;stroke-dasharray:5 4}
.dg .fl{font-size:16px;font-weight:900;fill:var(--orange)}
.bx{fill:#fff;stroke:var(--ink);stroke-width:2;transition:fill .28s,stroke .28s}
.hot .bx,.bx.hot{fill:#fff1e8;stroke:var(--orange)}
g.hot .bx{fill:#fff1e8;stroke:var(--orange);stroke-width:3}
.dg .bxt{font-weight:800;font-size:19px}.dg .bxt.sm{font-size:16px}
.okb{fill:#eef5ea;stroke:var(--green);stroke-width:2.5}.nob{fill:#fde9ef;stroke:#d23c3c;stroke-width:2.5}
.wl{stroke:var(--violet);stroke-width:3;stroke-dasharray:4 8}.cl{stroke:var(--ink);stroke-width:3}.ol{stroke:var(--orange);stroke-width:4}
.phb{fill:#fff;stroke:var(--ink);stroke-width:3}
.apb{fill:#efeaf7;stroke:var(--violet);stroke-width:3}.apw{fill:none;stroke:var(--violet);stroke-width:3;stroke-linecap:round}.apd{fill:var(--violet)}
.swb{fill:#fff1e8;stroke:var(--orange);stroke-width:3}.swp{fill:var(--orange)}
.rtb{fill:#efeaf7;stroke:var(--violet);stroke-width:3}.rtt{fill:#fff;stroke:var(--violet);stroke-width:3}.rta{stroke:var(--violet);stroke-width:3}
.envb{fill:#fff;stroke:var(--orange);stroke-width:3}.envl{fill:none;stroke:var(--orange);stroke-width:2.5}
.fcell,.acell{fill:var(--ink)}.dg .fct{fill:#fff;font-size:13px;font-weight:800}
.fval,.aval{fill:#fff;stroke:var(--line);stroke-width:2;transition:fill .28s,stroke .28s}
.fval.on,.aval.on{fill:#fff1e8;stroke:var(--orange)}
.dg .fvt{font-family:var(--mono);font-weight:900;font-size:20px}
.dg .avt{font-size:13px;font-weight:800;font-family:var(--mono)}.dg .avr{font-size:12px;fill:var(--dim)}
.halob{fill:rgba(242,96,12,.1);stroke:var(--orange);stroke-width:3}
.dg .adr{font-family:var(--mono);font-size:13px;font-weight:700}.dg .adr.mac{fill:var(--violet)}
.howb{fill:var(--ink)}.dg .how{fill:#fff;font-size:17px;font-weight:700}
.zone{stroke-width:2;stroke-dasharray:8 6}.zone.o{fill:rgba(242,96,12,.06);stroke:var(--orange)}.zone.v{fill:rgba(111,82,168,.06);stroke:var(--violet)}
/* title & cats */
.tslide .sc{padding-left:clamp(16px,10vw,220px)}
.title{position:relative}
.kick{font-size:1rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--orange);margin-bottom:.5rem}
.title h1{font-size:clamp(2.6rem,7vw,6rem);line-height:.95;font-weight:900;text-transform:uppercase;margin-bottom:1.3rem}
.title h1 .o2{color:var(--orange)}
.lead{font-size:1.4rem;line-height:1.45;color:var(--dim);max-width:40ch;margin-bottom:2.2rem}
.authors{font-size:1.05rem;line-height:1.6}
.cat{display:block;height:auto}
.tcat{position:absolute;right:2%;bottom:-2rem;width:clamp(160px,24vw,420px)}
.scat{position:absolute;right:-.5rem;bottom:-1.5rem;width:clamp(120px,14vw,250px);z-index:0;pointer-events:none;border-radius:50%;background:radial-gradient(circle at 50% 56%,#ffe3cd 0%,#ffe3cd 52%,rgba(255,227,205,0) 72%);filter:drop-shadow(0 10px 22px rgba(20,16,12,.18))}
.bl,.p,.g2{position:relative;z-index:1}
.catbox{display:grid;place-items:center}.catbox .cat{width:min(22rem,70%)}
/* trainers */
.trn,.quiz{padding:1.4rem 1.5rem}
.tq{font-size:1.3rem;line-height:1.4;margin-bottom:1rem}
.trow{display:flex;flex-wrap:wrap;gap:.7rem;align-items:center}
.btn{font:inherit;font-size:.95rem;font-weight:700;padding:.55rem 1rem;border-radius:10px;border:2px solid var(--ink);background:#fff;color:var(--ink);cursor:pointer;transition:background .15s,color .15s}
.btn:hover{background:#fff1e8}.btn:active{background:#ffe0cc}
.btn.pri{background:var(--orange);border-color:var(--orange);color:#fff}.btn.pri:hover{background:var(--ink);border-color:var(--ink)}
.btn:disabled{opacity:.4;cursor:default}
.btn:focus-visible,.opt:focus-visible,#nav button:focus-visible,.ovi:focus-visible{outline:3px solid var(--violet);outline-offset:2px}
.tres{min-height:2.6rem;font-size:1.05rem;line-height:1.45;margin:.2rem 0 .8rem}
.tres.ok{color:#3f7a2b}.tres.no{color:#c0392b}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:.6rem}.opts.col{grid-template-columns:1fr}
.opt{font:inherit;text-align:left;font-size:1.02rem;padding:.7rem 1rem;border-radius:10px;border:2px solid var(--line);background:#fff;color:var(--ink);cursor:pointer}
.opt:hover{border-color:var(--orange)}
.opt.ok{border-color:var(--green);background:#eef5ea}.opt.no{border-color:#c0392b;background:#fde9ef}
.qtop{display:flex;justify-content:space-between;color:var(--dim);margin-bottom:.6rem}
.quizrow{align-items:center}
/* nav */
#nav{position:fixed;z-index:40;left:50%;bottom:12px;transform:translateX(-50%);display:flex;align-items:center;gap:.3rem;background:#fff;border:1.5px solid var(--line);border-radius:var(--r);padding:.35rem .5rem;font-size:14px}
#nav button{font:inherit;font-size:13px;font-weight:700;border:0;background:transparent;color:var(--ink);border-radius:10px;padding:.42rem .65rem;cursor:pointer;display:inline-flex;align-items:center;gap:.35rem}
#nav button:hover{background:#fff1e8}#nav button:disabled{opacity:.35}
#nav svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
.nsep{width:1px;height:22px;background:var(--line);margin:0 .2rem}
#ind{font-family:var(--mono);font-size:13px;padding:0 .4rem;white-space:nowrap}
#ov{position:fixed;inset:0;z-index:60;background:rgba(251,249,247,.97);overflow:auto;padding:clamp(16px,5vh,60px) clamp(16px,6vw,120px)}
#ov h2{margin-bottom:1.2rem;font-size:1.8rem}
.ovg{display:grid;grid-template-columns:repeat(auto-fill,minmax(14rem,1fr));gap:.6rem}
.ovi{font:inherit;text-align:left;display:flex;gap:.8rem;align-items:center;padding:.7rem .9rem;background:#fff;border:1.5px solid var(--line);border-radius:12px;cursor:pointer;color:var(--ink);font-size:.95rem}
.ovi:hover,.ovi.cur{border-color:var(--orange)}.ovi .mono{color:var(--orange);font-weight:800;width:2rem}
@media (min-width:768px){.g2{grid-template-columns:repeat(2,minmax(0,1fr))}.g3{grid-template-columns:repeat(3,minmax(0,1fr))}}
@media (min-width:768px) and (max-width:1279px){.g3{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (min-width:1280px){.two{grid-template-columns:minmax(0,.85fr) minmax(0,1.15fr)}}
@media (max-width:767px){html{font-size:15px}h2,.tight h2{font-size:min(1.8rem,30px)}.sc{padding-bottom:7rem}.opts{grid-template-columns:1fr}
  .dg{max-height:none}.tbl{min-width:36rem}.bl.big li{font-size:1.2rem}.scat,.tcat{display:none}#nav .lbl2{display:none}}
@media (prefers-reduced-motion:reduce){*,*::before,*::after{transition:none!important;animation:none!important}}
"""

DECO = ('<svg id="deco" viewBox="0 0 1600 900" preserveAspectRatio="none" aria-hidden="true">'
        '<path fill="#f2600c" d="M0 0H330C300 18 250 30 205 58C160 86 120 128 70 150C45 162 18 168 0 172Z"/>'
        '<path fill="#14161c" d="M0 0H140C118 20 92 36 70 62C52 84 30 96 0 104Z"/>'
        '<path fill="#f2600c" d="M1600 900H1250C1290 880 1350 866 1400 836C1450 806 1490 760 1545 736C1570 726 1588 722 1600 720Z"/>'
        '<path fill="#14161c" d="M1600 900H1450C1478 878 1506 858 1530 832C1552 808 1576 796 1600 790Z"/>'
        + "".join(f'<circle cx="{1440+i*22}" cy="{40+j*22}" r="4" fill="#f2600c" opacity=".5"/>' for i in range(5) for j in range(2))
        + "".join(f'<circle cx="{40+i*22}" cy="{830+j*22}" r="4" fill="#6f52a8" opacity=".5"/>' for i in range(3) for j in range(2))
        + '</svg>')

JS = r"""
(function(){
'use strict';
var $=function(s,r){return (r||document).querySelector(s)}, $$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var SCENES=__SCENES__;
var slides=$$('.slide'), N=slides.length, cur=0, step=0, timer=null;
var RM=window.matchMedia('(prefers-reduced-motion: reduce)');
slides.forEach(function(s){
  var els=$$('[data-s]',s), mx=0;
  els.forEach(function(e){ mx=Math.max(mx,+e.dataset.s||0); });
  var sc=$('[data-scene]',s);
  if(sc){ var sp=SCENES[sc.dataset.scene]; sc._sp=sp; sc._map={};
    Object.keys(sp.e).forEach(function(id){ var el=$('[data-id="'+id+'"]',sc); if(el){ el._b=el.getAttribute('class')||''; sc._map[id]=el; } });
    s._scene=sc; mx=Math.max(mx,sp.n); }
  s._els=els; s._max=mx;
});
function applyScene(sc,k,instant){
  var sp=sc._sp; k=Math.min(k,sp.n);
  Object.keys(sp.e).forEach(function(id){
    var el=sc._map[id], t=sp.e[id]; if(!el) return;
    if(t.p) el.style.transform='translate('+t.p[k][0]+'px,'+t.p[k][1]+'px)';
    if(t.o) el.style.opacity=t.o[k];
    if(t.c) el.setAttribute('class',(el._b+' '+t.c[k]).trim());
    if(t.t && el.textContent!==t.t[k]){ el.textContent=t.t[k]; if(!instant){ el.classList.remove('flash'); void el.getBoundingClientRect(); el.classList.add('flash'); } }
  });
}
function waitFor(sl,k){
  if(sl._scene && k<=sl._scene._sp.n) return sl._scene._sp.w[k]||1100;
  var w=0; sl._els.forEach(function(e){ if(+e.dataset.s===k) w=Math.max(w,+e.dataset.w||0); });
  return w||450;
}
function setStep(k,instant){
  var sl=slides[cur]; step=Math.max(0,Math.min(sl._max,k));
  if(instant) sl.classList.add('ni');
  sl._els.forEach(function(e){ e.classList.toggle('in',+e.dataset.s<=step); });
  if(sl._scene) applyScene(sl._scene,step,instant);
  if(instant){ void sl.offsetWidth; sl.classList.remove('ni'); }
}
function tick(){ var sl=slides[cur]; if(step>=sl._max){ timer=null; return; } setStep(step+1,false); timer=setTimeout(tick,waitFor(sl,step)); }
function play(){ clearTimeout(timer); timer=null; var sl=slides[cur]; if(RM.matches||!sl._max){ setStep(sl._max,true); return; } setStep(0,true); timer=setTimeout(tick,350); }
function go(i){
  i=Math.max(0,Math.min(N-1,i)); clearTimeout(timer); timer=null;
  slides.forEach(function(s){s.classList.remove('on')}); cur=i; slides[cur].classList.add('on');
  var sc=$('.sc',slides[cur]); if(sc) sc.scrollTop=0;
  play();
  try{ history.replaceState(null,'','#'+(cur+1)); }catch(e){}
  $('#ind').textContent=(cur+1)+' / '+N; $('#prog i').style.width=((cur+1)/N*100)+'%';
  $('#b-play').disabled=!slides[cur]._max; $('#b-prev').disabled=cur===0; $('#b-next').disabled=cur===N-1;
}
function next(){ if(cur<N-1) go(cur+1); }
function prev(){ if(cur>0) go(cur-1); }
$('#b-prev').onclick=prev; $('#b-next').onclick=next; $('#b-play').onclick=play;
var ov=$('#ov'), ovg=$('.ovg',ov);
slides.forEach(function(s,k){ var b=document.createElement('button'); b.className='ovi'; b.type='button';
  b.innerHTML='<span class="mono">'+(k+1)+'</span><span></span>'; b.lastChild.textContent=s.dataset.label;
  b.onclick=function(){ ov.hidden=true; go(k); }; ovg.appendChild(b); });
function openOv(){ ov.hidden=false; $$('.ovi',ov).forEach(function(b,k){b.classList.toggle('cur',k===cur)}); var c=$('.ovi.cur',ov); if(c)c.focus(); }
$('#b-ov').onclick=openOv;
var dbuf='', dtm=null;
document.addEventListener('keydown',function(e){
  var t=e.target, tag=t.tagName;
  if(e.ctrlKey||e.metaKey||e.altKey) return;
  if(tag==='INPUT'){ if(e.key==='Escape') t.blur(); return; }
  if(e.key==='Escape'){ e.preventDefault(); ov.hidden?openOv():(ov.hidden=true); return; }
  if(!ov.hidden) return;
  switch(e.key){
    case 'ArrowRight': case 'ArrowDown': case 'PageDown': e.preventDefault(); next(); return;
    case 'ArrowLeft': case 'ArrowUp': case 'PageUp': e.preventDefault(); prev(); return;
    case ' ': if(tag==='BUTTON') return; e.preventDefault(); next(); return;
    case 'Home': e.preventDefault(); go(0); return;
    case 'End': e.preventDefault(); go(N-1); return;
  }
  var k=e.key.toLowerCase();
  if(k==='r'||k==='к'){ play(); return; }
  if(/^[0-9]$/.test(e.key)){ dbuf+=e.key; clearTimeout(dtm); dtm=setTimeout(function(){ var n=parseInt(dbuf,10); dbuf=''; if(n>=1&&n<=N) go(n-1); },550); }
});
var lastWheel=0;
window.addEventListener('wheel',function(e){
  if(!ov.hidden) return; var sc=$('.sc',slides[cur]); if(!sc) return; var dy=e.deltaY; if(Math.abs(dy)<4) return;
  if(dy>0 && sc.scrollTop+sc.clientHeight<sc.scrollHeight-2) return; if(dy<0 && sc.scrollTop>0) return;
  var now=Date.now(); if(now-lastWheel<420) return; lastWheel=now; dy>0?next():prev();
},{passive:true});
var tx=0,ty=0,tt=0;
window.addEventListener('touchstart',function(e){ var p=e.changedTouches[0]; tx=p.clientX; ty=p.clientY; tt=Date.now(); },{passive:true});
window.addEventListener('touchend',function(e){ var p=e.changedTouches[0], dx=p.clientX-tx, dy=p.clientY-ty;
  if(Date.now()-tt>700||Math.abs(dx)<60||Math.abs(dx)<Math.abs(dy)*1.4) return; if(e.target.closest&&e.target.closest('.tw')) return; dx<0?next():prev(); },{passive:true});

function rnd(n){ return Math.floor(Math.random()*n); }
function shuffle(a){ a=a.slice(); for(var i=a.length-1;i>0;i--){ var j=rnd(i+1), t=a[i]; a[i]=a[j]; a[j]=t; } return a; }
function choice(pre,gen,keep){
  var tot=0, ok=0;
  function nx(){ var q=gen(), o=$('#'+pre+'-o'), done=false; $('#'+pre+'-q').innerHTML=q.q; o.innerHTML=''; var r=$('#'+pre+'-r'); r.textContent=''; r.className='tres';
    (keep?q.o:shuffle(q.o)).forEach(function(t){ var b=document.createElement('button'); b.type='button'; b.className='opt'; b.textContent=t;
      b.onclick=function(){ if(done) return; done=true; var good=t===q.o[q.a||0];
        $$('.opt',o).forEach(function(x){ if(x.textContent===q.o[q.a||0]) x.classList.add('ok'); }); if(!good) b.classList.add('no');
        tot++; if(good) ok++; r.textContent=(good?'Верно. ':'Неверно. ')+q.e; r.className='tres '+(good?'ok':'no');
        var sc=$('#'+pre+'-sc'); if(sc) sc.textContent=ok+' / '+tot; };
      o.appendChild(b); }); }
  $('#'+pre+'-nx').onclick=nx; nx();
}
var ST=[['Используется в проводных сетях',0],['Используется в беспроводных сетях',1],['Начинает работать после коллизии',0],['Работает до коллизии',1],
  ['Сокращает время восстановления работоспособности сети',0],['Снижает вероятность коллизии',1],['Возобновляет передачу после устранения коллизии',0],
  ['Запрашивает разрешение на отправку',1],['Станция отправляет сигнал затора (jam signal), прежде чем передавать',1],['Похож на пожарную бригаду, которая тушит пожар',0],
  ['Похож на систему пожарной безопасности, предотвращающую пожар',1],['После коллизии ждёт случайный промежуток времени и повторяет попытку',0]];
choice('t1',function(){ var s=ST[rnd(ST.length)]; return {q:'«'+s[0]+'». О каком протоколе речь?', o:['CSMA/CD','CSMA/CA'], a:s[1],
  e:(s[1]?'CSMA/CA':'CSMA/CD')+(s[1]?' – предотвращение коллизий в беспроводных сетях.':' – обнаружение коллизий в сетях Ethernet.')}; },true);
var WF=[['смартфон отправляет кадр во внешнюю сеть через AP (To DS = 1, From DS = 0)',['MAC AP (Receiver)','MAC смартфона (Source / Transmitter)','MAC R1 (Destination)']],
  ['маршрутизатор R1 отправляет кадр смартфону через AP (To DS = 0, From DS = 1)',['MAC смартфона (Destination / Receiver)','MAC AP (Transmitter)','MAC R1 (Source)']],
  ['сервер отправляет кадр PC1 через AP1 и AP2 в режиме моста (To DS = 1, From DS = 1)',['MAC AP2 (Receiver)','MAC AP1 (Transmitter)','MAC PC1 (Destination)','MAC Server (Source)']]];
choice('t2',function(){ var w=WF[rnd(WF.length)], i=rnd(w[1].length); var all=[].concat(WF[0][1],WF[1][1],WF[2][1]);
  var others=shuffle(all.filter(function(x){return w[1].indexOf(x)<0||x!==w[1][i]})).filter(function(x){return x!==w[1][i]}).slice(0,3);
  return {q:'Ситуация: '+w[0]+'. Что записано в поле <b>MAC-адрес '+(i+1)+'</b>?', o:[w[1][i]].concat(others), a:0,
    e:'Порядок адресов: '+w[1].map(function(x,k){return (k+1)+') '+x}).join('; ')+'.'}; });
var FS=[['Преамбула Ethernet II','8 байт'],['MAC-адрес назначения Ethernet','6 байт'],['EtherType','2 байта'],['FCS Ethernet','4 байта'],['SFD 802.3','1 байт'],
  ['Тег 802.1Q','4 байта'],['Межпакетный интервал IPG','12 байт'],['Поле «Адрес» PPP','1 байт'],['Поле «Протокол» PPP','2 байта'],['MAC-адрес в кадре 802.11','6 байт'],
  ['QoS Control 802.11','2 байта'],['HT Control 802.11','4 байта']];
choice('t3',function(){ var f=FS[rnd(FS.length)]; var vals=['1 байт','2 байта','4 байта','6 байт','8 байт','12 байт'];
  return {q:'Какой размер поля <b>'+f[0]+'</b>?', o:[f[1]].concat(shuffle(vals.filter(function(v){return v!==f[1]})).slice(0,3)), a:0, e:f[0]+' – '+f[1]+'.'}; });
(function(){
  var Q=__QUIZ__, i=0, got=Q.map(function(){return -1});
  function sc(){ return got.filter(function(g,k){return g===Q[k].a}).length; }
  function render(){ var q=Q[i]; $('#qz-n').textContent=(i+1)+' / '+Q.length; $('#qz-q').textContent=q.q;
    var o=$('#qz-o'); o.innerHTML=''; var e=$('#qz-e'); e.textContent=''; e.className='tres';
    q.o.forEach(function(t,k){ var b=document.createElement('button'); b.type='button'; b.className='opt'; b.textContent=t; b.onclick=function(){ if(got[i]<0) got[i]=k; show(); }; o.appendChild(b); });
    if(got[i]>=0) show(); $('#qz-sc').textContent='верно: '+sc(); $('#qz-pv').disabled=i===0; $('#qz-nx').textContent=i===Q.length-1?'Начать заново':'Следующий вопрос'; }
  function show(){ var q=Q[i], bs=$$('.opt',$('#qz-o')); bs[q.a].classList.add('ok'); if(got[i]!==q.a) bs[got[i]].classList.add('no');
    var e=$('#qz-e'); e.textContent=(got[i]===q.a?'Верно. ':'Неверно. ')+q.e; e.className='tres '+(got[i]===q.a?'ok':'no'); $('#qz-sc').textContent='верно: '+sc(); }
  $('#qz-nx').onclick=function(){ if(i===Q.length-1){ got=Q.map(function(){return -1}); i=0; } else i++; render(); };
  $('#qz-pv').onclick=function(){ if(i>0){ i--; render(); } };
  render();
})();
var h=parseInt((location.hash||'').slice(1),10);
go(h>=1&&h<=N?h-1:0);
})();
"""

ICON_L = '<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>'
ICON_R = '<svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg>'

def render():
    out = ['<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           '<title>Глава 10. Канальный уровень</title><style>' + CSS + '</style></head><body>' + DECO + '<div id="prog"><i></i></div><main>']
    for label, t1, t2, body, cls in S:
        head = "" if not t1 else f'<header class="sh"><h2>{t1}<span class="o2">{t2}</span></h2></header>'
        out.append(f'<section class="slide {cls}" data-label="{label}"><div class="sc"><div class="wrap">{head}{body}</div></div></section>')
    out.append('</main><nav id="nav" aria-label="Навигация">'
               f'<button id="b-prev" type="button" aria-label="Предыдущий слайд">{ICON_L}</button><span id="ind"></span>'
               f'<button id="b-next" type="button" aria-label="Следующий слайд">{ICON_R}</button><span class="nsep"></span>'
               '<button id="b-play" type="button" title="Клавиша R"><svg viewBox="0 0 24 24"><path d="M4 12a8 8 0 1 0 2.5-5.8M4 4v5h5"/></svg><span class="lbl2">Повторить анимацию</span></button>'
               '<button id="b-ov" type="button" title="Esc"><svg viewBox="0 0 24 24"><path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z"/></svg><span class="lbl2">Меню</span></button></nav>'
               '<div id="ov" hidden><h2>Содержание</h2><div class="ovg"></div></div>')
    js = JS.replace("__SCENES__", json.dumps(SCENES, ensure_ascii=False, separators=(",", ":"))).replace("__QUIZ__", json.dumps(QUIZ, ensure_ascii=False))
    out.append('<script>' + js + '</script></body></html>')
    OUT.write_text("".join(out), encoding="utf-8")
    print(len(S), "slides", OUT.stat().st_size, "bytes")

render()
