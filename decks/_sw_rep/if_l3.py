# -*- coding: utf-8 -*-
"""Интерфейсы уровня L3: функции + конвейер L2→L3→ACL→таблица→L2 — вёрстка 1:1."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 170

CSS = """<style>
.il3-pan{position:absolute;border:2px solid #2ad4ff;border-radius:12px;background:rgba(6,20,56,.82);box-shadow:0 0 18px rgba(42,212,255,.5),inset 0 0 26px rgba(42,212,255,.1)}
.il3-it{position:absolute;left:62px;display:flex;align-items:center;gap:28px;font-family:'Golos Text',sans-serif;font-size:25px;line-height:1.3;color:#fff}
.il3-pb{position:absolute;top:534px;height:108px;border:3px solid #2ad4ff;border-radius:10px;background:rgba(6,30,80,.92);box-shadow:0 0 16px rgba(42,212,255,.75);
  display:flex;flex-direction:column;align-items:center;justify-content:space-between;padding:6px 0 10px;font-family:Oswald,sans-serif;font-weight:500;font-size:24px;color:#fff;line-height:1}
.il3-pb.v{border-color:#9b6bff;background:rgba(40,15,90,.92);box-shadow:0 0 16px rgba(155,107,255,.8)}
.il3-pb.y{border-color:#ffc53d;background:rgba(70,50,10,.85);box-shadow:0 0 16px rgba(255,197,61,.7);font-size:14px;line-height:1.1;text-align:center}
.il3-ar{position:absolute;top:572px;color:#2ad4ff;font-size:34px;line-height:1;text-shadow:0 0 8px #2ad4ff}
.il3-pb.go{animation:il3go 3.5s infinite}
@keyframes il3go{0%,100%{filter:none}10%{filter:brightness(1.6)}}
</style>"""

ITEMS = ["Декапсуляция кадра до уровня L3", "Фильтрация и отбрасывание<br>трафика посредством ACL", "Маршрутизация по таблице<br>маршрутизации",
         "Получение и обработка<br>управляющего трафика", "Инкапсуляция трафика L3<br>для передачи на уровень L2"]
YS = [268, 364, 462, 564, 666]

PIPE = [("L2", "if_l3_p1.png", 876, 108, "", 64), ("L3", "if_l3_p2.png", 1032, 112, "", 58), ("ACL", "if_l3_p3.png", 1182, 114, "v", 66),
        ("ТАБЛИЦА<br>МАРШРУТИЗАЦИИ", "if_l3_p4.png", 1334, 150, "y", 76), ("L2", "if_l3_p5.png", 1524, 98, "", 66)]


def _items():
    return "".join('<div class="il3-it step" style="top:%dpx">%s<div>%s</div></div>' % (y, img("rep/if_l3_i%d.png" % (i + 1), "width:100px"), t)
                   for i, (t, y) in enumerate(zip(ITEMS, YS)))


def _pipe():
    out = []
    for i, (t, ic, x, w, c, iw) in enumerate(PIPE):
        out.append('<div class="il3-pb go %s" style="left:%dpx;width:%dpx;animation-delay:%dms"><span>%s</span>%s</div>'
                   % (c, x, w, i * 500, t, img("rep/" + ic, "width:%dpx" % iw)))
        if i < 4:
            out.append('<div class="il3-ar" style="left:%dpx">➜</div>' % (x + w + 8))
    return '<div class="step">%s</div>' % "".join(out)


HTML = CSS + f"""
<div class="step">{img("rep/if_l3_scene.png", "left:745px;top:170px;width:927px", "ab")}</div>

<div class="step">
  <div class="il3-pan" style="left:34px;top:185px;width:710px;height:704px"></div>
  <div class="ab" style="left:62px;top:200px;font-family:Oswald,sans-serif;font-weight:700;font-size:42px;color:#2ad4ff;letter-spacing:.5px">ФУНКЦИИ ИНТЕРФЕЙСОВ L3</div>
</div>
{_items()}

{_pipe()}

<div class="step">
  <div class="ab" style="left:62px;top:776px;width:654px;height:2px;background:rgba(42,212,255,.6)"></div>
  <div class="ab" style="left:72px;top:792px;font-family:Oswald,sans-serif;font-weight:500;font-size:29px;line-height:1.35;color:#fff">
    <span style="color:#2ad4ff">L3-ИНТЕРФЕЙС</span> АНАЛИЗИРУЕТ <span style="color:#2ad4ff">IP-ЗАГОЛОВОК</span><br>И <span style="color:#2ad4ff">ВЫБИРАЕТ ДАЛЬНЕЙШИЙ ПУТЬ ПАКЕТА</span></div>
</div>
"""
