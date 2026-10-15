# -*- coding: utf-8 -*-
"""Неоновый кибер-стиль деки «Коммутаторы и коммутация» (под стиль инфографик 2.2)."""

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
--bg0:#02060f; --bg1:#050d22; --bg2:#081634;
--cy:#2ad4ff; --cy2:#7df3ff; --cyd:#0b6a8c;
--mg:#c45cff; --mg2:#ff7ae0;
--lm:#9dfc5a; --am:#ffc53d; --rd:#ff4d5e; --or:#ff8a3d;
--ink:#eaf6ff; --soft:#a8c8e8; --dim:#7794b8;
--line:rgba(60,160,230,.30);
--panel:linear-gradient(160deg,rgba(13,40,92,.70),rgba(5,14,38,.88));
--r:16px; --r2:11px;
--f:"Golos Text","Inter","Segoe UI",system-ui,-apple-system,Arial,sans-serif;
--fd:"Oswald","Anton","Arial Narrow","Arial Black",system-ui,sans-serif;
--m:"JetBrains Mono","Cascadia Mono",Consolas,ui-monospace,monospace;
--ease:cubic-bezier(.22,.7,.3,1);
}
html,body{height:100%}
body{font-family:var(--f);color:var(--ink);background:var(--bg0);overflow:hidden;
 -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility}

/* ===================== ФОН ===================== */
#bg{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none}
#bgfx{position:fixed;inset:0;z-index:0;pointer-events:none;
 background:
  radial-gradient(900px 540px at 12% -8%,rgba(42,212,255,.17),transparent 62%),
  radial-gradient(760px 520px at 92% 8%,rgba(196,92,255,.15),transparent 60%),
  radial-gradient(1000px 620px at 50% 118%,rgba(42,140,255,.16),transparent 62%)}
#bgfx::after{content:"";position:absolute;inset:0;
 background:repeating-linear-gradient(0deg,rgba(120,200,255,.045) 0 1px,transparent 1px 3px);
 opacity:.5;animation:scan 9s linear infinite}
@keyframes scan{to{background-position:0 240px}}

/* ===================== КАРКАС ===================== */
#stage{position:fixed;inset:0;z-index:1}
.slide{position:absolute;inset:0;padding:clamp(14px,1.6vw,30px) clamp(16px,2.2vw,44px) 70px;
 display:none;overflow:hidden;flex-direction:column}
.slide.on{display:flex;animation:sin .42s var(--ease)}
@keyframes sin{from{opacity:0;transform:translateY(14px)}to{opacity:1;transform:none}}
.slide>.sc{flex:1;min-height:0;overflow:auto;padding-right:6px;display:flex;flex-direction:column;gap:12px;
 scrollbar-width:thin;scrollbar-color:rgba(42,212,255,.45) transparent}
.slide>.sc::-webkit-scrollbar{width:9px}
.slide>.sc::-webkit-scrollbar-thumb{background:rgba(42,212,255,.4);border-radius:9px}
.slide>.sc>.g{flex:0 0 auto}
.slide>.sc>.grow{flex:1 1 auto;min-height:0}
.g{display:grid;gap:12px}
.g2{grid-template-columns:1fr 1fr}
.g3{grid-template-columns:1fr 1fr 1fr}
.g4{grid-template-columns:repeat(4,1fr)}
.g21{grid-template-columns:2fr 1fr}
.g12{grid-template-columns:1fr 2fr}
.g>*{min-width:0;min-height:0}
.col{display:flex;flex-direction:column;gap:12px;min-width:0}

/* ===================== ЗАГОЛОВОК ===================== */
.head{flex:none;margin-bottom:4px;position:relative;padding-left:16px}
.head::before{content:"";position:absolute;left:0;top:4px;bottom:6px;width:5px;border-radius:4px;
 background:linear-gradient(180deg,var(--cy),var(--mg));box-shadow:0 0 16px rgba(42,212,255,.85)}
h1.t{font-family:var(--fd);font-weight:700;line-height:.95;text-transform:uppercase;
 font-size:clamp(22px,2.7vw,48px);letter-spacing:.006em;color:#fff;
 text-shadow:0 0 22px rgba(42,212,255,.45)}
h1.t em{font-style:normal;color:var(--cy);text-shadow:0 0 24px rgba(42,212,255,.9)}
h1.t em.v{color:var(--mg);text-shadow:0 0 24px rgba(196,92,255,.9)}
p.sub{margin-top:7px;font-size:clamp(12px,.95vw,18px);color:var(--soft);font-weight:600;line-height:1.35;max-width:1250px}

