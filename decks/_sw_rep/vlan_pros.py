# -*- coding: utf-8 -*-
"""Преимущества VLAN — список преимуществ слева, неоновый город с котом и VLAN 10–40 справа."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 108

CSS = """<style>
.vp-h{position:absolute;left:192px;font-family:Oswald,sans-serif;font-weight:600;font-size:28px;line-height:1}
.vp-tx{position:absolute;left:194px;font-size:22px;line-height:1.24;color:#f0f4ff}
.vp-tag{position:absolute;border-radius:10px;border:3px solid var(--c);background:rgba(12,10,40,.85);box-shadow:0 0 16px var(--c);
  text-align:center;font-family:Oswald,sans-serif;font-weight:600;color:#fff;font-size:27px;line-height:1.05;padding-top:8px}
.vp-tag i{display:block;font-style:normal;font-size:17px;margin-top:4px}
@keyframes vp-pulse{0%,100%{box-shadow:0 0 10px var(--c)}50%{box-shadow:0 0 26px var(--c)}}
.vp-tag{animation:vp-pulse 2.4s ease-in-out infinite}
</style>"""

PROS = [("vlan_pros_i1.png", 263, 109, "#c78bff", "БЕЗОПАСНОСТЬ", "Группы с конфиденциальными данными<br>изолированы от остальных пользователей", 273),
        ("vlan_pros_i2.png", 383, 109, "#2ad4ff", "МЕНЬШЕ ШИРОКОВЕЩАТЕЛЬНЫХ ДОМЕНОВ", "Сеть делится на сегменты, а лишний<br>широковещательный трафик отбрасывается", 393),
        ("vlan_pros_i3.png", 511, 109, "#ffc53d", "УПРОЩЁННОЕ ОБСЛУЖИВАНИЕ", "Правила VLAN автоматически применяются<br>к назначенным портам; понятные имена<br>упрощают управление", 517),
        ("vlan_pros_i4.png", 643, 109, "#ff7be0", "МАСШТАБИРУЕМОСТЬ", "Пользователей и отделы можно объединять<br>независимо от их географического<br>расположения", 657)]
TAGS = [(838, 188, 142, "#2ad4ff", "VLAN 10", "ОФИС"), (1072, 116, 148, "#b56bff", "VLAN 20", "РАЗРАБОТКА"),
        (1308, 190, 138, "#ffb43d", "VLAN 30", "ГОСТИ"), (1503, 246, 144, "#ff5cd6", "VLAN 40", "БУХГАЛТЕРИЯ")]


def _pros():
    return "".join('<div class="step">%s<div class="vp-h" style="top:%dpx;color:%s">%s</div><div class="vp-tx" style="top:%dpx">%s</div></div>'
                   % (img("rep/" + ic, "left:58px;top:%dpx;width:%dpx" % (y, w), "ab"), ty, c, h, ty + 32, tx)
                   for ic, y, w, c, h, tx, ty in PROS)


def _tags():
    return "".join('<div class="vp-tag" style="--c:%s;left:%dpx;top:%dpx;width:%dpx;height:70px;transition-delay:%dms">%s<i>%s</i></div>'
                   % (c, x, y, w, i * 120, t, s) for i, (x, y, w, c, t, s) in enumerate(TAGS))


HTML = CSS + f"""
<div class="step">{img("rep/vlan_pros_art.png", "left:748px;top:108px;width:924px", "ab")}</div>
<div class="step">{_tags().replace('class="vp-tag"', 'class="vp-tag"')}</div>
<div class="ab" style="left:34px;top:184px;width:710px;height:704px;border-radius:14px;border:2px solid rgba(42,212,255,.55);background:rgba(4,14,44,.72);box-shadow:0 0 16px rgba(42,212,255,.35)"></div>
<div class="ab" style="left:60px;top:198px;font-family:Oswald,sans-serif;font-weight:700;font-size:42px;color:#2ad4ff;letter-spacing:.5px;text-shadow:0 0 10px rgba(42,212,255,.6)">ОСНОВНЫЕ ПРЕИМУЩЕСТВА</div>
{_pros()}
<div class="step">
  <div class="ab" style="left:62px;top:786px;width:654px;height:2px;background:rgba(42,212,255,.6)"></div>
  <div class="ab" style="left:34px;top:800px;width:710px;text-align:center;font-family:Oswald,sans-serif;font-weight:600;font-size:28px;line-height:1.25;color:#fff">
    VLAN <span style="color:#2ad4ff">ПОВЫШАЮТ</span> БЕЗОПАСНОСТЬ, <span style="color:#2ad4ff">СНИЖАЮТ</span><br>
    <span style="color:#2ad4ff">ЛИШНИЙ ТРАФИК</span> И <span style="color:#2ad4ff">УПРОЩАЮТ УПРАВЛЕНИЕ СЕТЬЮ</span></div>
</div>
"""
