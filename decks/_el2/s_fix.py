# -*- coding: utf-8 -*-
"""Слайды «как на фото»: вёрстка по координатам оригинала pptx (_el2ref/sNN.jpg).

Модуль грузится последним и перекрывает одноимённые ref из других файлов.
Координаты во всех вызовах — пиксели картинки-оригинала; Ref пересчитывает их в холст 1920x1080.
Иконки, фото устройств и иллюстрации вырезаются из оригинала (при первой сборке) в _el2assets.
"""
import sys, pathlib
import numpy as np
from PIL import Image

HERE = pathlib.Path(__file__).parent
sys.path.insert(0, str(HERE.parent))

SLIDES = []
REFDIR = HERE.parent / "_el2ref"
ASSETS = HERE.parent / "_el2assets"

NAVY = "#1f2d78"
BLUE = "#2f50d0"
INK = "#2a3150"
DIM = "#5f6b9a"
TITLE_GRAD = "linear-gradient(180deg,#26348c 0%,#2b3f9e 55%,#3f5cc8 100%)"


def _crop(n, box, name, white):
    out = ASSETS / name
    if out.exists():
        return
    im = Image.open(REFDIR / f"s{n:02d}.jpg").convert("RGB").crop(box)
    if white:
        # фон = медиана по рамке вырезки; прозрачность по удалённости цвета от фона + мягкие края
        a = np.asarray(im).astype(np.float32)
        border = np.concatenate([a[0], a[-1], a[:, 0], a[:, -1]])
        bg = np.median(border, axis=0)
        dist = np.sqrt(((a - bg) ** 2).sum(axis=2))
        alpha = np.clip((dist - 10) / 28, 0, 1)
        h, w = alpha.shape
        e = max(4, int(min(h, w) * 0.06))
        ry = np.clip(np.minimum(np.arange(h), np.arange(h)[::-1]) / e, 0, 1)
        rx = np.clip(np.minimum(np.arange(w), np.arange(w)[::-1]) / e, 0, 1)
        alpha *= np.outer(ry, rx)
        rgba = np.dstack([a, alpha * 255]).astype(np.uint8)
        Image.fromarray(rgba, "RGBA").save(out, optimize=True)
    else:
        im.save(out, quality=90)


class Ref:
    """Пересчёт координат оригинала в холст 1920x1080."""

    def __init__(self, n, pref):
        self.n, self.pref = n, pref
        self.W, self.H = Image.open(REFDIR / f"s{n:02d}.jpg").size
        self.sx, self.sy = 1920 / self.W, 1080 / self.H
        self.k = min(self.sx, self.sy)

    def X(self, x):
        return round(x * self.sx)

    def Y(self, y):
        return round(y * self.sy)

    def F(self, f):
        return round(f * self.k, 1)

    @staticmethod
    def _s(s, dl=None):
        r = f' data-s="{s}"' if s else ""
        return r

    def img(self, x0, y0, x1, y1, name, white=False, s=None, fade=False, extra="", dl=0):
        """Вырезка из оригинала; пропорции сохраняются, картинка по центру своей области."""
        name = f"{self.pref}fx_{name}" + ("" if "." in name else ".png" if white else ".jpg")
        _crop(self.n, (x0, y0, x1, y1), name, white)
        w = (x1 - x0) * self.k
        cx = (x0 + x1) / 2 * self.sx
        top = y0 * self.sy + ((y1 - y0) * self.sy - (y1 - y0) * self.k) / 2
        st = f"left:{cx - w / 2:.0f}px;top:{top:.0f}px;width:{w:.0f}px;"
        if fade:
            st += ("-webkit-mask-image:radial-gradient(ellipse 72% 72% at 50% 50%,#000 62%,transparent 100%);"
                   "mask-image:radial-gradient(ellipse 72% 72% at 50% 50%,#000 62%,transparent 100%);")
        if dl:
            st += f"--dl:{dl}ms;"
        return f'<img class="ab" src="assets/{name}"{self._s(s)} style="{st}{extra}">'

    def txt(self, x, y, w, html, fs, col=INK, wt=400, s=None, extra="", lh=1.3, dl=0):
        st = (f"left:{self.X(x)}px;top:{self.Y(y)}px;width:{self.X(w)}px;font-size:{self.F(fs)}px;"
              f"color:{col};font-weight:{wt};line-height:{lh};font-family:var(--f);")
        if dl:
            st += f"--dl:{dl}ms;"
        return f'<div class="ab"{self._s(s)} style="{st}{extra}">{html}</div>'

    def head(self, x, y, w, html, fs, col=NAVY, s=None, extra="", lh=1.12):
        return self.txt(x, y, w, html, fs, col, 800, s, "letter-spacing:.2px;" + extra, lh)

    def title(self, x, y, w, html, fs, extra="", lh=1.0):
        return (f'<div class="ab" style="left:{self.X(x)}px;top:{self.Y(y)}px;width:{self.X(w)}px;'
                f'font-family:var(--f);font-weight:800;font-size:{self.F(fs)}px;line-height:{lh};'
                f'letter-spacing:-.5px;background:{TITLE_GRAD};-webkit-background-clip:text;'
                f'background-clip:text;color:transparent;{extra}">{html}</div>')

    def box(self, x0, y0, x1, y1, s=None, r=22, extra="", dl=0):
        st = (f"left:{self.X(x0)}px;top:{self.Y(y0)}px;width:{self.X(x1) - self.X(x0)}px;"
              f"height:{self.Y(y1) - self.Y(y0)}px;border-radius:{r}px;"
              "background:linear-gradient(158deg,rgba(255,255,255,.86),rgba(240,244,255,.66));"
              "border:1.5px solid rgba(160,178,230,.55);"
              "box-shadow:0 10px 30px rgba(70,90,170,.12),inset 0 1px 0 #fff;")
        if dl:
            st += f"--dl:{dl}ms;"
        return f'<div class="ab"{self._s(s)} style="{st}{extra}"></div>'

    def badge(self, x0, y0, x1, y1, num, s=None, fs=None, extra=""):
        """Синий скруглённый квадрат с номером (как в оригинале)."""
        h = self.Y(y1) - self.Y(y0)
        fs = fs or h * 0.62
        return (f'<div class="ab"{self._s(s)} style="left:{self.X(x0)}px;top:{self.Y(y0)}px;'
                f'width:{self.X(x1) - self.X(x0)}px;height:{h}px;border-radius:{h * 0.26:.0f}px;'
                f'background:linear-gradient(160deg,#5b7cf0,#2c47c4);color:#fff;font-family:var(--f);'
                f'font-weight:800;font-size:{fs:.0f}px;display:flex;align-items:center;justify-content:center;'
                f'box-shadow:0 6px 16px rgba(40,70,190,.35);{extra}">{num}</div>')

    def wire(self, pts, s=None, col="#2f5fe0", w=3, dots=True):
        """Линия-выноска по точкам оригинала, с кружками на концах."""
        P = [(x * self.sx, y * self.sy) for x, y in pts]
        d = "M" + " L".join(f"{x:.0f} {y:.0f}" for x, y in P)
        dd = "".join(f'<circle class="hd" cx="{x:.0f}" cy="{y:.0f}" r="6" fill="{col}"/>'
                     for x, y in (P[0], P[-1])) if dots else ""
        g = f' data-s="{s}"' if s else ""
        return (f'<g{g}><path class="dr" pathLength="1" d="{d}" stroke="{col}" stroke-width="{w}" '
                f'fill="none" stroke-linejoin="round"/>{dd}</g>')

    def dev(self, name, x0, y0, x1, y1, s=None, extra="", shadow=True):
        """Официальное фото Eltex (_el2assets/dev) вписано в область оригинала; возвращает (html, (l, t, w, h))."""
        w0, h0 = Image.open(ASSETS / "dev" / name).size
        bw, bh = (x1 - x0) * self.sx, (y1 - y0) * self.sy
        k = min(bw / w0, bh / h0)
        w, h = w0 * k, h0 * k
        l, t = x0 * self.sx + (bw - w) / 2, y0 * self.sy + (bh - h) / 2
        sh = "filter:drop-shadow(0 18px 26px rgba(40,60,140,.22));" if shadow else ""
        html = (f'<img class="ab" src="assets/dev/{name}"{self._s(s)} style="left:{l:.0f}px;top:{t:.0f}px;'
                f'width:{w:.0f}px;{sh}{extra}">')
        return html, (l, t, w, h)

    def flow(self, x, y, w, rows, s=None, fs=14, gap=10, icw=44, lh=1.17, dl=90):
        """Колонка пунктов «иконка + текст» потоком: rows = [(src, text)]."""
        out = [f'<div class="ab" style="left:{self.X(x)}px;top:{self.Y(y)}px;width:{self.X(w)}px">']
        for j, (src, t) in enumerate(rows):
            out.append(f'<div{self._s(s)} style="display:flex;gap:16px;align-items:flex-start;'
                       f'margin-top:{gap if j else 0}px;--dl:{j * dl}ms">'
                       f'<img src="{src}" style="width:{icw}px;flex:none;margin-top:-2px">'
                       f'<div style="font-size:{self.F(fs)}px;line-height:{lh};color:{INK}">{t}</div></div>')
        return "".join(out) + '</div>'

    def src(self, x0, y0, x1, y1, name, white=True):
        name = f"{self.pref}fx_{name}" + ("" if "." in name else ".png" if white else ".jpg")
        _crop(self.n, (x0, y0, x1, y1), name, white)
        return f"assets/{name}"

    @staticmethod
    def layer(*parts):
        return ('<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" '
                'viewBox="0 0 1920 1080">' + "".join(parts) + '</svg>')


