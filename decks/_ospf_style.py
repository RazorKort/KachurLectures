# -*- coding: utf-8 -*-
"""Кавайный розово-голубой стиль деки «Протокол OSPF»."""

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
--paper:#ffffff;
--pink:#ff5c9e; --pink-bg:#fde7f0; --pink-soft:#ffd3e4; --pink-ink:#d8276f;
--blue:#3b9eff; --blue-bg:#e3f0fd; --blue-soft:#c7e2fb; --blue-ink:#1f6fc4;
--yellow:#ffd93d; --yellow-bg:#fef6dc; --yellow-ink:#8a6a00;
--green:#3fc47c; --green-bg:#e6f7ec; --green-ink:#1d8a51;
--violet:#9b7bf0; --violet-bg:#efe9fb; --violet-ink:#6b4fd0;
--ink:#121212; --dim:#56606b; --line:#e9eef3;
--r:20px; --r2:16px;
--ease:cubic-bezier(.22,.7,.3,1);
--f:"OspfText","Golos Text","Inter","Segoe UI Variable Text","Segoe UI",system-ui,-apple-system,Arial,sans-serif;
--fd:"OspfHead","Oswald","Arial Narrow",sans-serif;
--m:"Cascadia Mono","JetBrains Mono",Consolas,"SF Mono",ui-monospace,monospace;
}
html,body{height:100%}
body{font-family:var(--f);color:var(--ink);background:var(--paper);overflow:hidden;
-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* ---------- фон ---------- */
#bg{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}

/* ---------- каркас ---------- */
#stage{position:fixed;inset:0;z-index:1}
.slide{position:absolute;inset:0;padding:clamp(18px,1.9vw,38px) clamp(20px,2.6vw,52px) 74px;
 display:none;overflow:hidden;flex-direction:column}
.slide.on{display:flex}
.slide>.sc{flex:1;min-height:0;overflow:auto;padding-right:6px;scrollbar-width:thin;
 scrollbar-color:var(--pink-soft) transparent;display:flex;flex-direction:column;gap:13px}
.slide>.sc::-webkit-scrollbar{width:8px}
.slide>.sc::-webkit-scrollbar-thumb{background:var(--pink-soft);border-radius:8px}
.slide>.sc>.g{flex:0 0 auto}
.slide>.sc>.grow{flex:1 1 auto;min-height:0}
.g>.step{display:flex;flex-direction:column;min-height:0}
.g>.step>.c{flex:1 1 auto}
.g>.c{height:100%}
.col{display:flex;flex-direction:column;gap:13px;min-width:0}
.col>.step{display:flex;flex-direction:column}

/* ---------- заголовок ---------- */
.head{flex:none;margin-bottom:6px;display:flex;align-items:flex-start;gap:14px;position:relative}
h1.t{font-family:var(--fd);font-weight:700;line-height:.9;
 font-size:clamp(32px,4.1vw,84px);color:var(--ink);text-transform:uppercase;letter-spacing:-.005em}
p.sub{margin-top:8px;font-size:clamp(15px,1.45vw,28px);color:var(--ink);font-weight:700;line-height:1.25;max-width:1400px}
.head .sparks{flex:none;width:clamp(44px,4vw,74px);height:46px;margin-top:-4px}
.head .sparks path{stroke:var(--pink);stroke-width:8;stroke-linecap:round;fill:none;opacity:.85}

/* ---------- карточки ---------- */
.c{background:var(--paper);border-radius:var(--r);padding:clamp(13px,1.05vw,21px) clamp(15px,1.15vw,23px);
 box-shadow:0 3px 14px rgba(40,60,90,.07);display:flex;flex-direction:column;position:relative}
.c.pink{background:var(--pink-bg)}
.c.blue{background:var(--blue-bg)}
.c.yellow{background:var(--yellow-bg)}
.c.green{background:var(--green-bg)}
.c.violet{background:var(--violet-bg)}
.c.w{background:var(--paper);border:1px solid var(--line)}
.ch{display:flex;align-items:center;gap:11px;margin-bottom:10px}
.ch h3{font-family:var(--f);font-weight:800;line-height:1.1;
 font-size:clamp(16px,1.3vw,26px);color:var(--ink)}
.c p{font-size:clamp(14px,1.08vw,21px);line-height:1.4;color:var(--ink)}
.c p+p{margin-top:7px}
.c p.d{color:var(--dim)}
.c h4{font-size:clamp(13px,.9vw,17px);font-weight:800;margin-bottom:6px}
.hr{height:2px;background:rgba(0,0,0,.07);border-radius:2px;margin:10px 0 9px}
.c svg.fig{width:100%;height:auto;max-height:100%;display:block;margin:3px auto 0}
.figwrap{display:flex;flex:1 1 auto;min-height:0;min-width:0;align-items:center;justify-content:center;width:100%}
svg.fig{width:100%;height:auto;max-height:100%;display:block}
.g>*{min-width:0;min-height:0}
.kv{font-family:var(--m);font-weight:700}

/* ---------- номера ---------- */
.num{flex:none;width:34px;height:34px;border-radius:50%;display:grid;place-items:center;
 font:900 16px/1 var(--f);color:#fff;background:var(--pink)}
.num.b{background:var(--blue)} .num.y{background:var(--yellow);color:#121212}
.num.g{background:var(--green)} .num.v{background:var(--violet)} .num.w{background:#121212}
.num.sm{width:27px;height:27px;font-size:13px}

/* ---------- пилюли ---------- */
.tag{display:inline-block;padding:5px 13px;border-radius:999px;
 font:700 clamp(11.5px,.8vw,15px)/1.25 var(--f);background:var(--pink-bg);color:var(--pink-ink)}
.tag.b{background:var(--blue-bg);color:var(--blue-ink)}
.tag.y{background:var(--yellow-bg);color:var(--yellow-ink)}
.tag.g{background:var(--green-bg);color:var(--green-ink)}
.tag.v{background:var(--violet-bg);color:var(--violet-ink)}
.tag.w{background:#f2f5f8;color:#121212}
.tag.mono{font-family:var(--m);letter-spacing:.01em}
.tags{display:flex;gap:7px;flex-wrap:wrap;align-items:center}

/* ---------- строки с иконкой ---------- */
.ir{display:flex;align-items:center;gap:11px;background:#fff;border-radius:var(--r2);padding:8px 12px}
.ir+.ir{margin-top:7px}
.c.w .ir{background:#f7fafd}
.ir .ib{flex:none;width:30px;height:30px;border-radius:999px;background:var(--pink);display:grid;place-items:center}
.ir.b .ib{background:var(--blue)} .ir.y .ib{background:var(--yellow)}
.ir.g .ib{background:var(--green)} .ir.v .ib{background:var(--violet)}
.ir .ib svg{width:17px;height:17px;fill:none;stroke:#fff;stroke-width:1.9;stroke-linecap:round;stroke-linejoin:round}
.ir.y .ib svg{stroke:#121212}
.ir span:last-child{font-size:clamp(14px,1.05vw,20px);line-height:1.35}
.ir b{font-weight:800}

/* ---------- сноски ---------- */
.foot{display:flex;align-items:center;gap:12px;background:var(--blue-bg);border-radius:var(--r2);
 padding:11px 16px;font-weight:700;font-size:clamp(14px,1.05vw,20px);line-height:1.35}
.foot i{flex:none;width:28px;height:28px;border-radius:999px;background:var(--blue);color:#fff;
 display:grid;place-items:center;font:900 16px/1 var(--f);font-style:normal}
.foot.warn{background:var(--pink-bg)} .foot.warn i{background:var(--pink)}
.foot.ok{background:var(--green-bg)} .foot.ok i{background:var(--green)}
.foot.note{background:var(--yellow-bg)} .foot.note i{background:var(--yellow);color:#121212}

/* ---------- таблицы ---------- */
.tw{overflow:auto;border-radius:var(--r2);background:#fff}
.tw table{border-collapse:collapse;width:100%;font-size:clamp(13.5px,1.0vw,19px)}
.tw th{background:var(--pink-bg);color:var(--ink);font-weight:800;text-align:left;
 padding:9px 12px;white-space:nowrap}
.tw th.b{background:var(--blue-bg)} .tw th.y{background:var(--yellow-bg)}
.tw td{padding:8px 12px;border-top:1px solid var(--line);line-height:1.35;vertical-align:top}
.tw tbody tr:nth-child(even){background:#fff6fa}
.tw tr.hi{background:var(--yellow-bg)!important;box-shadow:inset 0 0 0 2px var(--yellow)}
.tw td.mono,.tw th.mono{font-family:var(--m);font-weight:700;white-space:nowrap}
.tw td.c,.tw th.c{text-align:center}

/* ---------- CLI ---------- */
.cli{background:#111820;border-radius:var(--r2);padding:13px 16px;overflow:auto;max-height:100%}
.cli pre{font-family:var(--m);font-size:clamp(11.5px,.78vw,15px);line-height:1.52;color:#dfe8f2;white-space:pre-wrap}
.cli .pr{color:#7fd6ff}
.cli .cm{color:#ffe08a;font-weight:700}
.cli .rem{color:#86939f;font-style:italic}
.cli .cur{display:inline-block;width:8px;height:1em;background:#ffe08a;vertical-align:-2px;
 animation:bl .9s steps(1) infinite}
@keyframes bl{50%{opacity:0}}

/* ---------- картинка-референс ---------- */
.figimg{border-radius:var(--r);overflow:hidden;background:#fff;box-shadow:0 3px 14px rgba(40,60,90,.09);
 display:flex;align-items:center;justify-content:center;min-height:0}
.figimg img{width:100%;height:100%;object-fit:contain;display:block}
.figcap{margin-top:7px;font-size:clamp(11.5px,.78vw,15px);color:var(--dim);font-weight:700}

/* ---------- сетки ---------- */
.g{display:grid;gap:13px}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.g5{grid-template-columns:repeat(5,1fr)}
.g7{grid-template-columns:repeat(7,1fr)}
.g21{grid-template-columns:2fr 1fr}
.g12{grid-template-columns:1fr 2fr}
.g32{grid-template-columns:3fr 2fr}
.g23{grid-template-columns:2fr 3fr}

/* ---------- шаги ---------- */
.step{opacity:0;transform:translateY(10px);transition:opacity .28s var(--ease),transform .28s var(--ease)}
.step.vis{opacity:1;transform:none}

/* ---------- сценарные классы ---------- */
.go-f{opacity:0;transition:opacity .34s var(--ease)}
.go-f.go{opacity:1}
.dash{stroke-dasharray:var(--L,400);stroke-dashoffset:var(--L,400);transition:stroke-dashoffset .72s var(--ease)}
.dash.go{stroke-dashoffset:0}
.pop{transform:scale(.6);opacity:0;transform-origin:center;transition:transform .32s var(--ease),opacity .32s var(--ease)}
.pop.go{transform:scale(1);opacity:1}
.fade30{opacity:1;transition:opacity .4s var(--ease)}
.fade30.dim{opacity:.3}
.halo{opacity:0;transition:opacity .3s var(--ease)}
.halo.go{opacity:1}

/* ---------- титул ---------- */
.cover-slide{justify-content:center;align-items:flex-start}
.cover h1{font-family:var(--fd);font-weight:700;line-height:.86;
 font-size:clamp(44px,7.6vw,150px);text-transform:uppercase;letter-spacing:-.02em}
.cover .lead{margin-top:16px;font-size:clamp(15px,1.5vw,30px);font-weight:800;max-width:900px;line-height:1.26}
.cover .who{margin-top:22px;display:flex;gap:9px;flex-wrap:wrap}

/* ---------- вёрстка в стиле инфографик ---------- */
.split{display:grid;gap:clamp(14px,1.4vw,26px);flex:1 1 0;min-height:0}
.lcol>.step{display:flex;flex-direction:column;flex:1 1 0;min-height:0}
.lcol>.step>*{flex:1 1 auto}
.rcol>.step{flex:none}
.split>.lcol{display:flex;flex-direction:column;gap:clamp(10px,.9vw,16px);min-height:0;min-width:0}
.split>.rcol{display:flex;flex-direction:column;gap:12px;min-height:0;min-width:0}
.ill{flex:1 1 auto;min-height:0;border-radius:24px;overflow:hidden;
 background:linear-gradient(135deg,#fff3f8 0%,#f6f9ff 55%,#eef6ff 100%);display:flex}
.ill>svg{width:100%;height:100%;display:block}
.ill.plain{background:transparent}

.rowc{display:grid;grid-template-columns:auto 1fr;gap:clamp(12px,1.1vw,22px);align-items:center;background:#fff;
 border:2px solid var(--pink-bg);border-radius:22px;padding:clamp(10px,.9vw,18px) clamp(14px,1.2vw,24px);
 box-shadow:0 3px 14px rgba(40,60,90,.05);flex:1 1 0;min-height:0}
.rowc.b{border-color:var(--blue-bg)} .rowc.y{border-color:var(--yellow-bg)}
.rowc.g{border-color:var(--green-bg)} .rowc.v{border-color:var(--violet-bg)}
.rowc .ico,.tile .ico{flex:none;width:clamp(52px,4.6vw,92px);height:clamp(52px,4.6vw,92px);border-radius:50%;
 background:#ffd3e4;display:grid;place-items:center}
.rowc.b .ico,.tile.b .ico{background:#c7e2fb} .rowc.y .ico,.tile.y .ico{background:#ffe9a8}
.rowc.g .ico,.tile.g .ico{background:#c6efd6} .rowc.v .ico,.tile.v .ico{background:#ddd2fa}
.rowc .ico svg,.tile .ico svg{width:52%;height:52%;fill:none;stroke:#121212;stroke-width:1.9;
 stroke-linecap:round;stroke-linejoin:round}
.rowc h3{font:800 clamp(18px,1.6vw,32px)/1.1 var(--f);margin-bottom:5px}
.rowc p{font-size:clamp(15px,1.22vw,24px);line-height:1.3}
.rowc p b{font-weight:800}

.tile{position:relative;background:#fff;border:2px solid var(--pink-bg);border-radius:24px;
 padding:clamp(14px,1.2vw,24px);display:flex;flex-direction:column;gap:6px;min-height:0;
 box-shadow:0 3px 14px rgba(40,60,90,.05)}
.tile.b{border-color:var(--blue-bg)} .tile.y{border-color:var(--yellow-bg)}
.tile.g{border-color:var(--green-bg)} .tile.v{border-color:var(--violet-bg)}
.tile .dash{position:absolute;left:calc(clamp(52px,4.6vw,92px) + 34px);top:clamp(34px,2.8vw,56px);
 width:22%;height:9px;border-radius:9px;background:#ffd3e4}
.tile.b .dash{background:#c7e2fb} .tile.y .dash{background:#ffe9a8} .tile.g .dash{background:#c6efd6}
.tile h3{font:700 clamp(22px,2.0vw,40px)/1 var(--fd);margin-top:6px}
.tile p{font-size:clamp(15px,1.2vw,23px);line-height:1.3}

.nrow{display:grid;grid-template-columns:auto minmax(0,1.05fr) auto minmax(0,1.25fr);gap:clamp(10px,1vw,20px);
 align-items:center;background:var(--pink-bg);border-radius:22px;padding:clamp(6px,.55vw,11px) clamp(12px,1vw,20px);
 flex:1 1 0;min-height:0}
.nrow.b{background:var(--blue-bg)} .nrow.y{background:var(--yellow-bg)} .nrow.g{background:var(--green-bg)}
.nrow.v{background:var(--violet-bg)}
.nrow .nn{width:clamp(38px,3.2vw,62px);height:clamp(38px,3.2vw,62px);border-radius:50%;background:var(--pink);
 color:#fff;display:grid;place-items:center;font:700 clamp(20px,1.9vw,36px)/1 var(--fd)}
.nrow.b .nn{background:var(--blue)} .nrow.y .nn{background:var(--yellow);color:#121212}
.nrow.g .nn{background:var(--green)} .nrow.v .nn{background:var(--violet)}
.nrow h3{font:800 clamp(15px,1.3vw,26px)/1.12 var(--f)}
.nrow .nill svg{width:clamp(44px,3.8vw,74px);height:clamp(40px,3.2vw,62px);display:block}
.nrow p{font-size:clamp(13px,1.05vw,20px);line-height:1.28}
svg.mini{display:block}
.rowc>svg.mini{width:100%;height:clamp(64px,13vh,150px)}
.col>.ill{flex:1 1 0;min-height:120px}
.col>.step{flex:none}
.col>.step>.rowc{flex:none}
.tile .ico{width:clamp(44px,3.6vw,72px);height:clamp(44px,3.6vw,72px)}
.tile .dash{left:calc(clamp(44px,3.6vw,72px) + 34px);top:clamp(30px,2.4vw,46px)}
.tile h3{font-size:clamp(20px,1.75vw,36px)}

.wide>.step{display:flex;flex-direction:column;min-height:0}
.wide>.step>.rowc{flex:1 1 auto}
.big-cover{display:grid;grid-template-columns:minmax(0,40fr) minmax(0,60fr);gap:24px;flex:1 1 auto;min-height:0;align-items:stretch}
.big-cover .ttl{display:flex;flex-direction:column;justify-content:center;gap:16px}
.big-cover h1{font:700 clamp(54px,8.2vw,170px)/.84 var(--fd);text-transform:uppercase;letter-spacing:-.01em}
.big-cover .lead{font:800 clamp(18px,1.9vw,38px)/1.18 var(--f)}
.big-cover .lead u{text-decoration:none;background:linear-gradient(transparent 62%,#ffd93d 62%)}

.wide{display:grid;gap:clamp(10px,1vw,18px)}

/* ---------- тренажёры ---------- */
.ui{display:flex;gap:8px;flex-wrap:wrap;align-items:center}
.ui button,.btn{font:800 clamp(12px,.84vw,15.5px)/1 var(--f);padding:10px 16px;border:none;cursor:pointer;
 border-radius:999px;background:var(--blue-bg);color:var(--blue-ink);transition:transform .14s var(--ease),background .18s}
.ui button:hover,.btn:hover{transform:translateY(-1px);background:var(--blue-soft)}
.ui button.pri{background:var(--pink);color:#fff}
.ui button.pri:hover{background:#ff3d8c}
.ui button.on{background:var(--green);color:#fff}
.ui button:disabled{opacity:.42;cursor:default;transform:none}
button:focus-visible,.btn:focus-visible{outline:3px solid var(--violet);outline-offset:2px}
.vbtn{font:800 clamp(13px,.92vw,17px)/1 var(--f);padding:11px 8px;border:none;cursor:pointer;border-radius:14px;
 background:#fff;color:var(--ink);box-shadow:0 2px 8px rgba(40,60,90,.1);transition:transform .14s var(--ease)}
.vbtn:hover{transform:translateY(-2px)}
.vbtn.good{background:var(--green);color:#fff}
.vbtn.bad{background:var(--pink);color:#fff}
.vbtn:disabled{cursor:default}
.note{font-size:clamp(12.5px,.86vw,16px);line-height:1.42;font-weight:700;min-height:2.6em}
.rw{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;background:#fff;border-radius:12px;
 padding:8px 12px;font-size:clamp(12px,.82vw,15.5px);transition:background .3s}
.rw+.rw{margin-top:6px}
.rw.upd{background:var(--yellow-bg);box-shadow:inset 0 0 0 2px var(--yellow)}
.rw.done{background:var(--green-bg)}
.stat{display:flex;gap:9px;flex-wrap:wrap}
.stat span{background:#fff;border-radius:999px;padding:6px 14px;font-weight:800;font-size:clamp(12px,.82vw,15px)}
.stat b{color:var(--pink-ink)}

/* ---------- выравнивание тренажёров ---------- */
#dijsim,#costsim{display:grid!important;grid-template-rows:1fr auto;gap:13px;min-height:0}
#dijsim>.g,#costsim>.g{min-height:0}
#dijsim .col,#costsim .col{min-height:0}
#dijsim .col>.c:first-child{flex:1 1 auto;overflow:auto}
#dijsim .figwrap,#costsim .figwrap{align-items:flex-start}

/* ---------- квиз ---------- */
.q{background:#fff;border-radius:var(--r);padding:clamp(13px,1.05vw,20px);box-shadow:0 3px 14px rgba(40,60,90,.07)}
.q .qt{font-weight:800;font-size:clamp(13px,.95vw,18px);line-height:1.38;margin-bottom:11px}
.q .opts{display:grid;gap:8px}
.q .opts.two{grid-template-columns:1fr 1fr}
.q .ex{display:none;margin-top:11px;background:var(--yellow-bg);border-radius:14px;padding:10px 14px;
 font-size:clamp(12.5px,.86vw,16px);line-height:1.42;font-weight:700}
.q .ex.on{display:block}

/* ---------- HUD ---------- */
#prog{position:fixed;left:0;top:0;height:4px;background:linear-gradient(90deg,var(--pink),var(--blue));
 z-index:40;transition:width .3s var(--ease)}
#hud{position:fixed;left:0;right:0;bottom:0;height:60px;z-index:30;display:flex;align-items:center;
 gap:9px;padding:0 clamp(16px,2.4vw,46px);background:rgba(255,255,255,.93);
 backdrop-filter:blur(8px);border-top:1px solid var(--line)}
#hud button{font:800 13px/1 var(--f);padding:9px 15px;border:none;border-radius:999px;cursor:pointer;
 background:var(--pink-bg);color:var(--pink-ink);transition:transform .14s var(--ease)}
#hud button:hover{transform:translateY(-1px);background:var(--pink-soft)}
#count{font:800 13px/1 var(--f);color:var(--dim);margin-left:8px;white-space:nowrap}
#sname{font:800 13px/1 var(--f);color:var(--ink);margin-left:6px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#hud .hint{margin-left:auto;font-size:11.5px;color:var(--dim);white-space:nowrap}

/* ---------- содержание ---------- */
#toc{position:fixed;inset:0;z-index:50;background:rgba(255,255,255,.97);display:none;
 padding:clamp(24px,3vw,54px);overflow:auto}
#toc.on{display:block}
#toc h2{font-family:var(--fd);font-weight:900;font-stretch:condensed;font-size:clamp(28px,3.4vw,58px);
 text-transform:uppercase;margin-bottom:18px}
#tocg{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:9px}
.tocit{display:flex;align-items:center;gap:10px;background:var(--pink-bg);border:none;border-radius:14px;
 padding:9px 13px;cursor:pointer;text-align:left;font:700 13px/1.3 var(--f);color:var(--ink);
 transition:transform .14s var(--ease)}
.tocit:hover{transform:translateY(-2px);background:var(--pink-soft)}
.tocit i{flex:none;width:26px;height:26px;border-radius:999px;background:var(--pink);color:#fff;
 display:grid;place-items:center;font:900 12px/1 var(--f);font-style:normal}

/* ---------- адаптив ---------- */
@media (max-width:1199px){
  .g7{grid-template-columns:repeat(4,1fr)}
  .g5{grid-template-columns:repeat(3,1fr)}
  .g4{grid-template-columns:repeat(2,1fr)}
}
@media (max-width:699px){
  .slide{padding:14px 16px 70px}
  h1.t{font-size:28px}
  .g7,.g5,.g4,.g3,.g2,.g21,.g12,.g32,.g23{grid-template-columns:1fr 1fr}
  .g21,.g12,.g32,.g23,.g3{grid-template-columns:1fr}
  .head .sparks{display:none}
  #hud .hint{display:none}
  .q .opts.two{grid-template-columns:1fr}
}
@media (prefers-reduced-motion: reduce){
  .step,.go-f,.pop,.dash,.halo{transition:none!important}
  .step{opacity:1;transform:none}
}
@media print{#hud,#prog,#toc{display:none}}
"""
