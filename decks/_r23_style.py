# -*- coding: utf-8 -*-
"""Стиль деки «Маршрутизаторы» (2.3): фиолетовое стекло, неоновый город, глянцевые карточки."""

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
--paper:#ffffff;
--vio:#6d4aff; --vio-bg:#ece8ff; --vio-soft:#d8d0ff; --vio-ink:#4327c9;
--ind:#4f46e5; --ind-bg:#e8e9ff; --ind-ink:#312bb0;
--cya:#1fb6e8; --cya-bg:#e0f5fd; --cya-soft:#bfe9fa; --cya-ink:#0a6f94;
--mag:#d64ae8; --mag-bg:#fbe8ff; --mag-soft:#f3cdfb; --mag-ink:#9d1eb0;
--grn:#16b16c; --grn-bg:#e1f7ee; --grn-ink:#0c7a49;
--amb:#f0a419; --amb-bg:#fff3da; --amb-ink:#8a5c00;
--red:#f0486b; --red-bg:#ffe6ec; --red-ink:#b11c3d;
--ink:#1a1142; --dim:#5d5682; --line:#e5e0f7;
--glass:rgba(255,255,255,.74); --glass2:rgba(255,255,255,.92);
--r:20px; --r2:14px;
--ease:cubic-bezier(.22,.7,.3,1);
--f:"Golos Text","Inter","Segoe UI Variable Text","Segoe UI",system-ui,-apple-system,Arial,sans-serif;
--fd:"Druk Cyr","Oswald","Anton","Arial Black","Golos Text",system-ui,sans-serif;
--m:"Cascadia Mono","JetBrains Mono",Consolas,"SF Mono",ui-monospace,monospace;
}
html,body{height:100%}
body{font-family:var(--f);color:var(--ink);background:#f3f1ff;overflow:hidden;
-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* ================= ФОН ================= */
#bg{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}
#bg .drift{animation:drift 26s ease-in-out infinite alternate}
#bg .drift2{animation:drift 34s ease-in-out infinite alternate-reverse}
@keyframes drift{from{transform:translate(0,0)}to{transform:translate(-26px,16px)}}
#bg .spin{transform-box:fill-box;transform-origin:center;animation:spin 90s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
#bg .twk{animation:twk 3.6s ease-in-out infinite}
#bg .twk:nth-of-type(2n){animation-duration:5.1s;animation-delay:-1.4s}
#bg .twk:nth-of-type(3n){animation-duration:4.3s;animation-delay:-2.6s}
@keyframes twk{0%,100%{opacity:.18}50%{opacity:.85}}
#bg .flow{stroke-dasharray:10 150;animation:flow 7s linear infinite}
#bg .flow:nth-of-type(2n){animation-duration:9.5s;animation-delay:-3s}
@keyframes flow{to{stroke-dashoffset:-320}}
#bg .rise{animation:rise 17s linear infinite}
#bg .rise:nth-of-type(3n){animation-duration:23s;animation-delay:-8s}
#bg .rise:nth-of-type(3n+1){animation-duration:20s;animation-delay:-14s}
@keyframes rise{0%{transform:translateY(0);opacity:0}12%{opacity:.75}88%{opacity:.6}100%{transform:translateY(-230px);opacity:0}}

/* ================= КАРКАС ================= */
#stage{position:fixed;inset:0;z-index:1}
.slide{position:absolute;inset:0;padding:clamp(16px,1.8vw,34px) clamp(18px,2.4vw,48px) 72px;
 display:none;overflow:hidden;flex-direction:column}
.slide.on{display:flex}
.slide>.sc{flex:1;min-height:0;overflow:auto;padding-right:6px;scrollbar-width:thin;
 scrollbar-color:var(--vio-soft) transparent;display:flex;flex-direction:column;gap:12px}
.slide>.sc::-webkit-scrollbar{width:8px}
.slide>.sc::-webkit-scrollbar-thumb{background:var(--vio-soft);border-radius:8px}
.slide>.sc>.g{flex:0 0 auto}
.slide>.sc>.grow{flex:1 1 auto;min-height:0}
.g>.step{display:flex;flex-direction:column;min-height:0}
.g>.step>.c{flex:1 1 auto}
.g>.c{height:100%}
.col{display:flex;flex-direction:column;gap:12px;min-width:0}
.col>.step{display:flex;flex-direction:column}
.col>.step>.c{flex:1 1 auto}

/* ================= ЗАГОЛОВОК ================= */
.head{flex:none;margin-bottom:4px;display:flex;align-items:flex-start;gap:14px;position:relative}
h1.t{font-family:var(--fd);font-weight:800;line-height:.94;
 font-size:clamp(24px,2.85vw,52px);color:var(--ink);letter-spacing:-.015em}
h1.t em{font-style:normal;background:linear-gradient(97deg,var(--vio),var(--mag) 55%,var(--cya));
 -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
p.sub{margin-top:7px;font-size:clamp(12.5px,.98vw,18px);color:var(--dim);font-weight:600;line-height:1.36;max-width:1240px}
p.sub b{color:var(--vio-ink);font-weight:800}
.head .spark{flex:none;width:clamp(40px,3.6vw,66px);height:44px;margin-top:3px;opacity:.9}

/* ================= КАРТОЧКИ ================= */
.c{background:var(--glass);backdrop-filter:blur(9px);-webkit-backdrop-filter:blur(9px);
 border:1px solid rgba(255,255,255,.75);border-radius:var(--r);
 padding:clamp(12px,1vw,20px) clamp(13px,1.1vw,22px);
 box-shadow:0 10px 30px rgba(60,40,140,.10),inset 0 1px 0 rgba(255,255,255,.9);
 display:flex;flex-direction:column;position:relative;min-width:0}
.c.vio{background:linear-gradient(160deg,rgba(236,232,255,.95),rgba(236,232,255,.68))}
.c.cya{background:linear-gradient(160deg,rgba(224,245,253,.95),rgba(224,245,253,.68))}
.c.mag{background:linear-gradient(160deg,rgba(251,232,255,.95),rgba(251,232,255,.68))}
.c.grn{background:linear-gradient(160deg,rgba(225,247,238,.95),rgba(225,247,238,.68))}
.c.amb{background:linear-gradient(160deg,rgba(255,243,218,.95),rgba(255,243,218,.68))}
.c.red{background:linear-gradient(160deg,rgba(255,230,236,.95),rgba(255,230,236,.68))}
.c.ind{background:linear-gradient(160deg,rgba(232,233,255,.95),rgba(232,233,255,.68))}
.c.w{background:var(--glass2)}
.c.dark{background:linear-gradient(160deg,#241a55,#17103c);border-color:rgba(140,110,255,.3);color:#efeaff}
.c.dark h3,.c.dark p,.c.dark h4{color:#efeaff}
.ch{display:flex;align-items:center;gap:10px;margin-bottom:9px}
.ch h3{font-family:var(--fd);font-weight:800;line-height:1.06;
 font-size:clamp(14px,1.08vw,23px);color:var(--ink);letter-spacing:-.005em}
.c p{font-size:clamp(12px,.86vw,16.5px);line-height:1.47;color:var(--ink)}
.c p+p{margin-top:6px}
.c p.d{color:var(--dim)}
.c h4{font-size:clamp(12.5px,.88vw,16.5px);font-weight:800;margin-bottom:5px}
.hr{height:1px;background:rgba(109,74,255,.16);margin:9px 0 8px}
.kv{font-family:var(--m);font-weight:700}
.c svg.fig{width:100%;height:auto;max-height:100%;display:block;margin:2px auto 0}
.figwrap{display:flex;flex:1 1 auto;min-height:0;min-width:0;align-items:center;justify-content:center;width:100%}
svg.fig{width:100%;height:auto;max-height:100%;display:block}
.g>*{min-width:0;min-height:0}

/* ================= НОМЕРА / ПИЛЮЛИ ================= */
.num{flex:none;width:32px;height:32px;border-radius:11px;display:grid;place-items:center;
 font:800 15px/1 var(--f);color:#fff;background:linear-gradient(145deg,var(--vio),#8a63ff);
 box-shadow:0 5px 14px rgba(109,74,255,.34)}
.num.c2{background:linear-gradient(145deg,var(--cya),#5ad2f5);box-shadow:0 5px 14px rgba(31,182,232,.32)}
.num.m{background:linear-gradient(145deg,var(--mag),#ee7bfb);box-shadow:0 5px 14px rgba(214,74,232,.3)}
.num.g{background:linear-gradient(145deg,var(--grn),#3fd394);box-shadow:0 5px 14px rgba(22,177,108,.3)}
.num.a{background:linear-gradient(145deg,var(--amb),#ffc55c);box-shadow:0 5px 14px rgba(240,164,25,.3);color:#3a2600}
.num.r{background:linear-gradient(145deg,var(--red),#ff7d99);box-shadow:0 5px 14px rgba(240,72,107,.3)}
.num.i{background:linear-gradient(145deg,var(--ind),#7b74ff)}
.num.sm{width:26px;height:26px;font-size:12.5px;border-radius:9px}
.tag{display:inline-block;padding:5px 12px;border-radius:999px;
 font:700 clamp(11px,.78vw,14.5px)/1.25 var(--f);background:var(--vio-bg);color:var(--vio-ink)}
.tag.c2{background:var(--cya-bg);color:var(--cya-ink)}
.tag.m{background:var(--mag-bg);color:var(--mag-ink)}
.tag.g{background:var(--grn-bg);color:var(--grn-ink)}
.tag.a{background:var(--amb-bg);color:var(--amb-ink)}
.tag.r{background:var(--red-bg);color:var(--red-ink)}
.tag.w{background:rgba(255,255,255,.85);color:var(--ink)}
.tag.sol{background:linear-gradient(135deg,var(--vio),var(--mag));color:#fff}
.tag.mono{font-family:var(--m)}
.tags{display:flex;gap:6px;flex-wrap:wrap;align-items:center}

/* ================= СТРОКИ С ИКОНКОЙ ================= */
.ir{display:flex;align-items:center;gap:10px;background:rgba(255,255,255,.8);border-radius:var(--r2);padding:8px 11px}
.ir+.ir{margin-top:6px}
.ir .ib{flex:none;width:29px;height:29px;border-radius:10px;background:linear-gradient(145deg,var(--vio),#8a63ff);display:grid;place-items:center}
.ir.c2 .ib{background:linear-gradient(145deg,var(--cya),#5ad2f5)}
.ir.m .ib{background:linear-gradient(145deg,var(--mag),#ee7bfb)}
.ir.g .ib{background:linear-gradient(145deg,var(--grn),#3fd394)}
.ir.a .ib{background:linear-gradient(145deg,var(--amb),#ffc55c)}
.ir.r .ib{background:linear-gradient(145deg,var(--red),#ff7d99)}
.ir .ib svg{width:16px;height:16px;fill:none;stroke:#fff;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.ir.a .ib svg{stroke:#3a2600}
.ir span:last-child{font-size:clamp(12px,.84vw,16px);line-height:1.4}
.ir b{font-weight:800}

/* ================= СНОСКИ ================= */
.foot{display:flex;align-items:center;gap:11px;border-radius:var(--r2);padding:10px 14px;
 font-weight:600;font-size:clamp(12px,.84vw,16px);line-height:1.4;
 background:linear-gradient(120deg,rgba(236,232,255,.95),rgba(224,245,253,.8))}
.foot i{flex:none;width:27px;height:27px;border-radius:9px;background:var(--vio);color:#fff;
 display:grid;place-items:center;font:800 15px/1 var(--f);font-style:normal}
.foot b{font-weight:800}
.foot.warn{background:linear-gradient(120deg,rgba(255,230,236,.95),rgba(255,243,218,.8))}
.foot.warn i{background:var(--red)}
.foot.ok{background:linear-gradient(120deg,rgba(225,247,238,.95),rgba(224,245,253,.8))}
.foot.ok i{background:var(--grn)}
.foot.note{background:linear-gradient(120deg,rgba(255,243,218,.95),rgba(251,232,255,.8))}
.foot.note i{background:var(--amb);color:#3a2600}

/* ================= ТАБЛИЦЫ ================= */
.tw{overflow:auto;border-radius:var(--r2);background:rgba(255,255,255,.9)}
.tw table{border-collapse:collapse;width:100%;font-size:clamp(11.5px,.8vw,15.5px)}
.tw th{background:var(--vio-bg);color:var(--vio-ink);font-weight:800;text-align:left;padding:9px 11px;white-space:nowrap}
.tw th.c2{background:var(--cya-bg);color:var(--cya-ink)}
.tw th.m{background:var(--mag-bg);color:var(--mag-ink)}
.tw th.a{background:var(--amb-bg);color:var(--amb-ink)}
.tw td{padding:8px 11px;border-top:1px solid var(--line);line-height:1.36;vertical-align:top}
.tw tbody tr:nth-child(even){background:rgba(240,238,255,.5)}
.tw tr.hi{background:var(--amb-bg)!important;box-shadow:inset 0 0 0 2px var(--amb)}
.tw tr.ok{background:var(--grn-bg)!important}
.tw td.mono,.tw th.mono{font-family:var(--m);font-weight:700;white-space:nowrap}
.tw td.c,.tw th.c{text-align:center}

/* ================= CLI ================= */
.cli{background:linear-gradient(165deg,#1d1450,#120c33);border-radius:var(--r2);
 padding:12px 15px;overflow:auto;max-height:100%;border:1px solid rgba(140,110,255,.28);
 box-shadow:inset 0 0 60px rgba(109,74,255,.16)}
.cli pre{font-family:var(--m);font-size:clamp(11px,.76vw,14.5px);line-height:1.56;color:#d9d2ff;white-space:pre-wrap;word-break:break-word}
.cli .pr{color:#5fd8ff}
.cli .cm{color:#ffd76a;font-weight:700}
.cli .rem{color:#8e86bd;font-style:italic}
.cli .out{color:#bdb4ea}
.cli .hl{color:#6bf0b0;font-weight:700}
.cli .er{color:#ff8fae;font-weight:700}
.cli .cur{display:inline-block;width:8px;height:1em;background:#ffd76a;vertical-align:-2px;animation:bl .9s steps(1) infinite}
@keyframes bl{50%{opacity:0}}
.clicap{font-size:clamp(11px,.76vw,14.5px);color:var(--dim);font-weight:700;margin-bottom:6px}

/* ================= КАРТИНКИ ================= */
.figimg{border-radius:var(--r);overflow:hidden;background:rgba(255,255,255,.7);
 box-shadow:0 10px 30px rgba(60,40,140,.14);display:flex;align-items:center;justify-content:center;min-height:0;
 border:1px solid rgba(255,255,255,.7)}
.figimg img{width:100%;height:100%;object-fit:contain;display:block}
.figcap{margin-top:6px;font-size:clamp(11px,.76vw,14.5px);color:var(--dim);font-weight:700}

/* ================= СЕТКИ ================= */
.g{display:grid;gap:12px}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.g5{grid-template-columns:repeat(5,1fr)}
.g6{grid-template-columns:repeat(6,1fr)}
.g21{grid-template-columns:2fr 1fr}
.g12{grid-template-columns:1fr 2fr}
.g32{grid-template-columns:3fr 2fr}
.g23{grid-template-columns:2fr 3fr}
.g31{grid-template-columns:3fr 1fr}
.g13{grid-template-columns:1fr 3fr}

/* ================= ШАГИ ================= */
.step{opacity:0;transform:translateY(12px);transition:opacity .3s var(--ease),transform .3s var(--ease)}
.step.vis{opacity:1;transform:none}
.go-f{opacity:0;transition:opacity .36s var(--ease)}
.go-f.go{opacity:1}
.dash{stroke-dasharray:var(--L,400);stroke-dashoffset:var(--L,400);transition:stroke-dashoffset .75s var(--ease)}
.dash.go{stroke-dashoffset:0}
.pop{transform:scale(.55);opacity:0;transform-origin:center;transition:transform .34s var(--ease),opacity .34s var(--ease)}
.pop.go{transform:scale(1);opacity:1}
.fade30{opacity:1;transition:opacity .4s var(--ease)}
.fade30.dim{opacity:.22}
.halo{opacity:0;transition:opacity .3s var(--ease)}
.halo.go{opacity:1}
.pulse.go{animation:pul 1.5s ease-in-out infinite}
@keyframes pul{0%,100%{opacity:.35}50%{opacity:1}}

/* ================= ТИТУЛ ================= */
.cover-slide{justify-content:center;align-items:flex-start}
.cover h1{font-family:var(--fd);font-weight:800;line-height:.9;
 font-size:clamp(40px,7vw,138px);letter-spacing:-.025em;
 background:linear-gradient(100deg,#2a1b7a,#6d4aff 42%,#d64ae8 72%,#1fb6e8);
 -webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.cover .lead{margin-top:14px;font-size:clamp(14px,1.4vw,28px);font-weight:700;max-width:960px;line-height:1.3;color:var(--ink)}
.cover .who{margin-top:20px;display:flex;gap:8px;flex-wrap:wrap}

/* ================= КНОПКИ / ТРЕНАЖЁРЫ ================= */
.ui{display:flex;gap:7px;flex-wrap:wrap;align-items:center}
.ui button,.btn{font:800 clamp(11.5px,.8vw,15px)/1 var(--f);padding:10px 15px;border:none;cursor:pointer;
 border-radius:999px;background:rgba(255,255,255,.9);color:var(--vio-ink);
 box-shadow:0 4px 12px rgba(60,40,140,.12);transition:transform .14s var(--ease),background .18s}
.ui button:hover,.btn:hover{transform:translateY(-1px);background:#fff}
.ui button.pri{background:linear-gradient(135deg,var(--vio),var(--mag));color:#fff}
.ui button.on{background:linear-gradient(135deg,var(--grn),#3fd394);color:#fff}
.ui button:disabled{opacity:.42;cursor:default;transform:none}
button:focus-visible,.btn:focus-visible,input:focus-visible{outline:3px solid var(--cya);outline-offset:2px}
.vbtn{font:800 clamp(12px,.88vw,16px)/1.25 var(--f);padding:11px 10px;border:none;cursor:pointer;border-radius:13px;
 background:rgba(255,255,255,.92);color:var(--ink);box-shadow:0 5px 16px rgba(60,40,140,.13);
 transition:transform .14s var(--ease);text-align:left}
.vbtn:hover{transform:translateY(-2px)}
.vbtn.good{background:linear-gradient(135deg,var(--grn),#3fd394);color:#fff}
.vbtn.bad{background:linear-gradient(135deg,var(--red),#ff7d99);color:#fff}
.vbtn:disabled{cursor:default}
input.fld{font:800 clamp(12px,.88vw,16px)/1 var(--m);padding:10px 13px;border-radius:12px;
 border:2px solid var(--vio-soft);background:#fff;color:var(--ink);width:100%;max-width:260px}
.note{font-size:clamp(12px,.84vw,15.5px);line-height:1.45;font-weight:600;min-height:2.6em}
.note b{font-weight:800}
.rw{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;background:rgba(255,255,255,.88);border-radius:12px;
 padding:8px 12px;font-size:clamp(11.5px,.8vw,15px);transition:background .3s;align-items:center}
.rw+.rw{margin-top:6px}
.rw.upd{background:var(--amb-bg);box-shadow:inset 0 0 0 2px var(--amb)}
.rw.done{background:var(--grn-bg)}
.rw.bad{background:var(--red-bg)}
.stat{display:flex;gap:8px;flex-wrap:wrap}
.stat span{background:rgba(255,255,255,.9);border-radius:999px;padding:6px 13px;font-weight:800;font-size:clamp(11.5px,.8vw,14.5px)}
.stat b{color:var(--vio-ink)}

/* ================= ТРЕНАЖЁРЫ: ВЫРАВНИВАНИЕ =================*/
#gwsim,#costsim,#privsim,#cfgsim,#diagsim,#ifsim{justify-content:center}

/* ================= КВИЗ ================= */
.q{background:var(--glass2);border-radius:var(--r);padding:clamp(12px,1vw,19px);
 box-shadow:0 10px 30px rgba(60,40,140,.10);border:1px solid rgba(255,255,255,.8)}
.q .qt{font-weight:800;font-size:clamp(12.5px,.92vw,17.5px);line-height:1.38;margin-bottom:10px}
.q .opts{display:grid;gap:7px}
.q .opts.two{grid-template-columns:1fr 1fr}
.q .ex{display:none;margin-top:10px;background:var(--amb-bg);border-radius:12px;padding:10px 13px;
 font-size:clamp(12px,.84vw,15.5px);line-height:1.44;font-weight:600}
.q .ex.on{display:block}

/* ================= HUD ================= */
#prog{position:fixed;left:0;top:0;height:4px;z-index:40;
 background:linear-gradient(90deg,var(--vio),var(--mag),var(--cya));transition:width .3s var(--ease)}
#hud{position:fixed;left:0;right:0;bottom:0;height:58px;z-index:30;display:flex;align-items:center;
 gap:8px;padding:0 clamp(14px,2.2vw,42px);background:rgba(255,255,255,.86);
 backdrop-filter:blur(12px);border-top:1px solid var(--line)}
#hud button{font:800 12.5px/1 var(--f);padding:9px 14px;border:none;border-radius:999px;cursor:pointer;
 background:var(--vio-bg);color:var(--vio-ink);transition:transform .14s var(--ease)}
#hud button:hover{transform:translateY(-1px);background:var(--vio-soft)}
#count{font:800 12.5px/1 var(--f);color:var(--dim);margin-left:8px;white-space:nowrap}
#sname{font:800 12.5px/1 var(--f);color:var(--ink);margin-left:6px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#hud .hint{margin-left:auto;font-size:11px;color:var(--dim);white-space:nowrap}

/* ================= СОДЕРЖАНИЕ ================= */
#toc{position:fixed;inset:0;z-index:50;background:rgba(243,241,255,.97);display:none;
 padding:clamp(22px,2.8vw,50px);overflow:auto}
#toc.on{display:block}
#toc h2{font-family:var(--fd);font-weight:800;font-size:clamp(26px,3.2vw,54px);margin-bottom:16px}
#tocg{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:8px}
.tocit{display:flex;align-items:center;gap:9px;background:rgba(255,255,255,.85);border:1px solid var(--line);
 border-radius:13px;padding:9px 12px;cursor:pointer;text-align:left;font:700 12.5px/1.3 var(--f);color:var(--ink);
 transition:transform .14s var(--ease)}
.tocit:hover{transform:translateY(-2px);background:var(--vio-bg)}
.tocit i{flex:none;width:25px;height:25px;border-radius:8px;background:linear-gradient(145deg,var(--vio),#8a63ff);
 color:#fff;display:grid;place-items:center;font:800 11.5px/1 var(--f);font-style:normal}

/* ================= АДАПТИВ ================= */
@media (max-width:1199px){
  .g6{grid-template-columns:repeat(3,1fr)}
  .g5{grid-template-columns:repeat(3,1fr)}
  .g4{grid-template-columns:repeat(2,1fr)}
}
@media (max-width:699px){
  .slide{padding:13px 15px 68px}
  h1.t{font-size:26px}
  .g6,.g5,.g4,.g3,.g2,.g21,.g12,.g32,.g23,.g31,.g13{grid-template-columns:1fr}
  .head .spark{display:none}
  #hud .hint{display:none}
  .q .opts.two{grid-template-columns:1fr}
  .rw{grid-template-columns:1fr}
}
@media (prefers-reduced-motion: reduce){
  .step,.go-f,.pop,.dash,.halo{transition:none!important}
  .step{opacity:1;transform:none}
  #bg *{animation:none!important}
}
@media print{#hud,#prog,#toc{display:none}}
"""
