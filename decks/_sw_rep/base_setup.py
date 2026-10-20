# -*- coding: utf-8 -*-
"""Базовая настройка коммутатора: 5 шагов — вёрстка 1:1 (pptx 75)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 205

CSS = """<style>
.bs-card{position:absolute;top:503px;width:310px;height:282px;border-radius:12px;border:3px solid var(--c);
  background:linear-gradient(180deg,var(--b1),var(--b2));box-shadow:0 0 22px var(--g),inset 0 0 26px var(--g)}
.bs-n{position:absolute;top:480px;width:86px;height:48px;border:3px solid var(--c);border-radius:8px;background:#071a44;
  font-family:Oswald,sans-serif;font-weight:700;font-size:32px;line-height:42px;text-align:center;color:#fff;box-shadow:0 0 14px var(--g)}
.bs-t{position:absolute;top:620px;width:310px;text-align:center;font-family:Oswald,sans-serif;font-weight:700;font-size:31px;color:#fff;letter-spacing:.01em}
.bs-hr{position:absolute;top:670px;height:2px;background:var(--c);opacity:.7}
.bs-d{position:absolute;width:310px;text-align:center;color:#e6f1ff;font-size:22px;line-height:1.3}
.bs-ln{position:absolute;border:0 solid #2ad4ff;filter:drop-shadow(0 0 5px #2ad4ff)}
.bs-dot{position:absolute;width:10px;height:10px;border-radius:50%;background:#bff3ff;box-shadow:0 0 10px #2ad4ff,0 0 3px #fff}
.bs-run{position:absolute;width:8px;height:8px;border-radius:50%;background:#fff;box-shadow:0 0 10px #2ad4ff;offset-rotate:0deg;animation:bsrun 2.2s linear infinite}
@keyframes bsrun{from{offset-distance:0%}to{offset-distance:100%}}
</style>"""

CARDS = [  # x, номер, иконка, заголовок, описание, цвет, фон1, фон2, сдвиг описания
    (30, "01", "i1", "ПОДКЛЮЧЕНИЕ", "Консольное<br>подключение и<br>параметры сеанса", "#2ad4ff", "rgba(10,60,120,.85)", "rgba(6,26,70,.92)", 686),
    (358, "02", "i2", "ИМЯ УСТРОЙСТВА", "Идентификация<br>коммутатора в сети", "#9b6bff", "rgba(60,30,140,.85)", "rgba(28,12,80,.92)", 696),
    (683, "03", "i3", "БАННЕР", "Предупреждение о<br>неавторизованном<br>доступе", "#e05cff", "rgba(110,20,120,.85)", "rgba(56,10,74,.92)", 686),
    (1004, "04", "i4", "IP-ПАРАМЕТРЫ", "IP-адрес &nbsp;•&nbsp; Маска &nbsp;•<br>Шлюз по умолчанию", "#2ad4ff", "rgba(10,70,120,.85)", "rgba(6,30,70,.92)", 696),
    (1330, "05", "i5", "ПОЛЬЗОВАТЕЛИ", "Разделение<br>полномочий и<br>защита конфигурации", "#2ad4ff", "rgba(10,60,130,.85)", "rgba(6,26,76,.92)", 686),
]
ICO = {"i1": (122, 545, 123), "i2": (470, 540, 82), "i3": (798, 540, 74), "i4": (1116, 540, 82), "i5": (1428, 546, 116)}


def _cards():
    out = []
    for i, (x, n, ic, t, d, c, b1, b2, dy) in enumerate(CARDS):
        st = f"--c:{c};--g:{c}66;--b1:{b1};--b2:{b2}"
        ix, iy, iw = ICO[ic]
        out.append(f'<div class="step" style="transition-delay:{i*90}ms">'
                   f'<div class="bs-card" style="{st};left:{x}px"></div>'
                   f'<div class="bs-n" style="{st};left:{x+112}px">{n}</div>'
                   + img(f"rep/base_setup_{ic}.png", f"left:{ix}px;top:{iy}px;width:{iw}px", "ab") +
                   f'<div class="bs-t" style="left:{x}px">{t}</div>'
                   f'<div class="bs-hr" style="--c:{c};left:{x+22}px;width:266px;background:{c}"></div>'
                   f'<div class="bs-d" style="left:{x}px;top:{dy}px">{d}</div></div>')
    return "".join(out)


HTML = CSS + f"""
<div class="step">{img("rep/base_setup_sw.png", "left:280px;top:215px;width:1106px", "ab")}</div>
<div class="step">
<svg class="ab" style="left:0;top:0;width:1672px;height:941px;overflow:visible" viewBox="0 0 1672 941">
 <g fill="none" stroke="#2ad4ff" stroke-width="3" style="filter:drop-shadow(0 0 5px #2ad4ff)">
  <path id="bsp1" d="M521 422 V442 H188 V480"/><path d="M521 442 H514 V480" stroke="#9b6bff"/>
  <path d="M836 422 V480" stroke="#e05cff"/>
  <path id="bsp2" d="M1150 422 V442 H1484 V480"/><path d="M1150 442 H1157 V480"/>
 </g>
 <g fill="#bff3ff"><circle cx="521" cy="422" r="5"/><circle cx="836" cy="422" r="5"/><circle cx="1150" cy="422" r="5"/>
  <circle cx="188" cy="474" r="4"/><circle cx="514" cy="474" r="4"/><circle cx="836" cy="474" r="4"/><circle cx="1157" cy="474" r="4"/><circle cx="1484" cy="474" r="4"/></g>
 <circle r="5" fill="#fff"><animateMotion dur="2.4s" repeatCount="indefinite" path="M521 422 V442 H188 V480"/></circle>
 <circle r="5" fill="#fff"><animateMotion dur="2.4s" repeatCount="indefinite" path="M1150 422 V442 H1484 V480"/></circle>
 <circle r="5" fill="#fff"><animateMotion dur="1.2s" repeatCount="indefinite" path="M836 422 V480"/></circle>
</svg></div>
{_cards()}
<div class="step">
<div class="ab" style="left:365px;top:818px;width:938px;height:66px;border:2px solid #2ad4ff;border-radius:8px;background:rgba(6,26,66,.88);
  box-shadow:0 0 16px rgba(42,212,255,.5);clip-path:polygon(2% 0,98% 0,100% 50%,98% 100%,2% 100%,0 50%)"></div>
<div class="ab" style="left:365px;top:832px;width:938px;text-align:center;font-family:Oswald,sans-serif;font-weight:700;font-size:28px;color:#fff">
<span style="color:#2ad4ff">РЕЗУЛЬТАТ:</span> БЕЗОПАСНОЕ УДАЛЁННОЕ АДМИНИСТРИРОВАНИЕ</div>
</div>
"""
