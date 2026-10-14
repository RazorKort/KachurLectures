# -*- coding: utf-8 -*-
"""Мятно-ботанический стиль деки «Динамическая маршрутизация: RIP»."""

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
--bg:#f3fbf7; --card:#ffffff; --edge:#bfe5cf;
--title:#1b6b47; --green:#36a56e; --green-l:#dff3e8; --mint:#8fd9b6;
--pink:#f3c3d8; --pink-ink:#c9517f;
--blue:#c8dcf6; --blue-ink:#4a7cc2;
--lav:#d8d1f4;  --lav-ink:#7566c4;
--ink:#2a3b33;  --dim:#6a8077;
--deep:#10402c;
--r:22px; --r2:13px; --r3:12px;
--ease:cubic-bezier(.22,.7,.3,1);
--f:"Montserrat","Segoe UI Variable Display","Segoe UI",Inter,system-ui,-apple-system,Arial,sans-serif;
--m:"Cascadia Mono","JetBrains Mono",Consolas,"SF Mono",ui-monospace,monospace;
}
html,body{height:100%}
body{font-family:var(--f);color:var(--ink);background:var(--bg);overflow:hidden;
-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* ---------- фон ---------- */
#bg{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}

/* ---------- каркас ---------- */
#stage{position:fixed;inset:0;z-index:1}
.slide{position:absolute;inset:0;padding:clamp(22px,2.1vw,42px) clamp(24px,2.9vw,56px) 78px;
 display:none;overflow:hidden;flex-direction:column}
.slide.on{display:flex}
.slide>.sc{flex:1;min-height:0;overflow:auto;padding-right:6px;scrollbar-width:thin;
 scrollbar-color:#bfe5cf transparent;display:flex;flex-direction:column;gap:14px}
.slide>.sc::-webkit-scrollbar{width:8px}
.slide>.sc::-webkit-scrollbar-thumb{background:#bfe5cf;border-radius:8px}
.slide>.sc>.g{flex:1 1 auto;align-content:stretch}
.slide>.sc>.g.fix{flex:0 0 auto}
.slide>.sc>.step{flex:0 0 auto}
.slide>.sc>.grow{flex:1 1 auto}
.g>.step{display:flex;flex-direction:column;min-height:0}
.g>.step>.c{flex:1 1 auto}
.g>.c{height:100%}
.col{display:flex;flex-direction:column;gap:14px;min-width:0}
.col>.step{display:flex;flex-direction:column}

/* ---------- заголовок слайда ---------- */
.head{flex:none;margin-bottom:4px;display:flex;align-items:flex-start;gap:16px}
.head .mark{flex:none;width:9px;height:64px;border-radius:0 7px 7px 0;margin-top:4px;
 background:linear-gradient(180deg,var(--mint),var(--green))}
h1.t{font-size:clamp(22px,2.35vw,44px);font-weight:900;line-height:.95;color:var(--title);
 text-transform:uppercase;letter-spacing:-.005em}
.ul{height:7px;border-radius:4px;margin-top:11px;width:clamp(120px,15vw,230px);
 background:linear-gradient(90deg,var(--green),var(--mint) 55%,var(--pink))}
p.sub{margin-top:10px;font-size:clamp(13px,1.02vw,20px);color:var(--dim);line-height:1.42;max-width:1120px}

/* ---------- панель ---------- */
.c{background:var(--card);border:2px solid var(--edge);border-radius:var(--r);
 padding:clamp(15px,1.15vw,23px) clamp(17px,1.25vw,25px);
 box-shadow:0 8px 26px rgba(40,110,80,.07);display:flex;flex-direction:column;position:relative}
.c.soft{background:#fbfefc}
.ch{display:flex;align-items:center;gap:12px;margin-bottom:11px}
.ch h3{font-size:clamp(14px,1.08vw,22px);font-weight:900;line-height:1.06;color:var(--title);
 text-transform:uppercase}
.ch h3.mix{text-transform:none;font-weight:800}
.num{flex:none;width:38px;height:38px;border-radius:50%;display:grid;place-items:center;
 font:900 17px/1 var(--f);color:#fff;background:linear-gradient(145deg,var(--mint),var(--green));
 box-shadow:0 4px 10px rgba(54,165,110,.3)}
.num.sm{width:30px;height:30px;font-size:14px}
.c p{font-size:clamp(12.5px,.9vw,17.5px);line-height:1.5;color:var(--ink)}
.c p+p{margin-top:8px}
.c p.d{color:var(--dim)}
.c h4{font-size:clamp(13px,.88vw,17px);font-weight:800;color:var(--title);margin-bottom:7px}
.hr{height:2px;background:var(--green-l);border-radius:2px;margin:11px 0 10px}
.c svg.fig{width:100%;display:block;margin:4px auto 0}

/* ---------- пастельные плашки ---------- */
.tag{display:inline-block;padding:6px 13px;border-radius:var(--r3);font:800 clamp(11.5px,.8vw,15px) var(--f);
 background:var(--green-l);color:#1d7a4f;line-height:1.25}
.tag.p{background:#fbe2ed;color:var(--pink-ink)}
.tag.b{background:#e4eefc;color:var(--blue-ink)}
.tag.v{background:#eae5fb;color:var(--lav-ink)}
.tag.mono{font-family:var(--m);font-weight:700;letter-spacing:.01em}
.tags{display:flex;gap:8px;flex-wrap:wrap}

/* ---------- строка с иконкой ---------- */
.ir{display:flex;align-items:center;gap:12px;background:#f4fbf7;border-radius:var(--r2);
 padding:9px 13px}
.ir+.ir{margin-top:8px}
.ir .ib{flex:none;width:32px;height:32px;border-radius:10px;background:#fff;display:grid;place-items:center;
 box-shadow:0 2px 7px rgba(40,110,80,.12)}
.ir .ib svg{width:18px;height:18px;fill:none;stroke:var(--green);stroke-width:1.6;
 stroke-linecap:round;stroke-linejoin:round}
.ir.p .ib svg{stroke:var(--pink-ink)}
.ir.b .ib svg{stroke:var(--blue-ink)}
.ir.v .ib svg{stroke:var(--lav-ink)}
.ir span{font-size:clamp(12.5px,.88vw,17px);line-height:1.38;color:var(--ink)}
.ir b{color:var(--title)}

/* ---------- список-галочки ---------- */
ul.ck{list-style:none;display:flex;flex-direction:column;gap:9px}
ul.ck li{display:flex;gap:11px;align-items:flex-start;font-size:clamp(12.5px,.88vw,17px);
 line-height:1.42;color:var(--ink)}
ul.ck li::before{content:"";flex:none;width:19px;height:19px;border-radius:50%;margin-top:1px;
 background:var(--green) url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M5 13l4 4 10-10' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round' stroke-linejoin='round'/></svg>") center/13px no-repeat}
ul.ck.no li::before{background:var(--pink-ink) url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M6 12h12' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round'/></svg>") center/13px no-repeat}
ul.ck.dot li::before{background:var(--blue-ink)}

/* ---------- сетки ---------- */
.g{display:grid;gap:14px}
.g>*{min-width:0}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.g21{grid-template-columns:2fr 1fr}
.g12{grid-template-columns:1fr 2fr}
.g32{grid-template-columns:3fr 2fr}
.g23{grid-template-columns:2fr 3fr}

/* ---------- таблица ---------- */
.tw{overflow:auto;border-radius:var(--r);border:2px solid var(--edge);background:var(--card);
 box-shadow:0 8px 26px rgba(40,110,80,.07)}
table{border-collapse:collapse;width:100%;font-size:clamp(12px,.88vw,17px)}
th,td{padding:10px 15px;text-align:left;border-bottom:1px solid var(--green-l);color:var(--ink)}
th{background:var(--green-l);color:var(--title);font-weight:800;position:sticky;top:0;
 font-size:clamp(11.5px,.82vw,15.5px);text-transform:uppercase;letter-spacing:.02em}
tr:last-child td{border-bottom:none}
tbody tr:hover td{background:#f4fbf7}
td.mono,th.mono{font-family:var(--m);font-weight:700}
td .g1{color:#1d7a4f;font-weight:800}
td .r1{color:var(--pink-ink);font-weight:800}
td.c,th.c{text-align:center}
tr.hot td{background:#fdeef5}
tr.new td{background:#eaf8f1}

/* ---------- CLI ---------- */
.cli{background:var(--deep);border-radius:var(--r2);padding:14px 17px;overflow-x:auto;
 box-shadow:0 10px 26px rgba(16,64,44,.22)}
.cli pre{font:600 clamp(11.5px,.82vw,15.5px)/1.62 var(--m);color:#dff3e8;white-space:pre}
.cli .pr{color:#8fd9b6}
.cli .cm{color:#ffffff}
.cli .ar{color:#9fd0ff}
.cli .rem{color:#8aa89a;font-style:italic}
.cli .cur{display:inline-block;width:8px;height:1.05em;vertical-align:-2px;background:#8fd9b6;
 animation:bl 1s steps(1) infinite}
@keyframes bl{50%{opacity:0}}

/* ---------- выноска со хвостиком ---------- */
.bub{position:relative;background:var(--green-l);color:#1d7a4f;border-radius:var(--r3);
 padding:11px 15px;font:700 clamp(12px,.85vw,16px)/1.35 var(--f);display:inline-block}
.bub.p{background:#fbe2ed;color:var(--pink-ink)}
.bub.b{background:#e4eefc;color:var(--blue-ink)}
.bub.v{background:#eae5fb;color:var(--lav-ink)}
.bub::after{content:"";position:absolute;left:24px;bottom:-8px;width:0;height:0;
 border:9px solid transparent;border-top-color:var(--green-l);border-bottom:0}
.bub.p::after{border-top-color:#fbe2ed}
.bub.b::after{border-top-color:#e4eefc}
.bub.v::after{border-top-color:#eae5fb}
.bub.nt::after{display:none}

/* ---------- сноска ---------- */
.foot{display:flex;align-items:center;gap:14px;margin-top:4px;flex:none}
.foot i{flex:1;height:2px;font-style:normal;border-radius:2px}
.foot i:first-child{background:linear-gradient(90deg,rgba(191,229,207,0),var(--edge))}
.foot i:last-child{background:linear-gradient(90deg,var(--edge),rgba(191,229,207,0))}
.foot span{font-size:clamp(11px,.76vw,14px);color:var(--dim);white-space:nowrap}

/* ---------- шаги и SVG-анимация ---------- */
.step{opacity:0;transform:translateY(10px);transition:opacity .3s var(--ease),transform .3s var(--ease)}
.step.vis{opacity:1;transform:none}
.dash{stroke-dasharray:var(--L);stroke-dashoffset:var(--L);transition:stroke-dashoffset .75s var(--ease)}
.vis .dash,.dash.go{stroke-dashoffset:0}
.fade{opacity:0;transition:opacity .4s var(--ease)}
.fade.go{opacity:1}

/* ---------- титул ---------- */
.cover{display:flex;flex-direction:column;justify-content:center;height:100%;gap:16px;max-width:1150px}
.cover h1{font-size:clamp(32px,5.6vw,92px);font-weight:900;line-height:.92;color:var(--title);
 text-transform:uppercase;letter-spacing:-.015em}
.cover .ul{width:clamp(180px,26vw,420px);height:9px;margin-top:4px}
.cover .meta{display:flex;gap:9px;flex-wrap:wrap;margin-top:8px}

/* ---------- тренажёр ---------- */
.ui{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.ui button,.btn{font:800 clamp(12px,.85vw,15.5px) var(--f);color:#fff;border:0;cursor:pointer;
 background:linear-gradient(145deg,var(--mint),var(--green));border-radius:var(--r3);padding:10px 16px;
 box-shadow:0 4px 12px rgba(54,165,110,.26);transition:.18s var(--ease)}
.ui button:hover,.btn:hover{transform:translateY(-1px);box-shadow:0 7px 17px rgba(54,165,110,.32)}
.ui button.gh{background:#fff;color:var(--title);box-shadow:none;border:2px solid var(--edge)}
.ui button.gh.on{background:var(--green-l);border-color:var(--green)}
.ui .lab{font-size:clamp(12px,.84vw,15.5px);color:var(--dim)}
.rt{display:grid;gap:9px;font:700 clamp(11px,.78vw,14.5px)/1.3 var(--m)}
.rt .rw{display:grid;grid-template-columns:1fr auto auto;gap:7px;align-items:center;
 background:#f4fbf7;border-radius:10px;padding:6px 9px;transition:.3s var(--ease)}
.rt .rw.upd{background:var(--green-l);box-shadow:0 0 0 2px var(--green) inset}
.rt .rw.inf{background:#fbe2ed;color:var(--pink-ink)}
.rt .rw b{color:var(--title)}
.big{font:900 clamp(22px,2.4vw,42px)/1 var(--m);color:var(--green)}

/* ---------- квиз ---------- */
.q{background:var(--card);border:2px solid var(--edge);border-radius:var(--r);padding:15px 18px;
 box-shadow:0 8px 26px rgba(40,110,80,.07)}
.q .qt{display:flex;gap:11px;align-items:flex-start;font-weight:800;color:var(--title);
 font-size:clamp(13.5px,.98vw,19px);margin-bottom:11px;line-height:1.3}
.q .opts{display:grid;gap:7px}
.q button{text-align:left;font:600 clamp(12.5px,.86vw,16.5px) var(--f);padding:11px 14px;
 border-radius:var(--r3);border:2px solid var(--edge);background:#fff;color:var(--ink);cursor:pointer;
 transition:.16s var(--ease)}
.q button:hover{background:#f4fbf7;border-color:var(--green)}
.q button.good{background:var(--green-l);border-color:var(--green);color:#1d7a4f;font-weight:800}
.q button.bad{background:#fbe2ed;border-color:var(--pink);color:var(--pink-ink)}
.q .ex{display:none;margin-top:11px;padding-top:10px;border-top:2px dashed var(--green-l);
 font-size:clamp(12.5px,.86vw,16.5px);line-height:1.45;color:var(--dim)}
.q .ex.on{display:block}
#score{font:900 15px var(--m);color:var(--green)}

/* ---------- HUD ---------- */
#hud{position:fixed;left:0;right:0;bottom:0;height:56px;z-index:5;display:flex;align-items:center;
 gap:9px;padding:0 18px;background:rgba(255,255,255,.82);backdrop-filter:blur(12px);
 border-top:2px solid var(--edge)}
#prog{position:fixed;left:0;bottom:56px;height:3px;z-index:6;transition:width .3s var(--ease);
 background:linear-gradient(90deg,var(--green),var(--mint),var(--pink))}
#hud button{font:700 13px var(--f);color:var(--title);background:#fff;border:2px solid var(--edge);
 border-radius:var(--r3);padding:7px 13px;cursor:pointer;transition:.18s var(--ease)}
#hud button:hover{background:var(--green);color:#fff;border-color:var(--green);transform:translateY(-1px)}
#count{font:800 13.5px var(--m);color:var(--green);min-width:116px}
#sname{font-size:13px;color:var(--dim);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
:focus-visible{outline:3px solid var(--green);outline-offset:2px;border-radius:8px}

/* ---------- содержание ---------- */
#toc{position:fixed;inset:0;z-index:20;background:rgba(243,251,247,.97);backdrop-filter:blur(8px);
 display:none;padding:40px 48px;overflow:auto}
#toc.on{display:block}
#toc h2{color:var(--title);font-size:24px;margin-bottom:18px;font-weight:900;text-transform:uppercase}
#tocg{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:10px}
.tocit{display:flex;gap:11px;align-items:center;text-align:left;padding:11px 13px;border-radius:var(--r2);
 background:#fff;border:2px solid var(--edge);color:var(--ink);font:600 13px var(--f);cursor:pointer;
 transition:.18s var(--ease)}
.tocit:hover{background:var(--green-l);border-color:var(--green);transform:translateY(-2px)}
.tocit i{font:900 12px/1 var(--m);font-style:normal;color:#fff;min-width:24px;height:24px;border-radius:50%;
 display:grid;place-items:center;background:linear-gradient(145deg,var(--mint),var(--green))}

/* ---------- адаптив ---------- */
#hud .hint{display:inline;font-size:11.5px;color:var(--dim)}
@media (max-width:1320px){#hud .hint{display:none}}
@media (max-width:1279px){
 .g4{grid-template-columns:repeat(2,1fr)}
 .g3{grid-template-columns:repeat(2,1fr)}
 .slide{padding:20px 24px 68px}
}
@media (max-width:1099px){.g2,.g21,.g12,.g32,.g23{grid-template-columns:1fr}}
@media (max-width:640px){
 .g,.g2,.g3,.g4,.g21,.g12,.g32,.g23{grid-template-columns:1fr}
 h1.t{font-size:26px}
 .cover h1{font-size:32px}
 .slide{padding:16px 15px 64px}
 #sname{display:none}
 #bg .leaf{display:none}
 .figwrap{overflow-x:auto}
}
@media (prefers-reduced-motion:reduce){
 .step{opacity:1!important;transform:none!important;transition:none}
 .dash{stroke-dashoffset:0!important;transition:none}
 .fade{opacity:1!important;transition:none}
 .cli .cur{animation:none}
}
"""
