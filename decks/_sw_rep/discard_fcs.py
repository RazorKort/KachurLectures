# -*- coding: utf-8 -*-
"""Отбрасывание — ошибка контрольной суммы (pptx 29): вёрстка 1:1 + кадр доходит до порта и гаснет."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _fwkit import *

W, H, TOP = 1672, 941, 30
N = "discard_fcs_"

DCSS = """<style>
.df-die{position:absolute;left:0;top:0;width:30px;height:18px;border-radius:3px;background:#ffc53d;box-shadow:0 0 10px #ff9a1f;
  offset-path:path('M 735 266 L 860 266 L 860 290');animation:dfdie 2.6s linear infinite}
@keyframes dfdie{0%{offset-distance:0%;opacity:0;background:#ffc53d}10%{opacity:1}70%{offset-distance:100%;opacity:1;background:#ffc53d}
  80%{offset-distance:100%;background:#ff3b4e;transform:scale(1.4)}100%{offset-distance:100%;opacity:0;transform:scale(.2)}}
.df-cnt{animation:dfcnt 2.6s ease-in-out infinite}
@keyframes dfcnt{0%,70%{transform:scale(1)}80%{transform:scale(1.25)}100%{transform:scale(1)}}
</style>"""


def F(k, x0, x1, t, y=242, h=50, s=15):
    return fields(y, h, [(k, x0, x1, t)], s)


def C(x, n, ic, ix, iw, t, s, tx0, d, tcol=""):
    return ('<div class="step" style="transition-delay:%dms">' % d + pan(x, 392, {25: 397, 437: 391, 842: 393, 1250: 397}[x], 108)
            + num(x + 38, 437, n) + pic(N + ic, ix, 408, iw) + tt(tx0, 410, t, 22, tcol) + tx(tx0, 442, s, 17) + '</div>')


HTML = CSS + DCSS + tx(50, 120, "Повреждённый Ethernet-кадр не перрсылается дальше", 29, "color:#5fd0ff;white-space:nowrap") + f"""
<div class="step">
  {pic(N + "pc1.png", 43, 183, 174)}
  {lab(25, 318, 275, 39, "ПК-1 &nbsp;•&nbsp; 34:60:f9:5f:df:5f", 21)}
  <div class="fw-call" style="left:238px;top:236px;width:494px;height:62px;border-color:#ff9a1f"></div>
  {F("DMAC", 245, 297, "FCS", s=16)}{F("DATA", 300, 415, "Данные", s=16)}{F("ET", 419, 478, "Ether<br>Type")}
  {F("SMAC", 482, 600, '<span>SMAC<br><small style="font-size:12px">34:60:f9:5f:df:5f</small></span>')}
  {F("DMAC", 603, 722, '<span>DMAC<br><small style="font-size:12px">a0:a3:f0:d1:26:5a</small></span>')}
  {svg(arrow(732, 266, 764, 266, "#ffb020", 4, 14))}
</div>
<div class="step">
  <div class="fw-warn" style="left:300px;top:170px;width:320px;height:45px;font-size:21px">ПОМЕХА • БИТЫ ИСКАЖЕНЫ</div>
  {pic(N + "bolt.png", 266, 163, 46)}
  <div class="fw-warn" style="left:350px;top:300px;width:240px;height:92px;display:block;text-align:left;padding:2px 12px"></div>
  {tt(363, 303, "ПОВРЕЖДЁННЫЙ КАДР", 19, "color:#ff5a6a")}
  {tx(363, 328, "SMAC: 34:60:f9:5f:df:5f<br>DMAC: a0:a3:f0:d1:26:5a<br>FCS: значение от ПК-1", 17, "line-height:1.22")}
</div>
<div class="step">
  {pic(N + "sw.png", 763, 210, 439)}
  <div class="df-die"></div>
  {blink(843, 262, 37, 36, "#ff9a1f")}
  {tx(835, 306, "1/0/2", 21, "font-weight:600")}{tx(962, 306, "• • •", 18)}{tx(1063, 306, "1/0/6", 21)}{tx(1143, 306, "1/0/8", 21)}
  {svg('<line x1="862" y1="215" x2="862" y2="262" stroke="#ff3b4e" stroke-width="2.5" class="fw-dash"/>')}
  <div class="fw-warn" style="left:870px;top:177px;width:252px;height:40px;font-size:20px;padding-left:22px">FCS НЕ СОВПАЛ • DROP</div>
  {pic(N + "x.png", 850, 178, 42)}
</div>
<div class="step">
  {svg(arrow(1165, 212, 1412, 112, "#8a9ab8", 3, 14, dash=True, glow=False) + arrow(1205, 265, 1450, 302, "#8a9ab8", 3, 14, dash=True, glow=False))}
  <div class="fw-warn" style="left:1177px;top:95px;width:173px;height:32px;font-size:17px">НЕ ПЕРЕСЫЛАЕТСЯ</div>
  <div class="fw-warn" style="left:1260px;top:229px;width:173px;height:32px;font-size:17px">НЕ ПЕРЕСЫЛАЕТСЯ</div>
  {pic(N + "m1.png", 1356, 66, 51)}{pic(N + "m2.png", 1380, 275, 50)}
  {pic(N + "pc2.png", 1418, 33, 169)}{pic(N + "pc3.png", 1453, 208, 167)}
  {lab(1393, 148, 254, 36, "ПК-2 &nbsp;•&nbsp; a0:a3:f0:d1:26:5a", 19)}
  {lab(1378, 333, 269, 36, "ПК-3 &nbsp;•&nbsp; cc:4e:24:b1:11:00", 19)}
</div>
{C(25, 1, "i1.png", 108, 62, "STORE-AND-FORWARD", "Кадр полностью принят<br>в буфер порта 1/0/2", 186, 0)}
{C(437, 2, "i2.png", 530, 57, "CRC-32 / FCS CHECK", "Вычисленное значение<br>сравнивается с FCS кадра", 603, 90)}
{C(842, 3, "i3.png", 916, 68, "НЕСОВПАДЕНИЕ", "Контрольная сумма<br>не сходится • кадр повреждён", 998, 180, "color:#ff4d5e")}
{C(1250, 4, "i4.png", 1338, 64, "DROP", "Кадр удаляется<br>из входного буфера", 1428, 270)}
<div class="step">
  {pan(25, 512, 1622, 143)}{pic(N + "tb.png", 43, 520, 41)}{tt(97, 520, "ПРОВЕРКА ЦЕЛОСТНОСТИ", 27)}
  {fields(573, 57, [("DMAC", 48, 146, "DMAC"), ("SMAC", 149, 247, "SMAC"), ("ET", 250, 332, "Ether<br>Type"), ("DATA", 335, 455, "Данные"), ("FCSR", 458, 568, "FCS<br>ПОЛУЧЕН")], 19)}
  {svg(arrow(580, 598, 634, 598, BLUE, 5, 16) + arrow(795, 598, 842, 598, BLUE, 5, 16) + arrow(1258, 598, 1322, 598, BLUE, 5, 16) + arrow(1425, 598, 1468, 598, "#ff4d5e", 5, 16))}
  {packets("M 580 598 L 630 598", "#7fe0ff", 1, 1.0, 0, 14, 10)}
  <div class="fw-chipu" style="left:655px;top:557px;width:113px;height:76px;font-size:24px;font-family:Oswald,sans-serif">CRC-32</div>
  <div class="fw-warn" style="left:853px;top:556px;width:387px;height:86px;display:block"></div>
  {tt(880, 568, "FCS ПОЛУЧЕН &nbsp; <span style='font-size:30px;vertical-align:-4px'>≠</span> &nbsp; FCS ВЫЧИСЛЕН", 19, "color:#ff6a78")}
  <div class="ab os fw-pulse" style="left:856px;top:599px;width:381px;height:40px;background:rgba(150,10,25,.55);color:#ff5a6a;font-size:30px;text-align:center;line-height:40px">ОШИБКА</div>
  {pic(N + "trash.png", 1333, 543, 79)}
  {tt(1483, 560, "КАДР<br>ОТБРОШЕН", 28, "color:#ff4d5e")}
</div>
<div class="step">
  {pan(25, 667, 847, 193)}{pic(N + "tb2.png", 43, 675, 41)}{tt(95, 677, "САМ-ТАБЛИЦА", 26)}
  {table(37, 712, [68, 172, 193, 107], [["VID", "MAC-адрес", "Интерфейс", "Тип"], ["1", "34:60:f9:5f:df:5f", "gigabitethernet 1/0/2", "Dynamic"],
     ["1", "a0:a3:f0:d1:26:5a", "gigabitethernet 1/0/6", "Dynamic"], ["1", "cc:4e:24:b1:11:00", "gigabitethernet 1/0/8", "Dynamic"]], 33, 17)}
  <div class="fw-warn" style="left:593px;top:711px;width:265px;height:132px"></div>{pic(N + "ex.png", 601, 723, 49)}
  {tt(660, 722, "ЗАПИСЬ DMAC<br>НЕ ИМЕЕТ ЗНАЧЕНИЯ", 20, "color:#ff5a6a")}
  {tx(660, 775, "Повреждённый кадр<br>не продвигается", 18)}
</div>
<div class="step">
  {pan(885, 667, 396, 193)}{pic(N + "bar.png", 898, 673, 41)}{tt(950, 678, "СЧЁТЧИК ПОРТА 1/0/2", 23)}
  {pan(897, 712, 371, 138, "", "fw-sub")}
  {tx(897, 718, "CRC Errors / FCS Errors / Input Errors", 18, "width:371px;text-align:center;color:#8fd8ff")}
  <div class="ab" style="left:1010px;top:748px;width:147px;height:50px"><div class="fw-warn df-cnt" style="left:0;top:0;width:147px;height:50px;font-size:42px;color:#fff">+1</div></div>
  {tx(897, 803, "Ошибка фиксируется<br>аппаратным счётчиком", 17, "width:371px;text-align:center;line-height:1.2")}
</div>
<div class="step">
  {pan(1293, 667, 354, 193)}{pic(N + "nb.png", 1306, 671, 41)}{tt(1365, 678, "БЕЗ УВЕДОМЛЕНИЯ", 23)}
  {pan(1300, 718, 340, 132, "", "fw-sub")}{pic(N + "bell.png", 1308, 733, 86)}
  {tx(1407, 738, "Ethernet не подтверждает<br>доставку", 16, "line-height:1.25")}
  {tx(1407, 790, "ПК-1 не получает сообщение<br>об ошибке", 16, "line-height:1.25")}
</div>
{info(25, 872, 1622, 50, N + "info.png", 368, 45, "Кадр с неверным FCS отбрасывается молча и не попадает ни на один выходной порт.", 436, 20)}
"""