def ul(items, gap=2):
    return ('<ul style="margin:0;padding-left:1.1em">'
            + "".join(f'<li style="margin-top:{gap}px;padding-left:2px">{t}</li>' for t in items)
            + '</ul>')



def kick(r, x, y, w, text, fs, col=DIM, sp=8, s=None):
    return r.txt(x, y, w, text, fs, col, 500, s, f"letter-spacing:{r.F(sp)}px;text-transform:uppercase")


# ======================================================= сетевые устройства (p066 = pptx 3)
def devices():
    r = Ref(3, "p066")
    o = [r.title(38, 62, 900, "СЕТЕВЫЕ&nbsp; УСТРОЙСТВА", 72),
         kick(r, 42, 136, 700, "Основа современных сетей", 20, "#6874a8", 9)]

    def para(x, y, w, txt, s):
        return (f'<div class="ab" data-s="{s}" style="left:{r.X(x)}px;top:{r.Y(y)}px;width:{r.X(w)}px;'
                f'border-left:2px solid #8fa2dc;padding-left:{r.X(18)}px;font-size:{r.F(16)}px;'
                f'line-height:1.2;color:{INK}">{txt}</div>')

    cards = [
        (14, 505, "01", "ROUTER", "МАРШРУТИЗАТОР", "R O U T E R", "Сетевой уровень<br>(3 уровень OSI)", "lay3",
         (30, 322, 492, 485), "router",
         "Это сетевое устройство, соединяющие сети и предназначенное для пересылки пакетов из одной сети в другую.",
         (47, 505, 400), (55, 592, 470, 715)),
        (513, 1022, "02", "SWITCH", "КОММУТАТОР", "S W I T C H", "Канальный уровень<br>(2 уровень OSI)", "lay2",
         (518, 340, 1012, 462), "switch",
         "Это сетевое устройство, предназначенное для пересылки кадров в пределах одной сети. "
         "Коммутаторы локальных сетей работают на канальном уровне (2 уровень модели OSI).",
         (545, 500, 420), (552, 598, 990, 732)),
        (1030, 1522, "03", "WIRELESS ACCESS POINT", "БЕСПРОВОДНАЯ<br>ТОЧКА ДОСТУПА", "WIRELESS ACCESS POINT",
         "Канальный уровень<br>(2 уровень OSI)", "lay2b", (1130, 336, 1400, 492), "ap",
         "Это сетевое устройство, которое представляет из себя базовую станцию для создания беспроводной "
         "локальной сети, работающей поверх проводной сети или параллельно с ней. Точка доступа работает "
         "на канальном уровне (2 уровень модели OSI).",
         (1060, 494, 450), (1075, 615, 1482, 712)),
    ]
    for i, (x0, x1, n, en, ttl, ens, osi, lay, dbox, dname, text, pbox, ill) in enumerate(cards):
        s = i + 1
        o.append(r.box(x0, 188, x1, 742, s, 18))
        o.append(f'<div class="ab" data-s="{s}" style="left:{r.X(x0 + 10)}px;top:{r.Y(203)}px;width:{r.X(88)}px;'
                 f'height:{r.Y(36)}px;background:linear-gradient(90deg,#26348c,#3550c0);'
                 f'clip-path:polygon(0 0,100% 0,82% 100%,0 100%);color:#fff;font-weight:800;'
                 f'font-size:{r.F(24)}px;padding-left:{r.X(16)}px;line-height:{r.Y(36)}px">{n}</div>')
        o.append(kick(r, x0 + 126, 210, 360, en, 10.5, "#7c88b8", 2.5, s))
        o.append(r.head(x0 + 28, 254, 300, ttl, 24, NAVY, s))
        o.append(kick(r, x0 + 28, 290 if i < 2 else 314, 330, ens, 14, "#8590bf", 7 if i < 2 else 3.5, s))
        lx = x0 + (290 if i == 0 else 298 if i == 1 else 284)
        o.append(r.img(lx, 245, lx + 46, 304, lay, True, s))
        o.append(r.txt(lx + 50, 256, 160, osi, 13.5, INK, 400, s, "white-space:nowrap"))
        o.append(r.dev({"router": "esr-30.webp", "switch": "mes1428.webp", "ap": "wep-3ax.webp"}[dname], *dbox, s)[0])
        o.append(para(*pbox, text, s))
        o.append(r.img(*ill, f"ill{i + 1}", True, s))

    o.append(r.box(14, 760, 1522, 1010, 4, 18))
    o.append(r.head(62, 788, 300, "НАСТРОЙКА<br>И ДОСТУП", 36, NAVY, 4, lh=1.15))
    o.append(kick(r, 62, 882, 280, "Больше, чем просто подключить", 12.5, "#8f99c4", 5, 4))
    o.append(f'<div class="ab" data-s="4" style="left:{r.X(340)}px;top:{r.Y(788)}px;width:2px;'
             f'height:{r.Y(88)}px;background:#9aaad8"></div>')
    o.append(r.txt(372, 788, 740, "Чтобы компьютерная сеть функционировала, мало собрать и подключить сетевые "
                   "устройства через кабели и подключить к интернет-провайдеру, необходимо на каждом сетевом "
                   "устройстве выполнить определённую настройку. Чтобы выполнить настройку необходимых "
                   "параметров, нужно получить доступ к сетевому устройству.", 15.5, INK, 400, 4))
    for k, (x, lbl) in enumerate([(360, "НАСТРОЙКА<br>ПАРАМЕТРОВ"),
                                  (636, 'ДОСТУП К УСТРОЙСТВУ<br><span style="color:#7380b0;font-size:.85em">'
                                        '(например, через Web-интерфейс, CLI, SSH)</span>'),
                                  (990, "СТАБИЛЬНАЯ<br>И БЕЗОПАСНАЯ<br>РАБОТА СЕТИ")]):
        o.append(r.img(x, 888, x + 70, 958, f"ic{k + 1}", True, 5, dl=k * 120))
        o.append(r.txt(x + 86, 895 if k else 898, 290 if k == 1 else 240, lbl, 14, NAVY, 600, 5, dl=k * 120))
    for x in (600, 962):
        o.append(f'<div class="ab" data-s="5" style="left:{r.X(x)}px;top:{r.Y(898)}px;width:2px;'
                 f'height:{r.Y(50)}px;background:#c3cdea"></div>')
    return "".join(o)


SLIDES.append(("p066", "Сетевые устройства", devices()))


def callout(r, x0, y0, x1, y1, html, fs, s=None):
    """Синяя плашка-выноска поверх фото (перекрывает надпись оригинала)."""
    return (f'<div class="ab"{r._s(s)} style="left:{r.X(x0)}px;top:{r.Y(y0)}px;width:{r.X(x1) - r.X(x0)}px;'
            f'height:{r.Y(y1) - r.Y(y0)}px;border-radius:6px;background:linear-gradient(180deg,#6c88e4,#4d69cf);'
            f'border:1.5px solid #c8d4ff;color:#fff;font-weight:600;font-size:{r.F(fs)}px;line-height:1.2;'
            f'display:flex;align-items:center;justify-content:center;text-align:center;'
            f'box-shadow:0 6px 16px rgba(40,70,190,.3)">{html}</div>')


def numbox(r, x0, y0, x1, y1, n, fs, s=None):
    """Крупная цифра 01/02 в светлом квадрате."""
    return (f'<div class="ab"{r._s(s)} style="left:{r.X(x0)}px;top:{r.Y(y0)}px;width:{r.X(x1) - r.X(x0)}px;'
            f'height:{r.Y(y1) - r.Y(y0)}px;border-radius:12px;background:linear-gradient(160deg,#eef2ff,#dfe6fb);'
            f'box-shadow:inset 0 1px 0 #fff,0 4px 12px rgba(70,90,170,.15);color:#2c3f9a;font-weight:800;'
            f'font-size:{r.F(fs)}px;display:flex;align-items:center;justify-content:center">{n}</div>')


