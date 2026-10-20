# -*- coding: utf-8 -*-
"""MACTABLE_AGE — период старения (aging time): вёрстка 1:1 инфографики."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 104
P = "rep/mactable_age_"

CSS = """<style>
.mta-pan{position:absolute;border-radius:12px;border:2px solid #2ad4ff;background:linear-gradient(180deg,rgba(10,34,80,.88),rgba(5,18,48,.92));
  box-shadow:0 0 16px rgba(42,212,255,.55),inset 0 0 22px rgba(42,212,255,.12)}
.mta-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;color:#e8f6ff;letter-spacing:1.2px;line-height:1}
.mta-t{position:absolute;color:#e6f1ff;font-size:23px;line-height:1.25}
.mta-s{position:absolute;color:#e6f1ff;font-size:18px;line-height:1.24}
.mta-code{position:absolute;border-radius:8px;border:1.5px solid rgba(42,212,255,.6);background:rgba(2,10,28,.85);
  font-family:'JetBrains Mono',monospace;color:#eef4ff;font-size:21px;line-height:29px;white-space:pre}
.mta-tk{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:25px;color:#fff;transform:translateX(-50%)}
.mta-tick{position:absolute;width:2px;background:#e6f1ff}
.mta-bar{position:absolute;left:862px;top:378px;width:728px;height:14px;border-radius:7px;
  background:linear-gradient(90deg,#ff3cc8 0%,#1fe0c8 14%,#18e8b8 40%,#2a8cff 60%,#9b6bff 80%,#ff3c9a 100%);box-shadow:0 0 14px rgba(42,212,255,.8)}
.mta-dot{position:absolute;width:20px;height:20px;border-radius:50%;background:#fff;border:3px solid #ff5ccf;box-shadow:0 0 10px #ff5ccf}
.mta-opt{position:absolute;left:943px;top:296px;width:234px;height:112px;border-radius:8px;border:2px solid rgba(42,255,190,.75);
  background:rgba(20,180,140,.22);box-shadow:0 0 18px rgba(42,255,190,.45);animation:mta-glow 2.4s ease-in-out infinite}
@keyframes mta-glow{50%{box-shadow:0 0 34px rgba(42,255,190,.9)}}
.mta-fill{position:absolute;left:56px;top:524px;width:18px;height:22px;border-radius:5px;background:#2ad4ff;box-shadow:0 0 10px #2ad4ff;animation:mta-pulse 1.6s infinite}
@keyframes mta-pulse{50%{opacity:.45}}
.mta-card{position:absolute;top:624px;height:210px;border-radius:12px;border:3px solid;background:rgba(6,16,40,.9)}
.mta-card.o{border-color:#ffb02e;box-shadow:0 0 22px rgba(255,176,46,.7),inset 0 0 26px rgba(255,140,40,.15)}
.mta-card.g{border-color:#2ae8d0;box-shadow:0 0 22px rgba(42,232,208,.7),inset 0 0 26px rgba(42,232,208,.15)}
.mta-card.p{border-color:#ff4fa8;box-shadow:0 0 22px rgba(255,79,168,.7),inset 0 0 26px rgba(255,79,168,.15)}
</style>"""

HTML = CSS + f"""
<div class="step">
  <div class="mta-pan" style="left:28px;top:110px;width:876px;height:82px"></div>
  {img(P + "book.png", "left:50px;top:120px;width:82px", "ab")}
  <div class="ab" style="left:152px;top:124px;width:2px;height:56px;background:#2ad4ff"></div>
  <div class="mta-t" style="left:178px;top:119px;font-size:27px;line-height:31px"><b>Период старения (aging time)</b> — время от изучения<br>MAC-адреса до его удаления из таблицы.</div>
</div>

<div class="step">
  <div class="mta-pan" style="left:20px;top:207px;width:768px;height:403px"></div>
  {img(P + "term.png", "left:40px;top:220px;width:74px", "ab")}
  <div class="mta-h" style="left:130px;top:224px;font-size:29px">ПРОВЕРКА ЗАПОЛНЕНИЯ ТАБЛИЦЫ</div>
  <div class="mta-t" style="left:133px;top:257px">Команда на коммутаторе Eltex:</div>
  <div class="mta-code" style="left:42px;top:294px;width:722px;height:176px;padding:10px 0 0 30px"><b>switch# show mac address-table count</b>
<span style="line-height:36px">Dynamic Address Count: 17</span>
Static Address Count: 0
Total MAC Addresses In Use: 17
Total MAC Address Space Available: 1983</div>
</div>

<div class="step">
  <div class="mta-h" style="left:50px;top:488px;font-size:21px">ИСПОЛЬЗОВАНИЕ ЁМКОСТИ ТАБЛИЦЫ</div>
  <div class="mta-h" style="left:646px;top:490px;font-size:23px;color:#2ad4ff">17 <span style="color:#fff">/ 2000</span></div>
  <div class="ab" style="left:48px;top:518px;width:706px;height:32px;border-radius:9px;border:2px solid #9fe8ff;box-shadow:0 0 10px rgba(42,212,255,.6)"></div>
  <div class="mta-fill"></div>
  <div class="mta-h" style="left:58px;top:557px;font-size:25px;color:#2ad4ff">17</div>
  <div class="mta-h" style="left:58px;top:582px;font-size:17px;color:#2ad4ff">занято</div>
  <div class="mta-h" style="left:692px;top:557px;font-size:22px;color:#2ad4ff">1983</div>
  <div class="mta-h" style="left:680px;top:582px;font-size:17px;color:#2ad4ff">свободно</div>
</div>

<div class="step">
  <div class="mta-pan" style="left:804px;top:207px;width:844px;height:403px"></div>
  {img(P + "watch.png", "left:826px;top:220px;width:72px", "ab")}
  <div class="mta-h" style="left:916px;top:225px;font-size:31px">ПЕРИОД СТАРЕНИЯ (AGING TIME)</div>
  <div class="mta-t" style="left:917px;top:260px">Диапазон значений на коммутаторах Eltex:</div>
  <div class="ab" style="left:1466px;top:240px;width:160px;height:56px;border-radius:7px;border:1.5px solid rgba(42,212,255,.7);background:rgba(6,24,64,.8)"></div>
  {img(P + "glass.png", "left:1474px;top:244px;width:38px", "ab")}
  <div class="mta-s" style="left:1522px;top:250px;font-size:16px;line-height:20px">Значения<br>в секундах</div>
</div>

<div class="step">
  <div class="mta-opt"></div>
  <div class="mta-h" style="left:943px;top:306px;width:234px;text-align:center;font-size:20px;color:#2affc0">ОПТИМАЛЬНО</div>
  <div class="mta-bar"></div>
  <div class="mta-tick" style="left:973px;top:360px;height:22px"></div>
  <div class="mta-tick" style="left:1108px;top:360px;height:34px"></div>
  <div class="mta-tick" style="left:1243px;top:360px;height:40px"></div>
  <div class="mta-tick" style="left:1360px;top:372px;height:12px"></div>
  <div class="mta-tick" style="left:1470px;top:372px;height:12px"></div>
  <div class="mta-dot" style="left:852px;top:375px"></div>
  <div class="mta-dot" style="left:1579px;top:375px"></div>
  <div class="mta-tk" style="left:862px;top:330px">10</div>
  <div class="mta-tk" style="left:974px;top:330px">60</div>
  <div class="mta-tk" style="left:1109px;top:330px">120</div>
  <div class="mta-tk" style="left:1244px;top:330px">300</div>
  <div class="mta-tk" style="left:1587px;top:330px">600</div>
  <div class="mta-s" style="left:846px;top:420px;font-size:17px;line-height:20px"><span style="font-size:24px">&larr;</span> Меньше<br>&nbsp;&nbsp;&nbsp;&nbsp;(быстрее удаление)</div>
  <div class="mta-s" style="left:1412px;top:420px;font-size:17px;line-height:20px;text-align:right">Больше <span style="font-size:24px">&rarr;</span><br>(дольше хранение)&nbsp;&nbsp;&nbsp;&nbsp;</div>
</div>

<div class="step">
  <div class="ab" style="left:818px;top:478px;width:816px;height:120px;border-radius:10px;border:1.5px solid rgba(42,212,255,.55);background:rgba(4,16,44,.7)"></div>
  <div class="mta-t" style="left:842px;top:489px"><b>Настройка периода старения</b> на коммутаторе Eltex:</div>
  <div class="mta-code" style="left:830px;top:526px;width:788px;height:60px;line-height:60px;font-size:23px;padding-left:0"></div>
  {img(P + "term2.png", "left:838px;top:534px;width:56px", "ab")}
  <div class="ab" style="left:918px;top:540px;font-family:'JetBrains Mono',monospace;font-size:23px;color:#eef4ff">switch(config)# mac address-table aging-time <b style="color:#2ad4ff">30</b></div>
</div>

<div class="step">
  <div class="mta-card o" style="left:20px;width:534px"></div>
  {img(P + "warn1.png", "left:40px;top:630px;width:62px", "ab")}
  {img(P + "c1.png", "left:40px;top:678px;width:305px", "ab")}
  <div class="mta-h" style="left:108px;top:640px;font-size:27px;color:#ffc53d">СЛИШКОМ БОЛЬШОЙ ПЕРИОД</div>
  <div class="mta-s" style="left:360px;top:687px">Записи долго<br>не удаляются &rarr;<br>таблица может<br>переполниться &rarr;<br>кадры рассылаются<br>во все порты.</div>
</div>

<div class="step">
  <div class="mta-card g" style="left:566px;width:528px"></div>
  {img(P + "ok.png", "left:588px;top:630px;width:62px", "ab")}
  {img(P + "c2.png", "left:590px;top:678px;width:308px", "ab")}
  <div class="mta-h" style="left:664px;top:641px;font-size:29px;color:#2ae8d0">ОПТИМАЛЬНЫЙ ПЕРИОД</div>
  <div class="mta-s" style="left:907px;top:689px">Освобождает место<br>и сохраняет<br>актуальные<br>соответствия<br>MAC-адресов<br>и портов.</div>
</div>

<div class="step">
  <div class="mta-card p" style="left:1106px;width:542px"></div>
  {img(P + "warn2.png", "left:1126px;top:630px;width:62px", "ab")}
  {img(P + "c3.png", "left:1126px;top:678px;width:302px", "ab")}
  <div class="mta-h" style="left:1197px;top:641px;font-size:27px;color:#ff6fc0">СЛИШКОМ КОРОТКИЙ ПЕРИОД</div>
  <div class="mta-s" style="left:1444px;top:692px">Записи удаляются<br>слишком часто &rarr;<br>растёт неизвестный<br>одноадресный<br>трафик.</div>
</div>

<div class="step">
  <div class="mta-pan" style="left:20px;top:850px;width:1630px;height:76px;border-radius:10px"></div>
  {img(P + "bulb.png", "left:60px;top:856px;width:68px", "ab")}
  <div class="ab" style="left:152px;top:868px;width:3px;height:44px;background:#2ad4ff"></div>
  <div class="mta-t" style="left:183px;top:873px;font-size:26px;font-weight:600">Значение aging time выбирают с учётом ёмкости таблицы и характера сетевого трафика.</div>
</div>
"""
