# -*- coding: utf-8 -*-
"""Пересылка — известная одноадресная (pptx 28): вёрстка 1:1 + полёт кадра только в 1/0/6."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _fwkit import *

W, H, TOP = 1672, 941, 55
N = "forward_known_"


def C(*a, **k):
    return step_card(N, *a, **k)


PORTS = "".join(tx(x, 340, "1/0/%d" % (i + 1), 17, "font-weight:700;font-size:18px" if i in (1, 5) else "") for i, x in enumerate([624, 692, 754, 814, 873, 930, 993, 1050]))
FX = [("DMAC", 625, 705, "DMAC"), ("SMAC", 709, 796, "SMAC"), ("ET", 800, 886, "Ether<br>Type"), ("DATA", 890, 1000, "Данные")]

HTML = CSS + tx(45, 136, "Known Unicast: DMAC найден в CAM-таблице", 29, "color:#5fd0ff;white-space:nowrap") + f"""
<div class="step">
  {pic(N + "pc1.png", 45, 198, 192)}
  {lab(30, 343, 282, 39, "ПК-1 &nbsp;•&nbsp; 34:60:f9:5f:df:5f", 21)}
  <div class="fw-call" style="left:285px;top:187px;width:305px;height:116px"></div>
  {tt(303, 193, "ОДНОАДРЕСНЫЙ КАДР", 22, "color:#ffb020")}
  {tx(303, 220, "SMAC: 34:60:f9:5f:df:5f<br>DMAC: a0:a3:f0:d1:26:5a", 19, "line-height:1.3")}
  <div class="ab os" style="left:330px;top:272px;width:222px;height:29px;border-radius:4px;background:linear-gradient(180deg,#ff8a1f,#c45200);border:1.5px solid #ffc060;
    color:#fff;font-size:18px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 12px rgba(255,140,0,.8)">ТОЛЬКО К ПК-2</div>
</div>
<div class="step">
  {svg(arrow(236, 316, 610, 316, "#ffb020", 4, 18))}
  {packets("M 240 316 L 600 316", "#ffc53d", 3, 2.0)}
  {pic(N + "sw.png", 610, 223, 484)}
  {blink(701, 288, 40, 40, "#ff9a1f")}{PORTS}
</div>
<div class="step">
  {svg(arrow(1060, 240, 1376, 134, BLUE, 4, 20))}
  {blink(929, 288, 40, 40, BLUE, .3)}
  {packets("M 1072 236 L 1355 141", "#3aa8ff", 3, 1.8, .2)}
  {pic(N + "pc2.png", 1383, 56, 189)}
  {lab(1350, 182, 297, 40, "ПК-2 &nbsp;•&nbsp; a0:a3:f0:d1:26:5a", 21)}
</div>
<div class="step">
  {svg(arrow(1094, 293, 1386, 326, "#8a9ab8", 3, 14, dash=True, glow=False))}
  {pic(N + "x.png", 1205, 287, 47)}
  <div class="fw-warn" style="left:1110px;top:340px;width:232px;height:32px;font-size:17px">КАДР НЕ ОТПРАВЛЯЕТСЯ</div>
  {pic(N + "pc3.png", 1386, 233, 184)}
  {lab(1358, 350, 285, 40, "ПК-3 &nbsp;•&nbsp; cc:4e:24:b1:11:00", 21)}
