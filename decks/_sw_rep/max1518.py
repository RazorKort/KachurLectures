# -*- coding: utf-8 -*-
"""MAX1518 — почему максимум 1518 байт: вёрстка 1:1 инфографики (pptx 8)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 196

CSS = """<style>
.mx-bx{position:absolute;border-radius:14px;border:2px solid rgba(42,212,255,.7);background:rgba(6,22,58,.8);box-shadow:0 0 14px rgba(42,212,255,.35)}
.mx-bar{position:absolute;top:256px;height:111px;border-radius:8px;display:flex;align-items:center;font-family:Oswald,sans-serif;font-weight:500;color:#fff}
.mx-os{font-family:Oswald,sans-serif;font-weight:500}
.mx-tx{position:absolute;color:#eef3ff;font-family:'Golos Text',sans-serif;font-size:25px;line-height:32px}
.mx-h{position:absolute;font-family:Oswald,sans-serif;font-weight:600;font-size:38px;line-height:46px}
@keyframes mx-shine{0%{background-position:-400px 0}100%{background-position:400px 0}}
.mx-hl{animation:mx-shine 3s linear infinite;background-image:linear-gradient(90deg,transparent,rgba(255,255,255,.18),transparent);background-size:400px 100%;background-repeat:no-repeat}
</style>"""

HTML = CSS + f"""
<div class="mx-bx step" style="left:38px;top:215px;width:1594px;height:175px;border-color:rgba(42,141,255,.6)"></div>
<div class="step">
  <div class="mx-bar" style="left:66px;width:544px;border:3px solid #2a8dff;background:linear-gradient(180deg,#123fa8,#0a2366);box-shadow:0 0 16px rgba(42,141,255,.7)">
    {img("rep/max1518_doc1.png", "margin-left:44px;width:64px")}
    <div style="margin-left:40px;text-align:center"><div style="font-size:32px;line-height:40px">Заголовок • 14 байт</div>
    <div style="font-family:Oswald,sans-serif;font-weight:400;font-size:19px;color:#dfe9ff">MAC назначения + MAC источника + EtherType</div></div></div>
</div>
<div class="step">
  <div class="mx-bar mx-hl" style="left:618px;width:615px;border:3px solid #2ad4ff;box-shadow:0 0 16px rgba(42,212,255,.7);
    background-color:rgba(10,90,120,.7)">{img("rep/max1518_doc2.png", "margin-left:62px;width:74px")}
    <span style="margin-left:36px;font-size:36px">Данные • до 1500 байт</span></div>
</div>
<div class="step">
  <div class="mx-bar" style="left:1240px;width:366px;border:3px solid #b98bff;background:linear-gradient(180deg,#5a24d0,#33118a);box-shadow:0 0 16px rgba(155,107,255,.7)">
    {img("rep/max1518_shield.png", "margin-left:22px;width:70px")}<span style="margin-left:22px;font-size:36px">FCS • 4 байта</span></div>
</div>
<div class="step">
  <div class="ab" style="left:0;top:398px;width:1672px;text-align:center;font-family:'Golos Text',sans-serif;font-weight:800;font-size:76px;line-height:96px;color:#fff">
    14 + 1500 + 4 = <span style="color:#2ad4ff">1518 байт</span></div>
</div>
<div class="step">
  <div class="mx-bx" style="left:42px;top:515px;width:780px;height:220px"></div>
  {img("rep/max1518_gear.png", "left:82px;top:565px;width:103px", "ab")}
  <div class="ab" style="left:220px;top:548px;width:2px;height:150px;background:rgba(42,212,255,.4)"></div>
  <div class="mx-h" style="left:252px;top:546px;color:#2ad4ff">MTU = 1500 байт</div>
  <div class="mx-tx" style="left:252px;top:604px;width:560px">Максимальный размер полезной нагрузки<br>Ethernet. Для IP это весь IP-пакет,<br>включая его заголовок.</div>
</div>
<div class="step">
  <div class="mx-bx" style="left:850px;top:515px;width:780px;height:220px"></div>
  {img("rep/max1518_bulb.png", "left:897px;top:562px;width:91px", "ab")}
  <div class="ab" style="left:1023px;top:548px;width:2px;height:150px;background:rgba(42,212,255,.4)"></div>
  <div class="mx-h" style="left:1053px;top:542px;color:#fff">Почему ограничили размер?</div>
  <div class="mx-tx" style="left:1053px;top:594px;width:570px">Исторический компромисс: меньше<br>накладных расходов, ограниченное время<br>занятия общей среды и умеренные<br>требования к буферам.</div>
</div>
<div class="step">
  <div class="mx-bx" style="left:46px;top:758px;width:1580px;height:68px"></div>
  {img("rep/max1518_tag.png", "left:410px;top:768px;width:57px", "ab")}
  <div class="ab mx-os" style="left:496px;top:770px;font-size:32px;line-height:46px;color:#fff">С тегом VLAN 802.1Q:&nbsp; 1518 + 4 &nbsp;= <span style="color:#2ad4ff">1522 байта</span></div>
</div>
<div class="step">
  <div class="mx-bx" style="left:48px;top:843px;width:788px;height:60px"></div>
  {img("rep/max1518_info.png", "left:76px;top:848px;width:48px", "ab")}
  <div class="mx-tx" style="left:146px;top:857px;font-size:20px;line-height:30px">Преамбула, SFD и межкадровый интервал в размер кадра не входят.</div>
  <div class="mx-bx" style="left:852px;top:843px;width:770px;height:60px"></div>
  {img("rep/max1518_dots.png", "left:871px;top:848px;width:51px", "ab")}
  <div class="mx-tx" style="left:948px;top:857px;font-size:20px;line-height:30px">Jumbo frames — увеличенные кадры при поддержке оборудования.</div>
</div>
"""
