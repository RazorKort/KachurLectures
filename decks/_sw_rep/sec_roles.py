# -*- coding: utf-8 -*-
"""Безопасность: управление на основе ролей + уровни привилегий 1–15 — вёрстка 1:1 (pptx 85)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 196

CSS = """<style>
.sr-card{position:absolute;top:210px;height:362px;border:3px solid var(--c);border-radius:14px;background:linear-gradient(180deg,var(--b1),var(--b2));
  box-shadow:0 0 24px var(--g),inset 0 0 30px var(--g)}
.sr-ib{position:absolute;top:240px;border:2px solid var(--c);border-radius:10px;background:rgba(0,0,0,.25);box-shadow:inset 0 0 14px var(--g)}
.sr-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:38px;line-height:1.08;color:#fff;letter-spacing:.01em}
.sr-tag{position:absolute;height:40px;border:2px solid var(--c);border-radius:6px;background:var(--tb);font-family:Oswald,sans-serif;font-weight:500;
  font-size:21px;line-height:36px;text-align:center;color:#fff;letter-spacing:.04em;box-sizing:border-box}
.sr-li{position:absolute;color:#fff;font-size:24px;line-height:1}
.sr-bar{position:absolute;top:672px;width:90px;height:38px;border-radius:2px;box-shadow:0 0 10px currentColor}
.sr-end{position:absolute;top:656px;width:90px;height:70px;border:3px solid var(--c);border-radius:8px;background:#0a1e4a;box-shadow:0 0 16px var(--c);
  font-family:Oswald,sans-serif;font-weight:700;font-size:44px;line-height:64px;text-align:center;color:#fff}
.sr-cap{position:absolute;top:740px;width:180px;text-align:center;font-family:Oswald,sans-serif;font-weight:500;font-size:20px;line-height:1.1;color:#fff}
.sr-run{position:absolute;top:668px;width:30px;height:46px;border-radius:4px;background:rgba(255,255,255,.55);filter:blur(6px);animation:srrun 4s ease-in-out infinite}
@keyframes srrun{from{transform:translateX(0);opacity:0}10%{opacity:1}90%{opacity:1}to{transform:translateX(1240px);opacity:0}}
.sr-ft{position:absolute;top:802px;height:86px;border:2px solid var(--c);border-radius:8px;background:var(--b);box-shadow:0 0 16px var(--g)}
.sr-ft span{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:22px;line-height:1.28;color:#fff;letter-spacing:.03em}
</style>"""

BL = "--c:#2ad4ff;--g:rgba(42,212,255,.4);--b1:rgba(10,58,120,.85);--b2:rgba(6,26,70,.92);--tb:rgba(10,60,110,.8)"
VI = "--c:#9b6bff;--g:rgba(155,107,255,.45);--b1:rgba(60,26,150,.88);--b2:rgba(30,12,90,.92);--tb:rgba(70,30,160,.8)"
MG = "--c:#ff5cd8;--g:rgba(255,92,216,.4);--b1:rgba(110,20,110,.86);--b2:rgba(60,10,70,.92);--tb:rgba(130,20,110,.8)"


def lst(x, y0, items, dy=52):
    out = []
    for i, (ok, t) in enumerate(items):
        out.append(img("rep/sec_roles_%s.png" % ("ok" if ok else "no"), f"left:{x}px;top:{y0+i*dy-22}px;width:51px", "ab")
                   + f'<div class="sr-li" style="left:{x+73}px;top:{y0+i*dy-12}px">{t}</div>')
    return "".join(out)


COLS = ["#19c8ff", "#14b4ff", "#169cff", "#1a84ff", "#1f6cff", "#3a5cff", "#4c4cff", "#5e40ff", "#7438ff", "#8a30f8", "#a42cf0", "#c42ae4", "#e22ad4"]


def _bars():
    return "".join(f'<div class="sr-bar" style="left:{203+i*98.2:.0f}px;background:linear-gradient(180deg,{c},{c}cc);color:{c};transition-delay:{i*50}ms"></div>'
                   for i, c in enumerate(COLS))


HTML = CSS + f"""
<div class="step">
<div class="sr-card" style="{BL};left:42px;width:526px"></div>
<div class="sr-ib" style="{BL};left:66px;width:122px;height:124px"></div>
{img("rep/sec_roles_u.png", "left:88px;top:260px;width:79px", "ab")}
<div class="sr-h" style="left:212px;top:244px">ПОЛЬЗОВАТЕЛЬ</div>
<div class="sr-tag" style="{BL};left:212px;top:302px;width:338px;color:#7fe6ff">НИЗКИЙ УРОВЕНЬ ДОСТУПА</div>
{lst(93, 416, [(1, "Просмотр IP-адреса"), (1, "Проверка связи: ping"), (0, "Изменение конфигурации")], 51)}
</div>
<div class="step">
<div class="sr-card" style="{VI};left:586px;width:500px"></div>
<div class="sr-ib" style="{VI};left:612px;width:126px;height:128px"></div>
{img("rep/sec_roles_a.png", "left:630px;top:253px;width:92px", "ab")}
<div class="sr-h" style="left:762px;top:228px">МЛАДШИЙ<br>АДМИНИСТРАТОР</div>
<div class="sr-tag" style="{VI};left:762px;top:314px;width:300px;height:36px;line-height:32px;font-size:19px">ТЕХПОДДЕРЖКА 1-Й ЛИНИИ</div>
<div class="sr-tag" style="{VI};left:762px;top:356px;width:300px;height:36px;line-height:32px;font-size:19px">ОГРАНИЧЕННЫЙ ДОСТУП</div>
{lst(632, 423, [(1, "Просмотр интерфейсов"), (1, "Просмотр части конфигурации"), (0, "Изменение конфигурации")], 51)}
</div>
<div class="step">
<div class="sr-card" style="{MG};left:1104px;width:524px"></div>
<div class="sr-ib" style="{MG};left:1130px;width:134px;height:132px"></div>
{img("rep/sec_roles_k.png", "left:1148px;top:258px;width:99px", "ab")}
<div class="sr-h" style="left:1288px;top:244px">СУПЕРАДМИН</div>
<div class="sr-tag" style="{MG};left:1288px;top:302px;width:314px;text-align:left;padding-left:24px">ПОЛНЫЙ ДОСТУП</div>
{lst(1170, 420, [(1, "Просмотр всей конфигурации"), (1, "Изменение всех параметров"), (1, "Управление пользователями")], 54)}
</div>

<div class="step">
<div class="ab" style="left:180px;top:620px;width:306px;height:2px;background:linear-gradient(90deg,transparent,#2ad4ff)"></div>
<div class="ab" style="left:1186px;top:620px;width:350px;height:2px;background:linear-gradient(90deg,#9b6bff,transparent)"></div>
<div class="ab" style="left:0;top:596px;width:1672px;text-align:center;font-family:Oswald,sans-serif;font-weight:700;font-size:44px;line-height:52px;color:#fff;letter-spacing:.02em">
УРОВНИ ПРИВИЛЕГИЙ <span style="color:#2ad4ff">ELTEX</span></div>
</div>
<div class="step">
<div class="sr-end" style="--c:#2ad4ff;left:100px">1</div>
{_bars()}
<div class="sr-run" style="left:206px"></div>
<div class="sr-end" style="--c:#ff5cd8;left:1478px;background:#3a0a40">15</div>
<div class="sr-cap" style="left:56px">МИНИМАЛЬНЫЙ<br>ДОСТУП</div>
<div class="sr-cap" style="left:1436px">ПОЛНЫЙ<br>ДОСТУП</div>
<div class="ab" style="left:262px;top:749px;width:308px;height:2px;background:#2ad4ff"></div>
<div class="ab" style="left:256px;top:742px;border:8px solid transparent;border-right:12px solid #2ad4ff;border-left:0"></div>
<div class="ab" style="left:590px;top:738px;font-size:22px;color:#e6f1ff">Чем выше уровень, тем больше разрешений</div>
<div class="ab" style="left:1090px;top:749px;width:316px;height:2px;background:#ff5cd8"></div>
<div class="ab" style="left:1404px;top:742px;border:8px solid transparent;border-left:12px solid #ff5cd8;border-right:0"></div>
</div>

<div class="step">
<div class="sr-ft" style="--c:#2ad4ff;--g:rgba(42,212,255,.4);--b:rgba(6,28,70,.88);left:62px;width:756px"><span style="left:132px;top:16px">РОЛИ И ПРАВА ОПРЕДЕЛЯЮТСЯ<br>ПОЛИТИКОЙ БЕЗОПАСНОСТИ ОРГАНИЗАЦИИ</span></div>
{img("rep/sec_roles_sh.png", "left:103px;top:813px;width:57px", "ab")}
</div>
<div class="step">
<div class="sr-ft" style="--c:#ff5cd8;--g:rgba(255,92,216,.4);--b:rgba(50,10,60,.88);left:838px;width:772px"><span style="left:138px;top:30px">ИСПОЛЬЗУЙТЕ УНИКАЛЬНЫЕ БЕЗОПАСНЫЕ ПАРОЛИ</span></div>
{img("rep/sec_roles_warn.png", "left:876px;top:813px;width:68px", "ab")}
</div>
"""
