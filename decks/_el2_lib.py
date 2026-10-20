# -*- coding: utf-8 -*-
"""Кит и движок деки «Сетевые устройства 2.1» (ледяной стиль Eltex).

Сцена 1920x1080, масштабируется под экран; фон морозный, без чёрных полей.
Шаги анимации: атрибут data-s="N" на элементе — элемент появляется на шаге N.
"""

PAL = dict(navy="#2b3356", blue="#5a7df0", deep="#221b3a", ice="#f1eefb")

CSS = r"""
@font-face{font-family:ElHead;src:url(__F_OS7__) format("woff2");font-weight:700;font-display:block}
@font-face{font-family:ElHead;src:url(__F_OS5__) format("woff2");font-weight:500;font-display:block}
@font-face{font-family:ElText;src:url(__F_IN4__) format("woff2");font-weight:400;font-display:block}
@font-face{font-family:ElText;src:url(__F_IN6__) format("woff2");font-weight:600;font-display:block}
@font-face{font-family:ElText;src:url(__F_IN8__) format("woff2");font-weight:800;font-display:block}
@font-face{font-family:ElMono;src:url(__F_MO4__) format("woff2");font-weight:400;font-display:block}
@font-face{font-family:ElMono;src:url(__F_MO7__) format("woff2");font-weight:700;font-display:block}
:root{
  --navy:#2b3356;--navy2:#221b3a;--blue:#5a7df0;--blue2:#4059d8;--sky:#9db6ff;
  --ice:#f1eefb;--mint:#e7f4ec;--cream:#fdf0e2;--rose:#fbeaf2;
  --ink:#303754;--dim:#6b7196;--line:rgba(150,145,200,.30);
  --card:rgba(255,255,255,.76);--card2:rgba(255,255,255,.90);
  --f:ElText,"Inter","Segoe UI",system-ui,sans-serif;--fh:ElHead,"Oswald","Segoe UI",sans-serif;
  --mono:ElMono,"IBM Plex Mono","Consolas",ui-monospace,monospace;
  --ez:cubic-bezier(.22,.7,.3,1);--sp:1;
  --sh:inset 0 2px 0 rgba(255,255,255,.98),inset 0 -5px 12px rgba(150,140,195,.09),0 4px 10px rgba(118,112,170,.10),0 22px 44px rgba(118,112,170,.16);
  --sh2:inset 0 2px 0 rgba(255,255,255,.96),inset 0 -4px 9px rgba(150,140,195,.09),0 3px 8px rgba(118,112,170,.10),0 12px 24px rgba(118,112,170,.13);
  --glass:linear-gradient(158deg,rgba(255,255,255,.96),rgba(246,243,255,.84));
}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;overflow:hidden;overscroll-behavior:none;background:#e9e6f4;font-family:var(--f);color:var(--ink)}
#bg{position:fixed;inset:0;background:url(__BG__) center/cover no-repeat}#bg::before,#bg::after{content:"";position:absolute;border-radius:50%;filter:blur(110px);opacity:.5}#bg::before{left:-6%;top:-12%;width:46vw;height:46vw;background:#ffe2c9}#bg::after{right:-8%;bottom:-14%;width:50vw;height:50vw;background:#e2ddfb}
#stage{position:fixed;inset:0;overflow-x:hidden;overflow-y:auto;display:flex;justify-content:center;align-items:flex-start;scrollbar-width:thin}
#scaler{position:relative;flex:none}
#deck{width:1920px;position:absolute;left:0;top:0;transform-origin:0 0}
.slide{position:relative;width:1920px;min-height:1080px;display:none;overflow:hidden;
  background:url(__BG__) center/cover no-repeat}
.slide::before,.slide::after{content:"";position:absolute;pointer-events:none;opacity:.85;z-index:0}
.slide.ice::before,.slide.ice::after{display:none}
__ICE__
.slide::before{left:0;top:0;width:520px;height:520px;background:url(__FTL__) left top/contain no-repeat}
.slide::after{right:0;bottom:0;width:520px;height:520px;background:url(__FBR__) right bottom/contain no-repeat}
.slide.on{display:block}.slide .pad>.glow{position:absolute;border-radius:50%;pointer-events:none;z-index:0}.slide::first-line{}
.pad{position:relative;min-height:1080px;z-index:2}
.ab{position:absolute}
.ctr-x{left:50%;transform:translateX(-50%)}
[data-s].ctr-x{transform:translateX(-50%) translateY(10px)}
[data-s].ctr-x.in{transform:translateX(-50%)}
.mono{font-family:var(--mono);font-variant-numeric:tabular-nums}
[style*="text-transform:uppercase"]{font-family:var(--fh);letter-spacing:.3px}
[style*="text-transform:uppercase"].mono{font-family:var(--mono)}
/* --- заголовки --- */
h1.t{font-family:var(--fh);font-size:66px;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:.6px;text-align:center;line-height:1.02}
h1.t .lt{color:var(--blue)}
h1.t.left{text-align:left}
.sub{font-family:var(--fh);font-size:26px;color:var(--blue);text-align:center;letter-spacing:5px;text-transform:uppercase;margin-top:10px;font-weight:500}
.sub.n{color:var(--dim);letter-spacing:1px;text-transform:none}
.big{font-family:var(--fh);font-size:92px;font-weight:700;color:var(--navy);line-height:.98;letter-spacing:0}
.big .lt{color:var(--blue)}
.kick{font-family:var(--fh);font-size:28px;font-weight:500;color:var(--blue);letter-spacing:6px;text-transform:uppercase}
/* --- карточки --- */
.card{background:var(--glass);border:none;border-radius:34px;box-shadow:var(--sh);
  backdrop-filter:blur(7px);-webkit-backdrop-filter:blur(7px);padding:26px 30px;position:relative}
.card.ab{position:absolute}
.card.solid{background:linear-gradient(158deg,#fff,#f3f0fe)}
.card.mint{background:linear-gradient(158deg,rgba(243,252,246,.97),rgba(206,233,215,.92))}
.card.cream{background:linear-gradient(158deg,rgba(255,248,238,.97),rgba(252,226,198,.92))}
.card.rose{background:linear-gradient(158deg,rgba(252,244,255,.97),rgba(232,219,250,.92))}
.ch{display:flex;align-items:center;gap:14px;font-family:var(--fh);font-size:32px;font-weight:700;color:var(--navy);text-transform:uppercase;letter-spacing:.4px;margin-bottom:18px;line-height:1.08}
.ch::before{content:"";width:8px;height:30px;border-radius:5px;flex:none;background:linear-gradient(180deg,#8aa2ff,#4f6ae4);box-shadow:0 2px 5px rgba(90,100,200,.35)}
.ch.nb::before{display:none}
.ch.sm{font-size:24px}
p.b{font-size:22px;line-height:1.5;color:var(--ink)}
p.b.sm{font-size:19px}
p.b.dim{color:var(--dim)}
.lead{font-size:26px;line-height:1.45}
/* --- элементы --- */
.chip{display:inline-flex;align-items:center;gap:10px;background:linear-gradient(170deg,#fff,#f1edfd);border:none;box-shadow:var(--sh2);
  border-radius:20px;padding:11px 20px;font-family:var(--mono);font-size:24px;color:var(--navy);font-weight:600}
.chip.key{min-width:76px;justify-content:center;font-weight:700;
  background:linear-gradient(180deg,#fff,#e9e4fb);box-shadow:inset 0 2px 0 #fff,0 5px 0 rgba(150,142,205,.30),0 12px 22px rgba(118,112,170,.18)}
.cmd{display:inline-block;background:linear-gradient(168deg,#3b3566,#241f45);color:#f0ecff;border-radius:22px;padding:14px 24px;
  font-family:var(--mono);font-size:26px;letter-spacing:.5px;box-shadow:inset 0 2px 0 rgba(255,255,255,.18),0 16px 30px rgba(58,48,110,.30)}
.cmd .a{color:#a9b9ff}
.num{font-family:var(--mono);font-size:56px;font-weight:800;color:#c6c0e8;line-height:1}
.badge{display:grid;place-items:center;width:50px;height:50px;border-radius:19px;background:linear-gradient(160deg,#90a6ff,#4a5fd8);color:#fff;
  font-weight:800;font-size:24px;font-family:var(--mono);flex:none;box-shadow:inset 0 2px 0 rgba(255,255,255,.55),inset 0 -3px 7px rgba(40,50,140,.25),0 10px 20px rgba(80,90,200,.30)}
.badge.o{background:linear-gradient(170deg,#fff,#efeafd);color:var(--blue);box-shadow:var(--sh2)}
.ico{display:grid;place-items:center;width:80px;height:80px;flex:none;border-radius:28px;
  background:linear-gradient(165deg,#ffffff,#eee9fc);border:none;color:var(--blue);box-shadow:var(--sh2)}
.ico svg{width:42px;height:42px;fill:none;stroke:currentColor;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.ico.sm{width:60px;height:60px;border-radius:22px}.ico.sm svg{width:30px;height:30px}
.ico.hex{border:none;background:none;position:relative}
.ico.hex::before{content:"";position:absolute;inset:0;background:rgba(255,255,255,.92);border:1.5px solid var(--line);
  clip-path:polygon(25% 3%,75% 3%,100% 50%,75% 97%,25% 97%,0 50%);border-radius:6px}
.ico.hex svg{position:relative}
.tag{display:inline-block;background:linear-gradient(170deg,#fff,#f1edfd);border:none;border-radius:24px;box-shadow:var(--sh2);
  padding:11px 24px;font-size:24px;font-weight:700;color:var(--navy)}
.tbl{width:100%;border-collapse:separate;border-spacing:0;font-size:20px;overflow:hidden;border-radius:20px;box-shadow:var(--sh2)}
.tbl th{background:#5a63a8;color:#fff;font-weight:700;padding:12px 16px;text-align:left;font-size:19px}
.tbl th.b2{background:#7a84c8}.tbl th.b3{background:#c3c4e6;color:var(--navy)}
.tbl td{background:rgba(255,255,255,.86);padding:12px 16px;border-bottom:1px solid rgba(160,155,205,.30);color:var(--ink)}
.tbl tr:last-child td{border-bottom:none}
.tbl td.hl{background:#dcf1e4;font-weight:700}
.note{display:flex;gap:14px;align-items:flex-start;background:linear-gradient(170deg,#fffdf8,#fbf0e2);border:none;box-shadow:var(--sh2);
  border-radius:26px;padding:18px 22px;font-size:20px;line-height:1.4}
.g{display:grid;gap:22px}
.row{display:flex;gap:22px}
.col{display:flex;flex-direction:column;gap:22px}
.ctr{align-items:center}.btw{justify-content:space-between}
.gr{flex:1}
img.ph{display:block;width:100%;height:auto;border-radius:26px;box-shadow:0 6px 14px rgba(118,112,170,.12),0 20px 40px rgba(118,112,170,.18)}
img.cut{display:block;width:100%;height:auto;mix-blend-mode:multiply;filter:drop-shadow(0 14px 24px rgba(110,100,165,.16))}
/* --- шаги --- */
[data-s]{opacity:0;transform:translateY(10px);
  transition:opacity calc(260ms/var(--sp)) var(--ez) calc(var(--dl,0ms)/var(--sp)),transform calc(260ms/var(--sp)) var(--ez) calc(var(--dl,0ms)/var(--sp))}
[data-s].in{opacity:1;transform:none}
svg .dr{stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset calc(620ms/var(--sp)) linear}
[data-s].in .dr,.dr[data-s].in{stroke-dashoffset:0}
svg .hd{opacity:0;transition:opacity calc(120ms/var(--sp)) linear calc(560ms/var(--sp))}
[data-s].in .hd,.hd[data-s].in{opacity:1}
.ni,.ni *{transition:none!important}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}
/* --- навигация --- */
#nav{opacity:1;transition:opacity .4s ease;position:fixed;z-index:50;left:50%;bottom:16px;transform:translateX(-50%);display:flex;align-items:center;gap:6px;
  background:rgba(255,255,255,.94);border:1px solid rgba(255,255,255,.95);border-radius:20px;
  box-shadow:0 10px 30px rgba(110,104,165,.22);padding:6px 8px;backdrop-filter:blur(8px)}
#nav button{font:inherit;font-size:14px;font-weight:600;border:1px solid transparent;background:transparent;color:var(--navy);
  border-radius:11px;padding:8px 13px;cursor:pointer;display:inline-flex;align-items:center;gap:6px}
#nav button:hover{background:var(--ice)}
#nav button.pri{background:var(--blue);color:#fff}
#nav button.pri:hover{background:var(--blue2)}
#nav button:focus-visible,.ovi:focus-visible{outline:3px solid var(--sky);outline-offset:2px}
#nav svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.4;stroke-linecap:round;stroke-linejoin:round}
#ind{font-family:var(--mono);font-size:13px;color:var(--navy);padding:0 8px;white-space:nowrap}
#ind .st{color:var(--dim);margin-left:10px}
#prog{position:fixed;left:0;top:0;height:4px;width:100%;z-index:60;background:rgba(255,255,255,.5)}
#prog i{display:block;height:100%;width:0;background:linear-gradient(90deg,#f3b98a,#b49bf0,#7f9bf5);transition:width .3s var(--ez)}
#ov{position:fixed;inset:0;z-index:70;background:rgba(243,240,252,.97);overflow:auto;padding:40px 60px}
#ov h2{font-size:30px;color:var(--navy);text-transform:uppercase;margin-bottom:18px}
.ovg{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:10px}
.ovi{font:inherit;text-align:left;display:flex;gap:12px;align-items:center;padding:12px 14px;background:#fff;
  border:1px solid var(--line);border-radius:18px;cursor:pointer;color:var(--navy);font-size:15px;box-shadow:0 3px 8px rgba(118,112,170,.08)}
.ovi:hover{border-color:var(--blue)}
.ovi .mono{color:var(--blue);font-weight:700;width:30px}
#nav.hid{opacity:0;pointer-events:none}
@media (max-width:860px){#nav{font-size:12px;bottom:8px}#nav .l2{display:none}}
"""