# ======================================================= доступ к устройству (p056 = pptx 5)
def access():
    r = Ref(5, "p056")
    dev = (438, 52, 1250, 398)

    def co(x0, y0, x1, y1, html, st):
        (a0, b0), (a1, b1) = (x0 * r.sx, y0 * r.sy), (x1 * r.sx, y1 * r.sy)
        return (f'<div class="ab" data-s="{st}" style="left:{a0:.0f}px;top:{b0:.0f}px;width:{a1 - a0:.0f}px;'
                f'height:{b1 - b0:.0f}px;border-radius:6px;background:linear-gradient(180deg,#6c88e4,#4d69cf);'
                f'border:1.5px solid #c8d4ff;color:#fff;font-weight:600;font-size:21px;line-height:1.15;'
                f'display:flex;align-items:center;justify-content:center;text-align:center;'
                f'box-shadow:0 6px 16px rgba(40,70,190,.3)">{html}</div>')

    o = [f'<div class="ab" style="left:{r.X(37)}px;top:{r.Y(58)}px;width:2px;height:{r.Y(160)}px;'
         f'background:linear-gradient(#7d93e0,transparent)"></div>',
         r.title(64, 50, 420, "ДОСТУП К<br>СЕТЕВОМУ<br>УСТРОЙСТВУ", 48, lh=1.08),
         r.txt(64, 222, 380, "Для доступа к сетевому устройству есть несколько способов подключения: "
               "по консольному порту с помощью консольного кабеля и через протоколы удалённого доступа "
               "Telnet или SSH.", 15, INK, 400, None, lh=1.25),
         ]
    dh, (dl_, dt, dw, dhh) = r.dev("esr-30.webp", 560, -150, 1240, 372)
    o.append(dh)
    o.append(r.box(1290, 52, 1515, 300, 1, 16))
    for k, t in enumerate(["НАСТРОЙКА", "УПРАВЛЕНИЕ", "МОНИТОРИНГ", "ОБСЛУЖИВАНИЕ"]):
        y = 72 + k * 61
        o.append(r.img(1308, y, 1360, y + 50, f"r{k + 1}", True, 1, dl=k * 90, extra="margin-top:-8px"))
        o.append(r.txt(1372, y + 12, 140, t, 13.5, "#5466a8", 500, 1, dl=k * 90))
    o.append(co(985, 62, 1230, 118, "Порты для подключения<br>(Telnet / SSH)", 2))
    o.append(co(590, 62, 800, 118, "Консольный порт<br>(Console)", 2))
    px, py = dl_ + 0.694 * dw, dt + 0.95 * dhh
    cx_, cy_ = dl_ + 0.383 * dw, dt + 0.92 * dhh
    o.append(Ref.layer(
        f'<g data-s="2"><path class="dr" pathLength="1" d="M{1107 * r.sx:.0f} {118 * r.sy:.0f} L{px:.0f} {py:.0f}" '
        f'stroke="#3f62d8" stroke-width="3" fill="none"/><circle class="hd" cx="{px:.0f}" cy="{py:.0f}" r="7" fill="#3f62d8"/>'
        f'<path class="dr" pathLength="1" d="M{695 * r.sx:.0f} {118 * r.sy:.0f} L{cx_:.0f} {cy_:.0f}" '
        f'stroke="#3f62d8" stroke-width="3" fill="none"/><circle class="hd" cx="{cx_:.0f}" cy="{cy_:.0f}" r="7" fill="#3f62d8"/></g>'))

    TOP, BOT = 372, 1022
    # 01
    o.append(r.box(18, TOP, 468, BOT, 3, 18))
    o.append(numbox(r, 36, TOP + 12, 116, TOP + 66, "01", 40, 3))
    o.append(r.head(128, TOP + 14, 230, "КОНСОЛЬНОЕ<br>ПОДКЛЮЧЕНИЕ", 23, NAVY, 3))
    o.append(r.txt(318, TOP + 20, 150, "Консольный порт<br>(Console)", 14, BLUE, 400, 3))
    o.append(r.img(45, 490, 500, 626, "cable", True, 3, extra=f"top:{r.Y(TOP + 76)}px;width:460px;left:50px"))
    ic = [(44, 646), (44, 707), (44, 788), (44, 872)]
    texts1 = [
        "Консольный порт (Console) — это интерфейс управления устройством, использует внеполосный доступ подключения.",
        "Внеполосный доступ (out-of-band) — доступ к устройству через специальный выделенный канал, "
        "предназначенный только для администрирования и технического обслуживания устройства.",
        "Позволяет выполнить первоначальное конфигурирование или может быть единственным способом доступа, "
        "если доступ по протоколам удалённого подключения невозможен или запрещен.",
        "Консольное подключение не зависит от наличия каких-либо настроек на сетевом устройстве."]
    o.append(r.flow(30, 580, 430, [(r.src(x, y, x + 46, y + 44, f"a{j + 1}"), t)
                                   for j, ((x, y), t) in enumerate(zip(ic, texts1))], 3, 13, 14))

    for c, (x0, x1, n, name, sub, ill, ys, texts, tag) in enumerate([
        (478, 994, "02", "TELNET", "Удалённый незащищённый<br>доступ", (552, 478, 990, 608), [624, 686, 736, 798, 846], [
            "Telnet — это протокол для установления удалённого незащищённого подключения к интерфейсу командной строки (CLI).",
            "Подключение по Telnet считается внутриполосным доступом (in-band — через общий канал).",
            "Требует наличия минимум одного настроенного IP-адреса и включения возможности использования "
            "протокола Telnet на сетевом устройстве (ip telnet server).",
            "Если необходимо использовать нестандартный номер порта, то используется команда ip telnet port.",
            "В случае маршрутизатора дополнительно необходима настройка правил разрешения межсетевого экрана "
            "для Telnet и настройка взаимодействия между зонами безопасности либо отключение межсетевого экрана "
            "на интерфейсе."], "b"),
        (1004, 1522, "03", "SSH", "Удалённый защищённый<br>доступ", (1045, 478, 1492, 608), [626, 688, 768, 830, 876], [
            "SSH (Secure Shell) — это протокол для установления удалённого защищённого внутриполосного "
            "подключения к интерфейсу CLI сетевого устройства.",
            "Защищённое подключение возможно благодаря использованию аутентификации на основе пароля "
            "и шифрования данных пользователя, но это несёт дополнительную нагрузку на сетевое устройство и канал.",
            "Требует наличия минимум одного настроенного IP-адреса и включения возможности использования "
            "протокола SSH на сетевом устройстве (ip ssh server).",
            "Если необходимо использовать нестандартный номер порта, то используется команда ip ssh port.",
            "В случае маршрутизатора дополнительно необходима настройка правил разрешения межсетевого экрана "
            "для SSH и настройка взаимодействия между зонами безопасности либо отключение межсетевого экрана "
            "на интерфейсе."], "c")]):
        st = 4 + c
        o.append(r.box(x0, TOP, x1, BOT, st, 18))
        o.append(numbox(r, x0 + 16, TOP + 12, x0 + 96, TOP + 66, n, 40, st))
        o.append(r.head(x0 + 114, TOP + 22, 140, name, 30, "#22284a", st))
        o.append(r.txt(x0 + 250, TOP + 18, 240, sub, 14, DIM, 400, st))
        ix0, iy0, ix1, iy1 = ill
        o.append(r.img(*ill, f"ill{c + 1}", True, st,
                       extra=f"top:{r.Y(TOP + 72)}px;width:{(ix1 - ix0) * r.k * 0.74:.0f}px;"
                             f"left:{r.X(x0) + 40}px"))
        rows = [(r.src(x0 + 22, y, x0 + 68, y + 44, f"{tag}{j + 1}"), t) for j, (y, t) in enumerate(zip(ys, texts))]
        o.append(r.flow(x0 + 12, 540, x1 - x0 - 20, rows, st, 13, 4, lh=1.13))
    return "".join(o)


SLIDES.append(("p056", "Доступ к сетевому устройству", access()))


