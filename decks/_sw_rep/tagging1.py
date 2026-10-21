# -*- coding: utf-8 -*-
"""Процесс тегирования кадров (вариант 1) — коммутатор с VLAN 10/20 и 4 этапа тегирования."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 62

R, B = "#ff4d5e", "#2ad4ff"

CSS = """<style>
.tg1-card{position:absolute;top:487px;height:318px;border-radius:12px;border:2px solid rgba(42,212,255,.7);background:rgba(6,24,64,.62);box-shadow:0 0 14px rgba(42,212,255,.4)}
.tg1-n{position:absolute;top:500px;font-family:Oswald,sans-serif;font-weight:700;font-size:46px;line-height:1;color:#2ad4ff;text-shadow:0 0 10px #2ad4ff}
.tg1-ch{position:absolute;top:510px;font-family:Oswald,sans-serif;font-weight:700;font-size:27px;color:#fff;letter-spacing:.3px}
.tg1-ch span{color:#2ad4ff}
.tg1-tx{position:absolute;font-size:17.5px;line-height:1.2;color:#e6f1ff}
.tg1-sm{position:absolute;font-size:13px;line-height:1.25;text-align:center;transform:translateX(-50%);white-space:nowrap}
.tg1-c{position:absolute;border:1px solid rgba(42,212,255,.7);background:rgba(10,40,100,.7);color:#fff;text-align:center;font-family:'Golos Text',sans-serif;
  display:flex;flex-direction:column}
.tg1-c b{flex:1;display:flex;align-items:center;justify-content:center;font-weight:500;font-size:11.5px;line-height:1.2;border-bottom:1px solid rgba(42,212,255,.6)}
.tg1-c i{height:26px;line-height:26px;font-style:normal;font-family:'JetBrains Mono',monospace;font-size:10px;letter-spacing:-.3px}
.tg1-c.r{border:2px solid #ff4d5e;background:rgba(150,20,40,.85);box-shadow:0 0 14px rgba(255,77,94,.8)}
.tg1-c.r b,.tg1-c.r i{border-color:rgba(255,120,130,.8);font-size:14px}
.tg1-bx{position:absolute;border:2px solid rgba(42,212,255,.75);border-radius:8px;background:rgba(10,30,80,.8);color:#fff;text-align:center;font-family:'Golos Text',sans-serif}
@keyframes tg1-fly{0%{transform:translateX(0);opacity:0}10%{opacity:1}85%{opacity:1}100%{transform:translateX(300px);opacity:0}}
.tg1-pk{position:absolute;left:198px;top:262px;width:24px;height:16px;border-radius:3px;background:#ff4d5e;box-shadow:0 0 12px #ff4d5e;animation:tg1-fly 2.2s linear infinite}
@keyframes tg1-dn{0%{transform:translateY(0);opacity:0}15%{opacity:1}80%{opacity:1}100%{transform:translateY(80px);opacity:0}}
.tg1-dp{position:absolute;width:12px;height:12px;border-radius:50%;background:#ff4d5e;box-shadow:0 0 10px #ff4d5e;animation:tg1-dn 1.6s linear infinite}
</style>"""

PORTS = {1: 558, 2: 637, 3: 716, 4: 797, 5: 879, 6: 961, 7: 1041, 8: 1121}


def _block(cx, y):
    return ('<svg class="ab" style="left:%dpx;top:%dpx" width="34" height="34"><circle cx="17" cy="17" r="14" fill="none" stroke="#2ad4ff" stroke-width="3"/>'
            '<line x1="7" y1="27" x2="27" y2="7" stroke="#2ad4ff" stroke-width="3"/></svg>' % (cx - 17, y - 17))


def _cross(cx, y, s=14):
    return ('<svg class="ab" style="left:%dpx;top:%dpx" width="%d" height="%d"><g stroke="#ff4d5e" stroke-width="4"><line x1="2" y1="2" x2="%d" y2="%d"/>'
            '<line x1="%d" y1="2" x2="2" y2="%d"/></g></svg>' % (cx - s, y - s, 2 * s, 2 * s, 2 * s - 2, 2 * s - 2, 2 * s - 2, 2 * s - 2))


def _ports_out():
    out = ['<svg class="ab" style="left:0;top:0" width="1672" height="941" fill="none" stroke-width="3">']
    for p, x in PORTS.items():
        if p == 1:
            out.append('<line x1="%d" y1="293" x2="%d" y2="378" stroke="%s" stroke-dasharray="7 5"/>' % (x - 14, x - 14, R))
        elif p in (3, 6, 8):
            out.append('<line x1="%d" y1="293" x2="%d" y2="372" stroke="%s" style="filter:drop-shadow(0 0 4px %s)"/>'
                       '<path d="M%d 386 l-11 -16 h22 z" fill="%s" stroke="none"/>' % (x, x, R, R, x, R))
        else:
            out.append('<line x1="%d" y1="293" x2="%d" y2="348" stroke="%s" stroke-dasharray="5 5"/>' % (x, x, B))
    out.append("</svg>")
    out.append(_cross(544, 393))
    out.append('<div class="tg1-sm" style="left:531px;top:416px;font-size:14px;color:#fff">Не отправляется<br>обратно на входной<br>порт</div>')
    for p, x in PORTS.items():
        if p in (2, 4, 5, 7):
            out.append(_block(x, 365) + '<div class="tg1-sm" style="left:%dpx;top:388px;color:#9fd6ff;font-size:12px">VLAN 20<br>(заблокировано)</div>' % x)
        elif p in (3, 6, 8):
            out.append(img("rep/tagging1_lap.png", "left:%dpx;top:390px;width:60px" % (x - 30), "ab"))
            out.append('<div class="tg1-sm" style="left:%dpx;top:442px;color:%s;font-size:15px">VLAN 10<br>(получает кадр)</div>' % (x, R))
            out.append('<div class="tg1-dp" style="left:%dpx;top:296px;animation-delay:%dms"></div>' % (x - 6, p * 90))
    return "".join(out)


def _frame(cells, x0, y0):
    out = []
    for x, w, t, v, c in cells:
        out.append('<div class="tg1-c %s" style="left:%dpx;top:%dpx;width:%dpx;height:80px"><b>%s</b><i>%s</i></div>' % (c, x0 + x, y0, w, t, v))
    return "".join(out)


F1 = [(0, 86, "Destination<br>MAC", "FF:FF:FF:FF:FF:FF", ""), (90, 86, "Source<br>MAC", "AA:BB:CC:DD:EE:01", ""),
      (180, 58, "EtherType", "0x0800", ""), (242, 56, "Payload", "...", ""), (302, 72, "FCS", "0x1A2B3C4D", "")]
F2 = [(0, 70, "Destination<br>MAC", "FF:FF:FF:FF:FF:FF", ""), (73, 66, "Source<br>MAC", "AA:BB:CC:DD:EE:01", ""),
      (143, 95, "TPID 0x8100 |<br>VLAN ID 10", "32 БИТА", "r"), (242, 50, "EtherType", "0x0800", ""), (295, 48, "Payload", "...", ""),
      (347, 53, "FCS", "0x??????", "")]

HTML = CSS + f"""
<div class="ab" style="left:57px;top:98px;font-family:Oswald,sans-serif;font-weight:600;font-size:40px;color:#2ad4ff">IEEE 802.1Q • VLAN</div>
<div class="ab" style="left:57px;top:149px;width:72px;height:4px;background:#2ad4ff;box-shadow:0 0 8px #2ad4ff"></div>

<div class="step">
  {img("rep/tagging1_sw.png", "left:415px;top:112px;width:867px", "ab")}
  {img("rep/tagging1_pc.png", "left:35px;top:195px;width:162px", "ab")}
  <div class="ab" style="left:35px;top:344px;width:186px;text-align:center;font-family:'Golos Text',sans-serif;font-weight:600;font-size:19px;line-height:1.2;color:#fff">Оконечное<br>устройство (ПК)</div>
</div>
<div class="step">
  <div class="tg1-bx" style="left:196px;top:208px;width:212px;height:42px;border-color:{R};background:rgba(110,15,30,.85);font-size:14px;line-height:1.2;padding-top:3px">Широковещательный кадр<br>(нетегированный)</div>
  <svg class="ab" style="left:186px;top:258px" width="332" height="26"><line x1="0" y1="13" x2="312" y2="13" stroke="{R}" stroke-width="5" style="filter:drop-shadow(0 0 6px {R})"/>
    <path d="M330 13 L308 1 V25 Z" fill="{R}"/></svg>
  <div class="tg1-pk"></div>
</div>
<div class="step">{_ports_out()}</div>

<div class="step">
  <div class="ab" style="left:1322px;top:66px;width:322px;height:204px;border-radius:12px;border:2px solid rgba(42,212,255,.6);background:rgba(6,24,64,.7)"></div>
  {img("rep/tagging1_pr.png", "left:1348px;top:88px;width:82px", "ab")}
  {img("rep/tagging1_pb.png", "left:1348px;top:178px;width:82px", "ab")}
  <div class="ab" style="left:1443px;top:98px;font-family:Oswald,sans-serif;font-weight:600;font-size:23px;color:{R}">КРАСНАЯ VLAN 10</div>
  <div class="ab" style="left:1443px;top:128px;font-size:19px;color:#fff">Порты: 1, 3, 6, 8</div>
  <div class="ab" style="left:1443px;top:188px;font-family:Oswald,sans-serif;font-weight:600;font-size:23px;color:{B}">СИНЯЯ VLAN 20</div>
  <div class="ab" style="left:1443px;top:216px;font-size:19px;color:#fff">Порты: 2, 4, 5, 7</div>
</div>

<div class="step">
  <div class="tg1-card" style="left:12px;width:408px"></div>
  <div class="tg1-n" style="left:38px">1.</div>
  <div class="tg1-ch" style="left:88px">НЕТЕГИРОВАННЫЙ <span>КАДР</span></div>
  <div class="tg1-tx" style="left:47px;top:556px">Кадр Ethernet поступает от оконечного<br>устройства</div>
  <div class="ab" style="left:20px;top:616px;width:392px;height:112px;border:1px solid rgba(42,212,255,.5);border-radius:8px"></div>
  {_frame(F1, 30, 632)}
  <div class="tg1-tx" style="left:12px;top:741px;width:408px;text-align:center">Кадр без тега 802.1Q<br>(поступает на порт 1)</div>
</div>
<div class="step">
  <div class="tg1-card" style="left:432px;width:423px"></div>
  <div class="tg1-n" style="left:455px">2.</div>
  <div class="tg1-ch" style="left:511px">ДОБАВЛЕНИЕ ТЕГА 802.1Q</div>
  <div class="tg1-tx" style="left:451px;top:556px">Коммутатор определяет VLAN входного<br>порта</div>
  <div class="ab" style="left:438px;top:616px;width:410px;height:112px;border:1px solid rgba(42,212,255,.5);border-radius:8px"></div>
  {_frame(F2, 442, 632)}
  <svg class="ab" style="left:617px;top:714px" width="16" height="36"><line x1="8" y1="8" x2="8" y2="36" stroke="{R}" stroke-width="2"/><path d="M8 0 L1 12 H15 Z" fill="{R}"/></svg>
  <div class="tg1-tx" style="left:432px;top:749px;width:412px;text-align:center;font-size:15px;color:{R}">Тег 802.1Q вставляется<br>между Source MAC и EtherType</div>
</div>
<div class="step">
  <div class="tg1-card" style="left:866px;width:352px"></div>
  <div class="tg1-n" style="left:892px">3.</div>
  <div class="tg1-ch" style="left:948px">ПЕРЕСЧЁТ <span>FCS</span></div>
  <div class="tg1-tx" style="left:898px;top:556px;font-size:18px">После изменения кадра контрольная<br>сумма вычисляется заново</div>
  <div class="tg1-bx" style="left:883px;top:630px;width:94px;height:98px"><div style="font-size:17px;line-height:1.2;padding:12px 0 6px;border-bottom:1px solid rgba(42,212,255,.6)">FCS<br>(старый)</div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:12px;line-height:24px">0x1A2B3C4D</div></div>
  <div class="tg1-bx" style="left:1112px;top:630px;width:94px;height:98px"><div style="font-size:17px;line-height:1.2;padding:12px 0 6px;border-bottom:1px solid rgba(42,212,255,.6)">FCS<br><span style="color:{B}">(новый)</span></div>
    <div style="font-family:'JetBrains Mono',monospace;font-size:12px;line-height:24px">0x5E6F7A8B</div></div>
  {img("rep/tagging1_ref.png", "left:993px;top:622px;width:109px", "ab")}
  <svg class="ab" style="left:978px;top:664px" width="134" height="24"><g fill="{B}"><path d="M0 8 H8 V2 L20 12 L8 22 V16 H0 Z"/><path d="M112 8 H120 V2 L132 12 L120 22 V16 H112 Z"/></g></svg>
  <div class="tg1-tx" style="left:866px;top:738px;width:362px;text-align:center;font-size:15px">Пересчёт<br>контрольной суммы</div>
</div>
<div class="step">
  <div class="tg1-card" style="left:1230px;width:430px"></div>
  <div class="tg1-n" style="left:1248px">4.</div>
  <div class="tg1-ch" style="left:1300px;font-size:21px;letter-spacing:0">ПЕРЕДАЧА В РАЗРЕШЁННЫЕ <span>ПОРТЫ</span></div>
  <div class="tg1-tx" style="left:1252px;top:558px;font-size:17px;white-space:nowrap">Кадр направляется только через порты VLAN 10</div>
  {''.join('<div class="ab" style="left:%dpx;top:602px;width:30px;text-align:center;font-size:16px;color:#fff">%d</div>' % (x - 15, i + 1)
           for i, x in enumerate([1271, 1320, 1368, 1417, 1467, 1516, 1565, 1613]))}
  {img("rep/tagging1_ports.png", "left:1244px;top:623px;width:401px", "ab")}
  {_cross(1270, 695, 9)}
  {''.join(_block(x, 695).replace('width="34" height="34"', 'width="34" height="34" style="transform:scale(.62)"') for x in (1320, 1417, 1467, 1565))}
  <svg class="ab" style="left:0;top:0" width="1672" height="941">{''.join('<line x1="%d" y1="662" x2="%d" y2="700" stroke="%s" stroke-width="3"/><path d="M%d 712 l-8 -13 h16 z" fill="%s"/>' % (x, x, R, x, R) for x in (1368, 1515, 1613))}</svg>
  {''.join(img("rep/tagging1_lap.png", "left:%dpx;top:710px;width:50px" % (x - 25), "ab") + '<div class="tg1-sm" style="left:%dpx;top:752px;color:%s;font-size:15px">VLAN 10</div>' % (x, R) for x in (1368, 1515, 1613))}
</div>

<div class="step">
  <div class="ab" style="left:22px;top:832px;width:1628px;height:76px;border-radius:12px;border:2px solid rgba(42,212,255,.6);background:rgba(6,24,64,.7)"></div>
  {img("rep/tagging1_lr.png", "left:53px;top:848px;width:54px", "ab")}
  <div class="ab" style="left:117px;top:856px;font-family:Oswald,sans-serif;font-weight:600;font-size:22px;color:{R}">КРАСНЫЙ — VLAN 10</div>
  <div class="ab" style="left:320px;top:852px;width:2px;height:36px;background:rgba(42,212,255,.5)"></div>
  {img("rep/tagging1_lb.png", "left:356px;top:848px;width:54px", "ab")}
  <div class="ab" style="left:425px;top:858px;font-family:Oswald,sans-serif;font-weight:600;font-size:22px;color:{B}">СИНИЙ — VLAN 20</div>
  <div class="ab" style="left:606px;top:848px;font-size:34px;line-height:1;color:{B}">›</div>
  <div class="ab" style="left:645px;top:842px;width:1000px;height:58px;border-radius:10px;border:2px solid {B};box-shadow:0 0 12px rgba(42,212,255,.5)"></div>
  <div class="ab" style="left:645px;top:842px;width:1000px;line-height:58px;text-align:center;font-family:Oswald,sans-serif;font-weight:600;font-size:23px;color:#fff">
    ТЕГ VLAN ОГРАНИЧИВАЕТ ШИРОКОВЕЩАТЕЛЬНУЮ РАССЫЛКУ В ПРЕДЕЛАХ ОДНОГО ДОМЕНА</div>
</div>
"""

# ---- анимация тегирования поверх схемы: кадр от ПК входит в порт 1, получает тег 802.1Q,
#      копии с тегом спускаются из красных портов 3, 6, 8 к ноутбукам, синие порты мигают запретом
_A1 = """<style>
.t1a-fr{position:absolute;left:0;top:0;display:flex;gap:2px;height:30px;font:700 12px/30px 'Golos Text',sans-serif;color:#fff;
  transform-origin:0 0;filter:drop-shadow(0 0 8px rgba(255,77,94,.7));animation:t1a-main 8s infinite}
.t1a-fr i{font-style:normal;flex:none;text-align:center;border-radius:4px;overflow:hidden;white-space:nowrap}
.t1a-fr .a{background:#1d5fd8;width:46px}.t1a-fr .e{background:#c9a21a;width:62px}.t1a-fr .d{background:#a83a78;width:54px}
.t1a-fr .f{background:#6a7ba0;width:42px;animation:t1a-fcs 8s infinite}.t1a-fr .q{background:#e0263c;width:0;animation:t1a-tag 8s infinite}
.t1a-pk{position:absolute;width:74px;height:26px;border-radius:6px;background:#e0263c;color:#fff;font:700 13px/26px 'Oswald',sans-serif;text-align:center;
  box-shadow:0 0 14px #ff4d5e;opacity:0;animation:t1a-down 8s infinite}
.t1a-no{position:absolute;width:40px;height:40px;border-radius:50%;box-shadow:0 0 0 3px #2ad4ff,0 0 18px #2ad4ff;opacity:0;animation:t1a-no 8s infinite}
.t1a-lbl{position:absolute;font:700 20px 'Oswald',sans-serif;color:#ff6b7c;opacity:0;animation:t1a-lbl 8s infinite;white-space:nowrap}
@keyframes t1a-main{0%{transform:translate(190px,282px) scale(.62);opacity:0}5%{opacity:1}30%{transform:translate(300px,282px) scale(.62);opacity:1}
  52%{transform:translate(300px,282px) scale(.62);opacity:1}58%,100%{transform:translate(300px,282px) scale(.62);opacity:0}}
@keyframes t1a-tag{0%,32%{width:0}42%,100%{width:58px}}
@keyframes t1a-fcs{0%,44%{background:#6a7ba0}47%{background:#fff}52%,100%{background:#2a9d5a}}
@keyframes t1a-down{0%,56%{transform:translateY(0);opacity:0}60%{opacity:1}82%{transform:translateY(78px);opacity:1}90%,100%{transform:translateY(78px);opacity:0}}
@keyframes t1a-no{0%,58%{opacity:0}64%,70%{opacity:1}74%{opacity:.2}78%,86%{opacity:1}92%,100%{opacity:0}}
@keyframes t1a-lbl{0%,33%{opacity:0}37%,54%{opacity:1}58%,100%{opacity:0}}
</style>"""

HTML += _A1 + """
<div class="step">
  <div class="t1a-fr"><i class="a">DMAC</i><i class="a">SMAC</i><i class="q">802.1Q</i><i class="e">EtherType</i><i class="d">Payload</i><i class="f">FCS</i></div>
  <div class="t1a-lbl" style="left:296px;top:306px;font-size:17px">+ тег 802.1Q, новый FCS</div>
""" + "".join('<div class="t1a-pk" style="left:%dpx;top:300px">802.1Q · 10</div>' % (x - 37) for x in (717, 961, 1123)) + \
    "".join('<div class="t1a-no" style="left:%dpx;top:343px"></div>' % (x - 20) for x in (637, 797, 880, 1041)) + """
</div>
"""
