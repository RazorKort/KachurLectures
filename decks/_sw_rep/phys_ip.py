# -*- coding: utf-8 -*-
"""Физические интерфейсы с IP-адресами (L3-порт) — вёрстка 1:1."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 228

CSS = """<style>
.pip-pan{position:absolute;border:2px solid #2ad4ff;border-radius:12px;background:rgba(6,22,60,.72);box-shadow:0 0 16px rgba(42,212,255,.5),inset 0 0 24px rgba(42,212,255,.1)}
.pip-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:26px;color:#2ad4ff;letter-spacing:.4px}
.pip-c{position:absolute;font-family:Oswald,sans-serif;font-size:15px;color:#cfe0ff}
.pip-f{position:absolute;border:1.5px solid #2ad4ff;border-radius:5px;background:rgba(8,40,80,.85);display:flex;flex-direction:column;align-items:center;justify-content:center;
  font-family:Oswald,sans-serif;font-size:15px;line-height:1.2;color:#fff;text-align:center}
.pip-f.t{background:linear-gradient(180deg,#1a8fb0,#0d5a80);color:#fff}
.pip-f.t b{font-weight:500;font-size:17px;color:#bff6ff}
.pip-f.p{border-color:#9b6bff;background:linear-gradient(180deg,#3a1a9a,#22106a);box-shadow:0 0 12px rgba(155,107,255,.7)}
.pip-ip{position:absolute;border:2px solid #9b6bff;border-radius:6px;background:linear-gradient(180deg,#3a1a9a,#22106a);box-shadow:0 0 14px rgba(155,107,255,.8);
  display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-size:16px;line-height:1.2;color:#fff}
.pip-lb{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:15px;line-height:1.25;color:#fff;text-align:center}
.pip-ar{position:absolute;height:14px;background:linear-gradient(90deg,rgba(42,212,255,0),#2ad4ff);clip-path:polygon(0 30%,70% 30%,70% 0,100% 50%,70% 100%,70% 70%,0 70%)}
.pip-ar.v{background:linear-gradient(90deg,rgba(155,107,255,0),#b07bff)}
.pip-ar.big{height:34px}
.pip-li{position:absolute;left:56px;display:flex;align-items:center;gap:30px;font-family:'Golos Text',sans-serif;font-size:19px;line-height:1.25;color:#fff}
.pip-bt{position:absolute;top:816px;font-family:Oswald,sans-serif;font-weight:700;font-size:25px;line-height:1.1;text-align:center}
.pip-tag{position:absolute;border:2px solid #2ad4ff;border-radius:6px;background:rgba(6,20,56,.92);box-shadow:0 0 12px rgba(42,212,255,.7);font-family:Oswald,sans-serif;color:#fff}
.pip-pk{position:absolute;width:14px;height:14px;border-radius:3px;background:#e0d0ff;box-shadow:0 0 12px #9b6bff;animation:pipgo 4s linear infinite}
@keyframes pipgo{0%{transform:translate(0,0);opacity:0}5%{opacity:1}45%{transform:translate(500px,0)}55%{transform:translate(500px,0)}95%{transform:translate(1000px,40px);opacity:1}100%{transform:translate(1000px,40px);opacity:0}}
.pip-port{position:absolute;border:2px solid #2ad4ff;box-shadow:0 0 14px #2ad4ff;animation:pipbl 1.2s ease-in-out infinite}
@keyframes pipbl{50%{opacity:.35}}
</style>"""


def _frame(x, y, cells):
    out = []
    for cls, w, html in cells:
        out.append('<div class="pip-f %s" style="left:%dpx;top:%dpx;width:%dpx;height:56px">%s</div>' % (cls, x, y, w, html))
        x += w + 4
    return "".join(out)


HTML = CSS + f"""
<div class="step">
  {img("rep/phys_ip_sw.png", "left:680px;top:240px;width:970px", "ab")}
  <div class="pip-port" style="left:968px;top:342px;width:56px;height:52px"></div>
  <div class="pip-tag" style="left:920px;top:234px;width:254px;height:62px;padding:4px 18px;font-size:19px;line-height:1.3;font-weight:500">IP: <span style="font-family:'JetBrains Mono',monospace;font-size:18px">192.168.1.1/24</span><br>MAC: <span style="font-family:'JetBrains Mono',monospace;font-size:16px;font-weight:400">00:1A:2B:3C:4D:5E</span></div>
  <div class="pip-tag" style="left:892px;top:438px;width:248px;height:36px;display:flex;align-items:center;justify-content:center;font-size:19px;font-weight:500">ФИЗИЧЕСКИЙ L3-ПОРТ</div>
</div>

<div class="step">
  <div class="pip-pan" style="left:18px;top:426px;width:446px;height:194px"></div>
  <div class="pip-h" style="left:58px;top:440px">ВХОДЯЩИЙ КАДР L2</div>
  <div class="pip-pan" style="left:40px;top:488px;width:410px;height:104px;border-radius:8px"></div>
  <div class="pip-c" style="left:66px;top:496px">КАДР ETHERNET (L2)</div>
  {_frame(54, 522, [("t", 110, "<b>Dst MAC</b><span style='font-size:14px'>= MAC ПОРТА</span>"), ("", 70, "Src MAC<br>…"), ("", 70, "Type<br>0x0800"), ("p", 120, "IP-ПАКЕТ (L3)<br>…")])}
</div>

<div class="step">
  <div class="pip-ar big" style="left:462px;top:524px;width:76px"></div>
  {img("rep/phys_ip_gl1.png", "left:542px;top:466px;width:150px", "ab")}
  <div class="pip-lb" style="left:530px;top:600px;width:160px">ДЕКАПСУЛЯЦИЯ<br>ДО L3</div>
  <div class="pip-ar v" style="left:690px;top:536px;width:44px"></div>
  <div class="pip-ip" style="left:736px;top:514px;width:150px;height:56px">IP-ПАКЕТ (L3)<br>…</div>
  <div class="ab" style="left:810px;top:572px;width:2px;height:24px;background:#9b6bff"></div>
  <div class="pip-lb" style="left:726px;top:600px;width:176px">РЕШЕНИЕ ПО<br>МАРШРУТИЗАЦИИ</div>
  <div class="pip-ar v" style="left:890px;top:536px;width:56px"></div>
</div>

<div class="step">
  <div class="ab" style="left:983px;top:474px;width:4px;height:60px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff"></div>
  <div class="ab" style="left:970px;top:524px;width:0;height:0;border-left:15px solid transparent;border-right:15px solid transparent;border-top:20px solid #2ad4ff"></div>
  <div class="pip-ip" style="left:986px;top:558px;width:124px;height:50px;font-size:14px">IP-ПАКЕТ (L3)<br>…</div>
  <div class="pip-ar" style="left:1112px;top:578px;width:42px"></div>
  {img("rep/phys_ip_gl2.png", "left:1156px;top:532px;width:118px", "ab")}
  <div class="pip-lb" style="left:1160px;top:646px;width:160px;font-size:16px">ИНКАПСУЛЯЦИЯ<br>В КАДР L2</div>
  <div class="pip-ar" style="left:1270px;top:584px;width:40px"></div>
</div>

<div class="step">
  <div class="pip-h" style="left:1172px;top:494px;font-size:23px">ИСХОДЯЩИЙ ПАКЕТ L3</div>
  <div class="pip-pan" style="left:1312px;top:532px;width:330px;height:104px;border-radius:8px"></div>
  <div class="pip-c" style="left:1330px;top:540px">КАДР ETHERNET (L2)</div>
  {_frame(1324, 566, [("t", 94, "<b>Src MAC</b><span style='font-size:13px'>= MAC ПОРТА</span>"), ("", 60, "Dst MAC<br>…"), ("", 52, "Type<br>0x0800"), ("p", 86, "<span style='font-size:13px'>IP-ПАКЕТ (L3)</span>…")])}
  <div class="pip-pk" style="left:470px;top:536px"></div>
</div>

<div class="step">
  <div class="pip-pan" style="left:24px;top:640px;width:490px;height:270px"></div>
  <div class="pip-li" style="top:656px">{img("rep/phys_ip_l1.png", "width:72px")}<div>Порт имеет собственные<br>IP- и MAC-адреса</div></div>
  <div class="ab" style="left:46px;top:727px;width:446px;height:1px;background:rgba(160,190,240,.35)"></div>
  <div class="pip-li" style="top:742px">{img("rep/phys_ip_l2.png", "width:74px")}<div>Принимает кадры,<br>адресованные его MAC-адресу</div></div>
  <div class="ab" style="left:46px;top:812px;width:446px;height:1px;background:rgba(160,190,240,.35)"></div>
  <div class="pip-li" style="top:824px">{img("rep/phys_ip_l3.png", "width:70px")}<div>Маршрутизирует пакеты<br>на уровне L3</div></div>
</div>

<div class="step">
  <div class="pip-pan" style="left:552px;top:708px;width:1094px;height:194px"></div>
  {img("rep/phys_ip_b1.png", "left:604px;top:738px;width:132px", "ab")}
  <div class="pip-ar big" style="left:756px;top:762px;width:80px"></div>
  {img("rep/phys_ip_b2.png", "left:864px;top:738px;width:96px", "ab")}
  <div class="pip-ar big v" style="left:980px;top:762px;width:80px"></div>
  {img("rep/phys_ip_b3.png", "left:1154px;top:728px;width:98px", "ab")}
  <div class="pip-ar big" style="left:1300px;top:762px;width:84px"></div>
  {img("rep/phys_ip_b4.png", "left:1434px;top:738px;width:156px", "ab")}
  <div class="pip-bt" style="left:590px;width:170px;color:#2ad4ff">ВХОД:<br><span style="color:#fff">КАДР L2</span></div>
  <div class="pip-bt" style="left:830px;width:170px;top:826px;color:#fff">ПАКЕТ L3</div>
  <div class="pip-bt" style="left:1086px;width:240px;top:826px;color:#fff">МАРШРУТИЗАЦИЯ</div>
  <div class="pip-bt" style="left:1430px;width:170px;color:#2ad4ff">КАДР L2:<br>ВЫХОД</div>
</div>
"""