# ======================================================= сервисные маршрутизаторы ESR (p051 = pptx 7)
def esr_line():
    r = Ref(7, "p051")
    o = [r.img(44, 26, 188, 66, "logo", True),
         r.title(46, 84, 520, "СЕРВИСНЫЕ", 56),
         r.txt(46, 146, 520, "МАРШРУТИЗАТОРЫ", 48, "#6a84cc", 800, None, "letter-spacing:-.5px", 1.0),
         r.title(46, 198, 300, "ESR", 84),
         f'<div class="ab" style="left:{r.X(48)}px;top:{r.Y(285)}px;width:{r.X(34)}px;height:2px;background:#7d8fc4"></div>',
         r.txt(48, 295, 300, "Надёжная основа<br>современных сетей", 17, "#3a4370", 400, None, "font-style:italic"),
         r.box(518, 38, 985, 275, 1, 16),
         r.txt(556, 62, 415, "Сервисные маршрутизаторы Элтекс (ESR) — это современные устройства, которые "
               "пересылают пакеты между элементами сети, основываясь на правилах или таблицах маршрутизации. "
               "Линейка ESR включает решения для сетей любого масштаба — от компактных устройств "
               "до высокопроизводительных маршрутизаторов операторского класса.", 15.5, INK, 400, 1, lh=1.35),
         r.txt(1340, 74, 190, "СЕТИ<br>ОБЪЕДИНЯЮТ<br>ВОЗМОЖНОСТИ", 21, "#5d72b4", 400, None, lh=1.3),
         f'<div class="ab" style="left:{r.X(1342)}px;top:{r.Y(186)}px;width:{r.X(62)}px;height:2px;background:#8fa0d0"></div>',
         r.txt(1340, 200, 200, "БЕЗОПАСНОСТЬ<br>ПРОИЗВОДИТЕЛЬНОСТЬ<br>ГИБКОСТЬ", 11.5, "#6c7db4", 500, None, lh=1.9)]
    models = [
        ("ESR-10", "Компактное решение<br>для небольших сетей", 125, 378, "esr-10.webp", (80, 492, 410, 628),
         (20, 632, 452, 772), [(50, 650, 98, 694), (183, 650, 229, 694), (311, 650, 357, 694)],
         ["Компактный<br>корпус", "Базовый набор<br>интерфейсов", "Для небольших<br>офисов и филиалов"], [52, 184, 313], 700),
        ("ESR-30", "Оптимальный баланс<br>функциональности", 567, 343, "esr-30.webp", (515, 445, 950, 615),
         (455, 640, 962, 772), [(518, 653, 566, 699), (662, 653, 710, 699), (820, 653, 868, 699)],
         ["Расширенные<br>возможности", "Больше<br>интерфейсов", "Для корпоративных<br>сегментов"], [523, 668, 824], 705),
        ("ESR-1700", "Высокая производительность<br>для крупных сетей", 1048, 338, "esr-1700.webp",
         (982, 430, 1512, 625), (1035, 632, 1516, 772),
         [(1070, 648, 1120, 694), (1225, 648, 1275, 694), (1362, 648, 1412, 694)],
         ["Высокая<br>производительность", "Многоядерный<br>процессор", "Для операторов<br>и крупных компаний"],
         [1068, 1228, 1366], 698)]
    for i, (name, sub, x, y, photo, pb, fb, icons, labels, lx, ly) in enumerate(models):
        s = 2 + i
        o.append(r.box(*fb, s, 14))
        o.append(r.head(x, y, 300, name, 30, "#1e2550", s))
        o.append(r.txt(x, y + 42, 330, sub, 16, "#2c3560", 400, s, lh=1.3))
        o.append(r.dev(photo, *pb, s)[0])
        for j, (ib, lb, xx) in enumerate(zip(icons, labels, lx)):
            o.append(r.img(*ib, f"m{i}{j}", True, s, dl=j * 90))
            nx = lx[j + 1] if j < 2 else fb[2]
            o.append(r.txt(xx, ly, nx - xx - 4, lb, 13.5, "#2c3560", 400, s, lh=1.2, dl=j * 90))
    o.append(r.box(10, 785, 560, 980, 5, 16))
    o.append(r.head(72, 802, 420, "КЛЮЧЕВЫЕ ОТЛИЧИЯ МОДЕЛЕЙ", 20.5, "#1e2550", 5))
    for j, (ib, xx, lb) in enumerate([((72, 848, 128, 896), 75, "Набор<br>интерфейсов"),
                                      ((222, 848, 278, 896), 218, "Центральный<br>процессор"),
                                      ((400, 848, 452, 896), 376, "Производительность")]):
        o.append(r.img(*ib, f"k{j}", True, 5, dl=j * 90))
        o.append(r.txt(xx, 905, 170, lb, 15, "#2c3560", 400, 5, lh=1.25, dl=j * 90))
    o.append(r.box(565, 785, 1075, 975, 6, 16))
    o.append(r.img(596, 822, 672, 902, "stack", True, 6))
    o.append(r.txt(694, 817, 360, "Все устройства серии ESR имеют единый набор функциональных возможностей. "
                   "Разница между моделями заключается в объёме трафика, который они могут обрабатывать.",
                   16, INK, 400, 6, lh=1.35))
    o.append(r.txt(1240, 915, 265, "ОТ НЕБОЛЬШИХ ОФИСОВ<br>ДО МАСШТАБНЫХ СЕТЕЙ", 17, "#7f93c8", 400, 6,
                   "text-align:right"))
    return "".join(o)


SLIDES.append(("p051", "Сервисные маршрутизаторы ESR", esr_line()))


def pill(r, x0, y0, x1, y1, html, fs, s=None, col=NAVY, extra=""):
    return (f'<div class="ab"{r._s(s)} style="left:{r.X(x0)}px;top:{r.Y(y0)}px;width:{r.X(x1) - r.X(x0)}px;'
            f'min-height:{r.Y(y1) - r.Y(y0)}px;border-radius:8px;background:linear-gradient(180deg,#f3f6ff,#e2e9fb);'
            f'border:1px solid #c5d1f0;color:{col};font-size:{r.F(fs)}px;line-height:1.2;display:flex;'
            f'align-items:center;justify-content:center;text-align:center;{extra}">{html}</div>')


def dev_callouts(r, photo, box, marks, s):
    """Официальное фото + синие плашки + линии к точкам на фото (доли ширины/высоты фото)."""
    html, (l, t, w, h) = r.dev(photo, *box)
    o = [html]
    lines = []
    for (x0, y0, x1, y1, text, fx, fy) in marks:
        o.append(f'<div class="ab" data-s="{s}" style="left:{r.X(x0)}px;top:{r.Y(y0)}px;'
                 f'width:{r.X(x1) - r.X(x0)}px;height:{r.Y(y1) - r.Y(y0)}px;border-radius:6px;'
                 f'background:linear-gradient(180deg,#6c88e4,#4d69cf);border:1.5px solid #c8d4ff;color:#fff;'
                 f'font-weight:600;font-size:21px;line-height:1.12;display:flex;align-items:center;'
                 f'justify-content:center;text-align:center;box-shadow:0 6px 16px rgba(40,70,190,.3)">{text}</div>')
        px, py = l + fx * w, t + fy * h
        sx_, sy_ = (x0 + x1) / 2 * r.sx, y1 * r.sy
        lines.append(f'<path class="dr" pathLength="1" d="M{sx_:.0f} {sy_:.0f} L{px:.0f} {py:.0f}" '
                     f'stroke="#3f62d8" stroke-width="3" fill="none"/>'
                     f'<circle class="hd" cx="{px:.0f}" cy="{py:.0f}" r="7" fill="#3f62d8"/>')
    o.append(Ref.layer(f'<g data-s="{s}">' + "".join(lines) + '</g>'))
    return o


