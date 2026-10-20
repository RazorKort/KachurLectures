# -*- coding: utf-8 -*-
"""COLL_DOMAINS — домены коллизий: вёрстка 1:1 инфографики (pptx 10)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 94

CSS = """<style>
.cd-pan{position:absolute;border-radius:10px;border:1.5px solid rgba(42,212,255,.6);background:rgba(6,20,52,.86);box-shadow:0 0 16px rgba(42,212,255,.35)}
.cd-os{font-family:Oswald,sans-serif;font-weight:500}
.cd-tx{position:absolute;color:#eef3ff;font-family:'Golos Text',sans-serif;font-size:26px;line-height:32px}
.cd-tx em{color:#2ad4ff;font-style:normal;font-weight:700}
.cd-num{position:absolute;top:513px;width:40px;height:40px;border-radius:50%;border:2px solid #2ad4ff;background:#071a3c;box-shadow:0 0 10px #2ad4ff;
  display:flex;align-items:center;justify-content:center;font-family:Oswald,sans-serif;font-weight:600;font-size:26px;color:#fff}
.cd-lb{position:absolute;top:648px;text-align:center;font-size:23px;line-height:27px;color:#eef3ff}
.cd-ar{position:absolute;top:582px;color:#2ad4ff;font-size:26px}
.cd-sl{position:absolute;top:842px;width:110px;text-align:center;font-size:17px;line-height:20px;color:#eef3ff}
.cd-ck{position:absolute;left:1406px;width:192px;padding-left:40px;font-size:16px;white-space:nowrap;line-height:21px;color:#eef3ff}
.cd-ck:before{content:"✓";position:absolute;left:0;top:2px;width:24px;height:24px;border-radius:50%;border:2px solid #2ad4ff;color:#2ad4ff;font-size:15px;line-height:22px;text-align:center}
@keyframes cd-flash{0%,100%{filter:brightness(1)}50%{filter:brightness(1.5) drop-shadow(0 0 12px #ff4d5e)}}
.cd-boom{animation:cd-flash 1.2s ease-in-out infinite}
</style>"""

STEPS = [("coll_domains_s1.png", "Прослушать<br>среду", 86, 52), ("coll_domains_s2.png", "Начать<br>передачу", 268, 52),
         ("coll_domains_s3.png", "Обнаружить<br>коллизию", 453, 54), ("coll_domains_s4.png", "Подождать<br>случайное время<br>и повторить", 658, 54)]


def _steps():
    out = []
    for k, (ic, t, x, half) in enumerate(STEPS):
        out.append('<div class="step" style="transition-delay:%dms">%s<div class="cd-num" style="left:%dpx">%d</div>'
                   '<div class="cd-lb" style="left:%dpx;width:220px">%s</div>%s</div>'
                   % (k * 150, img("rep/" + ic, "left:%dpx;top:543px;width:%dpx" % (x, 106 if k < 2 else 109), "ab"),
                      x + half - 22, k + 1, x + half - 110, t,
                      '<div class="cd-ar" style="left:%dpx">→</div>' % (x + 134) if k < 3 else ""))
    return "".join(out)


HTML = CSS + f"""
<div class="cd-pan" style="left:34px;top:142px;width:804px;height:613px"></div>
<div class="step">
  <div class="cd-tx" style="left:62px;top:168px;width:760px"><em>Коллизия</em> — одновременная передача двух устройств в общей среде. Сигналы накладываются, и кадры повреждаются.</div>
</div>
<div class="step">
  <div class="ab cd-os" style="left:62px;top:283px;width:753px;height:69px;border-radius:10px;border:2px solid #2ad4ff;background:rgba(8,40,90,.7);
    box-shadow:0 0 14px rgba(42,212,255,.6);display:flex;align-items:center;justify-content:center;font-size:33px;color:#2ad4ff">ОДИН ОБЩИЙ СЕГМЕНТ = ОДИН ДОМЕН КОЛЛИЗИЙ</div>
  <div class="cd-tx" style="left:62px;top:372px;width:760px">Чем больше устройств, тем чаще коллизии и ниже полезная пропускная способность.</div>
</div>
<div class="step">
  <div class="ab cd-os" style="left:62px;top:458px;font-size:40px;line-height:52px;font-weight:700;color:#2ad4ff">CSMA/CD</div>
  <div class="ab" style="left:270px;top:482px;width:545px;height:2px;background:linear-gradient(90deg,#2ad4ff,rgba(42,212,255,.3))"></div>
</div>
{_steps()}
<div class="step">
  <div class="cd-pan" style="left:34px;top:767px;width:804px;height:126px"></div>
  {img("rep/coll_domains_hd.png", "left:56px;top:783px;width:124px", "ab")}
  <div class="cd-tx" style="left:206px;top:792px;font-size:27px"><b class="cd-os" style="color:#2ad4ff;font-size:30px">ПОЛУДУПЛЕКС:</b> устройство либо передаёт,<br>либо принимает.</div>
</div>

<div class="step">
  <div class="ab" style="left:820px;top:190px">{img("rep/coll_domains_art.png", "width:852px")}</div>
  <div class="ab" style="left:985px;top:100px;width:524px;height:84px;border-radius:10px;border:2px solid #2ad4ff;background:rgba(6,24,60,.88);
    box-shadow:0 0 16px rgba(42,212,255,.6);text-align:center">
    <div style="font-size:25px;line-height:32px;color:#fff;margin-top:8px">Общий сегмент (коаксиальный кабель)</div>
    <div class="cd-os" style="font-size:28px;line-height:34px;color:#2ad4ff">ОДИН ДОМЕН КОЛЛИЗИЙ</div></div>
</div>
<div class="step">
  <div class="cd-pan" style="left:876px;top:612px;width:766px;height:281px"></div>
  <div class="ab cd-os" style="left:902px;top:620px;font-size:25px;color:#2ad4ff">КОММУТАТОР РАЗДЕЛЯЕТ ДОМЕНЫ КОЛЛИЗИЙ</div>
  {img("rep/coll_domains_sw.png", "left:905px;top:655px;width:470px", "ab")}
  <div class="cd-sl" style="left:884px">Свой домен<br>коллизий</div>
  <div class="cd-sl" style="left:1013px">Свой домен<br>коллизий</div>
  <div class="cd-sl" style="left:1138px">Свой домен<br>коллизий</div>
  <div class="cd-sl" style="left:1264px">Свой домен<br>коллизий</div>
</div>
<div class="step">
  <div class="ab" style="left:1393px;top:657px;width:237px;height:223px;border-radius:10px;border:1.5px solid #2ad4ff;background:rgba(8,30,70,.85);box-shadow:0 0 10px rgba(42,212,255,.4)"></div>
  <div class="cd-ck" style="top:676px">Каждый порт —<br>отдельный домен<br>коллизий.</div>
  <div class="cd-ck" style="top:754px">Коллизии между<br>портами не возникают.</div>
  <div class="cd-ck" style="top:814px">Возможен<br>полнодуплекс.</div>
</div>
"""
