# -*- coding: utf-8 -*-
"""MACTABLE — таблица коммутации (show mac address-table): вёрстка 1:1 инфографики."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 192
P = "rep/mactable_"

CSS = """<style>
.mt-pan{position:absolute;border-radius:10px;border:2px solid #2ad4ff;background:linear-gradient(180deg,rgba(10,34,80,.86),rgba(5,18,48,.9));
  box-shadow:0 0 16px rgba(42,212,255,.55),inset 0 0 22px rgba(42,212,255,.12)}
.mt-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;letter-spacing:.6px;line-height:1;color:#2ad4ff}
.mt-t{position:absolute;color:#e6f1ff;font-size:23px;line-height:1.22}
.mt-dev{position:absolute;border-radius:8px;border:1.5px solid rgba(42,212,255,.7);background:rgba(4,16,44,.82);box-shadow:0 0 10px rgba(42,212,255,.4)}
.mt-cli{position:absolute;font-family:'JetBrains Mono',monospace;color:#eef4ff;font-size:22px;line-height:36px;white-space:pre}
.mt-row{position:absolute;left:870px;width:770px;height:34px;border-radius:5px;background:rgba(42,212,255,0);animation:mt-hl 4s infinite}
@keyframes mt-hl{0%,40%,100%{background:rgba(42,212,255,0)}15%,25%{background:rgba(42,212,255,.22)}}
.mt-pkt{position:absolute;width:16px;height:16px;border-radius:50%;background:#fff;box-shadow:0 0 12px 4px #2ad4ff;opacity:0}
.mt-pkt.a{left:250px;top:486px;animation:mt-fa 3s 1s infinite}
.mt-pkt.b{left:654px;top:478px;box-shadow:0 0 12px 4px #ff4fd8;animation:mt-fb 3s 2.5s infinite}
@keyframes mt-fa{0%{opacity:0;transform:translate(0,0)}10%{opacity:1}50%{transform:translate(10px,-50px)}90%{opacity:1;transform:translate(196px,-104px)}100%{opacity:0;transform:translate(196px,-104px)}}
@keyframes mt-fb{0%{opacity:0;transform:translate(0,0)}10%{opacity:1}50%{transform:translate(-40px,-56px)}90%{opacity:1;transform:translate(-122px,-90px)}100%{opacity:0;transform:translate(-122px,-90px)}}
.mt-card{position:absolute;top:686px;height:122px;border-radius:10px;border:2px solid rgba(42,212,255,.75);background:rgba(4,18,48,.85);box-shadow:0 0 14px rgba(42,212,255,.45)}
</style>"""


def _card(x, w, ic, icw, title, txt, d, tx=146):
    return ('<div class="step" style="transition-delay:%dms"><div class="mt-card" style="left:%dpx;width:%dpx"></div>%s'
            '<div class="mt-h" style="left:%dpx;top:710px;font-size:28px">%s</div>'
            '<div class="mt-t" style="left:%dpx;top:744px">%s</div></div>'
            % (d, x, w, img(P + ic, "left:%dpx;top:700px;width:%dpx" % (x + 12, icw), "ab"), x + tx, title, x + tx, txt))


HTML = CSS + f"""
<div class="step">
  <div class="ab" style="left:322px;top:196px;width:312px;height:64px;border-radius:10px 10px 0 0;border:2px solid rgba(42,212,255,.55);border-bottom:none;background:rgba(6,24,64,.55)"></div>
  <div class="mt-h" style="left:322px;top:206px;width:312px;text-align:center;font-size:25px">КОММУТАТОР</div>
  <div class="ab" style="left:322px;top:232px;width:312px;text-align:center;font-size:19px;color:#e6f1ff">(L2, Ethernet Switch)</div>
  {img(P + "scene.webp", "left:40px;top:258px;width:790px", "ab")}
  <div class="mt-pkt a"></div><div class="mt-pkt b"></div>
</div>

<div class="step">
  <div class="mt-dev" style="left:82px;top:590px;width:260px;height:82px"></div>
  <div class="mt-h" style="left:103px;top:597px;font-size:23px;color:#2ad4ff">Устройство A</div>
  <div class="mt-t" style="left:103px;top:623px;font-size:19px;line-height:23px">MAC: 34:60:f9:5f:df:5f<br>VLAN: 10</div>
  <div class="mt-dev" style="left:554px;top:590px;width:256px;height:82px;transition-delay:.2s"></div>
  <div class="mt-h" style="left:576px;top:597px;font-size:23px;color:#2ad4ff">Устройство B</div>
  <div class="mt-t" style="left:576px;top:623px;font-size:19px;line-height:23px">MAC: a0:a3:f0:d1:26:5a<br>VLAN: 10</div>
</div>

<div class="step">
  <div class="mt-pan" style="left:856px;top:222px;width:796px;height:394px;border-radius:14px"></div>
  <div class="mt-h" style="left:902px;top:240px;font-size:29px">ТАБЛИЦА&nbsp; MAC-АДРЕСОВ КОММУТАТОРА</div>
  <div class="ab" style="left:866px;top:282px;width:776px;height:282px;border-radius:10px;border:1.5px solid rgba(42,212,255,.6);background:rgba(2,10,28,.86)"></div>
  <div class="mt-cli" style="left:886px;top:301px;font-size:24px">switch# show mac address-table</div>
</div>

<div class="step">
  <div class="mt-row" style="top:404px"></div>
  <div class="mt-row" style="top:440px;animation-delay:2s"></div>
  <div class="mt-cli" style="left:886px;top:359px;font-size:20px;line-height:20px">VID</div>
  <div class="mt-cli" style="left:974px;top:359px;font-size:20px;line-height:20px">MAC Address</div>
  <div class="mt-cli" style="left:1212px;top:359px;font-size:20px;line-height:20px">Interface</div>
  <div class="mt-cli" style="left:1536px;top:359px;font-size:20px;line-height:20px">Type</div>
  <div class="mt-cli" style="left:886px;top:390px;font-size:20px;line-height:20px">-----</div>
  <div class="mt-cli" style="left:974px;top:390px;font-size:20px;line-height:20px">-----------------</div>
  <div class="mt-cli" style="left:1212px;top:390px;font-size:20px;line-height:20px">-------------------------</div>
  <div class="mt-cli" style="left:1536px;top:390px;font-size:20px;line-height:20px">-------</div>
  <div class="mt-cli" style="left:886px;top:412px;font-size:20px;line-height:20px">10</div>
  <div class="mt-cli" style="left:974px;top:412px;font-size:20px;line-height:20px">34:60:f9:5f:df:5f</div>
  <div class="mt-cli" style="left:1212px;top:412px;font-size:20px;line-height:20px">gigabitethernet 1/0/2</div>
  <div class="mt-cli" style="left:1536px;top:412px;font-size:20px;line-height:20px">Dynamic</div>
  <div class="mt-cli" style="left:886px;top:448px;font-size:20px;line-height:20px">10</div>
  <div class="mt-cli" style="left:974px;top:448px;font-size:20px;line-height:20px">a0:a3:f0:d1:26:5a</div>
  <div class="mt-cli" style="left:1212px;top:448px;font-size:20px;line-height:20px">gigabitethernet 1/0/6</div>
  <div class="mt-cli" style="left:1536px;top:448px;font-size:20px;line-height:20px">Dynamic</div>
  <div class="mt-cli" style="left:886px;top:497px;font-size:20px;line-height:20px">2 valid mac entries</div>
</div>

{_card(32, 356, "ic1.png", 120, "VID", "идентификатор<br>VLAN", 0, 144)}
{_card(404, 392, "ic2.png", 120, "MAC Address", "адрес устройства", 120, 174)}
{_card(812, 384, "ic3.png", 102, "Interface", "порт коммутатора", 240, 160)}
{_card(1210, 430, "ic4.png", 95, "Type", "способ изучения<br>записи", 360, 166)}

<div class="step">
  <div class="mt-pan" style="left:32px;top:826px;width:1606px;height:84px"></div>
  {img(P + "bulb.png", "left:50px;top:836px;width:75px", "ab")}
  {img(P + "chev.png", "left:150px;top:840px;width:50px", "ab")}
  {img(P + "hatch.png", "left:1500px;top:840px;width:120px", "ab")}
  <div class="mt-t" style="left:232px;top:850px;font-size:29px;font-weight:500"><b style="color:#2ad4ff">Коммутатор</b> использует эти соответствия, чтобы <b style="color:#ffd84a">отправлять кадры в нужные порты.</b></div>
</div>
"""
