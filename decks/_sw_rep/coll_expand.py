# -*- coding: utf-8 -*-
"""COLL_EXPAND — расширение коллизионного домена: вёрстка 1:1 инфографики (pptx 13)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 10   # большой заголовок слева не рисуем (его даёт head()), справа две плашки остаются

CSS = """<style>
.cex-pan{position:absolute;border-radius:10px;border:2px solid rgba(42,212,255,.7);background:linear-gradient(180deg,rgba(8,40,90,.72),rgba(4,18,50,.85));
  box-shadow:0 0 14px rgba(42,212,255,.4),inset 0 0 22px rgba(42,212,255,.12)}
.cex-pan.m{border-color:#e05cff;box-shadow:0 0 14px rgba(224,92,255,.5),inset 0 0 22px rgba(224,92,255,.14)}
.cex-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:30px;line-height:1;color:#fff}
.cex-h em{font-style:normal;color:#2ad4ff}
.cex-t{position:absolute;font-size:19.5px;line-height:1.27;color:#e6f1ff}
.cex-pc{position:absolute;height:34px;padding:0 8px;border-radius:5px;border:2px solid #2ad4ff;background:rgba(6,24,60,.95);box-shadow:0 0 8px rgba(42,212,255,.6);
  display:flex;align-items:center;font-family:Oswald,sans-serif;font-weight:700;font-size:24px;color:#fff}
.cex-pc.m{border-color:#e05cff;box-shadow:0 0 8px rgba(224,92,255,.7)}
.cex-f{-webkit-mask-image:linear-gradient(90deg,transparent,#000 3%,#000 97%,transparent),linear-gradient(180deg,transparent,#000 5%,#000 95%,transparent);-webkit-mask-composite:source-in;mask-composite:intersect}
.cex-boom{position:absolute;width:110px;height:110px;border-radius:50%;background:radial-gradient(circle,rgba(255,240,200,.9),rgba(255,130,40,.55) 40%,transparent 70%);
  animation:cexBoom 1s ease-in-out infinite}
@keyframes cexBoom{0%,100%{transform:scale(.6);opacity:.45}50%{transform:scale(1.3);opacity:1}}
.cex-grad{position:absolute;height:26px;border-radius:13px;background:linear-gradient(90deg,#2ad4ff,#5a7bff 45%,#c04cff 75%,#ff4d8a);box-shadow:0 0 16px rgba(120,120,255,.7)}
</style>"""

PCS = [("PC-A", 152, 283, ""), ("PC-B", 128, 425, ""), ("PC-C", 152, 575, ""),
       ("PC-D", 1447, 283, ""), ("PC-E", 1470, 425, ""), ("PC-F", 1447, 575, "m")]


def _pcs():
    return "".join('<div class="cex-pc %s" style="left:%dpx;top:%dpx">%s</div>' % (c, x, y, t) for t, x, y, c in PCS)


HTML = CSS + f"""
<div class="step">
  <div class="cex-pan" style="left:820px;top:16px;width:388px;height:212px"></div>
  <div class="cex-h" style="left:852px;top:34px">ЧТО <em>ЭТО</em>?</div>
  {img("rep/coll_expand_book.png", "left:832px;top:96px;width:90px", "ab cex-f")}
  <div class="cex-t" style="left:940px;top:90px">Коллизионный домен —<br>сегмент сети, где при<br>одновременной передаче<br>двух и более устройств<br>может возникнуть коллизия.</div>
</div>
<div class="step">
  <div class="cex-pan" style="left:1222px;top:16px;width:426px;height:212px"></div>
  <div class="cex-h" style="left:1246px;top:34px">ПОЧЕМУ ДОМЕН <em>РАСТЁТ</em>?</div>
  {img("rep/coll_expand_share.png", "left:1236px;top:98px;width:102px", "ab cex-f")}
  <div class="cex-t" style="left:1356px;top:90px">Концентратор повторяет<br>сигнал на всех портах.<br>Соединение H1 и H2<br>объединяет все ПК в одну<br>общую среду.</div>
</div>

<div class="step">
  <div class="ab" style="left:100px;top:250px;width:1472px;height:450px;border:3px dashed #2ad4ff;border-radius:34px;box-shadow:0 0 10px rgba(42,212,255,.35)"></div>
  {img("rep/coll_expand_scene.png", "left:112px;top:300px;width:1448px", "ab cex-f")}
  <svg class="ab" style="left:496px;top:246px" width="680" height="56" viewBox="0 0 680 56"><path d="M2 2 H678 L640 54 H40 Z" fill="rgba(6,24,60,.95)"
    stroke="#2ad4ff" stroke-width="3" stroke-dasharray="14 8"/></svg>
  <div class="ab os" style="left:496px;top:256px;width:680px;text-align:center;font-weight:700;font-size:30px;letter-spacing:1px;color:#2ad4ff">ЕДИНЫЙ КОЛЛИЗОННЫЙ ДОМЕН</div>
  {_pcs()}
</div>

<div class="step">
  <div class="cex-boom" style="left:780px;top:428px"></div>
  <svg class="ab" style="left:731px;top:358px" width="216" height="50" viewBox="0 0 216 50"><path d="M2 25 L20 2 H196 L214 25 L196 48 H20 Z" fill="rgba(40,22,4,.95)"
    stroke="#ffb02e" stroke-width="2.5" style="filter:drop-shadow(0 0 8px #ffb02e)"/></svg>
  <div class="ab os" style="left:731px;top:363px;width:216px;text-align:center;font-weight:700;font-size:29px;color:#ffc53d">КОЛЛИЗИЯ</div>
</div>

<div class="step">
  <div class="cex-pan" style="left:24px;top:718px;width:1624px;height:200px"></div>
  <div class="ab os" style="left:0;top:730px;width:1672px;text-align:center;font-weight:700;font-size:39px;line-height:1;color:#fff">БОЛЬШЕ УСТРОЙСТВ → БОЛЬШЕ КОЛЛИЗИЙ → <span style="color:#ff4d8a">НИЖЕ ЭФФЕКТИВНОСТЬ</span></div>
  <div class="ab" style="left:0;top:775px;width:1672px;text-align:center;font-size:22px;color:#e6f1ff">Устройствам сложнее согласовать момент начала передачи данных.</div>
</div>

<div class="step">
  <div class="cex-pan" style="left:48px;top:810px;width:368px;height:84px"></div>
  {img("rep/coll_expand_bars1.png", "left:62px;top:826px;width:70px", "ab cex-f")}
  <div class="ab os" style="left:148px;top:826px;font-weight:700;font-size:22px;line-height:1.2;color:#2ad4ff">МАЛЫЙ ДОМЕН —<br>ВЫШЕ ЭФФЕКТИВНОСТЬ</div>
  <div class="cex-grad" style="left:434px;top:841px;width:756px"></div>
  <svg class="ab" style="left:1176px;top:824px" width="60" height="60" viewBox="0 0 60 60"><path d="M0 6 L58 30 L0 54 Z" fill="#ff4d8a" style="filter:drop-shadow(0 0 8px #ff4d8a)"/></svg>
  <div class="cex-pan m" style="left:1256px;top:810px;width:366px;height:84px"></div>
  {img("rep/coll_expand_bars2.png", "left:1278px;top:826px;width:68px", "ab cex-f")}
  <div class="ab os" style="left:1368px;top:826px;font-weight:700;font-size:22px;line-height:1.2;color:#ff6fa8">БОЛЬШОЙ ДОМЕН —<br><span style="color:#fff">НИЖЕ ЭФФЕКТИВНОСТЬ</span></div>
</div>
"""