JS = r"""
(function(){
'use strict';
var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
var deck=$('#deck'),slides=$$('.slide'),N=slides.length,cur=0,step=0,RM=matchMedia('(prefers-reduced-motion: reduce)');
slides.forEach(function(s){var e=$$('[data-s]',s),m=0;e.forEach(function(x){var v=+x.dataset.s||0;if(v>m)m=v});s._e=e;s._m=m});
var stage=$('#stage'),scaler=$('#scaler'),K=1;
function autofit(pad){
  // 1) замеряем авторскую геометрию карточек ДО изменений
  var cards=[].slice.call(pad.querySelectorAll('.card'));
  var pr=pad.getBoundingClientRect();
  var box=cards.map(function(c){var r=c.getBoundingClientRect();
    return {el:c,l:r.left-pr.left,r:r.right-pr.left,t:r.top-pr.top,b:r.bottom-pr.top,d:0,
            abs:getComputedStyle(c).position==='absolute',
            top:!c.parentNode.closest('.card')};});   // вложенные карточки в раздвигании не участвуют
  // 2a) карточка, выросшая по потоку выше авторской высоты, — это тоже прирост,
  //     но он УЖЕ попал в замер, поэтому авторский низ поднимаем обратно
  box.forEach(function(o){
    var mh=parseFloat(o.el.style.minHeight);
    if(mh>0){ var dd=o.el.getBoundingClientRect().height-mh; if(dd>1){ o.d=dd; o.b-=dd; } }
  });
  // 2b) абсолютные дети не растягивают карточку — дотягиваем её до содержимого
  box.forEach(function(o){
    var cr=o.el.getBoundingClientRect(), max=0, kids=o.el.querySelectorAll('*');
    for(var k=0;k<kids.length;k++){
      var r=kids[k].getBoundingClientRect(); if(!r.width&&!r.height) continue;
      var bb=r.bottom-cr.top; if(bb>max) max=bb;
    }
    var pb=parseFloat(getComputedStyle(o.el).paddingBottom)||0;
    var need=Math.ceil(max+pb);
    if(need>cr.height+1){ o.d+=need-cr.height; o.el.style.minHeight=need+'px'; }
  });

  // 3) карточки ниже выросшей опускаются ровно настолько, чтобы не перекрыться
  box.sort(function(a,b){return a.t-b.t});
  for(var i=0;i<box.length;i++) box[i].h2=box[i].el.getBoundingClientRect().height;
  for(var j=0;j<box.length;j++){
    var B=box[j]; B.shift=B.shift||0;
    if(!B.abs||!B.top) continue;
    for(var i=0;i<j;i++){
      var A=box[i];
      if(!A.top||A.d<=0) continue;
      if(B.t<A.t+6) continue;                                    // не ниже
      var ox=Math.min(A.r,B.r)-Math.max(A.l,B.l);
      if(ox<Math.min(A.r-A.l,B.r-B.l)*0.45) continue;            // другая колонка
      var gap=Math.max(24,B.t-A.b);                              // авторский зазор
      var need=(A.t+(A.shift||0)+A.h2+gap)-(B.t+B.shift);
      if(need>0) B.shift+=need;
    }
  }
  box.forEach(function(o){ if(o.shift>0){
    var cur=parseFloat(getComputedStyle(o.el).top)||0;
    o.el.style.top=Math.round(cur+o.shift)+'px';
  }});
}
function slideH(sl){
  var pad=sl.querySelector('.pad'), prev=deck.style.transform;
  deck.style.transform='none';
  if(!sl._grown){ autofit(pad); sl._grown=1; }
  var top=pad.getBoundingClientRect().top, mb=1080;
  var all=pad.querySelectorAll('*');
  for(var i=0;i<all.length;i++){
    var e=all[i]; if(e.tagName==='svg'&&e.parentNode===pad) continue;
    var r=e.getBoundingClientRect(); if(!r.width&&!r.height) continue;
    var b=r.bottom-top; if(b>mb) mb=b;
  }
  deck.style.transform=prev;
  sl._h=Math.max(1080,Math.ceil(mb)+110);
  // абсолютные карточки не растягивают .pad — задаём высоту явно, иначе overflow:hidden режет
  sl.style.height=sl._h+'px';
  pad.style.minHeight=sl._h+'px';
  return sl._h;
}
function fit(){
  var W=innerWidth,H=innerHeight; if(!(W>0&&H>0))return;
  K=Math.min(W/1920,H/1080);
  var h=slideH(slides[cur]);
  deck.style.transform='scale('+K+')';
  scaler.style.width=(1920*K)+'px';
  scaler.style.height=(h*K)+'px';
}
addEventListener('resize',fit);
addEventListener('load',fit);
if(document.fonts&&document.fonts.ready)document.fonts.ready.then(fit);
function setStep(k,inst){
  var s=slides[cur];step=Math.max(0,Math.min(s._m,k));
  if(inst)s.classList.add('ni');
  s._e.forEach(function(x){x.classList.toggle('in',+x.dataset.s<=step)});
  if(inst){void s.offsetWidth;s.classList.remove('ni')}
  ui();
}
function go(i,end){
  i=Math.max(0,Math.min(N-1,i));
  slides.forEach(function(s){s.classList.remove('on')});cur=i;slides[cur].classList.add('on');
  stopCasc();
  setStep(RM.matches||end||slides[cur].dataset.auto==='1'?slides[cur]._m:0,true);
  fit(); stage.scrollTop=0; requestAnimationFrame(fit); setTimeout(fit,260);
  if(slides[cur].dataset.auto==='1'&&!end&&!RM.matches) cascade();
  try{history.replaceState(null,'','#'+(cur+1))}catch(e){}
}
var casc=null;
function stopCasc(){ if(casc){clearTimeout(casc);casc=null;} }
function cascade(){
  stopCasc();
  var sl=slides[cur]; if(!sl._m) return;
  if(RM.matches){ setStep(sl._m,true); return; }
  setStep(0,true);
  (function tick(){ if(step>=sl._m){casc=null;return;} setStep(step+1); casc=setTimeout(tick,130); })();
}
function isAuto(){ return slides[cur].dataset.auto==='1'; }
function next(){
  if(isAuto()){ if(casc){ stopCasc(); setStep(slides[cur]._m,true); return; } if(cur<N-1) go(cur+1); return; }
  if(step<slides[cur]._m){setStep(step+1)}else if(cur<N-1){go(cur+1)}
}
function prev(){
  if(isAuto()){ stopCasc(); if(cur>0) go(cur-1,true); return; }
  if(step>0){setStep(step-1,true)}else if(cur>0){go(cur-1,true)}
}
function ui(){
  var m=slides[cur]._m;
  var auto=slides[cur].dataset.auto==='1';
  $('#ind').innerHTML='слайд '+(cur+1)+' / '+N+((m&&!auto)?'<span class="st">шаг '+step+' / '+m+'</span>':'');
  $('#prog i').style.width=((cur+1)/N*100)+'%';
}
$('#b-prev').onclick=prev;$('#b-next').onclick=next;
var ov=$('#ov'),ovg=$('.ovg',ov);
slides.forEach(function(s,k){var b=document.createElement('button');b.type='button';b.className='ovi';
  b.innerHTML='<span class="mono">'+(k+1)+'</span><span></span>';b.lastChild.textContent=s.dataset.label||'';
  b.onclick=function(){ov.hidden=true;go(k)};ovg.appendChild(b)});
$('#b-ov').onclick=function(){ov.hidden=false};
var buf='',bt=null;
addEventListener('keydown',function(e){
  if(e.ctrlKey||e.metaKey||e.altKey)return;
  var tag=e.target.tagName;
  if(e.key==='Escape'){e.preventDefault();ov.hidden=!ov.hidden;return}
  if(!ov.hidden)return;
  if(e.key==='ArrowRight'||e.key==='PageDown'||(e.key===' '&&tag!=='BUTTON')){e.preventDefault();next();return}
  if(e.key==='ArrowLeft'||e.key==='PageUp'){e.preventDefault();prev();return}
  if(e.key==='Home'){go(0);return}
  if(e.key==='End'){go(N-1);return}
  if(/^[0-9]$/.test(e.key)){buf+=e.key;clearTimeout(bt);bt=setTimeout(function(){var n=+buf;buf='';if(n>=1&&n<=N)go(n-1)},550)}
});
var lw=0;
addEventListener('wheel',function(e){
  if(!ov.hidden)return;
  if(Math.abs(e.deltaY)<6)return;
  var canScroll=stage.scrollHeight-stage.clientHeight>2;
  if(canScroll){
    if(e.deltaY>0&&stage.scrollTop<stage.scrollHeight-stage.clientHeight-2)return;
    if(e.deltaY<0&&stage.scrollTop>2)return;
  }
  var now=Date.now();if(now-lw<480)return;lw=now;
  if(e.deltaY>0){ if(cur<N-1) go(cur+1); } else { if(cur>0) go(cur-1,true); }
},{passive:true});
var tx=0,ty=0,tt=0;
addEventListener('touchstart',function(e){var p=e.changedTouches[0];tx=p.clientX;ty=p.clientY;tt=Date.now()},{passive:true});
addEventListener('touchend',function(e){var p=e.changedTouches[0],dx=p.clientX-tx,dy=p.clientY-ty;
  if(Date.now()-tt>700||Math.abs(dx)<60||Math.abs(dx)<Math.abs(dy)*1.4)return;dx<0?next():prev()},{passive:true});
var nav=$('#nav'),nt=null;
function wake(){nav.classList.remove('hid');clearTimeout(nt);nt=setTimeout(function(){nav.classList.add('hid')},2600)}
['mousemove','keydown','wheel','touchstart','click'].forEach(function(e){addEventListener(e,wake,{passive:true})});
wake();
var h=parseInt((location.hash||'').slice(1),10);
go(h>=1&&h<=N?h-1:0);
})();
"""

