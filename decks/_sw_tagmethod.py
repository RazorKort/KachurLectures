# -*- coding: utf-8 -*-
"""Метод тегирования подробно: куда вставляется метка, её поля по битам, алгоритм на входе, поведение на выходе.

Тексты — по слайдам 45, 46, 51, 55, 63, 69 pptx 2.2. Каждый слайд — фиксированный холст 1600×780,
вписывается в слайд механизмом .rep, анимация по шагам (класс step) + CSS keyframes с префиксом tm-.
"""
from _sw_lib import sc, head, grow, _esc

W, H = 1600, 780

CSS = """<style>
.tm{position:relative;width:1600px;height:780px;font-family:'Golos Text',sans-serif;color:#eaf6ff}
.tm .ab{position:absolute}
.tm-h{font:600 30px Oswald,sans-serif;letter-spacing:.5px;color:#7df3ff}
.tm-t{font-size:22px;line-height:1.4;color:#cfe3ff}.tm-t b{color:#fff}.tm-t em{font-style:normal;color:#ffc53d}
.tm-mono{font-family:'JetBrains Mono',monospace}
.tm-fr{display:flex;gap:4px;height:84px}
.tm-fr>div{flex:none;display:flex;flex-direction:column;align-items:center;justify-content:center;border-radius:10px;border:2px solid;
  font:600 22px Oswald,sans-serif;color:#fff;text-align:center;line-height:1.1}
.tm-fr small{font:500 16px 'JetBrains Mono',monospace;opacity:.85;margin-top:4px}
.tm-dmac{background:rgba(29,95,216,.35);border-color:#4d8dff}.tm-smac{background:rgba(29,140,120,.35);border-color:#3fd6b4}
.tm-tag{background:rgba(224,38,60,.55);border-color:#ff4d5e;box-shadow:0 0 22px rgba(255,77,94,.7)}
.tm-et{background:rgba(201,162,26,.35);border-color:#ffc53d}.tm-dat{background:rgba(168,58,120,.35);border-color:#e05cff}
.tm-fcs{background:rgba(106,123,160,.35);border-color:#9fb0d8}.tm-fcs1{background:rgba(42,157,90,.45);border-color:#9dfc5a;box-shadow:0 0 18px rgba(157,252,90,.5)}
.tm-pan{position:absolute;border-radius:16px;border:2px solid rgba(42,212,255,.6);background:rgba(6,22,60,.72);box-shadow:0 0 18px rgba(42,212,255,.25)}
.tm-pan.r{border-color:rgba(255,77,94,.7);box-shadow:0 0 18px rgba(255,77,94,.3)}
.tm-pan.g{border-color:rgba(157,252,90,.7);box-shadow:0 0 18px rgba(157,252,90,.25)}
.tm-pan.v{border-color:rgba(155,107,255,.7);box-shadow:0 0 18px rgba(155,107,255,.3)}
/* раздвижение кадра и падение тега */
.tm-gap{width:0;overflow:hidden;transition:width .9s cubic-bezier(.3,1.2,.4,1)}
.step.vis .tm-gap,.tm-gap.vis{width:150px}
.tm-drop{opacity:0;transform:translateY(-120px)}
.step.vis .tm-drop{animation:tm-drop .8s .5s cubic-bezier(.3,1.5,.5,1) forwards}
@keyframes tm-drop{to{opacity:1;transform:none}}
.step.vis .tm-flash{animation:tm-flash 1.6s .3s ease-out both}
@keyframes tm-flash{0%{background:rgba(106,123,160,.35);border-color:#9fb0d8}30%{background:#fff}100%{background:rgba(42,157,90,.45);border-color:#9dfc5a}}
/* битовая линейка */
.tm-bits{display:flex;gap:3px}
.tm-bits i{flex:none;width:42px;height:54px;border-radius:6px;font:700 24px/54px 'JetBrains Mono',monospace;text-align:center;font-style:normal;
  border:2px solid;opacity:0;transform:scale(.6)}
.step.vis .tm-bits i{animation:tm-bit .35s cubic-bezier(.3,1.6,.5,1) forwards}
@keyframes tm-bit{to{opacity:1;transform:none}}
.tm-b-tp{background:rgba(29,95,216,.35);border-color:#4d8dff;color:#bcd6ff}
.tm-b-pc{background:rgba(201,162,26,.35);border-color:#ffc53d;color:#ffe69a}
.tm-b-de{background:rgba(155,107,255,.35);border-color:#b48cff;color:#e2d3ff}
.tm-b-vi{background:rgba(224,38,60,.4);border-color:#ff4d5e;color:#ffd0d6}
.tm-br{position:absolute;height:14px;border:3px solid;border-top:none;border-radius:0 0 10px 10px}
/* блок-схема */
.tm-node{position:absolute;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;border-radius:14px;border:2px solid #2ad4ff;
  background:rgba(8,30,80,.85);font:500 21px/1.25 'Golos Text',sans-serif;color:#fff;padding:8px 14px;box-shadow:0 0 16px rgba(42,212,255,.35)}
.tm-node.q{border-color:#ffc53d;background:rgba(60,45,6,.85);box-shadow:0 0 16px rgba(255,197,61,.35);border-radius:40px}
.tm-node.ok{border-color:#9dfc5a;background:rgba(14,60,30,.85);box-shadow:0 0 16px rgba(157,252,90,.35)}
.tm-node.no{border-color:#ff4d5e;background:rgba(70,10,20,.85);box-shadow:0 0 16px rgba(255,77,94,.35)}
.tm-node.tg{border-color:#ff4d5e;background:rgba(110,16,32,.85);box-shadow:0 0 22px rgba(255,77,94,.55)}
.tm-ar{position:absolute;overflow:visible}
.tm-ar path{fill:none;stroke-width:4;stroke-linecap:round;stroke-dasharray:400;stroke-dashoffset:400}
.step.vis .tm-ar path{animation:tm-draw .7s ease-out forwards}
@keyframes tm-draw{to{stroke-dashoffset:0}}
.tm-lab{position:absolute;font:700 18px Oswald,sans-serif;letter-spacing:.5px}
/* таблица выхода */
.tm-tb{position:absolute;border-collapse:separate;border-spacing:0 8px;font-size:21px}
.tm-tb th{font:600 22px Oswald,sans-serif;color:#7df3ff;text-align:left;padding:4px 18px}
.tm-tb td{background:rgba(8,30,80,.8);padding:14px 18px;line-height:1.35;color:#dbe9ff}
.tm-tb td:first-child{border-radius:12px 0 0 12px;font:700 22px 'JetBrains Mono',monospace;color:#fff}
.tm-tb td:last-child{border-radius:0 12px 12px 0}
.tm-tb tr.step td{border-top:2px solid rgba(42,212,255,.35);border-bottom:2px solid rgba(42,212,255,.35)}
.tm-pill{display:inline-block;padding:2px 10px;border-radius:8px;font:600 18px 'JetBrains Mono',monospace}
.tm-pill.t{background:#e0263c;color:#fff}.tm-pill.u{background:#2b3b66;color:#cfe3ff;border:1px solid #6a7ba0}
/* бегущий кадр по блок-схеме */
.tm-run{position:absolute;width:30px;height:30px;border-radius:8px;background:#ffc53d;box-shadow:0 0 16px #ffc53d;opacity:0}
.step.vis .tm-run{animation:tm-run 6s 1s ease-in-out infinite}
@keyframes tm-run{0%{opacity:0;transform:translate(0,0)}6%{opacity:1}22%{transform:translate(0,120px)}38%{transform:translate(0,240px);background:#ffc53d}
  44%{background:#ff4d5e;box-shadow:0 0 18px #ff4d5e}60%{transform:translate(0,360px);background:#ff4d5e}78%{transform:translate(0,480px)}
  90%{opacity:1;transform:translate(0,480px);background:#9dfc5a;box-shadow:0 0 18px #9dfc5a}100%{opacity:0;transform:translate(0,480px)}}
</style>"""


