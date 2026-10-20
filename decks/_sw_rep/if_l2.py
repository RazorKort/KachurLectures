# -*- coding: utf-8 -*-
"""Интерфейсы уровня L2 — вёрстка 1:1 (заголовок у оригинала слева, полосы сверху нет)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 40

CSS = """<style>
.il2-pan{position:absolute;border:2px solid #2ad4ff;border-radius:12px;background:rgba(6,22,60,.78);box-shadow:0 0 16px rgba(42,212,255,.5),inset 0 0 26px rgba(42,212,255,.12)}
.il2-pan.s{border-width:1.5px;border-color:rgba(42,212,255,.55);box-shadow:none;background:rgba(8,28,72,.6)}
.il2-ct{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:25px;color:#fff;text-align:center}
.il2-tx{position:absolute;font-family:'Golos Text',sans-serif;font-size:17px;line-height:1.2;color:#e6f1ff;text-align:center}
.il2-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:30px;color:#fff;letter-spacing:.5px}
.il2-ul{position:absolute;height:4px;width:60px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff}
.il2-col{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:23px;line-height:1.1;color:#fff;text-align:center}
.il2-col i{font-style:normal;color:#2ad4ff}
.il2-li{position:absolute;display:flex;align-items:center;gap:14px;font-family:'Golos Text',sans-serif;font-size:13.5px;color:#e6f1ff;white-space:nowrap}
.il2-st{position:absolute;border:2px solid #ff4d5e;border-radius:12px;background:rgba(60,10,20,.55);box-shadow:0 0 14px rgba(255,77,94,.6),inset 0 0 18px rgba(255,77,94,.15)}
.il2-st b{position:absolute;top:10px;font-family:Oswald,sans-serif;font-weight:500;font-size:24px;color:#ff6a3d}
.il2-st b small{font-size:22px;font-weight:400}
.il2-st span{position:absolute;font-family:'Golos Text',sans-serif;font-size:14px;line-height:1.22;color:#fff}
.il2-cmd{position:absolute;height:34px;border:1.5px solid #2ad4ff;border-radius:6px;background:rgba(8,30,70,.85);display:flex;align-items:center;padding-left:10px;
  font-family:'JetBrains Mono',monospace;font-size:15px;color:#fff;white-space:nowrap;box-shadow:0 0 8px rgba(42,212,255,.4)}
.il2-cmd::before{content:'>';color:#2ad4ff;margin-right:12px}
.il2-wire path{fill:none;stroke:#2ad4ff;stroke-width:3;filter:drop-shadow(0 0 4px #2ad4ff)}
.il2-wire .r{stroke:#ff6a3d;filter:drop-shadow(0 0 4px #ff4d5e)}
.il2-pk{position:absolute;width:16px;height:10px;border-radius:3px;background:#bff6ff;box-shadow:0 0 10px #2ad4ff;animation:il2go 3s linear infinite}
@keyframes il2go{0%{transform:translateX(0);opacity:0}10%{opacity:1}90%{opacity:1}100%{transform:translateX(560px);opacity:0}}
.il2-led{animation:il2blink 1.1s steps(2) infinite}
@keyframes il2blink{50%{opacity:.25}}
</style>"""


def _li(x, y, items):
    return "".join('<div class="il2-li" style="left:%dpx;top:%dpx">%s%s</div>' % (x, y + i * 34, img("rep/if_l2_ok.png", "width:28px"), t)
                   for i, t in enumerate(items))


def _card(x, w, title, ic, icst, text, d):
    return ('<div class="step" style="transition-delay:%dms"><div class="il2-pan" style="left:%dpx;top:84px;width:%dpx;height:222px"></div>'
            '<div class="il2-ct" style="left:%dpx;top:102px;width:%dpx">%s</div>%s'
            '<div class="il2-tx" style="left:%dpx;top:256px;width:%dpx">%s</div></div>') % (d, x, w, x, w, title, img("rep/" + ic, icst, "ab"), x, w, text)


HTML = CSS + f"""
<div class="step">
  <div class="il2-pan" style="left:34px;top:44px;width:560px;height:290px;border-radius:18px;background:rgba(6,22,60,.6)"></div>
  <div class="ab" style="left:68px;top:76px;font-family:Oswald,sans-serif;font-weight:700;font-size:86px;line-height:.95;color:#fff">ИНТЕРФЕЙСЫ<br><span style="color:#2ad4ff">УРОВНЯ L2</span></div>
  <div class="il2-ul" style="left:76px;top:254px;width:190px"></div>
  <div class="ab" style="left:74px;top:270px;font-family:Oswald,sans-serif;font-size:19px;letter-spacing:4px;line-height:1.1;color:#cfe0ff">РАБОТАЕМ С КАДРАМИ<br>НА КАНАЛЬНОМ УРОВНЕ</div>
  <div class="il2-pan s" style="left:62px;top:346px;width:282px;height:178px"></div>
  {img("rep/if_l2_i1.png", "left:82px;top:360px;width:52px", "ab")}
  {img("rep/if_l2_i2.png", "left:82px;top:412px;width:52px", "ab")}
  {img("rep/if_l2_i3.png", "left:82px;top:464px;width:52px", "ab")}
  <div class="ab os" style="left:152px;top:370px;font-family:Oswald,sans-serif;font-size:17px;line-height:52px;color:#cfe0ff">КОММУТАЦИЯ<br>MAC-АДРЕСА<br>ЛОКАЛЬНАЯ СЕТЬ (L2)</div>
</div>

{_card(614, 266, "ПОЛУЧЕНИЕ КАДРА", "if_l2_cab1.png", "left:620px;top:150px;width:250px", "Порт принимает<br>кадр из сети", 0)}
{_card(896, 296, "ПРОВЕРКА ЦЕЛОСТНОСТИ", "if_l2_fcs.png", "left:975px;top:145px;width:145px", "Проверяется целостность<br>кадра (FCS)", 150)}
{_card(1208, 278, "ОТПРАВКА КАДРА", "if_l2_cab2.png", "left:1228px;top:150px;width:234px", "Кадр отправляется<br>на нужный порт", 300)}

<div class="step">
  <svg class="ab il2-wire" style="left:0;top:0;width:1672px;height:941px" viewBox="0 0 1672 941">
    <path d="M865 198H915"/><path d="M915 198l-12-8M915 198l-12 8"/>
    <path d="M1160 198H1222"/><path d="M1222 198l-12-8M1222 198l-12 8"/>
    <path d="M714 306V348H740V372"/><path d="M922 306V372"/><path d="M1354 306V348H1088V372"/><path d="M780 348H1088"/>
  </svg>
  <div class="il2-pk" style="left:640px;top:193px"></div>
</div>

<div class="step">
  {img("rep/if_l2_sw.png", "left:345px;top:352px;width:1031px", "ab")}
  <div class="ab il2-led" style="left:1270px;top:475px;width:12px;height:12px;border-radius:50%;background:#ffc53d;box-shadow:0 0 10px #ffc53d"></div>
</div>

<div class="step">
  <div class="il2-pan" style="left:140px;top:530px;width:654px;height:374px"></div>
  <div class="il2-h" style="left:178px;top:536px">ИНТЕРФЕЙСЫ ПО УМОЛЧАНИЮ</div>
  <div class="il2-ul" style="left:178px;top:580px"></div>
  <div class="il2-pan s" style="left:152px;top:584px;width:630px;height:304px"></div>
  <div class="ab" style="left:458px;top:604px;width:2px;height:262px;background:rgba(42,212,255,.4)"></div>
</div>

<div class="step">
  <div class="il2-col" style="left:162px;top:598px;width:284px">КОММУТАТОР:<br><i>SWITCHPORT (L2) —</i><br>ПО УМОЛЧАНИЮ</div>
  {img("rep/if_l2_swi.png", "left:208px;top:684px;width:190px", "ab")}
  {_li(162, 774, ["Работает на канальном уровне", "Коммутирует кадры по MAC-адресам", "Используется в локальной сети (VLAN)"])}
</div>

<div class="step">
  <div class="il2-col" style="left:486px;top:598px;width:280px">МАРШРУТИЗАТОР:<br><i>ROUTERPORT (L3) —</i><br>ПО УМОЛЧАНИЮ</div>
  {img("rep/if_l2_rt.png", "left:560px;top:678px;width:132px", "ab")}
  {_li(476, 774, ["Работает на сетевом уровне", "Маршрутизирует пакеты по IP-адресам", "Разделяет сети"])}
</div>

<div class="step">
  <div class="il2-pan" style="left:808px;top:530px;width:726px;height:374px"></div>
  <div class="il2-h" style="left:836px;top:536px">СОСТОЯНИЯ ПОРТА</div>
  <div class="il2-ul" style="left:836px;top:580px"></div>
  <div class="ab" style="left:982px;top:586px;width:366px;height:78px;border:2px solid #9dfc5a;border-radius:10px;background:rgba(10,50,30,.6);box-shadow:0 0 14px rgba(157,252,90,.6)"></div>
  {img("rep/if_l2_up.png", "left:996px;top:596px;width:58px", "ab")}
  <div class="ab" style="left:1078px;top:600px;font-family:Oswald,sans-serif;font-weight:500;font-size:34px;color:#9dfc5a">UP</div>
  <div class="ab" style="left:1146px;top:602px;width:2px;height:48px;background:#9dfc5a"></div>
  <div class="ab" style="left:1166px;top:595px;font-size:16px;line-height:1.25;color:#fff">кабель подключён,<br>устройство работает,<br>идёт UPTIME</div>
</div>

<div class="step">
  <svg class="ab il2-wire" style="left:0;top:0;width:1672px;height:941px" viewBox="0 0 1672 941">
    <path class="r" d="M1100 664V670H932V692M1170 670V692M1100 670H1404V692"/>
  </svg>
  <div class="il2-st" style="left:824px;top:696px;width:208px;height:106px"><b style="left:76px">DOWN <small>(nc)</small></b><span style="left:76px;top:44px">нет подключения<br>или устройство<br>не работает</span></div>
  {img("rep/if_l2_nc.png", "left:836px;top:706px;width:58px", "ab")}
  <div class="il2-st" style="left:1052px;top:696px;width:236px;height:106px"><b style="left:78px">DOWN <small>(adm)</small></b><span style="left:78px;top:44px">порт отключён<br>командой <b style="position:static;font-family:'Golos Text';font-size:14px;color:#fff">shutdown</b></span></div>
  {img("rep/if_l2_adm.png", "left:1062px;top:706px;width:58px", "ab")}
  <div class="il2-st" style="left:1306px;top:696px;width:212px;height:106px"><b style="left:76px">DOWN <small>(err)</small></b><span style="left:76px;top:44px">порт отключён<br>коммутатором<br>из-за ошибки</span></div>
  {img("rep/if_l2_err.png", "left:1318px;top:706px;width:56px", "ab")}
</div>

<div class="step">
  <div class="il2-pan s" style="left:1054px;top:806px;width:234px;height:84px"></div>
  <div class="ab" style="left:1054px;top:816px;width:234px;text-align:center;font-family:Oswald,sans-serif;font-size:14px;color:#fff">ВОССТАНОВЛЕНИЕ:</div>
  <div class="il2-cmd" style="left:1072px;top:840px;width:178px;color:#9ff0ff">no shutdown</div>
  <div class="il2-pan s" style="left:1306px;top:806px;width:212px;height:84px"></div>
  <div class="ab" style="left:1306px;top:816px;width:212px;text-align:center;font-family:Oswald,sans-serif;font-size:14px;color:#fff">ВОССТАНОВЛЕНИЕ:</div>
  <div class="il2-cmd" style="left:1316px;top:840px;width:182px;font-size:12px;font-family:Golos Text,sans-serif">shutdown → no shutdown</div>
</div>
"""
