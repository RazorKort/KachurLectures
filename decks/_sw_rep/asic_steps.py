# -*- coding: utf-8 -*-
"""ASIC_STEPS — 8 функций ASIC и 5 шагов обработки кадра: вёрстка 1:1 инфографики."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 146
P = "rep/asic_steps_"

CSS = """<style>
.as-o{font-family:Oswald,sans-serif}
.as-c{position:absolute;top:153px;height:207px;border-radius:8px;border:2px solid rgba(42,212,255,.8);background:rgba(4,18,50,.9);
  box-shadow:0 0 14px rgba(42,212,255,.5),inset 0 0 18px rgba(42,212,255,.12)}
.as-n{position:absolute;width:30px;height:30px;border-radius:50%;border:2.5px solid #cfefff;display:flex;align-items:center;justify-content:center;
  font-family:Oswald,sans-serif;font-weight:500;font-size:21px;color:#fff;box-shadow:0 0 8px rgba(42,212,255,.7)}
.as-n.y{border-color:#ffc53d;box-shadow:0 0 10px #ffc53d}
.as-h{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:17px;line-height:20px;color:#fff;white-space:nowrap}
.as-t{position:absolute;color:#e6f1ff;font-size:15px;line-height:19.5px;white-space:nowrap}
.as-mini{position:absolute;border-collapse:collapse;white-space:nowrap;font-size:11.5px;color:#fff;background:rgba(2,10,28,.9)}
.as-mini td{border:1px solid rgba(220,235,255,.75);padding:0 6px;height:25px}
.as-fr{position:absolute;border-radius:6px;border:2.5px solid;background:rgba(14,14,20,.9)}
.as-cells{position:absolute;display:flex}
.as-cells span{height:34px;line-height:34px;font-family:Oswald,sans-serif;font-size:16px;color:#fff;text-align:center;border:1.5px solid;margin-right:-1.5px}
.as-tb{position:absolute;left:1013px;top:385px;width:229px;height:177px;border-radius:6px;border:2px solid rgba(42,212,255,.8);background:rgba(4,16,44,.95);box-shadow:0 0 12px rgba(42,212,255,.5)}
.as-tr{position:absolute;left:1021px;width:213px;height:24px;font-size:13.5px;color:#fff;line-height:24px}
.as-tr b{position:absolute;left:162px;width:50px;text-align:center;font-weight:400}
.as-tr.hi{border:2px solid #2ad4ff;box-shadow:0 0 10px #2ad4ff;background:rgba(42,212,255,.2);animation:as-blink 1.4s infinite}
@keyframes as-blink{50%{box-shadow:0 0 2px #2ad4ff;background:rgba(42,212,255,.05)}}
.as-run{position:absolute;width:20px;height:12px;border-radius:6px;opacity:0}
.as-run.y{left:290px;top:514px;background:#ffd84a;box-shadow:0 0 12px 4px #ffb02e;animation:as-in 2.4s 1s infinite}
.as-run.c{left:1100px;top:600px;background:#9ff;box-shadow:0 0 12px 4px #2ad4ff;animation:as-out 2.4s 2.2s infinite}
@keyframes as-in{0%{opacity:0;transform:translateX(0)}15%{opacity:1}85%{opacity:1;transform:translateX(350px)}100%{opacity:0;transform:translateX(350px)}}
@keyframes as-out{0%{opacity:0;transform:translate(0,0)}15%{opacity:1}85%{opacity:1;transform:translate(260px,-40px)}100%{opacity:0;transform:translate(260px,-40px)}}
.as-bar{position:absolute;left:170px;top:707px;width:1333px;height:65px;border-radius:6px;border:2px solid rgba(42,212,255,.8);background:rgba(4,18,50,.9);box-shadow:0 0 14px rgba(42,212,255,.5)}
.as-s{position:absolute;top:786px;height:130px;border-radius:8px;border:2px solid rgba(42,212,255,.75);background:rgba(4,18,50,.9);box-shadow:0 0 14px rgba(42,212,255,.45)}
.as-s.y{border-color:#ffc53d;background:rgba(50,36,8,.9);box-shadow:0 0 16px rgba(255,197,61,.6)}
.as-big{position:absolute;width:40px;height:40px;border-radius:50%;border:3px solid #cfefff;display:flex;align-items:center;justify-content:center;
  font-family:Oswald,sans-serif;font-weight:500;font-size:28px;color:#fff;box-shadow:0 0 10px rgba(42,212,255,.8)}
.as-arr{position:absolute;top:832px;color:#2ad4ff;font-size:38px;line-height:1;text-shadow:0 0 8px #2ad4ff}
</style>"""

CARDS = [  # x, w, заголовок, иконка(файл, x, y, w) или None, текст
    (25, 205, "ПРИЁМ И АНАЛИЗ<br>КАДРА", ("i1", 58, 232, 154), "Принимает кадр<br>с порта и выделяет<br>заголовок"),
    (240, 205, "ЧТЕНИЕ<br>MAC-АДРЕСОВ", None, "Извлекает исходный<br>и конечный MAC-адреса"),
    (455, 191, "ПОИСК В<br>MAC-ТАБЛИЦЕ", ("i3", 522, 220, 66), "Ищет соответствие<br>конечного MAC-адреса<br>в таблице коммутации"),
    (657, 196, "ВЫБОР<br>ВЫХОДНОГО ПОРТА", ("i4", 702, 220, 106), "Определяет, на какой<br>порт отправить кадр"),
    (862, 195, "ПЕРЕСЫЛКА ИЛИ<br>ОТБРАСЫВАНИЕ", ("i5", 892, 220, 136), "Пересылает кадр<br>или отбрасывает,<br>если это необходимо"),
    (1067, 175, "ОБРАБОТКА<br>VLAN-ТЕГОВ", ("i6", 1102, 220, 100), "Анализирует<br>и обрабатывает<br>802.1Q VLAN-теги"),
    (1252, 191, "ФИЛЬТРАЦИЯ И<br>ПРИОРИТИЗАЦИЯ", ("i7", 1282, 220, 138), "Применяет правила<br>фильтрации и приоритеты<br>(QoS)"),
    (1453, 193, "ПРОВЕРКА<br>ЦЕЛОСТНОСТИ", ("i8", 1512, 218, 82), "Проверяет корректность<br>кадра (FCS/CRC)"),
]
TEXT_Y = [290, 296, 285, 296, 288, 292, 292, 296]


def _cards():
    out = []
    for i, (x, w, t, ic, tx) in enumerate(CARDS):
        icon = img(P + ic[0] + ".png", "left:%dpx;top:%dpx;width:%dpx" % ic[1:], "ab") if ic else (
            '<table class="as-mini" style="left:250px;top:229px;width:182px"><tr><td>MAC SRC</td><td>00:1A:2B:3C:4D:5E</td></tr>'
            '<tr><td>MAC DST</td><td>00:AA:BB:CC:DD:EE</td></tr></table>')
        col = "#ffd84a" if i == 0 else ("#5fe8ff" if i in (2, 3, 6) else "#fff")
        out.append('<div class="step" style="transition-delay:%dms"><div class="as-c" style="left:%dpx;width:%dpx"></div>'
                   '<div class="as-n%s" style="left:%dpx;top:167px">%d</div><div class="as-h" style="left:%dpx;top:169px;color:%s">%s</div>%s'
                   '<div class="as-t" style="left:%dpx;top:%dpx">%s</div></div>'
                   % (i * 80, x, w, " y" if i == 0 else "", x + 13, i + 1, x + 58, col, t, icon, x + 14, TEXT_Y[i], tx))
    return "".join(out)


def _cells(x, y, col, bg, first):
    ws = [46, 46, 46, 52, 46]
    s = "".join('<span style="width:%dpx;border-color:%s;background:%s">%s</span>' % (w, col, first if j == 0 else bg, n)
                for j, (w, n) in enumerate(zip(ws, ["DST", "SRC", "VLAN", "DATA", "FCS"])))
    return '<div class="as-cells" style="left:%dpx;top:%dpx">%s</div>' % (x, y, s)


MAC = [("MAC-АДРЕС", "ПОРТ", 418), ("00:1A:2B:3C:4D:5E", "1", 443), ("00:AA:BB:CC:DD:EE", "5", 468),
       ("00:11:22:33:44:55", "3", 492), ("00:DE:AD:BE:EF:00", "8", 516), ("... ... ...", ":", 538)]


def _mac():
    out = ['<div class="as-tb"></div><div class="ab as-o" style="left:1030px;top:392px;font-size:19px;color:#fff;font-weight:500">MAC-ТАБЛИЦА</div>']
    for i, (a, p, y) in enumerate(MAC):
        out.append('<div class="as-tr%s" style="top:%dpx;%s">&nbsp;%s<b>%s</b></div>'
                   % (" hi" if i == 2 else "", y, "background:rgba(42,212,255,.18);color:#bfefff" if i == 0 else "", a, p))
    return "".join(out)


HTML = CSS + f"""
{_cards()}

<div class="step">
  {img(P + "scene.webp", "left:0;top:362px;width:1672px", "ab")}
  <div class="as-run y"></div><div class="as-run c"></div>
</div>
<div class="step">
  <div class="as-fr" style="left:30px;top:452px;width:258px;height:120px;border-color:#ffc53d;box-shadow:0 0 14px rgba(255,197,61,.7)"></div>
  <div class="ab" style="left:48px;top:463px;font-size:19px;line-height:23px;color:#ffd84a">Входящий кадр<br>с порта 1</div>
  {_cells(45, 520, "#ffc53d", "rgba(60,40,6,.9)", "rgba(200,140,20,.9)")}
</div>
<div class="step">{_mac()}</div>
<div class="step">
  <div class="as-fr" style="left:1382px;top:482px;width:262px;height:120px;border-color:#2ad4ff;background:rgba(4,30,60,.9);box-shadow:0 0 14px rgba(42,212,255,.8)"></div>
  <div class="ab" style="left:1398px;top:492px;font-size:19px;line-height:23px;color:#bfefff">Кадр передаётся<br>на порт 5</div>
  {_cells(1396, 549, "#2ad4ff", "rgba(10,90,130,.9)", "rgba(20,150,190,.95)")}
</div>

<div class="step">
  <div class="as-bar"></div>
  {img(P + "gauge.png", "left:183px;top:712px;width:81px", "ab")}
  <div class="ab as-o" style="left:274px;top:722px;font-size:31px;color:#fff;font-weight:600;letter-spacing:.5px">АППАРАТНАЯ ОБРАБОТКА — <span style="color:#5fe8ff">ВЫСОКАЯ СКОРОСТЬ</span></div>
  <div class="ab" style="left:1020px;top:724px;width:2px;height:36px;background:#9fd8ff"></div>
  <div class="ab" style="left:1056px;top:718px;font-size:20px;line-height:23px;color:#fff">Кадры обрабатываются быстрее,<br>чем центральным процессором</div>
</div>

<div class="step">
  <div class="as-s y" style="left:20px;width:302px"></div>
  <div class="as-big" style="left:48px;top:806px;border-color:#ffc53d;box-shadow:0 0 10px #ffc53d">1</div>
  <div class="as-h" style="left:113px;top:807px">КАДР ПОСТУПАЕТ<br>НА ПОРТ</div>
  {img(P + "b1.png", "left:106px;top:848px;width:142px", "ab")}
  <div class="as-arr" style="left:300px;color:#ffc53d;text-shadow:0 0 8px #ffb02e">&#10140;</div>
</div>
<div class="step" style="transition-delay:.1s">
  <div class="as-s" style="left:353px;width:302px"></div>
  <div class="as-big" style="left:378px;top:806px">2</div>
  <div class="as-h" style="left:443px;top:807px">ASIC АНАЛИЗИРУЕТ<br>ЗАГОЛОВОК</div>
  {img(P + "b2.png", "left:463px;top:848px;width:94px", "ab")}
  <div class="as-arr" style="left:635px">&#10140;</div>
</div>
<div class="step" style="transition-delay:.2s">
  <div class="as-s" style="left:686px;width:302px"></div>
  <div class="as-big" style="left:710px;top:806px">3</div>
  <div class="as-h" style="left:794px;top:807px;color:#5fe8ff">ПОИСК В<br>MAC-ТАБЛИЦЕ</div>
  {img(P + "b3.png", "left:788px;top:848px;width:99px", "ab")}
  <div class="as-arr" style="left:968px">&#10140;</div>
</div>
<div class="step" style="transition-delay:.3s">
  <div class="as-s" style="left:1019px;width:302px"></div>
  <div class="as-big" style="left:1043px;top:806px">4</div>
  <div class="as-h" style="left:1122px;top:807px;color:#5fe8ff">ВЫБОР<br>ВЫХОДНОГО ПОРТА</div>
  {img(P + "b4.png", "left:1128px;top:842px;width:114px", "ab")}
  <div class="as-arr" style="left:1302px">&#10140;</div>
</div>
<div class="step" style="transition-delay:.4s">
  <div class="as-s" style="left:1351px;width:301px"></div>
  <div class="as-big" style="left:1375px;top:806px">5</div>
  <div class="as-h" style="left:1446px;top:817px">ПЕРЕДАЧА КАДРА</div>
  {img(P + "b5.png", "left:1436px;top:848px;width:132px", "ab")}
</div>
"""