NAV = ('<nav id="nav" aria-label="Навигация">'
       '<button id="b-prev" type="button" aria-label="Назад"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg></button>'
       '<span id="ind" aria-live="polite"></span>'
       '<button id="b-next" class="pri" type="button" aria-label="Дальше"><span class="l2">Дальше</span>'
       '<svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg></button>'
       '<button id="b-ov" type="button" title="Esc"><svg viewBox="0 0 24 24">'
       '<path d="M4 4h6v6H4zM14 4h6v6h-6zM4 14h6v6H4zM14 14h6v6h-6z"/></svg><span class="l2">Содержание</span></button>'
       '</nav><div id="prog"><i></i></div><div id="ov" hidden><h2>Содержание</h2><div class="ovg"></div></div>')


def icon(name):
    """Тонкие линейные иконки в стиле референсов."""
    p = {
        "wifi": '<path d="M5 12a10 10 0 0 1 14 0"/><path d="M8.5 15.5a5.5 5.5 0 0 1 7 0"/><circle cx="12" cy="19" r="1.3"/>',
        "speed": '<circle cx="12" cy="13" r="8"/><path d="M12 13l4-3.5"/><path d="M12 5V3"/>',
        "shield": '<path d="M12 3l7 3v6c0 4.5-3 7.5-7 9-4-1.5-7-4.5-7-9V6z"/>',
        "lock": '<rect x="5" y="10" width="14" height="10" rx="2.5"/><path d="M8.5 10V7.5a3.5 3.5 0 0 1 7 0V10"/>',
        "cloud": '<path d="M7 18h10a3.5 3.5 0 0 0 .3-7 5.5 5.5 0 0 0-10.5 1.3A3.4 3.4 0 0 0 7 18z"/>',
        "server": '<rect x="4" y="4" width="16" height="6" rx="2"/><rect x="4" y="14" width="16" height="6" rx="2"/><path d="M8 7h.01M8 17h.01"/>',
        "router": '<rect x="3" y="12" width="18" height="7" rx="2"/><path d="M7 16h.01M11 16h.01M15 16h.01"/><path d="M12 12V7m0 0l-3 3m3-3l3 3"/>',
        "switch": '<rect x="3" y="9" width="18" height="9" rx="2"/><path d="M6 13h.01M9 13h.01M12 13h.01M15 13h.01M18 13h.01"/>',
        "globe": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.5 2.6 2.5 14.4 0 17M12 3.5c-2.5 2.6-2.5 14.4 0 17"/>',
        "term": '<rect x="3" y="5" width="18" height="14" rx="3"/><path d="M7 10l3 2.5-3 2.5M13 15h4"/>',
        "gear": '<circle cx="12" cy="12" r="3.2"/><path d="M12 3v2.5M12 18.5V21M3 12h2.5M18.5 12H21M5.6 5.6l1.8 1.8M16.6 16.6l1.8 1.8M18.4 5.6l-1.8 1.8M7.4 16.6l-1.8 1.8"/>',
        "doc": '<path d="M7 3h7l4 4v14H7z"/><path d="M14 3v4h4"/><path d="M10 12h6M10 16h6"/>',
        "db": '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v12c0 1.7 3.1 3 7 3s7-1.3 7-3V6"/><path d="M5 12c0 1.7 3.1 3 7 3s7-1.3 7-3"/>',
        "fan": '<circle cx="12" cy="12" r="2"/><path d="M12 10c0-4 1-6 3-6s2 3-1 5M14 12c4 0 6 1 6 3s-3 2-5-1M12 14c0 4-1 6-3 6s-2-3 1-5M10 12c-4 0-6-1-6-3s3-2 5 1"/>',
        "ground": '<path d="M12 4v8"/><path d="M5 12h14M7.5 15.5h9M10 19h4"/>',
        "power": '<path d="M12 4v8"/><path d="M7.5 7a7 7 0 1 0 9 0"/>',
        "warn": '<path d="M12 4l9 16H3z"/><path d="M12 10v5M12 17.6h.01"/>',
        "info": '<circle cx="12" cy="12" r="8.5"/><path d="M12 11v6M12 8h.01"/>',
        "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7v5.5l3.5 2"/>',
        "temp": '<path d="M10 14V6a2 2 0 1 1 4 0v8a4 4 0 1 1-4 0z"/>',
        "chart": '<path d="M4 19V5"/><path d="M4 19h16"/><path d="M8 16v-5M12 16V8M16 16v-7"/>',
        "link": '<path d="M9.5 14.5l5-5"/><path d="M11 6.5l1.5-1.5a4 4 0 0 1 5.6 5.6L16.5 12"/><path d="M13 17.5L11.5 19a4 4 0 0 1-5.6-5.6L7.5 12"/>',
        "key": '<circle cx="8" cy="12" r="4"/><path d="M12 12h9M18 12v3M15 12v2"/>',
        "user": '<circle cx="12" cy="8.5" r="3.5"/><path d="M5 20c0-3.6 3.1-6 7-6s7 2.4 7 6"/>',
        "stack": '<path d="M12 4l8 4-8 4-8-4z"/><path d="M4 12l8 4 8-4"/><path d="M4 16l8 4 8-4"/>',
        "arrows": '<path d="M12 4v16M12 4l-3 3M12 4l3 3M12 20l-3-3M12 20l3-3"/><path d="M4 12h16M4 12l3-3M4 12l3 3M20 12l-3-3M20 12l3 3" opacity=".0"/>',
        "expand": '<path d="M4 9V4h5M20 15v5h-5M20 9V4h-5M4 15v5h5"/>',
        "bolt": '<path d="M13 3L5 14h6l-1 7 8-11h-6z"/>',
        "snow": '<path d="M12 3v18M4 7.5l16 9M20 7.5l-16 9"/>',
        "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 3v2M12 19v2M3 12h2M19 12h2M5.6 5.6l1.4 1.4M17 17l1.4 1.4M18.4 5.6L17 7M7 17l-1.4 1.4"/>',
        "mon": '<rect x="3" y="5" width="18" height="12" rx="2"/><path d="M9 21h6M12 17v4"/>',
        "net": '<circle cx="12" cy="5" r="2.2"/><circle cx="5" cy="19" r="2.2"/><circle cx="19" cy="19" r="2.2"/><path d="M12 7.2v6M12 13.2L6.6 17.4M12 13.2l5.4 4.2"/>',
        "phone": '<rect x="7" y="3" width="10" height="18" rx="2.5"/><path d="M10.5 18.5h3"/>',
        "print": '<path d="M7 9V4h10v5"/><rect x="4" y="9" width="16" height="7" rx="2"/><path d="M7 16h10v5H7z"/>',
        "pc": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
        "cable": '<path d="M7 3v5a5 5 0 0 0 10 0V3"/><path d="M9 3h2M13 3h2"/><path d="M12 13v8"/>',
        "usb": '<circle cx="12" cy="19" r="2"/><path d="M12 17V5"/><path d="M9 8l3-3 3 3"/><path d="M12 12l4-2.5"/>',
        "sd": '<path d="M8 3h8a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2V8z"/><path d="M10 6v3M13 6v3"/>',
        "check": '<circle cx="12" cy="12" r="8.5"/><path d="M8 12.5l2.6 2.6L16 9.5"/>',
        "cross": '<circle cx="12" cy="12" r="8.5"/><path d="M9 9l6 6M15 9l-6 6"/>',
        "search": '<circle cx="11" cy="11" r="6"/><path d="M15.5 15.5L20 20"/>',
        "save": '<path d="M5 3h11l3 3v15H5z"/><path d="M8 3v6h8V3M8 21v-7h8v7"/>',
        "reload": '<path d="M20 12a8 8 0 1 1-2.6-5.9"/><path d="M20 4v5h-5"/>',
        "list": '<path d="M8 7h12M8 12h12M8 17h12M4 7h.01M4 12h.01M4 17h.01"/>',
        "flag": '<path d="M6 21V4"/><path d="M6 5h11l-2 3.5L17 12H6z"/>',
        "layers": '<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/>',
        "wrench": '<path d="M15 7a4 4 0 0 1-5.3 5.3L5 17l2 2 4.7-4.7A4 4 0 0 0 17 9z"/>',
    }
    return '<svg viewBox="0 0 24 24">' + p.get(name, p["info"]) + '</svg>'


