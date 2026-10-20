# -*- coding: utf-8 -*-
"""ETHERNET — протокол Ethernet: вёрстка 1:1 инфографики (pptx 3)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 168

CSS = """<style>
.eth-pan{position:absolute;border-radius:12px;border:2px solid rgba(42,212,255,.55);background:rgba(6,18,48,.86);
  box-shadow:0 0 18px rgba(42,212,255,.35),inset 0 0 30px rgba(42,212,255,.08)}
.eth-tx{position:absolute;color:#f2f6ff;font-family:'Golos Text',sans-serif;font-size:31px;line-height:1.24}
.eth-tx em{color:#2ad4ff;font-style:normal;font-weight:600}
.eth-li{position:absolute;left:62px;width:960px;height:64px;display:flex;align-items:center;gap:36px;font-size:24.5px;color:#eef3ff}
.eth-li i{display:inline-block;width:10px;height:10px;border-radius:50%;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff;margin-left:2px}
.eth-li img{width:80px;height:62px;border-radius:8px}
.eth-hr{position:absolute;height:2px;background:linear-gradient(90deg,#2ad4ff,rgba(42,212,255,.25));box-shadow:0 0 8px #2ad4ff}
@keyframes eth-glow{0%,100%{filter:brightness(1)}50%{filter:brightness(1.35)}}
.eth-art{animation:eth-glow 3.2s ease-in-out infinite}
</style>"""

ITEMS = [
    ("ethernet_i1.png", "формат передаваемого кадра;", 390),
    ("ethernet_i2.png", "правила адресации устройств;", 455),
    ("ethernet_i3.png", "способ доступа к среде передачи;", 519),
    ("ethernet_i4.png", "требования к физическому подключению;", 587),
    ("ethernet_i5.png", "действия устройств при возникновении коллизий.", 655),
]


def _items():
    return "".join(
        '<div class="eth-li step" style="top:%dpx;transition-delay:%dms">%s<i></i><span>%s</span></div>'
        % (y, k * 120, img("rep/" + ic), t) for k, (ic, t, y) in enumerate(ITEMS))


HTML = CSS + f"""
<div class="ab eth-art">{img("rep/ethernet_art.png", "left:1055px;top:170px;width:617px", "ab")}</div>
<div class="eth-pan" style="left:34px;top:186px;width:1018px;height:688px"></div>
<div class="eth-tx step" style="left:63px;top:205px;width:960px"><em>Ethernet</em> — семейство технологий, используемых для
передачи данных в проводных локальных сетях. Они определяются стандартами <em>IEEE 802.3</em>.</div>
<div class="eth-tx step" style="left:63px;top:347px"><em>Ethernet</em> описывает:</div>
{_items()}
<div class="step">
  <div class="eth-hr" style="left:63px;top:749px;width:960px"></div>
  <div class="eth-tx" style="left:63px;top:774px;width:980px;font-size:27px;line-height:1.36">На канальном уровне данные передаются в виде <em>кадров Ethernet.</em><br>
  Для доставки кадров используются <em>MAC-адреса.</em></div>
</div>
"""
