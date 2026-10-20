# -*- coding: utf-8 -*-
"""Тег 802.1Q — нетегированный/тегированный кадр Ethernet и структура тега 32 бита."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 180

CSS = """<style>
.vq-h{position:absolute;font-family:Oswald,sans-serif;font-weight:600;font-size:30px;color:#2ad4ff;letter-spacing:.5px;text-shadow:0 0 10px rgba(42,212,255,.6)}
.vq-f{position:absolute;border-radius:6px;border:2px solid #2ad4ff;background:linear-gradient(180deg,rgba(26,90,200,.9),rgba(10,40,120,.9));
  box-shadow:0 0 12px rgba(42,212,255,.6),inset 0 0 14px rgba(42,212,255,.2);color:#fff;text-align:center;display:flex;flex-direction:column;justify-content:center;
  font-family:'Golos Text',sans-serif;font-weight:600;font-size:21px;line-height:1.08}
.vq-f i{font-style:normal;font-weight:400;font-size:18px;color:#d8e8ff;margin-top:4px}
.vq-f.big{font-size:24px}.vq-f.t{background:linear-gradient(180deg,rgba(14,130,150,.85),rgba(6,70,100,.9))}
.vq-f.tag{border-color:#e05cff;background:linear-gradient(180deg,#a02ad8,#5a1290);box-shadow:0 0 20px rgba(224,92,255,.9);font-family:Oswald,sans-serif;font-size:25px;font-weight:500}
.vq-dim{position:absolute;height:2px;background:#9fd6ff}
.vq-dim:before,.vq-dim:after{content:'';position:absolute;top:-9px;width:2px;height:20px;background:#9fd6ff}
.vq-dim:before{left:0}.vq-dim:after{right:0}
.vq-dl{position:absolute;font-size:18px;color:#e6f1ff;background:#06183f;padding:0 12px;transform:translateX(-50%);white-space:nowrap}
.vq-b{position:absolute;border-radius:5px;border:2px solid #9b6bff;color:#fff;text-align:center;font-family:Oswald,sans-serif;font-weight:500;font-size:22px;line-height:1.15;
  display:flex;flex-direction:column;justify-content:center}
.vq-note{position:absolute;border-radius:8px;border:2px solid #e05cff;background:rgba(60,10,90,.85);box-shadow:0 0 12px rgba(224,92,255,.6);color:#fff;
  text-align:center;font-size:17px;line-height:1.25;display:flex;align-items:center;justify-content:center}
@keyframes vq-up{0%,100%{transform:translateY(0)}50%{transform:translateY(-8px)}}
.vq-arr{position:absolute;animation:vq-up 1.4s ease-in-out infinite}
</style>"""

R1 = [("MAC<br>назначения", "6 байт", 74, 260, ""), ("MAC<br>источника", "6 байт", 340, 274, "t"), ("EtherType", "2 байта", 621, 194, "big"),
      ("Payload", "46–1500 байт", 821, 600, "big t"), ("FCS", "4 байта", 1427, 168, "big")]
R2 = [("MAC<br>назначения", "6 байт", 74, 216, ""), ("MAC<br>источника", "6 байт", 296, 210, "t"), ("EtherType", "2 байта", 808, 192, "big"),
      ("Payload", "42–1500 байт", 1007, 414, "big t"), ("FCS", "4 байта", 1427, 168, "big")]


def _row(row, top, h):
    return "".join('<div class="vq-f %s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx">%s<i>%s</i></div>'
                   % (c, x, top, w, h, t, b) for t, b, x, w, c in row)


def _dim(x0, x1, y, label):
    return ('<div class="vq-dim" style="left:%dpx;top:%dpx;width:%dpx"></div><div class="vq-dl" style="left:%dpx;top:%dpx">%s</div>'
            % (x0, y, x1 - x0, (x0 + x1) // 2, y - 13, label))


HTML = CSS + f"""
<div class="step">
  <div class="vq-h" style="left:72px;top:190px">НЕТЕГИРОВАННЫЙ КАДР ETHERNET</div>
  {_row(R1, 226, 80)}
  {_dim(76, 1596, 331, "<b>64–1518 байт</b> (без учета преамбулы и SFD)")}
</div>
<div class="step">
  <div class="vq-h" style="left:72px;top:358px">ТЕГИРОВАННЫЙ КАДР ETHERNET 802.1Q</div>
  {_row(R2, 397, 78)}
  <div class="vq-f tag" style="left:512px;top:397px;width:290px;height:78px">ТЕГ 802.1Q — 4 БАЙТА</div>
  {_dim(76, 1596, 503, "<b>68–1522 байт</b> (без учета преамбулы и SFD)").replace("left:836px", "left:1085px")}
</div>
<div class="step">
  <svg class="vq-arr" style="left:640px;top:460px" width="36" height="42" viewBox="0 0 36 42"><path d="M18 0 L36 18 H26 V42 H10 V18 H0 Z" fill="#e05cff" style="filter:drop-shadow(0 0 6px #e05cff)"/></svg>
  <div class="vq-note" style="left:481px;top:501px;width:358px;height:54px">Тег 802.1Q вставляется<br>между MAC источника и EtherType</div>
</div>

<div class="step">
  <div class="ab" style="left:40px;top:562px;width:1218px;height:284px;border-radius:12px;border:2px solid rgba(42,212,255,.6);background:rgba(6,24,64,.5);box-shadow:0 0 14px rgba(42,212,255,.35)"></div>
  <div class="vq-h" style="left:74px;top:566px">СТРУКТУРА ТЕГА 802.1Q — 32 БИТА</div>
  <div class="ab" style="left:74px;top:612px;width:1144px;height:146px;border-radius:8px;border:2px solid rgba(42,212,255,.5)"></div>
  {_dim(87, 551, 636, "16 бит")}
  {_dim(560, 1206, 636, "16 бит")}
  <div class="vq-b" style="left:86px;top:648px;width:464px;height:102px;background:linear-gradient(180deg,#8a2ad8 0,#8a2ad8 37%,#4d1290 37%);justify-content:flex-start">
    <div style="height:38px;line-height:38px">TPID — 16 БИТ</div><div style="color:#ffc53d;font-size:26px;line-height:1.1;margin-top:4px">0x8100</div>
    <div style="font-family:'Golos Text',sans-serif;font-weight:400;font-size:19px">1000 0001 0000 0000</div></div>
</div>
<div class="step">
  <div class="vq-b" style="left:560px;top:648px;width:646px;height:36px;background:#8a2ad8">TCI — 16 БИТ</div>
  <div class="vq-b" style="left:560px;top:686px;width:174px;height:64px;border-color:#2ad4ff;background:linear-gradient(180deg,#1a6fe0,#0d3c9a)">PCP<br>3 БИТА</div>
  <div class="vq-b" style="left:740px;top:686px;width:110px;height:64px;border-color:#2ad4ff;background:linear-gradient(180deg,#1a6fe0,#0d3c9a)">DEI<br>1 БИТ</div>
  <div class="vq-b" style="left:857px;top:686px;width:349px;height:64px;border-color:#2ad4ff;background:linear-gradient(180deg,#1a6fe0,#0d3c9a)">VLAN ID<br>12 БИТ</div>
</div>
<div class="step">
  <svg class="ab" style="left:0;top:0" width="1672" height="941"><g stroke="#9fd6ff" stroke-width="2" fill="#9fd6ff">
    <line x1="648" y1="750" x2="648" y2="784"/><circle cx="648" cy="753" r="5"/>
    <line x1="793" y1="750" x2="793" y2="784"/><circle cx="793" cy="753" r="5"/>
    <line x1="1078" y1="750" x2="1078" y2="784"/><circle cx="1078" cy="753" r="5"/></g></svg>
  <div class="vq-note" style="left:482px;top:784px;width:198px;height:52px">PCP — приоритет<br>трафика, 0–7</div>
  <div class="vq-note" style="left:697px;top:784px;width:230px;height:52px">DEI — возможность<br>отбрасывания кадра</div>
  <div class="vq-note" style="left:948px;top:784px;width:276px;height:52px">VLAN ID — идентификатор<br>VLAN, 1–4094</div>
</div>

<div class="step">
  <div class="ab" style="left:1288px;top:600px;width:332px;height:186px;border-radius:12px;border:2px solid #2ad4ff;background:rgba(8,30,80,.7);box-shadow:0 0 16px rgba(42,212,255,.5)"></div>
  {img("rep/vlan_tag8021q_fcs.png", "left:1315px;top:618px;width:87px", "ab")}
  <div class="ab" style="left:1417px;top:630px;font-family:Oswald,sans-serif;font-weight:500;font-size:21px;line-height:1.35;color:#fff">ПОСЛЕ<br>ДОБАВЛЕНИЯ ТЕГА<br>
    <span style="font-size:30px;line-height:1">FCS</span><br>ПЕРЕСЧИТЫВАЕТСЯ</div>
</div>

<div class="step">
  <div class="ab" style="left:180px;top:866px;width:1310px;height:60px;border-radius:10px;border:2px solid rgba(42,212,255,.6);background:rgba(6,24,64,.6);box-shadow:0 0 14px rgba(42,212,255,.4)"></div>
  <div class="ab" style="left:180px;top:868px;width:1310px;text-align:center;font-family:Oswald,sans-serif;font-weight:600;font-size:28px;line-height:56px;color:#fff">
    <span style="color:#2ad4ff;font-size:40px;vertical-align:-3px">VLAN</span> — ШИРОКОВЕЩАТЕЛЬНЫЙ ДОМЕН, ОГРАНИЧЕННЫЙ НА УРОВНЕ L2</div>
</div>
"""
