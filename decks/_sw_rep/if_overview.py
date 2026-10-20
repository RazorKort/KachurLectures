# -*- coding: utf-8 -*-
"""Интерфейсы коммутатора: обзор L2 / L3 — вёрстка 1:1."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 145

CSS = """<style>
.ifo-pan{position:absolute;border:2px solid #2ad4ff;border-radius:14px;background:rgba(6,24,64,.55);box-shadow:0 0 18px rgba(42,212,255,.5),inset 0 0 30px rgba(42,212,255,.12)}
.ifo-pan.v{border-color:#9b6bff;box-shadow:0 0 18px rgba(155,107,255,.55),inset 0 0 30px rgba(155,107,255,.14)}
.ifo-sub{position:absolute;border:1.5px solid rgba(42,212,255,.6);border-radius:10px;background:rgba(8,30,80,.6)}
.ifo-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:48px;line-height:1;color:#fff;letter-spacing:.5px}
.ifo-h i{font-style:normal;color:#2ad4ff}.ifo-h i.v{color:#9b6bff}
.ifo-ul{position:absolute;height:4px;width:80px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff}
.ifo-cap{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:24px;color:#fff}
.ifo-fld{position:absolute;height:56px;display:flex;align-items:center;justify-content:center;font-family:'Golos Text',sans-serif;font-size:22px;color:#fff;
  border:1.5px solid #2ad4ff;border-radius:6px;background:linear-gradient(180deg,rgba(20,90,150,.9),rgba(8,50,100,.9))}
.ifo-fld.d{background:rgba(10,40,80,.7)}.ifo-fld.b{background:linear-gradient(180deg,#1a6fe0,#0d3c9a)}
.ifo-ar{position:absolute;color:#2ad4ff;font-size:28px;line-height:56px}
.ifo-row{position:absolute;left:1128px;width:496px;height:86px;border:2px solid #6f8cff;border-radius:10px;background:rgba(14,30,90,.7);box-shadow:0 0 12px rgba(111,140,255,.45)}
.ifo-row b{position:absolute;left:150px;top:0;height:86px;display:flex;align-items:center;font-family:Oswald,sans-serif;font-weight:500;font-size:22px;line-height:1.25;color:#fff}
.ifo-row s{position:absolute;right:22px;top:24px;text-decoration:none;color:#2ad4ff;font-size:44px;line-height:1;top:16px}
.ifo-tx{position:absolute;font-family:'Golos Text',sans-serif;font-size:24px;line-height:1.35;color:#e6f1ff}
.ifo-tag{position:absolute;width:98px;height:72px;border:3px solid #2ad4ff;border-radius:10px;background:rgba(6,30,70,.85);box-shadow:0 0 18px rgba(42,212,255,.8);
  display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:700;font-size:50px;color:#9ff0ff}
.ifo-tag.v{border-color:#9b6bff;color:#fff;box-shadow:0 0 18px rgba(155,107,255,.8)}
.ifo-wire path{fill:none;stroke-width:3;filter:drop-shadow(0 0 4px currentColor)}
.ifo-flow{stroke-dasharray:10 14;animation:ifoflow 1.4s linear infinite}
@keyframes ifoflow{to{stroke-dashoffset:-48}}
</style>"""

HTML = CSS + f"""
<div class="step">
  <div class="ifo-pan" style="left:24px;top:158px;width:578px;height:632px"></div>
  <div class="ifo-h" style="left:68px;top:186px">ИНТЕРФЕЙСЫ <i>L2</i></div>
  <div class="ifo-ul" style="left:68px;top:244px"></div>
</div>

<div class="step">
  <div class="ifo-sub" style="left:48px;top:264px;width:524px;height:222px"></div>
  <div class="ifo-cap" style="left:70px;top:282px">ПОРТЫ КОММУТАТОРА</div>
  {img("rep/if_overview_ports.png", "left:52px;top:332px;width:520px", "ab")}
</div>

<div class="step">
  <div class="ifo-sub" style="left:48px;top:548px;width:510px;height:112px"></div>
  <div class="ab" style="left:68px;top:556px;font-size:18px;color:#e6f1ff">Кадр Ethernet (упрощенно)</div>
  <div class="ifo-fld d" style="left:64px;top:588px;width:50px">…</div>
  <div class="ifo-fld" style="left:116px;top:588px;width:96px">MAC</div>
  <div class="ifo-ar" style="left:218px;top:588px">➜</div>
  <div class="ifo-fld" style="left:252px;top:588px;width:124px">EtherType</div>
  <div class="ifo-ar" style="left:382px;top:588px">➜</div>
  <div class="ifo-fld" style="left:414px;top:588px;width:80px">FCS</div>
  <div class="ifo-fld d" style="left:496px;top:588px;width:46px">…</div>
</div>

<div class="step">
  {img("rep/if_overview_rjc.png", "left:64px;top:672px;width:108px", "ab")}
  <div class="ifo-tx" style="left:198px;top:696px">Обрабатывают информацию<br>канального уровня</div>
</div>

<div class="step">
  <svg class="ab ifo-wire" style="left:0;top:0;width:1672px;height:941px" viewBox="0 0 1672 941">
    <path d="M733 290V380L738 410" stroke="#2ad4ff" color="#2ad4ff"/><path d="M733 380L766 410" stroke="#2ad4ff" color="#2ad4ff"/>
    <path d="M940 290V370L906 410" stroke="#9b6bff" color="#9b6bff"/><path d="M940 370V410" stroke="#9b6bff" color="#9b6bff"/>
    <path class="ifo-flow" d="M733 290V380L766 410" stroke="#bff6ff" color="#2ad4ff"/>
    <path class="ifo-flow" d="M940 290V370L906 410" stroke="#e0d0ff" color="#9b6bff"/>
    <path d="M790 622V690H760L700 750H560" stroke="#2ad4ff" color="#2ad4ff"/>
    <path d="M878 636V680L940 740H1110" stroke="#9b6bff" color="#9b6bff"/>
  </svg>
  {img("rep/if_overview_sw.png", "left:560px;top:395px;width:560px;-webkit-mask-image:radial-gradient(ellipse 52% 54% at 50% 50%,#000 72%,transparent 100%);mask-image:radial-gradient(ellipse 52% 54% at 50% 50%,#000 72%,transparent 100%)", "ab")}
  <div class="ifo-tag" style="left:683px;top:214px">L2</div>
  <div class="ifo-tag v" style="left:891px;top:214px">L3</div>
</div>

<div class="step">
  <div class="ifo-pan v" style="left:1072px;top:158px;width:578px;height:632px"></div>
  <div class="ifo-h" style="left:1140px;top:186px">ИНТЕРФЕЙСЫ <i class="v">L3</i></div>
  <div class="ifo-ul" style="left:1140px;top:244px;background:#9b6bff;box-shadow:0 0 8px #9b6bff"></div>
</div>

<div class="step">
  <div class="ifo-row" style="top:265px"><b>ФИЗИЧЕСКИЙ ПОРТ<br>С IP-АДРЕСОМ</b><s>›</s></div>
  {img("rep/if_overview_rj.png", "left:1158px;top:278px;width:76px", "ab")}
  <div class="ifo-row" style="top:366px;transition-delay:120ms"><b>SVI — ИНТЕРФЕЙС VLAN</b><s>›</s></div>
  {img("rep/if_overview_vlan.png", "left:1152px;top:372px;width:90px", "ab")}
  <div class="ifo-row" style="top:465px"><b>LOOPBACK —<br>ОБРАТНАЯ ПЕТЛЯ</b><s>›</s></div>
  {img("rep/if_overview_inf.png", "left:1152px;top:478px;width:90px", "ab")}
</div>

<div class="step">
  <div class="ifo-sub" style="left:1128px;top:566px;width:496px;height:96px;border-color:rgba(155,107,255,.6)"></div>
  <div class="ab" style="left:1146px;top:572px;font-size:18px;color:#e6f1ff">IP-пакет (упрощенно)</div>
  <div class="ifo-fld d" style="left:1142px;top:604px;width:48px">…</div>
  <div class="ifo-fld b" style="left:1192px;top:604px;width:154px">Source IP</div>
  <div class="ifo-ar" style="left:1354px;top:604px">➜</div>
  <div class="ifo-fld b" style="left:1388px;top:604px;width:174px">Destination IP</div>
  <div class="ifo-fld d" style="left:1564px;top:604px;width:48px">…</div>
</div>

<div class="step">
  {img("rep/if_overview_arr.png", "left:1124px;top:678px;width:104px", "ab")}
  <div class="ifo-tx" style="left:1252px;top:696px">Обрабатывают данные L2<br>и заголовки сетевого уровня</div>
</div>

<div class="step">
  <div class="ifo-pan" style="left:164px;top:812px;width:1344px;height:78px;border-radius:12px"></div>
  <div class="ab os" style="left:330px;top:826px;font-family:Oswald,sans-serif;font-weight:500;font-size:32px;color:#fff"><span style="color:#2ad4ff;font-weight:700;font-size:38px">L2</span> <span style="color:#2ad4ff">—</span> КАДРЫ И MAC-АДРЕСА</div>
  <div class="ab" style="left:830px;top:830px;width:3px;height:40px;background:#cfe0ff"></div>
  <div class="ab os" style="left:912px;top:826px;font-family:Oswald,sans-serif;font-weight:500;font-size:32px;color:#fff"><span style="color:#9b6bff;font-weight:700;font-size:38px">L3</span> <span style="color:#9b6bff">—</span> ПАКЕТЫ И IP-АДРЕСА</div>
  <div class="ab" style="left:0;top:902px;width:1672px;text-align:center;font-size:17px;color:#a8bce0">IP-адрес на физическом порту поддерживается не всеми коммутаторами</div>
</div>
"""
