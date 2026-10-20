# -*- coding: utf-8 -*-
"""SWITCH_HOW — как работает коммутатор (обучение MAC и пересылка): вёрстка 1:1 инфографики."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 203
P = "rep/switch_how_"

CSS = """<style>
.sh-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;letter-spacing:.8px;line-height:1}
.sh-t{position:absolute;color:#e6f1ff;font-size:19px;line-height:22px}
.sh-g{font-family:"Golos Text",sans-serif!important}
.sh-m{font-family:'JetBrains Mono',monospace}
.sh-box{position:absolute;border-radius:8px;border:2.5px solid #2ad4ff;background:rgba(6,30,80,.82);box-shadow:0 0 16px rgba(42,212,255,.6),inset 0 0 18px rgba(42,212,255,.15)}
.sh-box.v{border-color:#9b6bff;background:rgba(40,20,100,.82);box-shadow:0 0 16px rgba(155,107,255,.65),inset 0 0 18px rgba(155,107,255,.18)}
.sh-box.m{border-color:#e05cff;background:rgba(70,10,80,.82);box-shadow:0 0 16px rgba(224,92,255,.65),inset 0 0 18px rgba(224,92,255,.18)}
.sh-hex{position:absolute;width:64px;height:70px;clip-path:polygon(50% 0,100% 25%,100% 75%,50% 100%,0 75%,0 25%);background:#cfefff;
  display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:700;font-size:44px;color:#fff}
.sh-hex::before{content:"";position:absolute;inset:3px;clip-path:inherit;background:#0b1f4a;z-index:-1}
.sh-hex{isolation:isolate}
.sh-arr{position:absolute;color:#cfefff;font-size:40px;line-height:1;text-shadow:0 0 8px #2ad4ff}
.sh-tb{position:absolute;border-collapse:collapse;font-size:21px;color:#fff}
.sh-tb td{border:1.5px solid rgba(42,212,255,.7);padding:0 14px;height:36px}
.sh-pkt{position:absolute;left:530px;top:304px;width:46px;height:16px;border-radius:4px;background:#2ad4ff;box-shadow:0 0 12px #2ad4ff;opacity:0;animation:sh-fly 2.6s 1s infinite}
@keyframes sh-fly{0%{opacity:0;transform:translateX(0)}15%{opacity:1}85%{opacity:1;transform:translateX(100px)}100%{opacity:0;transform:translateX(100px)}}
.sh-row{animation:sh-new 3s 1.5s infinite}
@keyframes sh-new{0%,100%{background:transparent}20%,50%{background:rgba(42,212,255,.25)}}
.sh-ln{fill:none;stroke:#2ad4ff;stroke-width:2.5;filter:drop-shadow(0 0 4px #2ad4ff)}
</style>"""

PCS = [("A", "AA:AA:AA:AA:AA:01", 512), ("B", "BB:BB:BB:BB:BB:02", 676), ("C", "CC:CC:CC:CC:CC:03", 836),
       ("D", "DD:DD:DD:DD:DD:04", 997), ("E", "EE:EE:EE:EE:EE:05", 1164)]


def _pcs():
    out = []
    for i, (n, mac, x) in enumerate(PCS):
        out.append(img(P + "pc%d.png" % (i + 1), "left:%dpx;top:400px;width:104px" % (464 + i * 160), "ab"))
        out.append('<div class="sh-h sh-g" style="left:%dpx;top:476px;width:200px;text-align:center;font-size:16px;font-weight:600;letter-spacing:0;color:#2ad4ff">Устройство %s</div>' % (x - 100, n))
        out.append('<div class="sh-t" style="left:%dpx;top:494px;width:200px;text-align:center;font-size:12px">MAC: %s</div>' % (x - 100, mac))
    return "".join(out)


LINES = """<svg class="ab" style="left:0;top:0" width="1672" height="941" viewBox="0 0 1672 941">
<path class="sh-ln" d="M682,356 V382 H568 V412"/><circle cx="568" cy="412" r="4" fill="#2ad4ff"/>
<path class="sh-ln" d="M758,356 V382 H728 V412"/><circle cx="728" cy="412" r="4" fill="#2ad4ff"/>
<path class="sh-ln" d="M835,356 V404"/><path d="M828,398 L835,410 L842,398Z" fill="#2ad4ff"/>
<path class="sh-ln" d="M912,356 V382 H942 V412"/><circle cx="942" cy="412" r="4" fill="#2ad4ff"/>
<path class="sh-ln" d="M988,356 V382 H1100 V412"/><circle cx="1100" cy="412" r="4" fill="#2ad4ff"/>
<path class="sh-ln" d="M1080,290 H1140 M1140,272 V308"/>
</svg>"""

CARDS = """<svg class="ab" style="left:0;top:0" width="1672" height="941" viewBox="0 0 1672 941">
<path class="sh-ln" d="M1390,630 V655 H290 V662"/><path class="sh-ln" d="M838,655 V662" style="stroke:#9b6bff"/><path class="sh-ln" d="M1374,655 V662" style="stroke:#e05cff"/>
</svg>"""


def _case(x, w, cls, color, title, sub, mimg, mw, bottom, d):
    return ('<div class="step" style="transition-delay:%dms"><div class="sh-box %s" style="left:%dpx;top:662px;width:%dpx;height:220px"></div>'
            '<div class="sh-h" style="left:%dpx;top:676px;width:%dpx;text-align:center;font-size:25px;color:%s">%s</div>'
            '<div class="sh-t" style="left:%dpx;top:704px;width:%dpx;text-align:center;font-size:18px">%s</div>%s'
            '<div class="sh-t" style="left:%dpx;top:846px;width:%dpx;text-align:center;font-size:21px">%s</div></div>'
            % (d, cls, x, w, x, w, color, title, x, w, sub, img(P + mimg, "left:%dpx;top:728px;width:%dpx" % (x + (w - mw) // 2, mw), "ab"),
               x, w, bottom))


HTML = CSS + f"""
<div class="step">
  <div class="sh-h" style="left:600px;top:207px;width:480px;text-align:center;font-size:26px;color:#2ad4ff">КОММУТАТОР</div>
  {img(P + "sw.png", "left:592px;top:236px;width:490px", "ab")}
  {LINES}
  {_pcs()}
</div>

<div class="step">
  {img(P + "pca.png", "left:60px;top:252px;width:136px", "ab")}
  <div class="sh-h" style="left:72px;top:353px;font-size:18px;font-weight:500;color:#2ad4ff">Устройство A</div>
  <div class="sh-t" style="left:47px;top:375px;font-size:15px">MAC: AA:AA:AA:AA:AA:01</div>
  <div class="ab" style="left:190px;top:309px;width:40px;height:3px;background:#2ad4ff;box-shadow:0 0 6px #2ad4ff"></div>
  <div class="sh-box" style="left:228px;top:266px;width:302px;height:86px;border-radius:10px"></div>
  <div class="sh-h" style="left:246px;top:274px;font-size:20px;font-weight:600;color:#2ad4ff;letter-spacing:0;font-family:'Golos Text',sans-serif">Ethernet кадр</div>
  <div class="sh-t" style="left:246px;top:300px;font-size:17px;line-height:25px">Источник:&nbsp; AA:AA:AA:AA:AA:01<br>Назначение:&nbsp; BB:BB:BB:BB:BB:02</div>
  <div class="ab" style="left:530px;top:310px;width:96px;height:3px;background:#2ad4ff;box-shadow:0 0 6px #2ad4ff"></div>
  <div class="sh-arr" style="left:614px;top:290px">&#9658;</div>
  <div class="sh-pkt"></div>
</div>

<div class="step">
  <div class="sh-box" style="left:1155px;top:220px;width:365px;height:162px;border-radius:6px"></div>
  <div class="sh-h" style="left:1155px;top:228px;width:365px;text-align:center;font-size:24px;color:#2ad4ff">MAC-ТАБЛИЦА</div>
  <table class="sh-tb" style="left:1167px;top:260px;width:341px"><tr style="font-weight:600"><td style="text-align:center">MAC-адрес</td><td style="text-align:center">Порт</td></tr>
    <tr><td>AA:AA:AA:AA:AA:01</td><td style="text-align:center">1</td></tr>
    <tr class="sh-row"><td>BB:BB:BB:BB:BB:02</td><td style="text-align:center">2</td></tr></table>
</div>

<div class="step">
  <div class="sh-box" style="left:50px;top:520px;width:452px;height:108px"></div>
  <div class="sh-hex" style="left:74px;top:540px">1</div>
  <div class="sh-h" style="left:160px;top:538px;font-size:31px;color:#2ad4ff">ПРИЁМ КАДРА</div>
  <div class="sh-t" style="left:160px;top:574px;font-size:18px">Коммутатор считывает<br>MAC источника и назначения</div>
  {img(P + "doc.png", "left:422px;top:540px;width:60px", "ab")}
  <div class="sh-arr" style="left:510px;top:556px">&#10140;</div>
</div>
<div class="step">
  <div class="sh-box v" style="left:558px;top:520px;width:557px;height:108px"></div>
  <div class="sh-hex" style="left:582px;top:540px">2</div>
  <div class="sh-h" style="left:666px;top:538px;font-size:31px;color:#c8a8ff">ОБУЧЕНИЕ</div>
  {img(P + "db.png", "left:882px;top:532px;width:42px", "ab")}
  <div class="sh-t" style="left:666px;top:574px;font-size:18px">MAC источника нет в таблице?<br>Записать его и номер входного порта</div>
  <div class="ab" style="left:938px;top:536px;width:166px;height:56px;border-radius:7px;border:1.5px solid rgba(42,212,255,.7);background:rgba(10,30,80,.8)"></div>
  <div class="sh-t" style="left:938px;top:545px;width:166px;text-align:center;font-size:14px;line-height:19px">Изучение MAC-адреса<br>на порту</div>
  <div class="sh-arr" style="left:1118px;top:556px">&#10140;</div>
</div>
<div class="step">
  <div class="sh-box m" style="left:1165px;top:520px;width:455px;height:108px"></div>
  <div class="sh-hex" style="left:1190px;top:540px">3</div>
  <div class="sh-h" style="left:1278px;top:558px;font-size:31px;color:#fff">ВЫБОР НАПРАВЛЕНИЯ</div>
</div>

<div class="step">{CARDS}</div>
{_case(50, 505, "", "#2ad4ff", "BROADCAST / MULTICAST", "FF:FF:FF:FF:FF:FF или 01:xx:xx:xx:xx:xx", "m1.png", 420, "Во все порты, кроме входного", 0)}
{_case(572, 524, "v", "#c8a8ff", "ИЗВЕСТНЫЙ UNICAST", "MAC назначения найден в таблице", "m2.png", 440, "Только в указанный порт", 150)}
{_case(1113, 507, "m", "#ff7ff0", "UNKNOWN UNICAST", "MAC назначения не найден", "m3.png", 390, "Во все порты, кроме входного", 300)}

<div class="step">
  <div class="ab" style="left:1327px;top:897px;width:313px;height:32px;border-radius:6px;border:1.5px solid rgba(42,212,255,.6);background:rgba(4,16,44,.8)"></div>
  <div class="sh-t" style="left:1327px;top:903px;width:313px;text-align:center;font-size:15px">x0:xx:xx:xx:xx:xx — одноадресный