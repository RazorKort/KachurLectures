# -*- coding: utf-8 -*-
"""SNAP — 5 байт: вёрстка 1:1 инфографики (pptx 6). ЭТАЛОН для остальных."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 145   # полоса заголовка оригинала срезана: заголовок даёт head() слайда

CSS = """<style>
.snp-nb{position:absolute;border-radius:8px;border:2px solid #2ad4ff;background:linear-gradient(180deg,rgba(18,60,140,.85),rgba(8,24,70,.9));
  box-shadow:0 0 14px rgba(42,212,255,.55),inset 0 0 18px rgba(42,212,255,.18);display:flex;flex-direction:column;align-items:center;justify-content:space-between;
  padding:12px 6px 10px;font-family:Oswald,sans-serif;color:#fff;text-align:center}
.snp-nb b{font-weight:500;font-size:25px;line-height:1}.snp-nb span{font-weight:500;font-size:24px;line-height:1}
.snp-nb.snp-v{border-color:#9b6bff;background:linear-gradient(180deg,rgba(70,30,150,.85),rgba(30,12,80,.9));box-shadow:0 0 14px rgba(155,107,255,.55),inset 0 0 18px rgba(155,107,255,.2)}
.snp-nb.snp-m{border-color:#e05cff;background:linear-gradient(180deg,rgba(110,25,140,.85),rgba(50,10,80,.9));box-shadow:0 0 14px rgba(224,92,255,.55),inset 0 0 18px rgba(224,92,255,.2)}
.snp-nb.snp-t{border-color:#2ad4ff;background:linear-gradient(180deg,rgba(14,110,140,.9),rgba(6,50,80,.95))}
.snp-nb.snp-hi{box-shadow:0 0 26px rgba(42,212,255,.95),inset 0 0 22px rgba(42,212,255,.35);border-width:3px}
.snp-nb.snp-dash{border:2px dashed #9fb8e8;background:rgba(10,20,50,.6);box-shadow:none}
.snp-pan{position:absolute;border-radius:12px;border:2px solid #2ad4ff;background:rgba(6,24,64,.82);box-shadow:0 0 14px rgba(42,212,255,.45)}
.snp-pan.snp-m{border-color:#d95cff;background:rgba(40,10,70,.82);box-shadow:0 0 14px rgba(217,92,255,.45)}
.snp-big{position:absolute;border-radius:16px;border:3px solid #d95cff;background:rgba(30,10,70,.55);box-shadow:0 0 28px rgba(217,92,255,.6),inset 0 0 40px rgba(120,40,200,.25)}
.snp-chip{position:absolute;border-radius:8px;border:2px solid #7b5cff;background:linear-gradient(180deg,#2a1a8a,#1a0f5c);box-shadow:0 0 14px rgba(123,92,255,.6);
  display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-size:30px;font-weight:500;color:#fff}
.snp-tx{position:absolute;color:#e6f1ff;font-size:22px;line-height:1.32}.snp-tx em{color:#2ad4ff;font-style:normal}
.snp-os{font-family:Oswald,sans-serif;font-weight:500}
.snp-ln{position:absolute;height:2px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff}
</style>"""

FRAME = [  # подпись, иконка, байты, x, w, класс
    ("Преамбула", "snap_wave.png", "7 байт", 26, 166, ""),
    ("SFD", "snap_sfd.png", "1 байт", 196, 96, ""),
    ("D.MAC", "snap_tri.png", "6 байт", 296, 140, "snp-v"),
    ("S.MAC", "snap_tri.png", "6 байт", 440, 140, "snp-m"),
    ("Length", "snap_doc.png", "2 байта", 584, 134, "snp-m"),
    ("LLC", "snap_layers.png", "3 байта", 722, 136, "snp-v"),
    ("SNAP", "snap_layers.png", "5 байта", 864, 192, "snp-hi"),
    ("Данные", "snap_db.png", "", 1060, 240, "snp-t"),
    ("FCS", "snap_shield.png", "4 байта", 1304, 132, ""),
]


def _frame():
    out = []
    for i, (t, ic, by, x, w, c) in enumerate(FRAME):
        out.append('<div class="snp-nb %s step" style="left:%dpx;top:192px;width:%dpx;height:142px;transition-delay:%dms">'
                   '<b>%s</b>%s<span>%s</span></div>' % (c, x, w, i * 70, t, img("rep/" + ic, "height:44px"), by))
    return "".join(out)


HTML = CSS + f"""
<div class="snp-ln" style="left:30px;top:171px;width:640px"></div>
<div class="snp-ln" style="left:1005px;top:171px;width:426px"></div>
<div class="ab snp-os" style="left:690px;top:150px;font-size:28px;color:#2ad4ff">КАДР IEEE 802.3 LLC</div>
<div class="ab snp-os" style="left:1470px;top:146px;font-size:18px;color:#cfe0ff">НЕ ВХОДИТ В КАДР</div>
{_frame()}
<div class="snp-nb snp-dash step" style="left:1464px;top:192px;width:184px;height:142px;justify-content:center;gap:10px">
  <b>IPG</b><div style="display:flex;gap:10px;align-items:center">{img("rep/snap_clock.png", "height:44px")}<span>12 байт</span></div></div>

<div class="snp-big step" style="left:22px;top:360px;width:1628px;height:560px"></div>
<div class="ab step" style="left:0;top:368px;width:1672px;text-align:center">
  <div style="font-family:Oswald,sans-serif;font-weight:700;font-size:62px;line-height:1.05;color:#fff">SNAP — <span style="color:#2ad4ff">5 БАЙТ</span></div>
  <div style="font-size:22px;color:#e6f1ff">SNAP расширяет пространство идентификаторов и позволяет указывать тип вложенного протокола аналогично EtherType.</div></div>

<div class="step">
  <div class="ab snp-os" style="left:54px;top:466px;width:796px;height:62px;border-radius:8px 0 0 8px;background:linear-gradient(180deg,#1a6fe0,#0d3c9a);
    border:2px solid #2ad4ff;box-shadow:0 0 16px rgba(42,212,255,.7);display:flex;align-items:center;justify-content:center;font-size:32px;color:#fff">
    <span style="color:#2ad4ff">OUI</span>&nbsp;— 3 байта</div>
  <div class="ab snp-os" style="left:850px;top:466px;width:768px;height:62px;border-radius:0 8px 8px 0;background:linear-gradient(180deg,#8a2ad8,#4d1290);
    border:2px solid #e05cff;box-shadow:0 0 16px rgba(224,92,255,.7);display:flex;align-items:center;justify-content:center;font-size:32px;color:#fff">Protocol ID — 2 байта</div>
</div>

<div class="step">
  <div class="snp-pan" style="left:54px;top:545px;width:772px;height:180px"></div>
  {img("rep/snap_bld.png", "left:80px;top:562px;width:72px", "ab")}
  <div class="ab snp-os" style="left:172px;top:560px;font-size:29px;color:#2ad4ff">OUI — Organizationally Unique Identifier</div>
  <div class="snp-tx" style="left:172px;top:598px;width:640px">Идентификатор организации, определившей протокол.<br>
    Стандартное значение: <em class="snp-os" style="font-size:25px">00-00-00</em><br>
    При OUI <em class="snp-os" style="font-size:25px">00-00-00</em> поле Protocol ID интерпретируется как EtherType.</div>
</div>

<div class="step">
  <div class="snp-pan snp-m" style="left:846px;top:545px;width:774px;height:180px"></div>
  {img("rep/snap_doc2.png", "left:872px;top:556px;width:54px", "ab")}
  <div class="ab" style="left:945px;top:566px;font-size:24px;color:#fff"><span class="snp-os" style="font-size:28px">Protocol ID</span> — идентификатор протокола в поле данных</div>
  <div class="snp-chip" style="left:864px;top:620px;width:240px;height:92px;flex-direction:column;font-size:28px;line-height:1.15"><span style="color:#cfe0ff">0x0800</span>— IPv4</div>
  <div class="snp-chip" style="left:1117px;top:620px;width:238px;height:92px;flex-direction:column;font-size:28px;line-height:1.15"><span style="color:#cfe0ff">0x0806</span>— ARP</div>
  <div class="snp-chip" style="left:1368px;top:620px;width:238px;height:92px;flex-direction:column;font-size:28px;line-height:1.15"><span style="color:#cfe0ff">0x86DD</span>— IPv6</div>
</div>

<div class="step">
  <div class="snp-pan" style="left:54px;top:740px;width:1564px;height:82px"></div>
  {img("rep/snap_doc3.png", "left:84px;top:752px;width:50px", "ab")}
  <div class="ab snp-os" style="left:160px;top:748px;font-size:28px;line-height:1.1;color:#2ad4ff">Пример SNAP<br>для IPv4:</div>
  <div class="snp-chip" style="left:384px;top:750px;width:322px;height:60px">LLC: AA-AA-03</div>
  <div class="ab" style="left:722px;top:762px;width:52px;height:30px;color:#2ad4ff;font-size:40px;line-height:30px">➜</div>
  <div class="snp-chip" style="left:789px;top:750px;width:322px;height:60px"><span style="color:#2ad4ff">OUI:</span>&nbsp;00-00-00</div>
  <div class="ab" style="left:1132px;top:762px;width:60px;height:30px;color:#2ad4ff;font-size:40px;line-height:30px">➜</div>
  <div class="snp-chip" style="left:1210px;top:750px;width:372px;height:60px;border-color:#e05cff;background:linear-gradient(180deg,#5a1580,#330a50)">Type: 08-00 (IPv4)</div>
</div>

<div class="step">
  <div class="snp-pan" style="left:54px;top:836px;width:1564px;height:76px"></div>
  {img("rep/snap_info.png", "left:84px;top:845px;width:58px", "ab")}
  <div class="snp-tx" style="left:174px;top:846px;font-size:21px">IEEE 802.3 <em>LLC/SNAP</em> определяет, какой протокол или служба должны обработать данные.<br>
    В современных Ethernet-сетях чаще используется EtherType формата Ethernet II.</div>
</div>
"""
