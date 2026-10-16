# -*- coding: utf-8 -*-
"""Стиль деки 2.6 — поверх неонового каркаса 2.2: тёмно-синий HUD с глобусом,
жирные гротеск-заголовки, глянцевые плашки этапов (жёлтый/оранжевый/фиолетовый/зелёный)."""

from _sw_style import CSS as BASE

EXTRA = r"""
:root{--ye:#ffd23f;--vi:#b077ff;--gr:#6cf08a;--bl:#4aa8ff;
 --fd:"Montserrat","Golos Text","Arial Black",system-ui,sans-serif;
 --panel:linear-gradient(160deg,rgba(16,48,104,.72),rgba(5,16,42,.9));}

/* фон: слои-варианты по слайдам */
.bgl{position:fixed;inset:0;width:100%;height:100%;z-index:0;pointer-events:none;opacity:0;
 transition:opacity .9s var(--ease)}
body[data-bg="a"] .bgl[data-bgk="a"],body[data-bg="b"] .bgl[data-bgk="b"],
body[data-bg="c"] .bgl[data-bgk="c"],body[data-bg="d"] .bgl[data-bgk="d"]{opacity:1}
.bgl .spin{transform-box:fill-box;transform-origin:center;animation:spin 26s linear infinite}
@keyframes spin{from{transform:scaleX(1)}50%{transform:scaleX(.35)}to{transform:scaleX(1)}}
.bgl .tw{animation:tw 3.6s ease-in-out infinite}
@keyframes tw{0%,100%{opacity:.25}50%{opacity:1}}
.bgl .run{animation:run 7s linear infinite}
@keyframes run{from{stroke-dashoffset:1460}to{stroke-dashoffset:0}}
.bgl .orb{animation:orb 40s linear infinite}
@keyframes orb{to{stroke-dashoffset:-600}}
#bgfx{background:radial-gradient(1200px 700px at 50% 50%,transparent 55%,rgba(0,3,12,.72) 100%)}
#bgfx::after{opacity:.28}
#bgfx .blob{position:absolute;border-radius:50%;filter:blur(60px);opacity:.35;animation:drift 22s ease-in-out infinite alternate}
#bgfx .b1{width:520px;height:420px;left:-120px;top:20%;background:#1c6dff}
#bgfx .b2{width:460px;height:380px;right:10%;bottom:-140px;background:#7a3cff;animation-duration:28s}
#bgfx .b3{width:380px;height:300px;left:40%;top:-160px;background:#00b4ff;animation-duration:34s}
@keyframes drift{to{transform:translate(120px,-60px) scale(1.15)}}
@media (prefers-reduced-motion:reduce){.bgl *,#bgfx *{animation:none!important}}

/* автоподгонка */
.slide>.sc{display:flex;flex-direction:column}
.slide>.sc>.wrap{display:flex;flex-direction:column;gap:12px;flex:1 1 auto;min-height:0}
.grow{grid-template-rows:minmax(0,1fr)}.col>.scene{min-height:0}
.scene .figwrap svg.fig{max-height:100%;height:100%}
.wrap>.g{flex:0 0 auto}.wrap>.grow{flex:1 1 auto;min-height:0}

/* заголовки — жирный гротеск как на инфографиках */
.head{padding-left:0}
.head::before{display:none}
.kick{font:800 clamp(11px,.8vw,15px)/1 var(--f);letter-spacing:.16em;text-transform:uppercase;color:var(--cy);margin-bottom:6px}
h1.t{font-family:var(--fd);font-weight:900;text-transform:none;letter-spacing:-.01em;line-height:1.02;
 font-size:clamp(26px,3vw,54px);text-shadow:0 2px 0 rgba(0,0,0,.4),0 0 30px rgba(60,170,255,.35)}
h1.t em{color:var(--cy)} h1.t em.y{color:var(--ye);text-shadow:0 0 24px rgba(255,210,63,.6)}
h1.t em.v{color:var(--vi)}
p.sub{color:#8fc4ff;font-size:clamp(14px,1.15vw,21px);font-weight:700}
.ch h3{font-family:var(--fd);font-weight:800;text-transform:none;font-size:clamp(15px,1.2vw,24px)}
.c p,ul.li li,.ir span:last-child,.foot{font-size:clamp(14px,1.02vw,19.5px)}
.tw table{font-size:clamp(13px,.95vw,18px)}
pre.cli{font-size:clamp(13px,.95vw,17.5px)}
.scbar .cap{font-size:clamp(14px,1vw,19px)}
.scbar button{font-size:14.5px;padding:9px 16px}
.q .qt{font-size:clamp(15px,1.1vw,21px)} .opts button{font-size:clamp(14px,1vw,19px)}
.c{border-color:rgba(80,170,255,.4);background:var(--panel);backdrop-filter:blur(3px)}
.c.ye{border-color:rgba(255,210,63,.6);box-shadow:inset 0 0 26px rgba(255,210,63,.08),0 0 24px rgba(255,210,63,.2)}
.c.vi{border-color:rgba(176,119,255,.6);box-shadow:inset 0 0 26px rgba(176,119,255,.09),0 0 24px rgba(176,119,255,.22)}
.c.or{border-color:rgba(255,138,61,.6);box-shadow:inset 0 0 26px rgba(255,138,61,.08),0 0 24px rgba(255,138,61,.2)}
svg.fig text{paint-order:stroke;stroke:rgba(2,8,24,.55);stroke-width:3px}

/* глянцевые плашки этапов */
.pill{display:flex;align-items:center;gap:14px;border-radius:999px;padding:7px 22px 7px 7px;
 color:#0b1630;box-shadow:0 0 22px rgba(0,0,0,.25),inset 0 2px 0 rgba(255,255,255,.45),inset 0 -6px 14px rgba(0,0,0,.12)}
.pill .pn{flex:none;width:46px;height:46px;border-radius:50%;background:#0b1630;color:#fff;display:grid;place-items:center;
 font:900 22px/1 var(--fd)}
.pill .ph{font:900 clamp(17px,1.5vw,28px)/1.05 var(--fd);letter-spacing:-.01em}
.pill .pt{margin-left:auto;font:700 clamp(13px,1vw,18px)/1.25 var(--f);text-align:right;opacity:.9}
.pill.y{background:linear-gradient(180deg,#ffe57a,#ffc21f);box-shadow:0 0 26px rgba(255,200,40,.5)}
.pill.o{background:linear-gradient(180deg,#ffb37a,#ff7a2b);box-shadow:0 0 26px rgba(255,130,50,.5)}
.pill.v{background:linear-gradient(180deg,#d2adff,#9c5cff);box-shadow:0 0 26px rgba(170,110,255,.5)}
.pill.g{background:linear-gradient(180deg,#b9ff9a,#57e06a);box-shadow:0 0 26px rgba(100,230,110,.5)}
.pill.cy{background:linear-gradient(180deg,#9fefff,#2ad4ff);box-shadow:0 0 26px rgba(42,212,255,.5)}
.pill.r{background:linear-gradient(180deg,#ff9aa5,#ff4d5e);box-shadow:0 0 26px rgba(255,77,94,.5)}

/* пакеты Источник/Назначение */
.kvs{display:flex;flex-direction:column;gap:7px}
.kv{display:flex;align-items:stretch;border-radius:10px;overflow:hidden;background:rgba(70,140,220,.2);
 font-size:clamp(13.5px,1vw,18.5px)}
.kv .kl{flex:0 0 38%;padding:8px 12px;color:var(--soft);font-weight:700}
.kv .kvv{flex:1;padding:8px 12px;font:800 1em/1.2 var(--m);color:#08142c;background:var(--cy)}
.kvv.y{background:var(--ye)}.kvv.o{background:var(--or)}.kvv.v{background:var(--vi)}.kvv.g{background:var(--gr)}
.kvv.r{background:var(--rd);color:#fff}
.bigline{font:900 clamp(18px,1.6vw,30px)/1.15 var(--fd);color:#fff;text-align:center;padding:14px 18px;border-radius:16px;
 background:linear-gradient(90deg,rgba(42,212,255,.18),rgba(176,119,255,.18));border:1px solid rgba(120,190,255,.45)}
.bigline.y{color:var(--ye)}
.mono{font-family:var(--m)}
.formula{font:800 clamp(18px,1.6vw,30px)/1.3 var(--m);color:var(--ye);text-align:center;padding:10px;
 background:rgba(2,10,28,.6);border-radius:12px;border:1px dashed rgba(255,210,63,.5)}

/* титул */
.cover .kick{font-size:clamp(13px,1.1vw,20px)}
.cover .big{font-family:var(--fd);font-weight:900;text-transform:none;font-size:clamp(46px,7.4vw,130px);letter-spacing:-.02em}
.cover .orn{display:flex;gap:10px;align-items:center}
.cover .orn i{width:70px;height:3px;background:linear-gradient(90deg,transparent,var(--cy))}
.cover .orn i:last-child{background:linear-gradient(90deg,var(--cy),transparent)}
.cover .orn b{width:12px;height:12px;transform:rotate(45deg);background:var(--ye);box-shadow:0 0 14px var(--ye)}
.cover .who{font:700 clamp(14px,1.2vw,22px)/1.5 var(--f);color:#cfe6ff}
"""