# ======================================================= подключение к устройству (p028 = pptx 6)
def connect():
    r = Ref(6, "p028")
    o = [f'<div class="ab" style="left:{r.X(33)}px;top:{r.Y(30)}px;width:2px;height:{r.Y(200)}px;'
         f'background:linear-gradient(#7d93e0,transparent)"></div>',
         r.title(58, 40, 680, "ПОДКЛЮЧЕНИЕ<br>К СЕТЕВОМУ УСТРОЙСТВУ", 46, lh=1.1),
         r.txt(60, 154, 660, "Для доступа к сетевому оборудованию можно использовать консольное подключение "
               "или удалённый доступ по протоколам Telnet/SSH.", 16.5, INK, 400, None, lh=1.3)]
    o += dev_callouts(r, "esr-20.webp", (690, -130, 1440, 290), [
        (1060, 52, 1300, 104, "Порты для управления<br>(Telnet / SSH)", 0.714, 0.83),
        (760, 52, 950, 104, "Консольный порт<br>(Console)", 0.38, 0.895)], 1)

    def need(x0, y0, x1, items, s, w):
        out = [f'<div class="ab" data-s="{s}" style="left:{r.X(x0)}px;top:{r.Y(y0)}px;width:{r.X(x1 - x0)}px;'
               f'height:{r.Y(30)}px;border-radius:6px;background:linear-gradient(90deg,#dfe6fb,rgba(223,230,251,0));'
               f'color:#2d3c84;font-weight:600;font-size:{r.F(16)}px;padding-left:12px;line-height:{r.Y(30)}px">'
               f'Что необходимо:</div>',
               f'<div class="ab" style="left:{r.X(x0 + 6)}px;top:{r.Y(y0 + 38)}px;width:{r.X(w)}px">']
        for j, t in enumerate(items):
            out.append(f'<div data-s="{s}" style="display:flex;gap:18px;align-items:center;margin-top:{6 if j else 0}px;'
                       f'min-height:{r.Y(40)}px;--dl:{j * 90}ms">'
                       f'<span style="flex:none;width:{r.Y(38)}px;height:{r.Y(38)}px;border-radius:10px;'
                       f'background:linear-gradient(160deg,#6d88e6,#3e58c4);color:#fff;font-weight:700;'
                       f'font-size:22px;display:flex;align-items:center;justify-content:center">{j + 1}</span>'
                       f'<span style="font-size:{r.F(14)}px;line-height:1.2;color:{INK}">{t}</span></div>')
        return out + ['</div>']

    # 01
    o.append(r.box(25, 282, 765, 852, 2, 18))
    o.append(numbox(r, 48, 300, 130, 368, "01", 40, 2))
    o.append(r.txt(150, 300, 420, "Консольное подключение", 28, NAVY, 700, 2))
    o.append(r.txt(150, 340, 380, "Используется для первоначальной настройки или когда недоступен удалённый доступ.",
                   16, DIM, 400, 2))
    o += need(42, 397, 390, ["Консольный порт на коммутаторе или маршрутизаторе (разъём RJ-45).",
                             "Консольный кабель (RJ-45 &harr; RS-232).", "Адаптер-переходник RS-232 – USB.",
                             "USB-интерфейс на ПК или ноутбуке администратора сети.",
                             "Программа эмуляции терминала (PuTTY, Tera Term, HyperTerminal, minicom и др.)."], 2, 345)
    o.append(r.img(505, 332, 748, 494, "cable2", True, 3))
    o.append(r.img(412, 418, 508, 494, "plug", True, 3))
    o.append(r.txt(420, 500, 80, "RJ-45", 17, "#1e2550", 700, 3))
    o.append(r.txt(655, 545, 100, "RS-232<br>(DE-9)", 16, "#1e2550", 700, 3, "text-align:center"))
    o.append(pill(r, 462, 546, 640, 578, "Консольный кабель", 15, 3))
    o.append(r.img(395, 598, 532, 702, "adapter", True, 3, dl=150))
    o.append(r.img(555, 598, 722, 702, "laptop", True, 3, dl=250))
    o.append(pill(r, 398, 704, 523, 746, "Адаптер<br>RS-232 – USB", 13.5, 3))
    o.append(pill(r, 530, 704, 752, 750, "Программа эмуляции<br>терминала (например, PuTTY)", 13, 3))
    o.append(r.box(50, 762, 737, 842, 3, 14))
    o.append(r.img(64, 765, 136, 832, "gear1", True, 3))
    o.append(r.txt(150, 773, 570, "При создании консольного подключения в программе эмуляции терминала "
                   "необходимо установить скорость 115200 бит/с.", 16, "#1e2550", 400, 3, lh=1.3))
    # 02
    o.append(r.box(772, 282, 1512, 852, 4, 18))
    o.append(numbox(r, 800, 300, 882, 368, "02", 40, 4))
    o.append(r.txt(906, 300, 520, "Удалённый доступ (Telnet / SSH)", 28, NAVY, 700, 4))
    o.append(r.txt(906, 340, 470, "Используется для управления устройством через сеть по IP-адресу.", 16, DIM, 400, 4))
    o += need(798, 397, 1140, ["Активный интерфейс с IP-адресом на коммутаторе или маршрутизаторе.",
                               "Кабель локальной сети (например, витая пара категории 7, разъём RJ-45).",
                               "Знать логин и пароль администратора.",
                               "ПК или ноутбук администратора сети подключены к локальной сети.",
                               "Программа эмуляции терминала (PuTTY, HyperTerminal, minicom и т.д.)."], 4, 365)
    o.append(r.img(1118, 402, 1508, 724, "putty", True, 5, extra="left:1452px;width:430px;top:450px"))
    o.append(r.box(802, 748, 1486, 844, 5, 14))
    o.append(r.img(812, 748, 886, 818, "gear2", True, 5, extra="top:808px"))
    o.append(r.txt(900, 754, 575, "При создании нового подключения в программе эмуляции терминала по протоколам "
                   "Telnet или SSH необходимо указать IP-адрес, настроенный на интерфейсе маршрутизатора во время "
                   "выполнения базовой настройки.", 15.5, "#1e2550", 400, 5, lh=1.25))
    for j, (bx, ib, tx, ttl, tw, txt) in enumerate([
        ((22, 860, 500, 1022), (58, 878, 134, 962), 140, "RJ-45", 355,
         "Registered Jack («Зарегистрированный разъём») — стандартизированный физический сетевой интерфейс, "
         "состоящий из «вилки» и «розетки», а также схемы их взаимодействия."),
        ((508, 860, 1040, 1022), (520, 878, 618, 945), 628, "RS-232", 405,
         "Recommended Standard 232 (EIA-232) — стандарт физического уровня, поддерживающий последовательный порт "
         "персональных компьютеров. Тип разъёма DE-9 (из-за формы в виде буквы «D», E — размер разъёма, "
         "9 контактов). В современных сетях почти вытеснен стандартом USB."),
        ((1048, 860, 1514, 1022), (1063, 878, 1152, 968), 1160, "Программы эмуляции терминала", 350,
         "Бывают платные, бесплатные и условно-бесплатные. Можно скачать в открытом доступе с официального "
         "сайта производителя.")]):
        o.append(r.box(*bx, 6, 14, dl=j * 120))
        o.append(r.img(*ib, f"b{j}", True, 6, dl=j * 120))
        o.append(r.txt(tx, 866, tw, f'<b style="color:#2a45b8;font-size:1.1em">{ttl}</b><br>{txt}', 12.5, "#3a4266", 400, 6, lh=1.08, dl=j * 120))
    return "".join(o)


SLIDES.append(("p028", "Подключение к сетевому устройству", connect()))


# ======================================================= функционал ESR (p012 = pptx 9)
def esr_functions():
    r = Ref(9, "p012")
    o = [r.img(0, 648, 1672, 941, "scene", False, 4,
               extra="-webkit-mask-image:linear-gradient(180deg,transparent,#000 12%);"
                     "mask-image:linear-gradient(180deg,transparent,#000 12%)"),
         r.dev("esr-3300.webp", 430, 735, 1180, 940, 4)[0],
         r.head(0, 22, 1672, "ОСНОВНОЙ ФУНКЦИОНАЛ МАРШРУТИЗАТОРОВ ESR", 42, "#14206a", None,
                "text-align:center"),
         r.txt(0, 74, 1672, "Возможности зависят от модели, версии ПО и установленных лицензий", 19, "#3f4f98",
               400, None, "text-align:center")]
    # где посмотреть
    o.append(r.box(25, 120, 368, 645, 1, 16))
    o.append(r.head(46, 132, 320, "ГДЕ ПОСМОТРЕТЬ<br>ФУНКЦИИ МОДЕЛИ", 25, "#14206a", 1))
    o.append(r.img(34, 198, 160, 640, "steps", True, 1))
    for j, (y, t) in enumerate([(228, "<b>eltex-co.ru</b>"), (312, "Каталог &rarr;<br>Маршрутизаторы ESR"),
                                (412, "Выбрать нужную<br>модель"), (512, "Документы и файлы"),
                                (582, "Руководство по эксплуатации<br>или Справочник команд CLI")]):
        o.append(r.txt(160, y - (12 if j == 4 else 0), 205, t, 15 if j < 4 else 13, "#1e2550", 400, 1, lh=1.2, dl=j * 90))
    # группы функций
    o.append(r.box(378, 120, 1218, 645, 2, 16))
    o.append(r.head(398, 132, 500, "ОСНОВНЫЕ ГРУППЫ ФУНКЦИЙ", 25, "#14206a", 2))
    cells = [
        ((390, 170, 655, 392), (486, 178, 562, 242), 250, "ИНТЕРФЕЙСЫ И VLAN", (408, 293, 454, 377), 467,
         [302, 345], ["Сетевые интерфейсы", "VLAN"]),
        ((663, 170, 930, 392), (758, 178, 838, 242), 248, "КОММУТАЦИЯ<br>И МАРШРУТИЗАЦИЯ", (676, 298, 722, 380), 735,
         [308, 346], ["L2, LAG/LACP", "RIP, OSPF, IS-IS, BGP"]),
        ((938, 170, 1205, 392), (1036, 178, 1112, 242), 248, "ТУННЕЛИ И VPN", (953, 280, 999, 390), 1011,
         [289, 325, 360], ["MPLS, GRE, DMVPN", "IPsec, OpenVPN", "WireGuard, PPTP, L2TP"]),
        ((390, 400, 655, 635), (486, 412, 562, 476), 482, "СЕТЕВЫЕ СЕРВИСЫ", (408, 518, 454, 607), 470,
         [529, 573], ["NAT и DHCP", "QoS"]),
        ((663, 400, 930, 635), (758, 410, 838, 474), 479, "БЕЗОПАСНОСТЬ", (678, 510, 722, 624), 738,
         [521, 557, 593], ["ACL и Firewall", "IPS/IDS", "Защита от DoS/DDoS"]),
        ((938, 400, 1205, 635), (1033, 410, 1112, 474), 476, "РЕЗЕРВИРОВАНИЕ<br>И МОНИТОРИНГ", (950, 520, 997, 627),
         1010, [531, 565, 599], ["VRRP, MultiWAN, кластер 1+1", "SNMP, Syslog, NetFlow", "Zabbix и SLA"])]
    for j, (cb, big, ty, ttl, strip, tx, ys, items) in enumerate(cells):
        dl = j * 110
        o.append(r.box(*cb, 2, 12, dl=dl))
        o.append(r.img(*big, f"g{j}", True, 2, dl=dl))
        o.append(r.head(cb[0], ty, cb[2] - cb[0], ttl, 16.5, "#14206a", 2, f"text-align:center;--dl:{dl}ms"))
        o.append(r.img(*strip, f"gs{j}", True, 2, dl=dl))
        for y, t in zip(ys, items):
            o.append(r.txt(tx, y, cb[2] - tx - 4, t, 14.5, "#1e2550", 400, 2, "letter-spacing:-.2px", lh=1.0, dl=dl))
    # критерии
    o.append(r.box(1228, 120, 1650, 645, 3, 16))
    o.append(r.head(1250, 134, 400, "КЛЮЧЕВЫЕ КРИТЕРИИ ВЫБОРА", 24, "#14206a", 3))
    tiles = [("Количество<br>и скорость портов", 0, 0), ("Производительность<br>маршрутизации", 1, 0),
             ("Производительность<br>Firewall и VPN", 0, 1), ("Поддерживаемые<br>протоколы", 1, 1),
             ("Безопасность", 0, 2), ("Резервирование", 1, 2)]
    for j, (t, c, rw) in enumerate(tiles):
        x0, x1 = (1240, 1432) if c == 0 else (1440, 1640)
        y0, y1 = [(178, 320), (328, 472), (480, 632)][rw]
        dl = j * 90
        o.append(r.box(x0, y0, x1, y1, 3, 12, dl=dl))
        o.append(r.img(x0 + 55, y0 + 12, x1 - 55, y0 + 82, f"c{j}", True, 3, dl=dl))
        o.append(r.txt(x0, y0 + 84 if rw < 2 else y0 + 100, x1 - x0, t, 16, "#1e2550", 400, 3,
                       "text-align:center", lh=1.2, dl=dl))
    return "".join(o)


