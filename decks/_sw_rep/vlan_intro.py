# -*- coding: utf-8 -*-
"""VLAN intro — принципы работы VLAN: нетегированный/тегированный кадр, метка 802.1Q."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 145

CSS = """<style>
.vi-pan{position:absolute;border-radius:10px;border:2px solid rgba(42,212,255,.55);background:rgba(6,24,64,.55);box-shadow:0 0 12px rgba(42,212,255,.3)}
.vi-h{position:absolute;font-family:Oswald,sans-serif;font-weight:600;font-size:31px;color:#fff;letter-spacing:.5px}
.vi-f{position:absolute;top:0;height:64px;border-radius:6px;border:2px solid #2ad4ff;background:linear-gradient(180deg,rgba(26,90,190,.85),rgba(8,30,90,.9));
  box-shadow:0 0 10px rgba(42,212,255,.5),inset 0 0 14px rgba(42,212,255,.2);color:#fff;text-align:center;font-family:'Golos Text',sans-serif}
.vi-f b{display:block;font-weight:500;font-size:21px;margin-top:7px;line-height:1.1}.vi-f i{display:block;font-style:normal;font-size:15px;color:#cfe0ff;margin-top:6px}
.vi-f.tag{border:3px solid #ffc53d;background:linear-gradient(180deg,#7a1fd0,#3d0f80);box-shadow:0 0 18px rgba(224,92,255,.9),0 0 6px #ffc53d}
.vi-card{position:absolute;border-radius:12px;border:2px solid #2ad4ff;background:rgba(8,30,80,.8);box-shadow:0 0 16px rgba(42,212,255,.5),inset 0 0 20px rgba(42,212,255,.15)}
.vi-card.m{border-color:#9b6bff;box-shadow:0 0 16px rgba(155,107,255,.55),inset 0 0 20px rgba(155,107,255,.18)}
.vi-ct{position:absolute;font-family:Oswald,sans-serif;font-weight:600;font-size:29px;line-height:1}
.vi-tx{position:absolute;font-size:21px;line-height:1.24;color:#e6f1ff}
.vi-c{position:absolute;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:500;color:#fff;border-radius:6px;text-align:center}
@keyframes vi-glow{0%,100%{box-shadow:0 0 18px rgba(224,92,255,.9),0 0 6px #ffc53d}50%{box-shadow:0 0 34px rgba(224,92,255,1),0 0 16px #ffc53d}}
.vi-f.tag{animation:vi-glow 2s ease-in-out infinite}
</style>"""

ROW1 = [("Preamble", "7 байт", 52, 176), ("SFD", "1 байт", 232, 106), ("Destination MAC", "6 байт", 342, 250),
        ("Source MAC", "6 байт", 596, 240), ("EtherType", "2 байта", 840, 172), ("Data", "46–1500 байт", 1017, 456),
        ("FCS", "4 байта", 1477, 145)]
ROW2 = [("Preamble", "7 байт", 52, 176, ""), ("SFD", "1 байт", 232, 106, ""), ("Destination MAC", "6 байт", 342, 238, ""),
        ("Source MAC", "6 байт", 585, 218, ""), ("802.1Q TAG", "4 байта", 807, 194, "tag"), ("EtherType", "2 байта", 1006, 152, ""),
        ("Data", "46–1500 байт", 1163, 310, ""), ("FCS", "4 байта", 1477, 145, "")]


def _row(row, top):
    out = []
    for r in row:
        t, b, x, w = r[:4]
        c = r[4] if len(r) > 4 else ""
        out.append('<div class="vi-f %s" style="left:%dpx;top:%dpx;width:%dpx"><b>%s</b><i>%s</i></div>' % (c, x, top, w, t, b))
    return "".join(out)


HTML = CSS + f"""
<div class="step">
  <div class="vi-pan" style="left:15px;top:150px;width:1642px;height:132px"></div>
  <div class="vi-h" style="left:60px;top:152px">НЕТЕГИРОВАННЫЙ КАДР</div>
  {_row(ROW1, 200)}
</div>
<div class="step">
  <div class="vi-pan" style="left:15px;top:288px;width:1642px;height:132px"></div>
  <div class="vi-h" style="left:60px;top:292px">ТЕГИРОВАННЫЙ КАДР <span style="color:#2ad4ff">802.1Q</span></div>
  {_row(ROW2, 338)}
</div>

<div class="step">
  <div class="vi-card" style="left:22px;top:460px;width:416px;height:124px"></div>
  {img("rep/vlan_intro_tag.png", "left:40px;top:478px;width:82px", "ab")}
  <div class="vi-ct" style="left:137px;top:480px;color:#2ad4ff">ТЕГИРОВАНИЕ</div>
  <div class="vi-tx" style="left:138px;top:516px">Добавление метки 802.1Q<br>в кадр Ethernet</div>
  <div class="vi-card" style="left:22px;top:606px;width:416px;height:126px"></div>
  {img("rep/vlan_intro_doc.png", "left:40px;top:630px;width:75px", "ab")}
  <div class="vi-ct" style="left:134px;top:642px;color:#2ad4ff">НЕТЕГИРОВАННЫЙ КАДР</div>
  <div class="vi-tx" style="left:135px;top:676px">Не содержит метку 802.1Q</div>
</div>

<div class="step">
  <div class="vi-card m" style="left:468px;top:472px;width:732px;height:238px;border-width:3px;box-shadow:0 0 24px rgba(155,107,255,.8),inset 0 0 26px rgba(155,107,255,.25)"></div>
  <div class="ab os" style="left:468px;top:484px;width:732px;text-align:center;font-family:Oswald,sans-serif;font-weight:600;font-size:31px;color:#fff">МЕТКА 802.1Q — 32 БИТА (4 БАЙТА)</div>
  <div class="vi-c" style="left:488px;top:537px;width:290px;height:154px;border:2px solid #9b6bff;background:rgba(70,30,150,.55);justify-content:flex-start;padding-top:12px;font-size:30px">TPID — 16 БИТ</div>
  <div class="vi-c" style="left:497px;top:598px;width:276px;height:84px;border:2px solid #9b6bff;background:rgba(30,12,80,.85);font-size:30px">0x8100</div>
  <div class="vi-c" style="left:784px;top:537px;width:400px;height:154px;border:2px solid #9b6bff;background:rgba(70,30,150,.55);justify-content:flex-start;padding-top:12px;font-size:30px">TCI — 16 БИТ</div>
  <div class="vi-c" style="left:790px;top:598px;width:97px;height:84px;border:2px solid #2ad4ff;background:rgba(18,60,140,.85);font-size:26px;line-height:1.2">PCP<br>3 БИТ</div>
  <div class="vi-c" style="left:893px;top:598px;width:78px;height:84px;border:2px solid #e05cff;background:rgba(80,20,120,.85);font-size:26px;line-height:1.2">DEI<br>1 БИТ</div>
  <div class="vi-c" style="left:977px;top:598px;width:200px;height:84px;border:3px solid #ffc53d;background:rgba(80,40,30,.85);box-shadow:0 0 14px rgba(255,197,61,.6);font-size:26px;line-height:1.2">VID<br>12 БИТ</div>
</div>

<div class="step">
  <div class="vi-card m" style="left:1234px;top:460px;width:416px;height:124px"></div>
  {img("rep/vlan_intro_doc2.png", "left:1258px;top:484px;width:74px", "ab")}
  <div class="vi-ct" style="left:1343px;top:480px;color:#f7a6ff">ТЕГИРОВАННЫЙ КАДР</div>
  <div class="vi-tx" style="left:1344px;top:518px">Содержит метку 802.1Q</div>
  <div class="vi-card" style="left:1234px;top:606px;width:416px;height:126px"></div>
  {img("rep/vlan_intro_bulb.png", "left:1248px;top:618px;width:84px", "ab")}
  <div class="vi-ct" style="left:1343px;top:625px;color:#2ad4ff">ЗАЧЕМ НУЖЕН ТЕГ?</div>
  <div class="vi-tx" style="left:1344px;top:662px;font-size:20px">Позволяет определить<br>принадлежность кадра к VLAN</div>
</div>

<div class="step">
  <div class="vi-card" style="left:80px;top:792px;width:1198px;height:88px"></div>
  <div class="ab" style="left:80px;top:810px;width:1198px;text-align:center;font-family:Oswald,sans-serif;font-weight:600;font-size:40px;color:#fff;line-height:52px">
    КАДР ETHERNET + МЕТКА <span style="color:#2ad4ff">802.1Q</span> = ТЕГИРОВАННЫЙ КАДР</div>
  <div class="vi-card" style="left:1302px;top:796px;width:338px;height:86px;border-color:rgba(42,212,255,.7)"></div>
  {img("rep/vlan_intro_gear.png", "left:1318px;top:806px;width:62px", "ab")}
  <div class="vi-tx" style="left:1387px;top:817px;font-size:17px;line-height:1.35">FCS пересчитывается<br>после вставки метки 802.1Q</div>
</div>
"""