def _wrap(inner):
    return ('<div class="rep"><div class="repc" style="width:%dpx;height:%dpx">%s<div class="tm">%s</div></div></div>'
            % (W, H, CSS, inner))


def _slide(label, title, sub, inner):
    return '<section class="slide" data-label="%s">%s</section>' % (
        _esc(label), sc(head(title, sub), grow("g", _wrap(inner))))


# ---------- 1. Куда вставляется метка ----------
def s_where():
    fr = lambda tag, fcs_cls, extra="": (
        '<div class="tm-fr">'
        '<div class="tm-dmac" style="width:230px">Destination MAC<small>6 байт</small></div>'
        '<div class="tm-smac" style="width:200px">Source MAC<small>6 байт</small></div>'
        + tag +
        '<div class="tm-et" style="width:150px">EtherType<small>2 байта</small></div>'
        '<div class="tm-dat" style="width:330px">Данные<small>46–1500 байт</small></div>'
        '<div class="%s" style="width:130px">FCS<small>4 байта</small></div></div>' % fcs_cls)
    inner = f"""
<div class="ab tm-h" style="left:40px;top:10px">Кадр Ethernet без метки</div>
<div class="ab" style="left:40px;top:60px">{fr("", "tm-fcs")}</div>
<div class="ab tm-t" style="left:1180px;top:72px;width:400px">длина кадра<br><b class="tm-mono" style="font-size:30px;color:#7df3ff">64 … 1518 байт</b></div>

<div class="step">
  <div class="ab tm-h" style="left:40px;top:205px;color:#ff8a9a">Коммутатор раздвигает кадр после Source MAC…</div>
  <div class="ab" style="left:40px;top:255px"><div class="tm-fr">
    <div class="tm-dmac" style="width:230px">Destination MAC<small>6 байт</small></div>
    <div class="tm-smac" style="width:200px">Source MAC<small>6 байт</small></div>
    <div class="tm-gap" style="border:none;background:none"><div class="tm-tag tm-drop" style="width:146px;height:84px;border-radius:10px;border:2px solid #ff4d5e;
       display:flex;flex-direction:column;align-items:center;justify-content:center;font:600 22px Oswald,sans-serif">802.1Q<small style="font:500 16px 'JetBrains Mono',monospace">4 байта</small></div></div>
    <div class="tm-et" style="width:150px">EtherType<small>2 байта</small></div>
    <div class="tm-dat" style="width:330px">Данные<small>46–1500 байт</small></div>
    <div class="tm-fcs tm-flash" style="width:130px">FCS<small>пересчитан</small></div></div></div>
</div>

<div class="step">
  <div class="tm-pan r" style="left:40px;top:390px;width:740px;height:170px"></div>
  <div class="ab tm-h" style="left:66px;top:404px;color:#ff8a9a">…и вставляет метку 802.1Q — 32 бита</div>
  <div class="ab tm-t" style="left:66px;top:452px;width:690px">Метка встаёт <b>между полями Source MAC и EtherType</b>.
     Адреса остаются на своих местах, данные не меняются — коммутатор лишь «вклинивает» 4 байта.</div>
</div>
<div class="step">
  <div class="tm-pan g" style="left:810px;top:390px;width:750px;height:170px"></div>
  <div class="ab tm-h" style="left:836px;top:404px;color:#b9ff8a">FCS пересчитывается</div>
  <div class="ab tm-t" style="left:836px;top:452px;width:700px">Длина заголовка L2 изменилась — старая контрольная сумма
     больше не подходит. Коммутатор вычисляет её заново.</div>
</div>
<div class="step">
  <div class="tm-pan v" style="left:40px;top:590px;width:1520px;height:140px"></div>
  <div class="ab tm-t" style="left:70px;top:612px;width:1460px;font-size:24px">Итог: кадр стал длиннее на <b>4 байта</b> —
     <span class="tm-mono" style="color:#7df3ff">64 … 1518</span> → <span class="tm-mono" style="color:#ff8a9a">68 … 1522 байт</span>.
     Такой кадр называется <em>тегированным</em> и находится в «зоне VLAN». Оконечные устройства (кроме, например, IP-телефонов)
     формат 802.1Q не понимают — поэтому метку ставит и снимает именно коммутатор.</div>
</div>
"""
    return _slide("Тег: куда вставляется", "Метка 802.1Q: <em>куда</em> вставляется",
                  "Тегирование происходит на входе порта коммутатора", inner)


