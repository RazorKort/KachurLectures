# -*- coding: utf-8 -*-
"""Стили практики по модели OSI (длинная скроллящаяся страница)."""

CSS = r"""
*{box-sizing:border-box;margin:0;padding:0}
:root{
--canvas:#eef1f6; --paper:#ffffff; --deep:#101726; --deep-2:#19223a;
--line:#d7deea; --line-d:rgba(150,180,230,.20);
--ink:#111827; --dim:#5b6678; --on-dark:#eef3fb; --on-dark-dim:#9fb0cc;

--l1:#7a8699;   /* физический   */
--l2:#e0922f;   /* канальный    */
--l3:#3b82f6;   /* сетевой      */
--l4:#8b5cf6;   /* транспортный */
--l5:#0ea5a3;   /* сеансовый    */
--l6:#d9557f;   /* представления*/
--l7:#22a060;   /* прикладной   */
--red:#e2504b; --amber:#e0922f; --green:#22a060; --blue:#3b82f6;

--r:14px; --ease:cubic-bezier(.22,.7,.3,1);
--f:"Segoe UI Variable Display","Segoe UI",Inter,system-ui,-apple-system,Arial,sans-serif;
--m:"Cascadia Mono","JetBrains Mono",Consolas,"SF Mono",ui-monospace,monospace;
}
html{scroll-behavior:smooth}
body{font-family:var(--f);color:var(--ink);background:var(--canvas);
 -webkit-font-smoothing:antialiased;text-rendering:optimizeLegibility;line-height:1.5}
#bg{position:fixed;inset:0;z-index:0;pointer-events:none;
 background:
  radial-gradient(900px 600px at 12% -5%,rgba(59,130,246,.10),transparent 60%),
  radial-gradient(800px 560px at 92% 8%,rgba(139,92,246,.09),transparent 62%),
  radial-gradient(900px 700px at 50% 108%,rgba(14,165,163,.09),transparent 60%)}

/* ---------- верхняя панель ---------- */
#top{position:fixed;top:0;left:0;right:0;z-index:50;backdrop-filter:blur(10px);
 background:rgba(238,241,246,.86);border-bottom:1px solid var(--line)}
#prog{height:3px;background:linear-gradient(90deg,var(--l7),var(--l4),var(--l3));width:0;
 transition:width .12s linear}
#nav{display:flex;gap:7px;align-items:center;padding:8px clamp(12px,2vw,26px);overflow-x:auto;
 scrollbar-width:none}
#nav::-webkit-scrollbar{display:none}
#nav b{font-size:13px;font-weight:800;letter-spacing:.02em;color:#0d1526;margin-right:6px;white-space:nowrap}
#nav a{flex:none;font-size:12.5px;font-weight:650;color:var(--dim);text-decoration:none;
 padding:5px 11px;border-radius:999px;border:1px solid transparent;white-space:nowrap;transition:.18s}
#nav a:hover{color:var(--ink);background:rgba(255,255,255,.8);border-color:var(--line)}
#nav a.on{color:#0b2f6b;background:rgba(59,130,246,.13);border-color:rgba(59,130,246,.42)}

/* ---------- каркас ---------- */
#page{position:relative;z-index:1;max-width:1180px;margin:0 auto;
 padding:clamp(70px,7vh,96px) clamp(16px,3vw,34px) 120px}
section.sc{padding:clamp(34px,5vh,64px) 0;scroll-margin-top:84px}
section.sc+section.sc{border-top:1px solid var(--line)}

.kick{display:inline-flex;align-items:center;gap:8px;font:800 11.5px/1 var(--f);
 letter-spacing:.14em;text-transform:uppercase;color:#64718a;margin-bottom:12px}
.kick i{width:22px;height:2px;background:currentColor;border-radius:2px;font-style:normal}

h1{font-size:clamp(30px,4.4vw,62px);font-weight:830;letter-spacing:-.025em;line-height:1.03;color:#07101f}
h1 em{font-style:normal;color:var(--l3)}
h2{font-size:clamp(23px,2.7vw,40px);font-weight:800;letter-spacing:-.02em;line-height:1.1;color:#07101f}
h3{font-size:clamp(16px,1.25vw,21px);font-weight:760;line-height:1.25;color:#0b1424}
h4{font-size:clamp(13.5px,1vw,16px);font-weight:740;color:#0b1424;margin-bottom:7px}
p{font-size:clamp(14px,1.02vw,17.5px);color:#3d4759;line-height:1.56}
p+p{margin-top:9px}
.lead{font-size:clamp(15px,1.2vw,21px);color:#36415a;max-width:860px;margin-top:14px}
.sub{margin-top:10px;max-width:880px;color:#4c586c}
small.note{display:block;margin-top:10px;font-size:13px;color:#6b7687}

/* ---------- сетки ---------- */
.g{display:grid;gap:clamp(12px,1.2vw,20px);margin-top:clamp(16px,2vw,26px)}
.g2{grid-template-columns:repeat(2,1fr)}
.g3{grid-template-columns:repeat(3,1fr)}
.g4{grid-template-columns:repeat(4,1fr)}
.g23{grid-template-columns:1.25fr 1fr}
.g32{grid-template-columns:1fr 1.25fr}
@media(max-width:880px){.g2,.g3,.g4,.g23,.g32{grid-template-columns:1fr}}

/* ---------- карточки ---------- */
.c{background:var(--paper);border:1px solid var(--line);border-radius:var(--r);
 padding:clamp(15px,1.15vw,22px) clamp(16px,1.25vw,24px);box-shadow:0 5px 18px rgba(23,42,80,.06);
 display:flex;flex-direction:column}
.c.d{background:var(--deep);border-color:var(--line-d);color:var(--on-dark-dim);
 box-shadow:0 14px 34px rgba(10,18,36,.3)}
.c.d h3,.c.d h4,.c.d b{color:var(--on-dark)}
.c.d p{color:var(--on-dark-dim)}
.c.tint{background:#f7f9fd}
.c>h3+p,.c>h4+p{margin-top:2px}
.ch{display:flex;gap:11px;align-items:flex-start;margin-bottom:9px}
.num{flex:none;min-width:34px;height:30px;border-radius:8px;display:grid;place-items:center;
 font:800 14px/1 var(--m);background:rgba(59,130,246,.11);border:1px solid rgba(59,130,246,.4);color:#1d5ec4}
.c.d .num{background:rgba(147,197,253,.11);border-color:rgba(147,197,253,.36);color:#9ec5fe}
.hr{height:1px;background:var(--line);margin:11px 0}
.c.d .hr{background:var(--line-d)}

/* ---------- бейджи уровней ---------- */
.lv{display:inline-flex;align-items:center;gap:7px;font:800 11.5px/1 var(--f);letter-spacing:.06em;
 padding:5px 10px;border-radius:999px;text-transform:uppercase;white-space:nowrap}
.lv b{font-weight:900;font-family:var(--m)}
.lv1{background:rgba(122,134,153,.14);color:#4d586b;border:1px solid rgba(122,134,153,.4)}
.lv2{background:rgba(224,146,47,.14);color:#92590d;border:1px solid rgba(224,146,47,.42)}
.lv3{background:rgba(59,130,246,.13);color:#17519f;border:1px solid rgba(59,130,246,.42)}
.lv4{background:rgba(139,92,246,.13);color:#5b2bbd;border:1px solid rgba(139,92,246,.42)}
.lv5{background:rgba(14,165,163,.13);color:#0a6b6a;border:1px solid rgba(14,165,163,.42)}
.lv6{background:rgba(217,85,127,.13);color:#9c2f55;border:1px solid rgba(217,85,127,.42)}
.lv7{background:rgba(34,160,96,.13);color:#146b3e;border:1px solid rgba(34,160,96,.42)}

/* ---------- списки ---------- */
ul.ck{list-style:none;display:flex;flex-direction:column;gap:7px}
ul.ck li{position:relative;padding-left:26px;font-size:clamp(13.5px,.95vw,16.5px);color:#3d4759;line-height:1.45}
ul.ck li::before{content:"";position:absolute;left:0;top:3px;width:16px;height:16px;border-radius:50%;
 background:rgba(34,160,96,.13);border:1px solid rgba(34,160,96,.45)}
ul.ck li::after{content:"";position:absolute;left:4.6px;top:7.4px;width:6px;height:3px;
 border-left:1.7px solid var(--green);border-bottom:1.7px solid var(--green);transform:rotate(-45deg)}
.c.d ul.ck li{color:var(--on-dark-dim)}
ul.ck.num{counter-reset:n}
ul.ck.num li::after{display:none}
ul.ck.num li::before{counter-increment:n;content:counter(n);display:grid;place-items:center;
 font:800 10px/16px var(--f);color:#17519f;background:rgba(59,130,246,.13);border-color:rgba(59,130,246,.42)}
ul.ck.q li::before{background:rgba(59,130,246,.12);border-color:rgba(59,130,246,.4)}
ul.ck.q li::after{content:"?";border:none;transform:none;left:5.4px;top:2px;width:auto;height:auto;
 font:800 11px/16px var(--f);color:#1d5ec4}
ul.ck.bad li::before{background:rgba(226,80,75,.12);border-color:rgba(226,80,75,.45)}
ul.ck.bad li::after{width:7px;height:0;border-left:none;border-bottom:1.8px solid var(--red);
 transform:none;left:4.5px;top:10px}

/* ---------- моно-плашки, байты, hex ---------- */
code,kbd,.mono{font-family:var(--m)}
.kv{font:600 13px/1.5 var(--m);color:#13325f;background:rgba(59,130,246,.09);
 border:1px solid rgba(59,130,246,.22);border-radius:6px;padding:1px 6px;white-space:nowrap}
.c.d .kv{color:#bcd6ff;background:rgba(147,197,253,.1);border-color:rgba(147,197,253,.22)}
pre.hex{font:600 clamp(11px,.85vw,13.5px)/1.75 var(--m);background:var(--deep);color:#cfe0ff;
 border:1px solid var(--line-d);border-radius:12px;padding:14px 16px;overflow-x:auto;margin-top:12px;
 white-space:pre}
pre.hex .o{color:#6f83a8}
pre.hex .h2{color:#f0b35c}
pre.hex .h3{color:#8fbcff}
pre.hex .h4{color:#c4a8ff}
pre.hex .h7{color:#7adfa4}
pre.hex b{color:#fff}

/* ---------- таблицы ---------- */
.tw{overflow-x:auto;margin-top:14px;border:1px solid var(--line);border-radius:12px;background:var(--paper)}
table{border-collapse:collapse;width:100%;font-size:clamp(12.5px,.9vw,15px)}
th,td{padding:9px 12px;text-align:left;border-bottom:1px solid var(--line);white-space:nowrap}
th{font-weight:780;font-size:12px;letter-spacing:.04em;text-transform:uppercase;color:#5d6a80;
 background:#f6f8fc}
tr:last-child td{border-bottom:none}
td.m,th.m{font-family:var(--m);font-size:.95em}
tr.hi td{background:rgba(59,130,246,.09)}
tr.ok td{background:rgba(34,160,96,.09)}
caption{caption-side:top;text-align:left;padding:10px 12px;font-size:13px;font-weight:720;color:#44506a;
 background:#fbfcfe;border-bottom:1px solid var(--line)}

/* ---------- схема заголовка (поля) ---------- */
.hdr{margin-top:14px}
.hdr .hrow{display:flex;flex-wrap:wrap;gap:6px}
.fld{flex:1 1 auto;min-width:72px;border-radius:9px;padding:7px 9px;cursor:default;
 border:1px solid var(--line);background:#f8fafd;transition:.18s var(--ease)}
.fld .fn{font:800 9.5px/1.2 var(--f);letter-spacing:.07em;text-transform:uppercase;color:#6b788f}
.fld .fv{font:700 clamp(11.5px,.85vw,14px)/1.35 var(--m);color:#0d1b33;margin-top:3px;word-break:break-all;
 white-space:normal}
.fld:hover{transform:translateY(-2px);box-shadow:0 7px 18px rgba(23,42,80,.1)}
.fld.c2{background:rgba(224,146,47,.09);border-color:rgba(224,146,47,.34)}
.fld.c3{background:rgba(59,130,246,.09);border-color:rgba(59,130,246,.32)}
.fld.c4{background:rgba(139,92,246,.09);border-color:rgba(139,92,246,.32)}
.fld.c7{background:rgba(34,160,96,.09);border-color:rgba(34,160,96,.32)}
.fld.key{box-shadow:inset 0 0 0 1.5px rgba(226,80,75,.5)}
.fld .fw{font:600 9.5px/1 var(--m);color:#8a94a8;margin-top:4px}

/* ---------- капсулы инкапсуляции ---------- */
.enc{margin-top:16px;display:flex;flex-direction:column;gap:0}
.enc .lay{border-radius:12px;padding:10px 12px;border:1px solid var(--line);background:#fff;
 position:relative}
.enc .lay+.lay{margin-top:-1px}
.pdu{display:flex;align-items:stretch;gap:0;border-radius:10px;overflow:hidden;border:1px solid var(--line);
 background:#fff;font-family:var(--m);font-size:12px;flex-wrap:nowrap;min-width:0}
.pdu span{padding:8px 10px;white-space:nowrap;border-right:1px solid var(--line);
 display:flex;align-items:center;justify-content:center;font-weight:700}
.pdu span:last-child{border-right:none}
.pdu .d7{background:rgba(34,160,96,.14);color:#146b3e;flex:1 1 auto;min-width:0}
.pdu .h4b{background:rgba(139,92,246,.16);color:#5b2bbd}
.pdu .h3b{background:rgba(59,130,246,.16);color:#17519f}
.pdu .h2b{background:rgba(224,146,47,.18);color:#92590d}
.pdu .t2b{background:rgba(224,146,47,.1);color:#92590d}
.pdu .h1b{background:rgba(122,134,153,.16);color:#4d586b}

/* ---------- сцены (анимация) ---------- */
.scene{margin-top:clamp(16px,2vw,24px);border:1px solid var(--line);border-radius:var(--r);
 background:var(--paper);box-shadow:0 6px 22px rgba(23,42,80,.07);overflow:hidden}
.scene>.sh{display:flex;align-items:center;gap:10px;padding:10px 14px;border-bottom:1px solid var(--line);
 background:#f7f9fd;flex-wrap:wrap}
.scene>.sh h4{margin:0;flex:1 1 auto}
.btn{font:700 12.5px/1 var(--f);padding:7px 12px;border-radius:999px;border:1px solid var(--line);
 background:#fff;color:#2c3850;cursor:pointer;transition:.16s}
.btn:hover{background:rgba(59,130,246,.1);border-color:rgba(59,130,246,.4);color:#17519f}
.btn.on{background:rgba(59,130,246,.14);border-color:rgba(59,130,246,.48);color:#17519f}
.scene .stepn{font:700 12px/1 var(--m);color:#6b788f;min-width:46px;text-align:right}
.scene .body{padding:clamp(10px,1.2vw,18px)}
.scene svg{display:block;width:100%;height:auto}
.scene .cap{padding:0 clamp(12px,1.3vw,18px) 14px;min-height:46px}
.scene .cap p{font-size:clamp(13px,.95vw,16px);color:#3d4759}
.scene .cap .t{display:none}
.scene .cap .t.on{display:block;animation:fadeup .3s var(--ease)}
@keyframes fadeup{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}

/* элементы сцен */
.sv .fade{opacity:0;transition:opacity .35s var(--ease)}
.sv .fade.on{opacity:1}
.sv .lit{transition:.35s var(--ease)}
svg text{font-family:var(--f);fill:#25314a}
svg .mono{font-family:var(--m)}

/* ---------- раскрытие при скролле ---------- */
.rv{opacity:0;transform:translateY(18px);transition:opacity .5s var(--ease),transform .5s var(--ease)}
.rv.on{opacity:1;transform:none}

/* ---------- задания ---------- */
.task{border:1px solid rgba(139,92,246,.35);background:linear-gradient(180deg,#fcfaff,#f7f4ff);
 border-radius:var(--r);padding:clamp(15px,1.2vw,22px);margin-top:clamp(16px,2vw,24px)}
.task .tt{display:flex;align-items:center;gap:10px;margin-bottom:10px}
.task .tt .tg{font:800 10.5px/1 var(--f);letter-spacing:.12em;text-transform:uppercase;color:#5b2bbd;
 background:rgba(139,92,246,.14);border:1px solid rgba(139,92,246,.4);padding:5px 9px;border-radius:999px}
.task .tt h4{margin:0}
.qrow{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin-top:9px;font-size:14.5px;color:#3d4759}
.qrow label{flex:1 1 230px;min-width:180px}
.qrow input{font:600 13.5px/1 var(--m);padding:8px 10px;border-radius:8px;border:1px solid #cdd6e6;
 background:#fff;width:100%;margin-top:5px;transition:.16s}
.qrow input:focus{outline:none;border-color:rgba(139,92,246,.6);box-shadow:0 0 0 3px rgba(139,92,246,.14)}
.qrow input.ok{border-color:rgba(34,160,96,.6);background:rgba(34,160,96,.07)}
.qrow input.no{border-color:rgba(226,80,75,.6);background:rgba(226,80,75,.07)}
.task .fo{margin-top:12px;display:flex;gap:9px;align-items:center;flex-wrap:wrap}
.task .ver{font:700 13px/1.4 var(--f);color:#146b3e;display:none}
.task .ver.on{display:block}
.task .ans{display:none;margin-top:11px;border-top:1px dashed rgba(139,92,246,.4);padding-top:11px}
.task .ans.on{display:block;animation:fadeup .3s var(--ease)}
.task .ans p{font-size:14px}

/* ---------- врезки ---------- */
.callout{display:flex;gap:12px;margin-top:14px;padding:13px 15px;border-radius:12px;
 background:rgba(59,130,246,.07);border:1px solid rgba(59,130,246,.26)}
.callout i{flex:none;width:24px;height:24px;border-radius:50%;display:grid;place-items:center;font-style:normal;
 font:800 13px/1 var(--f);background:rgba(59,130,246,.16);color:#17519f;border:1px solid rgba(59,130,246,.4)}
.callout p{font-size:14.5px;color:#2f3d57}
.callout.warn{background:rgba(226,80,75,.07);border-color:rgba(226,80,75,.28)}
.callout.warn i{background:rgba(226,80,75,.15);color:#b4322d;border-color:rgba(226,80,75,.4)}
.callout.ok{background:rgba(34,160,96,.07);border-color:rgba(34,160,96,.28)}
.callout.ok i{background:rgba(34,160,96,.15);color:#146b3e;border-color:rgba(34,160,96,.4)}

/* ---------- титул ---------- */
#hero{padding:clamp(26px,5vh,56px) 0 clamp(20px,3vh,36px)}
#hero .meta{display:flex;flex-wrap:wrap;gap:8px;margin-top:22px}
#hero .meta span{font:700 12.5px/1 var(--f);padding:7px 12px;border-radius:999px;background:#fff;
 border:1px solid var(--line);color:#3f4b61}
.foot{margin-top:40px;padding-top:18px;border-top:1px solid var(--line);display:flex;gap:16px;
 flex-wrap:wrap;align-items:center;font-size:13.5px;color:#5b6678}
.foot b{color:#1c2740}

@media(max-width:620px){
 th,td{white-space:normal}
 .pdu{flex-wrap:wrap}
 .pdu span{border-right:none}
}
@media print{#top{display:none}.rv{opacity:1;transform:none}}

/* ---------- svg-сцены: движение пакетов ---------- */
.sv .pk{transition:transform .85s var(--ease),opacity .3s linear}
.sv .fade{opacity:0;transition:opacity .3s linear,transform .85s var(--ease)}
.sv .fade.on{opacity:1}
.sv .pk rect{filter:drop-shadow(0 3px 7px rgba(23,42,80,.16))}
"""
