# -*- coding: utf-8 -*-
"""Переделанные слайды: официальные фото Eltex, собственные SVG, крупный текст.

Модуль грузится последним и перекрывает одноимённые ref из других файлов.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, arrow_svg

SLIDES = []


def ab(l, t, w=None, extra=""):
    s = f"position:absolute;left:{l}px;top:{t}px;"
    if w: s += f"width:{w}px;"
    return s + extra


def dev(name, l, t, w, extra=""):
    """Фото устройства с мягкой подставкой-бликом, как в soft-3D стиле."""
    return (f'<span style="position:absolute;left:{l}px;top:{t}px;width:{w}px">'
            f'<span style="position:absolute;left:8%;right:8%;bottom:-6%;height:16%;border-radius:50%;'
            f'background:radial-gradient(ellipse at center,rgba(60,100,180,.22),transparent 70%);filter:blur(10px)"></span>'
            f'<img src="assets/dev/{name}" style="position:relative;display:block;width:100%;'
            f'filter:drop-shadow(0 18px 30px rgba(30,60,130,.18));{extra}"></span>')


def layer(*parts):
    return ('<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" '
            'viewBox="0 0 1920 1080">' + "".join(parts) + '</svg>')


# ======================================================= сетевые устройства (p066)
def devices():
    o = ['<h1 class="t ab" style="left:90px;top:40px;text-align:left;width:1200px">Сетевые устройства</h1>',
         '<div class="sub ab" style="left:94px;top:124px;text-align:left;font-size:24px">Основа современных сетей</div>']

    cards = [
        ("01", "Маршрутизатор", "ROUTER", "Сетевой уровень (3 уровень OSI)", "esr-3300.webp", 500,
         "Сетевое устройство, соединяющее сети и предназначенное для пересылки пакетов из одной сети в другую."),
        ("02", "Коммутатор", "SWITCH", "Канальный уровень (2 уровень OSI)", "mes1428.webp", 520,
         "Сетевое устройство, предназначенное для пересылки кадров в пределах одной сети. "
         "Коммутаторы локальных сетей работают на канальном уровне (2 уровень модели OSI)."),
        ("03", "Точка доступа", "WIRELESS ACCESS POINT", "Канальный уровень (2 уровень OSI)", "wep-3ax.webp", 300,
         "Сетевое устройство, которое представляет из себя базовую станцию для создания беспроводной локальной сети, "
         "работающей поверх проводной сети или параллельно с ней."),
    ]
    for i, (n, title, en, osi, img, iw, text) in enumerate(cards):
        l = 90 + i * 590
        o.append(f'<div class="card" data-s="{i + 1}" style="{ab(l, 200, 550)}height:620px;padding:30px 34px">'
                 f'<div style="display:flex;align-items:center;gap:16px">'
                 f'<span class="mono" style="background:var(--navy);color:#fff;border-radius:10px;padding:6px 16px;'
                 f'font-size:26px;font-weight:700">{n}</span>'
                 f'<span class="mono" style="color:var(--dim);font-size:19px;letter-spacing:3px">{en}</span></div>'
                 f'<div style="margin-top:18px;font-size:38px;font-weight:700;color:var(--navy);'
                 f'font-family:var(--fh);text-transform:uppercase;line-height:1">{title}</div>'
                 f'<div class="chip" style="margin-top:14px;font-family:var(--f);font-size:19px;font-weight:600;'
                 f'color:var(--navy)">{osi}</div>'
                 f'<div style="position:relative;height:210px;margin-top:10px">{dev(img, (550 - 68 - iw) // 2, 18, iw)}</div>'
                 f'<p class="b" style="font-size:22px;line-height:1.45">{text}</p>'
                 f'</div>')

    o.append(f'<div class="card" data-s="4" style="{ab(90, 850, 1740)}height:190px;padding:28px 36px">'
             '<div class="ab" style="left:36px;top:30px;width:330px">'
             '<div style="font-size:36px;font-weight:700;color:var(--navy);font-family:var(--fh);'
             'text-transform:uppercase;line-height:1.05">Настройка<br>и доступ</div></div>'
             '<p class="b ab" style="left:400px;top:34px;width:720px;font-size:21px">'
             'Чтобы компьютерная сеть функционировала, мало собрать и подключить сетевые устройства через кабели '
             'и подключить к интернет-провайдеру: на каждом сетевом устройстве необходимо выполнить определённую '
             'настройку. Чтобы выполнить настройку, нужно получить доступ к сетевому устройству.</p>'
             + "".join(f'<div class="ab" style="left:{1192 + i * 196}px;top:40px;width:184px;text-align:center">'
                       f'<div style="display:flex;justify-content:center">{ico(icn, "sm")}</div>'
                       f'<div style="margin-top:10px;font-size:19px;font-weight:600;color:var(--navy);line-height:1.25">{t}</div></div>'
                       for i, (icn, t) in enumerate([("gear", "Настройка параметров"), ("mon", "Доступ к устройству"),
                                                     ("globe", "Стабильная работа сети")]))
             + '</div>')
    return "".join(o)


SLIDES.append(("p066", "Сетевые устройства", devices()))


# ======================================================= доступ к устройству (p056)
def access():
    """Доступ к устройству: выноски указывают на реальные разъёмы ESR-30."""
    # фото esr-30.webp: консольный разъём на 38.5% ширины / 90% высоты,
    # блок медных портов — на 71% / 84%; отсюда координаты выносок
    DX, DY, DW = 980, 70, 820
    DH = DW * 506 / 1100
    con_x, con_y = DX + 0.385 * DW, DY + 0.90 * DH
    eth_x, eth_y = DX + 0.7125 * DW, DY + 0.84 * DH

    o = ['<div class="ab" style="left:90px;top:56px;width:770px">'
         '<div class="big" style="font-size:76px;line-height:1.02">Доступ<br>к сетевому<br>устройству</div>'
         '<p class="b" style="margin-top:26px;font-size:25px;line-height:1.45">Для доступа к сетевому устройству '
         'есть несколько способов подключения: по консольному порту с помощью консольного кабеля '
         'и через протоколы удалённого доступа Telnet или SSH.</p></div>',
         dev("esr-30.webp", DX, DY, DW)]

    # два типа доступа — коротко, слева под лидом
    for k, (ttl, txt) in enumerate([
            ("Внеполосный доступ (out-of-band)",
             "Отдельный выделенный канал только для администрирования и обслуживания устройства."),
            ("Внутриполосный доступ (in-band)",
             "Общий канал передачи данных; нужен настроенный IP-адрес на интерфейсе."),
    ]):
        o.append(f'<div class="card ab" data-s="{5 + k}" style="left:90px;top:{476 + k * 140}px;width:770px;'
                 f'padding:20px 26px">'
                 f'<div style="font-size:24px;font-weight:700;color:var(--navy)">{ttl}</div>'
                 f'<p class="b" style="font-size:21px;line-height:1.4;margin-top:6px">{txt}</p></div>')

    # выноски: точка на разъёме, линия вниз, подпись под устройством
    o.append(f'<div class="card ab" data-s="1" style="{ab(1120, 500, 300)}padding:14px 20px;text-align:center">'
             '<div style="font-size:22px;font-weight:700;color:var(--navy)">Консольный порт</div>'
             '<div class="mono" style="font-size:21px;color:var(--blue)">Console</div></div>')
    o.append(f'<div class="card ab" data-s="2" style="{ab(1470, 500, 340)}padding:14px 20px;text-align:center">'
             '<div style="font-size:22px;font-weight:700;color:var(--navy)">Порты для подключения</div>'
             '<div class="mono" style="font-size:21px;color:var(--blue)">Telnet / SSH</div></div>')
    o.append(layer(
        f'<g data-s="1"><circle class="hd" cx="{con_x:.0f}" cy="{con_y:.0f}" r="9" fill="none" '
        f'stroke="var(--blue)" stroke-width="3.5"/>'
        f'<path class="dr" pathLength="1" d="M{con_x:.0f} {con_y + 10:.0f} L{con_x:.0f} 474 L1270 474 L1270 500" '
        f'stroke="var(--blue)" stroke-width="3.5" fill="none"/></g>',
        f'<g data-s="2"><circle class="hd" cx="{eth_x:.0f}" cy="{eth_y:.0f}" r="9" fill="none" '
        f'stroke="var(--blue)" stroke-width="3.5"/>'
        f'<path class="dr" pathLength="1" d="M{eth_x:.0f} {eth_y + 10:.0f} L{eth_x:.0f} 474 L1640 474 L1640 500" '
        f'stroke="var(--blue)" stroke-width="3.5" fill="none"/></g>'))

    # --- 01 консоль: SVG разъёма RJ-45, кабеля и USB
    rj45 = ('<svg viewBox="0 0 320 150" style="width:300px;height:140px">'
            '<defs><linearGradient id="mt" x1="0" y1="0" x2="0" y2="1">'
            '<stop offset="0" stop-color="#fdfefe"/><stop offset="1" stop-color="#ddd6f4"/></linearGradient></defs>'
            '<rect x="12" y="26" width="120" height="96" rx="9" fill="url(#mt)" stroke="#9d93c6" stroke-width="2.5"/>'
            '<rect x="40" y="10" width="64" height="30" rx="7" fill="url(#mt)" stroke="#9d93c6" stroke-width="2.5"/>'
            '<g fill="#c3bbe2">' + "".join(f'<rect x="{46 + i * 11}" y="46" width="7" height="34" rx="2"/>' for i in range(8)) + '</g>'
            '<rect x="30" y="92" width="84" height="18" rx="5" fill="#f2effc" stroke="#aaa0d0" stroke-width="2"/>'
            '<path d="M132 74 C190 74 200 54 250 54" stroke="#a9a0d8" stroke-width="16" fill="none" stroke-linecap="round"/>'
            '<path d="M132 74 C190 74 200 54 250 54" stroke="#e4defa" stroke-width="9" fill="none" stroke-linecap="round"/>'
            '<rect x="246" y="34" width="62" height="40" rx="8" fill="url(#mt)" stroke="#9d93c6" stroke-width="2.5"/>'
            '<rect x="256" y="44" width="42" height="8" rx="3" fill="#c3bbe2"/>'
            '<text x="72" y="142" text-anchor="middle" font-size="20" fill="#6b7196">RJ-45</text>'
            '<text x="277" y="142" text-anchor="middle" font-size="20" fill="#6b7196">USB</text>'
            '</svg>')
    items1 = ["Консольный порт (Console) — это интерфейс управления устройством, использует внеполосный доступ.",
              "Позволяет выполнить первоначальное конфигурирование и может быть единственным способом доступа, "
              "когда доступ по протоколам удалённого подключения невозможен или запрещён.",
              "Консольное подключение не зависит от настроек на сетевом устройстве.",
              "Скорость подключения в программе эмуляции терминала — 115200 бит/с."]
    o.append(f'<div class="card" data-s="3" style="{ab(90, 800, 560)}min-height:560px;padding:30px 34px">'
             '<div style="display:flex;align-items:center;gap:18px">'
             '<span class="mono" style="font-size:46px;font-weight:700;color:#c6c0e8">01</span>'
             '<div style="font-size:32px;font-weight:700;color:var(--navy);font-family:var(--fh);'
             'text-transform:uppercase;line-height:1.05">Консольное<br>подключение</div></div>'
             f'<div style="display:flex;justify-content:center;margin:16px 0 10px">{rj45}</div>'
             + "".join(f'<p class="b" style="font-size:21px;line-height:1.45;margin-bottom:14px">{t}</p>' for t in items1)
             + '</div>')

    def term(cmd):
        return ('<div style="background:linear-gradient(168deg,#3b3566,#241f45);border-radius:18px;'
                'padding:18px 22px;box-shadow:var(--sh)">'
                f'<div class="mono" style="color:#f0ecff;font-size:21px">{cmd}</div>'
                '<div class="mono" style="color:#a9b9ff;font-size:21px;margin-top:6px">'
                '<span style="display:inline-block;width:11px;height:21px;background:#a9b9ff;'
                'vertical-align:-4px"></span></div></div>')

    cards = [
        ("02", "Telnet", "Удалённый незащищённый доступ", term("C:\\&gt; telnet 192.168.1.1"), "порт 23",
         ["Telnet — это протокол для установления удалённого незащищённого подключения к интерфейсу командной строки (CLI).",
          "Подключение по Telnet считается внутриполосным доступом (in-band) — через общий канал.",
          "Требует минимум одного настроенного IP-адреса и включения протокола на устройстве "
          "(<span class=\"mono\">ip telnet server</span>).",
          "Нестандартный номер порта задаётся командой <span class=\"mono\">ip telnet port</span>."]),
        ("03", "SSH", "Удалённый защищённый доступ", term("C:\\&gt; ssh admin@192.168.1.1"), "порт 22",
         ["SSH (Secure Shell) — это протокол для установления удалённого защищённого внутриполосного подключения "
          "к интерфейсу CLI сетевого устройства.",
          "Защищённое подключение возможно благодаря аутентификации на основе пароля и шифрованию данных, "
          "но это несёт дополнительную нагрузку на устройство и канал.",
          "Требует минимум одного настроенного IP-адреса и включения протокола на устройстве "
          "(<span class=\"mono\">ip ssh server</span>).",
          "Нестандартный номер порта задаётся командой <span class=\"mono\">ip ssh port</span>."]),
    ]
    for i, (n, name, sub, tm, port, items) in enumerate(cards):
        o.append(f'<div class="card" data-s="{4 + i}" style="{ab(690 + i * 590, 800, 560)}min-height:560px;'
                 f'padding:30px 34px">'
                 f'<div style="display:flex;align-items:center;gap:18px">'
                 f'<span class="mono" style="font-size:46px;font-weight:700;color:#c6c0e8">{n}</span>'
                 f'<div><div style="font-size:36px;font-weight:700;color:var(--navy);font-family:var(--fh);'
                 f'text-transform:uppercase;line-height:1">{name}</div>'
                 f'<div class="b" style="font-size:20px;color:var(--dim)">{sub}</div></div>'
                 f'<span class="chip mono" style="margin-left:auto;font-size:20px;padding:8px 16px">{port}</span></div>'
                 f'<div style="margin:18px 0 16px">{tm}</div>'
                 + "".join(f'<p class="b" style="font-size:21px;line-height:1.45;margin-bottom:14px">{t}</p>' for t in items)
                 + '</div>')
    return "".join(o)


SLIDES.append(("p056", "Доступ к сетевому устройству", access()))


# ======================================================= сервисные маршрутизаторы ESR (p051)
def esr_line():
    o = ['<div class="ab" style="left:90px;top:70px;width:760px">'
         '<div class="big" style="font-size:76px;line-height:1.02">Сервисные<br>'
         '<span class="lt" style="color:var(--blue)">маршрутизаторы</span><br>ESR</div>'
         '<p class="b" style="margin-top:22px;font-size:22px;color:var(--dim)">Надёжная основа современных сетей</p></div>',
         f'<div class="card ab" data-s="1" style="{ab(900, 90, 930)}padding:28px 34px">'
         '<p class="b" style="font-size:23px">Сервисные маршрутизаторы Элтекс (ESR) — это современные устройства, '
         'которые пересылают пакеты между элементами сети, основываясь на правилах или таблицах маршрутизации. '
         'Линейка ESR включает решения для сетей любого масштаба: от компактных устройств до высокопроизводительных '
         'маршрутизаторов операторского класса.</p></div>']

    models = [("ESR-15", "Компактное решение для небольших сетей", "esr-15.webp", 420,
               [("expand", "Компактный корпус"), ("gear", "Базовый набор интерфейсов"), ("chart", "Для небольших офисов и филиалов")]),
              ("ESR-30", "Оптимальный баланс функциональности", "esr-30.webp", 430,
               [("layers", "Расширенные возможности"), ("net", "Больше интерфейсов"), ("server", "Для корпоративных сегментов")]),
              ("ESR-1700", "Высокая производительность для крупных сетей", "esr-1700.webp", 310,
               [("speed", "Высокая производительность"), ("gear", "Многоядерный процессор"), ("globe", "Для операторов и крупных компаний")])]
    for i, (name, sub, img, iw, feats) in enumerate(models):
        l = 90 + i * 590
        o.append(f'<div class="card" data-s="{2 + i}" style="{ab(l, 400, 550)}padding:28px 32px 34px">'
                 f'<div style="font-size:40px;font-weight:700;color:var(--navy);font-family:var(--fh)">{name}</div>'
                 f'<p class="b" style="font-size:20px;color:var(--dim);margin-top:6px">{sub}</p>'
                 f'<div style="position:relative;height:240px;margin-top:14px">{dev(img, (550 - 64 - iw) // 2, 20, iw)}</div>'
                 + "".join(f'<div style="display:flex;gap:14px;align-items:center;margin-top:12px">{ico(icn, "sm")}'
                           f'<p class="b" style="font-size:19px">{t}</p></div>' for icn, t in feats)
                 + '</div>')

    feats = [("net", "Набор интерфейсов"), ("gear", "Центральный процессор"), ("chart", "Производительность")]
    o.append(f'<div class="card" data-s="5" style="{ab(90, 1060, 1740)}padding:32px 40px">'
             '<div style="display:flex;align-items:flex-start;gap:40px">'
             '<div style="width:320px;flex:none;font-size:32px;font-weight:700;color:var(--navy);'
             'font-family:var(--fh);text-transform:uppercase;line-height:1.1">Ключевые отличия моделей</div>'
             '<p class="b" style="flex:1;font-size:22px;line-height:1.45">Все устройства серии ESR имеют единый '
             'набор функциональных возможностей. Разница между моделями заключается в объёме трафика, '
             'который они могут обрабатывать.</p></div>'
             '<div style="display:flex;gap:40px;margin-top:26px">'
             + "".join(f'<div style="display:flex;gap:16px;align-items:center;flex:1">{ico(icn, "sm")}'
                       f'<div style="font-size:22px;font-weight:600;color:var(--navy);line-height:1.25">{t}</div></div>'
                       for icn, t in feats)
             + '</div></div>')

    return "".join(o)


SLIDES.append(("p051", "Сервисные маршрутизаторы ESR", esr_line()))


# ======================================================= панели устройств
def _ratio(name):
    """Реальная пропорция фото: высота / ширина. Без неё выноски уходят мимо."""
    from PIL import Image
    p = pathlib.Path(__file__).parent.parent / "_el2assets" / "dev" / name
    w, h = Image.open(p).size
    return h / w


def panel(name, kick, img, iw, img_top, callouts, note=None):
    """callouts: [(доля ширины фото, заголовок, текст, иконка)] — выноски вниз к карточкам."""
    il = (1920 - iw) // 2
    ib = img_top + round(iw * _ratio(img))
    o = [f'<div class="ab" style="left:90px;top:52px"><div class="big">{name}</div>'
         f'<div class="kick" style="margin-top:8px">{kick}</div></div>',
         dev(img, il, img_top, iw)]
    n = len(callouts)
    cw = min(520 if n <= 2 else 460, (1740 - (n - 1) * 40) // n)
    x0 = (1920 - (n * cw + (n - 1) * 40)) // 2      # ряд выносок по центру холста
    y = ib + 90                                      # карточки всегда ниже фотографии
    lines = []
    for i, (fx, title, text, icn) in enumerate(callouts):
        cx = x0 + i * (cw + 40) + cw // 2
        px = il + int(iw * fx)
        o.append(f'<div class="card" data-s="{i + 1}" style="{ab(x0 + i * (cw + 40), y, cw)}padding:22px 24px">'
                 f'<div style="display:flex;gap:14px;align-items:center">'
                 f'<span class="badge">{i + 1}</span>'
                 f'<div style="font-size:23px;font-weight:700;color:var(--navy);font-family:var(--fh);'
                 f'text-transform:uppercase;line-height:1.15">{title}</div></div>'
                 f'<div style="display:flex;gap:14px;align-items:flex-start;margin-top:14px">{ico(icn, "sm")}'
                 f'<p class="b" style="font-size:19px">{text}</p></div></div>')
        lines.append(f'<g data-s="{i + 1}">'
                     f'<circle class="hd" cx="{px}" cy="{ib - 14}" r="8" fill="none" stroke="var(--blue)" '
                     f'stroke-width="3"/>'
                     f'<path class="dr" pathLength="1" d="M{px} {ib - 4} L{px} {ib + 40} '
                     f'L{cx} {ib + 40} L{cx} {y}" stroke="var(--blue)" stroke-width="3.5" fill="none"/></g>')
    o.append(layer(*lines))
    if note:
        o.append(f'<div class="card" data-s="{n + 1}" style="{ab(90, y + 280, 1740)}padding:20px 28px;'
                 f'display:flex;gap:18px;align-items:center">{ico("info", "sm")}'
                 f'<p class="b" style="font-size:20px">{note}</p></div>')
    return "".join(o)


SLIDES.append(("p040", "ESR-200: передняя панель", panel(
    "ESR-200", "Передняя панель", "esr-200.webp", 1480, 200,
    [(0.10, "Комбо-порты", "Комбинированные порты: оптический SFP или медный RJ-45 на выбор.", "link"),
     (0.42, "Порты Gigabit Ethernet", "Медные порты RJ-45 для подключения устройств локальной сети.", "net"),
     (0.70, "Консольный порт", "Разъём RJ-45 для управления устройством по консольному кабелю.", "term"),
     (0.88, "Индикаторы", "Отражают текущее состояние устройства и его интерфейсов.", "sun")])))

SLIDES.append(("p005", "ESR-200: задняя панель", panel(
    "ESR-200", "Задняя панель", "esr-200-back.webp", 1480, 220,
    [(0.11, "Клемма заземления", "Используется для подключения маршрутизатора к контуру заземления.", "ground"),
     (0.60, "Вентиляционный модуль", "Обеспечивает эффективное охлаждение устройства и стабильную работу системы.", "fan")])))

SLIDES.append(("p038", "ESR-3300: передняя панель", panel(
    "ESR-3300", "Передняя панель", "esr-3300.webp", 1560, 210,
    [(0.31, "Порты 25GE", "Оптические порты SFP28 для высокоскоростных соединений.", "bolt"),
     (0.47, "Порты 40/100GE", "Порты QSFP для магистральных каналов и стыка с ядром сети.", "link"),
     (0.63, "USB, micro SD, Console", "Порт USB 3.0, слот для SD-карты и консольный порт, рядом — порт внеполосного управления OOB.", "sd"),
     (0.86, "Индикаторы", "Status, Alarm, VPN, Flash, Power, Master, Fan, RPS.", "sun")])))

SLIDES.append(("p068", "ESR-3300: задняя панель", panel(
    "ESR-3300", "Задняя панель", "esr-3300-back.webp", 1480, 220,
    [(0.12, "Клемма заземления", "Подключение корпуса устройства к контуру защитного заземления.", "ground"),
     (0.40, "Блоки питания", "Два слота для установки резервируемых блоков питания.", "power"),
     (0.78, "Вентиляторные блоки", "Зарезервированные вентиляторные модули с горячей заменой.", "fan")],
    note="Для ESR-10 и ESR-15 питание подаётся от внешнего источника 12 В. Модели ESR-12, ESR-14, ESR-15R, ESR-20 "
         "и ESR-21 имеют встроенный источник питания 220 В. На старших моделях — два слота для блоков питания.")))

SLIDES.append(("p079", "MES1428: передняя панель", panel(
    "MES1428", "Передняя панель", "mes1428.webp", 1560, 240,
    [(0.08, "Разъём питания", "Подключение кабеля питания переменного тока 220 В.", "power"),
     (0.30, "Консольный порт", "Разъём RJ-45 для управления коммутатором по консольному кабелю.", "term"),
     (0.60, "Порты Ethernet", "Медные порты RJ-45 для подключения абонентских устройств.", "net"),
     (0.88, "Комбо-порты SFP", "Оптические порты для подключения к вышестоящему коммутатору.", "link")])))

SLIDES.append(("p015", "MES1428: задняя панель", panel(
    "MES1428", "Задняя панель", "mes1428-back.webp", 1480, 240,
    [(0.25, "Вентиляционные отверстия", "Обеспечивают теплообмен и охлаждение компонентов.", "fan"),
     (0.88, "Клемма заземления", "Подключение корпуса устройства к контуру защитного заземления.", "ground")],
    note="На других моделях сзади располагаются разъём питания переменного тока, разъём аккумуляторной батареи "
         "и вентиляторные модули.")))


# ======================================================= подключение к устройству (p028)
def connect():
    def box(x, w, title, sub):
        return (f'<g><rect x="{x}" y="40" width="{w}" height="150" rx="18" fill="rgba(255,255,255,.88)" '
                f'stroke="#b9cde8" stroke-width="2"/>'
                f'<text x="{x + w / 2}" y="222" text-anchor="middle" font-family="var(--fh)" font-size="24" '
                f'font-weight="700" fill="#0f1f56">{title}</text>'
                f'<text x="{x + w / 2}" y="250" text-anchor="middle" font-family="var(--mono)" font-size="18" '
                f'fill="#5a6b96">{sub}</text></g>')

    def link(x1, x2, label, step):
        mx = (x1 + x2) / 2
        return (f'<g data-s="{step}"><path class="dr" pathLength="1" d="M{x1} 115 L{x2} 115" stroke="var(--blue)" '
                f'stroke-width="4" fill="none" stroke-linecap="round"/>'
                f'<polygon class="hd" points="{x2},115 {x2 - 16},107 {x2 - 16},123" fill="var(--blue)"/>'
                f'<text x="{mx}" y="98" text-anchor="middle" font-family="var(--mono)" font-size="19" '
                f'fill="var(--blue)">{label}</text></g>')

    # пиктограммы внутри блоков
    sw = ('<g transform="translate(60,62)"><rect width="150" height="46" rx="8" fill="#eef4ff" stroke="#8fa6c8" stroke-width="2"/>'
          + "".join(f'<rect x="{14 + i * 16}" y="14" width="11" height="18" rx="2" fill="#b9c8de"/>' for i in range(8))
          + '</g>')
    cable = ('<g transform="translate(330,66)"><rect x="0" y="12" width="44" height="26" rx="6" fill="#eef4ff" stroke="#8fa6c8" stroke-width="2"/>'
             '<path d="M44 25 C90 25 100 18 140 18" stroke="#9db6dc" stroke-width="12" fill="none" stroke-linecap="round"/>'
             '<path d="M44 25 C90 25 100 18 140 18" stroke="#dbe8fb" stroke-width="6" fill="none" stroke-linecap="round"/>'
             '<rect x="136" y="6" width="40" height="26" rx="6" fill="#eef4ff" stroke="#8fa6c8" stroke-width="2"/></g>')
    adapt = ('<g transform="translate(700,64)"><rect x="10" y="8" width="60" height="34" rx="8" fill="#eef4ff" stroke="#8fa6c8" stroke-width="2"/>'
             '<rect x="70" y="18" width="46" height="14" rx="4" fill="#dbe8fb" stroke="#8fa6c8" stroke-width="2"/></g>')
    laptop = ('<g transform="translate(1020,58)"><path d="M18 8 h128 v74 h-128 z" fill="#13224d" rx="6"/>'
              '<path d="M4 86 h156 l10 16 h-176 z" fill="#cfdcee" stroke="#8fa6c8" stroke-width="2"/>'
              '<text x="34" y="52" font-family="var(--mono)" font-size="22" fill="#7fb0ff">&gt;_</text></g>')

    chain = ('<svg class="ab" style="left:120px;top:195px;width:1680px;height:270px" viewBox="0 0 1300 265">'
             + box(40, 190, "Сетевое устройство", "Console") + sw
             + box(330, 230, "Консольный кабель", "RJ-45 — RS-232") + cable
             + box(680, 160, "Адаптер", "RS-232 — USB") + adapt
             + box(1000, 200, "Ноутбук", "эмулятор терминала") + laptop
             + link(232, 326, "RJ-45", 1) + link(562, 676, "DE-9", 2) + link(842, 996, "USB", 3)
             + '</svg>')

    o = ['<h1 class="t ab ctr-x" style="top:44px;width:1700px">Подключение к сетевому устройству</h1>',
         '<p class="b ab ctr-x" style="top:132px;width:1300px;text-align:center;font-size:23px;color:var(--dim)">'
         'Для доступа к оборудованию используют консольное подключение или удалённый доступ по протоколам Telnet и SSH</p>',
         chain]

    need1 = ["Консольный порт на коммутаторе или маршрутизаторе (разъём RJ-45)",
             "Консольный кабель: RJ-45 с одной стороны и RS-232 (DE-9) с другой",
             "Адаптер-переходник RS-232 — USB",
             "USB-интерфейс на ПК или ноутбуке администратора сети",
             "Программа эмуляции терминала: PuTTY, Tera Term, HyperTerminal, minicom"]
    need2 = ["Активный интерфейс с IP-адресом на коммутаторе или маршрутизаторе",
             "Кабель локальной сети: витая пара категории 7, разъём RJ-45",
             "Логин и пароль администратора устройства",
             "ПК или ноутбук администратора, подключённый к локальной сети",
             "Программа эмуляции терминала: PuTTY, HyperTerminal и так далее"]

    def card(l, n, title, sub, items, note, s):
        return (f'<div class="card" data-s="{s}" style="{ab(l, 480, 840)}height:470px;padding:30px 34px">'
                f'<div style="display:flex;align-items:center;gap:18px">'
                f'<span class="mono" style="font-size:44px;font-weight:700;color:#b9cdf0">{n}</span>'
                f'<div><div style="font-size:30px;font-weight:700;color:var(--navy);font-family:var(--fh);'
                f'text-transform:uppercase;line-height:1.05">{title}</div>'
                f'<div class="b" style="font-size:19px;color:var(--dim)">{sub}</div></div></div>'
                f'<div style="margin-top:18px">'
                + "".join(f'<div style="display:flex;gap:14px;align-items:flex-start;margin-bottom:12px">'
                          f'<span class="badge" style="width:34px;height:34px;border-radius:10px;font-size:19px">{i + 1}</span>'
                          f'<p class="b" style="font-size:20px">{t}</p></div>' for i, t in enumerate(items))
                + f'</div><div class="note" style="margin-top:6px;font-size:19px">{ico("info", "sm")}'
                  f'<p class="b" style="font-size:19px">{note}</p></div></div>')

    o.append(card(90, "01", "Консольное подключение", "Первоначальная настройка, внеполосный доступ", need1,
                  "В программе эмуляции терминала установите скорость 115200 бит/с.", 4))
    o.append(card(990, "02", "Удалённый доступ", "Telnet или SSH по сети, внутриполосный доступ", need2,
                  "IP-адрес интерфейса настраивается заранее, во время базовой настройки устройства.", 5))
    return "".join(o)


SLIDES.append(("p028", "Подключение к сетевому устройству", connect()))


# ======================================================= память маршрутизатора (p073)
def dimm(x, y, w, label):
    h = int(w * 0.26)
    chips = "".join(f'<rect x="{x + 16 + i * (w - 40) / 8}" y="{y + h * 0.26}" width="{(w - 40) / 8 - 8}" '
                    f'height="{h * 0.42}" rx="3" fill="#1b2b4e"/>' for i in range(8))
    pins = "".join(f'<rect x="{x + 14 + i * (w - 28) / 30}" y="{y + h - 9}" width="{(w - 28) / 30 - 2.5}" '
                   f'height="9" fill="#cfa43a"/>' for i in range(30))
    return (f'<g><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="#2f6f4e" stroke="#20523a" stroke-width="2"/>'
            f'{chips}{pins}'
            f'<text x="{x + w / 2}" y="{y + h + 32}" text-anchor="middle" font-family="var(--mono)" font-size="22" '
            f'font-weight="700" fill="#0f1f56">{label}</text></g>')


def chip(x, y, s, label):
    legs = "".join(f'<rect x="{x - 10}" y="{y + 12 + i * (s - 24) / 6}" width="10" height="7" fill="#9aa8bd"/>'
                   f'<rect x="{x + s}" y="{y + 12 + i * (s - 24) / 6}" width="10" height="7" fill="#9aa8bd"/>'
                   for i in range(6))
    return (f'<g>{legs}<rect x="{x}" y="{y}" width="{s}" height="{s}" rx="6" fill="#20283a" stroke="#141b2a" stroke-width="2"/>'
            f'<text x="{x + s / 2}" y="{y + s / 2 + 7}" text-anchor="middle" font-family="var(--mono)" font-size="17" '
            f'fill="#8fb4ff">{label}</text></g>')


def memory():
    o = ['<div class="ab" style="left:90px;top:56px;width:640px">'
         '<div class="big" style="font-size:72px;line-height:1.02">Память<br>маршрутизатора</div>'
         '<p class="b" style="margin-top:20px;font-size:23px;color:var(--dim)">Где хранятся данные '
         'и что с ними происходит при перезагрузке</p></div>']

    # ОЗУ
    o.append(f'<div class="card" data-s="1" style="{ab(760, 60, 1070)}height:430px;padding:30px 34px">'
             '<div class="ch">Оперативная память (ОЗУ)</div>'
             '<p class="b" style="font-size:21px">ОЗУ — это энергозависимая память, в которой находятся данные, '
             'но только до момента отключения электропитания. При перезагрузке маршрутизатора содержимое ОЗУ теряется. '
             'Физически ОЗУ — это модули памяти, вставляемые в слоты материнской платы.</p>'
             '<svg class="ab" style="left:40px;top:180px;width:620px;height:190px" viewBox="0 0 620 190">'
             + dimm(10, 20, 280, "DDR3") + dimm(320, 20, 280, "DDR4") + '</svg>'
             '<div class="card ab" style="left:700px;top:190px;width:330px;padding:20px 24px;background:rgba(234,242,255,.9)">'
             + ico("bolt", "sm") +
             '<p class="b" style="font-size:20px;margin-top:12px">Данные в ОЗУ существуют только пока устройство включено</p></div>'
             '</div>')

    # что хранится в ОЗУ
    items = [("doc", "Конфигурация кандидат", "candidate-config: файл, куда записываются, но ещё не применяются все вводимые настройки"),
             ("db", "Буфер обмена", "Временный файл, который сохраняет приходящие на интерфейс пакеты или перед их отправкой"),
             ("net", "Таблица маршрутизации", "Хранит информацию о сетях и маршрутах к ним, используется для поиска оптимального маршрута"),
             ("list", "Таблица ARP", "Содержит сопоставления IP-адресов с MAC-адресами, аналогично ARP-кэшу на ПК")]
    o.append(f'<div class="card" data-s="2" style="{ab(90, 520, 1070)}height:260px;padding:26px 30px">'
             '<div class="ch sm">Что хранится в ОЗУ</div>'
             + "".join(f'<div class="ab" style="left:{30 + i * 255}px;top:96px;width:235px">'
                       f'<div style="display:flex;gap:12px;align-items:center">{ico(icn, "sm")}'
                       f'<div style="font-size:19px;font-weight:700;color:var(--navy);line-height:1.2">{t}</div></div>'
                       f'<p class="b" style="font-size:18px;margin-top:10px">{d}</p></div>'
                       for i, (icn, t, d) in enumerate(items))
             + '</div>')

    # текущая конфигурация
    o.append(f'<div class="card" data-s="3" style="{ab(1200, 520, 630)}height:260px;padding:26px 30px">'
             '<div class="ch sm">Текущая конфигурация</div>'
             '<div class="mono" style="font-size:30px;font-weight:700;color:var(--blue)">running-config</div>'
             '<p class="b" style="font-size:20px;margin-top:12px">Файл в ПЗУ, в который записываются команды '
             'конфигурирования, по которым маршрутизатор работает в данный момент.</p></div>')

    # ПЗУ
    o.append(f'<div class="card" data-s="4" style="{ab(90, 810, 1070)}height:240px;padding:26px 30px">'
             '<div class="ch sm">Постоянная память (ПЗУ)</div>'
             '<p class="b" style="font-size:20px">ПЗУ — энергонезависимая память, в которой находятся инструкции '
             'по загрузке, POST, файлы конфигурации и файлы прошивки. Эти данные остаются на маршрутизаторе даже '
             'после отключения питания. Физически — встроенная плата памяти на материнской плате.</p>'
             '<div class="note" style="margin-top:16px">' + ico("info", "sm") +
             '<p class="b" style="font-size:19px">На маршрутизаторах серии ESR ПЗУ существует двух типов: '
             '<b class="mono">SPI NOR Flash</b> и <b class="mono">NAND Flash (eMMC)</b>.</p></div></div>')

    def flash(l, title, items, cid, s):
        return (f'<div class="card" data-s="{s}" style="{ab(l, 810, 320)}height:240px;padding:24px 26px">'
                f'<svg class="ab" style="left:214px;top:22px;width:90px;height:90px" viewBox="0 0 90 90">'
                + chip(14, 14, 62, cid) + '</svg>'
                f'<div style="font-size:23px;font-weight:700;color:var(--navy);font-family:var(--fh);'
                f'text-transform:uppercase">{title}</div>'
                + "".join(f'<p class="b" style="font-size:18px;margin-top:9px">{t}</p>' for t in items) + '</div>')

    o.append(flash(1200, "SPI NOR Flash", ["Загрузчик U-Boot и переменные окружения",
                                           "Factory-параметры: S/N, MAC, HW rev.",
                                           "Номер активного раздела и параметры DDR"], "NOR", 5))
    o.append(flash(1540, "NAND Flash (eMMC)", ["Раздел с конфигурацией running-config",
                                               "Раздел с образом firmware (image-1/2)",
                                               "Раздел для дополнительных данных"], "eMMC", 6))
    return "".join(o)


SLIDES.append(("p073", "Память маршрутизатора", memory()))


# ======================================================= функционал ESR (p012)
def esr_functions():
    o = ['<h1 class="t ab ctr-x" style="top:34px;width:1800px;font-size:58px">'
         'Основной функционал маршрутизаторов ESR</h1>',
         '<p class="b ab ctr-x" style="top:112px;width:1200px;text-align:center;font-size:22px;color:var(--dim)">'
         'Возможности зависят от модели, версии ПО и установленных лицензий</p>']

    steps = [("globe", "eltex-co.ru"), ("doc", "Каталог, маршрутизаторы ESR"), ("router", "Выбрать нужную модель"),
             ("list", "Документы и файлы"), ("doc", "Руководство по эксплуатации или справочник команд CLI")]
    o.append(f'<div class="card" data-s="1" style="{ab(90, 180, 400)}height:540px;padding:26px 28px">'
             '<div class="ch sm">Где посмотреть функции модели</div>'
             + "".join(f'<div style="display:flex;gap:14px;align-items:center;margin-bottom:20px">'
                       f'<span class="badge" style="width:38px;height:38px;border-radius:11px;font-size:20px">{i + 1}</span>'
                       f'{ico(icn, "sm")}<p class="b" style="font-size:19px;flex:1">{t}</p></div>'
                       for i, (icn, t) in enumerate(steps)) + '</div>')

    groups = [("net", "Интерфейсы и VLAN", ["Сетевые интерфейсы", "VLAN"]),
              ("arrows", "Коммутация и маршрутизация", ["L2, LAG/LACP", "RIP, OSPF, IS-IS, BGP"]),
              ("lock", "Туннели и VPN", ["MPLS, GRE, DMVPN", "IPsec, OpenVPN", "WireGuard, PPTP, L2TP"]),
              ("gear", "Сетевые сервисы", ["NAT и DHCP", "QoS"]),
              ("shield", "Безопасность", ["ACL и Firewall", "IPS/IDS", "Защита от DoS/DDoS"]),
              ("chart", "Резервирование и мониторинг", ["VRRP, MultiWAN, кластер 1+1", "SNMP, Syslog, NetFlow", "Zabbix и SLA"])]
    o.append('<div class="ch sm ab" style="left:530px;top:184px">Основные группы функций</div>')
    for i, (icn, title, items) in enumerate(groups):
        l = 530 + (i % 3) * 310
        t = 236 + (i // 3) * 250
        o.append(f'<div class="card" data-s="{2 + i}" style="{ab(l, t, 290)}height:224px;padding:20px 22px;text-align:center">'
                 f'<div style="display:flex;justify-content:center">{ico(icn, "sm")}</div>'
                 f'<div style="margin-top:10px;font-size:19px;font-weight:700;color:var(--navy);'
                 f'text-transform:uppercase;line-height:1.2">{title}</div>'
                 + "".join(f'<p class="b" style="font-size:18px;color:var(--dim);margin-top:8px">{x}</p>' for x in items)
                 + '</div>')

    crit = [("speed", "Количество и скорость портов"), ("chart", "Производительность маршрутизации"),
            ("shield", "Производительность Firewall и VPN"), ("stack", "Поддерживаемые протоколы"),
            ("lock", "Безопасность"), ("reload", "Резервирование")]
    o.append('<div class="ch sm ab" style="left:1480px;top:184px">Ключевые критерии выбора</div>')
    # одна колонка: в две по 170px длинные названия не помещались
    for i, (icn, t) in enumerate(crit):
        o.append(f'<div class="card" data-s="{8 + i // 2}" style="{ab(1480, 236 + i * 88, 350)}'
                 f'min-height:76px;padding:8px 16px;display:flex;gap:16px;align-items:center;'
                 f'--dl:{(i % 2) * 80}ms">{ico(icn, "sm")}'
                 f'<div style="font-size:20px;font-weight:600;color:var(--navy);line-height:1.2">{t}</div></div>')

    # нижняя полоса: схема вместо вклеенной картинки
    nodes = [("globe", "Интернет / WAN", 140), ("shield", "Защита сети", 430), ("lock", "VPN-туннели", 700),
             ("arrows", "Маршрутизация и коммутация", 1080), ("mon", "Мониторинг и аналитика", 1460)]
    # svg по ширине карточки (1740), иначе уезжает за правый край холста
    scheme = ['<svg class="ab" style="left:0;top:0;width:1740px;height:260px" viewBox="0 0 1740 260">'
              '<path d="M200 150 H1540" stroke="#cdc8ee" stroke-width="5" stroke-linecap="round" fill="none"/>'
              '</svg>']
    o.append(f'<div class="card" data-s="11" style="{ab(90, 770, 1740)}height:270px;padding:0">'
             + "".join(scheme)
             + "".join(f'<div class="ab" style="left:{x - 90}px;top:{165 if i % 2 == 0 else 20}px;width:180px;'
                       f'text-align:center">'
                       f'<div style="display:flex;justify-content:center">{ico(icn, "sm")}</div>'
                       f'<div style="margin-top:8px;font-size:18px;font-weight:600;color:var(--navy);'
                       f'line-height:1.25">{t}</div></div>'
                       for i, (icn, t, x) in enumerate(nodes))
             + '</div>')
    return "".join(o)


SLIDES.append(("p012", "Основной функционал маршрутизаторов ESR", esr_functions()))
