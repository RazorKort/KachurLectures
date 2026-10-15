# -*- coding: utf-8 -*-
"""Стиль деки 2.5 «Статическая и динамическая маршрутизация».

Кинематографичный плакатный стиль по фото-референсам:
тёмно-бирюзовый ночной город, кремовые панели с жёсткой чёрной обводкой,
красный акцент, узкие прописные заголовки.
"""

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
--deep:#0c211f;        /* ночной фон */
--deep2:#123330;
--panel:#f4ecda;       /* кремовая панель */
--panel2:#eadfc6;
--ink:#14201f;         /* основной текст на панели */
--dim:#52635f;
--line:#101b1a;        /* жёсткая обводка */
--red:#dd3326;
--red-d:#a92419;
--cyan:#5ec6d8;
--amber:#e8a63c;
--green:#4fb07a;
--cream:#f7f2e6;
--r:6px; --r2:4px;
--ease:cubic-bezier(.22,.7,.3,1);
--f:"Roboto Condensed","Oswald","PT Sans Narrow","Segoe UI",Arial Narrow,system-ui,sans-serif;
--ft:"Oswald","Roboto Condensed",Impact,"Segoe UI",sans-serif;
--m:"JetBrains Mono","Cascadia Mono",Consolas,ui-monospace,monospace;
}
html,body{height:100%}
body{font-family:var(--f);color:var(--ink);background:var(--deep);overflow:hidden;
 -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* ---------- фон ---------- */
#bg{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;background:
 radial-gradient(130% 90% at 50% 0%,#1b4542 0%,#0e2725 45%,#081715 100%)}
#bg .tex{position:absolute;inset:0;background-size:cover;background-position:center bottom}
#bg .glow{position:absolute;left:50%;top:-14%;width:72vw;height:52vh;transform:translateX(-50%);
 background:radial-gradient(circle,rgba(221,51,38,.26),rgba(221,51,38,0) 65%)}
#bg .grain{position:absolute;inset:0;opacity:.10;background-image:
 url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='120' height='120'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3'/></filter><rect width='120' height='120' filter='url(%23n)' opacity='.6'/></svg>")}
#bg .arcs{position:absolute;inset:0;width:100%;height:100%}

/* ---------- каркас ---------- */
#stage{position:fixed;inset:0;z-index:1}
.slide{position:absolute;inset:0;padding:clamp(16px,1.8vw,34px) clamp(18px,2.4vw,46px) 74px;
 display:none;overflow:hidden;flex-direction:column}
.slide.on{display:flex}
.slide>.sc{flex:1;min-height:0;overflow:auto;padding-right:6px;scrollbar-width:thin;
 scrollbar-color:#355c58 transparent;display:flex;flex-direction:column;gap:13px}
.slide>.sc::-webkit-scrollbar{width:9px}
.slide>.sc::-webkit-scrollbar-thumb{background:#36605b;border-radius:8px}
.slide>.sc>.g{flex:0 0 auto}
.slide>.sc>.head+*{margin-top:auto}
.slide>.sc>:last-child{margin-bottom:auto}
.slide>.sc>.grow{flex:1 1 auto}
.g>.step{display:flex;flex-direction:column;min-height:0}
.g>.step>.c{flex:1 1 auto}
.g>.c{height:100%}
.col{display:flex;flex-direction:column;gap:13px;min-width:0}
.col>.step{display:flex;flex-direction:column}

/* ---------- заголовок ---------- */
.head{flex:none;margin-bottom:6px;display:flex;align-items:flex-start;gap:14px}
.head .mark{flex:none;width:12px;height:46px;background:var(--red);margin-top:3px}
h1.t{font-family:var(--ft);font-size:clamp(24px,3vw,58px);font-weight:700;line-height:.98;
 color:var(--cream);text-transform:uppercase;letter-spacing:.005em;
 text-shadow:0 3px 0 rgba(0,0,0,.45)}
p.sub{margin-top:7px;font-size:clamp(14px,1.25vw,24px);color:#bfd3cf;line-height:1.38;max-width:1180px}
p.sub b{color:#fff}

/* ---------- панель ---------- */
.c{background:var(--panel);border:3px solid var(--line);border-radius:var(--r);
 padding:clamp(12px,1.05vw,21px) clamp(14px,1.15vw,23px);
 box-shadow:6px 6px 0 rgba(0,0,0,.42);display:flex;flex-direction:column;position:relative}
.c.dark{background:#112b29;border-color:#000;color:#e6efed}
.c.dark p,.c.dark li,.c.dark .ir span{color:#d6e5e2}
.c.dark h3,.c.dark h4{color:#fff}
.ch{display:flex;align-items:center;gap:10px;margin-bottom:9px}
.ch h3{font-family:var(--ft);font-size:clamp(16px,1.5vw,30px);font-weight:600;line-height:1.05;
 color:var(--ink);text-transform:uppercase}
.ch h3.mix{text-transform:none}
.ch::before{content:"";flex:none;width:7px;height:22px;background:var(--red);align-self:center}
.ch.non::before{display:none}
.num{flex:none;width:30px;height:30px;display:grid;place-items:center;border:2px solid var(--line);
 font:700 16px/1 var(--ft);color:#fff;background:var(--red)}
.c p{font-size:clamp(14px,1.18vw,22px);line-height:1.46;color:var(--ink)}
.c p+p{margin-top:7px}
.c p.d{color:var(--dim)}
.c h4{font-family:var(--ft);font-size:clamp(15px,1.2vw,23px);font-weight:600;color:var(--red-d);
 margin-bottom:6px;text-transform:uppercase}
.hr{height:3px;background:var(--line);opacity:.18;margin:10px 0 9px}
.c svg.fig{width:100%;display:block;margin:2px auto 0}
b.hl{background:var(--red);color:#fff;padding:0 5px}
b.hc{background:#cfeef4;padding:0 5px}
code{font-family:var(--m);font-weight:600;background:#e2d7bd;padding:1px 5px;font-size:.92em}

/* ---------- плашки ---------- */
.tag{display:inline-block;padding:5px 12px;border:2px solid var(--line);background:var(--panel2);
 font:700 clamp(13px,1vw,19px) var(--f);color:var(--ink);line-height:1.3}
.tag.r{background:var(--red);color:#fff;border-color:var(--line)}
.tag.cy{background:#cfeef4}
.tag.am{background:#f6dfae}
.tag.gr{background:#cfead9}
.tag.mono{font-family:var(--m);font-weight:600}
.tags{display:flex;gap:7px;flex-wrap:wrap}

/* ---------- строка с иконкой ---------- */
.ir{display:flex;align-items:center;gap:10px;background:var(--panel2);border:2px solid var(--line);
 padding:7px 11px}
.ir+.ir{margin-top:7px}
.ir .ib{flex:none;width:28px;height:28px;background:#fff;border:2px solid var(--line);
 display:grid;place-items:center}
.ir .ib svg{width:16px;height:16px;fill:none;stroke:var(--red-d);stroke-width:1.8;
 stroke-linecap:round;stroke-linejoin:round}
.ir.cy .ib svg{stroke:#2a7f90}.ir.am .ib svg{stroke:#9a6a12}.ir.gr .ib svg{stroke:#2e7a50}
.ir span{font-size:clamp(14px,1.12vw,21px);line-height:1.35;color:var(--ink)}
.ir b{color:var(--red-d)}

/* ---------- списки ---------- */
ul.ck{list-style:none;display:flex;flex-direction:column;gap:7px}
ul.ck li{display:flex;gap:10px;align-items:flex-start;font-size:clamp(14px,1.15vw,21.5px);
 line-height:1.4;color:var(--ink)}
ul.ck li::before{content:"";flex:none;width:17px;height:17px;margin-top:2px;border:2px solid var(--line);
 background:var(--green) url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M5 13l4 4 10-10' fill='none' stroke='white' stroke-width='3.6' stroke-linecap='round' stroke-linejoin='round'/></svg>") center/12px no-repeat}
ul.ck.no li::before{background:var(--red) url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'><path d='M6 6l12 12M18 6L6 18' fill='none' stroke='white' stroke-width='3.4' stroke-linecap='round'/></svg>") center/12px no-repeat}
ul.ck.dot li::before{width:11px;height:11px;margin-top:6px;border:0;background:var(--red)}
.c.dark ul.ck li{color:#d6e5e2}

/* ---------- сетки ---------- */
.g{display:grid;gap:13px}
.g>*{min-width:0}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.g21{grid-template-columns:2fr 1fr}
.g12{grid-template-columns:1fr 2fr}
.g32{grid-template-columns:3fr 2fr}
.g23{grid-template-columns:2fr 3fr}

/* ---------- таблица ---------- */
.tw{overflow:auto;border:3px solid var(--line);background:var(--panel);
 box-shadow:6px 6px 0 rgba(0,0,0,.42)}
table{border-collapse:collapse;width:100%;font-size:clamp(13.5px,1.08vw,20px)}
th,td{padding:8px 13px;text-align:left;border-bottom:2px solid rgba(16,27,26,.16);color:var(--ink)}
th{background:var(--line);color:var(--cream);font-family:var(--ft);font-weight:500;position:sticky;top:0;
 font-size:clamp(13px,1vw,19px);text-transform:uppercase;letter-spacing:.03em}
tr:last-child td{border-bottom:none}
tbody tr:hover td{background:var(--panel2)}
td.mono,th.mono{font-family:var(--m);font-weight:600}
td .g1{color:#2e7a50;font-weight:700}
td .r1{color:var(--red-d);font-weight:700}
td.ctr,th.ctr{text-align:center}
tr.hot td{background:#f7d9d4}
tr.new td{background:#d9eee2}

/* ---------- CLI ---------- */
.cli{background:#0b1a19;border:3px solid #000;padding:11px 14px 12px;overflow-x:auto;
 box-shadow:6px 6px 0 rgba(0,0,0,.42)}
.cli .dots{display:flex;gap:6px;margin-bottom:8px}
.cli .dots i{width:9px;height:9px;border-radius:50%;background:#555}
.cli .dots i:nth-child(1){background:#e05545}.cli .dots i:nth-child(2){background:#e8b545}
.cli .dots i:nth-child(3){background:#56b06f}
.cli pre{font:600 clamp(13px,1.05vw,20px)/1.6 var(--m);color:#e9e2cf;white-space:pre}
.cli .pr{color:#6fd0a0}
.cli .cm{color:#ffd47a}
.cli .rem{color:#7e918c;font-style:italic}

/* ---------- иллюстрация-плакат ---------- */
.shot{border:3px solid var(--line);box-shadow:6px 6px 0 rgba(0,0,0,.42);overflow:hidden;background:#0b1a19}
.shot img{display:block;width:100%;height:auto}
.shot.sm img{max-height:46vh;object-fit:contain;margin:0 auto}

/* ---------- сноска ---------- */
.foot{display:flex;align-items:center;gap:12px;margin-top:2px;flex:none}
.foot i{flex:1;height:3px;font-style:normal;background:rgba(244,236,218,.25)}
.foot span{font-size:clamp(12px,.95vw,18px);color:#cfe0dc;white-space:nowrap;text-transform:uppercase;
 letter-spacing:.04em;font-weight:700}

/* ---------- лента-вывод ---------- */
.band{background:var(--panel);border:3px solid var(--line);box-shadow:6px 6px 0 rgba(0,0,0,.42);
 padding:10px 16px;display:flex;align-items:center;gap:12px}
.band .bm{flex:none;width:10px;height:26px;background:var(--red)}
.band p{font-family:var(--ft);font-size:clamp(16px,1.45vw,28px);text-transform:uppercase;
 font-weight:500;line-height:1.14;color:var(--ink)}

/* ---------- шаги и SVG-анимация ---------- */
.step{opacity:0;transform:translateY(9px);transition:opacity .28s var(--ease),transform .28s var(--ease)}
.step.vis{opacity:1;transform:none}
.dash{stroke-dasharray:var(--L);stroke-dashoffset:var(--L);transition:stroke-dashoffset .7s var(--ease)}
.vis .dash,.dash.go{stroke-dashoffset:0}
.fade{opacity:0;transition:opacity .35s var(--ease)}
.fade.go{opacity:1}

/* ---------- сцена на всю ширину, пояснение под ней ---------- */
.g:has(> .step > .sx),.g:has(> .step > .figwrap){grid-template-columns:1fr!important}
.figwrap svg.fig{max-height:52vh}
.sx svg{max-height:58vh;margin:0 auto}

/* ---------- слайд-плакат ---------- */
.slide.pslide{padding:8px 10px 62px;align-items:center;justify-content:center}
.pwrap{flex:1;min-height:0;width:100%;display:flex;align-items:center;justify-content:center}
.pwrap svg.pst{width:100%;height:100%;max-height:100%;display:block;
 filter:drop-shadow(0 10px 22px rgba(0,0,0,.45))}
.pwrap .step{transform:none}
.pwrap .step.vis{transform:none}

/* ---------- титул ---------- */
.cover{display:flex;flex-direction:column;justify-content:center;height:100%;gap:14px;max-width:1240px}
.cover h1{font-family:var(--ft);font-size:clamp(30px,5.4vw,88px);font-weight:700;line-height:.94;
 color:var(--cream);text-transform:uppercase;text-shadow:0 5px 0 rgba(0,0,0,.45)}
.cover .rule{width:clamp(150px,22vw,380px);height:12px;background:var(--red)}
.cover .meta{display:flex;gap:8px;flex-wrap:wrap;margin-top:6px}
.cover p.lead{font-size:clamp(14px,1.25vw,24px);color:#d7e6e2;line-height:1.35;max-width:900px}

/* ---------- покадровый проигрыватель сцены ---------- */
.sx{border:3px solid var(--line);background:#0d2422;box-shadow:6px 6px 0 rgba(0,0,0,.42);
 display:flex;flex-direction:column;overflow:hidden}
.sx .sxv{position:relative;background:linear-gradient(180deg,rgba(11,31,30,.55),rgba(11,31,30,.78)),
 var(--scenebg) center/cover no-repeat,#0b1f1d}
.sx svg{width:100%;display:block}
.sx .sxb{display:flex;align-items:center;gap:9px;padding:8px 11px;background:var(--panel);
 border-top:3px solid var(--line);flex-wrap:wrap}
.sx .sxb button{font:700 15px var(--f);color:#fff;background:var(--line);border:2px solid var(--line);
 padding:6px 13px;cursor:pointer;transition:.15s var(--ease)}
.sx .sxb button:hover{background:var(--red);border-color:var(--red)}
.sx .sxb button[disabled]{opacity:.35;cursor:default}
.sx .sxb button[disabled]:hover{background:var(--line)}
.sx .sxb .sxn{font:700 12.5px var(--m);color:var(--dim);min-width:46px;text-align:center}
.sx .sxb .sxc{font-size:clamp(14px,1.15vw,21px);line-height:1.3;color:var(--ink);flex:1;min-width:160px}
.sx .sxb .sxc b{color:var(--red-d)}
.sx .sxt{background:var(--line);color:var(--cream);font:700 13px var(--f);
 padding:6px 12px;text-transform:uppercase;letter-spacing:.04em}
.sx .fr{opacity:0;transition:opacity .3s var(--ease)}
.sx .fr.on{opacity:1}

/* ---------- квиз / задачи ---------- */
.q{background:var(--panel);border:3px solid var(--line);padding:13px 16px;
 box-shadow:6px 6px 0 rgba(0,0,0,.42)}
.q .qt{display:flex;gap:10px;align-items:flex-start;font-weight:700;color:var(--ink);
 font-size:clamp(15px,1.25vw,23px);margin-bottom:10px;line-height:1.3}
.q .qt i{flex:none;font-style:normal;background:var(--red);color:#fff;border:2px solid var(--line);
 min-width:26px;height:26px;display:grid;place-items:center;font:700 14px var(--ft)}
.q .opts{display:grid;gap:6px}
.q button{text-align:left;font:600 clamp(14px,1.1vw,20px) var(--f);padding:9px 13px;
 border:2px solid var(--line);background:#fff;color:var(--ink);cursor:pointer;transition:.15s var(--ease)}
.q button:hover{background:var(--panel2)}
.q button.good{background:#cfead9;font-weight:700}
.q button.bad{background:#f7d9d4}
.q .ex{display:none;margin-top:10px;padding-top:9px;border-top:2px dashed rgba(16,27,26,.3);
 font-size:clamp(12px,.86vw,16.5px);line-height:1.42;color:var(--dim)}
.q .ex.on{display:block}
.q .inp{display:flex;gap:8px;align-items:center;flex-wrap:wrap}
.q input{font:600 15px var(--m);padding:8px 11px;border:2px solid var(--line);background:#fff;
 width:210px;color:var(--ink)}
.q .chk{font:700 13px var(--f);color:#fff;background:var(--red);border:2px solid var(--line);
 padding:9px 15px;cursor:pointer}
.q .verdict{font-weight:700;font-size:15px}
.q .verdict.ok{color:#2e7a50}.q .verdict.no{color:var(--red-d)}
#score{font:700 14px var(--m);color:var(--red-d)}

/* ---------- HUD ---------- */
#hud{position:fixed;left:0;right:0;bottom:0;height:54px;z-index:5;display:flex;align-items:center;
 gap:8px;padding:0 16px;background:rgba(9,25,24,.92);border-top:3px solid #000}
#prog{position:fixed;left:0;bottom:54px;height:4px;z-index:6;background:var(--red);
 transition:width .3s var(--ease)}
#hud button{font:700 13px var(--f);color:var(--cream);background:#16403c;border:2px solid #2d615b;
 padding:6px 12px;cursor:pointer;transition:.15s var(--ease)}
#hud button:hover{background:var(--red);border-color:var(--red)}
#count{font:700 13px var(--m);color:var(--cyan);min-width:112px}
#sname{font-size:13px;color:#9fb8b4;flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
#hud .hint{font-size:11.5px;color:#6d8884}
:focus-visible{outline:3px solid var(--red);outline-offset:2px}

/* ---------- содержание ---------- */
#toc{position:fixed;inset:0;z-index:20;background:rgba(8,22,21,.97);display:none;padding:34px 42px;
 overflow:auto}
#toc.on{display:block}
#toc h2{font-family:var(--ft);color:var(--cream);font-size:26px;margin-bottom:16px;font-weight:600;
 text-transform:uppercase}
#tocg{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:8px}
.tocit{display:flex;gap:10px;align-items:center;text-align:left;padding:9px 11px;
 background:#10302d;border:2px solid #2d615b;color:#dceae7;font:600 13px var(--f);cursor:pointer;
 transition:.15s var(--ease)}
.tocit:hover{background:var(--red);border-color:var(--red);color:#fff}
.tocit i{font:700 12px/1 var(--m);font-style:normal;color:#fff;min-width:24px;height:22px;
 display:grid;place-items:center;background:var(--red)}

/* ---------- адаптив ---------- */
@media (max-width:1320px){#hud .hint{display:none}}
@media (max-width:1279px){
 .g4{grid-template-columns:repeat(2,1fr)}
 .g3{grid-template-columns:repeat(2,1fr)}
 .slide{padding:16px 20px 66px}
}
@media (max-width:1099px){.g2,.g21,.g12,.g32,.g23{grid-template-columns:1fr}}
@media (max-width:640px){
 .g,.g2,.g3,.g4,.g21,.g12,.g32,.g23{grid-template-columns:1fr}
 h1.t{font-size:25px}.cover h1{font-size:31px}
 .slide{padding:14px 13px 62px}
 #sname{display:none}
}
@media (prefers-reduced-motion:reduce){
 .step{opacity:1!important;transform:none!important;transition:none}
 .dash{stroke-dashoffset:0!important;transition:none}
 .fade{opacity:1!important;transition:none}
}
"""
