# -*- coding: utf-8 -*-
"""Подключение к коммутатору: консоль / SSH-Telnet / Web — вёрстка 1:1 (pptx 76)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 228

CSS = """<style>
.b2-pan{position:absolute;top:492px;height:246px;border:2px solid #2ad4ff;border-radius:10px;background:rgba(6,22,60,.86);
  box-shadow:0 0 18px rgba(42,212,255,.55),inset 0 0 26px rgba(42,212,255,.12);clip-path:polygon(0 0,100% 0,100% 88%,97% 100%,3% 100%,0 88%)}
.b2-h{position:absolute;top:506px;font-family:Oswald,sans-serif;font-weight:700;font-size:40px;line-height:1.1;color:#fff;letter-spacing:.01em}
.b2-h em{font-style:normal;color:#2ad4ff}
.b2-it{position:absolute;width:210px;height:68px;border:2px solid rgba(42,212,255,.6);border-radius:6px;background:rgba(8,30,76,.8);box-sizing:border-box}
.b2-it span{position:absolute;left:76px;top:0;height:64px;display:flex;align-items:center;color:#fff;font-size:18px;line-height:1.25}
.b2-side{position:absolute;color:#cfe6ff;font-family:Oswald,sans-serif;font-weight:300;font-size:17px;line-height:27.5px;letter-spacing:.04em}
.b2-ln{position:absolute;border:0 solid #2ad4ff;filter:drop-shadow(0 0 5px #2ad4ff)}
.b2-bar{position:absolute;border:2px solid #2ad4ff;background:rgba(6,22,60,.88);box-shadow:0 0 14px rgba(42,212,255,.45)}
</style>"""


def item(x, y, ico, ix, iy, iw, t):
    return (f'<div class="b2-it" style="left:{x}px;top:{y}px"><span>{t}</span></div>'
            + img(f"rep/base_setup2_{ico}.png", f"left:{ix}px;top:{iy}px;width:{iw}px", "ab"))


HTML = CSS + f"""
<div class="step">
<div class="b2-side" style="left:42px;top:315px">СЕТИ<br>ЗНАНИЯ<br>ПРАКТИКА<br>РЕЗУЛЬТАТ</div>
<div class="ab" style="left:42px;top:431px;width:44px;height:3px;background:#2ad4ff"></div>
<div class="b2-side" style="left:1491px;top:330px">СТАБИЛЬНОСТЬ<br>МАСШТАБИРУЕМОСТЬ<br>БЕЗОПАСНОСТЬ</div>
<div class="ab" style="left:1491px;top:421px;width:44px;height:3px;background:#2ad4ff"></div>
{img("rep/base_setup2_sw.png", "left:280px;top:232px;width:1114px", "ab")}
</div>
<div class="step">
<svg class="ab" style="left:0;top:0;width:1672px;height:941px" viewBox="0 0 1672 941">
 <g fill="none" stroke="#2ad4ff" stroke-width="3" style="filter:drop-shadow(0 0 5px #2ad4ff)">
  <path d="M432 452 V472 H236 V490"/><path d="M760 424 V478 H700 V490"/><path d="M1240 452 V478 H1420 V490"/>
 </g>
 <circle r="5" fill="#fff"><animateMotion dur="1.8s" repeatCount="indefinite" path="M760 424 V478 H700 V490"/></circle>
</svg></div>

<div class="step">
<div class="b2-pan" style="left:34px;width:528px"></div>
<div class="b2-h" style="left:72px">КОНСОЛЬНЫЙ ПОРТ</div>
{img("rep/base_setup2_cab.png", "left:40px;top:572px;width:176px", "ab")}
{img("rep/base_setup2_cport.png", "left:210px;top:618px;width:90px", "ab")}
{item(328, 567, "t1", 338, 576, 56, "Локальное<br>подключение")}
{item(328, 647, "g1", 342, 652, 52, "Эмулятор<br>терминала")}
</div>

<div class="step">
<div class="b2-pan" style="left:580px;width:512px"></div>
<div class="b2-h" style="left:622px"><em>SSH</em> или <em>TELNET</em></div>
{img("rep/base_setup2_ssh.png", "left:622px;top:582px;width:196px", "ab")}
{item(851, 567, "n2", 862, 576, 54, "Удалённое<br>подключение")}
{item(851, 647, "g2", 862, 656, 52, "Эмулятор<br>терминала")}
</div>

<div class="step">
<div class="b2-pan" style="left:1110px;width:528px"></div>
<div class="b2-h" style="left:1148px"><em>WEB</em>-ИНТЕРФЕЙС</div>
{img("rep/base_setup2_web.png", "left:1152px;top:578px;width:190px", "ab")}
{item(1385, 567, "n3", 1396, 576, 54, "Удалённое<br>подключение")}
{item(1385, 647, "g3", 1396, 656, 52, "Веб-браузер")}
</div>

<div class="step">
<div class="b2-bar" style="left:216px;top:756px;width:1238px;height:66px;clip-path:polygon(2% 0,98% 0,100% 50%,98% 100%,2% 100%,0 50%)"></div>
{img("rep/base_setup2_lap.png", "left:320px;top:763px;width:74px", "ab")}
<div class="ab" style="left:420px;top:774px;font-size:24px;color:#fff;white-space:nowrap"><b class="os" style="font-family:Oswald,sans-serif;font-weight:500;color:#2ad4ff">WINDOWS:</b>&nbsp; PuTTY &nbsp;•&nbsp; HyperTerminal &nbsp;•&nbsp; Tera Term</div>
<div class="ab" style="left:1007px;top:768px;width:2px;height:42px;background:rgba(42,212,255,.6)"></div>
{img("rep/base_setup2_tux.png", "left:1056px;top:760px;width:54px", "ab")}
<div class="ab" style="left:1142px;top:774px;font-size:24px;color:#fff;white-space:nowrap"><b style="font-family:Oswald,sans-serif;font-weight:500;color:#2ad4ff">LINUX:</b>&nbsp; Minicom</div>
</div>

<div class="step">
<div class="b2-bar" style="left:184px;top:840px;width:1304px;height:70px;clip-path:polygon(3% 0,97% 0,100% 50%,97% 100%,3% 100%,0 50%)"></div>
<div class="ab" style="left:184px;top:854px;width:1304px;text-align:center;font-family:Oswald,sans-serif;font-weight:700;font-size:31px;color:#fff">
<span style="color:#2ad4ff">ТРИ СПОСОБА ДОСТУПА:</span>&nbsp; КОНСОЛЬ &nbsp;•&nbsp; КОМАНДНАЯ СТРОКА &nbsp;•&nbsp; БРАУЗЕР</div>
</div>
"""
