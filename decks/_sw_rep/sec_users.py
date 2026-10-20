# -*- coding: utf-8 -*-
"""Безопасность: создание и удаление учётных записей — вёрстка 1:1 (pptx 86)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from _sw_lib import img

W, H, TOP = 1672, 941, 246

CSS = """<style>
.su-p{position:absolute;border:2px solid #2ad4ff;border-radius:10px;background:rgba(6,22,60,.86);box-shadow:0 0 16px rgba(42,212,255,.45),inset 0 0 22px rgba(42,212,255,.1)}
.su-h{position:absolute;font-family:Oswald,sans-serif;font-weight:700;color:#fff;line-height:1;letter-spacing:.01em}
.su-tb{position:absolute;left:58px;top:330px;width:586px;border-collapse:collapse;color:#fff}
.su-tb th{height:46px;font-family:'Golos Text',sans-serif;font-weight:500;font-size:18px;border:1px solid rgba(42,212,255,.45);background:rgba(10,40,90,.6)}
.su-tb td{height:51px;font-size:23px;border:1px solid rgba(42,212,255,.3);text-align:center}
.su-tb td:first-child{text-align:left;padding-left:38px}
.su-lab{position:absolute;left:686px;color:#fff;font-size:16px}
.su-in{position:absolute;left:684px;width:308px;height:36px;border:1px solid rgba(42,212,255,.6);border-radius:4px;background:rgba(4,14,40,.9);
  box-sizing:border-box;padding-left:13px;font-size:15px;line-height:34px;color:#8ea6cc}
.su-bt{position:absolute;top:538px;width:150px;height:48px;border-radius:6px;font-family:Oswald,sans-serif;font-weight:700;font-size:20px;line-height:46px;
  text-align:center;color:#fff;box-sizing:border-box}
.su-ru{position:absolute;left:48px;width:372px;height:52px;border:1px solid rgba(42,212,255,.5);border-radius:6px;background:rgba(8,28,70,.8)}
.su-ru span{position:absolute;left:84px;top:0;height:52px;display:flex;align-items:center;color:#fff;font-size:16px;line-height:1.2}
.su-nm{position:absolute;left:434px;width:228px;height:96px;border:3px solid var(--c);border-radius:10px;background:var(--b);box-shadow:0 0 18px var(--c)}
.su-nm b{position:absolute;left:72px;top:10px;font-family:Oswald,sans-serif;font-size:32px;font-weight:500;color:#fff}
.su-nm i{position:absolute;left:0;width:100%;top:60px;text-align:center;font-style:normal;font-size:15px;color:#e6f1ff}
.su-val{position:absolute;left:870px;width:112px;height:36px;border:1px solid rgba(42,212,255,.5);border-radius:4px;background:rgba(10,40,90,.7);
  box-sizing:border-box;padding-left:10px;font-family:Oswald,sans-serif;font-weight:500;font-size:24px;line-height:32px;color:#2ad4ff}
.su-at{position:absolute;top:333px;width:182px;height:232px;border:2px solid rgba(42,212,255,.6);border-radius:8px;background:rgba(10,40,96,.6);text-align:center;color:#fff}
.su-at b{position:absolute;left:0;width:100%;font-family:Oswald,sans-serif;font-weight:700;font-size:20px;line-height:1.02}
.su-at i{position:absolute;left:0;width:100%;font-style:normal;font-size:15px;line-height:1.3;color:#e6f1ff}
.su-mc{position:absolute;top:713px;width:178px;height:150px;border:2px solid #2ad4ff;border-radius:8px;background:rgba(6,24,64,.9);box-shadow:0 0 12px rgba(42,212,255,.4)}
.su-mc small{position:absolute;left:52px;top:6px;font-size:11px;line-height:1.2;color:#fff}
.su-mi{position:absolute;left:10px;top:44px;width:154px;height:86px;border:2px solid #2ad4ff;border-radius:6px;font-size:13px;line-height:25px;color:#fff;padding:6px 0 0 10px;box-sizing:border-box}
.su-mi em{font-style:normal;color:#2ad4ff;font-weight:600;font-size:15px;position:absolute;left:72px}
.su-ar{position:absolute;top:780px;width:0;height:0;border:10px solid transparent;border-left:16px solid #2ad4ff;filter:drop-shadow(0 0 6px #2ad4ff)}
.su-x{position:absolute;left:1462px;top:770px;width:156px;height:3px;background:#ff3a6a;transform-origin:left;transform:rotate(24deg) scaleX(0);animation:suX 1s .6s forwards}
@keyframes suX{to{transform:rotate(24deg) scaleX(1)}}
.su-blink{animation:subl 1.4s ease-in-out infinite}
@keyframes subl{50%{opacity:.4}}
</style>"""


def mini(x, icon, t, rows, extra=""):
    r = "".join(f'{a}<em>{b}</em><br>' for a, b in rows)
    return (f'<div class="su-mc" style="left:{x}px">{extra}<small>{t}</small><div class="su-mi">{r}</div></div>'
            + img(f"rep/sec_users_{icon}.png", f"left:{x+12}px;top:716px;width:36px", "ab"))


HTML = CSS + f"""
<div class="step">
<div class="su-p" style="left:36px;top:268px;width:628px;height:290px"></div>
{img("rep/sec_users_grp.png", "left:53px;top:280px;width:49px", "ab")}
<div class="su-h" style="left:106px;top:283px;font-size:32px;font-family:'Golos Text',sans-serif;font-weight:700">Пользователи коммутатора</div>
<table class="su-tb"><tr><th style="width:216px">Имя пользователя</th><th style="width:212px">Уровень привилегий</th><th>Действия</th></tr>
<tr><td>admin</td><td>15</td><td></td></tr><tr><td>Admin1</td><td>15</td><td></td></tr><tr><td>admin1</td><td>1</td><td></td></tr></table>
{img("rep/sec_users_btn.png", "left:506px;top:383px;width:118px", "ab")}{img("rep/sec_users_btn.png", "left:506px;top:435px;width:118px", "ab")}
{img("rep/sec_users_btn.png", "left:506px;top:487px;width:118px", "ab")}
</div>

<div class="step">
<div class="su-p" style="left:668px;top:272px;width:340px;height:330px"></div>
{img("rep/sec_users_add.png", "left:678px;top:276px;width:49px", "ab")}
<div class="su-h" style="left:738px;top:290px;font-size:16px;font-family:'Golos Text',sans-serif">Создать нового пользователя</div>
<div class="su-lab" style="top:331px">Имя пользователя</div><div class="su-in" style="top:353px">Введите имя пользователя</div>
<div class="su-lab" style="top:400px">Пароль</div><div class="su-in" style="top:422px">Введите пароль<span style="position:absolute;right:12px;color:#cfe0ff">👁</span></div>
<div class="su-lab" style="top:468px">Уровень привилегий (1–15)</div><div class="su-in" style="top:488px;color:#fff">1<span style="position:absolute;right:12px">⌄</span></div>
<div class="su-bt" style="left:682px;background:linear-gradient(180deg,#1aa0ff,#0a60d8);border:2px solid #7fd8ff">+ &nbsp;СОЗДАТЬ</div>
<div class="su-bt" style="left:842px;background:linear-gradient(180deg,#e0306a,#a01848);border:2px solid #ff7aa0">🗑 &nbsp;УДАЛИТЬ</div>
</div>

<div class="step">
<div class="su-p" style="left:1018px;top:256px;width:620px;height:322px"></div>
<div class="su-h" style="left:1058px;top:282px;font-size:40px"><span style="color:#2ad4ff;font-size:46px">3</span> ОБЯЗАТЕЛЬНЫХ АТРИБУТА</div>
<div class="su-at" style="left:1042px"><b style="top:94px">ИМЯ<br>ПОЛЬЗОВАТЕЛЯ</b><i style="top:142px">Уникальное имя<br>для входа</i></div>
{img("rep/sec_users_a1.png", "left:1098px;top:348px;width:74px", "ab")}
<div class="su-at" style="left:1236px"><b style="top:98px">ПАРОЛЬ</b><i style="top:140px">Обеспечивает<br>защиту доступа</i></div>
{img("rep/sec_users_a2.png", "left:1288px;top:348px;width:74px", "ab")}
<div class="su-at" style="left:1428px;width:200px"><b style="top:82px">УРОВЕНЬ<br>ПРИВИЛЕГИЙ</b><i style="top:134px">Определяет права<br>пользователя</i>
 <div style="position:absolute;left:6px;top:182px;display:flex;gap:3px">{''.join('<span style="width:9px;height:14px;background:rgba(42,212,255,.55)"></span>' for _ in range(13))}</div>
 <div class="su-blink" style="position:absolute;left:162px;top:176px;width:28px;height:24px;border:2px solid #2ad4ff;background:#0a4a90;font-family:Oswald,sans-serif;font-size:17px;line-height:22px">15</div>
 <span style="position:absolute;left:6px;top:200px;font-size:14px">1</span><span style="position:absolute;left:170px;top:206px;font-size:14px">15</span></div>
{img("rep/sec_users_a3.png", "left:1488px;top:343px;width:69px", "ab")}
</div>

<div class="step">
<div class="su-p" style="left:36px;top:574px;width:628px;height:300px"></div>
{img("rep/sec_users_doc.png", "left:64px;top:588px;width:34px", "ab")}
<div class="su-h" style="left:120px;top:588px;font-size:30px">ПРАВИЛА ИМЕНИ ПОЛЬЗОВАТЕЛЯ</div>
<div class="su-ru" style="top:636px"><span>Латинские буквы: A–Z, a–z</span></div>{img("rep/sec_users_aa.png", "left:50px;top:638px;width:67px", "ab")}
<div class="su-ru" style="top:694px"><span>Разрешены специальные символы</span></div>{img("rep/sec_users_at.png", "left:50px;top:695px;width:67px", "ab")}
<div class="su-ru" style="top:752px"><span>Имя с пробелами указывается<br>в кавычках: “Network Admin”</span></div>{img("rep/sec_users_q.png", "left:50px;top:750px;width:67px", "ab")}
<div class="su-ru" style="top:810px"><span>Регистр важен: Admin1 ≠ admin1</span></div>{img("rep/sec_users_inf.png", "left:50px;top:808px;width:67px", "ab")}
<div class="su-nm" style="--c:#3dffb0;--b:rgba(6,50,60,.9);top:642px"><b>Admin1</b><i>Это один пользователь</i></div>
{img("rep/sec_users_pg.png", "left:453px;top:653px;width:44px", "ab")}
<div class="su-nm" style="--c:#ff4d8a;--b:rgba(60,10,40,.9);top:750px"><b>admin1</b><i>Это другой пользователь</i></div>
{img("rep/sec_users_pp.png", "left:453px;top:760px;width:44px", "ab")}
</div>

<div class="step">
<div class="su-p" style="left:690px;top:616px;width:308px;height:242px"></div>
{img("rep/sec_users_gear.png", "left:710px;top:623px;width:47px", "ab")}
<div class="su-h" style="left:768px;top:630px;font-size:30px">ПО УМОЛЧАНИЮ</div>
<div class="ab" style="left:704px;top:676px;width:286px;height:170px;border:1px solid rgba(42,212,255,.4);border-radius:8px"></div>
<div class="ab" style="left:720px;top:704px;font-size:18px;color:#fff">Имя:</div><div class="su-val" style="top:698px">admin</div>
<div class="ab" style="left:720px;top:750px;font-size:18px;color:#fff">Пароль:</div><div class="su-val" style="top:742px">admin</div>
<div class="ab" style="left:720px;top:796px;font-size:15px;color:#fff">Уровень привилегий:</div><div class="su-val" style="top:786px">15</div>
</div>

<div class="step">
<div class="ab" style="left:1020px;top:586px;width:618px;height:118px;border:2px solid #ff3a5e;border-radius:10px;background:rgba(70,10,30,.85);box-shadow:0 0 18px rgba(255,58,94,.55)"></div>
{img("rep/sec_users_warn.png", "left:1048px;top:598px;width:84px", "ab")}
<div class="ab" style="left:1158px;top:598px;font-family:'Golos Text',sans-serif;font-weight:700;font-size:23px;line-height:1.02;color:#fff">
<span style="color:#ff7a8a">Стандартная запись</span> <span style="color:#ff4d8a;font-size:27px">admin</span><br>перестаёт действовать после создания<br><span style="color:#ff7a8a">пе</span>рвой учётной записи с уровнем<br>привилегий <span style="color:#ff4d8a">15</span>.</div>
</div>
<div class="step">
{mini(1032, "l1", "Стандартная запись<br>(по умолчанию)", [("Имя:", "admin"), ("Пароль:", "admin"), ("Уровень:", "15")])}
<div class="su-ar" style="left:1208px"></div>
{mini(1240, "l2", "Создание новой<br>учётной записи", [("Имя:", "Admin1"), ("Пароль:", "••••••"), ("Уровень:", "15")])}
<div class="su-ar" style="left:1416px"></div>
{mini(1448, "l3", "Запись admin<br>становится неактивной", [("Имя:", "admin"), ("Пароль:", "admin"), ("Уровень:", "15")])}
<div class="ab" style="left:1448px;top:713px;width:178px;height:150px;background:rgba(0,0,0,.35);border-radius:8px"></div>
<div class="su-x"></div>
<div class="ab" style="left:1448px;top:844px;width:178px;text-align:center;font-family:Oswald,sans-serif;font-weight:700;font-size:16px;color:#ff3a6a">НЕАКТИВНА</div>
</div>
"""
