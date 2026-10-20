# -*- coding: utf-8 -*-
"""FRAME_LLC — структура кадра IEEE 802.3 LLC: вёрстка 1:1 инфографики (pptx 5)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 178

CSS = """<style>
.fll-nb{position:absolute;top:237px;height:150px;border-radius:8px;border:2px solid #2ad4ff;
  background:linear-gradient(180deg,rgba(18,70,170,.9),rgba(8,30,90,.92));box-shadow:0 0 16px rgba(42,212,255,.6),inset 0 0 20px rgba(42,212,255,.2);
  display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:16px 4px 8px;font-family:Oswald,sans-serif;font-weight:500;color:#fff;text-align:center}
.fll-nb b{font-weight:500;font-size:24px;line-height:1}.fll-nb span{font-size:25px;line-height:1}
.fll-nb.v{border-color:#9b6bff;background:linear-gradient(180deg,rgba(80,36,170,.9),rgba(36,14,96,.92));box-shadow:0 0 16px rgba(155,107,255,.6),inset 0 0 20px rgba(155,107,255,.2)}
.fll-nb.m{border-color:#e05cff;background:linear-gradient(180deg,rgba(130,30,160,.9),rgba(64,12,96,.92));box-shadow:0 0 16px rgba(224,92,255,.6),inset 0 0 20px rgba(224,92,255,.25)}
.fll-nb.t{border-color:#2ad4ff;background:linear-gradient(180deg,rgba(14,120,150,.9),rgba(6,60,90,.95))}
.fll-pan{position:absolute;top:424px;height:480px;border-radius:14px;border:3px solid #d95cff;background:rgba(36,10,64,.82);
  box-shadow:0 0 22px rgba(217,92,255,.55),inset 0 0 40px rgba(120,40,200,.2)}
.fll-pan.b{border-color:#2a9dff;background:rgba(6,22,62,.84);box-shadow:0 0 22px rgba(42,157,255,.55),inset 0 0 40px rgba(42,157,255,.15)}
.fll-tx{position:absolute;color:#f2f6ff;font-family:'Golos Text',sans-serif;font-size:29px;line-height:40px}
.fll-tx em{color:#2ad4ff;font-style:normal;font-weight:600}
.fll-os{font-family:Oswald,sans-serif;font-weight:500}
.fll-rg{position:absolute;top:682px;height:130px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
  font-family:'Golos Text',sans-serif;font-size:24px;line-height:31px;color:#f2f6ff}
.fll-rg b{font-family:Oswald,sans-serif;font-weight:500;font-size:31px;line-height:36px}
.fll-dot{position:absolute;width:14px;height:14px;border-radius:50%}
.fll-f{position:absolute;top:613px;height:82px;border-radius:6px;display:flex;flex-direction:column;align-items:center;justify-content:center;
  font-family:Oswald,sans-serif;font-weight:500;color:#fff;font-size:26px;line-height:34px}
.fll-f span{font-family:'Golos Text',sans-serif;font-weight:400;font-size:25px}
.fll-d{position:absolute;top:728px;text-align:center;font-size:20.5px;line-height:26px;color:#e6efff}
@keyframes fll-pulse{0%,100%{box-shadow:0 0 6px currentColor}50%{box-shadow:0 0 18px currentColor,0 0 4px #fff}}
.fll-dot{animation:fll-pulse 1.8s ease-in-out infinite}
</style>"""

FRAME = [
    ("Преамбула", "frame_llc_wave.png", "7 байт", 28, 165, ""),
    ("SFD", "frame_llc_sfd.png", "1 байт", 199, 97, ""),
    ("D.MAC", "frame_llc_tri.png", "6 байт", 302, 135, "v"),
    ("S.MAC", "frame_llc_tri2.png", "6 байт", 443, 135, "m"),
    ("Length", "frame_llc_doc.png", "2 байта", 584, 128, "m"),
    ("LLC", "frame_llc_lay.png", "3 байта", 718, 128, "v"),
    ("SNAP", "frame_llc_lay2.png", "5 байт", 852, 142, ""),
    ("Данные", "frame_llc_db.png", "", 1000, 283, "t"),
    ("FCS", "frame_llc_shield.png", "4 байта", 1289, 137, ""),
]


def _frame():
    return "".join(
        '<div class="fll-nb %s step" style="left:%dpx;width:%dpx;transition-delay:%dms"><b>%s</b>%s<span>%s</span></div>'
        % (c, x, w, i * 70, t, img("rep/" + ic, "height:%dpx" % (62 if t == "Данные" else 46)), by)
        for i, (t, ic, by, x, w, c) in enumerate(FRAME))


def _field(x, w, name, col, grad, desc):
    mx = x + w // 2
    return ('<div class="fll-f" style="left:%dpx;width:%dpx;border:2px solid %s;background:%s;box-shadow:0 0 14px %s">%s<span>1 байт</span></div>'
            '<div class="ab" style="left:%dpx;top:697px;width:2px;height:16px;background:%s"></div>'
            '<div class="fll-dot" style="left:%dpx;top:710px;width:10px;height:10px;background:%s;color:%s"></div>'
            '<div class="fll-d" style="left:%dpx;width:%dpx">%s</div>'
            % (x, w, col, grad, col, name, mx - 1, col, mx - 5, col, col, x - 10, w + 20, desc))


HTML = CSS + f"""
<div class="step">
  <div class="ab" style="left:32px;top:212px;width:620px;height:2px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff"></div>
  <div class="ab" style="left:1020px;top:212px;width:405px;height:2px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff"></div>
  <div class="ab fll-os" style="left:652px;top:183px;width:368px;text-align:center;font-size:30px;color:#2ad4ff;letter-spacing:1px">КАДР IEEE 802.3 LLC</div>
  <div class="ab fll-os" style="left:1446px;top:185px;width:204px;text-align:center;font-size:17px;color:#e6efff;letter-spacing:1px">НЕ ВХОДИТ В КАДР</div>
  <div class="ab" style="left:1450px;top:212px;width:196px;height:2px;background:#e6efff"></div>
  <div class="ab" style="left:1443px;top:200px;height:200px;border-left:2px dashed rgba(230,239,255,.55)"></div>
</div>
{_frame()}
<div class="step" style="transition-delay:640ms">
  <div class="ab" style="left:1455px;top:237px;width:193px;height:151px;border:2px dashed #b9c8ec;border-radius:8px;background:rgba(10,22,54,.65)"></div>
  {img("rep/frame_llc_clock.png", "left:1468px;top:268px;width:61px", "ab")}
  <div class="ab fll-os" style="left:1538px;top:250px;font-size:25px;color:#fff;line-height:35px">IPG<br>12 байт</div>
  <div class="ab" style="left:1455px;top:330px;width:197px;text-align:center;font-size:18px;color:#dfe9ff;line-height:23px">(96 битовых<br>интервалов)</div>
</div>

<div class="step">
  <div class="fll-pan" style="left:28px;width:798px"></div>
  {img("rep/frame_llc_docbig.png", "left:64px;top:442px;width:68px", "ab")}
  <div class="ab fll-os" style="left:162px;top:443px;font-size:54px;line-height:72px;font-weight:700;color:#f07bff">Length <span style="color:#fff;font-size:40px;font-weight:500">— 2 байта</span></div>
  <div class="ab" style="left:64px;top:522px;width:726px;height:1px;background:rgba(217,92,255,.4)"></div>
  <div class="fll-tx" style="left:64px;top:535px;width:760px">Количество байт после поля <em>Length</em> и до <em>FCS</em>.<br>
    В длину входят: <em>LLC</em> + <em>SNAP</em> + данные.<br>Максимальное значение: <em>1500 байт</em>.</div>
</div>
<div class="step">
  <div class="fll-rg" style="left:60px;width:220px;border:2px solid #2affa0;border-radius:10px 0 0 10px;background:rgba(10,90,80,.55);box-shadow:0 0 12px rgba(42,255,160,.45)">
    <b style="color:#2ad4ff">0–1500</b>— Length<br>(IEEE 802.3)</div>
  <div class="fll-rg" style="left:280px;width:260px;border:2px solid #ffc53d;background:rgba(130,90,20,.55);box-shadow:0 0 12px rgba(255,197,61,.45)">
    <b style="color:#ffc53d">1501–1535</b>— зарезервировано</div>
  <div class="fll-rg" style="left:540px;width:258px;border:2px solid #e05cff;border-radius:0 10px 10px 0;background:rgba(90,20,110,.55);box-shadow:0 0 12px rgba(224,92,255,.45)">
    <b style="color:#ffd6ff">1536–65535</b>— EtherType<br><span style="color:#d7b6ff">(Ethernet II)</span></div>
</div>
<div class="step">
  <div class="ab" style="left:62px;top:832px;width:728px;height:3px;background:linear-gradient(90deg,#2ad4ff,#2affa0 30%,#ffc53d 64%,#e05cff)"></div>
  <div class="fll-dot" style="left:55px;top:826px;background:#2ad4ff;color:#2ad4ff"></div>
  <div class="fll-dot" style="left:275px;top:826px;background:#2affa0;color:#2affa0"></div>
  <div class="fll-dot" style="left:521px;top:826px;background:#ffc53d;color:#ffc53d"></div>
  <div class="fll-dot" style="left:783px;top:826px;background:#e05cff;color:#e05cff"></div>
  <div class="ab" style="left:54px;top:854px;font-size:22px;color:#e6efff">0</div>
  <div class="ab" style="left:256px;top:854px;font-size:22px;color:#e6efff">1500</div>
  <div class="ab" style="left:504px;top:854px;font-size:22px;color:#e6efff">1535</div>
  <div class="ab" style="left:742px;top:854px;font-size:22px;color:#e6efff">65535</div>
</div>

<div class="step">
  <div class="fll-pan b" style="left:846px;width:800px"></div>
  {img("rep/frame_llc_laybig.png", "left:883px;top:438px;width:79px", "ab")}
  <div class="ab fll-os" style="left:988px;top:443px;font-size:54px;line-height:72px;font-weight:700;color:#2ad4ff">LLC <span style="color:#fff;font-size:40px;font-weight:500">— 3 байта</span></div>
  <div class="ab" style="left:888px;top:520px;width:720px;height:1px;background:rgba(42,212,255,.4)"></div>
  <div class="fll-tx" style="left:888px;top:530px;width:740px;font-size:26px;line-height:33px"><em>Logical Link Control</em> — управление логическим каналом.<br>
    Определяет службу, которая должна обработать данные.</div>
</div>
<div class="step">
  {_field(887, 236, "DSAP", "#2a9dff", "linear-gradient(180deg,#1a5fe0,#0d2c8a)", "DSAP — служба<br>назначения")}
  {_field(1128, 234, "SSAP", "#9b6bff", "linear-gradient(180deg,#5a2ad8,#2d1290)", "SSAP — служба<br>источника")}
  {_field(1367, 240, "Control", "#e05cff", "linear-gradient(180deg,#8a2ad8,#4d1290)", "Control — тип<br>LLC-сообщения")}
</div>
<div class="step">
  <div class="ab" style="left:942px;top:795px;width:610px;height:85px;border-radius:14px;border:2px solid rgba(42,212,255,.75);background:rgba(6,30,66,.8);
    box-shadow:0 0 12px rgba(42,212,255,.4);text-align:center">
    <div class="fll-os" style="font-size:29px;line-height:40px;color:#2ad4ff;margin-top:6px">LLC/SNAP: AA-AA-03</div>
    <div style="font-size:22px;line-height:30px;color:#fff;word-spacing:2px">DSAP 0xAA &nbsp;<span style="color:#2ad4ff">•</span>&nbsp; SSAP 0xAA &nbsp;<span style="color:#2ad4ff">•</span>&nbsp; Control 0x03</div></div>
</div>
"""