WS = r"""
.ws{border-radius:14px;overflow:hidden;border:1px solid rgba(80,170,255,.5);background:#071330;
 box-shadow:0 0 30px rgba(20,100,220,.3);display:flex;flex-direction:column;min-height:0}
.wsbar{display:flex;gap:7px;align-items:center;padding:8px 12px;background:linear-gradient(90deg,#123a7a,#0b234f)}
.wsbar i{width:11px;height:11px;border-radius:50%;background:#ff5f57}.wsbar i+i{background:#febc2e}.wsbar i+i+i{background:#28c840}
.wsbar span{margin-left:8px;font:700 13px/1 var(--m);color:#bfe1ff}
.wstop{display:flex;gap:10px;align-items:center;padding:9px 12px;background:rgba(255,210,63,.16);
 border-bottom:1px solid rgba(255,210,63,.4);font:700 clamp(13px,.95vw,17px)/1.3 var(--m);color:#fff}
pre.wsp{margin:0;padding:10px 12px;font:600 clamp(13px,.95vw,17.5px)/1.65 var(--m);color:#bcd6f5;overflow:auto;white-space:pre}
pre.wsp span{display:block}
pre.wsp .wsh{background:rgba(255,77,94,.16);outline:1.5px solid rgba(255,77,94,.75);border-radius:4px;color:#fff;margin:2px 0}
.wsn{display:inline-grid;place-items:center;width:22px;height:22px;border-radius:50%;background:var(--rd);color:#fff;
 font:800 12px/1 var(--f);margin-right:8px;vertical-align:1px}
"""

CSS = BASE + EXTRA + WS

CSS += r"""
.col>.step:has(>.pill){flex:0 0 auto}
.col:has(>.step>.pill){justify-content:space-around}
.pill .ph{flex:0 0 auto;max-width:42%}
"""
