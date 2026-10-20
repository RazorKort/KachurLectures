# -*- coding: utf-8 -*-
"""ASIC1 — ASIC в сетевом коммутаторе: функции, процесс обработки, сравнение ASIC/CPU. Вёрстка 1:1 (источник — webp)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 238
P = "rep/asic1_"

CSS = """<style>
.a1-o{font-family:Oswald,sans-serif}
.a1-b{position:absolute;border-radius:8px;border:2px solid rgba(42,212,255,.85);background:rgba(4,20,56,.9);
  box-shadow:0 0 16px rgba(42,212,255,.6),inset 0 0 18px rgba(42,212,255,.14)}
.a1-bt{position:absolute;text-align:center;font-family:Oswald,sans-serif;font-weight:500;font-size:16.5px;line-height:19px;color:#fff;letter-spacing:.3px}
.a1-t{position:absolute;color:#e6f1ff;font-size:13px;line-height:16px}
.a1-n{position:absolute;width:28px;height:28px;border-radius:50%;border:2px solid #cfefff;display:flex;align-items:center;justify-content:center;
  font-family:Oswald,sans-serif;font-size:19px;color:#fff;box-shadow:0 0 8px #2ad4ff}
.a1-arr{position:absolute;top:826px;color:#2ad4ff;font-size:30px;line-height:1;text-shadow:0 0 8px #2ad4ff}
.a1-chip{position:absolute;left:690px;top:450px;width:90px;height:76px;border-radius:10px;animation:a1-pulse 1.8s ease-in-out infinite}
@keyframes a1-pulse{50%{box-shadow:0 0 40px 10px rgba(42,212,255,.55)}}
.a1-pkt{position:absolute;width:24px;height:12px;border-radius:3px;opacity:0}
.a1-pkt.i{left:40px;top:500px;background:#9ff;box-shadow:0 0 10px 3px #2ad4ff;animation:a1-in 2.6s .6s infinite}
.a1-pkt.o{left:1080px;top:540px;background:#ffd84a;box-shadow:0 0 10px 3px #ffb02e;animation:a1-out 2.6s 1.8s infinite}
@keyframes a1-in{0%{opacity:0;transform:translateX(0)}15%{opacity:1}85%{opacity:1;transform:translateX(160px)}100%{opacity:0;transform:translateX(160px)}}
@keyframes a1-out{0%{opacity:0;transform:translateX(0)}15%{opacity:1}85%{opacity:1;transform:translateX(110px)}100%{opacity:0;transform:translateX(110px)}}
</style>"""

TOPB = [(376, 176, "t1", 422, 252, 86, "ПРИЁМ И АНАЛИЗ<br>КАДРА"), (566, 184, "t2", 582, 268, 152, "ЧТЕНИЕ SOURCE MAC<br>И DESTINATION MAC"),
        (763, 170, "t3", 808, 252, 80, "ПОИСК В<br>MAC-ТАБЛИЦЕ"), (946, 180, "t4", 992, 252, 88, "ВЫБОР<br>ВЫХОДНОГО ПОРТА")]
BOTB = [(308, 176, "u1", 352, 628, 86, "ПЕРЕСЫЛКА ИЛИ<br>ОТБРАСЫВАНИЕ"), (497, 156, "u2", 536, 626, 78, "ОБРАБОТКА<br>VLAN-ТЕГОВ"),
        (665, 177, "u3", 698, 618, 114, "ФИЛЬТРАЦИЯ<br>И ПРИОРИТИЗАЦИЯ"), (856, 174, "u4", 906, 624, 72, "ПРОВЕРКА<br>ЦЕЛОСТНОСТИ FCS")]
STEPS = [(45, 193, "s1", 108, 806, 110, "КАДР ПОСТУПАЕТ<br>НА ПОРТ"), (270, 196, "s2", 342, 798, 70, "ASIC АНАЛИЗИРУЕТ<br>ЗАГОЛОВОК"),
         (497, 196, "s3", 572, 798, 46, "ПОИСК В<br>MAC-ТАБЛИЦЕ"), (724, 196, "s4", 792, 793, 66, "ВЫБОР<br>ВЫХОДНОГО ПОРТА"),
         (953, 219, "s5", 1032, 808, 96, "ПЕРЕДАЧА КАДРА")]


def _boxes(rows, y, h, ty, step_delay=90):
    out = []
    for i, (x, w, ic, ix, iy, iw, t) in enumerate(rows):
        out.append('<div class="step" style="transition-delay:%dms"><div class="a1-b" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"></div>%s'
                   '<div class="a1-bt" style="left:%dpx;top:%dpx;width:%dpx">%s</div></div>'
                   % (i * step_delay, x, y, w, h, img(P + ic + ".png", "left:%dpx;top:%dpx;width:%dpx" % (ix, iy, iw), "ab"), x, ty, w, t))
    return "".join(out)


def _steps():
    out = []
    for i, (x, w, ic, ix, iy, iw, t) in enumerate(STEPS):
        one = "<br>" not in t
        out.append('<div class="step" style="transition-delay:%dms"><div class="a1-b" style="left:%dpx;top:786px;width:%dpx;height:114px"></div>'
                   '<div class="a1-n" style="left:%dpx;top:794px">%d</div>%s<div class="a1-bt" style="left:%dpx;top:%dpx;width:%dpx">%s</div>%s</div>'
                   % (i * 110, x, w, x + 7, i + 1, img(P + ic + ".png", "left:%dpx;top:%dpx;width:%dpx" % (ix, iy, iw), "ab"),
                      x, 862 if one else 856, w, t,
                      '<div class="a1-arr" style="left:%dpx">&#10140;</div>' % (x + w + 2) if i < 4 else ""))
    return "".join(out)


HTML = CSS + f"""
<div class="step">
  <div class="ab a1-o" style="left:58px;top:257px;font-size:15px;letter-spacing:1px;color:#5fe8ff">ОТ КАДРА К ПЕРЕДАЧЕ — В АППАРАТЕ</div>
  {img(P + "scene.webp", "left:0;top:372px;width:1210px", "ab")}
  <div class="a1-chip"></div><div class="a1-pkt i"></div><div class="a1-pkt o"></div>
  <div class="ab a1-o" style="left:24px;top:425px;padding:2px 10px;font-size:16px;line-height:19px;color:#fff;background:rgba(6,14,36,.95);border-radius:4px">ВХОДЯЩИЕ<br>ETHERNET-КАДРЫ</div>
  <div class="ab a1-o" style="left:1076px;top:584px;padding:2px 8px;font-size:16px;line-height:18px;color:#fff;background:rgba(6,14,36,.85);border-radius:4px">К ВЫХОДНЫМ<br>ПОРТАМ</div>
</div>
{_boxes(TOPB, 245, 128, 327)}
{_boxes(BOTB, 614, 124, 689)}

<div class="step">
  <div class="a1-b" style="left:18px;top:748px;width:1177px;height:172px;border-radius:4px;background:rgba(4,16,44,.82)"></div>
  <div class="ab a1-o" style="left:52px;top:752px;font-size:21px;font-weight:500;color:#fff;letter-spacing:.4px">ПРОЦЕСС ОБРАБОТКИ КАДРА В КОММУТАТОРЕ</div>
</div>
{_steps()}

<div class="step">
  <div class="a1-b" style="left:1210px;top:420px;width:450px;height:502px;border-radius:6px;background:rgba(4,14,40,.9)"></div>
  <div class="ab a1-o" style="left:1230px;top:434px;font-size:21px;font-weight:500;color:#fff;letter-spacing:.4px">СРАВНЕНИЕ СПОСОБОВ ОБРАБОТКИ</div>
</div>
<div class="step">
  <div class="a1-b" style="left:1218px;top:475px;width:434px;height:198px"></div>
  <div class="ab a1-o" style="left:1238px;top:485px;font-size:24px;font-weight:600;color:#2ad4ff">ASIC —</div>
  <div class="ab a1-o" style="left:1315px;top:487px;font-size:17px;font-weight:500;color:#5fe8ff">АППАРАТНАЯ ОБРАБОТКА</div>
  <div class="a1-t" style="left:1315px;top:508px;font-size:14px;color:#5fe8ff">Быстро и параллельно</div>
  {img(P + "dasic.png", "left:1225px;top:535px;width:267px", "ab")}
  {img(P + "chk.png", "left:1500px;top:525px;width:32px", "ab")}
  <div class="a1-t" style="left:1533px;top:524px;font-size:11px;line-height:13px">Параллельная<br>обработка<br>множества кадров</div>
  <div class="a1-t" style="left:1533px;top:576px;font-size:11px;line-height:13px">Аппаратная<br>пересылка на скорости<br>линии</div>
  <div class="a1-t" style="left:1533px;top:628px;font-size:11px;line-height:13px">Высокая<br>производительность</div>
</div>
<div class="step">
  <div class="a1-b" style="left:1218px;top:688px;width:434px;height:157px;border-color:rgba(255,197,61,.6);box-shadow:0 0 12px rgba(255,197,61,.35)"></div>
  <div class="ab a1-o" style="left:1238px;top:692px;font-size:24px;font-weight:600;color:#ffb02e">CPU —</div>
  <div class="ab a1-o" style="left:1315px;top:698px;font-size:17px;font-weight:500;color:#fff">ПРОГРАММНАЯ ОБРАБОТКА</div>
  <div class="a1-t" style="left:1315px;top:718px;font-size:14px">Последовательно и медленнее</div>
  {img(P + "dcpu.png", "left:1225px;top:736px;width:270px", "ab")}
  {img(P + "chk2.png", "left:1500px;top:735px;width:32px", "ab")}
  <div class="a1-t" style="left:1533px;top:740px;font-size:11px;line-height:13px">Обработка<br>по одному кадру</div>
  <div class="a1-t" style="left:1533px;top:780px;font-size:11px">Больше задержка</div>
  <div class="a1-t" style="left:1533px;top:808px;font-size:11px;line-height:13px">Ниже<br>производительность</div>
</div>
<div class="step">
  <div class="ab" style="left:1225px;top:852px;width:425px;height:54px;border-radius:6px;border:1.5px solid rgba(42,212,255,.45);background:rgba(4,16,44,.7)"></div>
  <div class="a1-t" style="left:1238px;top:860px;font-size:12.5px">CPU также используется для управления, настройки и выполнения<br>дополнительных функций коммутатора.</div>
</div>
"""