/* ===================== ПАНЕЛИ ===================== */
.c{background:var(--panel);border:1px solid var(--line);border-radius:var(--r);
 padding:clamp(10px,.9vw,18px) clamp(12px,1.0vw,20px);display:flex;flex-direction:column;position:relative;
 box-shadow:inset 0 1px 0 rgba(140,220,255,.14),0 0 24px rgba(10,80,160,.22)}
.c::before{content:"";position:absolute;left:14px;right:14px;top:-1px;height:1px;
 background:linear-gradient(90deg,transparent,rgba(42,212,255,.9),transparent)}
.c.cy{border-color:rgba(42,212,255,.55);box-shadow:inset 0 0 26px rgba(42,212,255,.09),0 0 26px rgba(42,212,255,.22)}
.c.mg{border-color:rgba(196,92,255,.55);box-shadow:inset 0 0 26px rgba(196,92,255,.09),0 0 26px rgba(196,92,255,.22)}
.c.lm{border-color:rgba(157,252,90,.5);box-shadow:inset 0 0 26px rgba(157,252,90,.08),0 0 24px rgba(157,252,90,.18)}
.c.am{border-color:rgba(255,197,61,.55);box-shadow:inset 0 0 26px rgba(255,197,61,.08),0 0 24px rgba(255,197,61,.2)}
.c.rd{border-color:rgba(255,77,94,.55);box-shadow:inset 0 0 26px rgba(255,77,94,.08),0 0 24px rgba(255,77,94,.2)}
.c.flat{background:rgba(6,16,40,.6)}
.ch{display:flex;align-items:center;gap:10px;margin-bottom:8px}
.ch h3{font-family:var(--fd);font-weight:600;text-transform:uppercase;line-height:1.05;
 font-size:clamp(13px,1.05vw,22px);color:#fff;letter-spacing:.01em}
.ch h3 em{font-style:normal;color:var(--cy)}
.c p{font-size:clamp(11.5px,.85vw,17px);line-height:1.45;color:var(--soft)}
.c p+p{margin-top:6px}
.c p b,.c li b{color:#fff;font-weight:700}
.c h4{font-size:clamp(12px,.86vw,17px);font-weight:800;color:#fff;margin-bottom:5px}
.hr{height:1px;background:linear-gradient(90deg,transparent,rgba(42,212,255,.5),transparent);margin:9px 0 8px}
ul.li{list-style:none;display:flex;flex-direction:column;gap:6px}
ul.li li{position:relative;padding-left:20px;font-size:clamp(11.5px,.85vw,17px);line-height:1.42;color:var(--soft)}
ul.li li::before{content:"";position:absolute;left:3px;top:.56em;width:8px;height:8px;border-radius:2px;
 background:var(--cy);box-shadow:0 0 10px rgba(42,212,255,.9);transform:rotate(45deg)}
ul.li.mg li::before{background:var(--mg);box-shadow:0 0 10px rgba(196,92,255,.9)}
ul.li.lm li::before{background:var(--lm);box-shadow:0 0 10px rgba(157,252,90,.9)}

/* ===================== НОМЕРА, ПИЛЮЛИ ===================== */
.num{flex:none;width:32px;height:32px;border-radius:9px;display:grid;place-items:center;
 font:800 15px/1 var(--f);color:#02121f;background:linear-gradient(160deg,var(--cy2),var(--cy));
 box-shadow:0 0 16px rgba(42,212,255,.6)}
.num.v{background:linear-gradient(160deg,var(--mg2),var(--mg));box-shadow:0 0 16px rgba(196,92,255,.6)}
.num.g{background:linear-gradient(160deg,#d6ff9a,var(--lm));box-shadow:0 0 16px rgba(157,252,90,.6)}
.num.y{background:linear-gradient(160deg,#ffe08a,var(--am));box-shadow:0 0 16px rgba(255,197,61,.6)}
.num.r{background:linear-gradient(160deg,#ff9aa5,var(--rd));color:#fff;box-shadow:0 0 16px rgba(255,77,94,.6)}
.num.sm{width:25px;height:25px;font-size:12px;border-radius:7px}
.tag{display:inline-block;padding:4px 11px;border-radius:7px;border:1px solid rgba(42,212,255,.5);
 background:rgba(42,212,255,.12);color:var(--cy2);font:700 clamp(10.5px,.76vw,14.5px)/1.3 var(--f)}
.tag.v{border-color:rgba(196,92,255,.5);background:rgba(196,92,255,.13);color:#f0bcff}
.tag.g{border-color:rgba(157,252,90,.5);background:rgba(157,252,90,.12);color:#d6ff9a}
.tag.y{border-color:rgba(255,197,61,.5);background:rgba(255,197,61,.12);color:#ffe08a}
.tag.r{border-color:rgba(255,77,94,.55);background:rgba(255,77,94,.14);color:#ffb3bb}
.tag.mono{font-family:var(--m);letter-spacing:-.01em}
.tags{display:flex;gap:6px;flex-wrap:wrap;align-items:center}

/* ===================== СТРОКИ С ИКОНКОЙ ===================== */
.ir{display:flex;align-items:center;gap:10px;background:rgba(10,28,64,.55);border:1px solid rgba(60,160,230,.22);
 border-radius:var(--r2);padding:7px 11px}
.ir+.ir{margin-top:6px}
.ir .ib{flex:none;width:28px;height:28px;border-radius:8px;display:grid;place-items:center;
 background:rgba(42,212,255,.16);border:1px solid rgba(42,212,255,.5)}
.ir.v .ib{background:rgba(196,92,255,.16);border-color:rgba(196,92,255,.5)}
.ir.g .ib{background:rgba(157,252,90,.14);border-color:rgba(157,252,90,.5)}
.ir.y .ib{background:rgba(255,197,61,.14);border-color:rgba(255,197,61,.5)}
.ir.r .ib{background:rgba(255,77,94,.14);border-color:rgba(255,77,94,.5)}
.ir .ib svg{width:16px;height:16px;fill:none;stroke:var(--cy2);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.ir.v .ib svg{stroke:#f0bcff} .ir.g .ib svg{stroke:#d6ff9a}
.ir.y .ib svg{stroke:#ffe08a} .ir.r .ib svg{stroke:#ffb3bb}
.ir span:last-child{font-size:clamp(11.5px,.83vw,16.5px);line-height:1.38;color:var(--soft)}
.ir b{color:#fff;font-weight:700}

/* ===================== СНОСКИ ===================== */
.foot{display:flex;align-items:center;gap:11px;border-radius:var(--r2);padding:9px 14px;
 background:rgba(42,212,255,.1);border:1px solid rgba(42,212,255,.4);
 font-weight:600;font-size:clamp(11.5px,.83vw,16.5px);line-height:1.38;color:var(--ink)}
.foot i{flex:none;width:26px;height:26px;border-radius:7px;background:var(--cy);color:#02121f;
 display:grid;place-items:center;font:800 15px/1 var(--f);font-style:normal}
.foot.warn{background:rgba(255,77,94,.1);border-color:rgba(255,77,94,.45)}
.foot.warn i{background:var(--rd);color:#fff}
.foot.ok{background:rgba(157,252,90,.1);border-color:rgba(157,252,90,.45)}
.foot.ok i{background:var(--lm);color:#0b2a00}
.foot.note{background:rgba(255,197,61,.1);border-color:rgba(255,197,61,.45)}
.foot.note i{background:var(--am);color:#2a1c00}

/* ===================== ТАБЛИЦЫ ===================== */
.tw{overflow:auto;border-radius:var(--r2);border:1px solid rgba(60,160,230,.3);background:rgba(4,12,32,.7)}
.tw table{border-collapse:collapse;width:100%;font-size:clamp(11px,.8vw,15.5px)}
.tw th{background:rgba(42,212,255,.14);color:#fff;font-weight:700;text-align:left;padding:8px 11px;white-space:nowrap;
 border-bottom:1px solid rgba(42,212,255,.4)}
.tw td{padding:7px 11px;border-top:1px solid rgba(60,160,230,.18);line-height:1.34;vertical-align:top;color:var(--soft)}
.tw tr.hi td{background:rgba(157,252,90,.12);color:#eaffe0}
.tw tr.hl td{background:rgba(255,197,61,.1)}
.tw .mono{font-family:var(--m)}

/* ===================== КОД ===================== */
pre.cli{font-family:var(--m);font-size:clamp(10.5px,.78vw,15px);line-height:1.5;color:#bfe9ff;
 background:rgba(2,10,28,.85);border:1px solid rgba(42,212,255,.35);border-radius:var(--r2);
 padding:10px 13px;overflow:auto;white-space:pre;box-shadow:inset 0 0 26px rgba(42,212,255,.07)}
pre.cli .k{color:var(--lm);font-weight:700}
pre.cli .p{color:var(--cy2)}
pre.cli .c{color:var(--dim)}
pre.cli .h{color:var(--am);font-weight:700}
.clih{font:700 11px/1 var(--m);color:var(--cy);letter-spacing:.14em;text-transform:uppercase;margin-bottom:5px}

/* ===================== КАРТИНКИ-ИНФОГРАФИКИ ===================== */
.pic{flex:1 1 auto;min-height:0;display:flex;align-items:center;justify-content:center;
 border-radius:var(--r);overflow:hidden;border:1px solid rgba(42,212,255,.35);
 box-shadow:0 0 30px rgba(10,90,180,.3)}
.pic img{width:100%;height:100%;object-fit:contain;display:block;background:#030a1c}
.piccap{margin-top:6px;font-size:clamp(11px,.8vw,15.5px);color:var(--dim);text-align:center}

/* ===================== SVG-СЦЕНЫ ===================== */
.figwrap{display:flex;flex:1 1 auto;min-height:0;min-width:0;align-items:center;justify-content:center;width:100%}
svg.fig{width:100%;height:auto;max-height:100%;display:block}
svg.fig text{font-family:var(--f);fill:var(--ink)}
svg.fig .lbl{font-size:15px;font-weight:700}
svg.fig .sml{font-size:12.5px;fill:var(--soft)}
svg.fig .mono{font-family:var(--m);font-size:12.5px;fill:#bfe9ff}

/* показ по шагам */
.step{opacity:0;transform:translateY(10px);transition:opacity .34s var(--ease),transform .34s var(--ease)}
.step.vis{opacity:1;transform:none}
[data-ph]{opacity:0;transition:opacity .3s var(--ease),transform .3s var(--ease)}
[data-ph].on{opacity:1}
.ghost{opacity:.22;transition:opacity .3s var(--ease)}

/* ===================== СЦЕНА С КНОПКАМИ ВПЕРЁД/НАЗАД ===================== */
.scene{display:flex;flex-direction:column;gap:9px;flex:1 1 auto;min-height:0}
.scbar{display:flex;align-items:center;gap:9px;flex-wrap:wrap;
 background:rgba(8,22,56,.75);border:1px solid rgba(42,212,255,.4);border-radius:var(--r2);padding:7px 10px}
.scbar button{font:700 13px/1 var(--f);color:#02121f;background:linear-gradient(160deg,var(--cy2),var(--cy));
 border:0;border-radius:8px;padding:8px 14px;cursor:pointer;box-shadow:0 0 14px rgba(42,212,255,.45);
 transition:transform .15s var(--ease),filter .15s}
.scbar button:hover{filter:brightness(1.12);transform:translateY(-1px)}
.scbar button:disabled{opacity:.35;cursor:default;box-shadow:none;transform:none}
.scbar button.sec{background:rgba(42,212,255,.14);color:var(--cy2);border:1px solid rgba(42,212,255,.5);box-shadow:none}
.scbar .pos{font:800 13px/1 var(--m);color:var(--cy2);padding:0 4px}
.scbar .cap{flex:1 1 320px;font-size:clamp(11.5px,.84vw,16.5px);line-height:1.35;color:var(--ink);font-weight:600}
.scbar .cap b{color:var(--cy2)}
.dots{display:flex;gap:5px}
.dots i{width:9px;height:9px;border-radius:3px;background:rgba(120,190,240,.28);transition:background .2s,box-shadow .2s}
.dots i.on{background:var(--cy);box-shadow:0 0 10px rgba(42,212,255,.9)}


/* движение пакетов/кадров внутри SVG-сцен */
svg [data-ph].mv{transform:translate(var(--x0,0px),var(--y0,0px))}
svg [data-ph].mv.on{transform:translate(var(--x1,0px),var(--y1,0px));
 transition:transform 1s var(--ease),opacity .25s var(--ease)}
svg .flow{stroke-dasharray:14 10;animation:dash 1.1s linear infinite}
@keyframes dash{to{stroke-dashoffset:-24}}
svg .pulse{animation:pls 1.4s ease-in-out infinite}
@keyframes pls{0%,100%{opacity:.35}50%{opacity:1}}

/* ===================== ТЕСТ / ЗАДАЧИ ===================== */
.q{background:var(--panel);border:1px solid var(--line);border-radius:var(--r);padding:13px 16px}
.q+.q{margin-top:11px}
.q .qt{font-weight:700;color:#fff;font-size:clamp(12.5px,.92vw,18px);line-height:1.4;margin-bottom:9px}
.opts{display:grid;gap:7px}
.opts button{text-align:left;font:600 clamp(11.5px,.84vw,16.5px)/1.38 var(--f);color:var(--soft);
 background:rgba(10,28,64,.6);border:1px solid rgba(60,160,230,.3);border-radius:var(--r2);
 padding:9px 13px;cursor:pointer;transition:all .18s var(--ease)}
.opts button:hover{border-color:rgba(42,212,255,.7);color:#fff;background:rgba(18,50,105,.7)}
.opts button.good{border-color:var(--lm);background:rgba(157,252,90,.16);color:#e6ffd6}
.opts button.bad{border-color:var(--rd);background:rgba(255,77,94,.16);color:#ffd7db}
.ex{display:none;margin-top:9px;font-size:clamp(11.5px,.83vw,16px);line-height:1.42;color:var(--soft);
 border-left:3px solid var(--cy);padding-left:11px}
.ex.on{display:block}
.score{font:800 14px/1 var(--m);color:var(--cy2)}
.inrow{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-top:9px}
.inrow input{font:700 14px/1 var(--m);color:#fff;background:rgba(2,10,28,.85);
 border:1px solid rgba(42,212,255,.45);border-radius:8px;padding:9px 12px;min-width:170px;outline:none}
.inrow input:focus{border-color:var(--cy);box-shadow:0 0 14px rgba(42,212,255,.4)}
.inrow button{font:700 13px/1 var(--f);color:#02121f;background:linear-gradient(160deg,var(--cy2),var(--cy));
 border:0;border-radius:8px;padding:10px 16px;cursor:pointer}
.inrow button.sec{background:rgba(42,212,255,.14);color:var(--cy2);border:1px solid rgba(42,212,255,.5)}
.note{margin-top:9px;font-size:clamp(11.5px,.83vw,16px);line-height:1.42;color:var(--soft)}
.note b.ok{color:var(--lm)} .note b.no{color:var(--rd)}

/* ===================== ТИТУЛ ===================== */
.cover{flex:1;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;gap:18px}
.cover .big{font-family:var(--fd);font-weight:700;text-transform:uppercase;line-height:.92;
 font-size:clamp(40px,7vw,120px);color:#fff;text-shadow:0 0 50px rgba(42,212,255,.55)}
.cover .big em{font-style:normal;color:var(--cy);text-shadow:0 0 50px rgba(42,212,255,1)}
.cover .lead{font-size:clamp(14px,1.3vw,24px);color:var(--soft);font-weight:600;max-width:900px;line-height:1.45}
.cover .meta{display:flex;gap:10px;flex-wrap:wrap;justify-content:center}

/* ===================== HUD ===================== */
#prog{position:fixed;left:0;bottom:0;height:3px;background:linear-gradient(90deg,var(--cy),var(--mg));z-index:6;
 transition:width .3s var(--ease);box-shadow:0 0 12px rgba(42,212,255,.8)}
#hud{position:fixed;left:0;right:0;bottom:0;height:56px;z-index:5;display:flex;align-items:center;gap:8px;
 padding:0 16px;background:linear-gradient(0deg,rgba(2,6,15,.96),rgba(2,6,15,.6));
 border-top:1px solid rgba(42,212,255,.25);backdrop-filter:blur(8px)}
#hud button{font:700 12.5px/1 var(--f);color:var(--cy2);background:rgba(42,212,255,.1);
 border:1px solid rgba(42,212,255,.4);border-radius:8px;padding:8px 12px;cursor:pointer;transition:all .16s}
#hud button:hover{background:rgba(42,212,255,.22);color:#fff}
#hud #count{font:800 12.5px/1 var(--m);color:var(--cy2);margin-left:6px}
#hud #sname{font:600 12.5px/1.2 var(--f);color:var(--soft);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:36vw}
#hud .hint{margin-left:auto;font:600 11px/1 var(--f);color:var(--dim);white-space:nowrap}
@media(max-width:900px){#hud .hint{display:none}}
#toc{position:fixed;inset:0;z-index:7;background:rgba(2,6,15,.96);backdrop-filter:blur(10px);
 display:none;flex-direction:column;padding:26px clamp(16px,3vw,60px) 26px}
#toc.on{display:flex}
#toc h2{font-family:var(--fd);font-weight:700;text-transform:uppercase;font-size:clamp(20px,2vw,34px);
 color:#fff;margin-bottom:14px}
#tocg{flex:1;overflow:auto;display:grid;grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:7px;
 align-content:start;padding-right:8px}
.tocit{display:flex;align-items:center;gap:9px;text-align:left;font:600 12.5px/1.3 var(--f);color:var(--soft);
 background:rgba(10,28,64,.55);border:1px solid rgba(60,160,230,.25);border-radius:9px;padding:8px 11px;cursor:pointer}
.tocit:hover{border-color:var(--cy);color:#fff}
.tocit i{flex:none;font:800 11px/1 var(--m);color:var(--cy);font-style:normal;min-width:26px}
"""