# ---------- 2. Поля метки по битам ----------
def s_bits():
    # VLAN 10, PRI 0, CFI 0  ->  TCI = 0x000A
    tpid = "1000000100000000"
    tci = "000" + "0" + format(10, "012b")
    cells = []
    for i, b in enumerate(tpid + tci):
        cls = "tm-b-tp" if i < 16 else ("tm-b-pc" if i < 19 else ("tm-b-de" if i < 20 else "tm-b-vi"))
        cells.append('<i class="%s" style="animation-delay:%dms">%s</i>' % (cls, 40 * i, b))
    bits = "".join(cells)
    cw = 45  # ширина клетки с зазором
    x0 = 40
    inner = f"""
<div class="ab tm-h" style="left:40px;top:6px">Метка 802.1Q — 32 бита: <span style="color:#4d8dff">TPID</span> + <span style="color:#ff8a9a">TCI</span></div>
<div class="ab tm-t" style="left:40px;top:52px">Пример: кадр помещается в <b>VLAN 10</b>, приоритет 0</div>
<div class="step">
  <div class="ab tm-bits" style="left:{x0}px;top:110px">{bits}</div>
  <div class="tm-br" style="left:{x0}px;top:170px;width:{16*cw-3}px;border-color:#4d8dff"></div>
  <div class="tm-br" style="left:{x0+16*cw}px;top:170px;width:{16*cw-3}px;border-color:#ff4d5e"></div>
  <div class="ab tm-lab" style="left:{x0+250}px;top:188px;color:#7fb0ff;font-size:24px">TPID · 16 бит = 0x8100</div>
  <div class="ab tm-lab" style="left:{x0+16*cw+260}px;top:188px;color:#ff8a9a;font-size:24px">TCI · 16 бит = 0x000A</div>
</div>

<div class="step">
  <div class="tm-pan" style="left:40px;top:240px;width:1520px;height:120px;border-color:#4d8dff"></div>
  <div class="ab tm-h" style="left:66px;top:252px;color:#7fb0ff">TPID — Tag Protocol ID</div>
  <div class="ab tm-t" style="left:66px;top:298px;width:1470px">Идентификатор протокола тегирования. Для 802.1Q всегда
     <b class="tm-mono">0x8100</b> (<span class="tm-mono">1000 0001 0000 0000</span>). Стоит на месте EtherType — по нему коммутатор понимает, что дальше идёт метка.</div>
</div>

<div class="step">
  <div class="tm-pan" style="left:40px;top:382px;width:490px;height:250px;border-color:#ffc53d"></div>
  <div class="ab tm-h" style="left:66px;top:394px;color:#ffd77a">PRI (PCP) · 3 бита</div>
  <div class="ab tm-t" style="left:66px;top:440px;width:450px">Приоритет кадра для 802.1p (Class of Service): значения
     <b class="tm-mono">0…7</b>. Чем больше — тем раньше кадр уйдёт из очереди (голос, видео).</div>
</div>
<div class="step">
  <div class="tm-pan" style="left:555px;top:382px;width:440px;height:250px;border-color:#b48cff"></div>
  <div class="ab tm-h" style="left:581px;top:394px;color:#d4bfff">CFI (DEI) · 1 бит</div>
  <div class="ab tm-t" style="left:581px;top:440px;width:400px">Drop Eligible Indicator: <b>1</b> — кадр можно отбросить
     первым при переполнении очереди.</div>
</div>
<div class="step">
  <div class="tm-pan r" style="left:1020px;top:382px;width:540px;height:250px"></div>
  <div class="ab tm-h" style="left:1046px;top:394px;color:#ff8a9a">VLAN ID · 12 бит</div>
  <div class="ab tm-t" style="left:1046px;top:440px;width:500px">Номер виртуальной сети — главная часть метки.
     Значения <b class="tm-mono">1…4095</b>; на Eltex VLAN <b>1</b> (по умолчанию) и <b>4095</b> зарезервированы.
     <span class="tm-mono" style="color:#ff8a9a">000000001010</span> = 10.</div>
</div>
<div class="step">
  <div class="tm-pan v" style="left:40px;top:654px;width:1520px;height:96px"></div>
  <div class="ab tm-t" style="left:70px;top:672px;width:1460px;font-size:24px">В кадре метка выглядит как 4 байта
     <b class="tm-mono" style="color:#7fb0ff">81 00</b> <b class="tm-mono" style="color:#ff8a9a">00 0A</b> — сразу после Source MAC.
     VLAN — это широковещательный домен, ограниченный метками 802.1Q.</div>
</div>
"""
    return _slide("Тег: поля по битам", "Из чего состоит <em>метка 802.1Q</em>",
                  "TPID + TCI (PRI · CFI · VLAN ID)", inner)


