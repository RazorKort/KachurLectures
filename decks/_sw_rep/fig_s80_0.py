# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _figkit_s65 import CSS  # noqa
"""Рис. 2.6.1.3.2 — окно входа Web-интерфейса, сверстано формой (поля печатаются, кнопка подсвечивается)."""
W, H, TOP = 1008, 712, 0
CSS2 = """<style>
.s80-pane{position:absolute;left:0;top:40px;width:1008px;height:615px;background:rgba(6,20,55,.55);border:1px solid rgba(42,212,255,.25);border-radius:6px}
.s80-side{position:absolute;left:150px;top:110px;width:131px;height:470px;background:#121a2e;border-right:12px solid #46506a;box-shadow:0 0 18px rgba(42,212,255,.25)}
.s80-head{position:absolute;left:305px;top:110px;width:550px;height:70px;background:linear-gradient(180deg,rgba(60,80,130,.6),rgba(20,35,80,.6));
  border-bottom:1px solid rgba(42,212,255,.4);color:#fff;font:700 28px/70px 'Golos Text',sans-serif;padding-left:15px;box-sizing:border-box}
.s80-lb{position:absolute;left:325px;color:#cfe0ff;font:400 28px/1 'Golos Text',sans-serif}
.s80-in{position:absolute;left:325px;width:415px;height:46px;box-sizing:border-box;border:2px solid #4b6aa8;border-radius:3px;background:#0b1636;
  color:#fff;font:400 28px/42px 'Golos Text',sans-serif;padding-left:10px;white-space:nowrap;overflow:hidden}
.s80-in.s80-f{border:3px solid #2ad4ff;box-shadow:0 0 14px rgba(42,212,255,.7)}
.s80-ty{display:inline-block;overflow:hidden;vertical-align:top}
.step.vis .s80-ty{animation:s80-type 1s steps(6,end) both}
@keyframes s80-type{from{width:0}to{width:var(--w)}}
.s80-cur{display:inline-block;width:2px;height:30px;background:#2ad4ff;vertical-align:middle;animation:s80-cur 1s steps(1) infinite}
@keyframes s80-cur{50%{opacity:0}}
.s80-sel::after{content:"";position:absolute;right:14px;top:9px;width:11px;height:11px;border-right:3px solid #cfe0ff;border-bottom:3px solid #cfe0ff;transform:rotate(45deg)}
.s80-btn{position:absolute;left:680px;top:493px;width:165px;height:48px;box-sizing:border-box;border:2px solid #9dfc5a;border-radius:3px;
  background:rgba(157,252,90,.12);color:#fff;font:400 28px/44px 'Golos Text',sans-serif;text-align:center}
.step.vis .s80-btn{animation:s80-press 1.8s ease-in-out .3s infinite}
@keyframes s80-press{0%,100%{box-shadow:0 0 6px rgba(157,252,90,.4)}50%{box-shadow:0 0 22px rgba(157,252,90,.95);background:rgba(157,252,90,.3)}}
</style>"""

# логотип: серые «молекулы» (узлы со связками) и голубой треугольник, как на рисунке
_PAIRS = [((195, 128), (180, 160)), ((243, 128), (228, 160)), ((195, 192), (172, 222)), ((195, 255), (172, 285)),
          ((220, 222), (243, 255)), ((220, 285), (243, 255)), ((180, 160), (195, 192))]
_logo = "".join('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#8a93a8" stroke-width="12" stroke-linecap="round"/>' % (a + b) for a, b in _PAIRS)
_logo += "".join('<circle cx="%d" cy="%d" r="11" fill="#9aa3b8"/>' % p for pr in _PAIRS for p in pr)
_logo += ('<g stroke="#2ad4ff" stroke-width="7" fill="#2ad4ff"><line x1="245" y1="180" x2="228" y2="215"/><line x1="228" y1="215" x2="268" y2="215"/>'
          '<line x1="268" y1="215" x2="245" y2="180"/><circle cx="245" cy="180" r="12"/><circle cx="228" cy="215" r="12"/><circle cx="268" cy="215" r="12"/></g>')

HTML = (CSS + CSS2 + '<div class="s80-pane"></div><div class="s80-side"></div>'
        + '<svg class="fgk-l" width="1008" height="712" style="filter:drop-shadow(0 0 5px rgba(42,212,255,.5))">%s</svg>' % _logo
        + '<div class="s80-head">Auth</div>'
        + '<div class="ab step"><div class="s80-lb" style="top:203px">Username</div>'
        + '<div class="s80-in" style="top:233px"><span class="s80-ty" style="--w:80px;width:80px">admin</span></div></div>'
        + '<div class="ab step"><div class="s80-lb" style="top:305px">Password</div>'
        + '<div class="s80-in s80-f" style="top:336px"><span class="s80-ty" style="--w:84px;width:84px;letter-spacing:1px">••••••</span>'
          '<span class="s80-cur"></span></div></div>'
        + '<div class="ab step"><div class="s80-lb" style="top:405px">Language</div>'
        + '<div class="s80-in s80-sel" style="top:438px;width:408px;height:40px;line-height:36px">English</div></div>'
        + '<div class="ab step"><div class="s80-btn">Sign in</div></div>'
        + '<div class="fgk-cap" style="top:675px;font-size:20px">Рисунок 2.6.1.3.2 – Внешний вид окна входа Web-интерфейса⁴</div>')
