# -*- coding: utf-8 -*-
"""Слайды по референсам p059-p066."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.parent))
from _el2_lib import ico, icon, arrow_svg
from PIL import Image

SLIDES = []
ASSETS = pathlib.Path(__file__).parent.parent / "_el2assets"
GREEN = "#2e9b57"
ORANGE = "#e8920c"
PURPLE = "#6a4fd0"


def ab(l, t, w=None, extra=""):
    s = f"position:absolute;left:{l}px;top:{t}px;"
    if w:
        s += f"width:{w}px;"
    return s + extra


def layer(*parts):
    return ('<svg class="ab" style="left:0;top:0;width:1920px;height:1080px;overflow:visible" '
            'viewBox="0 0 1920 1080">' + "".join(parts) + '</svg>')


def arr_inline(w=34, col="currentColor"):
    return (f'<svg width="{w}" height="16" viewBox="0 0 34 16" style="display:inline-block;vertical-align:middle;'
            f'margin:0 8px"><path d="M1 8H30M23 2L31 8L23 14" stroke="{col}" stroke-width="2.6" fill="none" '
            f'stroke-linecap="round" stroke-linejoin="round"/></svg>')


def pair(a, b, fs=22, col="var(--blue)"):
    return f'<span class="mono" style="font-size:{fs}px;color:var(--navy)">{a}{arr_inline(34, col)}{b}</span>'


def mi(name, size=38, glyph=24):
    s = icon(name).replace("<svg ", f'<svg style="width:{glyph}px;height:{glyph}px" ')
    return f'<span class="ico sm" style="width:{size}px;height:{size}px;border-radius:10px">{s}</span>'


def devfit(name, cx, top, maxw, maxh, s=None):
    """Официальный рендер на прозрачном фоне: вписать в бокс, мягкая тень."""
    w, h = Image.open(ASSETS / name).size
    k = min(maxw / w, maxh / h)
    W, H = round(w * k), round(h * k)
    st = f' data-s="{s}"' if s else ""
    # у снятых с производства моделей рендера нет — там кроп с выбеленным фоном,
    # его кладём через multiply, чтобы белое слилось с карточкой
    blend = "" if Image.open(ASSETS / name).mode in ("RGBA", "LA", "P") else "mix-blend-mode:multiply;"
    return (f'<img class="ab"{st} src="assets/{name}" '
            f'style="left:{round(cx - W / 2)}px;top:{round(top + (maxh - H) / 2)}px;width:{W}px;{blend}'
            f'filter:drop-shadow(0 10px 18px rgba(110,100,165,.22))">')


def fit(name, cx, top, maxw, maxh, s=None, cls="cut", extra="mix-blend-mode:multiply;"):
    """Картинка по центру cx, вписанная в maxw x maxh, верх = top."""
    w, h = Image.open(ASSETS / name).size
    k = min(maxw / w, maxh / h)
    W, H = round(w * k), round(h * k)
    st = f' data-s="{s}"' if s else ""
    return (f'<img class="{cls} ab"{st} src="assets/{name}" '
            f'style="left:{round(cx - W / 2)}px;top:{round(top + (maxh - H) / 2)}px;width:{W}px;{extra}">')


def sd(s):
    return f' data-s="{s}"' if s else ""


# ======================================================= p059 механизм конфигураций
def configs():
    o = ['<h1 class="t ab ctr-x" style="top:26px;width:1700px">Механизм работы с конфигурациями</h1>']

    def doc(l, t, w, h, icn, name, desc, s, big=True):
        nf = 30 if big else 25
        df = 20 if big else 18
        return (f'<div class="card"{sd(s)} style="{ab(l, t, w)}height:{h}px;text-align:center;padding:0">'
                f'<div class="ab" style="right:22px;top:20px">{ico(icn, "" if big else "sm")}</div>'
                f'<div class="ab" style="left:14px;right:14px;top:{118 if big else 78}px;font-size:{nf}px;font-weight:800;'
                f'color:var(--navy);line-height:1.12">{name}</div>'
                f'<div class="ab b dim" style="left:20px;right:20px;bottom:{26 if big else 18}px;font-size:{df}px;'
                f'line-height:1.3">{desc}</div></div>')

    o.append(doc(90, 125, 320, 310, "doc", "candidate-<br>configuration", "Новые, ещё не применённые настройки", 1))
    o.append(doc(815, 125, 320, 310, "gear", "running-<br>configuration", "Текущая рабочая конфигурация", 1))
    o.append(doc(1500, 125, 320, 310, "db", "restore-<br>configuration", "Резервная копия предыдущей конфигурации", 2))

    # шаг 1: running -> restore
    o.append(f'<div class="chip"{sd(2)} style="{ab(1160, 195, 300)}justify-content:center;font-size:21px">'
             f'<b style="color:var(--blue)">1.</b>{pair("running", "restore", 21)}</div>')
    o.append(f'<p class="b sm ab" data-s="2" style="{ab(1150, 300, 335)}text-align:center;font-size:20px">'
             f'Сохранение предыдущей рабочей конфигурации</p>')
    # шаг 2: commit
    o.append(f'<div class="cmd mono ab" data-s="3" style="left:520px;top:128px;font-size:42px;padding:10px 30px">'
             f'<span class="a">&gt;</span> commit</div>')
    o.append(f'<div class="chip"{sd(3)} style="{ab(440, 205, 380)}justify-content:center;font-size:21px">'
             f'<b style="color:var(--blue)">2.</b>{pair("candidate", "running", 21)}</div>')
    o.append(f'<p class="b sm ab" data-s="3" style="{ab(440, 300, 380)}text-align:center;font-size:20px">'
             f'Применение новых настроек</p>')
    o.append(f'<div class="card"{sd(3)} style="{ab(430, 332, 400)}height:128px;padding:10px 16px;display:flex;'
             f'gap:14px;align-items:center">{ico("clock", "sm")}<div>'
             f'<div style="font-size:17px;font-weight:800;color:var(--navy);text-transform:uppercase">Защитный интервал</div>'
             f'<div style="font-size:17px;color:var(--navy)">600 секунд по умолчанию</div>'
             f'<div style="font-size:15px;color:var(--dim)">Новые настройки уже работают</div></div></div>')

    # ветвление
    o.append(f'<div class="card"{sd(4)} style="{ab(50, 456, 1820)}height:280px"></div>')
    o.append(f'<div class="ab"{sd(4)} style="{ab(865, 512, 190)}height:190px;transform:rotate(45deg);background:rgba(255,255,255,.92);'
             f'box-shadow:0 14px 30px rgba(90,110,180,.22);border:1.5px solid rgba(160,185,240,.6);border-radius:30px"></div>')
    o.append(f'<div{sd(4)} style="{ab(845, 545, 230)}height:130px;display:flex;align-items:center;justify-content:center;'
             f'text-align:center;font-size:25px;font-weight:800;color:var(--navy);line-height:1.3;'
             f'flex-direction:column">'
             f'<div>Введена команда</div><div class="mono">confirm?</div></div>')
    o.append(layer(
        arrow_svg(972, 436, 972, 474, 4, w=5),
        arrow_svg(822, 607, 552, 607, 5, col=GREEN, w=5),
        arrow_svg(1098, 607, 1366, 607, 6, col=ORANGE, w=5)))
    o.append(f'<div class="card mint"{sd(5)} style="{ab(90, 510, 460)}height:200px;display:flex;gap:24px;align-items:center;'
             f'padding:20px 28px"><svg width="96" height="96" viewBox="0 0 96 96" style="flex:none">'
             f'<circle cx="48" cy="48" r="44" fill="#3aa965"/><path d="M26 49L42 65L71 32" stroke="#fff" stroke-width="9" '
             f'fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg><div>'
             f'<div style="font-size:26px;font-weight:800;color:var(--navy)">Изменения подтверждены</div>'
             f'<p class="b sm dim" style="margin-top:12px;font-size:21px">Автоматический RESTORE отменён</p></div></div>')
    o.append(f'<div class="ab" data-s="5" style="left:600px;top:580px;width:190px;height:54px;border-radius:30px;'
             f'background:linear-gradient(90deg,#3aa965,#2e8f56);color:#fff;font-size:23px;font-weight:800;'
             f'display:grid;place-items:center;font-family:var(--mono);box-shadow:0 8px 18px rgba(40,140,80,.3)">ДА — confirm</div>')
    o.append(f'<div class="ab" data-s="6" style="left:1140px;top:580px;width:150px;height:54px;border-radius:30px;'
             f'background:linear-gradient(90deg,#f6b53a,#ee9a1c);color:#fff;font-size:26px;font-weight:800;'
             f'display:grid;place-items:center;box-shadow:0 8px 18px rgba(230,150,30,.35)">НЕТ</div>')
    o.append(f'<div class="card cream"{sd(6)} style="{ab(1370, 468, 480)}height:276px;padding:18px 24px">'
             f'<div style="display:flex;gap:20px;align-items:center">{ico("clock", "sm")}<div>'
             f'<div style="font-size:30px;font-weight:800;color:var(--navy)">RESTORE</div>'
             f'<div style="margin-top:2px">{pair("restore", "running", 21, ORANGE)}</div></div></div>'
             f'<p class="b sm dim" style="margin:10px 0 0 76px;font-size:19px">Предыдущая конфигурация восстановлена</p>'
             f'<div class="note" style="margin-top:14px;padding:12px 16px;gap:14px;align-items:center">'
             f'{mi("warn", 40, 26)}<p class="b sm" style="font-size:18px;line-height:1.3">Команду '
             f'<b class="mono">restore</b> можно ввести вручную до окончания таймера</p></div></div>')
    o.append(layer(arrow_svg(412, 285, 808, 285, 3, w=9), arrow_svg(1140, 285, 1494, 285, 2, w=9)))

    # rollback
    o.append(f'<div class="card"{sd(7)} style="{ab(50, 748, 1160)}height:316px"></div>')
    o.append(doc(80, 762, 290, 288, "doc", "candidate-<br>configuration", "Новые, ещё не применённые настройки", 7, False))
    o.append(doc(890, 762, 290, 288, "gear", "running-<br>configuration", "Текущая рабочая конфигурация", 7, False))
    o.append(f'<div class="ab mono" data-s="7" style="left:500px;top:762px;font-size:36px;font-weight:800;color:#fff;'
             f'padding:8px 28px;border-radius:12px;background:linear-gradient(90deg,#5a47c4,#3c2f93)">'
             f'<span style="color:#b9b0ff">&gt;</span> rollback</div>')
    o.append(f'<div class="chip"{sd(7)} style="{ab(450, 826, 380)}justify-content:center;font-size:19px">'
             f'{pair("running", "candidate", 19, PURPLE)}</div>')
    o.append(f'<p class="b sm ab" data-s="7" style="{ab(385, 900, 480)}text-align:center;font-size:17px;line-height:1.3">'
             f'Удаляет неприменённые изменения из <span class="mono">candidate-configuration</span></p>')
    o.append(f'<div class="note"{sd(7)} style="{ab(400, 966, 470)}padding:8px 14px;align-items:center">'
             f'{mi("info", 34, 22)}<p class="b sm" style="font-size:16px">Рабочая конфигурация устройства не изменяется</p></div>')
    o.append(layer(arrow_svg(880, 885, 380, 885, 7, col=PURPLE, w=9)))

    o.append(f'<div class="card"{sd(8)} style="{ab(1240, 748, 630)}height:300px;padding:24px 30px">'
             f'<div style="display:flex;gap:22px;align-items:center">{ico("link")}'
             f'<div style="font-size:30px;font-weight:800;color:var(--navy);line-height:1.15">'
             f'Потеряли IP-связность после <span class="mono">commit</span>?</div></div>'
             f'<div class="card solid" style="margin-top:26px;padding:18px 22px;display:flex;gap:18px;align-items:center">'
             f'{ico("clock", "sm")}<div style="font-size:23px;font-weight:700;color:var(--navy);line-height:1.25">'
             f'Без <span class="mono">confirm</span> через 600 секунд сработает RESTORE</div></div></div>')
    return "".join(o)


SLIDES.append(("p059", "Механизм работы с конфигурациями", configs()))


# ======================================================= p060 IP-адрес на интерфейсе
def ip_setup():
    o = ['<h1 class="t ab ctr-x" style="top:26px;width:1700px">Настройка IP-адреса на интерфейсе ESR</h1>',
         '<div class="sub ab ctr-x" style="top:104px;letter-spacing:6px;font-size:22px;color:var(--dim)">Простые шаги к надёжной сети</div>']

    def step(l, n, title, desc, cmd, short, icn, s):
        return (f'<div class="card"{sd(s)} style="{ab(l, 180, 570)}height:500px;padding:0">'
                f'<div class="num ab" style="left:36px;top:30px;font-size:118px;color:#9bb4e6">{n}</div>'
                f'<img class="ab" src="assets/{icn}" style="left:250px;top:26px;height:140px">'
                f'<div class="ab" style="left:36px;top:190px;width:500px;font-size:31px;font-weight:800;color:var(--navy);'
                f'line-height:1.15;height:76px">{title}</div>'
                f'<p class="b sm ab" style="left:36px;top:278px;width:500px;font-size:21px;line-height:1.3">{desc}</p>'
                f'<div class="card solid ab mono" style="position:absolute;left:36px;top:350px;width:498px;padding:14px 20px;'
                f'font-size:22px;color:var(--navy);line-height:1.35">{cmd}</div>'
                + (f'<div class="card solid ab" style="position:absolute;left:36px;top:432px;width:498px;padding:10px 20px;font-size:19px;'
                   f'color:var(--dim)">Сокращённо: <b class="mono" style="color:var(--navy)">{short}</b></div>' if short else "")
                + '</div>')

    o.append(step(70, "01", "Привилегированный режим", "Переход в режим глобальной конфигурации",
                  'esr# <b style="color:var(--blue)">config</b>', "", "p060_i1.png", 1))
    o.append(step(675, "02", "Режим глобальной конфигурации", "Выбор интерфейса Gigabit Ethernet 1/0/1",
                  'esr(config)# <b style="color:var(--blue)">interface gigabitethernet 1/0/1</b>', "int gi 1/0/1", "p060_i2.png", 2))
    o.append(step(1280, "03", "Режим конфигурирования интерфейса", "Назначение IP-адреса с префиксом /24",
                  'esr(config-if-gi)# <b style="color:var(--blue)">ip address 10.0.0.1/24</b>', "ip add 10.0.0.1/24", "p060_i3.png", 3))
    o.append('<img class="ab" data-s="2" src="assets/p060_arr.png" style="left:624px;top:370px;width:66px;z-index:3">'
             '<img class="ab" data-s="3" src="assets/p060_arr.png" style="left:1229px;top:370px;width:66px;z-index:3">')

    dot = '<i style="width:16px;height:16px;border-radius:50%;background:#7fb0ff;display:block"></i>'
    o.append(f'<div class="ab" data-s="4" style="{ab(110, 705, 1700)}height:225px;border-radius:22px;'
             f'background:linear-gradient(160deg,#17285a,#0d1a40);box-shadow:0 18px 40px rgba(16,37,90,.35);'
             f'border:1.5px solid rgba(110,150,230,.5)">'
             f'<div class="ab" style="left:0;right:0;top:0;height:50px;border-bottom:1px solid rgba(160,190,255,.25);'
             f'padding:0 32px;display:flex;align-items:center;justify-content:space-between;color:#cfe0ff;font-size:18px;'
             f'font-weight:700;letter-spacing:2px;text-transform:uppercase">Конфигурация в командной строке'
             f'<span style="display:flex;gap:12px">{dot}{dot}{dot}</span></div>'
             f'<div class="ab mono" style="left:36px;top:94px;font-size:34px;color:#9fb4e8">&gt;_</div></div>')
    lines = ['esr# <b>config</b>', 'esr(config)# <b>interface gigabitethernet 1/0/1</b>',
             'esr(config-if-gi)# <b>ip address 10.0.0.1/24</b>']
    for i, ln in enumerate(lines):
        o.append(f'<div class="ab mono" data-s="{5 + i}" style="left:230px;top:{770 + i * 48}px;font-size:29px;color:#dbe7ff;'
                 f'white-space:nowrap">{ln.replace("<b>", "<b style=color:#7fb8ff>")}</div>')
    o.append(f'<div class="card ab ctr-x" data-s="8" style="position:absolute;top:940px;width:640px;padding:12px 24px;display:flex;'
             f'gap:20px;align-items:center;justify-content:center">{ico("net", "sm")}'
             f'<span style="font-size:24px;color:var(--navy)">IP-адрес интерфейса: <b class="mono" '
             f'style="font-size:28px">10.0.0.1/24</b></span></div>')
    return "".join(o)


SLIDES.append(("p060", "Настройка IP-адреса на интерфейсе ESR", ip_setup()))


# ======================================================= p061 коммутаторы доступа MES
def mes_access():
    o = ['<h1 class="t ab ctr-x" style="top:30px;width:1700px">Коммутаторы доступа <span class="lt">MES</span></h1>']

    def col(l, pill, title, sub, s):
        return (f'<div class="card"{sd(s)} style="{ab(l, 150, 590)}height:730px"></div>'
                f'<div class="ab" data-s="{s}" style="left:{l + 30}px;top:178px;min-width:210px;height:80px;'
                f'padding:0 60px;clip-path:polygon(14% 0,86% 0,100% 50%,86% 100%,14% 100%,0 50%);background:linear-gradient(90deg,#9fb6f2,#5f7fd8);color:#fff;'
                f'font-size:50px;font-weight:800;display:grid;place-items:center;box-shadow:0 10px 24px rgba(60,100,200,.3);'
                f'text-shadow:0 2px 6px rgba(30,60,160,.4)">{pill}</div>'
                f'<div class="ab" data-s="{s}" style="left:{l + 20}px;top:290px;width:550px;font-size:29px;font-weight:800;'
                f'color:var(--navy);text-transform:uppercase;text-align:center">{title}</div>'
                f'<div class="ab" data-s="{s}" style="left:{l + 20}px;top:335px;width:550px;font-size:19px;'
                f'color:var(--dim);text-align:center">{sub}</div>')

    def cap(l, t, w, txt, s, fs=27):
        return (f'<div class="ab mono" data-s="{s}" style="{ab(l, t, w)}text-align:center;font-size:{fs}px;font-weight:800;'
                f'color:var(--navy)">{txt}</div>')

    o.append(col(30, "100M", "Коммутаторы доступа 100M", "Скорость физических интерфейсов — 100 Мбит/с", 1))
    o.append(devfit("dev/mes1124mb.webp", 325, 395, 520, 160, 1))
    o.append(cap(55, 560, 540, "MES1124MB", 1))
    o.append(devfit("dev/mes1124m.webp", 325, 615, 520, 160, 1))
    o.append(cap(55, 780, 540, "MES1124M", 1))
    o.append(f'<div class="ab b sm" data-s="1" style="{ab(55, 835, 540)}text-align:center;font-size:21px;color:var(--dim)">'
             f'Также: <span class="mono">MES1428</span></div>')

    o.append(col(665, "1G", "Коммутаторы доступа 1G", "Скорость физических интерфейсов — 1 Гбит/с", 2))
    o.append(f'<div class="ab" data-s="2" style="left:760px;top:410px;width:400px;height:400px;border-radius:50%;'
             f'background:radial-gradient(circle,rgba(180,210,255,.55),rgba(180,210,255,0) 70%)"></div>')
    o.append(devfit("dev/mes2300-08.webp", 960, 460, 540, 200, 2))
    o.append(cap(690, 665, 540, "MES2300-08", 2, 32))
    o.append(f'<div class="ab mono" data-s="2" style="{ab(690, 770, 540)}text-align:center;font-size:21px;line-height:1.75;'
             f'color:var(--navy)">MES2408 • MES2308R • MES2324<br>MES2428 • MES2424 • MES2411X • MES2448</div>')

    o.append(col(1300, "PoE", "Коммутаторы доступа PoE", "Одновременная передача данных и питания по Ethernet", 3))
    o.append(devfit("dev/mes2420d-24dp.webp", 1595, 402, 500, 145, 3))
    o.append(cap(1325, 560, 540, "MES2420D-24DP", 3))
    o.append(f'<div class="ab mono" data-s="3" style="{ab(1325, 615, 540)}text-align:center;font-size:19px;line-height:1.75;'
             f'color:var(--navy)">MES2408PL/P/CP • MES2308P • MES2324P<br>MES2424P • MES2448P • MES2428P • MES2348P</div>')
    o.append(f'<div class="ab" data-s="3" style="left:1325px;top:700px;width:540px;display:flex;align-items:center;'
             f'justify-content:center"><img src="assets/p061_poe.png" style="width:530px"></div>')
    o.append(f'<div class="ab b sm" data-s="3" style="{ab(1325, 838, 540)}text-align:center;font-size:19px">'
             f'Размещение устройств без отдельной розетки питания</div>')

    o.append(f'<div class="card"{sd(4)} style="{ab(30, 910, 1860)}height:130px"></div>')
    items = [("p061_g1.png", "100M", "100 Мбит/с", 4), ("p061_g2.png", "1G", "1 Гбит/с", 5), ("p061_g3.png", "PoE", "данные + питание", 6)]
    for i, (icn, a, b, s) in enumerate(items):
        x = 90 + i * 620
        o.append(f'<div class="ab" data-s="{s}" style="{ab(x, 935, 560)}height:80px;display:flex;gap:26px;align-items:center;'
                 f'justify-content:center"><img src="assets/{icn}" style="height:82px"><span style="font-size:30px;font-weight:700;color:var(--navy)">'
                 f'<b>{a}</b> — {b}</span></div>')
        if i:
            o.append(f'<div class="ab" data-s="{s}" style="left:{x - 28}px;top:930px;width:2px;height:90px;background:var(--line)"></div>')
    return "".join(o)


SLIDES.append(("p061", "Коммутаторы доступа MES", mes_access()))


# ======================================================= p062 контроллеры
def controllers():
    small = ('font-size:15px;letter-spacing:3px;color:var(--dim);text-transform:uppercase;line-height:1.5')
    o = ['<h1 class="t ab ctr-x" style="top:36px;width:1500px">Контроллеры <span class="lt">ELTEX</span></h1>',
         f'<div class="ab" style="left:70px;top:48px;width:230px;{small}">Надёжные сети<br>для знаний<br>и развития</div>',
         f'<div class="ab" style="right:70px;top:48px;width:260px;text-align:right;{small}">Современные<br>технологии<br>'
         f'для образования<br>и науки</div>']

    xs = [32, 506, 975, 1453]
    ws = [455, 450, 459, 435]
    names = ["WLC-3350", "WLC-3200", "WLC-30", "vWLC"]
    imgs = ["dev/wlc-3350.webp", "dev/wlc-3200.webp", "dev/wlc-30.webp", "dev/vwlc.webp"]
    for i in range(4):
        o.append(f'<div class="card"{sd(1 + i)} style="{ab(xs[i], 215, ws[i])}height:320px"></div>')
        o.append(f'<div class="ab mono" data-s="{1 + i}" style="{ab(xs[i], 238, ws[i])}text-align:center;font-size:38px;'
                 f'font-weight:800;color:var(--navy)">{names[i]}</div>')
        if i < 3:
            o.append(devfit(imgs[i], xs[i] + ws[i] / 2, 330, ws[i] - 40, 180, 1 + i))
        else:
            o.append(devfit(imgs[i], xs[i] + ws[i] / 2, 295, 380, 230, 1 + i))

    feats = [("p062_f1.png", "Управление<br>точками доступа"), ("p062_f2.png", "Мониторинг<br>клиентов и трафика"),
             ("p062_f3.png", "Бесшовный<br>роуминг"), ("p062_f4.png", "VLAN · VPN · L2/L3"),
             ("p062_f5.png", "WPA2/WPA3 · RADIUS · LDAP"), ("p062_f6.png", "FIREWALL · IDS · IPS")]
    for i, (icn, t) in enumerate(feats):
        o.append(f'<div class="card"{sd(5)} style="{ab(32 + i * 312, 565, 298)}height:215px;text-align:center;padding:22px 12px;'
                 f'--dl:{i * 90}ms"><div style="display:flex;justify-content:center;align-items:center;height:120px">'
                 f'<img src="assets/{icn}" style="max-height:118px;max-width:220px"></div>'
                 f'<div style="margin-top:6px;font-size:21px;font-weight:800;color:var(--navy);text-transform:uppercase;'
                 f'line-height:1.25">{t}</div></div>')

    places = [("p062_pl1.jpg", "Офисы и учебные корпуса"), ("p062_pl2.jpg", "Кампусы и предприятия"), ("p062_pl3.jpg", "Распределённые сети")]
    for i, (icn, t) in enumerate(places):
        o.append(f'<div class="card"{sd(6)} style="{ab(32 + i * 628, 815, 600)}height:225px;display:flex;gap:26px;'
                 f'padding:0;overflow:hidden;--dl:{i * 110}ms"><img src="assets/{icn}" style="position:absolute;left:0;top:0;width:100%;height:190px;object-fit:cover">'
                 f'<div style="position:absolute;left:150px;right:10px;top:178px;font-size:25px;font-weight:800;color:var(--navy);'
                 f'text-transform:uppercase;text-align:center">{t}</div></div>')
    return "".join(o)


SLIDES.append(("p062", "Контроллеры ELTEX", controllers()))


# ======================================================= p063 точки доступа
def aps():
    o = ['<h1 class="t ab ctr-x" style="top:24px;width:1700px;font-size:58px">Модели и характеристики</h1>',
         '<div class="sub ab ctr-x" style="top:98px;font-size:38px;font-weight:800;letter-spacing:1px">Точки доступа ELTEX</div>',
         '<p class="b sm ab ctr-x" style="top:158px;width:1700px;text-align:center;font-size:19px;color:var(--dim)">'
         'Точки доступа предназначены для офисов, вузов, гостиниц, конференц-залов, государственных учреждений и других объектов.</p>']

    aps_ = [("dev/wep-3ax.webp", "WEP-3ax"), ("dev/wep-1l.webp", "WEP-1L"), ("dev/wep-550k.webp", "WEP-550K"),
            ("p063_a4.jpg", "WEP-3L")]
    for i, (img, nm) in enumerate(aps_):
        l = 60 + i * 450
        o.append(f'<div class="card"{sd(1 + i)} style="{ab(l, 195, 435)}height:320px"></div>')
        o.append((devfit if img.startswith("dev/") else fit)(img, l + 217, 210, 380, 230, 1 + i))
        o.append(f'<div class="ab" data-s="{1 + i}" style="{ab(l, 452, 435)}text-align:center;font-size:34px;'
                 f'font-weight:800;color:var(--navy)">{nm}</div>')

    def row(icn, txt, l, t, w):
        return (f'<div class="ab" style="{ab(l, t, w)}display:flex;gap:14px;align-items:center">{mi(icn)}'
                f'<p class="b sm" style="font-size:20px;line-height:1.2">{txt}</p></div>')

    left1 = [("wifi", "2,4 и 5 ГГц"), ("net", "Встроенные всенаправленные антенны"), ("power", "PoE / PoE+ / PoE++"),
             ("wifi", "Бесшовный роуминг 802.11r/k/v"), ("layers", "Несколько SSID и поддержка VLAN"),
             ("gear", "Автовыбор канала и DFS")]
    left2 = [("chart", "WMM — приоритизация трафика"), ("shield", "RADIUS / 802.1X"), ("lock", "WPA2 / WPA3 / OWE"),
             ("user", "Captive Portal"), ("mon", "Удалённая настройка и мониторинг"),
             ("cloud", "Управление через WLC или vWLC")]
    o.append(f'<div class="card"{sd(5)} style="{ab(60, 540, 960)}height:500px"></div>')
    o.append(f'<div class="ab" data-s="5" style="left:96px;top:556px;font-size:29px;font-weight:800;color:var(--navy);'
             f'text-transform:uppercase;letter-spacing:.5px">Общий функционал</div>'
             f'<div class="ab" data-s="5" style="left:96px;top:600px;width:890px;height:2px;background:var(--blue);opacity:.6"></div>')
    for i, (icn, t) in enumerate(left1):
        o.append(f'<div class="ab" data-s="5" style="left:0;top:0;--dl:{i * 60}ms">{row(icn, t, 96, 622 + i * 56, 420)}</div>')
    for i, (icn, t) in enumerate(left2):
        o.append(f'<div class="ab" data-s="5" style="left:0;top:0;--dl:{i * 60}ms">{row(icn, t, 540, 622 + i * 56, 450)}</div>')
    o.append(f'<div class="note"{sd(5)} style="{ab(86, 962, 920)}padding:8px 18px;align-items:center;gap:16px">{mi("wifi", 44, 28)}'
             f'<p class="b sm" style="font-size:18px;line-height:1.3"><b style="color:var(--blue)">Wi-Fi 6 и Wi-Fi 7: OFDMA и MU-MIMO</b> '
             f'для одновременной работы с большим количеством клиентов.</p></div>')

    diffs = [("gear", "Стандарт: Wi-Fi 6 или Wi-Fi 7"), ("wifi", "Диапазоны: 2,4 / 5 / 6 ГГц"), ("speed", "Максимальная скорость"),
             ("user", "Количество подключённых пользователей"), ("layers", "Количество SSID"),
             ("net", "MU-MIMO: от 2×2 до 4×4"), ("link", "Ethernet: от 1 до 10 Гбит/с"),
             ("power", "Питание: PoE / PoE+ / PoE++"), ("shield", "Защита WIDS / WIPS"),
             ("gear", "MLO и контроллер Z-Wave для IoT")]
    o.append(f'<div class="card"{sd(6)} style="{ab(1040, 540, 820)}height:500px"></div>')
    o.append(f'<div class="ab" data-s="6" style="left:1076px;top:556px;font-size:29px;font-weight:800;color:var(--navy);'
             f'text-transform:uppercase;letter-spacing:.5px">Основные различия</div>'
             f'<div class="ab" data-s="6" style="left:1076px;top:600px;width:750px;height:2px;background:var(--blue);opacity:.6"></div>')
    for i, (icn, t) in enumerate(diffs):
        o.append(f'<div class="ab" data-s="6" style="left:0;top:0;--dl:{i * 50}ms">{row(icn, t, 1076, 618 + i * 41, 740)}</div>')
    return "".join(o)


SLIDES.append(("p063", "Модели и характеристики: точки доступа ELTEX", aps()))


# ======================================================= p064 модельный ряд ESR
def esr_line():
    o = ['<div class="ab" style="left:70px;top:10px;font-size:58px;font-weight:600;color:var(--navy);line-height:1">Модельный ряд</div>',
         '<div class="ab" style="left:70px;top:64px;display:flex;align-items:flex-end;gap:26px">'
         '<span class="big" style="font-size:80px;line-height:1;color:var(--navy2)">ESR</span>'
         '<span style="font-size:23px;color:var(--dim);margin-bottom:16px">Сервисные маршрутизаторы</span></div>']

    def column(l, n, title, sub, icn, s, rows):
        h = ['<div class="card"' + sd(s) + f' style="{ab(l, 158, 580)}height:522px"></div>',
             f'<div class="ab" data-s="{s}" style="left:{l + 24}px;top:170px;display:flex;gap:16px;align-items:center;width:540px">'
             f'<span class="num" style="font-size:54px">{n}</span><div style="flex:1">'
             f'<div style="font-size:29px;font-weight:700;color:var(--navy)">{title}</div>'
             f'<div style="font-size:16px;color:var(--dim);letter-spacing:.5px">{sub}</div></div>'
             f'<img src="assets/{icn}" style="height:58px"></div>']
        top, area = 262, 410
        pitch = area / len(rows)
        for ri, r in enumerate(rows):
            for ci, (img, lab) in enumerate(r):
                cx = l + 290 if len(r) == 1 else l + 150 + ci * 280
                t = top + ri * pitch
                h.append(devfit(img, cx, t, 250, pitch - 40, s))
                h.append(f'<div class="ab mono" data-s="{s}" style="left:{cx - 120}px;top:{t + pitch - 32}px;width:240px;'
                         f'text-align:center;font-size:17px;font-weight:800;color:var(--navy)">{lab}</div>')
        return "".join(h)

    D = "dev/%s.webp".__mod__
    o.append(column(60, "01", "Младшие модели", "Компактность, гибкость, удобство", "p064_h1.png", 1, [
        [(D("esr-15"), "ESR-15"), (D("esr-15r"), "ESR-15R")],
        [(D("esr-14vf"), "ESR-14VF"), (D("esr-12vf"), "ESR-12VF")],
        [(D("esr-12v"), "ESR-12V"), (D("esr-10"), "ESR-10")]]))
    o.append(column(670, "02", "Средние модели", "Оптимальный баланс возможностей", "p064_h2.png", 2, [
        [(D("esr-30"), "ESR-30"), (D("esr-21"), "ESR-21")],
        [(D("esr-20"), "ESR-20"), (D("esr-200"), "ESR-200")],
        [(D("esr-100"), "ESR-100")]]))
    o.append(column(1280, "03", "Старшие модели", "Максимальная производительность", "p064_h3.png", 3, [
        [(D("esr-3100"), "ESR-3100"), (D("esr-3200"), "ESR-3200")],
        [(D("esr-1700"), "ESR-1700")],
        [(D("esr-1500"), "ESR-1500"), (D("esr-1511"), "ESR-1511")],
        [(D("esr-1000"), "ESR-1000"), (D("esr-1200"), "ESR-1200")]]))

    descs = [("01", "Младшие модели", "p064_c1.png",
              "ESR-10, ESR-12, ESR-14, ESR-15, ESR-15R построены на одном процессоре и отличаются набором интерфейсов. "
              "Компактные решения для небольших и средних офисов."),
             ("02", "Средние модели", "p064_c2.png",
              "ESR-20, ESR-21, ESR-30, ESR-100, ESR-200 отличаются процессором и набором интерфейсов. "
              "Например, ESR-21 имеет 3 RS-232 интерфейса, а ESR-30 — комбинированные интерфейсы с поддержкой SFP+ 10 Гбит/с."),
             ("03", "Старшие модели", "p064_c3.png",
              "Серия ESR-1000 (ESR-1000, 1200, 1500, 1511, 1700) имеет чип коммутации, что разгружает центральный процессор. "
              "Серия ESR-3000 (ESR-3100, 3200) чипа коммутации не имеет — весь трафик проходит через центральный процессор. "
              "Все старшие модели оснащены 10 Гбит интерфейсами (SFP+/QSFP+).")]
    for i, (n, t, icn, txt) in enumerate(descs):
        l = 60 + i * 610
        o.append(f'<div class="card"{sd(4 + i)} style="{ab(l, 692, 580)}height:264px;padding:12px 18px">'
                 f'<div style="display:flex;gap:14px;align-items:center;margin-bottom:6px">'
                 f'<span class="badge" style="width:44px;height:44px;font-size:21px">{n}</span>'
                 f'<div style="font-size:24px;font-weight:700;color:var(--navy)">{t}</div></div>'
                 f'<div style="display:flex;gap:14px;align-items:flex-start"><img src="assets/{icn}" style="width:46px;flex:none;margin-top:4px">'
                 f'<p class="b sm" style="font-size:18px;line-height:1.24;flex:1">{txt}</p></div></div>')

    stars = ["ESR-1000 — первый маршрутизатор в линейке с 24 медными интерфейсами.",
             "ESR-1700 — очень мощный и единственный двухюнитовый маршрутизатор.",
             "ESR-3200 — 12 комбинированных интерфейсов с поддержкой 1, 10, 25 или 40 Гбит/с."]
    star = ('<svg width="34" height="34" viewBox="0 0 24 24" style="flex:none"><path d="M12 2.5l2.9 6.1 6.6.8-4.9 4.6 1.3 6.6'
            'L12 17.3 6.1 20.6l1.3-6.6L2.5 9.4l6.6-.8z" fill="#5b7bd4"/></svg>')
    for i, t in enumerate(stars):
        o.append(f'<div class="card"{sd(7)} style="{ab(60 + i * 610, 968, 580)}height:80px;padding:8px 18px;display:flex;'
                 f'gap:14px;align-items:center;--dl:{i * 100}ms">{star}'
                 f'<p class="b sm" style="font-size:17px;line-height:1.22">{t}</p></div>')
    return "".join(o)


SLIDES.append(("p064", "Модельный ряд ESR", esr_line()))


# ======================================================= p065 параметры беспроводного подключения
def wifi_params():
    o = ['<h1 class="t ab ctr-x" style="top:26px;width:1700px">Параметры беспроводного подключения</h1>']

    steps = [("p065_i1.png", "1. Подключитесь<br>к устройству"), ("p065_i2.png", "2. Откройте<br>web-браузер"),
             (None, "3. Введите 192.168.1.10"), ("p065_i4.png", "4. Авторизуйтесь"), ("p065_i5.png", "5. Откройте меню<br>мониторинга")]
    for i, (icn, t) in enumerate(steps):
        top = 150 + i * 140
        left = (f'<span class="chip mono" style="font-size:19px;padding:8px 14px;color:var(--dim)">'
                f'{mi("search", 26, 18)}192.168.1.10</span>' if icn is None else f'<img src="assets/{icn}" style="height:96px">')
        o.append(f'<div class="card"{sd(1 + i)} style="{ab(64, top, 640)}height:118px;padding:0 22px;display:flex;gap:22px;'
                 f'align-items:center"><span class="badge" style="width:62px;height:62px;font-size:34px;border-radius:14px;'
                 f'background:linear-gradient(160deg,#6d8be0,#4a68c4)">{i + 1}</span>'
                 f'<div style="width:190px;display:flex;justify-content:center">{left}</div>'
                 f'<div style="font-size:24px;font-weight:800;color:var(--navy);text-transform:uppercase;line-height:1.2">{t}</div></div>')

    # браузер
    o.append(f'<div class="card ab" data-s="2" style="{ab(732, 150, 840)}height:615px;padding:0;overflow:hidden">'
             f'<div class="ab" style="left:0;right:0;top:0;height:46px;background:rgba(225,233,250,.9)">'
             f'<i class="ab" style="left:18px;top:15px;width:14px;height:14px;border-radius:50%;background:#ee6a5f"></i>'
             f'<i class="ab" style="left:40px;top:15px;width:14px;height:14px;border-radius:50%;background:#f5bd4f"></i>'
             f'<i class="ab" style="left:62px;top:15px;width:14px;height:14px;border-radius:50%;background:#61c454"></i>'
             f'<div class="ab" style="left:96px;top:8px;width:160px;height:38px;border-radius:10px 10px 0 0;background:#fff;'
             f'font-size:15px;padding:10px 16px;color:var(--navy)">WEP-3ax</div></div>'
             f'<div class="ab" style="left:0;right:0;top:46px;height:48px;background:#fff;border-bottom:1px solid var(--line)">'
             f'<div class="ab mono" data-s="3" style="left:70px;top:8px;width:560px;height:32px;border-radius:16px;'
             f'background:#eef2fb;padding:5px 16px;font-size:15px;color:var(--navy)">http://192.168.1.10</div></div>'
             f'<div class="ab" style="left:0;right:0;top:94px;bottom:0;background:linear-gradient(180deg,#eef3fc,#e0e9f9)"></div></div>')
    o.append(f'<div class="card solid ab" data-s="4" style="{ab(875, 300, 545)}height:430px;padding:28px 34px">'
             f'<div style="text-align:center;font-size:42px;font-weight:800;color:var(--navy)">WEP-3ax</div>'
             f'<div style="margin-top:28px;font-size:15px;letter-spacing:1px;color:var(--dim)">ЛОГИН</div>'
             f'<div class="mono" style="margin-top:6px;padding:10px 16px;border:1.5px solid var(--line);border-radius:8px;'
             f'font-size:22px;color:var(--navy);background:#fff">admin</div>'
             f'<div style="margin-top:18px;font-size:15px;letter-spacing:1px;color:var(--dim)">ПАРОЛЬ</div>'
             f'<div class="mono" style="margin-top:6px;padding:10px 16px;border:1.5px solid var(--line);border-radius:8px;'
             f'font-size:22px;color:var(--navy);background:#fff;letter-spacing:3px">••••••••</div>'
             f'<div style="margin-top:26px;display:inline-flex;gap:10px;align-items:center;padding:12px 26px;border-radius:8px;'
             f'background:linear-gradient(180deg,#2a78e8,#1a5cc8);color:#fff;font-size:20px;font-weight:700">'
             f'<svg width="20" height="20" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7" stroke="#fff" stroke-width="3" '
             f'fill="none" stroke-linecap="round"/></svg>ВОЙТИ</div></div>')
    rows = [("IP-АДРЕС:", "192.168.1.10"), ("МАСКА:", "255.255.255.0"), ("ВОЗМОЖНО ПОЛУЧЕНИЕ АДРЕСА ПО DHCP", ""),
            ("ЛОГИН:", "admin"), ("ПАРОЛЬ:", "password")]
    body = "".join(
        f'<div style="display:flex;gap:16px;padding:10px 0;border-top:1px solid var(--line);font-size:17px;color:var(--navy)">'
        f'<span style="width:{150 if v else 340}px;font-weight:600">{k}</span><span class="mono">{v}</span></div>' for k, v in rows)
    o.append(f'<div class="card ab" data-s="5" style="{ab(1478, 405, 400)}height:350px;padding:20px 24px">'
             f'<div style="font-size:20px;font-weight:800;color:var(--navy);margin-bottom:12px;letter-spacing:.5px">'
             f'ТЕХНИЧЕСКИЕ ПАРАМЕТРЫ</div>{body}</div>')

    ssid = ('<span class="mono" style="font-size:21px;font-weight:800;color:#fff;background:#2f4fa8;padding:3px 10px;'
            'border-radius:6px">SSID</span>')
    bottom = [("p065_b1.png", "Режим беспроводной сети"), ("p065_b2.png", "SSID"), ("p065_b3.png", "Беспроводной канал")]
    for i, (icn, t) in enumerate(bottom):
        left = f'<img src="assets/{icn}" style="height:130px">'
        o.append(f'<div class="card"{sd(6)} style="{ab(64 + i * 600, 830, 560)}height:200px;padding:0 26px;display:flex;gap:24px;'
                 f'align-items:center;--dl:{i * 100}ms">{left}'
                 f'<div style="flex:1"><div style="font-size:22px;font-weight:800;color:var(--navy);text-transform:uppercase;'
                 f'line-height:1.2">{t}</div><div style="margin-top:20px;height:4px;border-radius:2px;background:var(--line)"></div>'
                 f'<div style="margin-top:14px;height:4px;width:70%;border-radius:2px;background:var(--line)"></div></div></div>')
    return "".join(o)


SLIDES.append(("p065", "Параметры беспроводного подключения", wifi_params()))


# ======================================================= p066 сетевые устройства
def net_devices():
    o = ['<div class="ab" style="left:70px;top:30px;font-size:82px;font-weight:800;color:var(--navy2);text-transform:uppercase;'
         'letter-spacing:1px;line-height:1">Сетевые устройства</div>',
         '<div class="ab" style="left:76px;top:128px;font-size:21px;letter-spacing:9px;color:var(--dim);text-transform:uppercase">'
         'Основа современных сетей</div>']

    def card(l, n, title, en, lvl, img, desc, s):
        en_top = 262 + (112 if len(title) > 14 else 40)
        return (f'<div class="card"{sd(s)} style="{ab(l, 190, 580)}height:610px;padding:0"></div>'
                f'<div class="ab" data-s="{s}" style="left:{l + 26}px;top:206px;width:90px;height:34px;background:var(--blue);'
                f'color:#fff;font-family:var(--mono);font-weight:800;font-size:20px;padding:5px 14px;'
                f'clip-path:polygon(0 0,100% 0,88% 100%,0 100%)">{n}</div>'
                f'<div class="ab" data-s="{s}" style="left:{l + 26}px;top:262px;width:330px;font-size:31px;font-weight:800;'
                f'color:var(--navy);text-transform:uppercase;line-height:1.12">{title}</div>'
                f'<div class="ab" data-s="{s}" style="left:{l + 26}px;top:{en_top}px;font-size:15px;'
                f'letter-spacing:5px;color:var(--dim);text-transform:uppercase;width:330px">{en}</div>'
                f'<div class="ab" data-s="{s}" style="left:{l + 370}px;top:262px;width:190px;display:flex;gap:10px;align-items:center">'
                f'{ico("layers", "sm")}<div style="font-size:16px;color:var(--navy);line-height:1.25">{lvl}</div></div>'
                + img +
                f'<p class="b sm ab" data-s="{s}" style="left:{l + 28}px;top:520px;width:525px;font-size:19px;line-height:1.32">{desc}</p>')

    o.append(card(70, "01", "Маршрутизатор", "Router", "Сетевой уровень<br>(3 уровень OSI)",
                  fit("p066_router.jpg", 360, 370, 520, 125, 1),
                  "Это сетевое устройство, соединяющее сети и предназначенное для пересылки пакетов из одной сети в другую.", 1))
    o.append(card(670, "02", "Коммутатор", "Switch", "Канальный уровень<br>(2 уровень OSI)",
                  fit("p066_switch.jpg", 960, 375, 520, 125, 2),
                  "Это сетевое устройство, предназначенное для пересылки кадров в пределах одной сети. "
                  "Коммутаторы локальных сетей работают на канальном уровне (2 уровень модели OSI).", 2))
    o.append(card(1270, "03", "Беспроводная точка доступа", "Wireless access point", "Канальный уровень<br>(2 уровень OSI)",
                  fit("p066_ap.jpg", 1560, 405, 300, 112, 3),
                  "Это сетевое устройство, которое представляет собой базовую станцию для создания беспроводной локальной сети, "
                  "работающей поверх проводной сети или параллельно с ней. Точка доступа работает на канальном уровне "
                  "(2 уровень модели OSI).", 3))

    # схемы
    def sm(n):
        return ico(n, "sm")

    def cap(t):
        return f'<div style="font-size:15px;color:var(--navy);text-align:center;margin-top:4px">{t}</div>'

    o.append(f'<div class="ab" data-s="4" style="{ab(100, 680, 520)}display:flex;justify-content:space-between;align-items:center">'
             f'<div style="text-align:center">{sm("cloud")}{cap("Сеть 1")}</div>{ico("router")}'
             f'<div style="text-align:center">{sm("cloud")}{cap("Сеть 2")}</div></div>')
    o.append(layer(
        '<g data-s="4" stroke="var(--blue)" stroke-width="3" fill="none" stroke-linecap="round">'
        '<path d="M236 706H262M246 698L236 706L246 714M454 706H428M444 698L454 706L444 714"/>'
        '<path d="M960 745V775M960 775H800V800M960 775H1100V800"/></g>'))
    o.append(f'<div class="ab" data-s="4" style="left:930px;top:690px">{sm("switch")}</div>'
             f'<div class="ab" data-s="4" style="left:770px;top:795px">{sm("mon")}</div>'
             f'<div class="ab" data-s="4" style="left:930px;top:795px">{sm("server")}</div>'
             f'<div class="ab" data-s="4" style="left:1072px;top:795px">{sm("print")}</div>')
    o.append(f'<div class="ab" data-s="4" style="{ab(1320, 700, 480)}display:flex;justify-content:space-between;align-items:center">'
             f'{sm("pc")}{sm("wifi")}{sm("phone")}{sm("phone")}</div>')

    o.append(f'<div class="card"{sd(5)} style="{ab(50, 850, 1830)}height:200px"></div>')
    o.append(f'<div class="ab" data-s="5" style="left:90px;top:880px;width:380px;font-size:44px;font-weight:800;'
             f'color:var(--navy2);text-transform:uppercase;line-height:1.1">Настройка<br>и доступ</div>'
             f'<div class="ab" data-s="5" style="left:92px;top:985px;width:380px;font-size:14px;letter-spacing:5px;'
             f'color:var(--dim);text-transform:uppercase;line-height:1.5">Больше, чем просто<br>подключить</div>')
    o.append(f'<p class="b sm ab" data-s="5" style="{ab(500, 870, 1330)}font-size:21px;line-height:1.38">Чтобы компьютерная сеть '
             f'функционировала, мало собрать и подключить сетевые устройства через кабели и подключить к интернет-провайдеру, '
             f'необходимо на каждом сетевом устройстве выполнить определённую настройку. Чтобы выполнить настройку необходимых '
             f'параметров, нужно получить доступ к сетевому устройству.</p>')
    items = [("gear", "Настройка<br>параметров", 520, 330),
             ("mon", "Доступ к устройству<br>(например, через Web-интерфейс, CLI, SSH)", 880, 520),
             ("globe", "Стабильная<br>и безопасная работа сети", 1440, 400)]
    for i, (icn, t, x, w) in enumerate(items):
        o.append(f'<div class="ab" data-s="6" style="{ab(x, 962, w)}display:flex;gap:16px;align-items:center;--dl:{i * 100}ms">'
                 f'{ico(icn, "sm")}<div style="font-size:17px;font-weight:700;color:var(--navy);text-transform:uppercase;'
                 f'line-height:1.25">{t}</div></div>')
        if i:
            o.append(f'<div class="ab" data-s="6" style="left:{x - 24}px;top:962px;width:2px;height:70px;background:var(--line)"></div>')
    return "".join(o)


SLIDES.append(("p066", "Сетевые устройства", net_devices()))
