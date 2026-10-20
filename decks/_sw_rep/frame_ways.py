# -*- coding: utf-8 -*-
"""Способы обработки кадров коммутатором (pptx 23): вёрстка 1:1 + полёт кадров в трёх панелях."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _fwkit import *

W, H, TOP = 1672, 941, 85
N = "frame_ways_"
GR, PK, GREY = "#3ee8a8", "#ff4d7a", "#8a9ab8"

FCSS = """<style>
.fwy-p{position:absolute;border-radius:10px;border:3px solid var(--c);background:rgba(4,18,48,.82);box-shadow:0 0 22px var(--c),inset 0 0 30px rgba(0,0,0,.3)}
.fwy-n{position:absolute;width:66px;height:66px;border-radius:50%;border:4px solid var(--c);box-shadow:0 0 16px var(--c);color:var(--c);
  font-family:Oswald,sans-serif;font-weight:600;font-size:44px;display:flex;align-items:center;justify-content:center}
.fwy-l{position:absolute;border-radius:10px;border:2px solid var(--c);background:rgba(4,18,48,.92);box-shadow:0 0 10px var(--c);color:#fff;
  font-size:20px;line-height:1.2;text-align:center;display:flex;align-items:center;justify-content:center}
</style>"""


def P(x, w, c, n, title, text, delay):
    return ('<div class="step" style="--c:%s;transition-delay:%dms"><div class="fwy-p" style="left:%dpx;top:310px;width:%dpx;height:490px"></div>'
            '<div class="fwy-n" style="left:%dpx;top:322px">%d</div>' % (c, delay, x, w, x + 22, n)
            + tt(x + 118, 330, title, 36, "color:%s;font-weight:600;text-shadow:0 0 10px %s" % (c, c))
            + tx(x + 118, 380, text, 21, "line-height:1.2") + '</div>')


HTML = CSS + FCSS + f"""
<div class="step">
  {pan(85, 92, 1503, 68)}{pic(N + "book.png", 103, 103, 74)}
  <div class="ab" style="left:191px;top:106px;width:3px;height:40px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff"></div>
  {tx(218, 110, "Коммутатор обрабатывает кадры тремя способами: лавинная передача, пересылка и отбрасывание.", 24, "font-weight:600;white-space:nowrap")}
  {pic(N + "sw.png", 523, 193, 621)}
</div>
{P(22, 543, BLUE, 1, "1. ЛАВИННАЯ ПЕРЕДАЧА", "Кадр поступает на один интерфейс<br>и передаётся через все остальные<br>интерфейсы.", 0)}
<div class="step">
  {pic(N + "l1.png", 68, 460, 89)}{pic(N + "s1.png", 96, 546, 396)}{pic(N + "b1.png", 48, 698, 494)}
  {svg(poly([(157, 497), (205, 497), (205, 558)], BLUE, 3, 14) + arrow(200, 612, 96, 696, BLUE, 3, 16) + arrow(203, 612, 203, 698, BLUE, 3, 16)
       + arrow(222, 612, 292, 696, BLUE, 3, 16) + arrow(232, 612, 363, 696, BLUE, 3, 16, dash=True))}
  {pic(N + "f1.png", 222, 500, 58)}
  {packets("M 160 497 L 205 497 L 205 550", "#7fe0ff", 1, 2.2, 0, 18, 11)}
  {packets("M 200 615 L 100 692", "#7fe0ff", 1, 2.2, 1.1, 18, 11)}{packets("M 203 615 L 203 690", "#7fe0ff", 1, 2.2, 1.1, 18, 11)}
  {packets("M 222 615 L 288 690", "#7fe0ff", 1, 2.2, 1.1, 18, 11)}{packets("M 232 615 L 358 690", "#7fe0ff", 1, 2.2, 1.1, 18, 11)}
  <div class="fwy-l" style="--c:{BLUE};left:357px;top:625px;width:195px;height:62px">Во все порты,<br>кроме входного</div>
</div>
{P(578, 517, GR, 2, "2. ПЕРЕСЫЛКА", "Кадр поступает на один интерфейс<br>и направляется только через нужный<br>интерфейс.", 0)}
<div class="step">
  {pic(N + "l2.png", 624, 460, 88)}{pic(N + "s2.png", 653, 546, 382)}{pic(N + "b2.png", 603, 698, 474)}
  {svg(poly([(712, 497), (760, 497), (760, 558)], GR, 3, 14) + arrow(815, 612, 815, 698, GR, 3, 16)
       + arrow(700, 616, 655, 696, GREY, 2, 12, dash=True, glow=False) + arrow(748, 616, 742, 696, GREY, 2, 12, dash=True, glow=False)
       + arrow(868, 680, 882, 698, GREY, 2, 12, dash=True, glow=False) + arrow(990, 684, 1000, 698, GREY, 2, 12, dash=True, glow=False))}
  {pic(N + "f2.png", 777, 500, 59)}
  {packets("M 715 497 L 760 497 L 760 550", "#7dffc8", 1, 2.2, 0, 18, 11)}{packets("M 815 615 L 815 690", "#7dffc8", 1, 2.2, 1.1, 18, 11)}
  <div class="fwy-l" style="--c:{GR};left:847px;top:630px;width:231px;height:53px">Только в нужный порт</div>
</div>
{P(1107, 543, PK, 3, "3. ОТБРАСЫВАНИЕ", "Кадр, полученный на интерфейсе,<br>не передаётся дальше и удаляется.", 0)}
<div class="step">
  {pic(N + "l3.png", 1158, 460, 84)}{pic(N + "s3.png", 1183, 546, 384)}{pic(N + "b3.png", 1143, 698, 489)}
  {svg(poly([(1242, 497), (1297, 497), (1297, 558)], PK, 3, 14)
       + arrow(1285, 620, 1200, 696, GREY, 2, 12, dash=True, glow=False) + arrow(1335, 620, 1320, 696, GREY, 2, 12, dash=True, glow=False)
       + arrow(1375, 620, 1416, 696, GREY, 2, 12, dash=True, glow=False) + arrow(1435, 620, 1530, 696, GREY, 2, 12, dash=True, glow=False))}
  {pic(N + "f3.png", 1312, 500, 58)}
  <div class="df" style="position:absolute;left:0;top:0">{packets("M 1245 497 L 1297 497 L 1297 572", "#ff7a9a", 1, 1.6, 0, 18, 11)}</div>
  <div class="fwy-l fw-pulse" style="--c:{PK};left:1405px;top:483px;width:202px;height:54px">Кадр удаляется</div>
</div>
<div class="step">
  {pan(22, 825, 1626, 80)}{pic(N + "bulb.png", 122, 832, 60)}
  <div class="ab" style="left:213px;top:845px;width:3px;height:42px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff"></div>
  {tx(252, 846, "Способ обработки зависит от MAC-адреса назначения и данных таблицы коммутации.", 27, "font-weight:600;white-space:nowrap")}
</div>
"""
