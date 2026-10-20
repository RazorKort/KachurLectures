# -*- coding: utf-8 -*-
"""Лавинная передача — неизвестная одноадресная (pptx 27): вёрстка 1:1 + полёт кадров."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _fwkit import *

W, H, TOP = 1672, 941, 60
N = "flood_unknown2_"


def C(*a, **k):
    return step_card(N, *a, **k)


PORTS = "".join(tx(x, 343, "1/0/%d" % (i + 1), 16, "font-weight:600" if i == 1 else "") for i, x in enumerate([640, 700, 755, 808, 862, 915, 970, 1033]))

HTML = CSS + tx(45, 126, "Unknown Unicast: адрес назначения отсутствует в CAM-таблице", 27, "color:#5fd0ff;white-space:nowrap") + f"""
<div class="step">
  {pic(N + "pc1.png", 45, 198, 192)}
  {lab(30, 343, 280, 39, "ПК-1 &nbsp;•&nbsp; 34:60:f9:5f:df:5f", 21)}
  <div class="fw-call" style="left:265px;top:185px;width:303px;height:105px"></div>
  {tt(282, 193, "ОДНОАДРЕСНЫЙ КАДР", 21, "color:#ffb020")}
  {tx(282, 221, "SMAC: 34:60:f9:5f:df:5f<br>DMAC: cc:4e:24:b1:11:00", 19, "line-height:1.35")}
</div>
<div class="step">
  {svg(arrow(236, 310, 616, 310, "#ffb020", 4, 18))}
  {packets("M 240 310 L 610 310", "#ffc53d", 3, 2.0)}
  {pic(N + "sw.png", 620, 238, 467)}
  {blink(705, 292, 36, 38, "#ff9a1f")}{PORTS}
</div>
<div class="step">
  {svg(arrow(725, 290, 756, 206, "#ff3b4e", 2.5, 12, dash=True))}
  <div class="fw-x" style="left:766px;top:191px;width:34px;height:34px;font-size:22px">✕</div>
  <div class="fw-warn" style="left:787px;top:170px;width:245px;height:55px;font-size:19px">НЕ ОТПРАВЛЯЕТСЯ<br>ВО ВХОДЯЩИЙ ПОРТ</div>
</div>
<div class="step">
  {svg(arrow(1055, 246, 1306, 146, BLUE, 4, 20) + arrow(1086, 307, 1310, 332, BLUE, 4, 20))}
  {tx(1083, 234, "1/0/6", 20)}
  {blink(948, 292, 36, 38, BLUE, .3)}{blink(1035, 292, 36, 38, BLUE, .6)}
  {packets("M 1070 240 L 1290 152", "#3aa8ff", 3, 1.8, .4)}
  {packets("M 1095 308 L 1295 330", "#3aa8ff", 3, 1.8, .4)}
  {pic(N + "pc2.png", 1316, 78, 144)}{pic(N + "pc3.png", 1316, 250, 144)}
  {lab(1305, 191, 302, 40, "ПК-2 &nbsp;•&nbsp; a0:a3:f0:d1:26:5a", 21)}
  {lab(1305, 362, 302, 40, "ПК-3 &nbsp;•&nbsp; cc:4e:24:b1:11:00", 21)}
</div>
<div class="step">
  <div class="fw-warn" style="left:1460px;top:105px;width:188px;height:60px;font-size:16px;padding-left:36px">DMAC НЕ СОВПАЛ •<br>КАДР ОТБРОШЕН</div>
  {pic(N + "x.png", 1453, 115, 42)}
  <div class="fw-ok" style="left:1455px;top:275px;width:193px;height:62px;font-size:16px;padding-left:40px">DMAC СОВПАЛ •<br>КАДР ПРИНЯТ</div>
  {pic(N + "ok.png", 1453, 280, 47)}
</div>
{C(25, 407, 336, 126, 1, "i1.png", 92, 422, 60, "ОБУЧЕНИЕ (LEARNING)", "Кадр принят на 1/0/2 • FCS<br>подтверждает целостность", 157, 0)}
{C(370, 407, 305, 126, 2, "i2.png", 446, 426, 56, "ЗАПИСЬ SMAC", "MAC источника<br>привязан к 1/0/2<br>в VLAN 1", 520, 90)}
{C(683, 407, 305, 126, 3, "i3.png", 750, 426, 46, "ПОИСК (LOOKUP)", "DMAC cc:4e:24:b1:11:00<br>в таблице отсутствует", 810, 180)}
{C(997, 407, 338, 126, 4, "i4.png", 1072, 420, 65, "ПЕРЕСЧЁТ FCS", "Входной FCS отброшен •<br>на выходе рассчитан<br>новый", 1148, 270)}
{C(1343, 407, 304, 126, 5, "i5.png", 1418, 426, 54, "FLOODING", "Во все активные порты<br>VLAN 1, кроме 1/0/2", 1485, 360)}
{cam_ba(N)}
{fcs_proc(N, chip="Проверка •<br>FCS отброшен")}
{where(N, ["1/0/6 &nbsp;→ &nbsp;ПК-2: MAC не совпал → отбрасывает", "1/0/8 &nbsp;→ &nbsp;ПК-3: MAC совпал → принимает"])}
{info(25, 876, 1622, 44, N + "info.png", 418, 44, "Коммутатор изучает MAC источника; MAC назначения в таблицу не добавляется.", 476, 20)}
"""
