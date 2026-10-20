# -*- coding: utf-8 -*-
"""BRIDGE_TO_ASIC — от сетевого моста к ASIC: вёрстка 1:1 (pptx 17)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 156   # «Интегральные схемы / От сетевого моста к ASIC» даёт head()

CSS = """<style>
.bta-pan{position:absolute;border-radius:12px;border:2px solid #2ad4ff;background:linear-gradient(180deg,rgba(8,40,90,.55),rgba(4,18,50,.8));
  box-shadow:0 0 16px rgba(42,212,255,.5),inset 0 0 24px rgba(42,212,255,.12)}
.bta-sm{position:absolute;border-radius:8px;border:1.5px solid rgba(42,212,255,.65);background:rgba(6,22,56,.85);box-shadow:0 0 8px rgba(42,212,255,.35)}
.bta-sm.m{border-color:#ff5ca8;box-shadow:0 0 10px rgba(255,92,168,.6)}
.bta-l{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:19px;line-height:1.2;color:#fff}
.bta-fr{position:absolute;left:42px;width:126px;height:34px;border-radius:4px;border:2px solid #2ad4ff;background:rgba(10,40,90,.9);box-shadow:0 0 8px rgba(42,212,255,.6);
  display:flex;align-items:center;justify-content:center;font-size:16px;color:#fff}
.bta-fr.m{border-color:#c06bff;box-shadow:0 0 8px rgba(192,107,255,.7)}
.bta-f{-webkit-mask-image:linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent),linear-gradient(180deg,transparent,#000 4%,#000 96%,transparent);-webkit-mask-composite:source-in;mask-composite:intersect}
.bta-hex{position:absolute;width:84px;height:84px;display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:700;font-size:50px;color:#fff;
  clip-path:polygon(30% 0,70% 0,100% 30%,100% 70%,70% 100%,30% 100%,0 70%,0 30%);background:linear-gradient(180deg,#1e5aa8,#0b2a60)}
.bta-run{animation:btaRun 1.8s linear infinite}
@keyframes btaRun{0%{transform:translateX(-30px);opacity:0}15%{opacity:1}85%{opacity:1}100%{transform:translateX(30px);opacity:0}}
</style>"""

FRAMES = [(348, ""), (401, ""), (455, "m")]


def _frames():
    return "".join('<div class="bta-fr %s" style="top:%dpx">Ethernet кадр</div>' % (c, y) for y, c in FRAMES)


def _feat(x, w, ico, ist, text, tx, cls="", col="#fff"):
    return ('<div class="bta-sm %s" style="left:%dpx;top:528px;width:%dpx;height:90px"></div>%s'
            '<div class="bta-l" style="left:%dpx;top:%dpx;color:%s">%s</div>'
            % (cls, x, w, img("rep/bridge_to_asic_%s.png" % ico, ist, "ab bta-f"), tx, 573 - 12 * text.count("<br>") - 12, col, text))


HTML = CSS + f"""
<div class="step">
  <div class="bta-pan" style="left:22px;top:172px;width:762px;height:456px"></div>
  <div class="ab os" style="left:56px;top:186px;font-weight:700;font-size:40px;color:#fff">РАННИЙ <span style="color:#2ad4ff">СЕТЕВОЙ МОСТ</span></div>
  <div class="ab" style="left:56px;top:236px;width:330px;height:3px;background:linear-gradient(90deg,#2ad4ff,transparent)"></div>
  {img("rep/bridge_to_asic_early.png", "left:176px;top:290px;width:584px", "ab bta-f")}
  <div class="bta-l" style="left:330px;top:250px;width:166px;text-align:center;font-size:18px">ЦЕНТРАЛЬНЫЙ<br>ПРОЦЕССОР + ПО</div>
  <div class="ab" style="left:224px;top:348px;font-size:15px;color:#fff;background:rgba(6,18,46,.9);padding:0 3px">Очередь кадров</div>
  {_frames()}
</div>
<div class="step">
  {_feat(28, 232, "i1", "left:40px;top:540px;width:65px", "МЕДЛЕННАЯ<br>ОБРАБОТКА", 120)}
  {_feat(272, 250, "i2", "left:284px;top:545px;width:58px", "ТОЛЬКО 2–4 ПОРТА", 355)}
  {_feat(534, 240, "i3", "left:545px;top:545px;width:63px", "РАСШИРЯТЬ<br>ДОРОГО", 625, "m", "#ff6fb0")}
</div>

<div class="step">
  <svg class="ab" style="left:774px;top:298px" width="172" height="182" viewBox="0 0 172 182"><path d="M2 46 H96 V2 L170 91 L96 180 V136 H2 Z" fill="rgba(20,90,200,.55)"
    stroke="#2ad4ff" stroke-width="3" style="filter:drop-shadow(0 0 12px #2ad4ff)"/></svg>
  <div class="ab os" style="left:770px;top:357px;width:140px;text-align:center;font-weight:700;font-size:23px;line-height:1.15;color:#fff">СЕРЕДИНА<br><span style="font-size:31px">1980-х</span></div>
</div>

<div class="step">
  <div class="bta-pan" style="left:892px;top:172px;width:758px;height:456px"></div>
  {img("rep/bridge_to_asic_asic.png", "left:896px;top:240px;width:754px", "ab bta-f")}
  <div class="ab os" style="left:936px;top:172px;font-weight:700;font-size:62px;color:#5fe8ff;text-shadow:0 0 14px rgba(42,212,255,.7)">ASIC</div>
  <div class="ab" style="left:936px;top:242px;width:150px;height:3px;background:#2ad4ff"></div>
</div>
<div class="step">
  {_feat(900, 246, "i4", "left:912px;top:540px;width:63px", "ОБРАБОТКА ВНУТРИ<br>МИКРОСХЕМЫ", 988)}
  {_feat(1154, 236, "i5", "left:1164px;top:540px;width:68px", "БЕЗ УЧАСТИЯ<br>ЦЕНТРАЛЬНОГО<br>ПРОЦЕССОРА", 1246)}
  {_feat(1398, 244, "i6", "left:1410px;top:545px;width:55px", "БОЛЬШЕ ПОРТОВ •<br><span style='color:#fff'>ВЫШЕ СКОРОСТЬ</span>", 1478, "", "#5fe8ff")}
</div>

<div class="step">
  <div class="bta-pan" style="left:48px;top:645px;width:1574px;height:124px"></div>
  <div class="bta-hex" style="left:78px;top:664px">1</div>
  <div class="bta-l" style="left:184px;top:660px;font-size:19px">КАДР ПОСТУПАЕТ</div>
  {img("rep/bridge_to_asic_s1.png", "left:220px;top:695px;width:285px", "ab bta-f bta-run")}
  <div class="bta-hex" style="left:574px;top:664px">2</div>
  <div class="bta-l" style="left:676px;top:660px;font-size:19px">ASIC АНАЛИЗИРУЕТ</div>
  {img("rep/bridge_to_asic_s2.png", "left:700px;top:665px;width:375px", "ab bta-f")}
  <div class="bta-hex" style="left:1124px;top:664px">3</div>
  <div class="bta-l" style="left:1228px;top:658px;font-size:19px">КАДР НАПРАВЛЯЕТСЯ<br>В НУЖНЫЙ ПОРТ</div>
  {img("rep/bridge_to_asic_s3.png", "left:1275px;top:675px;width:335px", "ab bta-f")}
</div>

<div class="step">
  <div class="bta-pan" style="left:166px;top:790px;width:1460px;height:130px"></div>
  {img("rep/bridge_to_asic_chip.png", "left:196px;top:805px;width:104px", "ab bta-f")}
  <div class="ab os" style="left:330px;top:806px;font-weight:700;font-size:46px;line-height:1;color:#fff"><span style="color:#5fe8ff">ASIC</span> — APPLICATION-SPECIFIC INTEGRATED CIRCUIT</div>
  <div class="ab os" style="left:332px;top:860px;font-weight:500;font-size:25px;color:#5fe8ff">ИНТЕГРАЛЬНАЯ СХЕМА ДЛЯ СПЕЦИАЛИЗИРОВАННОГО ПРИЛОЖЕНИЯ</div>
  {img("rep/bridge_to_asic_circ.png", "left:1140px;top:800px;width:190px", "ab bta-f")}
  <div class="bta-l" style="left:1336px;top:816px;font-weight:400;font-size:17px;line-height:1.55">СПЕЦИАЛИЗИРОВАННАЯ ЛОГИКА<br>ВЫСОКАЯ ПРОИЗВОДИТЕЛЬНОСТЬ<br>ЭФФЕКТИВНАЯ СЕТЕВАЯ ОБРАБОТКА</div>
</div>
"""