</div>
{C(25, 402, 320, 135, 1, "i1.png", 93, 420, 67, "ПРИЁМ И FCS", "Кадр принят на 1/0/2 •<br>целостность<br>подтверждена", 165, 0, 22, 15, 26, 64)}
{C(355, 402, 317, 135, 2, "i2.png", 428, 423, 52, "ОБНОВЛЕНИЕ SMAC", "Запись 1/0/2 найдена •<br>aging timer перезапущен", 490, 90, 21, 15, 26, 64)}
{C(682, 402, 308, 135, 3, "i3.png", 758, 426, 52, "DMAC LOOKUP", "a0:a3:f0:d1:26:5a<br>найден на порту 1/0/6", 823, 180, 22, 15, 26, 64)}
{C(998, 402, 320, 135, 4, "i4.png", 1070, 420, 67, "ПЕРЕСЧЁТ FCS", "Входной FCS отброшен •<br>на выходе рассчитан<br>новый", 1145, 270, 22, 15, 26, 62)}
{C(1328, 402, 319, 135, 5, "i5.png", 1403, 426, 64, "FORWARDING", "Прямая пересылка<br>только через 1/0/6", 1476, 360, 22, 16, 26, 64)}
<div class="step">
  {pan(25, 550, 567, 312)}{pic(N + "tb.png", 44, 561, 40)}{tt(95, 563, "САМ-ТАБЛИЦА", 26)}
  {table(38, 606, [74, 176, 180, 110], [["VID", "MAC-адрес", "Интерфейс", "Тип"], ["1", "34:60:f9:5f:df:5f", "gigabitethernet 1/0/2", "Dynamic"],
     ["1", "a0:a3:f0:d1:26:5a", "gigabitethernet 1/0/6", "Dynamic"], ["1", "cc:4e:24:b1:11:00", "gigabitethernet 1/0/8", "Dynamic"]], [44, 42, 41, 42], 18, hl=(2,))}
  <div class="fw-ok fw-pulse" style="left:102px;top:795px;width:414px;height:55px;font-size:26px;padding-left:50px;color:#7dff9a">DMAC НАЙДЕН → 1/0/6</div>
  {pic(N + "find.png", 148, 798, 54)}
</div>
<div class="step">
  {pan(600, 550, 513, 312)}{pic(N + "doc.png", 620, 558, 42)}{tt(676, 563, "ПРОЦЕСС ОБРАБОТКИ FCS", 25)}
  {pan(613, 602, 487, 83, "", "fw-sub")}{tt(627, 605, "ВХОДЯЩИЙ КАДР", 17, "color:#fff")}
  {fields(632, 42, FX + [("FCSR", 1005, 1090, "FCS")], 17)}
  {svg(arrow(846, 676, 846, 702, BLUE, 5, 14) + arrow(846, 760, 846, 792, BLUE, 5, 14))}
  {packets("M 846 676 L 846 790", "#7fe0ff", 1, 1.6, 0, 14, 10)}
  <div class="fw-chipu" style="left:777px;top:701px;width:140px;height:59px;font-size:16px">Проверка •<br>FCS отброшен</div>
  {pan(613, 775, 487, 83, "", "fw-sub")}{tt(625, 778, "ИСХОДЯЩИЙ КАДР", 17, "color:#fff")}
  {fields(803, 43, FX + [("FCSG", 1005, 1090, "FCS")], 17)}
</div>
<div class="step">
  {pan(1125, 550, 522, 312)}{pic(N + "res.png", 1141, 558, 56)}{tt(1207, 565, "РЕЗУЛЬТАТ", 27)}
  {pan(1135, 615, 502, 153, "", "fw-sub")}
  <div class="fw-ok" style="left:1143px;top:628px;width:484px;height:57px"></div>{pic(N + "ck.png", 1152, 637, 46)}
  {tx(1212, 642, "1/0/6 &nbsp;→ &nbsp;<b>ПК-2:</b> кадр принят", 22, "color:#fff")}
  {pan(1143, 700, 484, 57, "", "fw-sub")}{pic(N + "cx.png", 1152, 707, 46)}
  {tx(1212, 713, "1/0/8 &nbsp;→ &nbsp;<b>ПК-3:</b> кадр не отправляется", 22)}
  {pan(1137, 787, 496, 63, "", "fw-sub")}{pic(N + "ban.png", 1192, 797, 50)}
  {tt(1255, 800, "БЕЗ ЛАВИННОЙ РАССЫЛКИ", 27, "color:#e8f2ff")}
</div>
{info(25, 877, 1622, 45, N + "info.png", 380, 44, "Известный одноадресный кадр пересылается только в порт, указанный в CAM-таблице.", 448, 20)}
"""
