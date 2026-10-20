# -*- coding: utf-8 -*-
"""BRIDGE_PCAPCB — мост, передача внутри одного домена PC-A → PC-B: вёрстка 1:1 (pptx 15). Композиция из bridge_fwd.build()."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bridge_fwd import build, _card, W, H, TOP  # noqa: F401

MID = ('<div class="ab" style="left:680px;top:390px;width:120px;text-align:center;font-size:19px;line-height:1.15;color:#ff4d5e;background:rgba(6,18,46,.9)">Кадр<br>отфильтрован</div>'
       '<div class="ab" style="left:966px;top:396px;width:120px;text-align:center;font-size:18px;line-height:1.2;color:#fff;background:rgba(6,18,46,.9)">Кадр не<br>пересылается</div>')

HTML = build("bridge_pcapcb", "".join([
    _card(20, 506, "", "1", "ПОВТОРЕНИЕ", "Хаб H1 передаёт кадр<br>компьютеру PC-B и мосту B1.", "bridge_pcapcb_env.png", "left:434px;top:685px;width:72px"),
    _card(539, 550, "m", "2", "ФИЛЬТРАЦИЯ", "Адрес PC-B изучен на E1.<br>Кадр пришёл через E1 —<br>мост отбрасывает копию.", "bridge_pcapcb_env2.png", "left:984px;top:680px;width:80px"),
    _card(1106, 546, "", "3", "ОБУЧЕНИЕ", "Мост запоминает MAC-адрес<br>источника PC-A и порт E1.", "bridge_pcapcb_book.png", "left:1542px;top:680px;width:90px"),
]), '<div class="ab" style="left:474px;top:858px;font-size:23px;color:#5fe0ff">PC-B получает кадр внутри своего сегмента. Передача через E2 не нужна.</div>', MID, hl=1)
HTML = HTML.replace('top:732px">Адрес PC-B', 'top:726px;font-size:21px;line-height:1.28">Адрес PC-B')
