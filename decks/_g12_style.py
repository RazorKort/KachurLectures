# -*- coding: utf-8 -*-
CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
--canvas:#e9f6f2; --deep:#0d332f; --deep-2:#12423c;
--panel-l:rgba(255,255,255,.80); --line-l:#cfe3dc; --line-d:rgba(94,224,200,.22);
--teal:#19b89f; --aqua:#5ee0c8; --green:#49d67f; --blue:#4aa3f0; --red:#ef5a5a;
--amber:#e8a33d; --violet:#9b7fe0;
--ink:#0f2e2b; --dim:#5c7d77; --on-dark:#eafaf6; --on-dark-dim:#9dc4bc;
--r:16px; --ease:cubic-bezier(.22,.7,.3,1);
--f:"Segoe UI Variable Display","Segoe UI",Inter,system-ui,-apple-system,"Helvetica Neue",Arial,sans-serif;
--m:"Cascadia Mono","JetBrains Mono",Consolas,"SF Mono",ui-monospace,monospace;
}
html,body{height:100%}
body{font-family:var(--f);color:var(--ink);background:var(--canvas);overflow:hidden;
-webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* ---------- фон ---------- */
#bg{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}

/* ---------- каркас ---------- */
#stage{position:fixed;inset:0;z-index:1}
.slide{position:absolute;inset:0;padding:clamp(24px,2.2vw,44px) clamp(26px,3vw,58px) 80px;display:none;overflow:hidden;flex-direction:column}
.slide.on{display:flex}
.slide>.sc{flex:1;min-height:0;overflow:auto;padding-right:6px;scrollbar-width:thin;
 scrollbar-color:#b4d3cb transparent;display:flex;flex-direction:column}
.slide>.sc>.g{flex:1 1 auto;align-content:stretch}
.slide>.sc>.g[style*="align-items:start"]{flex:0 0 auto}
.slide>.sc>.step{flex:0 0 auto}
.slide>.sc>.col{flex:1 1 auto}
.g>.step{display:flex;flex-direction:column;min-height:0}
.g>.step>.c,.g>.step>.q,.g>.step>.bub{flex:1 1 auto;min-height:0;height:auto}
.g>.c,.g>.q{min-height:100%;height:auto}
.col>.step{display:flex;flex-direction:column}
.col{min-height:0}
.slide>.sc::-webkit-scrollbar{width:8px}
.slide>.sc::-webkit-scrollbar-thumb{background:#b4d3cb;border-radius:8px}

h1.t{font-size:clamp(28px,2.9vw,56px);font-weight:800;letter-spacing:-.02em;line-height:1.05;color:#06201d}
h1.t em{font-style:normal;color:#0e8d78}
p.sub{margin-top:9px;font-size:clamp(14px,1.08vw,22px);color:#3f6660;max-width:1080px;line-height:1.42}
.head{margin-bottom:16px;flex:none}

/* ---------- карточки ---------- */
.c{border-radius:var(--r);padding:clamp(16px,1.2vw,24px) clamp(18px,1.3vw,26px);position:relative;
 display:flex;flex-direction:column}
.c.l{background:var(--panel-l);border:1px solid var(--line-l);box-shadow:0 6px 20px rgba(23,78,70,.07)}
.c.d{background:rgba(13,51,47,.93);border:1px solid var(--line-d);box-shadow:0 12px 34px rgba(5,32,29,.26);color:var(--on-dark-dim)}
.c.d h3,.c.d h4,.c.d b,.c.d strong{color:var(--on-dark)}
.c.tint{background:rgba(226,245,240,.9)}
.ch{display:flex;align-items:flex-start;gap:11px}
.ch h3{font-size:clamp(15px,1.12vw,23px);font-weight:750;line-height:1.2;flex:1;color:#0a2c28}
.c.d .ch h3{color:var(--on-dark)}
.num{flex:none;min-width:40px;height:32px;border-radius:8px;display:grid;place-items:center;
 font:800 clamp(14px,.95vw,18px)/1 var(--m);letter-spacing:.02em;
 background:rgba(25,184,159,.13);border:1px solid rgba(25,184,159,.45);color:#0e8d78}
.c.d .num{background:rgba(94,224,200,.12);border-color:rgba(94,224,200,.42);color:var(--aqua)}
.ci{flex:none;width:clamp(26px,1.7vw,34px);height:clamp(26px,1.7vw,34px);stroke:var(--teal);fill:none;stroke-width:1.5;
 stroke-linecap:round;stroke-linejoin:round}
.c.d .ci{stroke:var(--aqua)}
.hr{height:1px;background:var(--line-l);margin:11px 0 10px}
.c.d .hr{background:var(--line-d)}
.c p{font-size:clamp(13px,.92vw,18px);line-height:1.46;color:#3f6660}
.c.d p{color:var(--on-dark-dim)}
.c p+p{margin-top:7px}
.c h4{font-size:clamp(13px,.88vw,17px);font-weight:720;color:#0a2c28;margin-bottom:7px}
.c.d h4{color:var(--on-dark)}

.c svg:not(.ci):not(.wide){width:100%;max-width:clamp(400px,30vw,620px);display:block;margin:10px auto}
.c svg.wide{width:100%;max-width:none}

/* ---------- списки с галочками ---------- */
ul.ck{list-style:none;display:flex;flex-direction:column;gap:8px}
ul.ck li{display:flex;gap:11px;align-items:flex-start;font-size:clamp(13px,.9vw,17.5px);
 line-height:1.4;color:#3b625c;position:relative}
.c.d ul.ck li{color:var(--on-dark-dim)}
ul.ck li::before{content:"";flex:none;width:17px;height:17px;border-radius:50%;margin-top:1px;
 background:rgba(25,184,159,.14);border:1px solid rgba(25,184,159,.5)}
.c.d ul.ck li::before{background:rgba(94,224,200,.12);border-color:rgba(94,224,200,.45)}
ul.ck li::after{content:"";position:absolute;left:5px;top:5px;width:6px;height:3px;
 border-left:1.6px solid var(--teal);border-bottom:1.6px solid var(--teal);
 transform:rotate(-45deg)}
.c.d ul.ck li::after{border-color:var(--aqua)}
ul.ck.minus li::before{background:rgba(239,90,90,.12);border-color:rgba(239,90,90,.45)}
ul.ck.minus li::after{width:7px;height:0;border-left:none;border-bottom:1.8px solid var(--red);
 transform:none;left:5px;top:8px}
ul.ck.ask li::before{background:rgba(74,163,240,.12);border-color:rgba(74,163,240,.45)}
ul.ck.ask li::after{content:"?";border:none;transform:none;left:5.5px;top:1px;width:auto;height:auto;
 font:800 11px/17px var(--f);color:#2a7cc4}
.c.d ul.ck.ask li::after{color:#8cc6fb}

/* ---------- формульная плашка ---------- */
.fz{background:var(--deep);border:1px solid var(--line-d);border-radius:var(--r);
 padding:clamp(20px,2.2vw,34px) 24px;text-align:center;box-shadow:0 14px 36px rgba(5,32,29,.28)}
.fz{overflow-x:auto}
.fz .f{font:900 clamp(24px,4.2vw,58px)/1.05 var(--m);color:#fff;letter-spacing:.04em;
 display:flex;align-items:center;justify-content:center;gap:.28em;flex-wrap:nowrap;white-space:nowrap}
.fz .f .g{color:var(--green)}
.fz .f .o{color:var(--blue)}
.fz .f .t{color:#fff}
.fz .f .op{color:var(--on-dark-dim);font-weight:700}
.fz .cap{margin-top:12px;font-size:clamp(13px,.88vw,17px);color:var(--on-dark-dim)}
.fml{font:600 clamp(16px,1.5vw,28px)/1.5 var(--m);color:#0a2c28;display:flex;align-items:center;
 justify-content:center;gap:4px;flex-wrap:wrap}
.frac{display:inline-flex;flex-direction:column;text-align:center;margin:0 4px}
.frac .n{border-bottom:2px solid currentColor;padding:0 9px 3px}
.frac .d{padding:3px 9px 0}

/* ---------- врезка-результат ---------- */
.res{display:flex;gap:11px;align-items:flex-start;margin-top:auto;padding-top:13px;
 border-top:1px dashed var(--line-l);font-size:clamp(12.5px,.88vw,16.5px);line-height:1.45;color:#3f6660}
.c.d .res{border-top-color:var(--line-d);color:var(--on-dark-dim)}
.res i{flex:none;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;
 font:800 13px/1 var(--f);font-style:normal;
 background:rgba(25,184,159,.15);border:1px solid rgba(25,184,159,.5);color:#0e8d78}
.res.bad i{background:rgba(239,90,90,.15);border-color:rgba(239,90,90,.55);color:#d13c3c}
.c.d .res.bad i{color:#ff8484}
.c.d .res i{background:rgba(94,224,200,.12);border-color:rgba(94,224,200,.45);color:var(--aqua)}

/* ---------- цепочка процесса ---------- */
.chain{display:flex;align-items:center;gap:6px;flex-wrap:wrap}
.chain .lk{display:flex;align-items:center;gap:9px;flex:1 1 150px;min-width:132px}
.chain .bl{flex:none;width:clamp(40px,3vw,54px);height:clamp(40px,3vw,54px);border-radius:50%;display:grid;place-items:center;
 background:var(--deep-2);border:1px solid var(--line-d)}
.chain .bl svg{width:50%;height:50%;stroke:var(--aqua);fill:none;stroke-width:1.6;
 stroke-linecap:round;stroke-linejoin:round}
.chain .lk.fin .bl{background:var(--teal);border-color:var(--teal)}
.chain .lk.fin .bl svg{stroke:#04231f;stroke-width:2.6}
.chain .lb{font-size:clamp(12px,.8vw,15.5px);line-height:1.3;color:#3f6660}
.chain .cv{flex:none;font:700 22px/1 var(--f);color:var(--teal);opacity:.7}

/* ---------- выноска ---------- */
.bub{position:relative;background:#fff;border:1px solid var(--line-l);border-radius:14px;
 padding:14px 17px;font-size:clamp(13px,.88vw,17px);line-height:1.45;color:#3b625c;
 box-shadow:0 8px 22px rgba(23,78,70,.1)}
.bub::after{content:"";position:absolute;left:-7px;top:18px;width:13px;height:13px;background:#fff;
 border-left:1px solid var(--line-l);border-bottom:1px solid var(--line-l);transform:rotate(45deg)}
.bub.r::after{left:auto;right:-7px;border:none;border-right:1px solid var(--line-l);
 border-top:1px solid var(--line-l)}
.bub.dn::after{left:26px;top:auto;bottom:-7px;border:none;
 border-right:1px solid var(--line-l);border-bottom:1px solid var(--line-l)}

/* ---------- сетки ---------- */
.g{display:grid;gap:14px}
.g>*{min-width:0}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.g5{grid-template-columns:repeat(5,1fr)}
.g6{grid-template-columns:repeat(6,1fr)}
@media (max-width:1499px){.g6{grid-template-columns:repeat(3,1fr)}}
.g21{grid-template-columns:2fr 1fr}
.g12{grid-template-columns:1fr 2fr}
.g32{grid-template-columns:3fr 2fr}
.col{display:flex;flex-direction:column;gap:14px}

/* ---------- таблица ---------- */
.tw{overflow-x:auto;border-radius:var(--r);border:1px solid var(--line-l);background:var(--panel-l)}
table{border-collapse:collapse;width:100%;font-size:clamp(13px,.92vw,17.5px)}
th,td{padding:11px 16px;text-align:left;border-bottom:1px solid var(--line-l);color:#3b625c}
th{background:rgba(13,51,47,.92);color:var(--on-dark);font-weight:700;position:sticky;top:0;
 border-bottom:none;font-size:clamp(12px,.85vw,16px)}
tr:last-child td{border-bottom:none}
tbody tr:hover td{background:rgba(25,184,159,.07)}
td b{color:#0a2c28}
td .mono{font-family:var(--m);color:#0e8d78;font-weight:700}

/* ---------- шаги ---------- */
.step{opacity:0;transform:translateY(10px);transition:opacity .3s var(--ease),transform .3s var(--ease)}
.step.vis{opacity:1;transform:none}
.dash{stroke-dasharray:var(--L);stroke-dashoffset:var(--L);transition:stroke-dashoffset .75s var(--ease)}
.vis .dash{stroke-dashoffset:0}

/* ---------- HUD ---------- */
#hud{position:fixed;left:0;right:0;bottom:0;height:58px;z-index:5;display:flex;align-items:center;
 gap:10px;padding:0 18px;background:rgba(255,255,255,.72);backdrop-filter:blur(12px);
 border-top:1px solid var(--line-l)}
#prog{position:fixed;left:0;bottom:58px;height:3px;background:linear-gradient(90deg,var(--teal),var(--aqua));
 z-index:6;transition:width .3s var(--ease)}
#hud button{font:600 13.5px var(--f);color:#255c54;background:#fff;border:1px solid var(--line-l);
 border-radius:9px;padding:7px 12px;cursor:pointer;transition:.18s var(--ease)}
#hud button:hover{background:var(--teal);color:#fff;border-color:var(--teal);transform:translateY(-1px)}
#count{font:700 14px var(--m);color:#0e8d78;min-width:118px}
#sname{font-size:13.5px;color:var(--dim);flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
:focus-visible{outline:2.5px solid var(--teal);outline-offset:2px;border-radius:6px}

/* ---------- содержание ---------- */
#toc{position:fixed;inset:0;z-index:20;background:rgba(10,40,36,.93);backdrop-filter:blur(8px);
 display:none;padding:40px 48px;overflow:auto}
#toc.on{display:block}
#toc h2{color:var(--on-dark);font-size:22px;margin-bottom:18px;font-weight:750}
#tocg{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:10px}
.tocit{display:flex;gap:10px;align-items:center;text-align:left;padding:11px 13px;border-radius:12px;
 background:rgba(255,255,255,.06);border:1px solid var(--line-d);color:var(--on-dark-dim);
 font:500 13px var(--f);cursor:pointer;transition:.18s var(--ease)}
.tocit:hover{background:rgba(94,224,200,.16);color:#fff;transform:translateY(-2px)}
.tocit i{font:800 12px var(--m);font-style:normal;color:var(--aqua);min-width:26px}

/* ---------- интерактив ---------- */
.ui{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin-top:10px}
.ui label{font-size:clamp(12px,.82vw,15px);color:var(--dim)}
.ui input[type=number],.ui select{font:600 clamp(14px,.95vw,18px) var(--m);padding:9px 12px;border-radius:9px;
 border:1px solid var(--line-l);background:#fff;color:#0a2c28;width:112px}
.ui input[type=range]{flex:1;min-width:150px;accent-color:var(--teal)}
.big{font:900 clamp(24px,2.6vw,46px)/1 var(--m);color:#0e8d78}
.pill{display:inline-block;padding:5px 13px;border-radius:999px;font:700 clamp(12px,.8vw,15px) var(--f);
 background:rgba(25,184,159,.14);color:#0e8d78;border:1px solid rgba(25,184,159,.4)}
.pill.b{background:rgba(74,163,240,.14);color:#2a7cc4;border-color:rgba(74,163,240,.4)}
.pill.r{background:rgba(239,90,90,.14);color:#d13c3c;border-color:rgba(239,90,90,.4)}
.pill.g{background:rgba(73,214,127,.16);color:#1f9b4f;border-color:rgba(73,214,127,.45)}
.pill.d{background:rgba(94,224,200,.12);color:var(--aqua);border-color:rgba(94,224,200,.4)}

/* ---------- квиз ---------- */
.q{border-radius:var(--r);background:var(--panel-l);border:1px solid var(--line-l);padding:15px 17px}
.q .qt{font-weight:700;font-size:clamp(14px,1vw,19px);color:#0a2c28;margin-bottom:10px;display:flex;gap:9px}
.q .qt i{font:800 12px/1.5 var(--m);font-style:normal;color:#0e8d78}
.q .opts{display:grid;gap:7px}
.q button{text-align:left;font:500 clamp(13px,.88vw,17px) var(--f);padding:11px 14px;border-radius:10px;
 border:1px solid var(--line-l);background:#fff;color:#3b625c;cursor:pointer;transition:.16s var(--ease)}
.q button:hover{border-color:var(--teal);background:rgba(25,184,159,.06)}
.q button.good{background:rgba(73,214,127,.16);border-color:var(--green);color:#1a7a40;font-weight:650}
.q button.bad{background:rgba(239,90,90,.14);border-color:var(--red);color:#c23434}
.q .ex{margin-top:11px;font-size:clamp(13px,.86vw,16.5px);line-height:1.45;color:#3f6660;display:none;
 padding-top:9px;border-top:1px dashed var(--line-l)}
.q .ex.on{display:block}
#score{font:800 15px var(--m);color:#0e8d78}

/* ---------- шкалы ---------- */
.bar{height:10px;border-radius:999px;background:rgba(13,51,47,.1);overflow:hidden}
.bar>i{display:block;height:100%;border-radius:999px;width:0;
 background:linear-gradient(90deg,var(--aqua),var(--teal));transition:width .9s var(--ease)}
.bar.red>i{background:linear-gradient(90deg,#ff8a8a,var(--red))}
.bar.green>i{background:linear-gradient(90deg,#8ae8ad,var(--green))}
.c.d .bar{background:rgba(255,255,255,.1)}

/* ---------- лесенка единиц ---------- */
.ladder{display:flex;align-items:flex-end;gap:10px;flex-wrap:wrap}
.ladder .stp{flex:1 1 150px;border-radius:var(--r);padding:13px 15px;color:#fff;
 box-shadow:0 10px 26px rgba(5,32,29,.2)}
.ladder .stp .u{font:800 clamp(18px,1.8vw,34px)/1 var(--m);letter-spacing:.02em}
.ladder .stp .e{font-size:clamp(12px,.8vw,15px);opacity:.82;margin-top:4px}
.ladder .stp .v{margin-top:10px;font-size:clamp(12.5px,.85vw,16px);background:rgba(255,255,255,.16);
 border-radius:9px;padding:6px 9px;line-height:1.3}
.ladder .mul{flex:none;font:800 12px var(--m);color:#0e8d78;padding-bottom:22px}

/* ---------- титул ---------- */
.cover{display:flex;flex-direction:column;justify-content:center;height:100%;gap:18px}
.cover h1{font-size:clamp(34px,6vw,84px);font-weight:850;letter-spacing:-.035em;line-height:.98;color:#06201d}
.cover h1 em{font-style:normal;color:#0e8d78}
.cover .ln{width:92px;height:4px;border-radius:4px;background:linear-gradient(90deg,var(--teal),var(--aqua))}
.cover .meta{display:flex;gap:10px;flex-wrap:wrap;margin-top:6px}

/* ---------- адаптив ---------- */
#hud .hint{display:inline}
@media (max-width:1320px){#hud .hint{display:none}}
@media (max-width:1279px){
 .g4,.g5{grid-template-columns:repeat(2,1fr)}
 .g6{grid-template-columns:repeat(2,1fr)}
 .g3{grid-template-columns:repeat(2,1fr)}
 .slide{padding:22px 26px 70px}
}
@media (max-width:1099px){.g2,.g21,.g12,.g32{grid-template-columns:1fr}}
@media (max-width:640px){
 .g,.g2,.g3,.g4,.g5,.g6,.g21,.g12,.g32{grid-template-columns:1fr}
 h1.t{font-size:26px}
 .cover h1{font-size:34px}
 .slide{padding:18px 16px 66px}
 #sname{display:none}
 .cl3,.cl4,.city2{display:none}
}
@media (prefers-reduced-motion:reduce){
 .step{opacity:1!important;transform:none!important;transition:none}
 .dash{stroke-dashoffset:0!important;transition:none}
 .bar>i{transition:none}
}
"""
