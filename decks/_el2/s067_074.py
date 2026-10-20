# -*- coding: utf-8 -*-
"""Слайды по референсам p067-p074 (загрузка, ESR-3300, WLC, базовые станции, файлы конфигурации, память, POST)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, arrow_svg

SLIDES = []
K = 1920 / 1400          # масштаб референса 1400 px -> холст
TH = 1920 / 900          # масштаб превью 900 px -> холст
KY = 1080 / 933          # вертикаль для референсов 3:2
RED = "#d3213f"
AR = ('<svg viewBox="0 0 24 12" style="width:26px;height:13px;vertical-align:middle;margin:0 5px">'
      '<path d="M1 6h20M16 1l6 5-6 5" fill="none" stroke="currentColor" stroke-width="2.2" '
      'stroke-linecap="round" stroke-linejoin="round"/></svg>')
CHIP = ('<rect x="7" y="7" width="10" height="10" rx="1.5"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4'
        'M3 10h4M3 14h4M17 10h4M17 14h4"/>')
SPK = '<path d="M4 9v6h4l5 4V5L8 9z"/><path d="M16 9a4 4 0 0 1 0 6M18.5 6.5a8 8 0 0 1 0 11"/>'
BIG = 'class="ico" style="width:{s}px;height:{s}px;border-radius:{r}px"'


def ab(l, t, w=None, h=None, extra=""):
    s = f"position:absolute;left:{round(l)}px;top:{round(t)}px;"
    if w is not None: s += f"width:{round(w)}px;"
    if h is not None: s += f"height:{round(h)}px;"
    return s + extra


def layer(*parts):
    return ('<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" '
            'viewBox="0 0 1920 1080">' + "".join(parts) + '</svg>')


def img(name, l, t, w, h=None, s=None, extra="", cls="cut", fit=False):
    d = f' data-s="{s}"' if s else ""
    st = ab(l, t, w, h, extra + (";object-fit:cover" if fit else ""))
    return f'<img class="{cls} ab" src="assets/{name}"{d} style="{st}">'


def chipimg(name, l, t, w, h, s=None):
    d = f' data-s="{s}"' if s else ""
    return (f'<img class="ab" src="assets/{name}"{d} style="{ab(l, t, w, h)}mix-blend-mode:multiply;'
            f'object-fit:cover">')


def xi(inner, cls="sm"):
    return f'<span class="ico {cls}"><svg viewBox="0 0 24 24">{inner}</svg></span>'


def big_ico(html, size, radius=22, bare=False):
    extra = ";border:none;background:none" if bare else ""
    h = html.replace('class="ico "', BIG.format(s=size, r=radius).rstrip('"') + extra + '"')
    return h.replace('<svg viewBox', f'<svg style="width:{int(size * .55)}px;height:{int(size * .55)}px" viewBox')


def faded(name, l, t, w, h, s=None, f=7, extra=""):
    d = f' data-s="{s}"' if s else ""
    g = lambda dr: (f"linear-gradient(to {dr},transparent,#000 {f}%,#000 {100 - f}%,transparent)")
    m = f"{g('right')},{g('bottom')}"
    return (f'<div class="ab"{d} style="{ab(l, t, w, h)}-webkit-mask-image:{m};mask-image:{m};'
            f'-webkit-mask-composite:source-in;mask-composite:intersect;{extra}">'
            f'<img src="assets/{name}" style="width:100%;height:100%;display:block;object-fit:cover"></div>')


def dot(color="var(--blue)", size=11):
    return (f'<span style="flex:none;width:{size}px;height:{size}px;border-radius:50%;background:{color};'
            f'margin-top:.42em"></span>')


def bullets(items, fs=20, gap=6, lh=1.25, color="var(--blue)"):
    return "".join(
        f'<div style="display:flex;gap:12px;align-items:flex-start;margin-bottom:{gap}px;font-size:{fs}px;'
        f'line-height:{lh};color:var(--ink)">{dot(color, max(8, int(fs // 2)))}<div>{t}</div></div>' for t in items)


def gline(d, s, dots=()):
    c = "".join(f'<circle cx="{x}" cy="{y}" r="6" fill="var(--blue)"/>' for x, y in dots)
    return (f'<g data-s="{s}"><path class="dr" pathLength="1" d="{d}" stroke="var(--blue)" stroke-width="3" '
            f'fill="none"/>{c}</g>')


def kcard(l, t, w, h, s=None, cls="card", inner="", extra=""):
    d = f' data-s="{s}"' if s else ""
    return f'<div class="{cls}"{d} style="{ab(l, t, w, h)}{extra}">{inner}</div>'


def hd(t, fs=26, color="var(--navy)", extra=""):
    return (f'<div style="font-size:{fs}px;font-weight:800;color:{color};text-transform:uppercase;'
            f'line-height:1.15;{extra}">{t}</div>')


def title(t, top=30, fs=64):
    return f'<h1 class="t ab ctr-x" style="top:{top}px;width:1800px;font-size:{fs}px">{t}</h1>'


def doc_svg(gid, c1, c2, l, t, w, h):
    return (f'<svg class="ab" style="{ab(l, t, w, h)}" viewBox="0 0 60 78"><defs><linearGradient id="{gid}" x1="0" y1="0" '
            f'x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>'
            f'<path d="M4 4h36l16 16v54H4z" fill="url(#{gid})"/><path d="M40 4v16h16z" fill="rgba(255,255,255,.55)"/>'
            f'<path d="M14 36h32M14 46h32M14 56h22" stroke="#fff" stroke-width="3.4" stroke-linecap="round"/></svg>')


# ======================================================= p067 POST и процесс загрузки
def post_boot():
    o = [title("POST и процесс загрузки коммутатора", 10, 62),
         f'<div class="ab ctr-x" style="top:84px;width:1800px;text-align:center;font-size:27px;color:var(--navy)">'
         f'Четыре последовательных этапа: инициализация{AR}выбор источника{AR}проверка подлинности{AR}запуск</div>']

    post = ['<div class="ab" style="left:32px;top:14px;font-size:50px;font-weight:800;color:var(--navy);line-height:1">'
            'POST <span style="font-size:32px;color:var(--blue);margin-left:6px">— POWER ON SELF TEST</span></div>',
            '<div class="ab" style="left:32px;top:86px;width:340px;font-size:22px;font-weight:700;color:var(--navy);'
            'line-height:1.3">Самотестирование при включении электропитания.</div>',
            '<div class="ab" style="left:32px;top:170px;width:320px;font-size:21px;line-height:1.35;color:var(--ink)">'
            'POST проверяет наличие и работоспособность компонентов до начала работы устройства.</div>']
    o.append(kcard(34, 122, 830, 312, 1, "card", "".join(post), "padding:0"))

    cx, cy = 610, 311
    nodes = [("sd", 494, 219, "Память", 494, 242, "c"), ("gear", 668, 219, "Прошивка", 700, 209, "l"),
             ("fan", 446, 322, "Вентиляторы", 446, 347, "c"), ("doc", 765, 322, "Конфигурация", 771, 347, "c"),
             ("cable", 512, 412, "Интерфейсы", 556, 399, "l")]
    lines = "".join(f'<path d="M{cx} {cy} L{x} {y}" stroke="#6b94e0" stroke-width="2" stroke-dasharray="3 7" '
                    f'stroke-linecap="round" fill="none"/>' for _, x, y, *_ in nodes)
    o.append(f'<div class="ab" data-s="1" style="left:0;top:0">{layer(lines)}</div>')
    o.append(chipimg("p067_cpu_big.jpg", 530, 254, 160, 118, 1))
    for icn, x, y, lab, lx, ly, al in nodes:
        o.append(f'<div class="ab" data-s="1" style="{ab(x - 28, y - 28)}">{ico(icn, "sm")}</div>')
        if al == "c":
            o.append(f'<div class="ab" data-s="1" style="{ab(lx - 100, ly, 200)}text-align:center;font-size:20px;color:var(--navy)">{lab}</div>')
        else:
            o.append(f'<div class="ab" data-s="1" style="{ab(lx, ly, 200)}font-size:20px;color:var(--navy)">{lab}</div>')

    sig = ['<div style="font-size:22px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.1;margin-bottom:8px">'
           'Сигналы<br>неисправности</div>',
           '<div class="card solid" style="padding:4px 10px;display:flex;gap:12px;align-items:center;margin-bottom:6px;border-radius:16px">'
           + big_ico(xi(SPK, ""), 52, 14) +
           '<div style="font-size:17px;line-height:1.12"><b>Звуковые</b> — комбинации коротких и длинных сигналов</div></div>',
           '<div class="card solid" style="padding:4px 10px;display:flex;gap:12px;align-items:center;margin-bottom:6px;border-radius:16px">'
           + big_ico(ico("mon"), 52, 14) +
           '<div style="font-size:17px;line-height:1.12"><b>Текстовые</b> — описание или код ошибки</div></div>',
           f'<div class="card rose" style="padding:6px 10px;display:flex;gap:10px;align-items:center;font-size:16px;'
           f'line-height:1.25;color:{RED};font-weight:600;border-radius:16px"><span style="display:grid;place-items:center;flex:none;width:34px;height:34px;'
           f'border-radius:50%;background:{RED};color:#fff;font-size:20px;font-weight:800">!</span><div>Ошибка компонента{AR}сигнал неисправности '
           f'и остановка соответствующего этапа.</div></div>']
    o.append(kcard(878, 122, 440, 312, 2, "card", "".join(sig), "padding:10px 14px"))
    o.append(img("dev/mes2424.webp", 1336, 150, 570, 260, 2, cls="ab", extra="object-fit:contain"))

    stages = [
        (34, 432, "01", "ROM BOOTLOADER", "Загрузчик ПЗУ", "p067_rom.jpg", 128, 64,
         ["Запуск устройства", "Инициализация аппаратных регистров", "Выбор источника: NOR Flash • SD/MMC • PCI Express",
          "Вычисление и сравнение хеша открытого ключа", f"Хеш совпал{AR}запуск Booton"],
         f"Хеш не совпал{AR}<span style=\"color:{RED}\">остановка загрузки</span>"),
        (471, 452, "02", "BOOTON", "Первичный загрузчик", "p067_booton.jpg", 138, 74,
         ["Запуск Booton", "Инициализация CPU, UART и DRAM", "Запуск защитного таймера",
          "Чтение параметров и выбор источника", "Копирование образа U-Boot в DRAM", "Проверка подлинности U-Boot",
          f"Проверка пройдена{AR}запуск U-Boot"],
         f"Ошибка проверки{AR}<span style=\"color:{RED}\">остановка загрузки</span>"),
        (928, 520, "03", "U-BOOT", "Универсальный загрузчик", "p067_uboot.jpg", 138, 75,
         ["Запуск U-Boot", "Проверка заголовка, ключа, цифровой подписи и хеша", "Минимальная инициализация аппаратного окружения",
          "Инициализация NOR Flash и сетевых интерфейсов", "Выбор активного раздела eMMC / NAND",
          "Проверка подлинности раздела", f"Проверка пройдена{AR}запуск Firmware"],
         f"Ошибка проверки{AR}<span style=\"color:{RED}\">остановка загрузки</span>"),
        (1453, 432, "04", "FIRMWARE", "Файл прошивки", "p067_fw.jpg", 95, 88,
         ["Запуск Firmware", "Проверка подлинности: CRC", "Распаковка образа Firmware",
          "Полная инициализация аппаратного окружения", "Проверка остальных компонентов", "Загрузка рабочей конфигурации"],
         None)]
    for i, (l, w, n, name, sub, chip, cw, ch, bl, err) in enumerate(stages):
        s = 3 + i
        head = (f'<div class="ab" style="left:20px;top:18px;display:flex;gap:16px;align-items:center">'
                f'<span style="display:grid;place-items:center;width:62px;height:62px;border-radius:50%;'
                f'background:linear-gradient(160deg,#4a86ff,#1f55d6);color:#fff;font-size:30px;font-weight:800;'
                f'box-shadow:0 6px 16px rgba(42,107,242,.35)">{n}</span>'
                f'<div><div style="font-size:25px;font-weight:800;color:var(--navy)">{name}</div>'
                f'<div style="font-size:21px;color:var(--blue)">{sub}</div></div></div>')
        pic = chipimg(chip, 40 + (110 - cw * .8) / 2, 84, cw * .8, ch * .8)
        body = f'<div class="ab" style="{ab(18, 150, w - 30)}">{bullets(bl, 21, 2, 1.13)}'
        if err:
            body += (f'<div style="margin-top:8px;border-radius:12px;background:rgba(253,226,234,.9);'
                     f'padding:5px 10px;display:flex;gap:10px;align-items:center;font-size:21px;font-weight:600;line-height:1.1;'
                     f'color:var(--navy)"><span style="display:grid;place-items:center;flex:none;width:24px;height:24px;'
                     f'border-radius:50%;background:{RED};color:#fff;font-size:16px;font-weight:800">!</span><div>{err}</div></div>')
        else:
            body += (f'<div style="margin-top:10px;border-radius:14px;background:rgba(210,244,226,.95);'
                     f'padding:10px 16px;display:flex;gap:14px;align-items:center;font-size:23px;font-weight:800;'
                     f'color:#12805a;line-height:1.15;border:1.5px solid rgba(60,190,140,.45)">'
                     f'<span style="display:grid;place-items:center;flex:none;width:42px;height:42px;border-radius:50%;'
                     f'background:#22b27a;color:#fff"><svg viewBox="0 0 24 24" style="width:26px;height:26px" fill="none" '
                     f'stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg></span>'
                     f'<div>КОММУТАТОР<br>ГОТОВ К РАБОТЕ</div></div>')
        body += '</div>'
        o.append(kcard(l, 446, w, 478, s, "card", head + pic + body, "padding:0"))
    for i, (ax, lc, st_) in enumerate([(430, 466 - 110, 4), (888, 923 - 110, 5), (1415, 1448 - 110, 6)]):
        o.append(f'<div class="ab" data-s="{st_}" style="{ab(lc - 142, 528, 250)}text-align:right;font-size:15px;white-space:nowrap;'
                 f'line-height:1.0;color:var(--navy);font-weight:600">Успешная проверка{AR}<br>следующий этап</div>')
        o.append(f'<svg class="ab" data-s="{st_}" style="{ab(ax + 4, 570, 52, 30)}overflow:visible" viewBox="0 0 110 72" preserveAspectRatio="none">'
                 f'<defs><linearGradient id="bg{i}" x1="0" x2="1"><stop offset="0" stop-color="#9cc3ff"/><stop offset="1" stop-color="#2a6bf2"/></linearGradient></defs>'
                 f'<path d="M0 18h62V0l48 36-48 36V54H0z" fill="url(#bg{i})"/></svg>')

    flow = [("p067_rom.jpg", 521, 110, 56, "ROM", "(BOOTLOADER)"), ("p067_booton.jpg", 793, 112, 60, "Booton", "(ПЕРВИЧНЫЙ ЗАГРУЗЧИК)"),
            ("p067_uboot.jpg", 1097, 112, 60, "U-Boot", "(УНИВЕРСАЛЬНЫЙ ЗАГРУЗЧИК)"),
            ("p067_fw.jpg", 1385, 58, 54, "Firmware", "(ФАЙЛ ПРОШИВКИ)"), ("p067_cfg.jpg", 1691, 56, 54, "Конфигурация", "")]
    bar = hd("Общая схема загрузки", 26, "var(--navy)", "position:absolute;left:30px;top:26px;width:300px")
    L0, T0 = 34, 934                       # координаты карточки: содержимое считаем от неё
    inner = [bar]
    for im, cxx, w, h, lab, sub in flow:
        inner.append(chipimg(im, cxx - w * .4 - L0, 6, w * .8, h * .8))
        inner.append(f'<div class="ab" style="{ab(cxx - 160 - L0, 62, 320)}text-align:center;line-height:1.05">'
                     f'<div style="font-size:20px;font-weight:800;color:var(--navy)">{lab}</div>'
                     f'<div style="font-size:14px;color:var(--navy);white-space:nowrap;letter-spacing:-.3px">{sub}</div></div>')
    inner.append('<svg class="ab" style="left:0;top:0;width:1778px;height:150px;overflow:visible" '
                 'viewBox="0 0 1778 150">'
                 + "".join(arrow_svg(x - L0, 39, x - L0 + 60, 39, None, w=5) for x in (636, 934, 1240, 1518))
                 + '</svg>')
    o.append(kcard(L0, T0, 1852, 140, 7, "card", "".join(inner), "padding:0"))
    return "".join(o)


SLIDES.append(("p067", "POST и процесс загрузки коммутатора", post_boot()))


# ======================================================= p068 ESR-3300 задняя панель
def esr3300():
    o = ['<div class="ab" style="left:68px;top:20px;font-size:112px;font-weight:800;color:var(--navy);line-height:1;'
         'letter-spacing:-1px">ESR-3300</div>',
         '<div class="ab" style="left:72px;top:134px;font-size:32px;color:#3a4a80;letter-spacing:1px">ЗАДНЯЯ ПАНЕЛЬ</div>',
         img("p068_device.jpg", 75, 446, 1765, 267)]

    def card(l, t, w, h, n, ttl, body, s):
        head = (f'<div style="display:flex;gap:18px;align-items:center;margin-bottom:12px">'
                f'<span class="badge" style="width:52px;height:52px;font-size:30px;border-radius:13px">{n}</span>'
                f'<div style="font-size:23px;font-weight:700;color:var(--navy)">{ttl}</div></div>')
        return kcard(l, t, w, h, s, "card solid", head + body, "padding:14px 22px;border-radius:16px")

    p = lambda t: f'<div style="font-size:18px;line-height:1.3;color:var(--ink)">{t}</div>'
    im = lambda n, w, h: (f'<img src="assets/{n}" style="width:{w}px;height:{h}px;object-fit:cover;border-radius:8px;'
                          f'mix-blend-mode:multiply;margin-top:8px;flex:none">')
    o.append(card(66, 199, 544, 238, 1, "Слоты для источников питания",
                  '<div style="display:flex;gap:22px;align-items:flex-start">' + im("p068_psu1.jpg", 96, 106)
                  + p("На старших моделях предусмотрено 2 слота для установки источников питания на переменный либо "
                      "постоянный ток. Использовать одновременно можно разные источники питания, замену можно "
                      "выполнять без отключения устройства.") + '</div>', 1))
    o.append(card(672, 199, 535, 238, 3, "Съемные вентиляторные модули",
                  '<div style="display:flex;gap:22px;align-items:flex-start">' + im("p068_fan.jpg", 104, 106)
                  + p("На старших моделях имеются зарезервированные вентиляторные блоки, обеспечивающие эффективное "
                      "охлаждение устройства и повышение надёжности работы. Вентиляторные модули поддерживают горячую замену.")
                  + '</div>', 3))
    o.append(card(1262, 199, 592, 238, 4, "Место для резервного источника питания",
                  '<div style="display:flex;gap:22px;align-items:flex-start">' + im("p068_psu4.jpg", 116, 106)
                  + '<div style="width:2px;align-self:stretch;background:var(--line)"></div>'
                  + p("Источники питания на старших моделях не входят в комплект поставки и приобретаются отдельно, "
                      "исходя из потребностей заказчика.") + '</div>', 4))
    o.append(card(192, 772, 490, 188, 2, "Клемма заземления",
                  '<div style="display:flex;gap:30px;align-items:center;margin-top:18px">'
                  + big_ico(ico("ground"), 104, 22, True)
                  + p("Используется для подключения маршрутизатора к контуру заземления.") + '</div>', 2))
    o.append(card(1001, 771, 748, 245, 5, "Особенности питания по моделям",
                  '<div style="display:flex;gap:22px;align-items:flex-start">'
                  '<img src="assets/p068_plug.jpg" style="width:80px;height:128px;object-fit:cover;mix-blend-mode:multiply;margin-top:6px;flex:none">'
                  '<div>' + bullets(["Для ESR-10 и ESR-15 – внешний источник питания 12 В.",
                                     "Модели ESR-12, ESR-14 (с разными литерами), ESR-15R, ESR-20, ESR-21 имеют встроенный источник питания на 220 В (1 источник переменного тока).",
                                     "На старших моделях можно использовать одновременно разные источники питания, заменять их можно не отключая устройство."],
                                    17, 4, 1.25) + '</div></div>', 5))
    o.append(layer(
        gline("M199 439 L199 590", 1, [(199, 439), (199, 590)]),
        gline("M425 634 L425 752 L741 752 L741 874 L682 874", 2, [(425, 634)]),
        gline("M680 548 L680 498 L1234 498 L1234 548 M960 436 L960 498", 3, [(680, 548), (1234, 548), (960, 436)]),
        gline("M1721 436 L1721 590", 4, [(1721, 436), (1721, 590)]),
        gline("M1478 597 L1478 768", 5, [(1478, 597)])))
    return "".join(o)


SLIDES.append(("p068", "ESR-3300: задняя панель", esr3300()))


# ======================================================= p069 Контроллеры беспроводного доступа
def wlc():
    o = [faded("p069_bld2.jpg", 1050, 0, 870, 616, None, 9),
         '<h1 class="t ab left" style="left:75px;top:44px;width:1250px;font-size:72px;line-height:1.08;white-space:nowrap">'
         'Контроллеры<br>беспроводного доступа</h1>']
    o.append(img("dev/wlc-30.webp", 110, 390, 960, 170, 1, cls="ab", extra="object-fit:contain"))
    o.append(kcard(292, 246, 492, 146, 1, "card solid",
                   '<div style="text-align:center;font-size:62px;font-weight:800;color:var(--navy);line-height:1">WLC-30</div>'
                   '<div style="text-align:center;font-size:27px;color:var(--navy);margin-top:6px;text-transform:uppercase">'
                   'до <b style="font-size:36px;color:var(--blue)">150</b> точек доступа</div>',
                   "padding:12px 20px;border-radius:20px;background:rgba(255,255,255,.6)"))

    feats = [(60, 570, "p069_hgear.png", "Централизованное управление", "Настройка и мониторинг точек доступа"),
             (667, 576, "p069_hchart.png", "Контроль сети", "Статистика трафика и времени сессий"),
             (1276, 584, "p069_hshield.png", "Безопасный доступ", "WPA/WPA2 Enterprise и Personal")]
    for i, (l, w, icn, t, d) in enumerate(feats):
        inner = (faded(icn, 18, 6, 168, 176, None, 10, "mix-blend-mode:multiply")
                 + f'<div class="ab" style="left:196px;top:22px;width:2px;height:144px;background:var(--line)"></div>'
                 + f'<div class="ab" style="{ab(222, 0, w - 236, 188)}display:flex;flex-direction:column;justify-content:center">'
                 f'{hd(t, 27)}<p class="b" style="margin-top:8px;font-size:25px;line-height:1.2">{d}</p></div>')
        o.append(kcard(l, 606, w, 188, 2 + i, "card", inner, "padding:0"))

    o.append(kcard(32, 812, 922, 252, 5, "card",
                   img("dev/wlc-30.webp", 24, 90, 230, 60, cls="ab", extra="object-fit:contain")
                   + f'<div class="ab" style="{ab(272, 14, 640)}">'
                   '<div style="font-size:40px;font-weight:800;color:var(--navy);line-height:1.1">WLC-30</div>'
                   '<p class="b sm" style="font-size:21px;line-height:1.2;margin:2px 0 4px">Аппаратный контроллер для централизованного управления корпоративной сетью Wi-Fi малого и среднего бизнеса.</p>'
                   + bullets(["Подключение до 150 точек доступа", "Мониторинг оборудования и клиентов",
                              "Анализ трафика и времени сессий", "Индивидуальная настройка Wi-Fi"], 21, 0, 1.18) + '</div>',
                   "padding:0"))
    o.append(kcard(970, 812, 918, 252, 6, "card",
                   faded("p069_hcloud.png", 30, 14, 214, 222, None, 8, "mix-blend-mode:multiply")
                   + f'<div class="ab" style="{ab(282, 14, 620)}">'
                   '<div style="font-size:40px;font-weight:800;color:var(--navy);line-height:1.1">SoftWLC</div>'
                   '<p class="b sm" style="font-size:21px;line-height:1.2;margin:2px 0 4px">Программный комплекс для управления беспроводной сетью.</p>'
                   + bullets(["Единый интерфейс управления", "Организация HotSpot", "Авторизация пользователей",
                              "Поддержка корпоративных и операторских сетей", "Возможность построения гибридных схем"], 21, 0, 1.18)
                   + '</div>', "padding:0"))
    return "".join(o)


SLIDES.append(("p069", "Контроллеры беспроводного доступа", wlc()))


# ======================================================= p070 Базовые станции (устройства)
def bs_devices():
    T = TH
    o = [title("Базовые станции", 10, 80)]
    o.append(faded("p070_scene2.jpg", 440, 130, 1030, 590, 1, 6))

    def dev(l, t, w, h, s, im, iw, ih, ix, iy, name, sub, tx, tw):
        txt = (f'<div class="ab" style="{ab(tx, 0, tw)}top:50%;transform:translateY(-50%)">'
               f'<div style="font-size:30px;font-weight:700;color:var(--navy);line-height:1.15">{name}</div>'
               f'<div style="font-size:24px;color:var(--navy);margin-top:6px;line-height:1.2;text-transform:uppercase">{sub}</div>'
               f'<div style="width:{tw - 20}px;height:2px;background:var(--line);margin-top:14px"></div></div>')
        pic = (f'<img src="assets/{im}" class="ab" style="{ab(ix, iy, iw, ih)}object-fit:contain;mix-blend-mode:multiply">')
        return kcard(l, t, w, h, s, "card", pic + txt, "padding:0;background:rgba(255,255,255,.55)")

    o.append(dev(17, 60, 456, 346, 2, "p070_wop3ax2.png", 168, 292, 28, 28, "WOP-3ax-LR5", "Базовая станция", 230, 200))
    o.append(dev(1446, 60, 448, 346, 3, "dev/wop-2ac-lr5.webp", 170, 300, 26, 24, "WOP-2ac-LR5<br>SYNC", "Базовая станция", 220, 210))
    o.append(dev(17, 427, 420, 267, 4, "p070_wb2plr22.png", 180, 200, 22, 32, "WB-2P-LR2", "Абонентская станция", 230, 170))
    o.append(dev(1483, 427, 411, 267, 5, "dev/wb-2p-lr5.webp", 186, 200, 20, 32, "WB-2P-LR5", "Абонентская станция", 218, 170))

    feats = [("Дальняя связь", "Беспроводные каналы между удалёнными объектами", "p070_h1.png"),
             ("MIMO / MU-MIMO", "Одновременная передача данных", "p070_h2.png"),
             ("Безопасность", "WPA2/WPA3 и RADIUS", "p070_h3.png"),
             ("PoE", "Питание по Ethernet-кабелю", "p070_h4.png"),
             ("Всепогодное исполнение", "от −45 до +60 °C", "p070_h5.png")]
    xs = [(20, 190), (200, 362), (368, 530), (536, 697), (704, 880)]
    for (x0, x1), (t, d, ic) in zip(xs, feats):
        inner = (f'<div style="display:flex;gap:14px;align-items:center;height:100%"><img src="assets/{ic}" style="width:92px;height:100px;flex:none;mix-blend-mode:multiply"><div>'
                 f'<div style="font-size:18px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.15">{t}</div>'
                 f'<div style="font-size:16px;color:var(--ink);margin-top:5px;line-height:1.25">{d}</div></div></div>')
        o.append(kcard(x0 * T, 729, (x1 - x0) * T, 152, 6, "card", inner, "padding:12px 14px;border-radius:18px"))

    o.append(kcard(26, 896, 593, 160, 7, "card",
                   '<img src="assets/p070_tower2.jpg" class="ab" style="left:12px;top:10px;width:240px;height:140px;object-fit:cover;mix-blend-mode:multiply">'
                   '<div class="ab" style="left:262px;top:30px;width:320px"><div style="font-size:34px;font-weight:800;color:var(--navy)">2,4 ГГц</div>'
                   '<div style="font-size:21px;color:var(--navy);margin-top:6px">больше дальность, больше помех</div></div>', "padding:0"))
    o.append(kcard(631, 896, 638, 160, 7, "card",
                   '<img src="assets/p070_city2.jpg" class="ab" style="left:20px;top:14px;width:240px;height:132px;object-fit:cover;mix-blend-mode:multiply">'
                   '<div class="ab" style="left:280px;top:34px;width:340px"><div style="font-size:34px;font-weight:800;color:var(--navy)">5 и 6 ГГц</div>'
                   '<div style="font-size:21px;color:var(--navy);margin-top:6px">выше скорость, нужна прямая видимость</div></div>', "padding:0"))
    chips = "".join(f'<span class="chip" style="font-family:var(--f);font-size:19px;font-weight:500;padding:8px 14px;border-radius:10px">{c}</span>'
                    for c in ["Wi-Fi 4 / 5 / 6 / 6E", "TDD", "ECCM", "AP / клиент"])
    o.append(kcard(1286, 896, 598, 160, 7, "card",
                   f'<div style="display:flex;gap:14px;align-items:center;margin-bottom:18px">{ico("gear", "sm")}'
                   f'{hd("Ключевые характеристики", 21)}</div><div style="display:flex;gap:10px;flex-wrap:wrap">{chips}</div>',
                   "padding:18px 22px"))
    return "".join(o)


SLIDES.append(("p070", "Базовые станции: устройства", bs_devices()))


# ======================================================= p071 Базовые станции (сценарии)
def bs_map():
    T = TH
    o = ['<div class="ab" style="left:64px;top:64px;font-size:88px;font-weight:800;line-height:1.02;color:var(--navy);'
         'letter-spacing:-.5px">БАЗОВЫЕ<br><span style="color:#6b7db0">СТАНЦИИ</span></div>']
    o.append(img("p071_A.jpg", 0.28 * 1920, 0, 0.515 * 1920, 0.79 * 1080, 1, cls="ab"))
    o.append(img("p071_B.jpg", 0.03 * 1920, 0.27 * 1080, 0.25 * 1920, 0.52 * 1080, 1, cls="ab"))
    o.append(img("p071_C.jpg", 0.795 * 1920, 0.36 * 1080, 0.135 * 1920, 0.43 * 1080, 1, cls="ab"))
    leg = ('<img src="assets/p071_leg1.jpg" class="ab" style="left:36px;top:16px;width:92px;height:158px;object-fit:cover;mix-blend-mode:multiply">'
           '<div class="ab" style="left:164px;top:62px;font-size:22px;font-weight:700;color:var(--navy)">WOP-2ac-LR5 SYNC</div>'
           '<img src="assets/p071_leg2.jpg" class="ab" style="left:42px;top:182px;width:85px;height:119px;object-fit:cover;mix-blend-mode:multiply">'
           '<div class="ab" style="left:164px;top:222px;font-size:24px;font-weight:700;color:var(--navy)">WB-2P-LR5</div>')
    o.append(kcard(1532, 64, 367, 318, 2, "card", leg, "padding:0"))
    cards = [(43, 576, "Широкая зона покрытия", "Надёжная беспроводная связь на больших расстояниях.", "p071_h1.png"),
             (646, 616, "Связь с удалёнными объектами", "Эффективное подключение отдалённых населённых пунктов, предприятий и инфраструктуры.", "p071_h2.png"),
             (1280, 597, "Единая синхронизация", "Согласованная работа всех базовых станций в единой сети.", "p071_h3.png")]
    for i, (l, w, t, d, ic) in enumerate(cards):
        inner = (f'<div style="display:flex;gap:24px;align-items:center;height:100%"><img src="assets/{ic}" style="width:110px;height:132px;flex:none;mix-blend-mode:multiply"><div>{hd(t, 22)}'
                 f'<p class="b" style="font-size:20px;line-height:1.35;margin-top:10px;color:var(--dim)">{d}</p></div></div>')
        o.append(kcard(l, 875, w, 181, 3 + i, "card", inner, "padding:16px 22px"))
    return "".join(o)


SLIDES.append(("p071", "Базовые станции: сценарии применения", bs_map()))


# ======================================================= p072 Файлы конфигурации ESR
def cfg_files():
    o = ['<h1 class="t ab ctr-x" style="top:28px;width:1800px;font-size:66px">Файлы конфигурации <span class="lt">ESR</span></h1>']

    def fcard(l, t, w, h, s, name, ncol, c1, c2, items, cmd, cw, gid):
        inner = (doc_svg(gid, c1, c2, 36, 40, 94, 122)
                 + f'<div class="ab" style="left:190px;top:26px;font-size:46px;font-weight:800;color:{ncol};line-height:1.1">{name}</div>'
                 + f'<div class="ab" style="left:190px;top:96px;width:{w - 200}px">{bullets(items, 20 if len(items) > 4 else 21, 8 if len(items) > 4 else 10, 1.2)}</div>'
                 + f'<div class="ab mono" style="left:190px;top:{h - 78}px;width:{cw}px;padding:12px 18px;border-radius:12px;white-space:nowrap;'
                   f'background:rgba(255,255,255,.88);border:1.5px solid var(--line);font-size:{23 if cw < 600 else 18}px;color:var(--navy)">{cmd}</div>')
        return kcard(l, t, w, h, s, "card", inner, "padding:0;border-radius:26px")

    o.append(fcard(32, 192, 796, 367, 1, "running-config", "var(--navy)", "#6f9cf0", "#3f66d6",
                   ["Текущая активная конфигурация", "Маршрутизатор работает по ней сейчас",
                    "Хранится в энергонезависимой памяти"], "esr# show running-config", 500, "gr1"))
    o.append(f'<div class="ab" data-s="2" style="{ab(836, 296, 230)}text-align:center;font-size:23px;line-height:1.2;'
             f'color:var(--navy);font-weight:600">Сравнить<br>изменения</div>')
    o.append(layer(f'<g data-s="2">{arrow_svg(868, 372, 1030, 372, None, w=3)}{arrow_svg(1030, 372, 868, 372, None, w=3)}</g>'))
    o.append(kcard(846, 400, 214, 108, 2, "card solid",
                   '<div class="mono" style="font-size:18px;line-height:1.5;color:var(--navy)">esr# show<br>configuration changes</div>',
                   "padding:14px 18px;border-radius:14px"))
    o.append(fcard(1092, 196, 790, 363, 2, "candidate-config", "#6a4fd0", "#9a82f0", "#6a4fd0",
                   ["Конфигурация-кандидат", "Сюда сначала попадают новые настройки", "До commit изменения не применяются",
                    '<span class="mono" style="font-size:19px">commit</span> — применить',
                    '<span class="mono" style="font-size:19px">commit + save</span> — сохранить в энергонезависимую память'],
                   "esr# show candidate-config", 520, "gr2"))
    o.append(fcard(32, 580, 900, 301, 3, "default-config", "var(--navy)", "#7fc0f5", "#3f97e0",
                   ["Пустая конфигурация", "Используется для сброса настроек"],
                   "esr# copy system:default-config system:candidate-config", 690, "gr3"))
    o.append(fcard(986, 580, 880, 301, 4, "factory-config", "var(--navy)", "#8aa4f0", "#5a4fd0",
                   ["Заводская конфигурация", "Используется для возврата заводских настроек",
                    "Например, перед передачей маршрутизатора на склад"],
                   "esr# copy system:factory-config system:candidate-config", 680, "gr4"))

    def pill(l, t, w, txt, bg, col):
        return (f'<div class="ab" data-s="5" style="{ab(l, t, w, 54)}border-radius:12px;background:{bg};border:1.5px solid var(--line);'
                f'display:grid;place-items:center;font-size:24px;font-weight:700;color:{col}">{txt}</div>')

    o.append(kcard(139, 911, 1637, 134, 5, "card", "", "padding:0;border-radius:22px"))
    row = [(210, 270, "Новые настройки", "rgba(255,255,255,.9)", "var(--navy)"),
           (570, 330, "candidate-config", "rgba(218,208,252,.95)", "#4b3aa8"),
           (1010, 230, "commit", "rgba(255,255,255,.9)", "var(--navy)"),
           (1320, 330, "running-config", "linear-gradient(90deg,#8fb3f5,#4f7fe6)", "#fff")]
    for l, w, t, g, c in row:
        o.append(pill(l, 928, w, t, g, c))
    arrs = "".join(f'<g data-s="5">{arrow_svg(x0, 955, x1, 955, None, w=3)}</g>'
                   for x0, x1 in [(492, 550), (922, 990), (1262, 1310)])
    o.append(layer(arrs))
    o.append(f'<div class="ab" data-s="6" style="{ab(497, 992, 975, 40)}border-radius:20px;background:rgba(255,255,255,.8);'
             f'border:1.5px solid var(--line);display:flex;gap:6px;justify-content:center;align-items:center;font-size:22px;color:var(--navy)">'
             f'<b>save</b>{AR}сохранение в энергонезависимую память</div>')
    return "".join(o)


SLIDES.append(("p072", "Файлы конфигурации ESR", cfg_files()))


# ======================================================= p073 Память маршрутизатора
def memory():
    X = lambda v: v * K
    Y = lambda v: v * KY
    o = [faded("p073_ram_hero.jpg", X(405), 0, X(300), Y(345), None, 5),
         f'<div class="ab" style="{ab(41, Y(78), 560)}font-size:49px;font-weight:800;line-height:1.08;letter-spacing:-.5px">'
         f'<span style="color:#1c2c63">ПАМЯТЬ</span><br><span style="color:#4a5fa0">МАРШРУТИЗАТОРА</span></div>',
         f'<div class="ab" style="{ab(41, Y(183), 520)}font-size:30px;line-height:1.3;color:#2a3a6e">Где хранятся данные<br>и что с ними происходит</div>',
         f'<div class="ab" style="{ab(41, Y(262), 400)}height:2px;background:var(--line)"></div>',
         f'<div class="ab" style="{ab(41, Y(288), 520)}font-size:17px;letter-spacing:3px;color:#5a6ca0">РАБОТА. ХРАНЕНИЕ. СТАБИЛЬНОСТЬ.</div>']
    ram = (f'<div class="ab" style="left:24px;top:12px;display:flex;gap:18px;align-items:center">{xi(CHIP)}{hd("Оперативная память (ОЗУ)", 28)}</div>'
           '<p class="b ab" style="left:28px;top:80px;width:520px;font-size:20px;line-height:1.2">ОЗУ — это энергозависимая память, в которой находятся данные, '
           'но только до момента отключения электропитания. При перезагрузке маршрутизатора содержимое ОЗУ теряется.</p>'
           '<p class="b ab" style="left:28px;top:182px;width:520px;font-size:20px;line-height:1.2">Физически ОЗУ — это модули памяти, вставляемые в слоты материнской платы.</p>')
    o.append(kcard(X(695), Y(22), 560, Y(323), 1, "card", ram, "padding:0;border-radius:24px"))
    for i, (nm, l) in enumerate([("DDR3", 722), ("DDR4", 922)]):
        o.append(kcard(X(l), Y(222), X(178), Y(108), 1, "card solid",
                       f'<div class="ab" style="left:0;right:0;top:8px;text-align:center;font-size:21px;font-weight:800;color:var(--navy)">{nm}</div>'
                       f'<img src="assets/p073_ddr{3 + i}.jpg" class="ab" style="left:10px;top:36px;width:{X(178) - 20:.0f}px;height:{Y(108) - 44:.0f}px;object-fit:cover;mix-blend-mode:multiply">',
                       "padding:0;border-radius:18px"))
    o.append(faded("p073_globe.jpg", X(1118), Y(20), X(282), Y(215), 1, 8))
    o.append(faded("p073_stack.jpg", X(1112), Y(190), X(150), Y(135), 1, 10))
    o.append(f'<div class="ab" data-s="1" style="{ab(X(1268), Y(236), 190)}font-size:19px;line-height:1.3;color:var(--navy)">Данные в ОЗУ существуют только пока устройство включено</div>')

    sub = [(25, 225, "doc", "Конфигурация кандидат (candidate-config)", "Файл, куда записываются, но ещё не применяются все вводимые настройки."),
           (238, 435, "layers", "Буфер обмена", "Временный файл, который сохраняет приходящие на интерфейс пакеты или перед их отправкой."),
           (447, 652, "net", "Таблица маршрутизации", "Хранит информацию о сетях и маршрутах к этим сетям. Используется для поиска оптимального маршрута."),
           (665, 875, "link", "Таблица ARP", "Содержит сопоставления IP-адресов с MAC-адресами (аналогично ARP-кэшу на ПК). Используется интерфейсами типа GigabitEthernet, TenGigabitEthernet и т.д.")]
    cell = ""
    for a, b, icn, t, d in sub:
        cell += (f'<div class="card solid ab" style="{ab(X(a - 10), Y(57), X(b - a), Y(172))}padding:12px 14px;border-radius:16px;background:rgba(255,255,255,.55)">'
                 f'<div style="display:flex;gap:10px;align-items:center;margin-bottom:8px">{ico(icn, "sm")}<div style="font-size:18px;font-weight:800;color:var(--navy);line-height:1.15">{t}</div></div>'
                 f'<div style="font-size:16px;line-height:1.22;color:var(--ink)">{d}</div></div>')
    o.append(kcard(14, Y(358), X(890), Y(240), 2, "card",
                   f'<div class="ab" style="left:24px;top:12px;display:flex;gap:18px;align-items:center">{xi(CHIP)}{hd("Что хранится в ОЗУ", 28)}</div>' + cell,
                   "padding:0;border-radius:24px"))
    cur = (f'<div class="ab" style="left:24px;top:12px;display:flex;gap:18px;align-items:center">{ico("doc", "sm")}{hd("Текущая конфигурация", 28)}</div>'
           f'<div class="card solid ab" style="left:{X(35):.0f}px;top:{Y(72):.0f}px;width:{X(445):.0f}px;height:{Y(150):.0f}px;border-radius:18px;background:rgba(255,255,255,.55)">'
           + doc_svg("gcur", "#6f9cf0", "#3f66d6", 22, 22, 84, 104) +
           '<div class="ab" style="left:130px;top:16px;width:300px"><div style="font-size:22px;font-weight:800;color:var(--navy)">running-config</div>'
           '<div style="font-size:18px;line-height:1.25;margin-top:4px">Файл в ПЗУ, в который записываются команды конфигурирования, по которым маршрутизатор работает в данный момент.</div></div>'
           f'<img src="assets/p073_srv.jpg" class="ab" style="right:6px;top:6px;width:120px;height:{Y(140):.0f}px;object-fit:cover;mix-blend-mode:multiply;opacity:.9"></div>')
    o.append(kcard(X(910), Y(358), X(488), Y(240), 3, "card", cur, "padding:0;border-radius:24px"))

    o.append(faded("p073_flash.jpg", 0, Y(735), X(175), Y(170), 4, 8))
    rom = (f'<div class="ab" style="left:24px;top:12px;display:flex;gap:16px;align-items:center">{ico("db", "sm")}{hd("Постоянная память (ПЗУ)", 28)}</div>'
           '<p class="b ab" style="left:28px;top:78px;width:680px;font-size:20px;line-height:1.2">ПЗУ — это энергонезависимая память, в которой находятся данные '
           '(инструкции по загрузке, POST, файлы конфигурации, файлы прошивки). Эти данные остаются на маршрутизаторе даже после отключения питания.</p>'
           '<p class="b ab" style="left:28px;top:172px;width:680px;font-size:20px;line-height:1.2">Физически — это встроенная плата памяти в материнскую плату маршрутизатора.</p>'
           f'<div class="card solid ab" style="left:{X(228 - 90):.0f}px;top:236px;width:{X(370):.0f}px;height:92px;border-radius:16px;padding:12px 18px;'
           f'display:flex;gap:14px;align-items:center">{ico("info", "sm")}<div style="font-size:19px;line-height:1.3">На маршрутизаторах серии ESR ПЗУ существует двух типов: '
           f'<b>SPI NOR Flash и NAND Flash (eMMC)</b>.</div></div>')
    o.append(kcard(X(90), Y(612), X(525), Y(293), 4, "card", rom, "padding:0;border-radius:24px"))
    spi = (f'<div class="ab" style="left:24px;top:14px;display:flex;gap:16px;align-items:center">{xi(CHIP)}{hd("SPI NOR FLASH", 26)}</div>'
           '<div class="ab" style="left:34px;top:70px;font-size:19px;font-weight:800;color:var(--navy)">Содержит:</div>'
           f'<div class="ab" style="left:34px;top:100px;width:460px">{bullets(["Загрузчик U-Boot и переменные окружения U-Boot", "Factory-параметры (S/N, MAC, HW rev.)", "Номер активного раздела (image-1 или image-2)", "Параметры инициализации DDR-памяти", "Логи критичных событий (/mnt/critlog)", "Boot-лицензия"], 16.5, 3, 1.18)}</div>'
           '<img src="assets/p073_spi.jpg" class="ab" style="right:12px;bottom:8px;width:176px;height:100px;object-fit:cover;mix-blend-mode:multiply">')
    o.append(kcard(X(628), Y(612), X(375), Y(293), 5, "card", spi, "padding:0;border-radius:24px"))
    nand = (f'<div class="ab" style="left:24px;top:14px;display:flex;gap:16px;align-items:center">{xi(CHIP)}{hd("NAND FLASH (eMMC)", 26)}</div>'
            '<div class="ab" style="left:34px;top:70px;font-size:19px;font-weight:800;color:var(--navy)">Содержит:</div>'
            f'<div class="ab" style="left:34px;top:100px;width:460px">{bullets(["Раздел с конфигурацией running-config (/mnt/config)", "Раздел с образом firmware (image-1/2)", "Раздел для хранения дополнительной информации (/mnt/data)"], 17, 6, 1.25)}</div>'
            '<img src="assets/p073_emmc.jpg" class="ab" style="right:18px;bottom:10px;width:199px;height:116px;object-fit:cover;mix-blend-mode:multiply">')
    o.append(kcard(X(1015), Y(612), X(378), Y(293), 6, "card", nand, "padding:0;border-radius:24px"))
    return "".join(o)


SLIDES.append(("p073", "Память маршрутизатора", memory()))


# ======================================================= p074 POST: самотестирование
# bump() при сборке поднимает мелкие кегли до 21px, поэтому слайд свёрстан
# сразу крупным шрифтом; этапы загрузки вынесены на отдельный слайд — в одну
# страницу четыре списка читаемым кеглем не помещались и текст уезжал за карточки
def chip(label, w=250, h=150):
    """Микросхема: корпус с ножками и подписью — вместо размытого кропа из pptx."""
    gid = "cg_" + label.replace("-", "")
    legs = "".join(f'<rect x="{34 + i * 26}" y="18" width="14" height="14" rx="3" fill="#aebbe4"/>'
                   f'<rect x="{34 + i * 26}" y="118" width="14" height="14" rx="3" fill="#aebbe4"/>' for i in range(7))
    legs += "".join(f'<rect x="12" y="{40 + i * 28}" width="14" height="14" rx="3" fill="#aebbe4"/>'
                    f'<rect x="224" y="{40 + i * 28}" width="14" height="14" rx="3" fill="#aebbe4"/>' for i in range(2))
    return (f'<svg viewBox="0 0 250 150" style="{ab(0, 0, w, h)}">'
            f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="#7f9bea"/><stop offset="1" stop-color="#36'
            f'4da6"/></linearGradient></defs>{legs}'
            f'<rect x="32" y="30" width="186" height="90" rx="12" fill="url(#{gid})"/>'
            f'<rect x="40" y="38" width="170" height="74" rx="8" fill="none" stroke="rgba(255,255,255,.45)" stroke-width="2"/>'
            f'<text x="125" y="84" text-anchor="middle" font-family="Oswald,sans-serif" font-weight="700" '
            f'font-size="30" fill="#fff" letter-spacing="1">{label}</text></svg>')


def fw_chip(w=250, h=150):
    """Пакет прошивки: слои образа и шестерня."""
    return (f'<svg viewBox="0 0 250 150" style="{ab(0, 0, w, h)}">'
            f'<defs><linearGradient id="fwg" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="#7f9bea"/><stop offset="1" stop-color="#364da6"/></linearGradient></defs>'
            f'<path d="M125 96l82 22-82 22-82-22z" fill="#aebbe4"/>'
            f'<path d="M125 62l82 22-82 22-82-22z" fill="url(#fwg)"/>'
            f'<g fill="none" stroke="#364da6" stroke-width="7" stroke-linecap="round">'
            f'<circle cx="125" cy="40" r="15"/>'
            f'<path d="M125 12v10M125 58v10M97 40h10M143 40h10M105 20l7 7M138 53l7 7M145 20l-7 7M112 53l-7 7"/></g></svg>')


def post_self():
    o = ['<div class="ab" style="left:52px;top:14px;font-size:140px;font-weight:800;line-height:1;letter-spacing:-2px;'
         'background:linear-gradient(90deg,#1c2c63,#4a62b0);-webkit-background-clip:text;background-clip:text;color:transparent">POST</div>',
         '<div class="ab" style="left:59px;top:168px;width:540px;font-size:36px;font-weight:700;line-height:1.18;color:#6a7fb8;'
         'text-transform:uppercase">Самотестирование<br>при включении</div>',
         '<p class="b ab" style="left:59px;top:272px;width:520px;font-size:26px;line-height:1.32">В любом электронном устройстве есть механизм '
         'самотестирования перед началом работы или при включении электропитания.</p>',
         '<p class="b ab" style="left:59px;top:434px;width:520px;font-size:26px;line-height:1.32">POST (Power On Self Test) — '
         'это механизм, который проверяет наличие всех компонентов, необходимых для нормальной работы устройства, и их работоспособность '
         'сразу при включении питания и перед началом работы.</p>']
    hexi = lambda inner, top: (f'<span class="ico hex ab" style="left:18px;top:{top}px;width:76px;height:76px">'
                               f'<svg viewBox="0 0 24 24">{inner}</svg></span>')
    mon = '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M9 21h6M12 17v4"/>'
    morse = ('<div class="ab" style="left:452px;top:48px;width:148px;height:74px;border-radius:14px;'
             'background:linear-gradient(180deg,#a9bdf0,#8fa6e6)">'
             '<svg viewBox="0 0 136 68" style="width:148px;height:74px"><path d="M10 34h6M22 34h2M30 30v8M36 24v20M42 30v8'
             'M50 34h8M64 28v12M70 34h4M80 22v24M86 34h6M98 30v8M104 34h4M114 34h12" stroke="#fff" stroke-width="3" '
             'stroke-linecap="round" fill="none"/></svg></div>')
    term = ('<div class="ab mono" style="left:352px;top:30px;width:248px;border-radius:12px;'
            'background:linear-gradient(180deg,#3a52b0,#26398a);color:#dfe8ff;font-size:21px;line-height:1.5;'
            'padding:14px;box-shadow:inset 0 0 0 2px rgba(255,255,255,.4)">POST ERROR<br>MEMORY NOT FOUND<br>CODE: 0x1A</div>')

    def row(top, icn, ttl, txt, side, h, tw=330):
        return (f'<div class="card solid ab" style="{ab(18, top, 616, h)}border-radius:18px;padding:0">'
                + faded(icn, 10, 36, 92, 104, None, 16, "mix-blend-mode:multiply") +
                f'<div class="ab" style="left:112px;top:18px;width:{tw}px;font-size:22px;line-height:1.28">'
                f'<b style="font-size:26px;color:var(--navy)">{ttl}</b><br>{txt}</div>' + side + '</div>')

    sig = (row(116, "p074_spk.png", "Звуковой",
               "По типу азбуки Морзе — каждая комбинация «точек» и «тире» обозначает конкретную неисправность.", morse, 190)
           + row(322, "p074_mon.png", "Текстовый", "С описанием или кодом неисправности.", term, 190, 228))
    o.append(kcard(620, 40, 652, 532, 1, "card",
                   '<div class="ab" style="left:28px;top:22px;width:580px;font-size:28px;font-weight:700;color:var(--navy);line-height:1.25">'
                   'При обнаружении неисправности POST подаёт сигнал:</div>' + sig, "padding:0;border-radius:24px"))

    o.append(img("dev/esr-200.webp", 1300, 120, 590, None, 1, cls="ab"))

    o.append(kcard(59, 700, 1213, 250, 2, "card",
                   '<div class="ab" style="left:28px;top:6px;font-size:90px;font-family:Georgia,serif;font-weight:800;color:#5f86e6;line-height:1">&#8220;</div>'
                   '<div class="ab" style="left:116px;top:36px;width:1060px;font-size:26px;line-height:1.4;color:var(--navy)">'
                   'Механизм POST присутствует во всех современных устройствах: персональных компьютерах, ноутбуках, '
                   'смартфонах, точках доступа, коммутаторах, маршрутизаторах и др. Это более сложный процесс, '
                   'интегрированный в систему загрузки устройства.</div>', "padding:0;border-radius:22px"))
    o.append(kcard(1310, 700, 560, 250, 3, "card",
                   f'<div style="display:flex;gap:18px;align-items:center;height:100%">{ico("warn", "sm")}'
                   '<div style="font-size:24px;line-height:1.35;color:var(--navy)">Различные модели маршрутизаторов ESR имеют свои особенности загрузки, '
                   'но общий принцип остаётся единым.</div></div>', "padding:16px 24px;border-radius:22px"))
    return "".join(o)


SLIDES.append(("p074", "POST: самотестирование при включении", post_self()))


# ======================================================= p074b этапы загрузки
def boot_stages():
    o = [title("Этапы загрузки устройства", 30, 58),
         f'<div class="ab" data-s="1" style="{ab(160, 112, 1600)}text-align:center;font-size:24px;line-height:1.32;color:var(--navy)">'
         f'На каждом этапе происходит инициализация, выбор или поиск и проверка хеша и подлинности. '
         f'Если все условия этапа удовлетворяются — происходит переход к следующему этапу.</div>']

    st = [("01", "ROM BOOTLOADER", "Загрузчик ПЗУ", "p074_rom.png", "power", "Запуск устройства",
           ["Инициализация аппаратных регистров.",
            "Чтение параметров загрузки и выбор источника загрузки (NOR flash, SD/MMC card, PCI Express).",
            "Вычисление и сравнение хеш-суммы открытого ключа с хешем в регистре.",
            "Если хеши не совпадают — остановка загрузки.",
            "Если совпадают — запуск Primary loader."]),
          ("02", "PRIMARY LOADER", "Первичный загрузчик", "p074_cpu.png", "gear", "Запуск Primary-loader",
           ["Инициализация CPU (процессор), UART (RS-232 или COM-порт), DRAM (память).",
            "Запуск таймера.",
            "Чтение параметров загрузки и выбор источников загрузки.",
            "Копирование образа U-boot в DRAM.",
            "Проверка подлинности образа U-boot.",
            "Если проверка не пройдена — остановка загрузки.",
            "Если пройдена — запуск U-boot."]),
          ("03", "U-BOOT", "Универсальный загрузчик", "p074_uboot.png", "gear", "Запуск U-boot",
           ["Проверка заголовка, ключа, цифровой подписи и значения хеш.",
            "Инициализация аппаратного окружения, NOR-flash и сетевых интерфейсов.",
            "Выбор активного раздела (eMMC / NAND).",
            "Проверка подлинности.",
            "Если проверка пройдена — запуск Firmware."]),
          ("04", "FIRMWARE", "Файл прошивки", "p074_fw.png", "play", "Запуск Firmware",
           ["Проверка подлинности (CRC).",
            "Распаковка образа Firmware.",
            "Загрузка готовой конфигурации.",
            "Запуск Firmware."])]
    icons = {"power": '<path d="M12 4v8M7.5 7a7 7 0 1 0 9 0"/>',
             "gear": '<circle cx="12" cy="12" r="3"/><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8'
                     'M16.6 16.6l1.8 1.8M18.4 5.6l-1.8 1.8M7.4 16.6l-1.8 1.8"/>',
             "play": '<circle cx="12" cy="12" r="9"/><path d="M10 8.5l5 3.5-5 3.5z" fill="currentColor"/>'}
    W, GAP, L0, TOP, H = 430, 46, 22, 196, 860
    for i, (n, nm, sb, pic, picn, pill, bl) in enumerate(st):
        l = L0 + i * (W + GAP)
        head = (f'<div class="ab" style="{ab(24, 18, W - 48)}display:flex;gap:16px;align-items:center">'
                f'<span style="font-size:58px;font-weight:800;color:#2d3d7c;line-height:1">{n}</span>'
                f'<div><div style="font-size:24px;font-weight:800;color:#33458a;line-height:1.1">{nm}</div>'
                f'<div style="font-size:22px;color:#4f6199">{sb}</div></div></div>')
        chp = faded(pic, (W - 230) / 2, 102, 230, 140, None, 14, "mix-blend-mode:multiply")
        pl = (f'<div class="ab card solid" style="{ab(20, 268, W - 40, 56)}border-radius:28px;padding:0;display:flex;gap:12px;'
              f'align-items:center;justify-content:center;font-size:22px;font-weight:700;color:var(--navy)">'
              f'<span style="color:var(--blue);display:inline-flex"><svg viewBox="0 0 24 24" style="width:28px;height:28px" fill="none" '
              f'stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">{icons[picn]}</svg></span>{pill}</div>')
        inner = (f'<div class="ab" style="{ab(16, 340, W - 32, H - 356)}border-radius:16px;background:rgba(255,255,255,.5)"></div>'
                 f'<div class="ab" style="{ab(30, 354, W - 56)}">{bullets(bl, 21, 9, 1.26)}</div>')
        o.append(kcard(l, TOP, W, H, 2 + i, "card", head + chp + pl + inner, "padding:0;border-radius:24px"))
        if i:
            o.append(layer(arrow_svg(l - GAP + 6, TOP + 170, l - 6, TOP + 170, 2 + i)))
    return "".join(o)


SLIDES.append(("p074b", "Этапы загрузки устройства", boot_stages()))
