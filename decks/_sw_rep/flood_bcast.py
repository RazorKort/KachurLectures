# -*- coding: utf-8 -*-
"""Лавинная передача — широковещательная рассылка (pptx 25): вёрстка 1:1 + полёт кадров."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _fwkit import *

W, H, TOP = 1672, 941, 60
N = "flood_bcast_"


def C(*a, **k):
    return step_card(N, *a, **k)


HTML = CSS + tx(45, 126, "Broadcast-кадр отправляется во все активные порты, кроме порта источника", 27, "color:#5fd0ff;white-space:nowrap") + f"""
<div class="step">
  {pic(N + "pc1.png", 45, 195, 192)}
  {lab(28, 344, 282, 38, "ПК-1 &nbsp;•&nbsp; 34:60:f9:5f:df:5f", 21)}
  <div class="fw-call" style="left:270px;top:180px;width:344px;height:118px"></div>
  {tt(287, 188, 'ARP-ЗАПРОС <span style="color:#ffe9b0">“КТО ИМЕЕТ IP...?”</span>', 21, "color:#ffb020")}
  {tx(287, 213, "SMAC: 34:60:f9:5f:df:5f<br>DMAC: ff:ff:ff:ff:ff:ff", 18, "line-height:1.3")}
  <div class="ab os" style="left:345px;top:264px;width:190px;height:30px;border-radius:4px;background:linear-gradient(180deg,#ff8a1f,#c45200);border:1.5px solid #ffc060;
    color:#fff;font-size:18px;display:flex;align-items:center;justify-content:center;box-shadow:0 0 12px rgba(255,140,0,.8)">BROADCAST</div>
</div>
<div class="step">
  {svg(arrow(236, 314, 636, 314, "#ffb020", 4, 18))}
  {packets("M 240 314 L 630 314", "#ffc53d", 3, 2.0)}
  {pic(N + "sw.png", 638, 238, 479)}
  {blink(727, 291, 36, 36, "#ff9a1f")}
  {tx(653, 340, "1/0/1", 17)}{tx(718, 336, "1/0/2", 21, "font-weight:600")}{tx(852, 336, "• • •", 18)}
  {tx(970, 338, "1/0/6", 20)}{tx(1053, 338, "1/0/8", 20)}
</div>
<div class="step">
  {svg(arrow(745, 292, 776, 212, "#ff3b4e", 2.5, 12, dash=True))}
  <div class="fw-x" style="left:784px;top:200px;width:34px;height:34px;font-size:22px">✕</div>
  <div class="fw-warn" style="left:805px;top:171px;width:243px;height:54px;font-size:19px">НЕ ВОЗВРАЩАЕТСЯ<br>В ПОРТ ИСТОЧНИКА</div>
</div>
<div class="step">
  {svg(arrow(1088, 252, 1378, 133, BLUE, 4, 20) + arrow(1112, 302, 1378, 318, BLUE, 4, 20))}
  {blink(983, 291, 36, 36, BLUE, .3)}{blink(1060, 291, 36, 36, BLUE, .6)}
  {packets("M 1100 246 L 1360 140", "#3aa8ff", 3, 1.8, .4)}
  {packets("M 1120 300 L 1360 316", "#3aa8ff", 3, 1.8, .4)}
  {pic(N + "pc2.png", 1383, 62, 189)}{pic(N + "pc3.png", 1388, 236, 186)}
  {lab(1349, 186, 294, 40, "ПК-2 &nbsp;•&nbsp; a0:a3:f0:d1:26:5a", 21)}
  {lab(1349, 353, 294, 40, "ПК-3 &nbsp;•&nbsp; cc:4e:24:b1:11:00", 21)}
</div>
{C(25, 403, 336, 126, 1, "i1.png", 92, 422, 60, "ОБУЧЕНИЕ (LEARNING)", "Кадр принят на 1/0/2 • FCS<br>подтверждает целостность", 160, 0)}
{C(372, 403, 304, 126, 2, "i2.png", 444, 425, 56, "ЗАПИСЬ SMAC", "34:60:f9:5f:df:5f<br>заносится в CAM-таблицу", 510, 90)}
{C(686, 403, 303, 126, 3, "i3.png", 744, 425, 48, "ОПРЕДЕЛЕНИЕ ТИПА", "ff:ff:ff:ff:ff:ff — Broadcast •<br>в таблицу не заносится", 805, 180)}
{C(999, 403, 357, 126, 4, "i4.png", 1072, 420, 65, "ПЕРЕСЧЁТ FCS", "Входной FCS отбрасывается •<br>на выходе рассчитывается<br>новый", 1146, 270, xsize=14)}
{C(1366, 403, 281, 126, 5, "i5.png", 1436, 424, 52, "FLOODING", "Во все активные<br>интерфейсы VLAN 1,<br>кроме 1/0/2", 1499, 360, xsize=14)}
{cam_ba(N)}
{fcs_proc(N)}
{where(N, ["1/0/6 &nbsp;→ &nbsp;ПК-2: принимает и обрабатывает", "1/0/8 &nbsp;→ &nbsp;ПК-3: принимает и обрабатывает"])}
{info(25, 878, 1622, 44, N + "info.png", 468, 44, "Широковещательный адрес никогда не заносится в CAM-таблицу.", 525, 20)}
"""
