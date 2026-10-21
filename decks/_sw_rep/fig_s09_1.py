# -*- coding: utf-8 -*-
"""fig_s09_1 — «Что такое MAC-адрес?»: сетевая карта и её MAC как удостоверение личности. Вёрстка + SVG."""

W, H, TOP = 1208, 528, 0
P = "s09"
C = "#2ad4ff"

FACE = """<svg viewBox="0 0 60 70" width="%d" height="%d" style="position:absolute;left:%dpx;top:%dpx;overflow:visible">
<path d="M8 28 C8 6 52 6 52 28" fill="#0d2d66" stroke="#2ad4ff" stroke-width="2.5"/>
<ellipse cx="30" cy="34" rx="22" ry="22" fill="#0b2250" stroke="#2ad4ff" stroke-width="2.5"/>
<path d="M8 30 C14 14 46 14 52 30 C42 22 18 22 8 30Z" fill="#2ad4ff" opacity=".85"/>
<circle cx="22" cy="34" r="3" fill="#e6f1ff"/><circle cx="38" cy="34" r="3" fill="#e6f1ff"/>
<path d="M22 46 Q30 40 38 46" fill="none" stroke="#e6f1ff" stroke-width="2.5" stroke-linecap="round"/>%s</svg>"""
BODY = '<path d="M4 70 C6 58 18 56 30 56 C42 56 54 58 56 70" fill="#0d2d66" stroke="#2ad4ff" stroke-width="2.5"/>'

CELLS = "".join(f'<div class="{P}-cell" style="left:{360 + i * 40}px;animation-delay:{.3 + i * .18:.2f}s"></div>' for i in range(6))

HTML = f"""<style>
.{P}-tx{{position:absolute;font-family:"Golos Text",sans-serif;color:#e6f1ff}}
.{P}-pan{{position:absolute;border:2px solid rgba(42,212,255,.55);border-radius:6px;background:rgba(6,24,64,.55)}}
.{P}-card{{position:absolute;border:2.5px solid {C};border-radius:22px;background:rgba(10,40,96,.6);box-shadow:0 0 16px rgba(42,212,255,.45)}}
.{P}-bub{{position:absolute;border:2.5px solid {C};border-radius:16px;background:rgba(10,40,96,.75);box-shadow:0 0 12px rgba(42,212,255,.4)}}
.{P}-cell{{position:absolute;top:407px;width:37px;height:26px;border:1.5px solid {C};border-radius:4px;
  background:repeating-linear-gradient(45deg,rgba(42,212,255,.55) 0 3px,rgba(42,212,255,.15) 3px 6px)}}
.vis .{P}-cell{{animation:{P}-cl .45s ease-out both}}
@keyframes {P}-cl{{from{{opacity:0;transform:translateY(-12px)}}to{{opacity:1;transform:none}}}}
.{P}-hd{{position:absolute;background:linear-gradient(180deg,#1aa6e0,#0a6fb0);border:2px solid {C};border-radius:4px;box-shadow:0 0 16px rgba(42,212,255,.7);
  display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:600;font-size:23px;color:#fff}}
.{P}-def{{position:absolute;border:2px solid rgba(42,212,255,.6);background:rgba(6,24,64,.75);padding:10px 10px 0 10px;
  font-family:"Golos Text",sans-serif;font-size:18.5px;line-height:34px;color:#e6f1ff;text-align:justify}}
</style>
<div class="{P}-tx step" style="left:42px;top:16px;width:1130px;font-size:22.5px;line-height:40px;text-align:justify;padding-left:30px">
  <span style="position:absolute;left:0;color:{C}">•</span>MAC-адрес идентифицирует сетевую карту в сети. У каждой сетевой карты должен быть глобальный уникальный MAC-адрес.</div>
<div class="step">
  <div class="{P}-pan" style="left:133px;top:177px;width:546px;height:304px"></div>
  <div class="{P}-tx" style="left:133px;width:546px;top:200px;text-align:center;font-size:18.5px">Что такое MAC-адрес?</div>
  <div class="{P}-bub" style="left:148px;top:254px;width:164px;height:86px"></div>
  <svg style="position:absolute;left:250px;top:336px" width="40" height="30"><path d="M8 0 L30 22 L26 0" fill="rgba(10,40,96,.95)" stroke="{C}" stroke-width="2.5"/></svg>
  <div class="{P}-tx" style="left:156px;top:255px;font-size:14.5px;line-height:19px">У меня есть<br>MAC-адрес,<br>когда я покидаю<br>производство.</div>
  {FACE % (64, 76, 263, 356, BODY)}
</div>
<div class="step">
  <div class="{P}-card" style="left:345px;top:265px;width:308px;height:191px"></div>
  <div class="{P}-tx" style="left:362px;top:298px;font-size:16.5px">Имя: NIC</div>
  {FACE % (48, 52, 532, 292, "")}
  <div class="{P}-tx" style="left:360px;top:350px;font-size:16.5px;line-height:30px">MAC-адрес/адрес Ethernet/<br>физический адрес:</div>
  {CELLS}
</div>
<div class="step">
  <svg style="position:absolute;left:0;top:0;overflow:visible" width="{W}" height="{H}"><defs><linearGradient id="{P}-pj" x1="0" x2="1">
    <stop offset="0" stop-color="#2ad4ff" stop-opacity=".05"/><stop offset="1" stop-color="#2ad4ff" stop-opacity=".45"/></linearGradient></defs>
    <path d="M679 177 L758 185 L758 433 L679 481 Z" fill="url(#{P}-pj)"/></svg>
  <div class="{P}-hd" style="left:758px;top:178px;width:396px;height:44px">MAC-адрес</div>
  <div class="{P}-def" style="left:758px;top:227px;width:396px;height:207px"><span style="display:block;text-align-last:justify">У каждой сетевой карты есть номер,</span><span style="display:block;text-align-last:justify">т.е. MAC-адрес, для идентификации,</span><span style="display:block;text-align-last:justify">так же как у каждого человека есть</span>удостоверение личности.</div>
</div>
"""