SLIDES.append(("p012", "Основной функционал маршрутизаторов ESR", esr_functions()))


# ======================================================= память маршрутизатора (p073 = pptx 10)
def memory():
    r = Ref(10, "p073")
    H = "#1e2a6e"
    o = [r.img(440, 0, 772, 378, "hero", False, None,
               extra="-webkit-mask-image:radial-gradient(ellipse 70% 75% at 55% 45%,#000 55%,transparent 100%);"
                     "mask-image:radial-gradient(ellipse 70% 75% at 55% 45%,#000 55%,transparent 100%)"),
         r.title(32, 92, 500, "ПАМЯТЬ", 48),
         r.txt(32, 148, 520, "МАРШРУТИЗАТОРА", 41, "#4b5ca4", 800, None, "letter-spacing:-.3px", 1.0),
         r.txt(32, 204, 360, "Где хранятся данные<br>и что с ними происходит", 22, "#2c3560", 400, None, lh=1.25),
         f'<div class="ab" style="left:{r.X(33)}px;top:{r.Y(296)}px;width:{r.X(280)}px;height:1px;background:#b4bfe0"></div>',
         kick(r, 33, 318, 400, "Работа. Хранение. Стабильность.", 12, "#5d6aa0", 2.5)]
    # ОЗУ
    o.append(r.box(762, 22, 1225, 382, 1, 18))
    o.append(r.img(780, 38, 832, 92, "ic_ram", True, 1))
    o.append(r.head(848, 46, 370, "ОПЕРАТИВНАЯ ПАМЯТЬ (ОЗУ)", 20.5, H, 1))
    o.append(r.txt(848, 88, 365, "ОЗУ — это энергозависимая память, в которой находятся данные, но только до момента "
                   "отключения электропитания. При перезагрузке маршрутизатора содержимое ОЗУ теряется.<br>"
                   "<span style='display:block;margin-top:6px'>Физически ОЗУ — это модули памяти, вставляемые "
                   "в слоты материнской платы.</span>", 14, INK, 400, 1, lh=1.13))
    for j, (x0, x1, lbl) in enumerate([(785, 988, "DDR3"), (1003, 1208, "DDR4")]):
        o.append(r.box(x0, 268, x1, 374, 1, 10, dl=200 + j * 120))
        o.append(r.txt(x0, 270, x1 - x0, lbl, 17, H, 700, 1, "text-align:center", dl=200 + j * 120))
        o.append(r.img(x0 + 8, 272, x1 - 8, 356, f"ddr{j}", True, 1, dl=200 + j * 120, extra="margin-top:22px"))
    o.append(r.img(1222, 205, 1390, 372, "cube", True, 1))
    o.append(r.txt(1385, 236, 150, "Данные<br>в ОЗУ существуют только пока устройство включено", 14, INK, 400, 1, lh=1.2))
    # что хранится в ОЗУ
    o.append(r.box(10, 388, 985, 656, 2, 18))
    o.append(r.img(32, 396, 88, 446, "ic_ram2", True, 2))
    o.append(r.head(102, 404, 500, "ЧТО ХРАНИТСЯ В ОЗУ", 20.5, H, 2))
    tiles = [((25, 455, 246, 640), (38, 464, 100, 524), 106, "Конфигурация кандидат (candidate-config)",
              "Файл, куда записываются, но ещё не применяются все вводимые настройки."),
             ((262, 455, 476, 640), (272, 464, 328, 516), 334, "Буфер обмена",
              "Временный файл, который сохраняет приходящие на интерфейс пакеты или перед их отправкой."),
             ((490, 455, 716, 640), (498, 464, 556, 512), 562, "Таблица маршрутизации",
              "Хранит информацию о сетях и маршрутах к этим сетям. Используется для поиска оптимального маршрута."),
             ((730, 455, 962, 640), (742, 468, 808, 500), 812, "Таблица ARP",
              "Содержит сопоставления IP-адресов с MAC-адресами (аналогично ARP-кэшу на ПК). Используется "
              "интерфейсами типа GigabitEthernet, TenGigabitEthernet и т.д.")]
    for j, (tb, ib, tx, ttl, txt) in enumerate(tiles):
        dl = j * 110
        o.append(r.box(*tb, 2, 12, dl=dl))
        o.append(r.img(*ib, f"t{j}", True, 2, dl=dl))
        o.append(r.txt(tx, 464, tb[2] - tx - 6, ttl, 13.5, H, 700, 2, lh=1.15, dl=dl))
        o.append(r.txt(tb[0] + 10, [548, 520, 520, 506][j], tb[2] - tb[0] - 14, txt, 12.5, INK, 400, 2, lh=1.06, dl=dl))
    # текущая конфигурация
    o.append(r.box(998, 388, 1530, 656, 3, 18))
    o.append(r.img(1026, 395, 1078, 449, "ic_doc", True, 3))
    o.append(r.head(1098, 404, 420, "ТЕКУЩАЯ КОНФИГУРАЦИЯ", 20.5, H, 3))
    o.append(r.box(1040, 460, 1515, 638, 3, 12))
    o.append(r.img(1386, 452, 1514, 592, "srv", True, 3))
    o.append(r.img(1056, 476, 1142, 578, "doc", True, 3))
    o.append(r.txt(1155, 482, 240, "running-config", 17, H, 700, 3, "font-family:var(--mono)"))
    o.append(r.txt(1155, 515, 235, "Файл в ПЗУ, в который записываются команды конфигурирования, по которым "
                   "маршрутизатор работает в данный момент.", 13.5, INK, 400, 3, lh=1.15))
    # ПЗУ
    o.append(r.img(0, 655, 255, 1024, "flash", False, None,
                   extra="-webkit-mask-image:linear-gradient(90deg,#000 60%,transparent);"
                         "mask-image:linear-gradient(90deg,#000 60%,transparent)"))
    o.append(r.box(95, 668, 672, 1010, 4, 18))
    o.append(r.img(128, 680, 178, 732, "ic_db", True, 4))
    o.append(r.head(195, 688, 460, "ПОСТОЯННАЯ ПАМЯТЬ (ПЗУ)", 20.5, H, 4))
    o.append(r.txt(196, 722, 465, "ПЗУ — это энергонезависимая память, в которой находятся данные (инструкции по "
                   "загрузке, POST, файлы конфигурации, файлы прошивки). Эти данные остаются на маршрутизаторе "
                   "даже после отключения питания.<span style='display:block;margin-top:6px'>Физически — это "
                   "встроенная плата памяти в материнскую плату маршрутизатора.</span>", 14.5, INK, 400, 4, lh=1.2))
    o.append(r.box(250, 900, 656, 998, 4, 12))
    o.append(r.img(262, 896, 296, 930, "ic_info", True, 4, extra="margin-top:14px"))
    o.append(r.txt(303, 906, 345, "На маршрутизаторах серии ESR ПЗУ существует двух типов: SPI NOR Flash "
                   "и NAND Flash (eMMC).", 14.5, "#1e2550", 400, 4, lh=1.18))
    for j, (x0, x1, ic, ttl, chip, items) in enumerate([
        (680, 1100, (708, 684, 764, 736), "SPI NOR FLASH", (870, 862, 1098, 1004),
         ["Загрузчик U-Boot и переменные окружения U-Boot", "Factory-параметры (S/N, MAC, HW rev.)",
          "Номер активного раздела (image-1 или image-2)", "Параметры инициализации DDR-памяти",
          "Логи критичных событий (/mnt/critlog)", "Boot-лицензия"]),
        (1112, 1530, (1138, 684, 1194, 736), "NAND FLASH (eMMC)", (1300, 862, 1528, 1004),
         ["Раздел с конфигурацией running-config (/mnt/config)", "Раздел с образом firmware (image-1/2)",
          "Раздел для хранения дополнительной информации (/mnt/data)"])]):
        st = 5 + j
        o.append(r.box(x0, 668, x1, 1010, st, 18))
        o.append(r.img(*chip, f"chip{j}", True, st, extra="opacity:.45"))
        o.append(r.img(*ic, f"ic_f{j}", True, st))
        o.append(r.head(x0 + 92, 694, 300, ttl, 19, H, st))
        o.append(r.txt(x0 + 92, 727, 200, "Содержит:", 14, H, 700, st))
        o.append(r.txt(x0 + 70, 748, x1 - x0 - 80, ul(items, 0), 13, INK, 400, st, lh=1.12))
    return "".join(o)


