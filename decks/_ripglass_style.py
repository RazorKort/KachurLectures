# -*- coding: utf-8 -*-
"""Стеклянный стиль деки RIP: матовое стекло поверх тёмной аврора-сцены.

Концепция та же, что на референс-инфографиках (заглавный блок, нумерованные панели,
цепочка маршрутизаторов, пастельные акценты), но сборка и сцена другие: глубокий
сине-зелёный фон с северным сиянием, полупрозрачные панели со светящейся кромкой,
светлый текст и неоново-пастельные акценты.
"""

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
--bg:#07201c; --ink:#e4f5ee; --dim:#9cbdb1;
--title:#ffffff; --accent:#5ddca6; --aqua:#56d7e6; --lime:#aef0c4;
--pink:#ff9ec6; --blue:#a8c8ff; --lav:#c6b9ff; --amber:#f3cf9a;
--glass:rgba(255,255,255,.075);
--glass-2:rgba(255,255,255,.045);
--glass-line:rgba(255,255,255,.40);
--glass-edge:rgba(255,255,255,.14);
--shadow:0 24px 60px rgba(0,22,18,.5), 0 2px 10px rgba(0,22,18,.35);
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
.slide>.sc{flex:1;min-height:0;overflow:auto;padding:2px 10px 2px 2px;scrollbar-width:thin;
 scrollbar-color:rgba(93,220,166,.4) transparent;display:flex;flex-direction:column;gap:16px}
.slide>.sc::-webkit-scrollbar{width:8px}
.slide>.sc::-webkit-scrollbar-thumb{background:rgba(93,220,166,.35);border-radius:8px}
.slide>.sc>.g{flex:1 1 auto;align-content:stretch}
.slide>.sc>.g.fix{flex:0 0 auto}
.slide>.sc>.step{flex:0 0 auto}
.g>.step{display:flex;flex-direction:column;min-height:0}
.g>.step>.c{flex:1 1 auto}
.g>.c{height:100%}
.col{display:flex;flex-direction:column;gap:16px;min-width:0}

/* ---------- шапка ---------- */
.head{flex:none;margin-bottom:2px;display:flex;align-items:flex-start;gap:18px;position:relative}
.head .mark{flex:none;width:12px;height:72px;border-radius:999px;margin-top:6px;
 background:linear-gradient(180deg,var(--aqua),var(--accent));
 box-shadow:0 0 26px rgba(93,220,166,.6)}
h1.t{font-size:clamp(21px,2.3vw,43px);font-weight:900;line-height:.95;color:var(--title);
 text-transform:uppercase;letter-spacing:-.012em;
 text-shadow:0 0 34px rgba(93,220,166,.28)}
.ul{height:6px;border-radius:999px;margin-top:12px;width:clamp(140px,18vw,280px);
 background:linear-gradient(90deg,var(--accent),var(--aqua) 42%,var(--lav) 76%,var(--pink));
 box-shadow:0 0 22px rgba(86,215,230,.55)}
p.sub{margin-top:11px;font-size:clamp(13px,1.02vw,20px);color:var(--dim);line-height:1.46;
 max-width:1120px}

/* ---------- стеклянная панель ---------- */
.c{position:relative;display:flex;flex-direction:column;border-radius:var(--r);
 padding:clamp(16px,1.2vw,24px) clamp(18px,1.3vw,26px);
 background:linear-gradient(150deg,rgba(255,255,255,.11),rgba(255,255,255,.035));
 backdrop-filter:blur(26px) saturate(1.3);-webkit-backdrop-filter:blur(26px) saturate(1.3);
 border:1px solid var(--glass-edge);box-shadow:var(--shadow);
 transition:transform .25s var(--ease),box-shadow .25s var(--ease),border-color .25s var(--ease)}