# ---------- 3. Алгоритм добавления метки на входе ----------
def s_algo():
    def node(x, y, w, h, txt, cls=""):
        return '<div class="tm-node %s" style="left:%dpx;top:%dpx;width:%dpx;height:%dpx">%s</div>' % (cls, x, y, w, h, txt)

    def arrow(x1, y1, x2, y2, col="#2ad4ff"):
        mx = min(x1, x2) - 10
        my = min(y1, y2) - 10
        d = "M%d %d L%d %d" % (x1 - mx, y1 - my, x2 - mx, y2 - my)
        return ('<svg class="tm-ar" style="left:%dpx;top:%dpx" width="%d" height="%d"><path d="%s" stroke="%s"/>'
                '<circle cx="%d" cy="%d" r="7" fill="%s"/></svg>'
                % (mx, my, abs(x2 - x1) + 20, abs(y2 - y1) + 20, d, col, x2 - mx, y2 - my, col))
    cx = 420
    inner = f"""
<div class="tm-run" style="left:{cx-15}px;top:62px"></div>
{node(cx-260, 20, 520, 70, "Кадр пришёл на порт коммутатора")}
<div class="step">{arrow(cx, 92, cx, 140)}{node(cx-260, 140, 520, 76, "Есть метка 802.1Q?<br><span style='font-size:17px;color:#ffe69a'>(EtherType = 0x8100?)</span>", "q")}</div>
<div class="step">
  {arrow(cx, 218, cx, 262, "#ffc53d")}<div class="tm-lab" style="left:{cx+12}px;top:226px;color:#ffc53d">НЕТ</div>
  {node(cx-260, 262, 520, 76, "Берём VLAN порта — PVID<br><span style='font-size:17px;color:#bfe9ff'>access vlan / native vlan / general pvid</span>")}
</div>
<div class="step">
  {arrow(cx, 340, cx, 384, "#ff4d5e")}
  {node(cx-260, 384, 520, 76, "Вставляем метку после Source MAC<br><span class='tm-mono' style='font-size:17px'>TPID=0x8100 · PRI · CFI=0 · VID=PVID</span>", "tg")}
</div>
<div class="step">
  {arrow(cx, 462, cx, 506, "#9dfc5a")}
  {node(cx-260, 506, 520, 70, "Пересчитываем FCS", "ok")}
  {arrow(cx, 578, cx, 618, "#9dfc5a")}
  {node(cx-260, 618, 520, 76, "Кадр в «зоне VLAN» → только в порты,<br>где разрешён этот VLAN ID", "ok")}
</div>
<div class="step">
  {arrow(cx+262, 178, 960, 178, "#ffc53d")}<div class="tm-lab" style="left:{cx+290}px;top:146px;color:#ffc53d">ДА</div>
  {node(960, 140, 560, 76, "VLAN ID из метки разрешён на порту?", "q")}
  {arrow(1150, 218, 1150, 300, "#9dfc5a")}<div class="tm-lab" style="left:1162px;top:244px;color:#9dfc5a">ДА</div>
  {node(940, 300, 420, 86, "Метку не трогаем — кадр уже тегирован<br><span style='font-size:17px;color:#bfe9ff'>(trunk / general tagged)</span>", "ok")}
  {node(1380, 420, 180, 70, "Отбросить кадр", "no")}
  {arrow(1470, 218, 1470, 420, "#ff4d5e")}<div class="tm-lab" style="left:1482px;top:300px;color:#ff4d5e">НЕТ</div>
</div>
<div class="step">
  <div class="tm-pan v" style="left:960px;top:520px;width:600px;height:200px"></div>
  <div class="ab tm-t" style="left:986px;top:536px;width:560px">Метка добавляется <b>один раз — на входе</b> в коммутатор.
     Дальше по магистрали (trunk) кадр идёт уже с меткой, и следующий коммутатор её только читает.
     Нетегированный кадр на trunk попадает в <em>native VLAN</em>.</div>
</div>
"""
    return _slide("Тег: алгоритм на входе", "Как коммутатор <em>добавляет метку</em>",
                  "Алгоритм на входе порта", inner)


