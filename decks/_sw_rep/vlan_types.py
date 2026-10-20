# -*- coding: utf-8 -*-
"""Типы VLAN — три классификации: по методу создания, назначения трафика, виду трафика."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 100

CSS = """<style>
.vt-col{position:absolute;top:206px;height:622px;border-radius:16px;border:3px solid var(--c);background:rgba(6,24,70,.5);box-shadow:0 0 22px var(--g),inset 0 0 30px var(--g)}
.vt-hd{position:absolute;top:212px;height:86px;border-bottom:2px solid var(--c);display:flex;align-items:center;justify-content:center;text-align:center;
  font-family:Oswald,sans-serif;font-weight:700;font-size:34px;line-height:1.02;color:#fff;letter-spacing:.5px}
.vt-it{position:absolute;border-radius:12px;border:2px solid var(--c);background:rgba(10,30,80,.6);box-shadow:0 0 10px var(--g)}
.vt-h{position:absolute;font-family:Oswald,sans-serif;font-weight:600;font-size:27px;color:#fff;line-height:1}
.vt-tx{position:absolute;font-size:18px;line-height:1.18;color:#dfe9ff}
</style>"""

COLS = [  # x, w, цвет, свечение
    (37, 518, "#2ad4ff", "rgba(42,212,255,.4)"),
    (586, 502, "#c05cff", "rgba(192,92,255,.45)"),
    (1117, 520, "#2ad4ff", "rgba(42,212,255,.4)"),
]
ITEMS = [  # колонка, иконка-кроп(x,y,x1,y1), бокс(top,h), заголовок, текст
    (0, (55, 322, 197, 463), (320, 142), "VLAN ПО УМОЛЧАНИЮ", "VLAN 1; все порты<br>принадлежат ей при первом<br>включении"),
    (0, (55, 484, 197, 625), (484, 140), "СТАТИЧЕСКИЕ", "Создаются администратором<br>вручную"),
    (0, (55, 644, 197, 787), (644, 142), "ДИНАМИЧЕСКИЕ", "Создаются автоматически<br>по протоколам GVRP или VTP"),
    (1, (602, 321, 728, 426), (320, 106), "НА ОСНОВЕ ПОРТОВ", "VLAN ID определяется<br>настройкой порта"),
    (1, (602, 442, 728, 550), (441, 108), "НА ОСНОВЕ MAC-АДРЕСОВ", "VLAN выбирается<br>по MAC-адресу устройства"),
    (1, (602, 566, 728, 685), (565, 120), "НА ОСНОВЕ ПРОТОКОЛОВ", "Назначение выполняется<br>протоколами, например<br>LLDP-MED"),
    (1, (602, 699, 728, 810), (699, 112), "НА ОСНОВЕ ПОЛИТИК", "VLAN назначается по условиям<br>политик и ACL"),
    (2, (1131, 321, 1264, 433), (320, 112), "VLAN ДАННЫХ", "Обычный пользовательский<br>трафик: файлы, FTP"),
    (2, (1131, 446, 1264, 558), (446, 112), "VOICE VLAN", "Голосовой трафик<br>с высоким приоритетом"),
    (2, (1131, 572, 1264, 685), (572, 112), "MULTICAST VLAN", "Многоадресный трафик,<br>например multicast-TV"),
    (2, (1131, 699, 1264, 811), (699, 112), "VLAN УПРАВЛЕНИЯ", "SSH и диагностика сетевых<br>устройств; не использовать<br>VLAN 1"),
]
HEADS = ['ПО МЕТОДУ <span style="color:#2ad4ff">СОЗДАНИЯ</span>',
         'ПО МЕТОДУ<br><span style="color:#ff5cd6">НАЗНАЧЕНИЯ ТРАФИКА</span>',
         'ПО ВИДУ <span style="color:#2ad4ff">ТРАФИКА</span>']


def _col(k):
    x, w, c, g = COLS[k]
    out = ['<div class="step" style="--c:%s;--g:%s"><div class="vt-col" style="left:%dpx;width:%dpx"></div>'
           '<div class="vt-hd" style="left:%dpx;width:%dpx"><div>%s</div></div>' % (c, g, x, w, x, w, HEADS[k])]
    n = 0
    for col, (ix, iy, ix1, iy1), (t, h), hd, tx in ITEMS:
        if col != k:
            continue
        ty = t + (12 if h < 125 else 20)
        out.append('<div style="transition-delay:%dms"><div class="vt-it" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"></div>%s'
                   '<div class="vt-h" style="left:%dpx;top:%dpx">%s</div><div class="vt-tx" style="left:%dpx;top:%dpx">%s</div></div>'
                   % (n * 90, ix, t, x + w - 18 - ix, h, img("rep/vlan_types_i%d.png" % (ITEMS.index((col, (ix, iy, ix1, iy1), (t, h), hd, tx)) + 1),
                      "left:%dpx;top:%dpx;width:%dpx" % (ix, iy, ix1 - ix), "ab"),
                      ix1 + 24, ty + 6, hd, ix1 + 24, ty + 42, tx))
        n += 1
    out.append("</div>")
    return "".join(out)


HTML = CSS + f"""
<div class="ab" style="left:0;top:106px;width:1672px;text-align:center;font-size:24px;color:#e6f1ff">Классификация по способу создания, назначения трафика и его виду</div>
<svg class="ab" style="left:0;top:0;filter:drop-shadow(0 0 5px #2ad4ff)" width="1672" height="941" fill="none" stroke="#2ad4ff" stroke-width="3">
  <path d="M295 192 V160 H1378 V192 M836 160 V192"/><circle cx="836" cy="158" r="7" fill="#2ad4ff"/>
  <path d="M287 188 l8 12 l8 -12 z M828 188 l8 12 l8 -12 z M1370 188 l8 12 l8 -12 z" fill="#2ad4ff"/></svg>
{_col(0)}
{_col(1)}
{_col(2)}
<div class="step">
  <div class="ab" style="left:290px;top:856px;width:1092px;height:48px;border-radius:10px;border:2px solid #2ad4ff;background:rgba(6,24,64,.7);box-shadow:0 0 14px rgba(42,212,255,.5)"></div>
  <div class="ab" style="left:290px;top:856px;width:1092px;text-align:center;line-height:48px;font-family:Oswald,sans-serif;font-weight:600;font-size:25px;color:#2ad4ff;letter-spacing:.5px">
    ОДНА VLAN МОЖЕТ ОДНОВРЕМЕННО ОТНОСИТЬСЯ К НЕСКОЛЬКИМ КЛАССИФИКАЦИЯМ</div>
</div>
"""
