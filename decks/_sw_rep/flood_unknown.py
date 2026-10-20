# -*- coding: utf-8 -*-
"""Лавинная передача — неизвестная одноадресная, DMAC нет в CAM (pptx 26): вёрстка 1:1 + полёт кадров."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _fwkit import *

W, H, TOP = 1672, 941, 55
N = "flood_unknown_"


def C(*a, **k):
    return step_card(N, *a, **k)


PORTS = "".join(tx(x, 342, "1/0/%d" % (i + 1), 16, "font-weight:600;font-size:19px" if i == 1 else "") for i, x in enumerate([646, 708, 770, 825, 878, 930, 993, 1050]))

HTML = CSS + tx(45, 126, "Unknown Unicast: DMAC отсутствует в CAM-таблице", 29, "color:#5fd0ff;white-space:nowrap") + f"""
<div class="step">
  {pic(N + "pc1.png", 45, 200, 192)}
  {lab(25, 343, 323, 39, "ПК-1 &nbsp;•&nbsp; VLAN 1 &nbsp;•&nbsp; 34:60:f9:5f:df:5f", 19)}
  <div class="fw-call" style="left:273px;top:178px;width:332px;height:119px"></div>
  {tt(291, 186, "ОДНОАДРЕСНЫЙ КАДР", 22, "color:#ffb020")}
  {tx(291, 212, "SMAC: 34:60:f9:5f:df:5f<br>DMAC: cc:4e:24:b1:11:00", 19, "line-height:1.3")}
</div>
<div class="step">
  {svg(arrow(236, 312, 628, 312, "#ffb020", 4, 18))}
  {packets("M 240 312 L 620 312", "#ffc53d", 3, 2.0)}
  {pic(N + "sw.png", 633, 238, 474)}
  {blink(718, 290, 37, 40, "#ff9a1f")}{PORTS}
</div>
<div class="step">
  {svg(arrow(740, 290, 772, 206, "#ff3b4e", 2.5, 12, dash=True))}
  <div class="fw-warn" style="left:808px;top:172px;width:237px;height:54px;font-size:19px">НЕ ОТПРАВЛЯЕТСЯ<br>В ПОРТ ИСТОЧНИКА</div>
  <div class="fw-x" style="left:784px;top:191px;width:34px;height:34px;font-size:22px">✕</div>
</div>
<div class="step">
  {svg(arrow(1075, 246, 1280, 130, BLUE, 4, 20) + arrow(1105, 312, 1292, 336, BLUE, 4, 20))}
  {blink(932, 290, 37, 40, BLUE, .3)}{blink(1052, 290, 37, 40, BLUE, .6)}
  {packets("M 1090 238 L 1265 139", "#3aa8ff", 3, 1.8, .4)}
  {packets("M 1115 312 L 1275 333", "#3aa8ff", 3, 1.8, .4)}
  {pic(N + "pc2.png", 1283, 63, 169)}{pic(N + "pc3.png", 1296, 243, 168)}
  {lab(1280, 188, 368, 39, "ПК-2 &nbsp;•&nbsp; VLAN 1 &nbsp;•&nbsp; a0:a3:f0:d1:26:5a", 20)}
  {lab(1288, 365, 360, 40, "ПК-3 &nbsp;•&nbsp; VLAN 1 &nbsp;•&nbsp; cc:4e:24:b1:11:00", 20)}
</div>
<div class="step">
  <div class="fw-warn" style="left:1478px;top:92px;width:184px;height:60px;font-size:17px;padding-left:22px">DMAC НЕ СОВПАЛ •<br>КАДР СБРОШЕН</div>
  {pic(N + "x.png", 1456, 98, 48)}
  <div class="fw-ok" style="left:1495px;top:268px;width:167px;height:60px;font-size:17px;padding-left:22px">DMAC СОВПАЛ •<br>КАДР ПРИНЯТ</div>
  {pic(N + "ok.png", 1468, 274, 52)}
</div>
{C(25, 412, 327, 123, 1, "i1.png", 92, 422, 60, "ПРИЁМ И FCS", "Кадр принят на 1/0/2 •<br>целостность подтверждена", 162, 0, 22, 15)}
{C(361, 412, 314, 123, 2, "i2.png", 440, 428, 56, "ПРОВЕРКА SMAC", "Запись уже есть •<br>aging timer обновлён", 500, 90, 22, 16)}
{C(684, 412, 301, 123, 3, "i3.png", 756, 432, 50, "ПОИСК DMAC", "cc:4e:24:b1:11:00<br>отсутствует в VLAN 1", 820, 180, 22, 16)}
{C(996, 412, 359, 123, 4, "i4.png", 1072, 422, 68, "ПЕРЕСЧЁТ FCS", "Входной FCS отброшен •<br>на выходе рассчитан<br>новый", 1148, 270, 22, 16, xy=56)}
{C(1363, 412, 284, 123, 5, "i5.png", 1436, 428, 56, "FLOODING", "Во все активные порты<br>VLAN 1, кроме 1/0/2", 1497, 360, 22, 15)}
<div class="step">
  {pan(25, 547, 832, 175)}{pic(N + "tb.png", 48, 553, 40)}{tt(98, 554, "САМ-ТАБЛИЦА ДО КАДРА", 25)}
  {table(40, 590, [93, 223, 266, 220], [["VID", "MAC-адрес", "Интерфейс", "Тип"], ["1", "34:60:f9:5f:df:5f", "gigabitethernet 1/0/2", "Dynamic"],
     ["1", "a0:a3:f0:d1:26:5a", "gigabitethernet 1/0/6", "Dynamic"]], [32, 33, 33], 19)}
  {tt(47, 691, "DMAC ПК-3 В ТАБЛИЦЕ НЕТ", 20, "color:#ffd23d")}
</div>
<div class="step">
  {pan(870, 547, 777, 175)}{pic(N + "tb2.png", 898, 553, 44)}{tt(958, 554, "ПОСЛЕ РАССЫЛКИ", 25)}
  {pan(883, 590, 750, 120, "", "fw-sub")}{pic(N + "eq.png", 896, 603, 102)}
  {tx(1015, 606, "Состав CAM-таблицы не изменился<br>Обновлён только таймер записи SMAC на 1/0/2<br>MAC ПК-3 не изучен: он был адресом назначения", 19, "line-height:1.8")}
</div>
{fcs_proc(N, 726, chip="Проверка •<br>FCS отброшен")}
{where(N, ["1/0/6 &nbsp;→ &nbsp;ПК-2: MAC не совпал &nbsp;→ &nbsp;сбрасывает", "1/0/8 &nbsp;→ &nbsp;ПК-3: MAC совпал &nbsp;→ &nbsp;принимает"], 726, 1125, 522)}
{info(25, 884, 1622, 42, N + "info.png", 488, 42, "Коммутатор изучает MAC источника, а не MAC назначения.", 550, 20)}
"""