SLIDES.append(("p073", "Память маршрутизатора", memory()))


# ======================================================= панели устройств: официальное фото + карточки-выноски
CARD_BG = ("background:linear-gradient(158deg,rgba(255,255,255,.93),rgba(240,244,255,.84));"
           "border:1.5px solid rgba(160,178,230,.6);border-radius:16px;"
           "box-shadow:0 10px 30px rgba(70,90,170,.14),inset 0 1px 0 #fff;")


def pcard(r, x0, y0, x1, num, title, icon, body, s, title_col="#2440c0", fs=15, tfs=19, upper=False):
    """Карточка выноски: номер + заголовок, ниже иконка (вырезка) и текст; высота по содержимому."""
    tt = "text-transform:uppercase;" if upper else ""
    ic = (f'<img src="{icon}" style="width:{r.X(70)}px;flex:none">' if icon else "")
    return (f'<div class="ab" data-s="{s}" style="left:{r.X(x0)}px;top:{r.Y(y0)}px;width:{r.X(x1 - x0)}px;'
            f'{CARD_BG}padding:0 {r.X(16)}px {r.Y(14)}px 0">'
            f'<div style="display:flex;align-items:center;gap:{r.X(18)}px">'
            f'<span style="flex:none;width:{r.X(54)}px;height:{r.Y(46)}px;border-radius:14px 6px 14px 6px;'
            f'background:linear-gradient(160deg,#5b7cf0,#2c47c4);color:#fff;font-weight:800;font-size:{r.F(30)}px;'
            f'display:flex;align-items:center;justify-content:center;box-shadow:0 6px 14px rgba(40,70,190,.35);'
            f'margin-top:-2px">{num}</span>'
            f'<span style="font-weight:800;font-size:{r.F(tfs)}px;color:{title_col};line-height:1.12;{tt}'
            f'padding-top:{r.Y(8)}px">{title}</span></div>'
            f'<div style="display:flex;gap:{r.X(18)}px;align-items:center;padding-left:{r.X(18)}px;margin-top:{r.Y(6)}px">'
            f'{ic}<div style="font-size:{r.F(fs)}px;line-height:1.2;color:{INK}">{body}</div></div></div>')


def panel_slide(n, pref, title, sub, photo, fit, cards, wires, title_fs=92, sub_col="#3b52b8", extra=None):
    """fit = (x0, x1, y_bottom) — куда в оригинале ложится фото (по ширине, низом).
    wires = [(шаг, [(x, y) точки оригинала ...], (px, py) точка на фото в пикселях фото)]."""
    r = Ref(n, pref)
    w0, h0 = Image.open(ASSETS / "dev" / photo).size
    x0, x1, yb = fit
    yt = yb - (x1 - x0) * h0 / w0
    html, (l, t, w, h) = r.dev(photo, x0, yt, x1, yb)
    o = [html, r.title(58, 26, 900, title, title_fs),
         r.txt(62, 112, 800, sub, 26, sub_col, 600, None, "letter-spacing:2px;text-transform:uppercase", 1.0)]
    paths = []
    for st, pts, (px, py) in wires:
        P = [(x * r.sx, y * r.sy) for x, y in pts] + [(l + px * w / w0, t + py * h / h0)]
        d = "M" + " L".join(f"{a:.0f} {b:.0f}" for a, b in P)
        paths.append(f'<g data-s="{st}"><path class="dr" pathLength="1" d="{d}" stroke="#2f5fe0" stroke-width="3" '
                     f'fill="none" stroke-linejoin="round"/>'
                     f'<circle class="hd" cx="{P[-1][0]:.0f}" cy="{P[-1][1]:.0f}" r="7" fill="#fff" '
                     f'stroke="#2f5fe0" stroke-width="3"/>'
                     f'<circle class="hd" cx="{P[0][0]:.0f}" cy="{P[0][1]:.0f}" r="5" fill="#2f5fe0"/></g>')
    o.append(Ref.layer(*paths))
    for c in cards:
        x0_, y0_, x1_, num, ttl, ib, body = c[:7]
        kw = c[7] if len(c) > 7 else {}
        icon = r.src(*ib, f"ic{num}") if ib else None
        o.append(pcard(r, x0_, y0_, x1_, num, ttl, icon, body, kw.pop("s", int(num)), **kw))
    if extra:
        o += extra(r)
    return "".join(o)


def bl(items):
    return ul(items, 0)


SLIDES.append(("p040", "ESR-200: передняя панель", panel_slide(
    11, "p040", "ESR-200", "Передняя панель", "esr-200.webp", (205, 1465, 606),
    [(58, 166, 450, "1", "Слот для SD-карты", (72, 228, 142, 310),
      "Имеется у всех, кроме младших моделей (ESR-10/12V/12VF/14VF). Может хранить образ системы, файлы журнала, "
      "файлы настройки, резервные копии конфигурации и любые другие файлы, необходимые для работы системы."),
     (238, 665, 548, "2", "USB-разъёмы", (250, 722, 328, 806),
      "Два USB-разъёма для подключения flash-карт и 3G/4G модемов."),
     (562, 166, 942, "3", "Сетевые интерфейсы", (583, 230, 662, 298),
      "Медные и комбинированные. Комбинированный интерфейс может использоваться как для медных соединений, "
      "так и для оптоволоконных, но только с использованием модулей SFP/SFP+/QSFP/QSFP+."),
     (1012, 166, 1476, "4", "Индикаторы состояния", (1040, 226, 1132, 342),
      "Отображают состояние:" + bl(["электропитание;", "текущее состояние устройства;",
                                     "наличие и уровень аварии устройства;", "состояние вентиляторов."])),
     (616, 655, 990, "5", "Функциональная кнопка F", (632, 735, 698, 802),
      "Используется для перезагрузки устройства и сброса к заводским настройкам:"
      + bl(["удержание менее 10 секунд — перезагрузка устройства;",
            "удержание более 10 секунд — перезагрузка и сброс к заводским настройкам."])),
     (1012, 665, 1330, "6", "Консольный интерфейс", (1026, 718, 1100, 792),
      "Используется для локального управления устройством."),
     (1378, 665, 1642, "7", "Разъём питания", (1398, 712, 1468, 802),
      "Для подключения к источнику электропитания переменного тока.")],
    [(1, [(193, 362)], (90, 386)), (2, [(388, 665), (388, 612), (350, 612)], (196, 368)),
     (2, [(388, 612), (428, 612)], (256, 368)), (3, [(766, 362), (766, 398), (600, 398)], (365, 300)),
     (3, [(766, 398), (938, 398)], (590, 297)), (4, [(1073, 362)], (698, 352)),
     (5, [(976, 655), (976, 640), (1122, 640)], (766, 368)), (6, [(1210, 665)], (828, 372)),
     (7, [(1488, 665), (1488, 650), (1418, 650)], (980, 345))])))

SLIDES.append(("p005", "ESR-200: задняя панель", panel_slide(
    12, "p005", "ESR-200", "Задняя панель", "esr-200-back.webp", (100, 1572, 588),
    [(115, 657, 612, "1", "Клемма для заземления<br>устройства", (180, 738, 268, 826),
      "Используется для подключения маршрутизатора к контуру заземления.", {"tfs": 19.5}),
     (850, 657, 1322, "2", "Вентиляционный модуль", (938, 728, 1022, 812),
      "Обеспечивает эффективное охлаждение устройства и стабильную работу системы.", {"tfs": 19.5})],
    [(1, [(287, 657), (287, 628), (182, 628)], (78, 375)),
     (2, [(1050, 657), (1050, 628), (928, 628)], (632, 352)),
     (2, [(1050, 628), (1170, 628)], (815, 352))], title_fs=82)))

