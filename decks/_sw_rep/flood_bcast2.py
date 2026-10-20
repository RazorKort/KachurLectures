# -*- coding: utf-8 -*-
"""Лавинная передача — широковещательная, 6 шагов (pptx 24): вёрстка 1:1 + полёт кадров."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _fwkit import *

W, H, TOP = 1672, 941, 85
N = "flood_bcast2_"

CARDS = [  # x, y, иконка, ix, iy, iw, заголовок, текст
    (35, 430, "i1.png", 118, 438, 64, "ПРИЁМ И ПРОВЕРКА", "Кадр принят на 1/0/2 • FCS<br>подтверждает целостность"),
    (577, 430, "i2.png", 670, 438, 54, "ОБРАБОТКА FCS", "Входное поле FCS<br>отбрасывается"),
    (1112, 430, "i3.png", 1200, 444, 70, "ОБУЧЕНИЕ", "SMAC изучен • таймер записи<br>1/0/2 обновлён"),
    (35, 537, "i4.png", 123, 548, 61, "РАСПОЗНАВАНИЕ", "DMAC ff:ff:ff:ff:ff:ff —<br>широковещательный"),
    (577, 537, "i5.png", 670, 548, 58, "РЕПЛИКАЦИЯ", "Во все порты VLAN 1,<br>кроме входящего"),
    (1112, 537, "i6.png", 1206, 548, 66, "НОВЫЙ FCS", "Перед отправкой контрольная<br>сумма рассчитывается заново"),
]


def _cards():
    out = []
    for i, (x, y, ic, ix, iy, iw, t, s) in enumerate(CARDS):
        out.append('<div class="step" style="transition-delay:%dms">' % (i % 3 * 90) + pan(x, y, 523, 92) + num(x + 38, y + 37, i + 1)
                   + pic(N + ic, ix, iy, iw) + tt(x + 171, y + 9, t, 22, "color:#e8f2ff") + tx(x + 172, y + 36, s, 18, "line-height:1.3") + '</div>')
    return "".join(out[:3]) + "".join(out[3:])


HTML = CSS + tx(40, 128, "Broadcast-кадр отправляется во все порты, кроме входящего", 27, "color:#5fd0ff;white-space:nowrap") + f"""
<div class="step">
  {pic(N + "pc1.png", 58, 220, 194)}
  {lab(43, 366, 255, 39, "ПК-1 &nbsp;•&nbsp; 34:60:f9:5f:df:5f", 20)}
  <div class="fw-call" style="left:282px;top:190px;width:273px;height:138px"></div>
  {tt(300, 199, "ARP-ЗАПРОС", 25, "color:#ffb020")}
  {tx(300, 230, "SMAC: 34:60:f9:5f:df:5f<br>DMAC: ff:ff:ff:ff:ff:ff", 20, "line-height:1.3")}
  <div class="ab os" style="left:335px;top:287px;width:165px;height:33px;border-radius:4px;background:linear-gradient(180deg,#ff8a1f,#c45200);border:1.5px solid #ffc060;
    color:#fff;font-size:19px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 12px rgba(255,140,0,.8)">BROADCAST</div>
</div>
<div class="step">
  {svg(arrow(255, 345, 592, 345, "#ffb020", 4, 18))}
  {packets("M 258 345 L 585 345", "#ffc53d", 3, 2.0)}
  {pic(N + "sw.png", 596, 248, 514)}
  {blink(704, 311, 37, 36, "#ff9a1f")}
  {tx(622, 360, "1/0/1", 16)}{tx(695, 357, "1/0/2", 20, "font-weight:600")}{tx(832, 357, "• • •", 18)}
  {tx(953, 358, "1/0/6", 20)}{tx(1042, 358, "1/0/8", 20)}
</div>
<div class="step">
  {svg(arrow(722, 302, 745, 228, "#ff3b4e", 2.5, 12, dash=True))}
  <div class="fw-warn" style="left:782px;top:170px;width:238px;height:62px;font-size:19px;justify-content:flex-start;padding-left:26px;text-align:left">НЕ ВОЗВРАЩАЕТСЯ<br>ВО ВХОДЯЩИЙ ПОРТ</div>
  <div class="fw-x" style="left:764px;top:215px;width:36px;height:36px;font-size:22px">✕</div>
