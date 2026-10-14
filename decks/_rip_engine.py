# -*- coding: utf-8 -*-
"""Движок деки RIP: шаги, навигация, сценарии, печать CLI, тренажёр сходимости."""

JS = r"""
(function(){
'use strict';
var slides=[].slice.call(document.querySelectorAll('.slide'));
var cur=0, step=0, timer=null, speed=1;
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var elCount=document.getElementById('count'), elName=document.getElementById('sname'),
    elProg=document.getElementById('prog'), toc=document.getElementById('toc');

function qa(root,sel){return [].slice.call(root.querySelectorAll(sel));}
function q(root,sel){return root.querySelector(sel);}
function steps(i){return qa(slides[i],'.step');}

/* ---------- сценарии ---------- */
var SCEN={}, T=[];
function later(fn,ms){T.push(setTimeout(fn,ms/speed));}
function clearScen(){T.forEach(clearTimeout);T=[];}
function resetScen(s){
  qa(s,'.go').forEach(function(e){if(!e.dataset.keep)e.classList.remove('go');});
}
function runScen(){
  var s=slides[cur];
  clearScen(); resetScen(s);
  /* универсальный сценарий: всё с data-at загорается по расписанию */
  qa(s,'[data-at]').forEach(function(e){
    var ms=parseInt(e.dataset.at,10)||0;
    if(reduce){e.classList.add('go');return;}
    later(function(){e.classList.add('go');},ms);
  });
  var k=s.dataset.scen;
  if(k&&SCEN[k])SCEN[k](s,reduce);
}

function paint(){
  var st=steps(cur);
  st.forEach(function(e,k){e.classList.toggle('vis',k<step);});
  elCount.textContent=(cur+1)+' / '+slides.length+(st.length?'  ·  '+step+'/'+st.length:'');
  elName.textContent=slides[cur].dataset.label||'';
  elProg.style.width=((cur+1)/slides.length*100)+'%';
}
function show(i,openAll){
  stop(); clearScen();
  slides[cur].classList.remove('on');
  cur=Math.max(0,Math.min(slides.length-1,i));
  slides[cur].classList.add('on');
  var box=q(slides[cur],'.sc'); if(box)box.scrollTop=0;
  step=(openAll||reduce)?steps(cur).length:0;
  paint(); runScen();
  if(!reduce&&!openAll) run();
}
function run(){
  stop();
  var total=steps(cur).length;
  if(step>=total)return;
  timer=setInterval(function(){
    if(step>=total){stop();return;}
    step++;paint();
  },420/speed);
}
function stop(){if(timer){clearInterval(timer);timer=null;}}
function next(){stop();if(step<steps(cur).length){step++;paint();}else if(cur<slides.length-1)show(cur+1);}
function prev(){stop();if(step>0){step--;paint();}else if(cur>0)show(cur-1,true);}
function replay(){stop();step=0;paint();runScen();if(!reduce)run();}

/* ---------- содержание ---------- */
(function(){
  var g=document.getElementById('tocg');
  slides.forEach(function(s,i){
    var b=document.createElement('button');
    b.className='tocit';
    b.innerHTML='<i>'+(i+1)+'</i><span></span>';
    q(b,'span').textContent=s.dataset.label||'';
    b.onclick=function(){toc.classList.remove('on');show(i);};
    g.appendChild(b);
  });
})();

/* ---------- клавиатура ---------- */
function inField(e){var t=e.target;return t&&(t.tagName==='INPUT'||t.tagName==='TEXTAREA'||t.isContentEditable);}
var digits='';
document.addEventListener('keydown',function(e){
  if(inField(e))return;
  var k=e.key;
  if(k==='Escape'){toc.classList.toggle('on');e.preventDefault();return;}
  if(toc.classList.contains('on')){if(k==='Enter')toc.classList.remove('on');return;}
  if(k>='0'&&k<='9'){
    digits+=k; clearTimeout(window.__dt);
    window.__dt=setTimeout(function(){var n=parseInt(digits,10);digits='';if(n>=1)show(n-1);},550);
    e.preventDefault(); return;
  }
  if(k==='ArrowRight'){next();e.preventDefault();}
  else if(k===' '){if(timer)stop();else next();e.preventDefault();}
  else if(k==='ArrowLeft'){prev();e.preventDefault();}
  else if(k==='ArrowDown'||k==='PageDown'){show(cur+1);e.preventDefault();}
  else if(k==='ArrowUp'||k==='PageUp'){show(cur-1);e.preventDefault();}
  else if(k==='Home')show(0);
  else if(k==='End')show(slides.length-1);
  else if(k==='r'||k==='R'||k==='к'||k==='К')replay();
});

/* ---------- колесо и свайп ---------- */
var lock=0;
window.addEventListener('wheel',function(e){
  if(toc.classList.contains('on'))return;
  var box=e.target.closest?e.target.closest('.sc,.tw,.cli,.figwrap'):null;
  if(box){
    var atTop=box.scrollTop<=0, atEnd=box.scrollTop+box.clientHeight>=box.scrollHeight-1;
    if((e.deltaY>0&&!atEnd)||(e.deltaY<0&&!atTop))return;
  }
  var now=Date.now(); if(now-lock<420)return; lock=now;
  if(e.deltaY>0)next(); else prev();
},{passive:true});
var tx=0,ty=0;
window.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
window.addEventListener('touchend',function(e){
  var dx=e.changedTouches[0].clientX-tx, dy=e.changedTouches[0].clientY-ty;
  if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)){dx<0?next():prev();}
},{passive:true});

document.getElementById('bprev').onclick=prev;
document.getElementById('bnext').onclick=next;
document.getElementById('btoc').onclick=function(){toc.classList.toggle('on');};
document.getElementById('brun').onclick=replay;
document.getElementById('bspeed').onclick=function(){
  speed=speed===1?2:(speed===2?0.5:1);
  this.textContent=speed+'×';
};

/* ===================== СЦЕНАРИИ ===================== */

/* метрика: пакет идёт R1->R2->R3, счётчик переходов */
SCEN.metric=function(s,rm){
  var pk=q(s,'#mpk'), cnt=q(s,'#mcnt'), stops=[150,390,630,870];
  if(!pk)return;
  var i=0;
  function put(k){pk.setAttribute('cx',stops[k]);if(cnt)cnt.textContent=k;}
  put(0);
  if(rm){put(3);return;}
  function go(){
    i++; if(i>=stops.length)return;
    var from=stops[i-1], to=stops[i], t0=null, D=760;
    function fr(ts){
      if(!t0)t0=ts;
      var k=Math.min(1,(ts-t0)/(D/speed)), e=k<.5?2*k*k:1-Math.pow(-2*k+2,2)/2;
      pk.setAttribute('cx',from+(to-from)*e);
      if(k<1)requestAnimationFrame(fr);
      else{if(cnt)cnt.textContent=i;later(go,520);}
    }
    requestAnimationFrame(fr);
  }
  later(go,600);
};

/* предел 15 / 16 */
SCEN.limit=function(s,rm){
  var cells=qa(s,'.hopcell'), dead=q(s,'#deadnet'), bad=q(s,'#badge16');
  cells.forEach(function(e){e.classList.remove('on','bad');});
  if(dead)dead.classList.remove('go');
  if(bad)bad.classList.remove('go');
  if(rm){cells.forEach(function(e,i){e.classList.add(i===15?'bad':'on');});
         if(dead)dead.classList.add('go');if(bad)bad.classList.add('go');return;}
  cells.forEach(function(e,i){
    later(function(){e.classList.add(i===15?'bad':'on');
      if(i===15){if(dead)dead.classList.add('go');if(bad)bad.classList.add('go');}},300+i*150);
  });
};

/* таймеры: бегунок по шкале */
SCEN.timers=function(s,rm){
  var run=q(s,'#tmrun'), marks=qa(s,'.tmk'), lab=q(s,'#tmlab');
  if(!run)return;
  var X0=110, X1=1030, D=9200;
  marks.forEach(function(e){e.classList.remove('go');});
  run.setAttribute('x1',X0);run.setAttribute('x2',X0);
  if(rm){marks.forEach(function(e){e.classList.add('go');});run.setAttribute('x1',X1);run.setAttribute('x2',X1);
         if(lab)lab.textContent='flush 240 c';return;}
  var t0=null;
  function fr(ts){
    if(!t0)t0=ts;
    var k=Math.min(1,(ts-t0)/(D/speed)), x=X0+(X1-X0)*k;
    run.setAttribute('x1',x);run.setAttribute('x2',x);
    marks.forEach(function(e){
      var mx=parseFloat(e.dataset.x);
      if(x>=mx){e.classList.add('go');if(lab&&e.dataset.lab)lab.textContent=e.dataset.lab;}
    });
    if(k<1&&slides[cur]===s)requestAnimationFrame(fr);
  }
  later(function(){requestAnimationFrame(fr);},500);
};

/* петля: метрика растёт по кольцу */
SCEN.loop=function(s,rm){
  var out=q(s,'#loopm'), arcs=qa(s,'.lparc'), note=q(s,'#loopnote');
  if(!out)return;
  var vals=[2,3,4,5,6,7,'…',16], i=0;
  arcs.forEach(function(e){e.classList.remove('go');});
  if(note)note.classList.remove('go');
  out.textContent='2';
  if(rm){out.textContent='16';if(note)note.classList.add('go');arcs.forEach(function(e){e.classList.add('go')});return;}
  function tick(){
    if(i>=vals.length){if(note)note.classList.add('go');return;}
    out.textContent=vals[i];
    var a=arcs[i%arcs.length]; if(a){a.classList.remove('go');void a.offsetWidth;a.classList.add('go');}
    i++; later(tick,620);
  }
  later(tick,500);
};

/* печать команд */
SCEN.type=function(s,rm){
  var pre=q(s,'[data-type]');
  if(!pre)return;
  var full=pre.dataset.type;
  if(rm){pre.innerHTML=full;return;}
  pre.textContent='';
  var i=0, raw=full.replace(/<[^>]+>/g,'');
  var iv=setInterval(function(){
    if(slides[cur]!==s){clearInterval(iv);return;}
    i++; pre.textContent=raw.slice(0,i);
    if(i>=raw.length){clearInterval(iv);pre.innerHTML=full+'<span class="cur"></span>';}
  },28/speed);
  T.push(iv);
};

/* ===================== ТРЕНАЖЁР СХОДИМОСТИ ===================== */
(function(){
  var root=document.getElementById('sim');
  if(!root)return;
  var NAMES=['R1','R2','R3','R4'];
  var DEST='192.168.1.0/24';           /* сеть за R1 */
  var INF=16;
  var sh=true, broken=false, tick=0, conv=-1, state=null, busy=null;

  function fresh(){
    /* метрика до сети DEST: R1=0 (своя), остальные по цепочке */
    return [
      {m:0,via:null},{m:1,via:0},{m:2,via:1},{m:3,via:2}
    ];
  }
  function neighbours(i){
    var n=[];
    if(i>0)n.push(i-1);
    if(i<3)n.push(i+1);
    /* разрыв линка R1-R2 */
    if(broken){n=n.filter(function(j){return !((i===0&&j===1)||(i===1&&j===0));});}
    return n;
  }
  function reset(){
    state=fresh(); broken=false; tick=0; conv=-1;
    if(busy){clearTimeout(busy);busy=null;}
    draw([]);
    note('Исходное состояние: сеть '+DEST+' известна всем. Разорвите линк R1—R2.');
  }
  function note(t){q(root,'#simnote').textContent=t;}

  function stepSim(){
    /* каждый маршрутизатор рассылает вектор соседям, затем все применяют */
    var offers=[];
    for(var i=0;i<4;i++){
      neighbours(i).forEach(function(j){
        var m=state[i].m;
        if(sh&&state[i].via===j)return;          /* разделение горизонта */
        offers.push({to:j,from:i,m:Math.min(INF,m+1)});
      });
    }
    var changed=[];
    var snapshot=state.map(function(r){return {m:r.m,via:r.via};});
    offers.forEach(function(o){
      var r=state[o.to];
      if(o.to===0)return;                         /* R1 — владелец сети */
      if(o.m<r.m || r.via===o.from){
        if(r.m!==o.m||r.via!==o.from){
          r.m=o.m; r.via=o.from;
        }
      }
    });
    for(var k=0;k<4;k++){
      if(state[k].m!==snapshot[k].m||state[k].via!==snapshot[k].via)changed.push(k);
    }
    tick++;
    draw(changed);
    var allInf=state.slice(1).every(function(r){return r.m>=INF;});
    if(changed.length===0||allInf){
      if(conv<0){conv=tick;}
      note(allInf
        ? 'Сходимость за '+tick+' тактов: метрика дошла до 16, сеть объявлена недоступной.'
        : 'Сходимость за '+tick+' тактов: таблицы перестали меняться.');
      return false;
    }
    note('Такт '+tick+': обновились '+changed.map(function(i){return NAMES[i];}).join(', ')+'.');
    return true;
  }
  function autoRun(){
    if(busy){clearTimeout(busy);busy=null;}
    (function loop(){
      if(stepSim())busy=setTimeout(loop,780);
      else busy=null;
    })();
  }
  function draw(changed){
    var box=q(root,'#simtab'); box.innerHTML='';
    state.forEach(function(r,i){
      var d=document.createElement('div');
      var inf=r.m>=INF;
      d.className='rw'+(changed.indexOf(i)>=0?' upd':'')+(inf?' inf':'');
      d.innerHTML='<span><b>'+NAMES[i]+'</b> &nbsp;'+DEST+'</span>'+
                  '<span>'+(r.via===null?'своя':'через '+NAMES[r.via])+'</span>'+
                  '<span>'+(inf?'16 — недоступна':'метрика '+r.m)+'</span>';
      box.appendChild(d);
    });
    q(root,'#simtick').textContent=tick;
    q(root,'#simconv').textContent=conv<0?'—':conv;
    var cut=q(root,'#simcut'); if(cut)cut.style.opacity=broken?1:0;
  }
  q(root,'#simbreak').onclick=function(){
    if(broken)return;
    broken=true;
    state[1].m=INF; state[1].via=null;          /* R2 теряет прямой путь */
    tick=0; conv=-1; draw([1]);
    note('Линк R1—R2 разорван. R2 ставит метрику 16 и рассылает обновление.');
    autoRun();
  };
  q(root,'#simstep').onclick=function(){if(busy){clearTimeout(busy);busy=null;}stepSim();};
  q(root,'#simreset').onclick=reset;
  q(root,'#simsh').onclick=function(){
    sh=!sh; this.classList.toggle('on',sh);
    this.textContent='Разделение горизонта: '+(sh?'вкл':'выкл');
    reset();
  };
  reset();
})();

/* ===================== КВИЗ ===================== */
(function(){
  var done=0, right=0, total=qa(document,'.q').length;
  qa(document,'.q').forEach(function(box){
    var ex=q(box,'.ex'), answered=false;
    qa(box,'.opts button').forEach(function(b){
      b.onclick=function(){
        if(answered)return; answered=true;
        var good=b.dataset.ok==='1';
        b.classList.add(good?'good':'bad');
        if(!good)qa(box,'.opts button').forEach(function(o){if(o.dataset.ok==='1')o.classList.add('good');});
        if(ex)ex.classList.add('on');
        done++; if(good)right++;
        var sc=document.getElementById('score');
        if(sc)sc.textContent=right+' / '+total;
      };
    });
  });
})();

show(0);
})();
"""
