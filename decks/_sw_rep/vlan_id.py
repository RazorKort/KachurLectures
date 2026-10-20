# -*- coding: utf-8 -*-
"""Идентификатор VLAN — формат TCI, VLAN 10/20 на коммутаторе, таблица MAC."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 50

CSS = """<style>
.vd-pan{position:absolute;border-radius:12px;border:2px solid rgba(42,212,255,.7);background:rgba(6,24,64,.6);box-shadow:0 0 14px rgba(42,212,255,.4)}
.vd-tx{position:absolute;color:#e6f1ff;font-size:22px;line-height:1.3}
.vd-card{position:absolute;left:1190px;width:456px;border-radius:12px;border:2px solid #2ad4ff;background:rgba(8,30,80,.75);box-shadow:0 0 14px rgba(42,212,255,.5)}
.vd-ct{position:absolute;left:1305px;color:#fff;font-size:22px;line-height:1.3}
.vd-lbl{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:22px;color:#fff;text-align:center;line-height:1.2}
.vd-mono{font-family:'JetBrains Mono',monospace}
@keyframes vd-dash{to{stroke-dashoffset:-40}}
.vd-bc{animation:vd-dash 1.2s linear infinite}
@keyframes vd-blink{0%,100%{opacity:1}50%{opacity:.3}}
.vd-x{animation:vd-blink 1s ease-in-out infinite}
</style>"""

BITS = "".join('<div class="ab" style="left:%dpx;top:240px;width:1px;height:72px;background:rgba(224,92,255,.6)"></div>'
               % (416 + i * 57) for i in range(1, 12))

CARDS = [("vlan_id_i1.png", 58, 102, 1208, 78, 79, "VLAN ID — 12-битное поле<br>в составе TCI метки 802.1Q", 82),
         ("vlan_id_i2.png", 172, 86, 1212, 183, 71, "Диапазон: 1–4095", 200),
         ("vlan_id_i3.png", 272, 86, 1212, 283, 71, "VLAN 1 — сеть по умолчанию", 300),
         ("vlan_id_i4.png", 370, 92, 1212, 378, 71, "VLAN 1 и 4095<br>зарезервированы на Eltex", 388),
         ("vlan_id_i5.png", 476, 100, 1208, 492, 79, "Один VLAN = один<br>широковещательный домен", 498)]


def _cards():
    return "".join('<div class="step" style="transition-delay:%dms"><div class="vd-card" style="top:%dpx;height:%dpx"></div>%s'
                   '<div class="vd-ct" style="top:%dpx">%s</div></div>'
                   % (i * 80, t, h, img("rep/" + ic, "left:%dpx;top:%dpx;width:%dpx" % (x, y, w), "ab"), ty, txt)
                   for i, (ic, t, h, x, y, w, txt, ty) in enumerate(CARDS))


HTML = CSS + f"""
<div class="ab" style="left:12px;top:52px;width:1140px;height:298px;border-radius:14px;border:2px solid rgba(42,212,255,.45)"></div>
<div class="vd-tx" style="left:58px;top:110px;font-size:23px">VLAN ID определяет, к какой виртуальной локальной сети принадлежит кадр.<br>
  Коммутатор разделяет трафик по VLAN, изолируя широковещательные домены.</div>

<div class="step">
  <div class="vd-pan" style="left:45px;top:192px;width:1085px;height:142px"></div>
  <div class="ab" style="left:68px;top:198px;font-family:'Golos Text',sans-serif;font-weight:600;font-size:23px;color:#fff">Формат метки 802.1Q (TCI)</div>
  <div class="ab" style="left:74px;top:238px;width:340px;height:74px;border:2px solid #2ad4ff;background:rgba(18,60,140,.85);box-shadow:0 0 12px rgba(42,212,255,.6)"></div>
  <div class="ab" style="left:222px;top:240px;width:2px;height:72px;background:#2ad4ff"></div>
  <div class="vd-tx" style="left:100px;top:246px;width:120px;text-align:center;font-size:18px;line-height:1.2">3 бита<br>Priority<br>(PCP)</div>
  <div class="vd-tx" style="left:226px;top:246px;width:186px;text-align:center;font-size:18px;line-height:1.2">1 бит<br>DEI<br><span style="font-size:13px">(кол. отбрасывания)</span></div>
  <div class="ab" style="left:416px;top:238px;width:682px;height:74px;border:2px solid #e05cff;background:rgba(90,20,110,.7);box-shadow:0 0 14px rgba(224,92,255,.8)"></div>
  {BITS}
  <div class="vd-tx" style="left:416px;top:250px;width:714px;text-align:center;font-size:20px;line-height:1.2">12 бит<br>VLAN ID (VID)</div>
</div>

<div class="step">
  <div class="ab" style="left:36px;top:460px;width:570px;height:236px;border:2px dashed #2ad4ff;border-radius:8px;background:rgba(10,60,110,.25)"></div>
  <div class="ab" style="left:652px;top:460px;width:505px;height:236px;border:2px dashed #e05cff;border-radius:8px;background:rgba(90,20,110,.25)"></div>
  <div class="ab" style="left:62px;top:468px;font-family:Oswald,sans-serif;font-weight:600;font-size:30px;color:#2ad4ff">VLAN 10</div>
  <div class="vd-tx" style="left:62px;top:502px;font-size:18px;line-height:1.25;color:#2ad4ff">Широковещательный<br>домен VLAN 10</div>
  <div class="ab" style="left:1020px;top:468px;font-family:Oswald,sans-serif;font-weight:600;font-size:30px;color:#e05cff">VLAN 20</div>
  <div class="vd-tx" style="left:900px;top:502px;width:232px;text-align:right;font-size:18px;line-height:1.25">Широковещательный<br>домен VLAN 20</div>
  {img("rep/vlan_id_sw.png", "left:340px;top:340px;width:665px", "ab")}
</div>

<div class="step">
  <svg class="ab" style="left:0;top:0" width="1672" height="941" fill="none" stroke-width="4">
    <g stroke="#2ad4ff" style="filter:drop-shadow(0 0 4px #2ad4ff)">
      <path d="M516 426 V488 H330 V512 Q330 530 312 530 H200 V560"/>
      <path d="M560 426 V495 Q560 515 540 515 H470 V555"/></g>
    <g stroke="#ff5cd6" style="filter:drop-shadow(0 0 4px #ff5cd6)">
      <path d="M696 426 V520 Q696 545 720 545 H785 V560"/>
      <path d="M741 426 V475 Q741 495 760 495 H890 Q908 495 908 515 V530 Q908 548 930 548 H1015 L1020 565"/></g>
  </svg>
  {img("rep/vlan_id_pc1.png", "left:85px;top:553px;width:115px", "ab")}
  {img("rep/vlan_id_pc2.png", "left:405px;top:553px;width:117px", "ab")}
  {img("rep/vlan_id_pc3.png", "left:738px;top:553px;width:112px", "ab")}
  {img("rep/vlan_id_pc4.png", "left:1012px;top:553px;width:115px", "ab")}
  <div class="vd-lbl" style="left:108px;top:636px">ПК-1</div>
  <div class="vd-lbl" style="left:415px;top:636px">ПК-2</div>
  <div class="vd-lbl" style="left:758px;top:638px">ПК-3</div>
  <div class="vd-lbl" style="left:1037px;top:640px">ПК-4</div>
  <div class="vd-tx vd-mono" style="left:62px;top:662px;font-size:15px">MAC: 34:60:f9:5f:df:5f</div>
  <div class="vd-tx vd-mono" style="left:353px;top:662px;font-size:15px">MAC: a0:a3:f0:d1:26:5a</div>
</div>

<div class="step">
  <svg class="ab" style="left:0;top:0" width="1672" height="941" fill="none" stroke-width="3">
    <g stroke="#2ad4ff"><line class="vd-bc" x1="222" y1="586" x2="380" y2="586" stroke-dasharray="14 6"/>
      <path d="M215 586 l14 -8 v16 z M388 586 l-14 -8 v16 z" fill="#2ad4ff"/></g>
    <g stroke="#ff5cd6"><line class="vd-bc" x1="870" y1="586" x2="995" y2="586" stroke-dasharray="14 6"/>
      <path d="M862 586 l14 -8 v16 z M1003 586 l-14 -8 v16 z" fill="#ff5cd6"/></g>
    <g stroke="#ff5cd6" stroke-dasharray="8 6"><line x1="555" y1="598" x2="610" y2="598"/><line x1="652" y1="598" x2="712" y2="598"/></g>
    <path d="M548 598 l12 -7 v14 z M718 598 l-12 -7 v14 z" fill="#ff5cd6"/>
    <g class="vd-x" stroke="#ff5cd6" stroke-width="6"><line x1="616" y1="583" x2="646" y2="615"/><line x1="646" y1="583" x2="616" y2="615"/></g>
  </svg>
  <div class="vd-tx" style="left:222px;top:598px;width:158px;text-align:center;font-size:15px;line-height:1.25;color:#2ad4ff">Broadcast<br>(только в VLAN 10)</div>
  <div class="vd-tx" style="left:855px;top:600px;width:150px;text-align:center;font-size:15px;line-height:1.25;color:#ff9be8">Broadcast<br>(только в VLAN 20)</div>
  <div class="vd-tx" style="left:540px;top:628px;width:182px;text-align:center;font-size:16px;line-height:1.2">Широковещательный<br>трафик не проходит<br>между VLAN</div>
</div>

{_cards()}

<div class="step">
  <div class="vd-pan" style="left:18px;top:714px;width:1318px;height:206px"></div>
  <div class="ab vd-mono" style="left:44px;top:724px;font-size:23px;color:#2ad4ff">&gt; switch# show mac address-table</div>
  <pre class="ab vd-mono" style="left:58px;top:760px;margin:0;font-size:18px;line-height:1.3;color:#e6f1ff">VID      |  MAC Address           |  Interface                 |  Type
---------+------------------------+----------------------------+------------</pre>
  <div class="ab" style="left:42px;top:810px;width:880px;height:28px;border:1px solid #2ad4ff;border-radius:4px;background:rgba(42,212,255,.08)"></div>
  <div class="ab" style="left:42px;top:840px;width:880px;height:28px;border:1px solid #2ad4ff;border-radius:4px;background:rgba(42,212,255,.08)"></div>
  <pre class="ab vd-mono" style="left:58px;top:812px;margin:0;font-size:18px;line-height:30px;color:#fff">10       |  34:60:f9:5f:df:5f     |  gigabitethernet 1/0/2     |  Dynamic
10       |  a0:a3:f0:d1:26:5a     |  gigabitethernet 1/0/6     |  Dynamic</pre>
  <div class="ab vd-mono" style="left:46px;top:880px;font-size:18px;color:#e6f1ff">2 valid mac entries</div>
  <div class="ab" style="left:938px;top:800px;font-size:60px;line-height:1;color:#2ad4ff;font-weight:300">}}</div>
  <div class="ab" style="left:966px;top:838px;width:34px;border-top:2px dashed #2ad4ff"></div>
  <div class="ab" style="left:1002px;top:780px;width:312px;height:104px;border-radius:10px;border:2px solid #2ad4ff;background:rgba(8,30,80,.7)"></div>
  <div class="vd-tx" style="left:1030px;top:793px;font-size:20px;line-height:1.27">VID 10 хранится вместе<br>с изученным MAC-адресом<br>и портом коммутатора.</div>
</div>
"""