.c::before{content:"";position:absolute;inset:0;border-radius:var(--r);pointer-events:none;
 border-top:1.5px solid var(--glass-line);border-left:1px solid rgba(255,255,255,.22);
 -webkit-mask:linear-gradient(#000,transparent 58%);mask:linear-gradient(#000,transparent 58%)}
.c:hover{transform:translateY(-3px);border-color:rgba(93,220,166,.38);
 box-shadow:0 30px 70px rgba(0,22,18,.55),0 0 0 1px rgba(93,220,166,.12)}
.c.soft{background:linear-gradient(150deg,rgba(255,255,255,.07),rgba(255,255,255,.02))}
.ch{display:flex;align-items:center;gap:13px;margin-bottom:12px}
.ch h3{font-size:clamp(14px,1.06vw,22px);font-weight:900;line-height:1.08;color:#fff;
 text-transform:uppercase;letter-spacing:.012em}
.ch h3.mix{text-transform:none;font-weight:800}
.num{flex:none;width:40px;height:40px;border-radius:50%;display:grid;place-items:center;
 font:900 17px/1 var(--f);color:#06241d;
 background:linear-gradient(145deg,var(--lime),var(--accent));
 box-shadow:0 0 22px rgba(93,220,166,.55),inset 0 1.5px 0 rgba(255,255,255,.8)}
.num.sm{width:31px;height:31px;font-size:14px}
.c p{font-size:clamp(12.5px,.9vw,17.5px);line-height:1.54;color:var(--ink)}
.c p+p{margin-top:9px}
.c p.d{color:var(--dim)}
.c b,.c strong{color:#fff}
.c h4{font-size:clamp(13px,.88vw,17px);font-weight:800;color:var(--accent);margin-bottom:9px;
 text-transform:uppercase;letter-spacing:.05em}
.hr{height:1px;background:linear-gradient(90deg,rgba(255,255,255,.3),rgba(255,255,255,0));
 margin:12px 0 11px}
.c svg.fig{width:100%;display:block;margin:4px auto 0}

/* ---------- плашки ---------- */
.tag{display:inline-block;padding:7px 15px;border-radius:var(--r3);
 font:800 clamp(11.5px,.8vw,15px) var(--f);line-height:1.25;
 background:rgba(93,220,166,.14);color:var(--accent);border:1px solid rgba(93,220,166,.35)}
.tag.p{background:rgba(255,158,198,.14);color:var(--pink);border-color:rgba(255,158,198,.35)}
.tag.b{background:rgba(168,200,255,.14);color:var(--blue);border-color:rgba(168,200,255,.35)}
.tag.v{background:rgba(198,185,255,.14);color:var(--lav);border-color:rgba(198,185,255,.35)}
.tag.mono{font-family:var(--m);font-weight:700}
.tags{display:flex;gap:9px;flex-wrap:wrap}

/* ---------- строка с иконкой ---------- */
.ir{display:flex;align-items:center;gap:13px;border-radius:var(--r2);padding:10px 14px;
 background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.09)}
.ir+.ir{margin-top:9px}
.ir .ib{flex:none;width:34px;height:34px;border-radius:12px;display:grid;place-items:center;
 background:rgba(93,220,166,.14);border:1px solid rgba(93,220,166,.3)}
.ir .ib svg{width:18px;height:18px;fill:none;stroke:var(--accent);stroke-width:1.7;
 stroke-linecap:round;stroke-linejoin:round}
.ir.p .ib{background:rgba(255,158,198,.14);border-color:rgba(255,158,198,.3)}
.ir.p .ib svg{stroke:var(--pink)}
.ir.b .ib{background:rgba(168,200,255,.14);border-color:rgba(168,200,255,.3)}
.ir.b .ib svg{stroke:var(--blue)}
.ir.v .ib{background:rgba(198,185,255,.14);border-color:rgba(198,185,255,.3)}
.ir.v .ib svg{stroke:var(--lav)}
.ir span{font-size:clamp(12.5px,.88vw,17px);line-height:1.42;color:var(--ink)}
.ir b{color:#fff}

/* ---------- списки ---------- */
ul.ck{list-style:none;display:flex;flex-direction:column;gap:10px}
ul.ck li{display:flex;gap:12px;align-items:flex-start;font-size:clamp(12.5px,.88vw,17px);
 line-height:1.46;color:var(--ink)}
ul.ck li::before{content:"";flex:none;width:20px;height:20px;border-radius:50%;margin-top:1px;
 box-shadow:0 0 14px rgba(93,220,166,.5);
 background:linear-gradient(145deg,var(--lime),var(--accent)),
  url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M5 13l4 4 10-10' fill='none' stroke='%2306241d' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/></svg>") center/13px no-repeat}
ul.ck.no li::before{box-shadow:0 0 14px rgba(255,158,198,.45);
 background:linear-gradient(145deg,#ffc4dd,var(--pink)),
  url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M6 12h12' fill='none' stroke='%234a1228' stroke-width='3.4' stroke-linecap='round'/></svg>") center/13px no-repeat}
ul.ck.dot li::before{background:linear-gradient(145deg,#cfe0ff,var(--blue))}

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
 background:rgba(255,255,255,.05);backdrop-filter:blur(18px);box-shadow:var(--shadow)}
table{border-collapse:collapse;width:100%;font-size:clamp(12px,.88vw,17px)}
th,td{padding:11px 16px;text-align:left;border-bottom:1px solid rgba(255,255,255,.09);
 color:var(--ink)}
th{background:rgba(93,220,166,.14);color:var(--accent);font-weight:800;position:sticky;top:0;
 backdrop-filter:blur(14px);font-size:clamp(11.5px,.82vw,15.5px);text-transform:uppercase;
 letter-spacing:.04em}
tr:last-child td{border-bottom:none}
tbody tr:hover td{background:rgba(255,255,255,.055)}
td b{color:#fff}
td.mono,th.mono{font-family:var(--m);font-weight:700}
td .g1{color:var(--accent);font-weight:800}
td .r1{color:var(--pink);font-weight:800}
td.c,th.c{text-align:center}
tr.hot td{background:rgba(255,158,198,.12)}
tr.new td{background:rgba(93,220,166,.13)}

/* ---------- CLI ---------- */
.cli{border-radius:var(--r2);padding:15px 18px;overflow-x:auto;
 background:rgba(2,16,13,.62);border:1px solid rgba(255,255,255,.1);
 box-shadow:inset 0 1px 0 rgba(255,255,255,.12),0 18px 40px rgba(0,16,12,.45)}
.cli pre{font:600 clamp(11.5px,.82vw,15.5px)/1.65 var(--m);color:#d7f2e6;white-space:pre}
.cli .pr{color:var(--accent)}
.cli .cm{color:#ffffff}
.cli .rem{color:#86a89a;font-style:italic}
.cli .cur{display:inline-block;width:8px;height:1.05em;vertical-align:-2px;background:var(--accent);
 animation:bl 1s steps(1) infinite}
@keyframes bl{50%{opacity:0}}

/* ---------- выноска ---------- */
.bub{position:relative;border-radius:var(--r2);padding:12px 16px;display:inline-block;
 background:rgba(93,220,166,.14);color:var(--accent);border:1px solid rgba(93,220,166,.3);
 font:700 clamp(12px,.85vw,16px)/1.35 var(--f)}
.bub.p{background:rgba(255,158,198,.14);color:var(--pink);border-color:rgba(255,158,198,.3)}
.bub.b{background:rgba(168,200,255,.14);color:var(--blue);border-color:rgba(168,200,255,.3)}
.bub.v{background:rgba(198,185,255,.14);color:var(--lav);border-color:rgba(198,185,255,.3)}

/* ---------- сноска ---------- */
.foot{display:flex;align-items:center;gap:16px;margin-top:2px;flex:none}
.foot i{flex:1;height:1px;font-style:normal}
.foot i:first-child{background:linear-gradient(90deg,rgba(255,255,255,0),rgba(255,255,255,.22))}
.foot i:last-child{background:linear-gradient(90deg,rgba(255,255,255,.22),rgba(255,255,255,0))}
.foot span{font-size:clamp(11px,.76vw,14px);color:var(--dim);white-space:nowrap}

/* ---------- шаги ---------- */
.step{opacity:0;transform:translateY(14px) scale(.985);
 transition:opacity .34s var(--ease),transform .34s var(--ease),filter .34s var(--ease)}
.step.vis{opacity:1;transform:none}
.dash{stroke-dasharray:var(--L);stroke-dashoffset:var(--L);transition:stroke-dashoffset .75s var(--ease)}
.vis .dash,.dash.go{stroke-dashoffset:0}
.fade{opacity:0;transition:opacity .45s var(--ease)}
.fade.go{opacity:1}

/* ---------- титул ---------- */
.cover{display:flex;flex-direction:column;justify-content:center;height:100%;gap:18px;
 max-width:1180px}
.cover h1{font-size:clamp(32px,5.4vw,90px);font-weight:900;line-height:.92;color:#fff;
 text-transform:uppercase;letter-spacing:-.02em;text-shadow:0 0 50px rgba(93,220,166,.35)}
.cover .ul{width:clamp(200px,30vw,480px);height:10px;margin-top:6px}
.cover .meta{display:flex;gap:10px;flex-wrap:wrap;margin-top:10px}

/* ---------- тренажёр ---------- */
.ui{display:flex;gap:11px;align-items:center;flex-wrap:wrap}
.ui button,.btn{font:800 clamp(12px,.85vw,15.5px) var(--f);color:#06241d;border:0;cursor:pointer;
 background:linear-gradient(145deg,var(--lime),var(--accent));border-radius:var(--r3);
 padding:11px 19px;box-shadow:0 0 24px rgba(93,220,166,.45);transition:.2s var(--ease)}
.ui button:hover,.btn:hover{transform:translateY(-2px);box-shadow:0 0 34px rgba(93,220,166,.65)}
.ui button.gh{background:rgba(255,255,255,.07);color:var(--ink);
 border:1px solid rgba(255,255,255,.18);box-shadow:none}
.ui button.gh.on{background:rgba(93,220,166,.18);color:var(--accent);
 border-color:rgba(93,220,166,.5)}
.ui .lab{font-size:clamp(12px,.84vw,15.5px);color:var(--dim)}
.rt{display:grid;gap:10px;font:700 clamp(11px,.78vw,14.5px)/1.3 var(--m)}
.rt .rw{display:grid;grid-template-columns:1fr auto auto;gap:9px;align-items:center;
 background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1);border-radius:14px;
 padding:9px 13px;transition:.3s var(--ease);color:var(--ink)}
.rt .rw.upd{background:rgba(93,220,166,.18);border-color:rgba(93,220,166,.5);
 box-shadow:0 0 22px rgba(93,220,166,.25)}
.rt .rw.inf{background:rgba(255,158,198,.14);border-color:rgba(255,158,198,.4);color:var(--pink)}
.rt .rw b{color:#fff}
.big{font:900 clamp(22px,2.4vw,42px)/1 var(--m);color:var(--accent);
 text-shadow:0 0 26px rgba(93,220,166,.5)}

/* ---------- квиз ---------- */
.q{border-radius:var(--r);padding:17px 20px;
 background:linear-gradient(150deg,rgba(255,255,255,.1),rgba(255,255,255,.03));
 backdrop-filter:blur(26px) saturate(1.3);border:1px solid var(--glass-edge);
 box-shadow:var(--shadow)}
.q .qt{display:flex;gap:12px;align-items:flex-start;font-weight:800;color:#fff;
 font-size:clamp(13.5px,.98vw,19px);margin-bottom:12px;line-height:1.3}
.q .opts{display:grid;gap:8px}
.q button{text-align:left;font:600 clamp(12.5px,.86vw,16.5px) var(--f);padding:12px 16px;
 border-radius:14px;border:1px solid rgba(255,255,255,.12);background:rgba(255,255,255,.045);
 color:var(--ink);cursor:pointer;transition:.18s var(--ease)}
.q button:hover{background:rgba(255,255,255,.1);transform:translateX(3px)}
.q button.good{background:rgba(93,220,166,.2);border-color:rgba(93,220,166,.55);
 color:var(--lime);font-weight:800}
.q button.bad{background:rgba(255,158,198,.16);border-color:rgba(255,158,198,.45);
 color:var(--pink)}
.q .ex{display:none;margin-top:12px;padding-top:11px;border-top:1px solid rgba(255,255,255,.13);
 font-size:clamp(12.5px,.86vw,16.5px);line-height:1.48;color:var(--dim)}
.q .ex.on{display:block}
#score{font:900 15px var(--m);color:var(--accent)}

/* ---------- HUD ---------- */
#hud{position:fixed;left:0;right:0;bottom:0;height:56px;z-index:5;display:flex;align-items:center;
 gap:10px;padding:0 20px;background:rgba(7,32,28,.6);
 backdrop-filter:blur(26px) saturate(1.4);border-top:1px solid rgba(255,255,255,.12)}
#prog{position:fixed;left:0;bottom:56px;height:3px;z-index:6;transition:width .3s var(--ease);
 background:linear-gradient(90deg,var(--accent),var(--aqua),var(--lav),var(--pink));
 box-shadow:0 0 16px rgba(93,220,166,.6)}
#hud button{font:700 13px var(--f);color:var(--ink);background:rgba(255,255,255,.07);
 border:1px solid rgba(255,255,255,.16);border-radius:var(--r3);padding:8px 15px;cursor:pointer;
 transition:.2s var(--ease)}
#hud button:hover{background:linear-gradient(145deg,var(--lime),var(--accent));color:#06241d;
 border-color:transparent;transform:translateY(-2px);box-shadow:0 0 22px rgba(93,220,166,.5)}
#count{font:800 13.5px var(--m);color:var(--accent);min-width:116px}
#sname{font-size:13px;color:var(--dim);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
:focus-visible{outline:3px solid var(--aqua);outline-offset:2px;border-radius:10px}

/* ---------- содержание ---------- */
#toc{position:fixed;inset:0;z-index:20;background:rgba(5,24,21,.86);
 backdrop-filter:blur(30px) saturate(1.3);display:none;padding:40px 48px;overflow:auto}
#toc.on{display:block}
#toc h2{color:#fff;font-size:25px;margin-bottom:20px;font-weight:900;text-transform:uppercase;
 letter-spacing:.03em}
#tocg{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:11px}
.tocit{display:flex;gap:12px;align-items:center;text-align:left;padding:12px 14px;
 border-radius:16px;background:rgba(255,255,255,.055);border:1px solid rgba(255,255,255,.12);
 color:var(--ink);font:600 13px var(--f);cursor:pointer;transition:.2s var(--ease)}
.tocit:hover{background:rgba(93,220,166,.16);border-color:rgba(93,220,166,.45);
 transform:translateY(-3px)}
.tocit i{font:900 12px/1 var(--m);font-style:normal;color:#06241d;min-width:26px;height:26px;
 border-radius:50%;display:grid;place-items:center;
 background:linear-gradient(145deg,var(--lime),var(--accent))}

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

/* ---------- живая сцена ---------- */
#bg .orb{transform-box:fill-box;transform-origin:center;will-change:transform}
@keyframes drift1{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(60px,34px) scale(1.09)}}
@keyframes drift2{0%,100%{transform:translate(0,0) scale(1)}50%{transform:translate(-54px,-40px) scale(1.12)}}
@keyframes drift3{0%,100%{transform:translate(0,0) scale(1.04)}50%{transform:translate(42px,-30px) scale(.94)}}
@keyframes drift4{0%,100%{transform:translate(0,0) scale(.97)}50%{transform:translate(-46px,30px) scale(1.1)}}
#bg .oa{animation:drift1 26s ease-in-out infinite}
#bg .ob{animation:drift2 31s ease-in-out infinite}
#bg .oc{animation:drift3 23s ease-in-out infinite}
#bg .od{animation:drift4 35s ease-in-out infinite}
@keyframes aurora{0%,100%{opacity:.5;transform:translateY(0)}50%{opacity:1;transform:translateY(-26px)}}
#bg .aur{animation:aurora 19s ease-in-out infinite}
@keyframes tw{0%,100%{opacity:.14}50%{opacity:.85}}
#bg .st{animation:tw var(--d,5s) ease-in-out infinite}
#bg .leaf{animation:sway 17s ease-in-out infinite;transform-box:fill-box;transform-origin:left center}
@keyframes sway{0%,100%{filter:brightness(1)}50%{filter:brightness(1.35)}}

/* ---------- неон на схемах ---------- */
.c svg.fig path[marker-end]{filter:drop-shadow(0 0 7px rgba(255,255,255,.35))}
.c svg.fig g.rtr{filter:drop-shadow(0 8px 18px rgba(0,16,12,.55))}
.c svg.fig text{paint-order:stroke}

/* ---------- живой титул ---------- */
.cover h1{background:linear-gradient(104deg,#ffffff 12%,#aef0c4 38%,#a8e8ff 58%,#ffffff 82%);
 background-size:280% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;
 animation:shine 9s ease-in-out infinite}
@keyframes shine{0%,100%{background-position:0% 50%}50%{background-position:100% 50%}}
.cover .ul{animation:pulsebar 4.5s ease-in-out infinite}
@keyframes pulsebar{0%,100%{box-shadow:0 0 22px rgba(86,215,230,.45)}50%{box-shadow:0 0 38px rgba(93,220,166,.8)}}

/* ---------- появление карточек ---------- */
.step{filter:blur(6px)}
.step.vis{filter:none}
.step.vis .num{animation:popn .55s var(--ease) both}
@keyframes popn{0%{transform:scale(.4);box-shadow:0 0 0 rgba(93,220,166,0)}
 60%{transform:scale(1.14)}100%{transform:scale(1);box-shadow:0 0 22px rgba(93,220,166,.55)}}

@media (prefers-reduced-motion:reduce){
 #bg .orb,#bg .aur,#bg .st,#bg .leaf,.cover h1,.cover .ul,.step.vis .num{animation:none}
 .step{filter:none}
 .cover h1{color:#fff;-webkit-text-fill-color:#fff}
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
#  Сцена: северное сияние, стеклянные пластины, светящиеся листья
# ======================================================================
def background():
    leaves = []
    spots = [
        (-30, 120, 1.35, -26, .20), (-58, 320, 1.75, 16, .15),
        (-14, 520, 1.15, -50, .18), (-42, 720, 1.55, 26, .13),
        (1366, 100, 1.45, 196, .19), (1400, 290, 1.75, 164, .14),
        (1358, 490, 1.2, 212, .17), (1392, 700, 1.6, 150, .13),
    ]
    for (x, y, s, rot, op) in spots:
        leaves.append('<use href="#gleaf" class="leaf" transform="translate(%d %d) rotate(%d) '
                      'scale(%.2f)" opacity="%.2f"/>' % (x, y, rot, s, op))

    plates = []
    for (x, y, w, h, rot, op) in [(110, 530, 330, 200, -12, .07), (970, 110, 320, 190, 9, .06),
                                  (600, 650, 400, 180, -5, .05), (1050, 530, 280, 160, 14, .06)]:
        plates.append('<rect x="%d" y="%d" width="%d" height="%d" rx="34" fill="#ffffff" '
                      'opacity="%.2f" transform="rotate(%d %d %d)" stroke="rgba(255,255,255,.22)" '
                      'stroke-width="1.5"/>' % (x, y, w, h, op, rot, x + w / 2, y + h / 2))

    dots = []
    for (x, y, w, h) in [(330, 160, 86, 60), (1080, 390, 74, 50), (520, 800, 100, 52)]:
        dots.append('<rect x="%d" y="%d" width="%d" height="%d" fill="url(#gdot)" opacity=".45"/>'
                    % (x, y, w, h))

    stars = []
    seed = 7
    for i in range(46):
        seed = (seed * 1103515245 + 12345) % 2147483648
        x = seed % 1440
        seed = (seed * 1103515245 + 12345) % 2147483648
        y = seed % 900
        seed = (seed * 1103515245 + 12345) % 2147483648
        r = 0.8 + (seed % 100) / 90.0
        stars.append('<circle class="st" style="--d:%.1fs" cx="%d" cy="%d" r="%.1f" '
                     'fill="#dffaf0" opacity="%.2f"/>'
                     % (2.4 + (seed % 70) / 10.0, x, y, r, .10 + (seed % 30) / 100.0))

    return """<svg id="bg" viewBox="0 0 1440 900" preserveAspectRatio="xMidYMid slice" aria-hidden="true">
<defs>
  <linearGradient id="gsky" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#062a24"/><stop offset=".45" stop-color="#07211f"/>
    <stop offset="1" stop-color="#121634"/>
  </linearGradient>
  <radialGradient id="o1"><stop offset="0" stop-color="#2fe0a8" stop-opacity=".42"/><stop offset="1" stop-color="#2fe0a8" stop-opacity="0"/></radialGradient>
  <radialGradient id="o2"><stop offset="0" stop-color="#ff7fb6" stop-opacity=".30"/><stop offset="1" stop-color="#ff7fb6" stop-opacity="0"/></radialGradient>
  <radialGradient id="o3"><stop offset="0" stop-color="#7c6cff" stop-opacity=".36"/><stop offset="1" stop-color="#7c6cff" stop-opacity="0"/></radialGradient>
  <radialGradient id="o4"><stop offset="0" stop-color="#2bc8e8" stop-opacity=".34"/><stop offset="1" stop-color="#2bc8e8" stop-opacity="0"/></radialGradient>
  <linearGradient id="glf" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0" stop-color="#4fd9a8"/><stop offset="1" stop-color="#a7f0d6"/>
  </linearGradient>
  <linearGradient id="gaur" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0" stop-color="#2fe0a8" stop-opacity="0"/>
    <stop offset=".35" stop-color="#2fe0a8" stop-opacity=".30"/>
    <stop offset=".65" stop-color="#7c6cff" stop-opacity=".26"/>
    <stop offset="1" stop-color="#ff7fb6" stop-opacity="0"/>
  </linearGradient>
  <pattern id="gdot" width="14" height="14" patternUnits="userSpaceOnUse">
    <circle cx="3" cy="3" r="2" fill="#5ddca6"/>
  </pattern>
  <g id="gleaf">
    <path d="M0 0 C 26 -34 74 -34 100 0 C 74 34 26 34 0 0 Z" fill="url(#glf)"/>
    <path d="M2 0 H98" stroke="#bff3dd" stroke-width="1.6" fill="none" opacity=".7"/>
    <path d="M26 -2 C 38 -12 46 -16 58 -17" stroke="#bff3dd" stroke-width="1.2" fill="none" opacity=".6"/>
    <path d="M46 -2 C 58 -11 66 -14 78 -15" stroke="#bff3dd" stroke-width="1.2" fill="none" opacity=".6"/>
    <path d="M26 2 C 38 12 46 16 58 17" stroke="#bff3dd" stroke-width="1.2" fill="none" opacity=".6"/>
    <path d="M46 2 C 58 11 66 14 78 15" stroke="#bff3dd" stroke-width="1.2" fill="none" opacity=".6"/>
  </g>
</defs>
<rect width="1440" height="900" fill="url(#gsky)"/>
<ellipse class="orb oa" cx="250" cy="110" rx="430" ry="300" fill="url(#o1)"/>
<ellipse class="orb ob" cx="1230" cy="770" rx="440" ry="310" fill="url(#o4)"/>
<ellipse class="orb oc" cx="1190" cy="110" rx="340" ry="250" fill="url(#o2)"/>
<ellipse class="orb od" cx="250" cy="840" rx="380" ry="250" fill="url(#o3)"/>
<path d="M-60 300 C 240 180 520 420 820 300 C 1080 196 1300 330 1500 250 L1500 520 C 1300 600 1080 460 820 560
 C 520 676 240 440 -60 560 Z" fill="url(#gaur)" class="aur"/>
%s
%s
%s
%s
</svg>""" % ("\n".join(stars), "\n".join(plates), "\n".join(dots), "\n".join(leaves))


# ======================================================================
#  Перекраска SVG-схем под тёмную сцену
# ======================================================================
#  Схемы в _rip_lib нарисованы для светлого фона. Для стеклянной деки
#  заменяем палитру внутри каждой фигуры: белые подложки становятся
#  полупрозрачными, тёмный текст — светлым, акценты — неоновыми.
TINT = [
    # белая карточка-таблица внутри схемы
    ('fill="#fff" stroke="#bfe5cf" stroke-width="2"',
     'fill="rgba(255,255,255,.06)" stroke="rgba(255,255,255,.22)" stroke-width="1.5"'),
    ('fill="#eef7f2" stroke="#bfe5cf" stroke-width="2"',
     'fill="rgba(255,255,255,.08)" stroke="rgba(255,255,255,.24)" stroke-width="1.5"'),
    ('fill="#fff" stroke="#d94a74"', 'fill="#1a0f16" stroke="#ff7fae"'),
    ('stroke="#d94a74"', 'stroke="#ff7fae"'),
    # заливки-подложки
    ('fill="#dbe9fb"', 'fill="rgba(168,200,255,.18)"'),
    ('fill="#dff3e8"', 'fill="rgba(93,220,166,.18)"'),
    ('fill="#e7e2fa"', 'fill="rgba(198,185,255,.18)"'),
    ('fill="#fbe2ed"', 'fill="rgba(255,158,198,.18)"'),
    ('fill="#e4eefc"', 'fill="rgba(168,200,255,.18)"'),
    ('fill="#eae5fb"', 'fill="rgba(198,185,255,.18)"'),
    ('fill="#fbe9d8"', 'fill="rgba(243,207,154,.18)"'),
    ('fill="#dce9fb"', 'fill="rgba(168,200,255,.18)"'),
    ('fill="#c8dcf6"', 'fill="rgba(168,200,255,.26)"'),
    # линии связи
    ('stroke="#bfe5cf"', 'stroke="rgba(255,255,255,.20)"'),
    ('stroke="#9fd4b8"', 'stroke="rgba(255,255,255,.26)"'),
    ('stroke="#dff3e8"', 'stroke="rgba(255,255,255,.20)"'),
    # текст и акценты
    ('"#2a3b33"', '"#e4f5ee"'),
    ('"#6a8077"', '"#a9c7ba"'),
    ('"#1b6b47"', '"#5ddca6"'),
    ('"#1d7a4f"', '"#5ddca6"'),
    ('"#3b6ba8"', '"#a8c8ff"'),
    ('"#4a7cc2"', '"#a8c8ff"'),
    ('"#6a5ab8"', '"#c6b9ff"'),
    ('"#7566c4"', '"#c6b9ff"'),
    ('"#9a6a35"', '"#f3cf9a"'),
    ('"#c9517f"', '"#ff9ec6"'),
    # стрелки
    ('"#36a56e"', '"#5ddca6"'),
    ('"#e58cb4"', '"#ff9ec6"'),
    ('"#7ba7e0"', '"#a8c8ff"'),
    ('"#9f90dd"', '"#c6b9ff"'),
]


def tint(markup):
    """Перекрашивает содержимое всех <svg class="fig…"> под тёмную сцену."""
    import re

    def one(m):
        s = m.group(0)
        for a, b in TINT:
            s = s.replace(a, b)
        return s

    return re.sub(r'<svg class="fig.*?</svg>', one, markup, flags=re.S)
