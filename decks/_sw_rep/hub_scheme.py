# -*- coding: utf-8 -*-
"""HUB_SCHEME — схема работы концентратора: вёрстка 1:1 инфографики (pptx 12)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 92   # заголовок «Схема работы концентратора» даёт head() слайда

CSS = """<style>
.hsc-pan{position:absolute;border-radius:10px;border:2px solid rgba(42,212,255,.75);background:linear-gradient(180deg,rgba(8,40,90,.72),rgba(4,18,50,.85));
  box-shadow:0 0 14px rgba(42,212,255,.45),inset 0 0 22px rgba(42,212,255,.14)}
.hsc-hex{position:absolute;width:76px;height:116px;display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:700;
  font-size:64px;color:#e8fbff;text-shadow:0 0 12px #2ad4ff}
.hsc-hex svg{position:absolute;left:0;top:0}
.hsc-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:27px;line-height:1.14;color:#fff}
.hsc-t{position:absolute;font-size:21px;line-height:1.36;color:#e6f1ff}
.hsc-f{-webkit-mask-image:linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent),linear-gradient(180deg,transparent,#000 4%,#000 96%,transparent);-webkit-mask-composite:source-in;mask-composite:intersect}
.hsc-boom{position:absolute;width:70px;height:70px;border-radius:50%;background:radial-gradient(circle,rgba(255,240,200,.95),rgba(255,120,40,.6) 40%,transparent 70%);
  animation:hscBoom 1.1s ease-in-out infinite}
@keyframes hscBoom{0%,100%{transform:scale(.6);opacity:.5}50%{transform:scale(1.25);opacity:1}}
.hsc-env{position:absolute;animation:hscFly 2.6s linear infinite}
@keyframes hscFly{0%{transform:translate(0,0);opacity:0}10%{opacity:1}85%{opacity:1}100%{transform:translate(170px,48px);opacity:0}}
</style>"""


def _hex(x, y, col):
    return ('<div class="hsc-hex" style="left:%dpx;top:%dpx;text-shadow:0 0 12px %s">'
            '<svg width="76" height="116" viewBox="0 0 76 116"><path d="M14 2 H62 L74 14 V102 L62 114 H14 L2 102 V14 Z" fill="rgba(6,24,60,.85)" '
            'stroke="%s" stroke-width="2.5" style="filter:drop-shadow(0 0 6px %s)"/></svg><span style="position:relative">%%s</span></div>' % (x, y, col, col, col))


ENV = ('<svg width="44" height="32" viewBox="0 0 44 32"><rect x="2" y="2" width="40" height="28" rx="3" fill="rgba(140,230,255,.35)" stroke="#bff3ff" stroke-width="2"/>'
       '<path d="M3 4 L22 18 L41 4" fill="none" stroke="#bff3ff" stroke-width="2"/></svg>')

HTML = CSS + f"""
<div class="step">
  <div class="hsc-pan" style="left:22px;top:212px;width:426px;height:154px"></div>
  {_hex(36, 226, "#2ad4ff") % "1"}
  <div class="hsc-h" style="left:138px;top:240px">PC-A ПЕРЕДАЁТ КАДР</div>
  <div class="hsc-t" style="left:138px;top:284px">Хаб H1 получает сигнал<br>на одном порту.</div>
</div>
<div class="step">
  <div class="hsc-pan" style="left:22px;top:380px;width:426px;height:154px"></div>
  {_hex(36, 397, "#2ad4ff") % "2"}
  <div class="hsc-h" style="left:138px;top:409px;color:#7fe6ff">H1 КОПИРУЕТ СИГНАЛ</div>
  <div class="hsc-t" style="left:138px;top:451px">Кадр передаётся во все<br>остальные порты.</div>
</div>
<div class="step">
  <div class="hsc-pan" style="left:22px;top:556px;width:426px;height:182px"></div>
  {_hex(36, 574, "#ff5ca8") % "3"}
  <div class="hsc-h" style="left:138px;top:585px;color:#7fe6ff">PC-D ПЕРЕДАЁТ<br>ОДНОВРЕМЕННО</div>
  <div class="hsc-t" style="left:138px;top:660px">В общей среде возникает<br>коллизия.</div>
</div>

<div class="step">
  <div class="ab" style="left:470px;top:96px;width:1182px;height:648px;border:2px solid rgba(42,212,255,.6);border-radius:14px;box-shadow:0 0 14px rgba(42,212,255,.35)"></div>
  <div class="ab" style="left:482px;top:166px;width:1140px;height:554px;border:2px dashed #9fe8ff;border-radius:60px"></div>
  {img("rep/hub_scheme_scene.png", "left:492px;top:200px;width:1118px", "ab hsc-f")}
  <svg class="ab" style="left:816px;top:138px" width="438" height="52" viewBox="0 0 438 52"><path d="M2 26 L24 2 H414 L436 26 L414 50 H24 Z" fill="rgba(6,24,64,.95)"
    stroke="#2ad4ff" stroke-width="2.5" style="filter:drop-shadow(0 0 8px #2ad4ff)"/></svg>
  <div class="ab os" style="left:816px;top:144px;width:438px;text-align:center;font-weight:700;font-size:29px;letter-spacing:1px;color:#e6fbff">ОДИН ДОМЕН КОЛЛИЗИЙ</div>
</div>

<div class="step">
  <div class="ab" style="left:760px;top:262px;padding:0 6px;font-size:21px;color:#e6f1ff;background:rgba(6,20,50,.9);border-radius:4px">Кадр от PC-A</div>
  <div class="hsc-env" style="left:770px;top:300px">{ENV}</div>
</div>

<div class="step">
  <div class="hsc-boom" style="left:1240px;top:510px"></div>
  <div class="ab os" style="left:1295px;top:441px;width:156px;height:46px;border-radius:7px;border:2px solid #ff4d5e;background:rgba(60,8,24,.95);
    box-shadow:0 0 14px rgba(255,77,94,.8);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:25px;color:#fff">КОЛЛИЗИЯ</div>
</div>

<div class="step">
  <div class="hsc-pan" style="left:22px;top:760px;width:1628px;height:150px"></div>
  {img("rep/hub_scheme_chip.png", "left:58px;top:772px;width:126px", "ab hsc-f")}
  <div class="ab os" style="left:216px;top:782px;font-weight:700;font-size:44px;line-height:1;color:#5fe0ff;text-shadow:0 0 10px rgba(42,212,255,.6)">ХАБ <span style="font-size:40px">РАБОТАЕТ НА ФИЗИЧЕСКОМ УРОВНЕ</span></div>
  <div class="ab" style="left:216px;top:847px;font-size:21.5px;color:#fff">Он не анализирует MAC-адреса, не выбирает получателя и не предотвращает коллизии.</div>
  <div class="ab" style="left:1148px;top:798px;width:2px;height:70px;background:rgba(42,212,255,.5)"></div>
  {img("rep/hub_scheme_env.png", "left:1180px;top:800px;width:70px", "ab hsc-f")}
  <div class="ab os" style="left:1278px;top:793px;font-size:21px;color:#5fe0ff">Все устройства получают кадр.</div>
  <div class="ab" style="left:1278px;top:826px;font-size:18px;line-height:1.3;color:#e6f1ff">Обрабатывает его только узел<br>с подходящим MAC-адресом назначения.</div>
</div>
"""
