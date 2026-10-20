# -*- coding: utf-8 -*-
"""BRIDGE_FWD — сетевой мост, пересылка по таблице MAC: вёрстка 1:1 (pptx 14).
build() общий для bridge_fwd и bridge_pcapcb (одинаковая композиция)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 150   # заголовок «Сетевой мост» + подзаголовок даёт head()

CSS = """<style>
.brf-dom{position:absolute;border:2.5px dashed #2ad4ff;border-radius:14px;background:rgba(6,30,70,.25)}
.brf-dom.m{border-color:#e05cff;background:rgba(40,10,70,.22)}
.brf-dh{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:27px;color:#2ad4ff}
.brf-mac{position:absolute;font-family:'JetBrains Mono',monospace;font-size:18px;color:#fff;background:rgba(6,18,46,.92);padding:0 3px;letter-spacing:-.5px}
.brf-tb{position:absolute;left:630px;top:164px;width:410px;border:2px solid #2ad4ff;border-radius:6px;background:rgba(6,24,64,.92);box-shadow:0 0 14px rgba(42,212,255,.55);
  border-collapse:collapse;font-size:21px;color:#fff;overflow:hidden}
.brf-tb th{font-family:Oswald,sans-serif;font-weight:700;font-size:25px;color:#2ad4ff;height:40px;border-bottom:2px solid #2ad4ff}
.brf-tb td{height:37px;border-top:1.5px solid rgba(42,212,255,.6);border-left:1.5px solid rgba(42,212,255,.6);text-align:center}
.brf-tb td:first-child{border-left:none}
.brf-tb td.mo{font-family:'JetBrains Mono',monospace;font-size:19px;letter-spacing:-.5px}
.brf-tb tr.hl td{background:rgba(255,190,40,.28);box-shadow:inset 0 0 0 2px #ffc53d}
.brf-pan{position:absolute;border-radius:10px;border:2px solid #2ad4ff;background:linear-gradient(180deg,rgba(8,44,96,.75),rgba(4,20,54,.88));
  box-shadow:0 0 14px rgba(42,212,255,.5),inset 0 0 22px rgba(42,212,255,.14)}
.brf-pan.m{border-color:#e05cff;background:linear-gradient(180deg,rgba(60,20,110,.78),rgba(28,10,66,.88));box-shadow:0 0 14px rgba(224,92,255,.55),inset 0 0 22px rgba(224,92,255,.16)}
.brf-num{position:absolute;width:68px;height:72px;border-radius:9px;border:2.5px solid #2ad4ff;background:rgba(6,30,70,.9);box-shadow:0 0 12px rgba(42,212,255,.7);
  display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:700;font-size:48px;color:#fff}
.brf-num.m{border-color:#e05cff;box-shadow:0 0 12px rgba(224,92,255,.8)}
.brf-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:30px;line-height:1;color:#2ad4ff;white-space:nowrap}
.brf-t{position:absolute;font-size:22px;line-height:1.36;color:#fff;white-space:nowrap}
.brf-f{-webkit-mask-image:linear-gradient(90deg,transparent,#000 3%,#000 97%,transparent),linear-gradient(180deg,transparent,#000 3%,#000 97%,transparent);-webkit-mask-composite:source-in;mask-composite:intersect}
.brf-glow{animation:brfGlow 1.4s ease-in-out infinite}
@keyframes brfGlow{50%{filter:brightness(1.6) drop-shadow(0 0 10px #ffc53d)}}
</style>"""

ROWS = [("PC-A", "AA:BB:CC:11:22:33", "E1"), ("PC-B", "AA:BB:CC:11:22:55", "E1"), ("PC-C", "BA:BB:CC:11:22:44", "E2")]


def _table(hl):
    rows = "".join('<tr class="%s"><td>%s</td><td class="mo">%s</td><td>%s</td></tr>' % ("hl" if i == hl else "", a, b, c)
                   for i, (a, b, c) in enumerate(ROWS))
    return ('<table class="brf-tb"><tr><th colspan="3">Таблица MAC-адресов B1</th></tr>'
            '<tr><td style="width:100px">Узел</td><td>MAC-адрес</td><td style="width:96px">Порт</td></tr>%s</table>' % rows)


def _card(x, w, cls, num, head, text, ico, ico_st):
    return ('<div class="step"><div class="brf-pan %s" style="left:%dpx;top:660px;width:%dpx;height:156px"></div>'
            '<div class="brf-num %s" style="left:%dpx;top:680px">%s</div>%s'
            '<div class="brf-h" style="left:%dpx;top:686px;color:%s">%s</div>'
            '<div class="brf-t" style="left:%dpx;top:732px">%s</div></div>'
            % (cls, x, w, cls, x + 20, num, img("rep/" + ico, ico_st, "ab brf-f"), x + 114,
               "#ff6fe0" if cls == "m" else "#2ad4ff", head, x + 114, text))


def build(n, cards, info, mid_extra="", hl=-1):
    return CSS + f"""
<div class="step">
  <div class="brf-dom" style="left:20px;top:168px;width:582px;height:468px"></div>
  <div class="brf-dom m" style="left:1068px;top:168px;width:582px;height:468px"></div>
  {img("rep/%s_l.png" % n, "left:26px;top:220px;width:572px", "ab brf-f")}
  {img("rep/%s_r.png" % n, "left:1074px;top:220px;width:572px", "ab brf-f")}
  <div class="brf-dh" style="left:44px;top:178px">Домен коллизий 1</div>
  <div class="brf-dh" style="left:1410px;top:178px;color:#ff7af0">Домен коллизий 2</div>
  <div class="brf-mac" style="left:38px;top:370px">AA:BB:CC:11:22:33</div>
  <div class="brf-mac" style="left:40px;top:597px">AA:BB:CC:11:22:55</div>
  <div class="brf-mac" style="left:1464px;top:373px">BA:BB:CC:11:22:44</div>
  <div class="brf-mac" style="left:1464px;top:600px">BA:BB:CC:11:22:66</div>
</div>
<div class="step">{_table(hl)}</div>
<div class="step">{img("rep/%s_m.png" % n, "left:598px;top:362px;width:476px", "ab brf-f")}{mid_extra}</div>
{cards}
<div class="step">
  <div class="brf-pan" style="left:72px;top:844px;width:1526px;height:56px;border-color:rgba(42,212,255,.5);box-shadow:none"></div>
  {img("rep/bridge_fwd_i.png", "left:390px;top:852px;width:42px", "ab brf-f")}
  {info}
</div>
"""


HTML = build("bridge_fwd", "".join([
    _card(20, 506, "", "1", "ОБУЧЕНИЕ", "Мост запоминает MAC-адрес<br>источника и входной порт.", "bridge_fwd_book.png", "left:432px;top:680px;width:78px"),
    _card(539, 550, "m", "2", "ПЕРЕСЫЛКА PC-A → PC-C", "Адрес PC-C изучен на E2:<br>мост передаёт кадр из E1 в E2.", "bridge_fwd_env.png", "left:990px;top:690px;width:72px"),
    _card(1106, 546, "", "3", "ФИЛЬТРАЦИЯ PC-A → PC-B", "Оба узла за E1: мост не передаёт<br>кадр в другой сегмент.", "bridge_fwd_no.png", "left:1560px;top:685px;width:72px"),
]), '<div class="ab" style="left:460px;top:858px;font-size:23px;color:#fff">Неизвестный адрес назначения &nbsp;— &nbsp;рассылка во все порты, кроме входного.</div>',
    '<svg class="ab brf-glow" style="left:800px;top:478px" width="70" height="30" viewBox="0 0 70 30"><path d="M2 15 H58 M46 4 L64 15 L46 26" fill="none" stroke="#ffb02e" stroke-width="4"/></svg>')
