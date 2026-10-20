# -*- coding: utf-8 -*-
"""Консольное подключение и параметры терминала — вёрстка 1:1 (pptx 77)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 196

CSS = """<style>
.bc-lb{position:absolute;top:486px;height:54px;border:2px solid #2ad4ff;border-radius:8px;background:rgba(6,24,62,.88);box-shadow:0 0 14px rgba(42,212,255,.5);
  font-family:Oswald,sans-serif;font-weight:500;font-size:26px;color:#fff;display:flex;align-items:center;justify-content:center;
}
.bc-v{position:absolute;width:2px;background:#2ad4ff;box-shadow:0 0 6px #2ad4ff}
.bc-v:after{content:"";position:absolute;left:-4px;bottom:-5px;width:10px;height:10px;border-radius:50%;background:#bff3ff;box-shadow:0 0 8px #2ad4ff}
.bc-arr{position:absolute;height:8px;background:linear-gradient(90deg,rgba(42,212,255,.2),#2ad4ff);box-shadow:0 0 10px #2ad4ff}
.bc-arr:after{content:"";position:absolute;right:-18px;top:-12px;border:16px solid transparent;border-left:20px solid #2ad4ff;border-right:0}
.bc-flow{position:absolute;width:14px;height:14px;border-radius:50%;background:#fff;box-shadow:0 0 12px #2ad4ff;animation:bcfly 1.6s linear infinite}
@keyframes bcfly{from{transform:translateX(0);opacity:0}20%{opacity:1}to{transform:translateX(60px);opacity:0}}
.bc-card{position:absolute;top:644px;height:216px;border:2px solid var(--c);border-radius:8px;background:var(--b);box-shadow:0 0 14px var(--g)}
.bc-num{position:absolute;top:644px;width:62px;height:54px;background:var(--c2);border:2px solid var(--c);border-radius:8px 0 8px 0;
  font-family:Oswald,sans-serif;font-weight:700;font-size:34px;line-height:50px;text-align:center;color:#fff}
.bc-t{position:absolute;text-align:center;color:#fff;font-size:24px;line-height:1.24}
.bc-t b{font-weight:700}
</style>"""

B = "--c:#2ad4ff;--g:rgba(42,212,255,.45);--b:rgba(8,30,76,.85);--c2:#0b4fa0"
V = "--c:#9b6bff;--g:rgba(155,107,255,.55);--b:rgba(46,22,120,.85);--c2:#5a2fc8"

CARDS = [  # x, w, стиль, номер, иконка(x,y,w), текст, top текста
    (48, 246, B, "1", (128, 673, 99), "<b>COM-порт:</b><br>выбрать<br>соответствующий", 748),
    (308, 228, V, "2", (386, 673, 84), "<b>Скорость:<br><span style='font-size:28px'>115200 бод</span></b>", 756),
    (549, 274, B, "3", (660, 663, 60), "<b>Формат данных:</b><br>8 бит, 1 стоповый бит,<br>без контроля<br>чётности (8N1)", 736),
    (836, 228, V, "4", (923, 666, 71), "<b>Управление<br>потоком:</b><br>отключено", 748),
    (1077, 226, B, "5", (1163, 666, 79), "<b>Эмуляция<br>терминала:<br>VT100</b>", 748),
]


def _cards():
    out = []
    for i, (x, w, st, n, (ix, iy, iw), t, ty) in enumerate(CARDS):
        out.append(f'<div class="step" style="transition-delay:{i*80}ms"><div class="bc-card" style="{st};left:{x}px;width:{w}px"></div>'
                   f'<div class="bc-num" style="{st};left:{x}px">{n}</div>'
                   + img(f"rep/base_console_i{n}.png", f"left:{ix}px;top:{iy}px;width:{iw}px", "ab") +
                   f'<div class="bc-t" style="left:{x}px;width:{w}px;top:{ty}px">{t}</div></div>')
    return "".join(out)


HTML = CSS + f"""
<div class="step">{img("rep/base_console_lap.png", "left:0;top:203px;width:378px", "ab")}
<div class="bc-v" style="left:194px;top:480px;height:6px"></div>
<div class="bc-lb" style="left:52px;width:292px">Ноутбук</div></div>
<div class="step"><div class="bc-arr" style="left:366px;top:348px;width:56px"></div><div class="bc-flow" style="left:366px;top:345px"></div>
{img("rep/base_console_usb.png", "left:442px;top:312px;width:266px", "ab")}
<div class="bc-v" style="left:595px;top:442px;height:40px"></div>
<div class="bc-lb" style="left:472px;width:238px">USB–RS-232</div></div>
<div class="step"><div class="bc-arr" style="left:706px;top:376px;width:46px"></div><div class="bc-flow" style="left:706px;top:373px;animation-delay:.8s"></div>
{img("rep/base_console_sw.png", "left:772px;top:222px;width:900px", "ab")}
<div class="bc-v" style="left:955px;top:450px;height:32px"></div>
<div class="bc-lb" style="left:832px;width:286px">Консольный кабель</div>
<div class="bc-v" style="left:1352px;top:420px;height:62px"></div>
<div class="bc-lb" style="left:1171px;width:236px">CONSOLE (RJ-45)</div>
<div class="bc-v" style="left:1509px;top:440px;height:42px"></div>
<div class="bc-lb" style="left:1438px;width:196px">Коммутатор</div></div>

<div class="step">
<div class="ab" style="left:28px;top:572px;width:1616px;height:314px;border:2px solid #2ad4ff;border-radius:14px;background:rgba(6,20,56,.75);box-shadow:0 0 18px rgba(42,212,255,.45)"></div>
<div class="ab" style="left:60px;top:582px;font-family:Oswald,sans-serif;font-weight:700;font-size:38px;color:#fff;letter-spacing:.02em">ПАРАМЕТРЫ ТЕРМИНАЛА</div>
<div class="ab" style="left:626px;top:607px;width:990px;height:2px;background:#2ad4ff;box-shadow:0 0 6px #2ad4ff"></div>
</div>
{_cards()}
<div class="step">
<div class="ab" style="left:1322px;top:644px;width:2px;height:216px;border-left:2px dashed rgba(42,212,255,.6)"></div>
<div class="ab" style="left:1346px;top:668px;width:286px;height:156px;border:2px solid #2ad4ff;border-radius:10px;background:rgba(8,30,76,.85);box-shadow:0 0 14px rgba(42,212,255,.5)"></div>
{img("rep/base_console_bulb.png", "left:1363px;top:686px;width:59px", "ab")}
<div class="ab" style="left:1438px;top:692px;font-size:19px;line-height:1.38;color:#e6f1ff">Рекомендуется<br>устанавливать<br>скорость 115200 бод<br>вручную.</div>
</div>
"""
