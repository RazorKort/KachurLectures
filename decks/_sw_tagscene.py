# -*- coding: utf-8 -*-
"""Сцена «Процесс тегирования кадров» по рисункам 2.4.2.2–2.4.2.4 из pptx 2.2 (слайды 47–50).

Вёрстка повторяет схемы pptx (белое поле, порты на левой кромке коммутатора, цветные поля кадра),
шаги идут кнопками сцены «Назад / Вперёд»: кадр входит в красный порт → тег 802.1Q → FCS1 →
копии во все порты → синие порты отбрасывают, красный снимает тег и пересчитывает FCS.
"""
from _sw_lib import scene

W, H = 1500, 660
BOX_X, BOX_Y, BOX_W, BOX_H = 604, 40, 870, 590
PORTS = [("r", 80), ("b", 200), ("r", 320), ("b", 440)]   # цвет, верх сегмента
PORT_H = 72
ROW_H = 54
FIELD = {  # подпись, ширина, класс
    "dst": ("Destination MAC<br><small>ff:ff:ff:ff:ff:ff</small>", 160, "dst"),
    "src": ("Source MAC", 140, "src"),
    "tpid": ("TPID", 62, "tag"),
    "tci": ("TCI", 62, "tag"),
    "et": ("Ether<br>Type", 70, "et"),
    "pl": ("Payload", 120, "pl"),
    "fcs": ("FCS", 66, "fcs"),
    "fcs1": ("FCS1", 66, "fcs1"),
    "fcs2": ("FCS2", 66, "fcs1"),
}

CSS = """<style>
.tgs{position:relative;width:%dpx;height:%dpx;background:#fff;border-radius:16px;box-shadow:0 0 0 2px rgba(42,212,255,.55),0 0 30px rgba(42,212,255,.3);
  overflow:hidden;font-family:Arial,'Golos Text',sans-serif;color:#222}
.tgs *{box-sizing:border-box}
.tgs-box{position:absolute;border:2px solid #333;border-radius:2px}
.tgs-port{position:absolute;width:16px;height:%dpx;border:1px solid #111}
.tgs-port.r{background:#e3121b}.tgs-port.b{background:#0b1a8c}
.tgs-row{position:absolute;display:flex;height:%dpx}
.tgs-row i{font-style:normal;flex:none;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
  font-size:15px;line-height:1.15;border:1px solid #777;border-radius:8px;margin-right:2px}
.tgs-row i small{font-size:12px}
.tgs-row .dst{background:#dbe8f7;border-color:#7d9cc8}.tgs-row .src{background:#d6ead2;border-color:#8fbf86}
.tgs-row .tag{background:#e3121b;color:#fff;font-weight:700;border-color:#a00}
.tgs-row .et{background:#fde7c9;border-color:#e0b070}.tgs-row .pl{background:#f6cfcf;border-color:#d79a9a}
.tgs-row .fcs{background:#fff;border-color:#555}.tgs-row .fcs1{background:#bff0c8;border-color:#2a9d5a;font-weight:700}
.tgs-x{position:absolute;width:64px;height:64px}
.tgs-x::before,.tgs-x::after{content:"";position:absolute;left:28px;top:-4px;width:8px;height:72px;background:#e3121b;border-radius:4px;transform:rotate(45deg)}
.tgs-x::after{transform:rotate(-45deg)}
.tgs-lbl{position:absolute;font:700 22px 'Oswald',sans-serif;letter-spacing:.3px}
.tgs-cap{position:absolute;left:0;bottom:0;width:100%%;text-align:center;font-style:italic;font-size:17px;color:#333;padding:6px}
/* движение: элементы появляются из стартовой точки, заданной --dx/--dy */
.tgs-fly.on{animation:tgs-fly .9s cubic-bezier(.2,.7,.2,1) both}
@keyframes tgs-fly{from{transform:translate(var(--dx,0),var(--dy,0));opacity:.2}to{transform:none;opacity:1}}
.tgs-pop.on{animation:tgs-pop .6s cubic-bezier(.3,1.6,.5,1) both}
@keyframes tgs-pop{from{transform:scale(.2);opacity:0}to{transform:none;opacity:1}}
.tgs-glow.on{animation:tgs-glow 1.4s ease-in-out infinite alternate}
@keyframes tgs-glow{from{box-shadow:0 0 0 0 rgba(42,157,90,.0)}to{box-shadow:0 0 0 6px rgba(42,157,90,.45)}}
.tgs .tgs-dim.on{opacity:.25}
</style>""" % (W, H, PORT_H, ROW_H)


def _row(keys, x, y, attrs="", cls="", style=""):
    cells = "".join('<i class="%s" style="width:%dpx">%s</i>' % (FIELD[k][2], FIELD[k][1], FIELD[k][0]) for k in keys)
    return ('<div class="tgs-row %s" style="left:%dpx;top:%dpx;%s" %s>%s</div>'
            % (cls, x, y, style, attrs, cells))


def _width(keys):
    return sum(FIELD[k][1] + 2 for k in keys)


def _port_mid(i):
    return BOX_Y + PORTS[i][1] - BOX_Y + PORT_H // 2


