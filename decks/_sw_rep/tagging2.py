# -*- coding: utf-8 -*-
"""Процесс тегирования кадров (вариант 2) — кадр без тега/с тегом, красный порт, рассылка в VLAN."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 160

R, B = "#ff4d5e", "#2ad4ff"

CSS = """<style>
.tg2-pan{position:absolute;top:186px;height:144px;border-radius:12px;border:2px solid rgba(42,212,255,.7);background:rgba(6,24,64,.6);box-shadow:0 0 14px rgba(42,212,255,.4)}
.tg2-pt{position:absolute;top:192px;font-family:'Golos Text',sans-serif;font-weight:700;font-size:23px;color:#fff;text-align:center}
.tg2-c{position:absolute;top:240px;height:62px;border-radius:6px;display:flex;align-items:center;justify-content:center;color:#fff;
  font-family:'Golos Text',sans-serif;font-weight:500;font-size:18px;border:2px solid var(--b);background:var(--f);box-shadow:0 0 10px var(--b)}
.tg2-bx{position:absolute;border-radius:8px;border:2px solid #2ad4ff;background:rgba(6,24,64,.75);box-shadow:0 0 12px rgba(42,212,255,.5);color:#fff;
  text-align:center;font-family:'Golos Text',sans-serif;font-weight:700}
.tg2-row{position:absolute;left:598px;width:468px;height:54px;border-radius:8px;border:1px solid rgba(42,212,255,.6);background:rgba(10,40,100,.35)}
.tg2-rt{position:absolute;left:694px;font-size:21px;color:#fff;font-weight:500}
@keyframes tg2-run{to{stroke-dashoffset:-60}}
.tg2-flow{stroke-dasharray:18 12;animation:tg2-run 1s linear infinite}
@keyframes tg2-pop{0%,100%{transform:scale(1)}50%{transform:scale(1.08)}}
.tg2-tag{animation:tg2-pop 1.6s ease-in-out infinite}
</style>"""

C_BLUE = ("#2ad4ff", "linear-gradient(180deg,#1a6fe0,#0d3c9a)")
C_YEL = ("#ffc53d", "linear-gradient(180deg,#c9932a,#8a5a12)")
C_PINK = ("#e05c9a", "linear-gradient(180deg,#b04a7a,#702a52)")
C_GRAY = ("#9fb8e8", "linear-gradient(180deg,#6f86b8,#45577f)")
C_RED = ("#ff4d5e", "linear-gradient(180deg,#e0202f,#99101c)")
F1 = [(115, 92, "DMAC", C_BLUE), (212, 93, "SMAC", C_BLUE), (310, 94, "EtherType", C_YEL), (410, 136, "Данные", C_PINK), (552, 63, "FCS", C_GRAY)]
F2 = [(1037, 90, "DMAC", C_BLUE), (1132, 81, "SMAC", C_BLUE), (1218, 85, "802.1Q", C_RED), (1309, 87, "EtherType", C_YEL),
      (1402, 111, "Данные", C_PINK), (1519, 63, "FCS", C_GRAY)]


def _cells(cells):
    return "".join('<div class="tg2-c%s" style="--b:%s;--f:%s;left:%dpx;width:%dpx">%s</div>'
                   % (" tg2-tag" if t == "802.1Q" else "", c[0], c[1], x, w, t) for x, w, t, c in cells)


HTML = CSS + f"""
<div class="step">
  <div class="tg2-pan" style="left:80px;width:570px"></div><div class="tg2-pt" style="left:80px;width:570px">Кадр без тега</div>
  {_cells(F1)}
</div>

<div class="step">
  {img("rep/tagging2_pc.png", "left:25px;top:403px;width:252px", "ab")}
  <div class="tg2-bx" style="left:28px;top:552px;width:244px;height:74px;font-size:23px;line-height:1.1;padding-top:10px">Оконечное<br>устройство</div>
  <div class="ab" style="left:334px;top:432px;font-family:'Golos Text',sans-serif;font-weight:700;font-size:23px;color:#fff">Входящий кадр</div>
  <svg class="ab" style="left:300px;top:466px" width="252" height="24"><line x1="10" y1="12" x2="226" y2="12" stroke="{B}" stroke-width="5" style="filter:drop-shadow(0 0 5px {B})"/><path d="M248 12 L224 0 V24 Z" fill="{B}"/></svg>
</div>
<div class="step">
  {img("rep/tagging2_sw.png", "left:588px;top:378px;width:574px", "ab")}
  <svg class="ab" style="left:0;top:0" width="1672" height="941" fill="none">
    <path d="M250 512 H640 Q680 512 694 488" stroke="{R}" stroke-width="5" style="filter:drop-shadow(0 0 6px {R})"/>
    <path class="tg2-flow" d="M250 512 H640 Q680 512 694 488" stroke="#fff" stroke-width="2" opacity=".8"/>
    <line x1="738" y1="370" x2="700" y2="470" stroke="{R}" stroke-width="2"/></svg>
  <div class="tg2-bx" style="left:668px;top:325px;width:186px;height:44px;border-color:{R};background:rgba(110,15,30,.85);box-shadow:0 0 12px {R};font-size:21px;line-height:40px;color:#ffb0b8">Красный порт</div>
  <div class="tg2-bx" style="left:712px;top:530px;width:246px;height:48px;font-size:24px;line-height:44px">Коммутатор</div>
</div>

<div class="step">
  <div class="ab" style="left:570px;top:590px;width:522px;height:226px;border-radius:12px;border:2px solid rgba(42,212,255,.7);background:rgba(6,24,64,.55);box-shadow:0 0 14px rgba(42,212,255,.4)"></div>
  <div class="tg2-row" style="top:610px"></div><div class="tg2-row" style="top:673px"></div><div class="tg2-row" style="top:738px"></div>
  {img("rep/tagging2_i1.png", "left:612px;top:612px;width:56px", "ab")}
  {img("rep/tagging2_i2.png", "left:612px;top:676px;width:56px", "ab")}
  {img("rep/tagging2_i3.png", "left:612px;top:738px;width:56px", "ab")}
  <div class="tg2-rt" style="top:622px">Добавление тега 802.1Q (32 бита)</div>
  <div class="tg2-rt" style="top:686px">Пересчёт FCS</div>
  <div class="tg2-rt" style="top:751px">VLAN ID определяет порты</div>
</div>

<div class="step">
  <div class="tg2-pan" style="left:1012px;width:592px"></div><div class="tg2-pt" style="left:1012px;width:592px">Кадр с тегом</div>
  {_cells(F2)}
</div>

<div class="step">
  <svg class="ab" style="left:0;top:0" width="1672" height="941" fill="none" stroke-width="4">
    <g stroke="{R}" style="filter:drop-shadow(0 0 5px {R})"><path d="M1140 438 H1200 Q1235 438 1245 410 Q1255 385 1290 385 H1330"/><path d="M1140 480 H1330"/></g>
    <g stroke="#fff" stroke-width="2" opacity=".8"><path class="tg2-flow" d="M1140 438 H1200 Q1235 438 1245 410 Q1255 385 1290 385 H1330"/><path class="tg2-flow" d="M1140 480 H1330"/></g>
    <path d="M1348 385 l-20 -10 v20 z M1348 480 l-20 -10 v20 z" fill="{R}"/>
    <g stroke="{B}" stroke-width="2.5" stroke-dasharray="6 5"><path d="M1140 510 H1240 V578 H1312"/><path d="M1140 545 H1218 V660 H1312"/></g>
    <g stroke="{B}" stroke-width="4"><path d="M1318 568 l20 20 M1338 568 l-20 20"/><path d="M1318 650 l20 20 M1338 650 l-20 20"/></g>
    <path d="M1488 370 H1496 V498 H1488" stroke="{R}" stroke-width="2.5"/><path d="M1488 560 H1496 V690 H1488" stroke="{B}" stroke-width="2.5"/>
  </svg>
  {img("rep/tagging2_p1.png", "left:1356px;top:355px;width:124px", "ab")}
  {img("rep/tagging2_p2.png", "left:1356px;top:453px;width:124px", "ab")}
  {img("rep/tagging2_p3.png", "left:1356px;top:546px;width:124px", "ab")}
  {img("rep/tagging2_p4.png", "left:1356px;top:633px;width:124px", "ab")}
  <div class="ab" style="left:1513px;top:402px;font-size:18px;line-height:1.28;color:{R}">Порты<br>VLAN (красная)<br>— активны</div>
  <div class="ab" style="left:1513px;top:592px;font-size:18px;line-height:1.28;color:{B}">Порты<br>других VLAN<br>— неактивны</div>
</div>

<div class="step">
  <div class="ab" style="left:1128px;top:727px;width:476px;height:84px;border-radius:12px;border:2px solid {R};background:rgba(30,6,20,.75);box-shadow:0 0 16px rgba(255,77,94,.7)"></div>
  <svg class="ab" style="left:1160px;top:752px" width="68" height="32"><line x1="0" y1="16" x2="46" y2="16" stroke="{R}" stroke-width="6"/><path d="M66 16 L42 2 V30 Z" fill="{R}"/></svg>
  <div class="ab" style="left:1256px;top:738px;font-family:'Golos Text',sans-serif;font-weight:600;font-size:22px;line-height:1.3;color:#fff">Передача только в порты<br>разрешённой VLAN</div>
</div>
"""
