# -*- coding: utf-8 -*-
"""SWITCH_SEGMENTS — каждый порт коммутатора — отдельный сегмент (домен коллизий): вёрстка 1:1."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 186
P = "rep/switch_segments_"

CSS = """<style>
.ss-tag{position:absolute;border-radius:8px;border:2px solid;padding:2px 16px;font-family:"Golos Text",sans-serif;font-weight:600;font-size:24px;line-height:34px;background:rgba(10,14,30,.75)}
.ss-lb{position:absolute;font-family:"Golos Text",sans-serif;font-weight:600;font-size:23px;color:#fff}
.ss-card{position:absolute;top:728px;height:166px;border-radius:6px;border:2px solid rgba(42,212,255,.6);background:rgba(4,18,48,.82);box-shadow:0 0 14px rgba(42,212,255,.35)}
.ss-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:27px;letter-spacing:.6px;line-height:1}
.ss-t{position:absolute;color:#e6f1ff;font-size:23px;line-height:27px}
.ss-cab{fill:none;stroke-width:9;stroke-linecap:round}
.ss-flow{fill:none;stroke:#fff;stroke-width:3;stroke-dasharray:6 40;stroke-linecap:round;opacity:.85;animation:ss-run 1.6s linear infinite}
@keyframes ss-run{to{stroke-dashoffset:-46}}
</style>"""

BLOBS = """<svg class="ab" style="left:0;top:0" width="1672" height="941" viewBox="0 0 1672 941">
<path d="M70,215 C200,180 600,190 690,260 C740,300 730,350 660,380 C560,420 380,420 200,400 C40,385 10,250 70,215Z" fill="rgba(170,130,20,.2)" stroke="#ffc53d" stroke-width="2.5" style="filter:drop-shadow(0 0 8px #ffc53d)"/>
<path d="M60,485 C200,460 650,470 790,520 C820,560 760,640 600,672 C420,700 180,700 60,660 C0,620 0,510 60,485Z" fill="rgba(110,50,170,.2)" stroke="#b46bff" stroke-width="2.5" style="filter:drop-shadow(0 0 8px #b46bff)"/>
<path d="M1100,330 C1180,240 1400,190 1560,205 C1660,220 1660,420 1600,455 C1480,480 1300,470 1110,420 C1060,400 1070,360 1100,330Z" fill="rgba(20,90,170,.2)" stroke="#2a8cff" stroke-width="2.5" style="filter:drop-shadow(0 0 8px #2a8cff)"/>
<path d="M880,530 C1000,480 1400,470 1580,505 C1680,540 1660,680 1560,700 C1400,715 1100,700 960,640 C860,600 840,555 880,530Z" fill="rgba(20,130,130,.18)" stroke="#2ad4c8" stroke-width="2.5" style="filter:drop-shadow(0 0 8px #2ad4c8)"/>
</svg>"""

CABLES = [  # путь, цвет
    ("M398,345 C520,350 560,465 700,462", "#ffb52e"),
    ("M770,484 C760,560 620,575 356,566", "#2fd060"),
    ("M845,486 C870,585 1020,592 1252,592", "#a050ff"),
    ("M918,486 C960,540 1150,530 1250,330", "#2a7cff"),
]


def _cables():
    out = []
    for i, (d, c) in enumerate(CABLES):
        out.append('<svg class="ab step" style="left:0;top:0;transition-delay:%dms" width="1672" height="941" viewBox="0 0 1672 941">'
                   '<path class="ss-cab" d="%s" stroke="%s" style="filter:drop-shadow(0 0 6px %s)"/>'
                   '<path class="ss-flow" d="%s" style="animation-delay:%dms"/></svg>' % (i * 150, d, c, c, d, i * 300))
    return "".join(out)


HTML = CSS + f"""
<div class="step">{BLOBS}</div>
<div class="step">
  {img(P + "nb.png", "left:178px;top:205px;width:234px", "ab")}
  {img(P + "pc.png", "left:1238px;top:212px;width:274px", "ab")}
  {img(P + "srv.png", "left:132px;top:470px;width:230px", "ab")}
  {img(P + "prn.png", "left:1243px;top:505px;width:265px", "ab")}
  <div class="ss-lb" style="left:60px;top:280px">Ноутбук</div>
  <div class="ss-lb" style="left:1521px;top:280px">Компьютер</div>
  <div class="ss-lb" style="left:38px;top:580px">Сервер</div>
  <div class="ss-lb" style="left:1526px;top:577px">Принтер</div>
</div>
{_cables()}
<div class="step">
  {img(P + "sw.png", "left:560px;top:328px;width:532px", "ab")}
  <div class="ab" style="left:842px;top:224px;width:258px;height:76px;border-radius:8px;border:2px solid rgba(42,212,255,.6);background:rgba(6,20,52,.85)"></div>
  <div class="ss-lb" style="left:866px;top:231px;line-height:30px">Граница домена —<br>порт L2</div>
  <div class="ab" style="left:816px;top:300px;width:2px;height:46px;background:#2ad4ff;box-shadow:0 0 6px #2ad4ff"></div>
</div>
<div class="step">
  <div class="ss-tag" style="left:354px;top:246px;border-color:#ffc53d;color:#ffd04a;box-shadow:0 0 10px rgba(255,197,61,.6)">Домен коллизий 1</div>
  <div class="ss-tag" style="left:1368px;top:410px;border-color:#2ae8d0;color:#9ff;box-shadow:0 0 10px rgba(42,232,208,.6);transition-delay:.1s">Домен коллизий 2</div>
  <div class="ss-tag" style="left:376px;top:615px;border-color:#d07bff;color:#e3b4ff;box-shadow:0 0 10px rgba(208,123,255,.6)">Домен коллизий 3</div>
  <div class="ss-tag" style="left:984px;top:616px;border-color:#2ae8d0;color:#9ff;box-shadow:0 0 10px rgba(42,232,208,.6)">Домен коллизий 4</div>
</div>

<div class="step">
  <div class="ss-card" style="left:44px;width:514px"></div>
  {img(P + "ic1.png", "left:66px;top:752px;width:100px", "ab")}
  <div class="ss-h" style="left:194px;top:747px;color:#2ad4ff">ПРЯМОЕ ПОДКЛЮЧЕНИЕ</div>
  <div class="ss-t" style="left:194px;top:782px">Оконечные устройства<br>подключаются к коммутатору<br>без концентраторов.</div>
</div>
<div class="step">
  <div class="ss-card" style="left:578px;width:516px"></div>
  {img(P + "ic2.png", "left:608px;top:748px;width:100px", "ab")}
  <div class="ss-h" style="left:730px;top:747px;color:#c78bff">ИЗОЛЯЦИЯ КОЛЛИЗИЙ</div>
  <div class="ss-t" style="left:730px;top:782px;line-height:26.5px">В полудуплексном режиме<br>коллизия на одном порту<br>не распространяется<br>на другие.</div>
</div>
<div class="step">
  <div class="ss-card" style="left:1114px;width:514px"></div>
  {img(P + "ic3.png", "left:1138px;top:760px;width:102px", "ab")}
  <div class="ss-h" style="left:1270px;top:747px;color:#2ad4ff">ПОЛНЫЙ ДУПЛЕКС</div>
  <div class="ss-t" style="left:1270px;top:782px">В режиме full-duplex<br><b style="color:#2ad4ff">коллизий нет.</b></div>
</div>
"""