def ico(name, cls=""):
    return f'<span class="ico {cls}">{icon(name)}</span>'


def arrow_svg(x1, y1, x2, y2, step=None, col="var(--blue)", w=4, dash=False):
    """Прямая стрелка; рисуется при появлении шага."""
    import math
    dx, dy = x2 - x1, y2 - y1
    L = math.hypot(dx, dy) or 1
    ux, uy = dx / L, dy / L
    ex, ey = x2 - ux * 13, y2 - uy * 13
    nx, ny = -uy, ux
    bx, by = x2 - ux * 18, y2 - uy * 18
    at = f' data-s="{step}"' if step else ""
    d = ' stroke-dasharray="10 8"' if dash else ""
    return (f'<g{at}><path class="dr" pathLength="1" d="M{x1} {y1}L{ex:.1f} {ey:.1f}" stroke="{col}" stroke-width="{w}" '
            f'fill="none" stroke-linecap="round"{d}/>'
            f'<polygon class="hd" points="{x2},{y2} {bx+nx*8:.1f},{by+ny*8:.1f} {bx-nx*8:.1f},{by-ny*8:.1f}" fill="{col}"/></g>')


def build(slides, out, bg="assets/bg.jpg", ftl="assets/frost_tl.png", fbr="assets/frost_br.png", assets_dir=".", ice=()):
    """slides: список (label, html). Картинки src="assets/..." инлайнятся в base64."""
    import base64, os, re, pathlib
    root = pathlib.Path(assets_dir)

    cache = {}
    def b64(rel):
        if rel in cache: return cache[rel]
        p = root / rel
        data = base64.b64encode(p.read_bytes()).decode()
        ext = p.suffix.lower()
        mt = {".png": "image/png", ".svg": "image/svg+xml", ".woff2": "font/woff2", ".webp": "image/webp"}.get(ext, "image/jpeg")
        u = f"data:{mt};base64,{data}"
        cache[rel] = u
        return u

    css = CSS.replace("__BG__", b64(bg)).replace("__FTL__", b64(ftl)).replace("__FBR__", b64(fbr))
    for ph, fn in (("__F_OS7__", "oswald700.woff2"), ("__F_OS5__", "oswald500.woff2"),
                   ("__F_IN4__", "inter400.woff2"), ("__F_IN6__", "inter600.woff2"),
                   ("__F_IN8__", "inter800.woff2"), ("__F_MO4__", "mono400.woff2"),
                   ("__F_MO7__", "mono700.woff2")):
        css = css.replace(ph, b64(fn))
    css = css.replace("__ICE__", "".join(f".slide.ice.b{k}{{background-image:url({b64(f)})}}" for k, f in enumerate(ice)))
    body = []
    for item in slides:
        label, html = item[0], item[1]
        auto = item[2] if len(item) > 2 else "1"
        cls = f"slide ice b{item[3]}" if len(item) > 3 and ice else "slide"
        html = re.sub(r'src="assets/([^"]+)"', lambda m: f'src="{b64(m.group(1))}"', html)
        body.append(f'<section class="{cls}" data-label="{label}" data-auto="{auto}">'
                    f'<div class="pad">{html}</div></section>')
    doc = ('<!doctype html><html lang="ru"><head><meta charset="utf-8">'
           '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
           '<title>Сетевые устройства 2.1</title><style>' + css + '</style></head><body>'
           '<div id="bg"></div><div id="stage"><div id="scaler"><div id="deck">' + "".join(body) + '</div></div></div>'
           + NAV + '<script>' + JS + '</script></body></html>')
    pathlib.Path(out).write_text(doc, encoding="utf-8")
    return len(slides), os.path.getsize(out)
