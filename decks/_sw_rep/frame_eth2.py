# -*- coding: utf-8 -*-
"""FRAME_ETH2 — структура кадра Ethernet II: вёрстка 1:1 инфографики (pptx 4)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 236

CSS = """<style>
.fe2-nb{position:absolute;top:325px;height:150px;border-radius:8px;border:2px solid #2ad4ff;
  background:linear-gradient(180deg,rgba(18,70,170,.9),rgba(8,30,90,.92));box-shadow:0 0 16px rgba(42,212,255,.6),inset 0 0 20px rgba(42,212,255,.2);
  display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px;font-family:Oswald,sans-serif;font-weight:500;color:#fff;text-align:center;font-size:27px;line-height:1.12}
.fe2-nb span{font-size:27px}
.fe2-nb.v{border-color:#9b6bff;background:linear-gradient(180deg,rgba(80,36,170,.9),rgba(36,14,96,.92));box-shadow:0 0 16px rgba(155,107,255,.6),inset 0 0 20px rgba(155,107,255,.2)}
.fe2-nb.m{border-color:#e05cff;background:linear-gradient(180deg,rgba(150,30,170,.92),rgba(80,12,110,.92));box-shadow:0 0 16px rgba(224,92,255,.6),inset 0 0 20px rgba(224,92,255,.25)}
.fe2-nb.t{border-color:#2ad4ff;background:linear-gradient(180deg,rgba(14,120,150,.9),rgba(6,60,90,.95))}
.fe2-cd{position:absolute;top:537px;height:203px;border-radius:10px;border:1.5px solid rgba(42,212,255,.6);background:rgba(8,26,60,.82);
  box-shadow:0 0 10px rgba(42,212,255,.3);display:flex;flex-direction:column;align-items:center;padding-top:16px;text-align:center;
  font-family:'Golos Text',sans-serif;font-size:19px;line-height:1.18;color:#dfe9ff}
.fe2-cd b{font-family:Oswald,sans-serif;font-weight:500;font-size:26px;line-height:1.0;color:#2ad4ff;margin:8px 0 10px}
.fe2-cd.v{border-color:rgba(155,107,255,.75);background:rgba(36,18,80,.8)}.fe2-cd.v b{color:#fff}
.fe2-cd.m{border-color:rgba(224,92,255,.75);background:rgba(50,14,80,.8)}.fe2-cd.m b{color:#fff}
.fe2-cd.e b{color:#e6e9ff}
.fe2-vl{position:absolute;width:2px;background:#2ad4ff;box-shadow:0 0 6px #2ad4ff}
.fe2-dot{position:absolute;width:9px;height:9px;border-radius:50%;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff}
.fe2-ln{position:absolute;height:2px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff}
.fe2-os{font-family:Oswald,sans-serif;font-weight:500}
@keyframes fe2-run{0%{left:30px;opacity:0}8%{opacity:1}92%{opacity:1}100%{left:1366px;opacity:0}}
.fe2-bit{position:absolute;top:293px;width:12px;height:12px;border-radius:50%;background:#fff;box-shadow:0 0 12px #2ad4ff,0 0 4px #fff;animation:fe2-run 4s linear infinite}
</style>"""

# подпись, байты, x, w, класс; связанная карточка: иконка, заголовок, текст, x, w, класс
FIELDS = [
    ("Преамбула", "7 байт", 24, 196, "", "frame_eth2_wave.png", "Преамбула", "синхронизация<br>приёмника", 28, 170, ""),
    ("SFD", "1 байт", 226, 102, "", "frame_eth2_sfd.png", "SFD", "признак<br>начала кадра", 211, 143, "e"),
    ("MAC<br>назначения", "6 байт", 334, 184, "v", "frame_eth2_tri.png", "MAC<br>назначения", "адрес<br>получателя", 367, 173, "v"),
    ("MAC<br>источника", "6 байт", 524, 176, "m", "frame_eth2_tri2.png", "MAC<br>источника", "адрес<br>отправителя", 552, 166, "m"),
    ("EtherType", "2 байта", 706, 178, "v", "frame_eth2_doc.png", "EtherType", "протокол<br>полезной<br>нагрузки", 731, 197, "v"),
    ("Полезная нагрузка", "46–1500 байт", 890, 330, "t", "frame_eth2_db.png", "Payload", "данные<br>верхнего уровня", 941, 301, ""),
    ("FCS", "4 байта", 1226, 156, "", "frame_eth2_shield.png", "FCS", "обнаружение<br>ошибок<br>(CRC-32)", 1255, 208, "e"),
]


def _row():
    return "".join(
        '<div class="fe2-nb %s step" style="left:%dpx;width:%dpx;transition-delay:%dms"><div>%s</div><span>%s</span></div>'
        % (c, x, w, k * 80, t, b, ) for k, (t, b, x, w, c, *_r) in enumerate(FIELDS))


def _cards():
    out = []
    for k, (_t, _b, x, w, _c, ic, h, tx, cx, cw, cc) in enumerate(FIELDS):
        mx = x + w // 2
        out.append('<div class="step" style="transition-delay:%dms"><div class="fe2-vl" style="left:%dpx;top:478px;height:46px"></div>'
                   '<div class="fe2-dot" style="left:%dpx;top:521px"></div>'
                   '<div class="fe2-cd %s" style="left:%dpx;width:%dpx">%s<b>%s</b><div>%s</div></div></div>'
                   % (k * 90, mx - 1, mx - 4, cc, cx, cw, img("rep/" + ic, "height:50px"), h, tx))
    return "".join(out)


HTML = CSS + f"""
<div class="step">
  <div class="ab fe2-os" style="left:0;top:244px;width:1662px;text-align:center;font-size:30px;color:#2ad4ff;letter-spacing:1px">КАДР ETHERNET II</div>
  <div class="fe2-ln" style="left:30px;top:298px;width:580px"></div>
  <div class="fe2-ln" style="left:1008px;top:298px;width:370px"></div>
  <div class="ab" style="left:24px;top:290px;color:#2ad4ff;font-size:16px;line-height:16px">◀</div>
  <div class="ab" style="left:1370px;top:290px;color:#2ad4ff;font-size:16px;line-height:16px">▶</div>
  <div class="ab fe2-os" style="left:596px;top:286px;width:426px;white-space:nowrap;text-align:center;font-size:19px;color:#2ad4ff;letter-spacing:1.5px;font-weight:400">ОТ 64 ДО 1518 БАЙТ (БЕЗ УЧЕТА IPG)</div>
  <div class="fe2-bit"></div>
  <div class="ab fe2-os" style="left:1416px;top:268px;width:232px;text-align:center;font-size:17px;color:#e6efff;letter-spacing:1px">НЕ ВХОДИТ В КАДР</div>
  <div class="ab" style="left:1416px;top:297px;width:228px;height:2px;background:#e6efff"></div>
</div>
{_row()}
<div class="step" style="transition-delay:600ms">
  <div class="ab" style="left:1397px;top:290px;width:0;height:195px;border-left:2px dashed rgba(42,212,255,.6)"></div>
  <div class="ab" style="left:1416px;top:325px;width:232px;height:151px;border:2px dashed #b9c8ec;border-radius:8px;background:rgba(10,22,54,.65)"></div>
  {img("rep/frame_eth2_clock.png", "left:1434px;top:365px;width:68px", "ab")}
  <div class="ab fe2-os" style="left:1515px;top:337px;font-size:29px;color:#fff;line-height:1.35">IPG<br>12 байт</div>
  <div class="ab" style="left:1516px;top:413px;font-size:18px;color:#dfe9ff;line-height:1.3">(96 битовых<br>интервалов)</div>
</div>
{_cards()}
<div class="step">
  <div class="ab" style="left:824px;top:742px;width:0;height:32px;border-left:2px dashed rgba(42,212,255,.7)"></div>
  <div class="ab fe2-os" style="left:628px;top:774px;width:619px;height:56px;border-radius:10px;border:2px solid rgba(42,212,255,.7);background:rgba(8,30,66,.85);
    box-shadow:0 0 12px rgba(42,212,255,.4);display:flex;align-items:center;justify-content:center;gap:26px;font-size:22px;color:#fff;font-weight:400">
    <span>0x0800 — IPv4</span><span style="color:#2ad4ff">•</span><span>0x0806 — ARP</span><span style="color:#2ad4ff">•</span><span>0x86DD — IPv6</span></div>
</div>
"""
