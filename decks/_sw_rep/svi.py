# -*- coding: utf-8 -*-
"""Интерфейсы SVI — вёрстка 1:1."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 278

CSS = """<style>
.svi-pan{position:absolute;border:2px solid #2ad4ff;border-radius:12px;background:rgba(6,22,60,.75);box-shadow:0 0 14px rgba(42,212,255,.45),inset 0 0 22px rgba(42,212,255,.1)}
.svi-in{position:absolute;border:1.5px solid rgba(42,212,255,.45);border-radius:8px;background:rgba(8,28,72,.55)}
.svi-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:25px;color:#fff;letter-spacing:.3px}
.svi-h i{font-style:normal;color:#2ad4ff}
.svi-ul{position:absolute;width:30px;height:3px;background:#2ad4ff;box-shadow:0 0 6px #2ad4ff}
.svi-tx{position:absolute;font-family:'Golos Text',sans-serif;font-size:18px;line-height:1.38;color:#fff}
.svi-box{position:absolute;top:283px;width:290px;height:128px;border:3px solid #2ad4ff;border-radius:10px;background:rgba(6,30,80,.9);box-shadow:0 0 22px rgba(42,212,255,.8)}
.svi-box.v{border-color:#b07bff;background:rgba(40,15,100,.9);box-shadow:0 0 22px rgba(176,123,255,.85)}
.svi-box b{position:absolute;left:108px;top:16px;font-family:Oswald,sans-serif;font-weight:500;font-size:25px;line-height:1.2;color:#fff}
.svi-box b i{font-style:normal;color:#9ff0ff}.svi-box.v b i{color:#fff}
.svi-pill{position:absolute;top:84px;height:32px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:500;font-size:22px;color:#fff}
.svi-wire path{fill:none;stroke-width:3}
.svi-flow{stroke-dasharray:8 12;animation:sviflow 1.2s linear infinite}
@keyframes sviflow{to{stroke-dashoffset:-40}}
.svi-br{position:absolute;top:580px;height:34px;border:3px solid #2ad4ff;border-top:none;border-radius:0 0 10px 10px;text-align:center;font-family:Oswald,sans-serif;font-weight:500;font-size:22px;line-height:52px;color:#2ad4ff}
.svi-st{position:absolute;font-family:Oswald,sans-serif;font-size:20px;line-height:1.25;color:#fff}
.svi-st b{font-weight:700;font-size:30px}
.svi-pk{position:absolute;top:842px;width:14px;height:14px;border-radius:50%;background:#bff6ff;box-shadow:0 0 12px #2ad4ff;animation:svigo 3.2s linear infinite}
@keyframes svigo{0%{transform:translateX(0);opacity:0}8%{opacity:1}92%{opacity:1}100%{transform:translateX(560px);opacity:0}}
.svi-red{animation:svired 1.4s ease-in-out infinite}@keyframes svired{50%{opacity:.4}}
</style>"""


def _card(x, y, w, h, title, ic, icst, text, tx, d=0):
    return ('<div class="step" style="transition-delay:%dms"><div class="svi-pan" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"></div>'
            '<div class="svi-h" style="left:%dpx;top:%dpx">%s</div><div class="svi-ul" style="left:%dpx;top:%dpx"></div>'
            '<div class="svi-in" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"></div>%s<div class="svi-tx" style="left:%dpx;top:%dpx">%s</div></div>') % (
        d, x, y, w, h, x + 24, y + 10, title, x + 24, y + 50, x + 18, y + 56, w - 36, h - 66, img("rep/" + ic, icst, "ab"), tx, y + 82 if h > 150 else y + 80, text)


HTML = CSS + f"""
{_card(28, 310, 412, 162, "ВИРТУАЛЬНЫЙ <i>ИНТЕРФЕЙС</i>", "svi_l1.png", "left:56px;top:378px;width:84px", "SVI привязан<br>к определённой VLAN", 162)}
{_card(28, 488, 392, 156, "ОДИН <i>SVI</i> — <i>ОДНА VLAN</i>", "svi_l2.png", "left:60px;top:552px;width:74px", "Имя интерфейса<br>совпадает с номером VLAN", 158)}
{_card(28, 664, 392, 168, "УСЛОВИЕ СОСТОЯНИЯ <i>UP</i>", "svi_l3.png", "left:56px;top:738px;width:82px", "В VLAN есть хотя бы один<br>активный access- или<br>trunk-порт", 162)}

<div class="step">
  {img("rep/svi_sw.png", "left:440px;top:470px;width:796px", "ab")}
</div>

<div class="step">
  <div class="svi-box" style="left:510px"><b>SVI VLAN 10<br><i>192.168.10.1/24</i></b>
    <div class="svi-pill" style="left:86px;width:120px;border:2px solid #9dfc5a;background:rgba(20,90,70,.9);box-shadow:0 0 10px rgba(157,252,90,.6);color:#9dfc5a">SVI UP</div></div>
  {img("rep/svi_r1.png", "left:526px;top:296px;width:80px", "ab")}
  <svg class="ab svi-wire" style="left:0;top:0;width:1672px;height:941px" viewBox="0 0 1672 941">
    <path d="M630 414L580 496M650 414L645 496M670 414L710 496M690 414L776 496" stroke="#2ad4ff" style="filter:drop-shadow(0 0 4px #2ad4ff)"/>
    <path class="svi-flow" d="M630 414L580 496M650 414L645 496M670 414L710 496M690 414L776 496" stroke="#e0fbff"/>
  </svg>
  <div class="svi-br" style="left:548px;width:256px">VLAN 10</div>
</div>

<div class="step">
  <div class="svi-box v" style="left:876px"><b>SVI VLAN 20<br><i>192.168.20.1/24</i></b>
    <div class="svi-pill" style="left:84px;width:136px;border:2px solid #e05cff;background:rgba(90,20,90,.9);color:#ffd6f0">SVI DOWN</div></div>
  {img("rep/svi_r2.png", "left:894px;top:296px;width:80px", "ab")}
  <svg class="ab svi-wire" style="left:0;top:0;width:1672px;height:941px" viewBox="0 0 1672 941">
    <path d="M1005 414L898 496M1012 414L964 496M1028 414L1028 496M1046 414L1092 496" stroke="#b07bff" style="filter:drop-shadow(0 0 4px #b07bff)"/>
  </svg>
  <div class="svi-br" style="left:866px;width:256px;border-color:#b07bff;color:#b07bff">VLAN 20</div>
</div>

<div class="step">
  <div class="svi-pan" style="left:440px;top:646px;width:826px;height:90px"></div>
  {img("rep/svi_ok.png", "left:468px;top:658px;width:76px", "ab")}
  <div class="svi-st" style="left:560px;top:664px">ЕСТЬ АКТИВНЫЙ ПОРТ В VLAN<br><b style="color:#9dfc5a">→ SVI UP</b></div>
  <div class="ab" style="left:880px;top:664px;width:2px;height:56px;background:#cfe0ff"></div>
  {img("rep/svi_x.png", "left:914px;top:658px;width:76px", "ab")}
  <div class="svi-st" style="left:1006px;top:664px">НЕТ АКТИВНЫХ ПОРТОВ<br><b style="color:#ff4d5e">→ SVI DOWN</b></div>
</div>

{_card(1250, 310, 394, 160, "ШЛЮЗ ПО УМОЛЧАНИЮ", "svi_g1.png", "left:1270px;top:380px;width:88px", "IP-адрес SVI используется<br>узлами своей VLAN", 1380)}
{_card(1264, 488, 380, 156, "СЕТЕВЫЕ <i>СЕРВИСЫ</i>", "svi_g2.png", "left:1292px;top:558px;width:72px", "DHCP • VRRP •<br>МАРШРУТИЗАЦИЯ", 1396)}

<div class="step">
  <div class="svi-pan" style="left:434px;top:752px;width:1032px;height:156px"></div>
  <div class="svi-h" style="left:454px;top:762px">ПРИМЕР <i>ТРАФИКА</i></div>
  <div class="svi-ul" style="left:454px;top:800px"></div>
  {img("rep/svi_pc.png", "left:474px;top:820px;width:88px", "ab")}
  <div class="ab" style="left:584px;top:826px;font-family:Oswald,sans-serif;font-size:21px;line-height:1.25;color:#fff">ПК VLAN 10<br><span style="font-family:'Golos Text';font-size:18px">192.168.10.100/24</span></div>
  <div class="ab" style="left:740px;top:828px;color:#2ad4ff;font-size:40px;line-height:40px;text-shadow:0 0 8px #2ad4ff">⟶</div>
  <div class="svi-in" style="left:814px;top:798px;width:632px;height:96px"></div>
  {img("rep/svi_gw.png", "left:820px;top:806px;width:86px", "ab")}
  <div class="ab" style="left:916px;top:810px;font-family:Oswald,sans-serif;font-size:20px;line-height:1.2;color:#fff">ШЛЮЗ<br><b style="font-weight:500;font-size:21px">192.168.10.1</b><br><span style="color:#2ad4ff">SVI VLAN 10</span></div>
  <div class="ab" style="left:1040px;top:828px;color:#2ad4ff;font-size:40px;line-height:40px;text-shadow:0 0 8px #2ad4ff">⟶</div>
  {img("rep/svi_cl.png", "left:1134px;top:810px;width:106px", "ab")}
  <div class="ab" style="left:1256px;top:824px;font-family:Oswald,sans-serif;font-size:20px;line-height:1.2;color:#fff">ДРУГАЯ СЕТЬ<br><span style="font-family:'Golos Text';font-size:17px">например, 8.8.8.8</span></div>
  <div class="svi-pk" style="left:600px"></div>
  <div class="ab" style="left:1540px;top:720px;font-family:Oswald,sans-serif;font-size:16px;line-height:1.38;color:#2ad4ff">ОДНА VLAN<br>МНОГО<br>УСТРОЙСТВ<br>ОДИН SVI</div>
</div>
"""
