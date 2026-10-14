# -*- coding: utf-8 -*-
"""Стеклянный стиль деки RIP: матовое стекло поверх живого градиента.

Концепция та же, что на референс-инфографиках (заглавный блок, нумерованные панели,
цепочка маршрутизаторов, пастельные акценты), но сборка другая: стеклянные панели
с подсветкой по верхней кромке, крупный номер-водяной знак в шапке и бенто-ритм сетки.
"""

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
--bg:#eaf6f2; --ink:#10332b; --dim:#55736b;
--title:#0d5c40; --green:#1f9c6b; --mint:#7ad7b2; --aqua:#56c7d6;
--pink:#ef9ec4; --pink-ink:#b94574; --blue:#8fb6ee; --blue-ink:#3a6cb4;
--lav:#b9adec; --lav-ink:#6353b8;
--glass:rgba(255,255,255,.58);
--glass-2:rgba(255,255,255,.38);
--glass-line:rgba(255,255,255,.85);
--glass-edge:rgba(23,110,82,.13);
--shadow:0 18px 48px rgba(16,70,54,.14), 0 2px 8px rgba(16,70,54,.07);
--r:26px; --r2:16px; --r3:999px;
--ease:cubic-bezier(.22,.7,.3,1);
--f:"Montserrat","Segoe UI Variable Display","Segoe UI",Inter,system-ui,-apple-system,Arial,sans-serif;
--m:"Cascadia Mono","JetBrains Mono",Consolas,"SF Mono",ui-monospace,monospace;
}
html,body{height:100%}
body{font-family:var(--f);color:var(--ink);background:var(--bg);overflow:hidden;
-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* ---------- сцена ---------- */
#bg{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}
#stage{position:fixed;inset:0;z-index:1}
.slide{position:absolute;inset:0;padding:clamp(20px,2vw,40px) clamp(22px,2.8vw,54px) 76px;
 display:none;overflow:hidden;flex-direction:column}
.slide.on{display:flex}
.slide>.sc{flex:1;min-height:0;overflow:auto;padding:2px 8px 2px 2px;scrollbar-width:thin;
 scrollbar-color:rgba(31,156,107,.35) transparent;display:flex;flex-direction:column;gap:16px}
.slide>.sc::-webkit-scrollbar{width:8px}
.slide>.sc::-webkit-scrollbar-thumb{background:rgba(31,156,107,.3);border-radius:8px}
.slide>.sc>.g{flex:1 1 auto;align-content:stretch}
.slide>.sc>.g.fix{flex:0 0 auto}
.slide>.sc>.step{flex:0 0 auto}
.g>.step{display:flex;flex-direction:column;min-height:0}
.g>.step>.c{flex:1 1 auto}
.g>.c{height:100%}
.col{display:flex;flex-direction:column;gap:16px;min-width:0}

/* ---------- шапка: номер-водяной знак слева ---------- */
.head{flex:none;margin-bottom:2px;display:flex;align-items:flex-start;gap:18px;position:relative}
.head .mark{flex:none;width:12px;height:72px;border-radius:999px;margin-top:6px;
 background:linear-gradient(180deg,var(--aqua),var(--green));
 box-shadow:0 6px 18px rgba(31,156,107,.35)}
h1.t{font-size:clamp(21px,2.3vw,43px);font-weight:900;line-height:.96;color:var(--title);
 text-transform:uppercase;letter-spacing:-.012em;
 text-shadow:0 1px 0 rgba(255,255,255,.65)}
.ul{height:6px;border-radius:999px;margin-top:12px;width:clamp(140px,18vw,280px);
 background:linear-gradient(90deg,var(--green),var(--aqua) 45%,var(--lav) 78%,var(--pink));
 box-shadow:0 4px 14px rgba(86,199,214,.4)}
p.sub{margin-top:11px;font-size:clamp(13px,1.02vw,20px);color:var(--dim);line-height:1.44;
 max-width:1120px}

/* ---------- стеклянная панель ---------- */
.c{position:relative;display:flex;flex-direction:column;border-radius:var(--r);
 padding:clamp(16px,1.2vw,24px) clamp(18px,1.3vw,26px);
 background:linear-gradient(145deg,rgba(255,255,255,.72),rgba(255,255,255,.42));
 backdrop-filter:blur(22px) saturate(1.45);-webkit-backdrop-filter:blur(22px) saturate(1.45);
 border:1px solid var(--glass-edge);box-shadow:var(--shadow);
 transition:transform .25s var(--ease),box-shadow .25s var(--ease)}
.c::before{content:"";position:absolute;inset:0;border-radius:var(--r);pointer-events:none;
 border-top:1.5px solid var(--glass-line);border-left:1px solid rgba(255,255,255,.6);
 -webkit-mask:linear-gradient(#000,transparent 55%);mask:linear-gradient(#000,transparent 55%)}
.c:hover{transform:translateY(-3px);box-shadow:0 26px 60px rgba(16,70,54,.18),0 3px 10px rgba(16,70,54,.08)}
.c.soft{background:linear-gradient(145deg,rgba(255,255,255,.52),rgba(255,255,255,.3))}
.ch{display:flex;align-items:center;gap:13px;margin-bottom:12px}
.ch h3{font-size:clamp(14px,1.06vw,22px);font-weight:900;line-height:1.08;color:var(--title);
 text-transform:uppercase;letter-spacing:.005em}
.ch h3.mix{text-transform:none;font-weight:800}
.num{flex:none;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;
 font:900 17px/1 var(--f);color:#fff;
 background:linear-gradient(145deg,var(--aqua),var(--green));
 box-shadow:0 6px 16px rgba(31,156,107,.4),inset 0 1.5px 0 rgba(255,255,255,.75)}
.num.sm{width:31px;height:31px;font-size:14px}
.c p{font-size:clamp(12.5px,.9vw,17.5px);line-height:1.52;color:var(--ink)}
.c p+p{margin-top:9px}
.c p.d{color:var(--dim)}
.c h4{font-size:clamp(13px,.88vw,17px);font-weight:800;color:var(--title);margin-bottom:9px;
 text-transform:uppercase;letter-spacing:.03em}
.hr{height:1px;background:linear-gradient(90deg,rgba(23,110,82,.22),rgba(23,110,82,0));
 margin:12px 0 11px}
.c svg.fig{width:100%;display:block;margin:4px auto 0}

/* ---------- плашки ---------- */
.tag{display:inline-block;padding:7px 15px;border-radius:var(--r3);
 font:800 clamp(11.5px,.8vw,15px) var(--f);line-height:1.25;
 background:rgba(255,255,255,.6);color:#166b4b;border:1px solid rgba(255,255,255,.8);
 box-shadow:0 4px 14px rgba(16,70,54,.1)}
.tag.p{color:var(--pink-ink)}
.tag.b{color:var(--blue-ink)}
.tag.v{color:var(--lav-ink)}
.tag.mono{font-family:var(--m);font-weight:700}
.tags{display:flex;gap:9px;flex-wrap:wrap}

/* ---------- строка с иконкой: стеклянная пилюля ---------- */
.ir{display:flex;align-items:center;gap:13px;border-radius:var(--r2);padding:10px 14px;
 background:rgba(255,255,255,.44);border:1px solid rgba(255,255,255,.6)}
.ir+.ir{margin-top:9px}
.ir .ib{flex:none;width:34px;height:34px;border-radius:12px;display:grid;place-items:center;
 background:linear-gradient(150deg,rgba(255,255,255,.95),rgba(255,255,255,.65));
 box-shadow:0 4px 12px rgba(16,70,54,.14),inset 0 1px 0 #fff}
.ir .ib svg{width:18px;height:18px;fill:none;stroke:var(--green);stroke-width:1.7;
 stroke-linecap:round;stroke-linejoin:round}
.ir.p .ib svg{stroke:var(--pink-ink)}
.ir.b .ib svg{stroke:var(--blue-ink)}
.ir.v .ib svg{stroke:var(--lav-ink)}
.ir span{font-size:clamp(12.5px,.88vw,17px);line-height:1.4;color:var(--ink)}
.ir b{color:var(--title)}

/* ---------- списки ---------- */
ul.ck{list-style:none;display:flex;flex-direction:column;gap:10px}
ul.ck li{display:flex;gap:12px;align-items:flex-start;font-size:clamp(12.5px,.88vw,17px);
 line-height:1.44;color:var(--ink)}
ul.ck li::before{content:"";flex:none;width:20px;height:20px;border-radius:50%;margin-top:1px;
 box-shadow:0 3px 9px rgba(31,156,107,.35);
 background:linear-gradient(145deg,var(--mint),var(--green)) ,
  url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M5 13l4 4 10-10' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/></svg>") center/13px no-repeat}
ul.ck.no li::before{background:linear-gradient(145deg,#f7b7d2,var(--pink-ink)),
  url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M6 12h12' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round'/></svg>") center/13px no-repeat;
  box-shadow:0 3px 9px rgba(185,69,116,.3)}
ul.ck.dot li::before{background:linear-gradient(145deg,#b9d4f7,var(--blue-ink))}

/* ---------- сетки: бенто-ритм ---------- */
.g{display:grid;gap:16px}
.g>*{min-width:0}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.g21{grid-template-columns:2fr 1fr}
.g12{grid-template-columns:1fr 2fr}
.g32{grid-template-columns:3fr 2fr}
.g23{grid-template-columns:2fr 3fr}
@media (min-width:1280px){
 .g3>*:nth-child(2),.g4>*:nth-child(2),.g4>*:nth-child(4){margin-top:14px}
}

/* ---------- таблица ---------- */
.tw{overflow:auto;border-radius:var(--r2);border:1px solid var(--glass-edge);
 background:rgba(255,255,255,.5);backdrop-filter:blur(14px);box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;font-size:clamp(12px,.88vw,17px)}
th,td{padding:11px 16px;text-align:left;border-bottom:1px solid rgba(23,110,82,.1);color:var(--ink)}
th{background:linear-gradient(180deg,rgba(255,255,255,.9),rgba(255,255,255,.55));
 color:var(--title);font-weight:800;position:sticky;top:0;backdrop-filter:blur(10px);
 font-size:clamp(11.5px,.82vw,15.5px);text-transform:uppercase;letter-spacing:.03em}
tr:last-child td{border-bottom:none}
tbody tr:hover td{background:rgba(255,255,255,.45)}
td.mono,th.mono{font-family:var(--m);font-weight:700}
td .g1{color:#166b4b;font-weight:800}
td .r1{color:var(--pink-ink);font-weight:800}
td.c,th.c{text-align:center}
tr.hot td{background:rgba(239,158,196,.18)}
tr.new td{background:rgba(122,215,178,.2)}

/* ---------- CLI: тёмное стекло ---------- */
.cli{border-radius:var(--r2);padding:15px 18px;overflow-x:auto;
 background:linear-gradient(150deg,rgba(8,46,36,.92),rgba(10,58,52,.86));
 border:1px solid rgba(255,255,255,.14);
 box-shadow:0 18px 40px rgba(8,46,36,.3),inset 0 1px 0 rgba(255,255,255,.18)}
.cli pre{font:600 clamp(11.5px,.82vw,15.5px)/1.65 var(--m);color:#dcf6ea;white-space:pre}
.cli .pr{color:#7ad7b2}
.cli .cm{color:#ffffff}
.cli .rem{color:#8fb0a4;font-style:italic}
.cli .cur{display:inline-block;width:8px;height:1.05em;vertical-align:-2px;background:#7ad7b2;
 animation:bl 1s steps(1) infinite}
@keyframes bl{50%{opacity:0}}

/* ---------- выноска ---------- */
.bub{position:relative;border-radius:var(--r2);padding:12px 16px;display:inline-block;
 background:rgba(255,255,255,.6);color:#166b4b;border:1px solid rgba(255,255,255,.75);
 font:700 clamp(12px,.85vw,16px)/1.35 var(--f);box-shadow:var(--shadow)}
.bub.p{color:var(--pink-ink)}
.bub.b{color:var(--blue-ink)}
.bub.v{color:var(--lav-ink)}

/* ---------- сноска ---------- */
.foot{display:flex;align-items:center;gap:16px;margin-top:2px;flex:none}
.foot i{flex:1;height:1px;font-style:normal}
.foot i:first-child{background:linear-gradient(90deg,rgba(23,110,82,0),rgba(23,110,82,.25))}
.foot i:last-child{background:linear-gradient(90deg,rgba(23,110,82,.25),rgba(23,110,82,0))}
.foot span{font-size:clamp(11px,.76vw,14px);color:var(--dim);white-space:nowrap}

/* ---------- шаги ---------- */
.step{opacity:0;transform:translateY(14px) scale(.985);
 transition:opacity .34s var(--ease),transform .34s var(--ease)}
.step.vis{opacity:1;transform:none}
.dash{stroke-dasharray:var(--L);stroke-dashoffset:var(--L);transition:stroke-dashoffset .75s var(--ease)}
.vis .dash,.dash.go{stroke-dashoffset:0}
.fade{opacity:0;transition:opacity .45s var(--ease)}
.fade.go{opacity:1}

/* ---------- титул ---------- */
.cover{display:flex;flex-direction:column;justify-content:center;height:100%;gap:18px;
 max-width:1180px}
.cover h1{font-size:clamp(32px,5.4vw,90px);font-weight:900;line-height:.92;color:var(--title);
 text-transform:uppercase;letter-spacing:-.02em;text-shadow:0 2px 0 rgba(255,255,255,.6)}
.cover .ul{width:clamp(200px,30vw,480px);height:10px;margin-top:6px}
.cover .meta{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px}

/* ---------- тренажёр ---------- */
.ui{display:flex;gap:11px;align-items:center;flex-wrap:wrap}
.ui button,.btn{font:800 clamp(12px,.85vw,15.5px) var(--f);color:#fff;border:0;cursor:pointer;
 background:linear-gradient(145deg,var(--aqua),var(--green));border-radius:var(--r3);
 padding:11px 19px;box-shadow:0 8px 20px rgba(31,156,107,.32),inset 0 1px 0 rgba(255,255,255,.6);
 transition:.2s var(--ease)}
.ui button:hover,.btn:hover{transform:translateY(-2px);box-shadow:0 12px 26px rgba(31,156,107,.4)}
.ui button.gh{background:rgba(255,255,255,.55);color:var(--title);
 border:1px solid rgba(255,255,255,.8);box-shadow:0 5px 14px rgba(16,70,54,.1)}
.ui button.gh.on{background:linear-gradient(145deg,rgba(122,215,178,.55),rgba(86,199,214,.4));
 color:#0d5c40}
.ui .lab{font-size:clamp(12px,.84vw,15.5px);color:var(--dim)}
.rt{display:grid;gap:10px;font:700 clamp(11px,.78vw,14.5px)/1.3 var(--m)}
.rt .rw{display:grid;grid-template-columns:1fr auto auto;gap:9px;align-items:center;
 background:rgba(255,255,255,.5);border:1px solid rgba(255,255,255,.7);border-radius:14px;
 padding:9px 13px;transition:.3s var(--ease)}
.rt .rw.upd{background:linear-gradient(145deg,rgba(122,215,178,.5),rgba(86,199,214,.3));
 border-color:rgba(31,156,107,.5)}
.rt .rw.inf{background:rgba(239,158,196,.26);border-color:rgba(185,69,116,.35);
 color:var(--pink-ink)}
.rt .rw b{color:var(--title)}
.big{font:900 clamp(22px,2.4vw,42px)/1 var(--m);
 background:linear-gradient(145deg,var(--aqua),var(--green));-webkit-background-clip:text;
 background-clip:text;color:transparent}

/* ---------- квиз ---------- */
.q{border-radius:var(--r);padding:17px 20px;
 background:linear-gradient(145deg,rgba(255,255,255,.7),rgba(255,255,255,.42));
 backdrop-filter:blur(22px) saturate(1.4);border:1px solid var(--glass-edge);
 box-shadow:var(--shadow)}
.q .qt{display:flex;gap:12px;align-items:flex-start;font-weight:800;color:var(--title);
 font-size:clamp(13.5px,.98vw,19px);margin-bottom:12px;line-height:1.3}
.q .opts{display:grid;gap:8px}
.q button{text-align:left;font:600 clamp(12.5px,.86vw,16.5px) var(--f);padding:12px 16px;
 border-radius:14px;border:1px solid rgba(255,255,255,.7);background:rgba(255,255,255,.45);
 color:var(--ink);cursor:pointer;transition:.18s var(--ease)}
.q button:hover{background:rgba(255,255,255,.75);transform:translateX(3px)}
.q button.good{background:linear-gradient(145deg,rgba(122,215,178,.6),rgba(86,199,214,.35));
 border-color:rgba(31,156,107,.55);color:#0d5c40;font-weight:800}
.q button.bad{background:rgba(239,158,196,.3);border-color:rgba(185,69,116,.4);
 color:var(--pink-ink)}
.q .ex{display:none;margin-top:12px;padding-top:11px;
 border-top:1px solid rgba(23,110,82,.15);
 font-size:clamp(12.5px,.86vw,16.5px);line-height:1.46;color:var(--dim)}
.q .ex.on{display:block}
#score{font:900 15px var(--m);color:var(--green)}

/* ---------- HUD ---------- */
#hud{position:fixed;left:0;right:0;bottom:0;height:56px;z-index:5;display:flex;align-items:center;
 gap:10px;padding:0 20px;background:rgba(255,255,255,.55);
 backdrop-filter:blur(26px) saturate(1.5);border-top:1px solid rgba(255,255,255,.8)}
#prog{position:fixed;left:0;bottom:56px;height:3px;z-index:6;transition:width .3s var(--ease);
 background:linear-gradient(90deg,var(--green),var(--aqua),var(--lav),var(--pink))}
#hud button{font:700 13px var(--f);color:var(--title);background:rgba(255,255,255,.6);
 border:1px solid rgba(255,255,255,.85);border-radius:var(--r3);padding:8px 15px;cursor:pointer;
 transition:.2s var(--ease)}
#hud button:hover{background:linear-gradient(145deg,var(--aqua),var(--green));color:#fff;
 border-color:transparent;transform:translateY(-2px);box-shadow:0 8px 18px rgba(31,156,107,.3)}
#count{font:800 13.5px var(--m);color:var(--green);min-width:116px}
#sname{font-size:13px;color:var(--dim);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
:focus-visible{outline:3px solid var(--aqua);outline-offset:2px;border-radius:10px}

/* ---------- содержание ---------- */
#toc{position:fixed;inset:0;z-index:20;background:rgba(234,246,242,.8);
 backdrop-filter:blur(26px) saturate(1.3);display:none;padding:40px 48px;overflow:auto}
#toc.on{display:block}
#toc h2{color:var(--title);font-size:25px;margin-bottom:20px;font-weight:900;
 text-transform:uppercase;letter-spacing:.02em}
#tocg{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:11px}
.tocit{display:flex;gap:12px;align-items:center;text-align:left;padding:12px 14px;
 border-radius:16px;background:rgba(255,255,255,.55);border:1px solid rgba(255,255,255,.8);
 color:var(--ink);font:600 13px var(--f);cursor:pointer;transition:.2s var(--ease);
 box-shadow:0 6px 16px rgba(16,70,54,.08)}
.tocit:hover{background:rgba(255,255,255,.9);transform:translateY(-3px);
 box-shadow:0 12px 26px rgba(16,70,54,.14)}
.tocit i{font:900 12px/1 var(--m);font-style:normal;color:#fff;min-width:26px;height:26px;
 border-radius:50%;display:grid;place-items:center;
 background:linear-gradient(145deg,var(--aqua),var(--green));
 box-shadow:inset 0 1px 0 rgba(255,255,255,.7)}

/* ---------- адаптив ---------- */
#hud .hint{display:inline;font-size:11.5px;color:var(--dim)}
@media (max-width:1320px){#hud .hint{display:none}}
@media (max-width:1279px){
 .g4,.g3{grid-template-columns:repeat(2,1fr)}
 .slide{padding:18px 22px 66px}
}
@media (max-width:1099px){.g2,.g21,.g12,.g32,.g23{grid-template-columns:1fr}}
@media (max-width:640px){
 .g,.g2,.g3,.g4,.g21,.g12,.g32,.g23{grid-template-columns:1fr}
 .g3>*,.g4>*{margin-top:0!important}
 h1.t{font-size:25px}
 .cover h1{font-size:32px}
 .slide{padding:15px 14px 62px}
 #sname{display:none}
 #bg .leaf{display:none}
 .figwrap{overflow-x:auto}
}
@media (prefers-reduced-motion:reduce){
 .step{opacity:1!important;transform:none!important;transition:none}
 .dash{stroke-dashoffset:0!important;transition:none}
 .fade{opacity:1!important;transition:none}
 .cli .cur{animation:none}
 .c:hover{transform:none}
}
"""


# ======================================================================
#  Сцена: градиентная аврора, стеклянные пластины, листья
# ======================================================================
def background():
    leaves = []
    spots = [
        (-30, 110, 1.3, -26, .34), (-56, 300, 1.7, 16, .26),
        (-16, 500, 1.1, -50, .30), (-40, 700, 1.5, 26, .22),
        (1364, 90, 1.4, 196, .32), (1398, 270, 1.7, 164, .25),
        (1356, 470, 1.15, 212, .29), (1390, 680, 1.55, 150, .22),
    ]
    for (x, y, s, rot, op) in spots:
        leaves.append('<use href="#gleaf" class="leaf" transform="translate(%d %d) rotate(%d) '
                      'scale(%.2f)" opacity="%.2f"/>' % (x, y, rot, s, op))

    plates = []
    for (x, y, w, h, rot, op) in [(120, 520, 320, 190, -12, .28), (980, 120, 300, 180, 9, .24),
                                  (620, 640, 380, 170, -5, .20), (1060, 520, 260, 150, 14, .22)]:
        plates.append('<rect x="%d" y="%d" width="%d" height="%d" rx="34" fill="url(#gpl)" '
                      'opacity="%.2f" transform="rotate(%d %d %d)" stroke="rgba(255,255,255,.55)" '
                      'stroke-width="1.5"/>' % (x, y, w, h, op, rot, x + w / 2, y + h / 2))

    dots = []
    for (x, y, w, h) in [(330, 150, 86, 60), (1080, 380, 74, 50), (520, 790, 100, 52)]:
        dots.append('<rect x="%d" y="%d" width="%d" height="%d" fill="url(#gdot)" opacity=".5"/>'
                    % (x, y, w, h))

    return """<svg id="bg" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs>
  <linearGradient id="gsky" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#e6f7f1"/><stop offset=".45" stop-color="#eaf4fb"/>
    <stop offset="1" stop-color="#f6eefa"/>
  </linearGradient>
  <radialGradient id="o1"><stop offset="0" stop-color="#5fd3b2" stop-opacity=".62"/><stop offset="1" stop-color="#5fd3b2" stop-opacity="0"/></radialGradient>
  <radialGradient id="o2"><stop offset="0" stop-color="#f2a9cd" stop-opacity=".55"/><stop offset="1" stop-color="#f2a9cd" stop-opacity="0"/></radialGradient>
  <radialGradient id="o3"><stop offset="0" stop-color="#9fb8f2" stop-opacity=".55"/><stop offset="1" stop-color="#9fb8f2" stop-opacity="0"/></radialGradient>
  <radialGradient id="o4"><stop offset="0" stop-color="#64cfdd" stop-opacity=".5"/><stop offset="1" stop-color="#64cfdd" stop-opacity="0"/></radialGradient>
  <linearGradient id="gpl" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#ffffff" stop-opacity=".75"/>
    <stop offset="1" stop-color="#ffffff" stop-opacity=".15"/>
  </linearGradient>
  <linearGradient id="glf" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#93dcbe"/><stop offset="1" stop-color="#d6f1ea"/>
  </linearGradient>
  <pattern id="gdot" width="14" height="14" patternUnits="userSpaceOnUse">
    <circle cx="3" cy="3" r="2" fill="#9fd9c3"/>
  </pattern>
  <g id="gleaf">
    <path d="M0 0 C 26 -34 74 -34 100 0 C 74 34 26 34 0 0 Z" fill="url(#glf)"/>
    <path d="M2 0 H98" stroke="#7fc9ab" stroke-width="1.6" fill="none"/>
    <path d="M26 -2 C 38 -12 46 -16 58 -17" stroke="#7fc9ab" stroke-width="1.2" fill="none"/>
    <path d="M46 -2 C 58 -11 66 -14 78 -15" stroke="#7fc9ab" stroke-width="1.2" fill="none"/>
    <path d="M26 2 C 38 12 46 16 58 17" stroke="#7fc9ab" stroke-width="1.2" fill="none"/>
    <path d="M46 2 C 58 11 66 14 78 15" stroke="#7fc9ab" stroke-width="1.2" fill="none"/>
  </g>
</defs>
<rect width="1440" height="900" fill="url(#gsky)"/>
<ellipse cx="260" cy="120" rx="400" ry="290" fill="url(#o1)"/>
<ellipse cx="1210" cy="740" rx="420" ry="300" fill="url(#o4)"/>
<ellipse cx="1180" cy="120" rx="330" ry="250" fill="url(#o2)"/>
<ellipse cx="280" cy="820" rx="360" ry="240" fill="url(#o3)"/>
<ellipse cx="730" cy="430" rx="460" ry="330" fill="url(#o1)" opacity=".45"/>
%s
%s
%s
</svg>""" % ("\n".join(plates), "\n".join(dots), "\n".join(leaves))
