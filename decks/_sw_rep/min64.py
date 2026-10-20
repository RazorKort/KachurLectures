# -*- coding: utf-8 -*-
"""MIN64 — почему минимум 64 байта: вёрстка 1:1 инфографики (pptx 7)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 146

CSS = """<style>
.m64-pan{position:absolute;top:158px;height:752px;border-radius:14px;border:3px solid #2a8dff;background:rgba(6,18,52,.8);
  box-shadow:0 0 22px rgba(42,141,255,.55),inset 0 0 40px rgba(42,141,255,.12)}
.m64-bx{position:absolute;border-radius:14px;border:2px solid rgba(42,212,255,.75);background:rgba(6,30,66,.78);box-shadow:0 0 12px rgba(42,212,255,.35)}
.m64-bx.m{border-color:#d95cff;background:rgba(46,12,76,.8);box-shadow:0 0 14px rgba(217,92,255,.45)}
.m64-tx{position:absolute;color:#f2f6ff;font-family:'Golos Text',sans-serif;font-size:24px;line-height:31px}
.m64-os{font-family:Oswald,sans-serif;font-weight:500}
.m64-h{position:absolute;font-family:'Golos Text',sans-serif;font-weight:800;font-size:45px;line-height:56px;letter-spacing:.5px}
.m64-bar{position:absolute;top:262px;height:110px;border-radius:8px;display:flex;align-items:center;justify-content:center;text-align:center;
  font-family:Oswald,sans-serif;font-weight:700;font-size:42px;line-height:40px;color:#fff}
.m64-ch{position:absolute;top:583px;height:76px;border-radius:10px;border:2px solid rgba(42,212,255,.7);background:rgba(10,40,90,.7);
  display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:21px;line-height:29px;color:#f2f6ff}
.m64-lab{position:absolute;font-size:24px;color:#e6efff;text-align:center}
@keyframes m64-go{0%{left:178px;opacity:0}10%{opacity:1}90%{opacity:1}100%{left:438px;opacity:0}}
@keyframes m64-back{0%{left:520px;opacity:0}10%{opacity:1}90%{opacity:1}100%{left:250px;opacity:0}}
@keyframes m64-boom{0%,100%{transform:scale(1);filter:brightness(1)}50%{transform:scale(1.12);filter:brightness(1.4)}}
.m64-pkt{position:absolute;top:381px;width:16px;height:16px;border-radius:4px;background:#2ad4ff;box-shadow:0 0 14px #2ad4ff;animation:m64-go 2.6s linear infinite}
.m64-sig{position:absolute;top:423px;width:16px;height:16px;border-radius:50%;background:#ff4fa8;box-shadow:0 0 14px #ff4fa8;animation:m64-back 2.6s linear infinite 1.3s;opacity:0}
.m64-boom{animation:m64-boom 1.3s ease-in-out infinite}
</style>"""

HTML = CSS + f"""
<div class="m64-pan step" style="left:22px;width:806px"></div>
<div class="step">
  <div class="m64-h" style="left:50px;top:180px;color:#2ad4ff">Чтобы обнаружить коллизию</div>
  <div class="ab" style="left:51px;top:238px;font-size:30px;color:#b9d6ff">Классический Ethernet: half-duplex, CSMA/CD</div>
</div>
<div class="step">
  {img("rep/min64_pcA.png", "left:58px;top:350px;width:112px", "ab")}
  {img("rep/min64_pcB.png", "left:678px;top:350px;width:112px", "ab")}
  <div class="m64-lab" style="left:20px;top:448px;width:190px;line-height:31px"><b class="m64-os" style="font-size:26px;color:#fff">Станция A</b><br>(отправитель)</div>
  <div class="m64-lab" style="left:636px;top:448px;width:190px;line-height:31px"><b class="m64-os" style="font-size:26px;color:#fff">Станция B</b><br>(получатель)</div>
</div>
<div class="step">
  <div class="ab" style="left:175px;top:387px;width:262px;height:3px;background:linear-gradient(90deg,rgba(42,212,255,.3),#2ad4ff);box-shadow:0 0 8px #2ad4ff"></div>
  <div class="ab" style="left:430px;top:373px;color:#2ad4ff;font-size:30px;line-height:30px">➤</div>
  <div class="m64-pkt"></div>
  <div class="ab m64-os" style="left:214px;top:332px;font-size:26px;color:#2ad4ff">Передача кадра</div>
  <div class="ab" style="left:545px;top:388px;width:135px;height:2px;background:#ff4fa8;box-shadow:0 0 6px #ff4fa8;opacity:.8"></div>
</div>
<div class="step">
  <div class="ab m64-boom" style="left:440px;top:350px;width:120px;height:95px">{img("rep/min64_boom.png", "width:120px")}</div>
  <div class="ab m64-os" style="left:478px;top:300px;font-size:27px;color:#ff5fb8">Коллизия</div>
</div>
<div class="step">
  <div class="ab" style="left:262px;top:430px;width:260px;height:3px;background:linear-gradient(90deg,#ff4fa8,rgba(255,79,168,.3));box-shadow:0 0 8px #ff4fa8"></div>
  <div class="ab" style="left:243px;top:416px;color:#ff4fa8;font-size:30px;line-height:30px;transform:scaleX(-1)">➤</div>
  <div class="m64-sig"></div>
  <div class="ab m64-os" style="left:290px;top:442px;width:262px;text-align:center;font-size:26px;line-height:31px;color:#ff5fb8">Сигнал коллизии<br>возвращается</div>
</div>
<div class="step">
  <div class="m64-bx" style="left:40px;top:545px;width:770px;height:125px"></div>
  {img("rep/min64_excl.png", "left:62px;top:560px;width:98px", "ab")}
  <div class="ab" style="left:184px;top:566px;font-size:30px;line-height:40px;color:#fff;font-weight:700">Отправитель должен ещё передавать<br>кадр, когда вернётся сигнал коллизии.</div>
</div>
<div class="step">
  <div class="m64-bx" style="left:40px;top:690px;width:770px;height:83px"></div>
  {img("rep/min64_calc.png", "left:64px;top:702px;width:56px", "ab")}
  <div class="ab" style="left:138px;top:712px;font-size:26px;color:#fff;font-weight:700">512 битовых интервалов → 512 бит ÷ 8 = 64 байта</div>
</div>
<div class="step">
  <div class="m64-bx" style="left:40px;top:793px;width:768px;height:93px"></div>
  {img("rep/min64_info.png", "left:70px;top:806px;width:68px", "ab")}
  <div class="m64-tx" style="left:168px;top:808px">Минимум связан с допустимым временем<br>распространения сигнала туда и обратно.</div>
</div>

<div class="m64-pan step" style="left:846px;width:802px"></div>
<div class="step">
  <div class="m64-h" style="left:846px;top:182px;width:802px;text-align:center;color:#fff;font-size:41px">ИЗ ЧЕГО ПОЛУЧАЮТСЯ 64 БАЙТА</div>
</div>
<div class="step">
  <div class="m64-bar" style="left:866px;width:191px;border:3px solid #2a8dff;background:linear-gradient(180deg,#1a5fe0,#0d2c8a);box-shadow:0 0 16px rgba(42,141,255,.7)">14<br>байт</div>
  <div class="m64-bar" style="left:1060px;width:397px;border:3px solid #2ad4ff;box-shadow:0 0 16px rgba(42,212,255,.7);
    background:repeating-linear-gradient(135deg,rgba(42,212,255,.28) 0 3px,rgba(10,110,140,.75) 3px 16px);transition-delay:150ms">46<br>байт</div>
  <div class="m64-bar" style="left:1461px;width:164px;border:3px solid #b98bff;background:linear-gradient(180deg,#6a2ae0,#38128a);box-shadow:0 0 16px rgba(155,107,255,.7);transition-delay:300ms">4<br>байта</div>
  <div class="m64-lab" style="left:866px;top:386px;width:191px">Заголовок</div>
  <div class="m64-lab" style="left:1060px;top:386px;width:397px">Данные + Padding</div>
  <div class="m64-lab" style="left:1461px;top:386px;width:164px">FCS</div>
</div>
<div class="step">
  <div class="m64-bx" style="left:862px;top:433px;width:768px;height:83px"></div>
  <div class="ab m64-os" style="left:862px;top:440px;width:768px;text-align:center;font-family:'Golos Text',sans-serif;font-weight:800;font-size:54px;line-height:68px;font-weight:700;color:#2ad4ff">14 + 46 + 4 = 64 байта</div>
</div>
<div class="step">
  <div class="m64-bx" style="left:862px;top:533px;width:768px;height:139px"></div>
  <div class="ab m64-os" style="left:878px;top:534px;font-size:29px;color:#2ad4ff">Разбор заголовка (14 байт):</div>
  <div class="m64-ch" style="left:874px;width:198px">MAC назначения<span>6 байт</span></div>
  <div class="ab" style="left:1082px;top:600px;font-size:30px;color:#fff">+</div>
  <div class="m64-ch" style="left:1110px;width:183px">MAC источника<span>6 байт</span></div>
  <div class="ab" style="left:1303px;top:600px;font-size:30px;color:#fff">+</div>
  <div class="m64-ch" style="left:1331px;width:132px">EtherType<span>2 байта</span></div>
  <div class="ab m64-os" style="left:1474px;top:600px;font-size:31px;color:#2ad4ff">= 14 байт</div>
</div>
<div class="step">
  <div class="m64-bx m" style="left:862px;top:688px;width:768px;height:88px"></div>
  {img("rep/min64_doc.png", "left:896px;top:696px;width:68px", "ab")}
  <div class="m64-tx" style="left:1002px;top:702px;font-size:26px;line-height:30px">Если данных меньше 46 байт,<br>добавляется Padding.</div>
</div>
<div class="step">
  <div class="m64-bx" style="left:862px;top:793px;width:768px;height:93px"></div>
  {img("rep/min64_info2.png", "left:876px;top:808px;width:66px", "ab")}
  <div class="m64-tx" style="left:966px;top:806px;font-size:20.5px;line-height:33px">Счёт: от MAC назначения до FCS. Преамбула, SFD и IPG не входят.<br>
    В full-duplex коллизий нет, но минимум 64 байта сохранён.</div>
</div>
"""
