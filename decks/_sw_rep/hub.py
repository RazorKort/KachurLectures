# -*- coding: utf-8 -*-
"""HUB — концентратор: вёрстка 1:1 инфографики (pptx 11)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 40   # большой заголовок слева пустой; справа плашка-определение остаётся

CSS = """<style>
.hub-pan{position:absolute;border-radius:10px;border:2px solid #2ad4ff;background:linear-gradient(180deg,rgba(10,50,110,.78),rgba(6,24,64,.86));
  box-shadow:0 0 14px rgba(42,212,255,.55),inset 0 0 22px rgba(42,212,255,.16)}
.hub-pan.v{border-color:#b06bff;background:linear-gradient(180deg,rgba(60,24,130,.8),rgba(30,12,80,.88));box-shadow:0 0 14px rgba(176,107,255,.55),inset 0 0 22px rgba(176,107,255,.18)}
.hub-pan.r{border-color:#ff4d8a;background:linear-gradient(180deg,rgba(90,14,60,.78),rgba(40,8,40,.88));box-shadow:0 0 14px rgba(255,77,138,.55),inset 0 0 22px rgba(255,77,138,.18)}
.hub-num{position:absolute;width:60px;height:62px;border-radius:8px;border:2px solid #2ad4ff;background:rgba(6,30,70,.9);box-shadow:0 0 12px rgba(42,212,255,.6);
  display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:700;font-size:44px;color:#fff}
.hub-num.v{border-color:#e05cff;box-shadow:0 0 12px rgba(224,92,255,.7)}
.hub-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:28px;letter-spacing:1px;color:#2ad4ff;line-height:1}
.hub-t{position:absolute;font-size:20px;line-height:1.25;color:#dbe8ff;white-space:nowrap}
.hub-tag{position:absolute;height:34px;border-radius:5px;border:2px solid #2ad4ff;background:rgba(6,30,80,.9);box-shadow:0 0 10px rgba(42,212,255,.6);
  display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:500;font-size:21px;color:#fff}
.hub-tag.m{border-color:#e05cff;box-shadow:0 0 10px rgba(224,92,255,.7)}
.hub-ln{position:absolute;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff}
.hub-ln.m{background:#ff5cf0;box-shadow:0 0 8px #ff5cf0}
.hub-pc{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:22px;color:#fff;width:80px;text-align:center}
.hub-pulse{position:absolute;width:12px;height:12px;border-radius:50%;background:#fff;box-shadow:0 0 12px 4px #2ad4ff;animation:hubRun 2.4s linear infinite}
@keyframes hubRun{0%{transform:translateX(0);opacity:0}8%{opacity:1}92%{opacity:1}100%{transform:translateX(660px);opacity:0}}
.hub-f{-webkit-mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent),linear-gradient(180deg,transparent,#000 6%,#000 94%,transparent);-webkit-mask-composite:source-in;mask-composite:intersect}
.hub-blink{animation:hubBlink 1.2s ease-in-out infinite}
@keyframes hubBlink{50%{opacity:.35}}
</style>"""

COPIES = [(652, 734), (764, 845), (875, 956)]
DROPS = [622, 716, 811, 907, 1002, 1097, 1191]


def _signal():
    out = ['<div class="hub-tag m" style="left:435px;top:239px;width:187px">Входящий сигнал</div>']
    for x0, x1 in COPIES:
        out.append('<div class="hub-tag" style="left:%dpx;top:243px;width:%dpx">Копия</div>' % (x0, x1 - x0))
    out.append('<div class="hub-ln m" style="left:527px;top:273px;width:4px;height:58px"></div>')
    out.append('<div class="hub-ln" style="left:531px;top:306px;width:662px;height:3px"></div>')
    for x0, x1 in COPIES:
        out.append('<div class="hub-ln" style="left:%dpx;top:277px;width:3px;height:30px"></div>' % ((x0 + x1) // 2))
    for x in DROPS:
        out.append('<div class="hub-ln" style="left:%dpx;top:306px;width:3px;height:14px"></div>' % x)
    out.append('<div class="hub-pulse" style="left:528px;top:302px"></div>')
    return "".join(out)


def _card(x, y, w, h, cls, num, head, text, ico, ico_st, tx=0):
    n = '<div class="hub-num %s" style="left:%dpx;top:%dpx">%s</div>' % (cls, x + 16, y + 20, num) if num else ""
    hx = x + (104 if num else 22)
    hc = "#e05cff" if cls == "v" else ("#ff4d8a" if cls == "r" else "#2ad4ff")
    return ('<div class="step"><div class="hub-pan %s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"></div>%s'
            '%s<div class="hub-h" style="left:%dpx;top:%dpx;color:%s">%s</div>'
            '<div class="hub-t" style="left:%dpx;top:%dpx">%s</div></div>'
            % (cls, x, y, w, h, n, img("rep/" + ico, ico_st, "ab hub-f"), hx, y + 26, hc, head, hx + tx, y + 64, text))


HTML = CSS + f"""
<div class="step"><div class="hub-pan" style="left:908px;top:45px;width:716px;height:112px"></div>
  {img("rep/hub_tree.png", "left:930px;top:62px;width:110px", "ab hub-f")}
  <div class="ab os" style="left:1070px;top:68px;font-size:29px;line-height:1.2;color:#9fe8ff">Концентратор (hub) объединяет<br>устройства в один общий сегмент сети.</div></div>

<div class="step"><svg class="ab" style="left:238px;top:176px" width="1192" height="52" viewBox="0 0 1192 52">
  <path d="M2 26 L26 2 H1166 L1190 26 L1166 50 H26 Z" fill="rgba(30,10,70,.75)" stroke="#d95cff" stroke-width="2.5" style="filter:drop-shadow(0 0 8px #d95cff)"/></svg>
  <div class="ab os" style="left:238px;top:181px;width:1192px;text-align:center;font-weight:700;font-size:30px;letter-spacing:1.5px;color:#fff">СИГНАЛ С ОДНОГО ПОРТА КОПИРУЕТСЯ ВО ВСЕ ОСТАЛЬНЫЕ ПОРТЫ</div></div>

<div class="step">{img("rep/hub_dev.png", "left:300px;top:284px;width:1072px", "ab hub-f")}
  <div class="hub-pc" style="left:386px;top:574px">ПК 1</div><div class="hub-pc" style="left:540px;top:574px">ПК 2</div>
  <div class="hub-pc" style="left:689px;top:574px">ПК 3</div><div class="hub-pc" style="left:844px;top:574px">ПК 4</div></div>

<div class="step">{_signal()}</div>

{_card(28, 618, 532, 130, "", "1", "ПОДКЛЮЧЕНИЕ", "Витая пара с разъёмами RJ-45", "hub_rj.png", "left:428px;top:632px;width:102px")}
{_card(575, 618, 523, 130, "v", "2", "ПОВТОРЕНИЕ", "Хаб повторяет<br>электрический сигнал", "hub_wave.png", "left:900px;top:650px;width:182px")}
{_card(1114, 618, 530, 130, "", "3", "ОБЩАЯ СРЕДА", "Все устройства разделяют<br>полосу пропускания", "hub_net.png", "left:1512px;top:632px;width:120px")}
{_card(28, 768, 532, 130, "", "", "РАНЬШЕ", "Коаксиальный кабель &nbsp;•<br>Т-разъём • терминаторы", "hub_coax.png", "left:282px;top:788px;width:266px")}
{_card(575, 768, 523, 130, "", "", "С КОНЦЕНТРАТОРОМ", "Отдельный кабель от компьютера<br>к порту хаба", "hub_star.png", "left:884px;top:785px;width:188px")}
{_card(1114, 768, 530, 130, "r", "", "", "", "hub_warn.png", "left:1130px;top:793px;width:84px")}
<div class="step"><div class="ab os hub-blink" style="left:1228px;top:792px;font-weight:700;font-size:22px;letter-spacing:-.3px;white-space:nowrap;color:#ff4d8a">ВСЕ ПОРТЫ ХАБА = ОДИН ДОМЕН КОЛЛИЗИЙ</div>
  <div class="hub-t" style="left:1228px;top:828px;font-size:21px">Хаб не анализирует MAC-адреса<br>и не выбирает получателя.</div></div>
"""
