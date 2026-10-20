# -*- coding: utf-8 -*-
"""MAC_ADDR — MAC-адреса: вёрстка 1:1 инфографики (pptx 9)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 168

CSS = """<style>
.mac-pan{position:absolute;border-radius:10px;border:1.5px solid rgba(42,212,255,.6);background:rgba(6,20,52,.82);box-shadow:0 0 14px rgba(42,212,255,.3)}
.mac-os{font-family:Oswald,sans-serif;font-weight:500}
.mac-tx{position:absolute;color:#eef3ff;font-family:'Golos Text',sans-serif;font-size:22px;line-height:30px}
.mac-tx em{color:#2ad4ff;font-style:normal}
.mac-mono{font-family:'JetBrains Mono',monospace;font-weight:700}
.mac-g{position:absolute;top:393px;height:58px;display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:33px;color:#bfefff}
.mac-st{position:absolute;top:347px;height:140px;border-radius:8px;border:1.5px solid rgba(42,212,255,.6);background:rgba(10,34,76,.75);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;text-align:center;font-size:16px;line-height:19px;color:#eef3ff}
.mac-cd{position:absolute;top:588px;height:332px;border-radius:8px;border:1.5px solid rgba(42,212,255,.55);background:rgba(6,20,52,.82);box-shadow:0 0 12px rgba(42,212,255,.25)}
.mac-cd b{position:absolute;left:30px;top:8px;font-family:Oswald,sans-serif;font-weight:700;font-size:38px;color:#fff;line-height:48px}
.mac-cd i{position:absolute;left:30px;top:48px;font-style:normal;font-family:Oswald,sans-serif;font-weight:500;font-size:25px;color:#2ad4ff}
.mac-adr{position:absolute;height:38px;border-radius:6px;border:2px solid #2ad4ff;background:rgba(8,40,90,.8);box-shadow:0 0 10px rgba(42,212,255,.5);
  display:flex;align-items:center;justify-content:center;font-family:'JetBrains Mono',monospace;font-weight:700;font-size:23px;color:#bfefff}
@keyframes mac-blink{0%,100%{opacity:.35}50%{opacity:1}}
.mac-arw{animation:mac-blink 1.4s ease-in-out infinite;color:#2ad4ff}
@keyframes mac-glow{0%,100%{box-shadow:0 0 12px rgba(42,212,255,.5)}50%{box-shadow:0 0 28px rgba(42,212,255,.95)}}
</style>"""


def _groups():
    xs = [(450, 100), (550, 106), (656, 107), (763, 108), (871, 116), (987, 118)]
    gs = ["00", "1A", "2B", "3C", "4D", "5E"]
    return "".join('<div class="mac-g" style="left:%dpx;width:%dpx;transition-delay:%dms">%s</div>' % (x, w, k * 80, g)
                   for k, ((x, w), g) in enumerate(zip(xs, gs)))


def _brk(x0, x1, cx):
    return ('<div class="ab" style="left:%dpx;top:462px;width:%dpx;height:10px;border:1.5px solid #9fb8e8;border-top:none"></div>'
            '<div class="ab" style="left:%dpx;top:471px;width:1.5px;height:8px;background:#9fb8e8"></div>' % (x0, x1 - x0, cx))


HTML = CSS + f"""
<div class="step">
  <div class="mac-pan" style="left:28px;top:190px;width:374px;height:250px"></div>
  <div class="mac-tx" style="left:52px;top:206px;width:340px">MAC-адрес идентифицирует сетевой интерфейс в <em>канальном уровне Ethernet.</em></div>
  <div class="mac-tx" style="left:52px;top:316px;width:340px">Обычно записывается шестью группами шестнадцатеричных символов.</div>
</div>
<div class="step">
  {img("rep/mac_addr_hero.png", "left:430px;top:150px;width:1242px", "ab")}
  <div class="ab mac-os" style="left:450px;top:300px;font-size:21px;color:#fff">Компьютер</div>
</div>
<div class="step">
  <div class="ab mac-mono" style="left:612px;top:312px;width:453px;height:68px;border-radius:10px;border:2px solid #2ad4ff;background:rgba(8,40,90,.85);
    animation:mac-glow 2.4s ease-in-out infinite;display:flex;align-items:center;justify-content:center;font-size:37px;color:#bfefff;letter-spacing:1px">00:1A:2B:3C:4D:5E</div>
</div>
<div class="step">
  <div class="ab" style="left:450px;top:393px;width:655px;height:58px;border-radius:10px;border:2px solid #2ad4ff;background:rgba(8,30,70,.85);box-shadow:0 0 14px rgba(42,212,255,.5)"></div>
  {''.join('<div class="ab" style="left:%dpx;top:405px;width:2px;height:34px;background:rgba(42,212,255,.6)"></div>' % x for x in (550, 656, 763, 871, 987))}
  {_groups()}
</div>
<div class="step">
  {_brk(460, 563, 511)}{_brk(598, 930, 763)}{_brk(968, 1086, 1027)}
  <div class="ab" style="left:440px;top:484px;width:144px;text-align:center;font-size:20px;color:#e6efff">6 групп</div>
  <div class="ab" style="left:590px;top:484px;width:346px;text-align:center;font-size:20px;color:#e6efff">по 2 шестнадцатеричных символа</div>
  <div class="ab" style="left:948px;top:484px;width:160px;text-align:center;font-size:20px;color:#e6efff">48 бит = 6 байт</div>
</div>
<div class="step">
  <div class="mac-pan" style="left:1130px;top:285px;width:520px;height:225px;border-color:rgba(42,212,255,.45)"></div>
  <div class="ab mac-os" style="left:1158px;top:294px;font-size:27px;color:#2ad4ff">КАК РАБОТАЕТ?</div>
  <div class="ab" style="left:1158px;top:333px;width:40px;height:2px;background:#2ad4ff"></div>
  <div class="mac-st" style="left:1142px;width:100px">{img("rep/mac_addr_doc.png", "width:46px")}<span>Кадр<br>Ethernet</span></div>
  <div class="mac-st" style="left:1271px;width:99px">{img("rep/mac_addr_nic.png", "width:66px")}<span>Сетевая<br>карта (NIC)</span></div>
  <div class="mac-st" style="left:1398px;width:95px">{img("rep/mac_addr_gear.png", "width:50px")}<span>Проверка<br>D.MAC</span></div>
  <div class="mac-st" style="left:1520px;width:120px;gap:2px">{img("rep/mac_addr_ok.png", "width:34px")}<span style="font-size:14px;line-height:17px">Принять<br>или отбросить</span>{img("rep/mac_addr_no.png", "width:34px")}</div>
  <div class="ab mac-arw" style="left:1243px;top:393px;font-size:26px">➜</div>
  <div class="ab mac-arw" style="left:1371px;top:393px;font-size:26px;animation-delay:.3s">➜</div>
  <div class="ab mac-arw" style="left:1493px;top:393px;font-size:26px;animation-delay:.6s">➜</div>
</div>
<div class="step">
  <div class="ab" style="left:18px;top:554px;width:400px;height:2px;background:linear-gradient(90deg,rgba(42,212,255,.2),#2ad4ff)"></div>
  <div class="ab" style="left:1254px;top:554px;width:400px;height:2px;background:linear-gradient(90deg,#2ad4ff,rgba(42,212,255,.2))"></div>
  <div class="ab mac-os" style="left:0;top:530px;width:1672px;text-align:center;font-size:42px;line-height:52px;font-weight:700;color:#fff">ОСНОВНЫЕ ВИДЫ <span style="color:#2ad4ff">MAC-АДРЕСОВ</span></div>
</div>
<div class="step">
  <div class="mac-cd" style="left:16px;width:540px"></div>
  {img("rep/mac_addr_uni.png", "left:36px;top:668px;width:496px", "ab")}
  <div class="mac-cd" style="left:16px;width:10px;height:0;border:none;background:none;box-shadow:none"><b style="white-space:nowrap">UNICAST</b><i style="white-space:nowrap">Адрес одного устройства</i></div>
  <div class="ab" style="left:46px;top:827px;width:488px;height:80px;border-radius:8px;border:1px solid rgba(42,212,255,.4)"></div>
  <div class="ab" style="left:66px;top:833px;font-size:17px;color:#e6efff">Пример MAC-адреса:</div>
  <div class="mac-adr" style="left:162px;top:859px;width:262px">00:1A:2B:3C:4D:5E</div>
</div>
<div class="step">
  <div class="mac-cd" style="left:572px;width:525px"></div>
  {img("rep/mac_addr_bro.png", "left:588px;top:665px;width:492px", "ab")}
  <div class="mac-cd" style="left:572px;width:10px;height:0;border:none;background:none;box-shadow:none"><b style="white-space:nowrap">BROADCAST</b><i style="white-space:nowrap">Адрес всех устройств сети</i></div>
  <div class="ab" style="left:594px;top:827px;width:480px;height:80px;border-radius:8px;border:1px solid rgba(42,212,255,.4)"></div>
  <div class="ab" style="left:612px;top:833px;font-size:17px;color:#e6efff">MAC-адрес широковещательной рассылки:</div>
  <div class="mac-adr" style="left:700px;top:859px;width:270px">FF:FF:FF:FF:FF:FF</div>
</div>
<div class="step">
  <div class="mac-cd" style="left:1113px;width:542px"></div>
  {img("rep/mac_addr_mul.png", "left:1130px;top:660px;width:515px", "ab")}
  <div class="mac-cd" style="left:1113px;width:10px;height:0;border:none;background:none;box-shadow:none"><b style="white-space:nowrap">MULTICAST</b><i style="white-space:nowrap">Адрес определённой группы устройств</i></div>
  <div class="ab" style="left:1130px;top:832px;width:228px;white-space:nowrap;height:40px;border-radius:6px;border:1.5px solid rgba(42,212,255,.6);background:rgba(8,30,70,.85);
    display:flex;align-items:center;justify-content:center;font-size:18px;color:#e6efff">Одна группа получателей</div>
</div>
"""
