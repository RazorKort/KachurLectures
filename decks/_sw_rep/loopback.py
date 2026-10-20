# -*- coding: utf-8 -*-
"""Интерфейсы обратной петли Loopback — вёрстка 1:1."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 92

CSS = """<style>
.lbk-pan{position:absolute;border:2px solid #2ad4ff;border-radius:12px;background:rgba(6,22,60,.72);box-shadow:0 0 14px rgba(42,212,255,.45),inset 0 0 22px rgba(42,212,255,.1)}
.lbk-it{position:absolute;left:36px;width:384px;height:94px;border:1.5px solid rgba(42,212,255,.5);border-radius:8px;background:rgba(8,28,72,.6);
  display:flex;align-items:center;gap:24px;padding-left:20px;box-sizing:border-box;font-family:'Golos Text',sans-serif;font-size:22px;line-height:1.3;color:#fff}
.lbk-ex{position:absolute;top:702px;height:88px;border:1.5px solid rgba(42,212,255,.55);border-radius:8px;background:rgba(8,28,72,.6);
  display:flex;align-items:center;gap:26px;padding-left:28px;box-sizing:border-box;font-family:Oswald,sans-serif;font-weight:500;font-size:21px;line-height:1.2;color:#fff}
.lbk-term{position:absolute;font-family:'JetBrains Mono',monospace;color:#e6f1ff;white-space:pre;margin:0}
.lbk-lab{position:absolute;font-family:Oswald,sans-serif;font-size:18px;line-height:1.2;color:#fff;text-align:center}
.lbk-dots path{fill:none;stroke:#2ad4ff;stroke-width:3;stroke-dasharray:6 6;animation:lbkd 1s linear infinite}
@keyframes lbkd{to{stroke-dashoffset:-24}}
.lbk-spin{animation:lbkglow 2.4s ease-in-out infinite}
@keyframes lbkglow{50%{filter:brightness(1.35) drop-shadow(0 0 10px #2ad4ff)}}
.lbk-hl{position:absolute;border:2px solid #b07bff;border-radius:6px;box-shadow:0 0 14px #b07bff;animation:lbkhl 1.6s ease-in-out infinite}
@keyframes lbkhl{50%{box-shadow:0 0 3px #b07bff}}
</style>"""

ITEMS = [("Создаётся<br>пользователем", 205), ("Всегда находится<br>в состоянии UP", 309),
         ("IP-адрес имеет<br>префикс <b style='color:#b07bff;font-weight:600'>/32</b>", 413), ("Не зависит от состояния<br>физических портов", 517)]

TBL = """IP Address         I/F         I/F Status  Type     Status
------------------ ----------- ----------- -------- ------"""


def _items():
    return "".join('<div class="lbk-it step" style="top:%dpx">%s<div>%s</div></div>' % (y, img("rep/loopback_l%d.png" % (i + 1), "width:68px"), t)
                   for i, (t, y) in enumerate(ITEMS))


HTML = CSS + f"""
<div class="lbk-pan" style="left:20px;top:192px;width:416px;height:432px"></div>
{_items()}

<div class="step">
  {img("rep/loopback_scene.png", "left:455px;top:262px;width:637px;-webkit-mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent);mask-image:linear-gradient(90deg,transparent,#000 8%,#000 92%,transparent)", "ab")}
  {img("rep/loopback_inf.png", "left:470px;top:190px;width:590px;-webkit-mask-image:radial-gradient(ellipse 50% 50% at 50% 50%,#000 75%,transparent 100%);mask-image:radial-gradient(ellipse 50% 50% at 50% 50%,#000 75%,transparent 100%)", "ab lbk-spin")}
  <div class="ab" style="left:670px;top:144px;width:232px;height:118px;border:2px solid #2ad4ff;border-radius:10px;background:rgba(6,24,64,.92);box-shadow:0 0 16px rgba(42,212,255,.7);
    text-align:center;font-family:Oswald,sans-serif;font-weight:500;line-height:1.2;color:#fff">
    <div style="font-size:23px;margin-top:8px">LOOPBACK 1</div><div style="font-size:33px;color:#c89bff">8.8.8.8/32</div><div style="font-size:30px;color:#2ad4ff">UP/UP</div></div>
  <div class="ab" style="left:780px;top:262px;width:3px;height:196px;background:#9ff0ff;box-shadow:0 0 8px #2ad4ff"></div>
</div>

<div class="step">
  <div class="ab" style="left:1000px;top:96px;width:148px;height:90px;border:2px dashed #2ad4ff;border-radius:10px;background:rgba(6,24,64,.75);
    font-family:Oswald,sans-serif;font-size:17px;line-height:1.3;color:#fff;padding:12px 0 0 20px;box-sizing:border-box">ЛОГИЧЕСКИЙ<br>ИНТЕРФЕЙС<br>УСТРОЙСТВА</div>
  <svg class="ab" style="left:0;top:0;width:1672px;height:941px" viewBox="0 0 1672 941"><path d="M998 134H974L922 188" fill="none" stroke="#2ad4ff" stroke-width="1.5"/><circle cx="922" cy="188" r="4" fill="#2ad4ff"/></svg>
</div>

<div class="step">
  <div class="lbk-pan" style="left:1088px;top:204px;width:570px;height:294px"></div>
  <div class="lbk-term" style="left:1108px;top:234px;font-size:21px;color:#fff">switch# <b style="color:#2ad4ff;font-weight:600">show ip interfaces</b></div>
  <pre class="lbk-term" style="left:1108px;top:290px;font-size:15.5px;line-height:24px">{TBL}</pre>
  <div class="lbk-hl" style="left:1098px;top:342px;width:548px;height:36px;background:rgba(40,20,100,.55)"></div>
  <pre class="lbk-term" style="left:1108px;top:340px;font-size:15.5px;line-height:39px"><span style="color:#c89bff">8.8.8.8/32         loopback 1</span>  <span style="color:#9ff0ff">UP/UP</span>       Static   <span style="color:#ffc53d">Valid</span>
10.10.1.1/24       vlan 1      UP/UP       Static   Valid
192.168.20.254/24  gi1/0/1     UP/UP       Static   Valid</pre>
</div>

<div class="step">
  <svg class="ab lbk-dots" style="left:0;top:0;width:1672px;height:941px" viewBox="0 0 1672 941">
    <path d="M1200 668H1282"/><path d="M1446 668H1526"/><path d="M1363 600V644"/>
  </svg>
  {img("rep/loopback_db.png", "left:1116px;top:618px;width:72px", "ab")}
  {img("rep/loopback_ci.png", "left:1310px;top:542px;width:106px", "ab")}
  {img("rep/loopback_sw3.png", "left:1292px;top:642px;width:142px", "ab")}
  {img("rep/loopback_srv.png", "left:1538px;top:634px;width:68px", "ab")}
  <div class="lbk-lab" style="left:1100px;top:694px;width:104px">VLAN<br>(SVI)</div>
  <div class="lbk-lab" style="left:1290px;top:716px;width:146px">L3 SWITCH</div>
  <div class="lbk-lab" style="left:1500px;top:694px;width:150px">ФИЗИЧЕСКИЙ<br>ИНТЕРФЕЙС<br><span style="font-family:'JetBrains Mono',monospace;font-size:16px">(gi1/0/1)</span></div>
</div>

<div class="step">
  <div class="lbk-pan" style="left:20px;top:640px;width:1004px;height:162px"></div>
  <div class="ab" style="left:40px;top:648px;font-family:Oswald,sans-serif;font-weight:700;font-size:24px;color:#2ad4ff">ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ</div>
  <div class="ab" style="left:40px;top:684px;width:80px;height:3px;background:#2ad4ff"></div>
  <div class="lbk-ex" style="left:40px;width:316px">{img("rep/loopback_e1.png", "width:58px")}<div>ИДЕНТИФИКАТОР<br>УСТРОЙСТВА</div></div>
  <div class="lbk-ex" style="left:368px;width:316px">{img("rep/loopback_e2.png", "width:70px")}<div>ДИНАМИЧЕСКАЯ<br>МАРШРУТИЗАЦИЯ</div></div>
  <div class="lbk-ex" style="left:696px;width:314px">{img("rep/loopback_e3.png", "width:62px")}<div>ТЕСТОВЫЕ<br>СЕТИ</div></div>
</div>

<div class="step">
  <div class="lbk-pan" style="left:20px;top:816px;width:1632px;height:96px"></div>
  <div class="ab" style="left:0;top:826px;width:1672px;text-align:center;font-family:Oswald,sans-serif;font-weight:700;font-size:36px;line-height:72px;color:#fff">
    <span style="color:#2ad4ff;font-size:50px">LOOPBACK</span> — СТАБИЛЬНЫЙ ЛОГИЧЕСКИЙ L3-ИНТЕРФЕЙС УСТРОЙСТВА</div>
</div>
"""