# ---------- 4. Что происходит с меткой на выходе ----------
def s_egress():
    rows = [
        ("access", '<span class="tm-pill u">без метки</span> → метка ставится: VID = access VLAN',
         'Метка <b>снимается</b>, FCS пересчитывается — ПК получает обычный кадр Ethernet'),
        ("trunk", '<span class="tm-pill t">с меткой</span> — проверка allowed VLAN;<br><span class="tm-pill u">без метки</span> → native VLAN',
         'Метка <b>остаётся</b>. Кадр native VLAN уходит <b>без метки</b>'),
        ("general", '<span class="tm-pill t">с меткой</span> и <span class="tm-pill u">без метки</span> → PVID',
         'По настройке VLAN: <span class="tm-mono">tagged</span> — с меткой, <span class="tm-mono">untagged</span> — без'),
        ("customer<br>(Q-in-Q)", 'Любой кадр клиента (CVLAN)',
         'Сверху добавляется <b>вторая, внешняя</b> метка SVLAN; CVLAN становится внутренней'),
    ]
    trs = "".join('<tr class="step"><td>%s</td><td>%s</td><td>%s</td></tr>' % r for r in rows)
    inner = f"""
<table class="tm-tb" style="left:40px;top:10px;width:1520px">
  <tr><th style="width:230px">Режим порта</th><th style="width:560px">На входе</th><th>На выходе</th></tr>
  {trs}
</table>
<div class="step">
  <div class="tm-pan v" style="left:40px;top:600px;width:1520px;height:140px"></div>
  <div class="ab tm-t" style="left:70px;top:620px;width:1460px;font-size:24px">Правило: <b>метку ставит входной порт</b>,
     а <b>решает её судьбу выходной</b>. Снятие метки — такая же операция, как добавление: 4 байта убираются,
     FCS считается заново. Кадр с меткой одной VLAN никогда не попадает в другую VLAN.</div>
</div>
"""
    return _slide("Тег: что на выходе", "Метка <em>на выходе</em>: снять или оставить",
                  "Поведение по режимам порта", inner)


def slides():
    return [s_where(), s_bits(), s_algo(), s_egress()]