def build_html():
    o = [CSS, '<div class="tgs">']
    o.append('<div class="tgs-box" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx"></div>' % (BOX_X, BOX_Y, BOX_W, BOX_H))
    o.append('<div class="tgs-lbl" style="left:%dpx;top:%dpx;color:#0b1a8c">Коммутатор</div>' % (BOX_X + BOX_W - 160, BOX_Y + 10))
    for c, top in PORTS:
        o.append('<div class="tgs-port %s" style="left:%dpx;top:%dpx"></div>' % (c, BOX_X - 8, top))

    y1 = _port_mid(0) - ROW_H // 2
    # шаг 0: нетегированный кадр подлетает к красному порту снаружи (ведущее поле Destination MAC справа)
    out_keys = ["fcs", "pl", "et", "src", "dst"]
    x0 = BOX_X - 8 - _width(out_keys)
    o.append(_row(out_keys, x0, y1, 'data-ph="0" data-ph-only', cls='tgs-fly', style='--dx:-260px'))
    # шаг 1: кадр внутри, порт добавляет тег (TCI, TPID между EtherType и Source MAC)
    in_keys = ["fcs", "pl", "et", "tci", "tpid", "src", "dst"]
    xi = BOX_X + 14
    o.append(_row(["fcs", "pl", "et"], xi, y1, 'data-ph="1" data-ph-upto="2"', cls='tgs-fly', style='--dx:-420px'))
    o.append(_row(["tci", "tpid"], xi + _width(["fcs", "pl", "et"]), y1, 'data-ph="1" data-ph-upto="2"', cls='tgs-pop'))
    o.append(_row(["src", "dst"], xi + _width(["fcs", "pl", "et", "tci", "tpid"]), y1,
                  'data-ph="1" data-ph-upto="2"', cls='tgs-fly', style='--dx:-540px'))
    # шаг 2: FCS → FCS1 (поверх старого FCS)
    o.append(_row(["fcs1"], xi, y1, 'data-ph="2" data-ph-upto="2"', cls='tgs-pop tgs-glow'))
    o.append('<div class="tgs-lbl" data-ph="2" data-ph-upto="2" style="left:%dpx;top:%dpx;color:#2a9d5a">«Зона VLAN» (VLAN-enabled area)</div>'
             % (xi + 40, y1 + 74))

    # шаг 3: широковещательный кадр копируется во все порты (копии идут к портам, ведущее поле Destination MAC слева)
    copy_keys = ["dst", "src", "tpid", "tci", "et", "pl", "fcs1"]
    for i in (1, 2, 3):
        y = _port_mid(i) - ROW_H // 2
        o.append(_row(copy_keys, BOX_X + 14, y, 'data-ph="3" data-ph-upto="3"', cls="tgs-fly", style="--dx:300px;--dy:%dpx" % (y1 - y)))
    # шаг 4: синие порты отбрасывают (крест), красный — снимает тег, пересчитывает FCS, кадр выходит
    for i in (1, 3):
        y = _port_mid(i) - 32
        o.append('<div class="tgs-x tgs-pop" data-ph="4" style="left:%dpx;top:%dpx"></div>' % (BOX_X - 32, y))
        y2 = _port_mid(i) - ROW_H // 2
        o.append(_row(copy_keys, BOX_X + 14, y2, 'data-ph="4"', cls='tgs-dim'))
    y3 = _port_mid(2) - ROW_H // 2
    out2 = ["dst", "src", "et", "pl", "fcs2"]
    o.append(_row(out2, BOX_X - 8 - _width(out2) - 6, y3, 'data-ph="4"', cls="tgs-fly", style="--dx:%dpx" % (_width(out2) + 40)))
    o.append('<div class="tgs-lbl" data-ph="4" style="left:40px;top:%dpx;color:#e3121b">Тег снят · FCS пересчитан → FCS2</div>' % (y3 + 64))
    o.append('<div class="tgs-lbl" data-ph="4" style="left:%dpx;top:%dpx;color:#0b1a8c">Синие порты: тег не совпадает — кадр отброшен</div>'
             % (BOX_X + 60, BOX_Y + BOX_H - 46))
    o.append('<div class="tgs-cap">Рисунки 2.4.2.2–2.4.2.4 — тегирование кадра на порту коммутатора</div>')
    o.append('</div>')
    return "".join(o)


CAPS = [
    "Широковещательный кадр без тега приходит на «красный» порт коммутатора",
    "При получении кадра на порту коммутатор добавляет к нему соответствующий тег 802.1Q (TPID + TCI)",
    "Длина и поля кадра изменились — коммутатор пересчитывает FCS (FCS1). Кадр в «зоне VLAN»",
    "Кадр широковещательный — он копируется во все порты коммутатора",
    "«Синие» порты отбрасывают кадр (тег не совпадает); на «красном» тег удаляется, FCS пересчитывается — кадр уходит без тега",
]


def html():
    body = '<div class="rep" style="height:60vh;width:100%%"><div class="repc" style="width:%dpx;height:%dpx;background:none;box-shadow:none">%s</div></div>' % (W, H, build_html())
    return scene(body, CAPS)
