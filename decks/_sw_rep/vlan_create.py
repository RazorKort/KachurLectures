# -*- coding: utf-8 -*-
"""Создание и удаление VLAN — три панели CLI: создание, проверка, удаление."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 205

CSS = """<style>
.vc-col{position:absolute;top:232px;height:566px;border-radius:16px;border:3px solid #2ad4ff;background:rgba(6,24,70,.55);box-shadow:0 0 22px rgba(42,212,255,.65),inset 0 0 26px rgba(42,212,255,.15)}
.vc-col.v{border-color:#9b6bff;box-shadow:0 0 22px rgba(155,107,255,.65),inset 0 0 26px rgba(155,107,255,.15)}
.vc-col.m{border-color:#e05cff;box-shadow:0 0 22px rgba(224,92,255,.65),inset 0 0 26px rgba(224,92,255,.15)}
.vc-hex{position:absolute;top:244px;width:80px;height:78px;clip-path:polygon(25% 0,75% 0,100% 50%,75% 100%,25% 100%,0 50%);display:flex;align-items:center;justify-content:center;
  font-family:Oswald,sans-serif;font-weight:700;font-size:48px;color:#fff}
.vc-hex i{position:absolute;inset:4px;clip-path:inherit;background:#071a48;z-index:-1}
.vc-t{position:absolute;top:258px;font-family:Oswald,sans-serif;font-weight:700;font-size:40px;color:#fff;letter-spacing:.5px}
.vc-t span{color:#2ad4ff}
.vc-cli{position:absolute;top:340px;height:300px;border-radius:12px;border:2px solid #2ad4ff;background:rgba(2,10,30,.85);box-shadow:0 0 12px rgba(42,212,255,.45)}
.vc-cli:before{content:'SWITCH (CLI)';position:absolute;left:0;right:0;top:0;height:44px;line-height:44px;padding-left:24px;border-bottom:1px solid rgba(42,212,255,.6);
  font-family:'JetBrains Mono',monospace;font-size:17px;color:#2ad4ff;background:rgba(10,40,90,.6);border-radius:10px 10px 0 0}
.vc-cli.v,.vc-cli.v:before{border-color:#7b6bff}.vc-cli.m{border-color:#c05cff}
.vc-m{position:absolute;font-family:'JetBrains Mono',monospace;color:#fff;white-space:pre;margin:0}
.vc-m em{font-style:normal;color:#2ad4ff}
.vc-n{font-family:"Golos Text",sans-serif;font-size:16.5px;color:#fff}
.vc-b{position:absolute;top:664px;height:126px;border-radius:12px;border:2px solid #2ad4ff;background:rgba(8,30,80,.7);box-shadow:0 0 14px rgba(42,212,255,.5)}
.vc-b.v{border-color:#9b6bff;box-shadow:0 0 14px rgba(155,107,255,.55)}.vc-b.m{border-color:#e05cff;box-shadow:0 0 14px rgba(224,92,255,.55)}
.vc-bt{position:absolute;top:694px;font-size:26px;line-height:1.3;color:#fff}
@keyframes vc-arr{0%,100%{transform:translateX(0)}50%{transform:translateX(6px)}}
.vc-ar{position:absolute;top:462px;animation:vc-arr 1.2s ease-in-out infinite}
@keyframes vc-cur{50%{opacity:0}}
.vc-cur{display:inline-block;width:10px;height:20px;background:#2ad4ff;vertical-align:-3px;animation:vc-cur 1s steps(1) infinite}
</style>"""

ARROW = '<svg class="vc-ar" style="left:%dpx" width="40" height="44" viewBox="0 0 40 44"><path d="M0 12 H20 V0 L40 22 L20 44 V32 H0 Z" fill="#2ad4ff" style="filter:drop-shadow(0 0 6px #2ad4ff)"/></svg>'

HTML = CSS + f"""
<div class="step">
  <div class="vc-col" style="left:10px;width:488px"></div>
  <div class="vc-hex" style="left:26px;background:#2ad4ff"><i></i>1</div>
  <div class="vc-t" style="left:140px">СОЗДАНИЕ <span>VLAN</span></div>
  <div class="vc-cli" style="left:22px;width:466px"></div>
  <div class="vc-m" style="left:42px;top:396px;font-size:18px"><em>vlan num</em> <span class="vc-n">— создать VLAN, где num — номер VLAN</span></div>
  <pre class="vc-m" style="left:42px;top:436px;font-size:19.5px;line-height:34px">switch(config)# <em>vlan 10</em>
switch(config-vlan)# <em>name IT</em>
switch(config-vlan)# <em>vlan 20</em>
switch(config-vlan)# <em>name Management</em></pre>
  <div class="vc-b" style="left:22px;width:466px"></div>
  {img("rep/vlan_create_gear.png", "left:43px;top:683px;width:94px", "ab")}
  <div class="vc-bt" style="left:158px">Созданы VLAN 10 «IT»<br>и VLAN 20 «Management»</div>
</div>
<div class="step">
  {ARROW % 490}
  <div class="vc-col v" style="left:520px;width:562px"></div>
  <div class="vc-hex" style="left:536px;background:#9b6bff"><i></i>2</div>
  <div class="vc-t" style="left:646px">ПРОВЕРКА</div>
  <div class="vc-cli v" style="left:530px;width:542px"></div>
  <pre class="vc-m" style="left:550px;top:400px;font-size:21px">switch# <em>show vlan</em></pre>
  <pre class="vc-m" style="left:550px;top:464px;font-size:14.5px;line-height:28px">Vlan  Name          Tagged Ports  UnTagged Ports  Created by
----- ------------- ------------- --------------- -----------
1     -                           gi1/0/1-24      D
10    IT                                          S
20    Management                                  S</pre>
  <div class="vc-b v" style="left:530px;width:542px"></div>
  {img("rep/vlan_create_mag.png", "left:553px;top:683px;width:92px", "ab")}
  <div class="vc-bt" style="left:682px">VLAN 1 — по умолчанию;<br>порты gi1/0/1-24 — UnTagged</div>
</div>
<div class="step">
  {ARROW % 1072}
  <div class="vc-col m" style="left:1104px;width:558px"></div>
  <div class="vc-hex" style="left:1120px;background:#e05cff"><i></i>3</div>
  <div class="vc-t" style="left:1230px">УДАЛЕНИЕ <span>VLAN 10</span></div>
  <div class="vc-cli m" style="left:1112px;width:542px"></div>
  <div class="vc-m" style="left:1132px;top:396px;font-size:18px"><em>no vlan num</em> <span class="vc-n">— удалить VLAN с номером num</span></div>
  <pre class="vc-m" style="left:1132px;top:432px;font-size:19.5px;line-height:30px">switch(config)# <em>no vlan 10</em>
switch(config)# <em>do show vlan</em><span class="vc-cur"></span></pre>
  <pre class="vc-m" style="left:1130px;top:512px;font-size:14.5px;line-height:28px">Vlan  Name          Tagged Ports  UnTagged Ports  Created by
----- ------------- ------------- --------------- -----------
1     -                           gi1/0/1-24      D
20    Management                                  S</pre>
  <div class="vc-b m" style="left:1112px;width:542px"></div>
  {img("rep/vlan_create_trash.png", "left:1150px;top:683px;width:80px", "ab")}
  <div class="vc-bt" style="left:1265px">VLAN 10 удалён;<br>VLAN 1 и VLAN 20 сохранены</div>
</div>
"""
