# -*- coding: utf-8 -*-
"""Режимы работы портов: ACCESS / TRUNK / GENERAL / CUSTOMER — вёрстка 1:1 (pptx 55)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 180

CSS = """<style>
.pm-card{position:absolute;top:416px;height:434px;border-radius:14px;border:3px solid var(--c);background:linear-gradient(180deg,rgba(8,26,70,.9),rgba(6,14,44,.94));
  box-shadow:0 0 22px var(--g),inset 0 0 30px var(--gi)}
.pm-num{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:30px;color:var(--c);padding:0 12px;border:2px solid var(--c);border-radius:6px;
  background:rgba(0,0,0,.35);line-height:38px}
.pm-t{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:48px;line-height:1;color:var(--c);text-shadow:0 0 14px var(--g)}
.pm-s{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:23px;color:var(--c);text-align:center}
.pm-hr{position:absolute;height:2px;background:var(--c);opacity:.55}
.pm-tx{position:absolute;color:#e6f1ff;font-size:19px;line-height:1.38}
.pm-ft{position:absolute;font-family:Oswald,sans-serif;font-weight:300;font-size:19px;color:#e6f1ff;text-align:center;letter-spacing:.02em}
.pm-tag{position:absolute;font-family:Oswald,sans-serif;font-size:16px;color:#fff;text-align:center;border:2px solid var(--c);border-radius:5px;background:rgba(10,30,70,.85);
  box-shadow:0 0 10px var(--g);line-height:26px}
.pm-arr{position:absolute;height:3px;background:var(--c);box-shadow:0 0 8px var(--c)}
.pm-arr:after{content:"";position:absolute;right:-4px;top:-6px;border:7px solid transparent;border-left:11px solid var(--c);border-right:0}
.pm-arr.b:before{content:"";position:absolute;left:-4px;top:-6px;border:7px solid transparent;border-right:11px solid var(--c);border-left:0}
.pm-lb{position:absolute;font-family:Oswald,sans-serif;font-size:17px;line-height:1.1;color:#e6f1ff;text-align:center}
.pm-pkt{position:absolute;width:12px;height:12px;border-radius:50%;background:#fff;box-shadow:0 0 10px var(--c),0 0 4px #fff;animation:pmfly 2.4s linear infinite}
@keyframes pmfly{0%{transform:translateX(0);opacity:0}10%{opacity:1}90%{opacity:1}100%{transform:translateX(var(--d));opacity:0}}
.pm-ico{position:absolute;text-align:center;font-family:Oswald,sans-serif;font-size:15px;color:#2ad4ff}
.pm-ico.w{color:#fff}
</style>"""

A = "--c:#2ad4ff;--g:rgba(42,212,255,.6);--gi:rgba(42,212,255,.15)"
T = "--c:#e05cff;--g:rgba(224,92,255,.6);--gi:rgba(224,92,255,.15)"
G = "--c:#4fa8ff;--g:rgba(79,168,255,.6);--gi:rgba(79,168,255,.15)"
C = "--c:#ffb43d;--g:rgba(255,180,61,.6);--gi:rgba(255,180,61,.12)"


def head(x, st, n, t, s, tw=None):
    return (f'<div class="pm-card" style="{st};left:{x}px;width:394px"></div>'
            f'<div class="pm-num" style="{st};left:{x+12}px;top:432px">{n}</div>'
            f'<div class="pm-t" style="{st};left:{x}px;width:394px;top:436px;text-align:center;padding-left:{tw or 0}px">{t}</div>'
            f'<div class="pm-s" style="{st};left:{x}px;width:394px;top:486px">{s}</div>'
            f'<div class="pm-hr" style="{st};left:{x+18}px;top:522px;width:358px"></div>'
            f'<div class="pm-hr" style="{st};left:{x+18}px;top:806px;width:358px"></div>')


HTML = CSS + f"""
<div class="ab" style="left:68px;top:236px;font-family:Oswald,sans-serif;font-weight:500;font-size:23px;color:#cfe6ff;letter-spacing:.01em">КОММУТАТОР ПОДДЕРЖИВАЕТ ЧЕТЫРЕ РЕЖИМА</div>
<div class="ab" style="left:68px;top:272px;width:74px;height:4px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff"></div>
<div class="step">
  <div class="ab" style="left:40px;top:294px;width:540px;height:102px;border:2px solid rgba(42,212,255,.6);border-radius:8px;background:rgba(6,22,60,.7);
    clip-path:polygon(0 0,100% 0,88% 100%,0 100%)"></div>
  {img("rep/port_modes_eth.png", "left:78px;top:305px;width:64px", "ab")}<div class="pm-ico" style="left:60px;top:360px;width:100px">ETHERNET</div>
  {img("rep/port_modes_vlan.png", "left:192px;top:305px;width:52px", "ab")}<div class="pm-ico w" style="left:168px;top:360px;width:100px">VLAN</div>
  {img("rep/port_modes_q.png", "left:296px;top:305px;width:56px", "ab")}<div class="pm-ico w" style="left:274px;top:360px;width:100px">802.1Q</div>
  {img("rep/port_modes_shield.png", "left:403px;top:308px;width:51px", "ab")}<div class="pm-ico w" style="left:378px;top:355px;width:100px;line-height:1.05">НАДЕЖНАЯ<br>СЕТЬ</div>
</div>
<div class="step">{img("rep/port_modes_sw.png", "left:600px;top:185px;width:1022px", "ab")}</div>

<div class="step">
{head(22, A, "01", "ACCESS", "ИНТЕРФЕЙС ДОСТУПА", 30)}
<div class="pm-tx" style="left:46px;top:534px;width:350px">Нетегированный интерфейс<br>для одной VLAN</div>
{img("rep/port_modes_pc.png", "left:36px;top:636px;width:104px", "ab")}
<div class="pm-lb" style="left:40px;top:736px;width:70px">ПК<br>(КЛИЕНТ)</div>
<div class="pm-tag" style="{A};left:170px;top:640px;width:118px">UNTAGGED</div>
<div class="pm-arr" style="{A};left:146px;top:685px;width:166px"></div>
<div class="pm-pkt" style="{A};left:150px;top:680px;--d:150px"></div>
{img("rep/port_modes_port.png", "left:316px;top:650px;width:71px", "ab")}
<div class="pm-lb" style="left:300px;top:727px;width:100px;font-size:19px">VLAN 10</div>
<div class="pm-ft" style="left:22px;top:816px;width:394px">ОДНО УСТРОЙСТВО &nbsp;•&nbsp; ОДНА VLAN</div>
</div>

<div class="step">
{head(433, T, "02", "TRUNK", "МАГИСТРАЛЬНЫЙ ИНТЕРФЕЙС", 0)}
<div class="pm-tx" style="left:458px;top:534px;width:360px">Принимает тегированный трафик<br>нескольких VLAN<br>Native VLAN передаётся без тега</div>
{img("rep/port_modes_swl.png", "left:448px;top:658px;width:94px", "ab")}
{img("rep/port_modes_swr.png", "left:720px;top:658px;width:94px", "ab")}
<div class="pm-lb" style="left:446px;top:710px;width:96px;font-family:Golos Text,sans-serif;font-size:15px">Коммутатор</div>
<div class="pm-lb" style="left:720px;top:710px;width:96px;font-family:Golos Text,sans-serif;font-size:15px">Коммутатор</div>
<div class="pm-lb" style="left:548px;top:630px;width:166px;font-size:14px;color:#2ad4ff">VLAN 10 TAGGED</div>
<div class="pm-arr b" style="--c:#2ad4ff;left:552px;top:654px;width:158px"></div>
<div class="pm-lb" style="left:548px;top:663px;width:166px;font-size:14px;color:#e05cff">VLAN 20 TAGGED</div>
<div class="pm-arr b" style="--c:#e05cff;left:552px;top:686px;width:158px"></div>
<div class="pm-lb" style="left:540px;top:697px;width:182px;font-size:12px;color:#ffc53d">NATIVE VLAN UNTAGGED</div>
<div class="pm-arr b" style="--c:#ffc53d;left:552px;top:718px;width:158px"></div>
<div class="ab" style="left:453px;top:753px;width:356px;height:40px;border:2px solid #9fb8e8;border-radius:6px;background:rgba(4,10,30,.8);
  font-family:'JetBrains Mono',monospace;font-size:17px;line-height:38px;color:#e6f1ff;padding-left:14px;box-sizing:border-box">switchport <span style="color:#2ad4ff">trunk native vlan</span></div>
<div class="pm-ft" style="left:433px;top:816px;width:394px">НЕСКОЛЬКО VLAN ПО ОДНОМУ ЛИНКУ</div>
</div>

<div class="step">
{head(845, G, "03", "GENERAL", "ПОЛНАЯ ПОДДЕРЖКА 802.1Q", 30)}
<div class="pm-tx" style="left:869px;top:534px;width:350px">Принимает тегированный<br>и нетегированный трафик</div>
{img("rep/port_modes_srv.png", "left:880px;top:603px;width:52px", "ab")}
<div class="pm-lb" style="left:850px;top:660px;width:112px;font-family:Golos Text,sans-serif;font-size:15px">СЕРВЕР<br>(Тегированный)</div>
{img("rep/port_modes_pc2.png", "left:866px;top:703px;width:80px", "ab")}
<div class="pm-lb" style="left:852px;top:768px;width:136px;font-family:Golos Text,sans-serif;font-size:15px">ПК<br>(Нетегированный)</div>
<div class="pm-tag" style="--c:#2ad4ff;--g:rgba(42,212,255,.5);left:984px;top:604px;width:86px">TAGGED</div>
<div class="pm-arr" style="--c:#2ad4ff;left:956px;top:639px;width:130px"></div>
<div class="pm-tag" style="--c:#2ad4ff;--g:rgba(42,212,255,.5);left:982px;top:697px;width:90px">UNTAGGED</div>
<div class="pm-arr" style="--c:#2ad4ff;left:956px;top:735px;width:130px"></div>
<div class="ab" style="left:1092px;top:639px;width:12px;height:98px;border:3px solid #2ad4ff;border-left:0;border-radius:0 4px 4px 0"></div>
<div class="pm-arr" style="--c:#2ad4ff;left:1106px;top:686px;width:30px"></div>
<div class="pm-pkt" style="--c:#2ad4ff;left:960px;top:634px;--d:120px"></div>
<div class="pm-pkt" style="--c:#2ad4ff;left:960px;top:730px;--d:120px;animation-delay:1.2s"></div>
{img("rep/port_modes_port2.png", "left:1143px;top:653px;width:71px", "ab")}
<div class="pm-lb" style="left:1118px;top:728px;width:120px;font-size:17px">TAGGED +<br>UNTAGGED</div>
<div class="pm-ft" style="left:845px;top:816px;width:394px">ОДИН ПОРТ — ЛЮБОЙ ТРАФИК</div>
</div>

<div class="step">
{head(1256, C, "04", "CUSTOMER", "Q-IN-Q ИНТЕРФЕЙС", 30)}
<div class="pm-tx" style="left:1280px;top:534px;width:372px;font-size:18.5px">Добавляет внешний тег к уже<br>тегированному клиентскому трафику</div>
{img("rep/port_modes_bld.png", "left:1268px;top:633px;width:79px", "ab")}
<div class="pm-lb" style="left:1260px;top:730px;width:110px;font-size:15px">КЛИЕНТСКАЯ<br>СЕТЬ</div>
<div class="pm-tag" style="--c:#e05cff;--g:rgba(224,92,255,.5);left:1346px;top:660px;width:56px;font-size:15px">C-TAG</div>
<div class="pm-arr" style="--c:#e05cff;left:1354px;top:692px;width:62px"></div>
<div class="ab" style="left:1428px;top:640px;width:80px;height:80px;border:2px solid #e05cff;border-radius:6px;background:rgba(40,10,70,.8);box-shadow:0 0 12px rgba(224,92,255,.6)"></div>
<div class="pm-tag" style="--c:#ffb43d;--g:rgba(255,180,61,.5);left:1436px;top:652px;width:60px;font-size:14px;background:#c87a10;line-height:22px">S-TAG</div>
<div class="pm-tag" style="--c:#e05cff;--g:rgba(224,92,255,.5);left:1436px;top:681px;width:60px;font-size:14px;background:#a02cc8;line-height:22px">C-TAG</div>
<div class="pm-arr" style="--c:#2ad4ff;left:1516px;top:692px;width:44px"></div>
{img("rep/port_modes_bld2.png", "left:1563px;top:633px;width:79px", "ab")}
<div class="pm-lb" style="left:1404px;top:732px;width:126px;font-size:18px">S-TAG + C-TAG</div>
<div class="pm-lb" style="left:1550px;top:730px;width:106px;font-size:15px">СЕТЬ<br>ПРОВАЙДЕРА</div>
<div class="pm-ft" style="left:1256px;top:816px;width:394px">Q-IN-Q ДЛЯ ПОДКЛЮЧЕНИЯ КЛИЕНТОВ</div>
</div>

<div class="step">
<div class="ab" style="left:40px;top:866px;width:1576px;height:58px;border:2px solid rgba(42,212,255,.6);border-radius:6px;background:rgba(6,20,56,.85);
  box-shadow:0 0 14px rgba(42,212,255,.35);clip-path:polygon(2% 0,100% 0,98% 100%,0 100%)"></div>
<div class="ab" style="font-family:Oswald,sans-serif;left:40px;top:880px;width:1576px;text-align:center;font-size:23px;color:#e6f1ff;font-weight:400">
<b style="color:#2ad4ff;font-weight:500">ACCESS</b> — ОДНА VLAN &nbsp;•&nbsp; <b style="color:#e05cff;font-weight:500">TRUNK</b> — НЕСКОЛЬКО VLAN &nbsp;•&nbsp;
<b style="color:#4fa8ff;font-weight:500">GENERAL</b> — TAGGED И UNTAGGED &nbsp;•&nbsp; <b style="color:#ffc53d;font-weight:500">CUSTOMER</b> — ДВОЙНОЕ ТЕГИРОВАНИЕ</div>
</div>
"""