SLIDES.append(("p038", "ESR-3300: передняя панель", panel_slide(
    13, "p038", "ESR-3300", "Передняя панель", "esr-3300.webp", (88, 1585, 582),
    [(92, 188, 518, "1", "2.5GE [1 ... 4]", (115, 246, 210, 336),
      "4 порта 1000BASE-X/10GBASE-R/25GBASE-R."),
     (535, 188, 950, "2", "40/100GE [1 ... 4]", (552, 255, 722, 318),
      "4 порта Ethernet 40GBASE-R (QSFP+)/100GBASE-R (QSFP28)."),
     (967, 188, 1251, "3", "USB", (990, 246, 1068, 330), "Порт USB 3.0 для подключения USB-устройств."),
     (1268, 188, 1594, "4", "microSD", (1288, 250, 1385, 320), "Разъем для установки microSD-карт памяти."),
     (78, 640, 386, "5", "Console", (94, 698, 180, 782),
      "Консольный порт RS-232 (RJ-45) для локального управления устройством."),
     (398, 640, 732, "6", "OOB", (414, 698, 500, 782),
      "Ethernet-интерфейс для удаленного доступа и управления, в том числе для резервного доступа через "
      "вторичный загрузчик U-Boot."),
     (742, 640, 1162, "7", "F", (758, 698, 848, 782),
      "Функциональная кнопка для перезагрузки устройства и сброса к заводским настройкам:"
      + bl(["удержание менее 10 секунд — перезагрузка устройства;",
            "удержание более 10 секунд — перезагрузка и сброс к заводским настройкам."])),
     (1173, 640, 1612, "8", "Индикаторы состояния", None,
      "<b>Status</b> — текущее состояние устройства.<br><b>Alarm</b> — наличие и уровень аварии.<br>"
      "<b>User</b> — пользовательские сценарии.<br><b>Flash</b> — активность обмена с microSD/USB Flash.<br>"
      "<b>Power</b> — питание устройства.<br><b>Master</b> — работа в failover-режимах.<br>"
      "<b>Fan</b> — состояние вентиляторов.<br><b>RPS</b> — резервный источник питания.", {"fs": 13.5})],
    [(1, [(554, 345), (554, 425), (494, 425)], (322, 300)), (1, [(554, 425), (612, 425)], (383, 300)),
     (2, [(778, 345)], (522, 340)), (3, [(1032, 345), (1032, 380), (932, 380)], (659, 335)),
     (4, [(1122, 345), (1122, 408), (1008, 408)], (722, 352)),
     (5, [(636, 632), (636, 606), (1093, 606)], (776, 305)), (6, [(1093, 606), (1093, 590)], (776, 345)),
     (7, [(1008, 632), (1008, 615), (1152, 615)], (818, 340)),
     (8, [(1404, 632), (1404, 605), (1312, 605)], (858, 330))], title_fs=88)))

SLIDES.append(("p068", "ESR-3300: задняя панель", panel_slide(
    14, "p068", "ESR-3300", "Задняя панель", "esr-3300-back.webp", (82, 1592, 608),
    [(58, 172, 532, "1", "Слоты для источников питания", (82, 228, 180, 335),
      "На старших моделях предусмотрено 2 слота для установки источников питания на переменный либо постоянный "
      "ток. Использовать одновременно можно разные источники питания, замену можно выполнять без отключения "
      "устройства."),
     (585, 172, 1050, "3", "Съемные вентиляторные модули", (615, 230, 708, 322),
      "На старших моделях имеются зарезервированные вентиляторные блоки, обеспечивающие эффективное охлаждение "
      "устройства и повышение надёжности работы. Вентиляторные модули поддерживают горячую замену.", {"s": 2}),
     (1100, 172, 1614, "4", "Место для резервного источника питания", (1130, 232, 1265, 345),
      "Источники питания на старших моделях не входят в комплект поставки и приобретаются отдельно, исходя "
      "из потребностей заказчика.", {"s": 3}),
     (168, 676, 594, "2", "Клемма заземления", (192, 734, 282, 820),
      "Используется для подключения маршрутизатора к контуру заземления.", {"s": 4}),
     (872, 664, 1522, "5", "Особенности питания по моделям", (900, 735, 985, 845),
      bl(["Для ESR-10 и ESR-15 – внешний источник питания 12 В.",
          "Модели ESR-12, ESR-14 (с разными литерами), ESR-15R, ESR-20, ESR-21 имеют встроенный источник питания "
          "на 220 В (1 источник переменного тока).",
          "На старших моделях можно использовать одновременно разные источники питания, заменять их можно "
          "не отключая устройство."]), {"s": 5})],
    [(1, [(172, 380)], (85, 300)), (2, [(834, 380), (834, 432), (590, 432)], (385, 300)),
     (2, [(834, 432), (1076, 432)], (660, 300)), (3, [(1500, 380)], (1000, 300)),
     (4, [(594, 762), (648, 762), (648, 658), (370, 658)], (215, 315)),
     (5, [(1288, 664)], (878, 315))], title_fs=88)))

SLIDES.append(("p079", "MES1428: передняя панель", panel_slide(
    46, "p079", "КОНСТРУКТИВНОЕ ИСПОЛНЕНИЕ", "Передняя панель MES1428", "mes1428.webp", (68, 1605, 612),
    [(80, 198, 528, "1", "РАЗЪЁМ ПИТАНИЯ", (118, 268, 188, 342), "Подключение к источнику переменного тока",
      {"title_col": NAVY, "fs": 17}),
     (588, 198, 1052, "3", "КОНСОЛЬНЫЙ ИНТЕРФЕЙС", (632, 262, 718, 335), "Локальное управление устройством",
      {"title_col": NAVY, "fs": 17, "s": 2}),
     (1108, 198, 1585, "5", "ETHERNET-ИНТЕРФЕЙСЫ", (1168, 262, 1252, 335), "Порты 10/100BASE-TX (RJ-45)",
      {"title_col": NAVY, "fs": 17, "s": 3}),
     (70, 702, 538, "2", "ИНДИКАТОРЫ", None,
      "<b style='color:#2440c0'>Power</b> — индикатор питания устройства<br>"
      "<b style='color:#2440c0'>Alarm</b> — индикатор перегрева", {"title_col": NAVY, "fs": 17, "s": 4}),
     (592, 702, 1085, "4", "ФУНКЦИОНАЛЬНАЯ КНОПКА F", (632, 768, 704, 840),
      "Менее 10 секунд — перезагрузка<br>Более 10 секунд — перезагрузка и сброс настроек",
      {"title_col": NAVY, "fs": 17, "s": 5}),
     (1140, 702, 1605, "6", "COMBO-ПОРТЫ", (1172, 765, 1262, 840), "Порты 10/100/1000BASE-T (RJ-45)",
      {"title_col": NAVY, "fs": 17, "s": 6})],
    [(1, [(178, 355)], (95, 160)), (2, [(596, 268), (596, 375), (462, 375)], (222, 185)),
     (3, [(1152, 355), (1152, 390), (838, 390)], (520, 150)),
     (4, [(275, 702), (275, 658), (332, 658)], (170, 192)),
     (5, [(696, 702), (696, 658), (488, 658)], (250, 190)),
     (6, [(1418, 702), (1418, 630)], (1000, 205))], title_fs=66)))

SLIDES.append(("p015", "MES1428: задняя панель", panel_slide(
    47, "p015", "MES1428", "Задняя панель", "mes1428-back.webp", (108, 1560, 545),
    [(1176, 594, 1566, "1", "КЛЕММА ЗАЗЕМЛЕНИЯ", (1250, 632, 1332, 712),
      "Подключение корпуса устройства к контуру защитного заземления", {"title_col": "#2440c0", "tfs": 17,
                                                                         "s": 2}),
     (406, 612, 888, "2", "ВЕНТИЛЯЦИОННЫЕ ОТВЕРСТИЯ", (484, 664, 558, 738),
      "Обеспечивают теплообмен и охлаждение компонентов", {"title_col": "#2440c0", "tfs": 17, "s": 1})],
    [(1, [(660, 612), (660, 575), (370, 575)], (280, 170)), (1, [(660, 575), (1133, 575)], (800, 170)),
     (2, [(1492, 594)], (1078, 200))], title_fs=82,
    extra=lambda r: [r.box(1064, 750, 1640, 912, 3, 16),
                     r.head(1092, 762, 400, "НА ДРУГИХ МОДЕЛЯХ", 20, NAVY, 3),
                     r.img(1120, 800, 1192, 850, "o1", True, 3), r.img(1316, 800, 1392, 850, "o2", True, 3),
                     r.img(1512, 792, 1582, 850, "o3", True, 3),
                     r.txt(1070, 850, 180, "Разъём питания переменного тока", 14, INK, 400, 3, "text-align:center"),
                     r.txt(1258, 850, 196, "Разъём аккумуляторной батареи", 14, INK, 400, 3, "text-align:center"),
                     r.txt(1466, 850, 160, "Вентиляторные модули", 14, INK, 400, 3, "text-align:center")])))