</div>
<div class="step">
  {svg(arrow(1100, 270, 1370, 152, BLUE, 4, 20) + arrow(1110, 328, 1382, 333, BLUE, 4, 20))}
  {blink(961, 311, 37, 36, BLUE, .3)}{blink(1051, 311, 37, 36, BLUE, .6)}
  {packets("M 1112 262 L 1350 160", "#3aa8ff", 3, 1.8, .4)}
  {packets("M 1120 326 L 1360 332", "#3aa8ff", 3, 1.8, .4)}
  {pic(N + "pc2.png", 1378, 93, 169)}{pic(N + "pc3.png", 1388, 263, 169)}
  {lab(1355, 207, 278, 40, "ПК-2 &nbsp;•&nbsp; a0:a3:f0:d1:26:5a", 20)}
  {lab(1357, 375, 276, 40, "ПК-3 &nbsp;•&nbsp; cc:4e:24:b1:11:00", 20)}
</div>
{_cards()}
<div class="step">
  {pan(20, 647, 525, 211)}{pic(N + "tb.png", 34, 654, 34)}{tt(76, 657, "ТАБЛИЦА КОММУТАЦИИ", 23)}
  {table(32, 697, [55, 163, 184, 99], [["VID", "MAC-адрес", "Интерфейс", "Тип"], ["1", "34:60:f9:5f:df:5f", "gigabitethernet 1/0/2", "Dynamic"],
     ["1", "a0:a3:f0:d1:26:5a", "gigabitethernet 1/0/6", "Dynamic"], ["1", "cc:4e:24:b1:11:00", "gigabitethernet 1/0/8", "Dynamic"]], [40, 39, 39, 39], 17, hsize=16)}
</div>
<div class="step">
  {pan(560, 647, 690, 211)}{pic(N + "doc.png", 573, 654, 36)}{tt(621, 658, "ПРЕОБРАЗОВАНИЕ КАДРА В КОММУТАТОРЕ", 22)}
  {pan(570, 697, 668, 153, "", "fw-sub")}
  {tt(580, 711, "ВХОДЯЩИЙ КАДР", 18, "color:#fff")}{tt(973, 711, "ИСХОДЯЩИЕ КАДРЫ", 18, "color:#fff")}
  {fields(740, 50, [("DMAC", 578, 625, "DMAC"), ("SMAC", 628, 672, "SMAC"), ("ET", 675, 717, "Ether<br>Type"), ("DATA", 720, 772, "Данные"), ("FCSR", 775, 817, "FCS")], 14)}
  {svg(arrow(822, 765, 848, 765, BLUE, 4, 12) + arrow(943, 765, 970, 765, BLUE, 4, 12))}
  <div class="fw-chipu" style="left:852px;top:725px;width:85px;height:82px;font-size:12px">Обработка<br>в коммутаторе</div>
  {fields(740, 50, [("DMAC", 974, 1022, "DMAC"), ("SMAC", 1025, 1070, "SMAC"), ("ET", 1073, 1117, "Ether<br>Type"), ("DATA", 1120, 1180, "Данные"), ("FCSG", 1183, 1228, "FCS")], 14)}
</div>
<div class="step">
  {pan(1263, 647, 389, 211)}{pic(N + "share.png", 1276, 654, 38)}{tt(1326, 660, "КУДА УХОДИТ КАДР", 22)}
  {pan(1275, 702, 366, 73, "", "fw-sub")}{pan(1275, 788, 366, 52, "", "fw-sub")}
  {tx(1290, 714, "1/0/6 → ПК-2: принимает и передаёт<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;сетевому стеку", 18)}
  {tx(1290, 803, "1/0/8 → ПК-3: принимает и обрабатывает", 17)}
</div>
{info(20, 873, 1632, 49, N + "info.png", 293, 44, "Широковещательный кадр реплицируется независимо от содержимого таблицы коммутации.", 366, 20)}
"""
