# -*- coding: utf-8 -*-
"""BRIDGE_SPLIT — мост разделяет домены коллизий: вёрстка 1:1 (pptx 16)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 146   # «Сетевой мост / Разделение доменов коллизий» даёт head()

CSS = """<style>
.bsp-dom{position:absolute;border:2.5px dashed #2ad4ff;border-radius:22px;background:rgba(6,40,90,.25)}
.bsp-dom.m{border-color:#e05cff;background:rgba(60,16,100,.28)}
.bsp-dh{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:33px;color:#2ad4ff;text-shadow:0 0 10px rgba(42,212,255,.6)}
.bsp-pan{position:absolute;border-radius:10px;border:2px solid #2ad4ff;background:linear-gradient(180deg,rgba(8,44,96,.75),rgba(4,20,54,.88));
  box-shadow:0 0 14px rgba(42,212,255,.5),inset 0 0 22px rgba(42,212,255,.14)}
.bsp-pan.m{border-color:#b06bff;background:linear-gradient(180deg,rgba(50,20,110,.78),rgba(24,10,66,.88));box-shadow:0 0 14px rgba(176,107,255,.55),inset 0 0 22px rgba(176,107,255,.16)}
.bsp-num{position:absolute;width:62px;height:62px;border-radius:9px;border:2.5px solid #2ad4ff;background:rgba(6,30,70,.9);box-shadow:0 0 12px rgba(42,212,255,.7);
  display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:700;font-size:44px;color:#fff}
.bsp-num.m{border-color:#e05cff;box-shadow:0 0 12px rgba(224,92,255,.8)}
.bsp-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;font-size:30px;line-height:1;color:#2ad4ff}
.bsp-t{position:absolute;font-size:21px;line-height:1.33;color:#fff}
.bsp-f{-webkit-mask-image:linear-gradient(90deg,transparent,#000 4%,#000 96%,transparent),linear-gradient(180deg,transparent,#000 4%,#000 96%,transparent);-webkit-mask-composite:source-in;mask-composite:intersect}
.bsp-e{position:absolute;font-family:Oswald,sans-serif;font-weight:500;font-size:25px;color:#fff}
.bsp-pulse{animation:bspP 1.1s ease-in-out infinite}
@keyframes bspP{50%{opacity:.4;transform:scale(.97)}}
</style>"""


def _card(x, w, cls, num, head, text, ico, ico_st, tx, ty):
    return ('<div class="step"><div class="bsp-pan %s" style="left:%dpx;top:706px;width:%dpx;height:204px"></div>'
            '<div class="bsp-num %s" style="left:%dpx;top:716px">%s</div>%s'
            '<div class="bsp-h" style="left:%dpx;top:722px;color:%s">%s</div>'
            '<div class="bsp-t" style="left:%dpx;top:%dpx">%s</div></div>'
            % (cls, x, w, cls, x + 16, num, img("rep/" + ico, ico_st, "ab bsp-f"), x + 102,
               "#ff6fe0" if cls == "m" else "#2ad4ff", head, tx, ty, text))


HTML = CSS + f"""
<div class="step">
  <div class="bsp-dom" style="left:22px;top:158px;width:664px;height:428px"></div>
  {img("rep/bridge_split_l.png", "left:30px;top:214px;width:580px", "ab bsp-f")}
  <div class="bsp-dh" style="left:210px;top:172px">Домен коллизий 1</div>
  <div class="ab bsp-pulse" style="transform-origin:425px 512px">{img("rep/bridge_split_coll.png", "left:312px;top:490px;width:226px", "ab bsp-f")}</div>
  <div class="ab os" style="left:282px;top:536px;font-weight:700;font-size:26px;color:#ff8a3d">Коллизия остаётся в 1</div>
</div>
<div class="step">
  <div class="bsp-dom m" style="left:986px;top:158px;width:664px;height:428px"></div>
  {img("rep/bridge_split_r.png", "left:1070px;top:214px;width:575px", "ab bsp-f")}
  <div class="bsp-dh" style="left:1185px;top:172px;color:#ff7af0;text-shadow:0 0 10px rgba(224,92,255,.6)">Домен коллизий 2</div>
  <div class="ab os" style="left:1108px;top:532px;font-weight:700;font-size:26px;color:#ff8ae8">Независимый сегмент 2</div>
</div>
<div class="step">
  {img("rep/bridge_split_m.png", "left:700px;top:258px;width:275px", "ab bsp-f")}
  <div class="ab os" style="left:700px;top:200px;width:275px;text-align:center;font-weight:700;font-size:21px;line-height:1.22;color:#ffc53d">Коллизии не проходят<br>через мост</div>
  <div class="bsp-e" style="left:665px;top:436px">E1</div><div class="bsp-e" style="left:975px;top:436px">E2</div>
</div>
<div class="step">
  <div class="bsp-pan" style="left:240px;top:616px;width:1192px;height:68px;border-radius:14px"></div>
  <div class="ab os" style="left:240px;top:620px;width:1192px;text-align:center;font-weight:700;font-size:40px;line-height:58px;color:#2ad4ff">
    <span style="color:#fff">2</span> подключённых порта моста <span style="color:#2ad4ff">→</span> <span style="color:#fff">2</span> домена коллизий</div>
</div>
{_card(22, 538, "", "1", "КОНЦЕНТРАТОР • L1", "Повторяет сигналы.<br>Все его порты —<br>один домен коллизий.", "bridge_split_hub.png", "left:66px;top:772px;width:224px", 308, 780)}
{_card(578, 510, "", "2", "МОСТ • L2", "Анализирует кадры<br>и MAC-адреса.<br>Разделяет коллизионные<br>домены.", "bridge_split_br.png", "left:626px;top:780px;width:190px", 838, 770)}
{_card(1106, 544, "m", "3", "КОММУТАТОР • L2", "Преемник моста:<br>коммутация кадров<br>между множеством<br>портов.", "bridge_split_sw.png", "left:1128px;top:768px;width:294px", 1440, 776)}
"""
