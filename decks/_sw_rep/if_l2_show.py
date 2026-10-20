# -*- coding: utf-8 -*-
"""Интерфейсы L2: show interfaces status / show interfaces gi1/0/1 — вёрстка 1:1."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 180

CSS = """<style>
.ils-pan{position:absolute;border:2px solid #2ad4ff;border-radius:14px;background:rgba(6,22,60,.82);box-shadow:0 0 18px rgba(42,212,255,.55),inset 0 0 26px rgba(42,212,255,.12)}
.ils-term{position:absolute;border:1.5px solid rgba(42,212,255,.7);border-radius:8px;background:rgba(4,12,34,.9)}
.ils-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:34px;line-height:1;color:#fff;letter-spacing:.5px}
.ils-s{position:absolute;font-family:'Golos Text',sans-serif;font-size:23px;color:#e6f1ff}
.ils-cmd{position:absolute;font-family:'JetBrains Mono',monospace;font-size:24px;color:#fff;white-space:pre}
.ils-cmd i{font-style:normal;color:#2ad4ff;font-weight:600}
.ils-pre{position:absolute;font-family:'JetBrains Mono',monospace;font-size:18.5px;line-height:30px;color:#e6f1ff;white-space:pre;margin:0}
.ils-pre.b{font-size:17px;line-height:26px}
.ils-hr{position:absolute;height:1.5px;background:rgba(42,212,255,.45)}
.ils-bi{position:absolute;display:flex;align-items:center;gap:18px}
.ils-bi b{display:block;font-family:'Golos Text',sans-serif;font-weight:500;font-size:20px;color:#fff;line-height:1.25}
.ils-bi span{font-family:'Golos Text',sans-serif;font-size:18px;color:#cfe0ff}
.ils-sep{position:absolute;top:866px;width:2px;height:46px;background:rgba(160,180,230,.35)}
.ils-hl{position:absolute;border:3px solid #2ad4ff;border-radius:4px;box-shadow:0 0 16px #2ad4ff;animation:ilspulse 1.3s ease-in-out infinite}
@keyframes ilspulse{50%{box-shadow:0 0 4px #2ad4ff;opacity:.55}}
.ils-cur{display:inline-block;width:11px;height:22px;background:#2ad4ff;vertical-align:-3px;margin-left:4px;animation:ilscur 1s steps(2) infinite}
@keyframes ilscur{50%{opacity:0}}
</style>"""

ST = """Port      Type        Duplex  Speed  Link State   Uptime
--------- ----------- ------- ------ ------------ ------------
gi1/0/1   1G-Copper   Full    1000   Up           06,12:37:13
gi1/0/2   1G-Copper   Full    1000   Up           03,01:35:14
gi1/0/3   1G-Copper    --      --    Down (nc)         --
gi1/0/5   1G-Copper   Full    1000   Up           06,12:37:13"""

GI = """GigabitEthernet1/0/1 is up (connected)
 Interface index is 49
 Hardware is gigabitethernet, MAC address is e4:5a:d4:39:bc:e1
 Interface MTU is 1500
 Full-duplex, 1000Mbps, link type is auto, media type is 1G-Copper
 Link is up for 6 days, 11 hours, 51 minutes and 13 seconds
 Flow control is off, MDIX mode is normal"""

BOT = [("1G-Copper", "Порты 1–10", 78), ("Full/Half Duplex", "Режим передачи", 362), ("100/1000 Mbps", "Скорость", 684),
       ("Link State", "Состояние линии", 998), ("Uptime", "Время работы", 1312)]


def _bot():
    out = []
    for i, (a, b, x) in enumerate(BOT):
        out.append('<div class="ils-bi" style="left:%dpx;top:854px;transition-delay:%dms">%s<div><b>%s</b><span>%s</span></div></div>'
                   % (x, i * 90, img("rep/if_l2_show_b%d.png" % (i + 1), "width:78px"), a, b))
    return '<div class="step">%s%s</div>' % ("".join(out), "".join('<div class="ils-sep" style="left:%dpx"></div>' % x for x in (330, 650, 964, 1282)))


HTML = CSS + f"""
<div class="step">
  <div class="ils-pan" style="left:52px;top:190px;width:772px;height:362px"></div>
  {img("rep/if_l2_show_list.png", "left:70px;top:204px;width:76px", "ab")}
  <div class="ils-h" style="left:162px;top:205px">СОСТОЯНИЕ ВСЕХ ПОРТОВ</div>
  <div class="ils-s" style="left:162px;top:246px">Краткая информация о состоянии интерфейсов</div>
</div>
<div class="step">
  <div class="ils-term" style="left:68px;top:291px;width:740px;height:252px"></div>
  <div class="ils-cmd" style="left:86px;top:300px">switch# <i>show interfaces status</i><span class="ils-cur"></span></div>
  <div class="ils-hr" style="left:84px;top:338px;width:706px"></div>
  <pre class="ils-pre" style="left:86px;top:353px">{ST}</pre>
</div>

<div class="step">
  <div class="ils-pan" style="left:848px;top:190px;width:774px;height:362px"></div>
  {img("rep/if_l2_show_doc.png", "left:866px;top:204px;width:78px", "ab")}
  <div class="ils-h" style="left:960px;top:205px">ПАРАМЕТРЫ ОДНОГО ПОРТА</div>
  <div class="ils-s" style="left:960px;top:246px">Подробная информация о выбранном интерфейсе</div>
</div>
<div class="step">
  <div class="ils-term" style="left:864px;top:291px;width:742px;height:252px"></div>
  <div class="ils-cmd" style="left:882px;top:300px">switch# <i>show interfaces GigabitEthernet 1/0/1</i></div>
  <div class="ils-hr" style="left:880px;top:338px;width:710px"></div>
  <pre class="ils-pre b" style="left:882px;top:352px">{GI}</pre>
</div>

<div class="step">
  {img("rep/if_l2_show_sw.png", "left:140px;top:585px;width:1392px", "ab")}
  <svg class="ab" style="left:0;top:0;width:1672px;height:941px" viewBox="0 0 1672 941"><path d="M884 546L826 600V588" fill="none" stroke="#2ad4ff" stroke-width="2.5" style="filter:drop-shadow(0 0 4px #2ad4ff)"/></svg>
  <div class="ils-hl" style="left:792px;top:654px;width:74px;height:52px"></div>
</div>

<div class="step">
  <div class="ab" style="left:660px;top:792px;width:358px;height:42px;border:2px solid #2ad4ff;border-radius:8px;background:rgba(6,24,64,.92);box-shadow:0 0 14px rgba(42,212,255,.7);
    display:flex;align-items:center;justify-content:center;font-family:'Golos Text',sans-serif;font-size:21px;color:#fff"><b style="color:#2ad4ff;font-weight:600">InterfaceID</b>&nbsp;= тип + номер порта</div>
</div>

{_bot()}
"""
