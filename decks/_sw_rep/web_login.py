# -*- coding: utf-8 -*-
"""Вход в web-интерфейс коммутатора — вёрстка 1:1 (pptx 80)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 196

CSS = """<style>
.wl-box{position:absolute;border:3px solid #2ad4ff;border-radius:12px;background:rgba(6,26,70,.82);box-shadow:0 0 20px rgba(42,212,255,.6),inset 0 0 24px rgba(42,212,255,.15)}
.wl-cap{position:absolute;height:46px;border:2px solid #2ad4ff;border-radius:8px;background:rgba(4,16,44,.9);box-shadow:0 0 12px rgba(42,212,255,.45);
  font-family:Oswald,sans-serif;font-weight:500;font-size:22px;line-height:42px;text-align:center;color:#fff}
.wl-lab{position:absolute;left:686px;color:#fff;font-size:19px}
.wl-in{position:absolute;left:686px;width:440px;height:38px;border:2px solid #2ad4ff;border-radius:4px;background:#eef4ff;box-sizing:border-box;
  padding-left:12px;font-size:23px;line-height:34px;color:#0a1630;font-weight:500}
.wl-ln{position:absolute;height:3px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff}
.wl-ln:before,.wl-ln:after{content:"";position:absolute;top:-5px;width:13px;height:13px;border-radius:50%;background:#bff3ff;box-shadow:0 0 10px #2ad4ff}
.wl-ln:before{left:-6px}.wl-ln:after{right:-6px}
.wl-pk{position:absolute;width:10px;height:10px;border-radius:50%;background:#fff;box-shadow:0 0 10px #2ad4ff;animation:wlfly 1.5s linear infinite}
@keyframes wlfly{from{transform:translateX(0)}to{transform:translateX(var(--d))}}
.wl-big{position:absolute;top:606px;height:166px;border:3px solid var(--c);border-radius:12px;background:var(--b);box-shadow:0 0 22px var(--g),inset 0 0 26px var(--g)}
.wl-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:38px;line-height:1;color:var(--c)}
.wl-tx{position:absolute;color:#fff;font-size:31px;line-height:1.3;font-weight:600}
.wl-st{position:absolute;top:802px;height:96px;border:2px solid #2ad4ff;border-radius:10px;background:rgba(6,24,64,.86);box-shadow:0 0 14px rgba(42,212,255,.45)}
.wl-c{position:absolute;top:812px;width:76px;height:76px;border:3px solid #2ad4ff;border-radius:50%;box-shadow:0 0 14px #2ad4ff,inset 0 0 10px rgba(42,212,255,.4);
  font-family:Oswald,sans-serif;font-weight:500;font-size:46px;line-height:70px;text-align:center;color:#2ad4ff}
.wl-s{position:absolute;color:#fff;font-size:23px;line-height:1.22}
.wl-gt{position:absolute;top:818px;font-family:Golos Text,sans-serif;font-weight:700;font-size:64px;line-height:64px;color:#2ad4ff;text-shadow:0 0 10px #2ad4ff}
.wl-btn{animation:wlpulse 2s ease-in-out infinite}
@keyframes wlpulse{50%{box-shadow:0 0 26px #2ad4ff}}
</style>"""

HTML = CSS + f"""
<div class="step">
<div class="wl-box" style="left:110px;top:318px;width:224px;height:168px"></div>
{img("rep/web_login_user.png", "left:150px;top:333px;width:130px", "ab")}
<div class="wl-cap" style="left:96px;top:500px;width:258px">ПОЛЬЗОВАТЕЛЬ</div>
<div class="wl-ln" style="left:334px;top:407px;width:140px"></div><div class="wl-pk" style="left:336px;top:403px;--d:130px"></div>
</div>
<div class="step">
<div class="wl-box" style="left:488px;top:198px;width:698px;height:394px;border-radius:14px"></div>
<div class="ab" style="left:502px;top:216px;width:142px;height:362px;background:#1b2230;border:1px solid #3a4a66"></div>
{img("rep/web_login_logo.png", "left:512px;top:272px;width:116px", "ab")}
<div class="ab" style="left:648px;top:216px;width:524px;height:50px;background:linear-gradient(180deg,#2a4372,#1c3058);border-bottom:1px solid #4a6aa0"></div>
<div class="ab" style="left:682px;top:228px;font-size:21px;color:#fff">Web-интерфейс коммутатора</div>
<div class="ab" style="left:1132px;top:228px;font-size:22px;color:#6a86b8">✕</div>
<div class="wl-lab" style="top:287px">Имя пользователя</div><div class="wl-in" style="top:314px">admin</div>
<div class="wl-lab" style="top:366px">Пароль</div><div class="wl-in" style="top:394px">admin</div>
<div class="wl-lab" style="top:446px">Язык</div><div class="wl-in" style="top:473px">English<span style="position:absolute;right:14px;font-size:18px">⌄</span></div>
<div class="ab wl-btn" style="left:912px;top:527px;width:226px;height:40px;border-radius:8px;background:linear-gradient(180deg,#1aa0ff,#0a5ad0);border:2px solid #7fd8ff;
  font-family:Oswald,sans-serif;font-weight:700;font-size:23px;line-height:36px;text-align:center;color:#fff">ВОЙТИ</div>
</div>
<div class="step">
<div class="wl-ln" style="left:1198px;top:407px;width:96px"></div><div class="wl-pk" style="left:1200px;top:403px;--d:88px"></div>
<div class="wl-box" style="left:1316px;top:320px;width:292px;height:166px"></div>
{img("rep/web_login_sw.png", "left:1322px;top:356px;width:280px", "ab")}
<div class="wl-cap" style="left:1306px;top:500px;width:308px">СЕТЕВОЙ КОММУТАТОР</div>
</div>

<div class="step">
<div class="wl-big" style="--c:#2ad4ff;--g:rgba(42,212,255,.4);--b:rgba(6,28,74,.86);left:50px;width:772px"></div>
<div class="ab" style="left:70px;top:622px;width:172px;height:134px;border-right:2px solid rgba(42,212,255,.4)"></div>
{img("rep/web_login_key.png", "left:98px;top:633px;width:130px", "ab")}
<div class="wl-h" style="--c:#2ad4ff;left:280px;top:636px">ПО УМОЛЧАНИЮ:</div>
<div class="wl-tx" style="left:280px;top:675px">имя пользователя — admin;<br>пароль — admin.</div>
</div>
<div class="step">
<div class="wl-big" style="--c:#c85cff;--g:rgba(200,92,255,.45);--b:rgba(56,16,96,.86);left:848px;width:774px"></div>
{img("rep/web_login_shield.png", "left:898px;top:626px;width:124px", "ab")}
<div class="wl-h" style="--c:#ee7cff;left:1062px;top:636px">ПРИ ПЕРВОМ ПОДКЛЮЧЕНИИ:</div>
<div class="wl-tx" style="left:1064px;top:676px">создайте другого пользователя<br>и задайте безопасный пароль.</div>
</div>

<div class="step">
<div class="wl-st" style="left:76px;width:438px"></div><div class="wl-c" style="left:88px">1</div>
{img("rep/web_login_s1.png", "left:193px;top:823px;width:84px", "ab")}
<div class="wl-s" style="left:296px;top:822px">1. Введите<br>&nbsp;&nbsp;&nbsp;&nbsp;admin / admin</div>
<div class="wl-gt" style="left:548px">›</div>
</div>
<div class="step">
<div class="wl-st" style="left:600px;width:436px"></div><div class="wl-c" style="left:614px">2</div>
{img("rep/web_login_s2.png", "left:723px;top:820px;width:69px", "ab")}
<div class="wl-s" style="left:814px;top:822px">2. Войдите<br>&nbsp;&nbsp;&nbsp;&nbsp;в систему</div>
<div class="wl-gt" style="left:1072px">›</div>
</div>
<div class="step">
<div class="wl-st" style="left:1124px;width:472px"></div><div class="wl-c" style="left:1138px">3</div>
{img("rep/web_login_s3.png", "left:1238px;top:818px;width:74px", "ab")}
<div class="wl-s" style="left:1338px;top:822px">3. Создайте<br><span style="font-size:20px">&nbsp;&nbsp;&nbsp;&nbsp;нового пользователя</span></div>
</div>
"""
