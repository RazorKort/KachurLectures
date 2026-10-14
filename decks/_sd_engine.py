# -*- coding: utf-8 -*-
"""Движок деки 2.5: шаги, навигация, покадровые сцены, тесты и задачи."""

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

/* ---------- автозапуск анимаций слайда ---------- */
var T=[];
function later(fn,ms){T.push(setTimeout(fn,ms/speed));}
function clearScen(){T.forEach(clearTimeout);T=[];}
function runScen(){
  var s=slides[cur];
  clearScen();
  qa(s,'.go').forEach(function(e){if(!e.dataset.keep)e.classList.remove('go');});
  qa(s,'[data-at]').forEach(function(e){
    var ms=parseInt(e.dataset.at,10)||0;
    if(reduce){e.classList.add('go');return;}
    later(function(){e.classList.add('go');},ms);
  });
  qa(s,'.sx').forEach(function(sx){sxShow(sx,0);});
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
  },430/speed);
}
function stop(){if(timer){clearInterval(timer);timer=null;}}
function next(){stop();if(step<steps(cur).length){step++;paint();}else if(cur<slides.length-1)show(cur+1);}
function prev(){stop();if(step>0){step--;paint();}else if(cur>0)show(cur-1,true);}
function replay(){stop();step=0;paint();runScen();if(!reduce)run();}

/* ---------- покадровые сцены ---------- */
function sxShow(sx,k){
  var frames=qa(sx,'.fr'), caps=(sx.dataset.caps||'').split('|@|');
  k=Math.max(0,Math.min(frames.length-1,k));
  sx.dataset.k=k;
  frames.forEach(function(f,i){f.classList.toggle('on',i<=k);});
  var n=q(sx,'.sxn'); if(n)n.textContent=(k+1)+'/'+frames.length;
  var c=q(sx,'.sxc'); if(c)c.innerHTML=caps[k]||'';
  var bp=q(sx,'.sxp'), bn=q(sx,'.sxn2');
  if(bp)bp.disabled=(k===0);
  if(bn)bn.disabled=(k===frames.length-1);
}
qa(document,'.sx').forEach(function(sx){
  sxShow(sx,0);
  var bp=q(sx,'.sxp'), bn=q(sx,'.sxn2'), br=q(sx,'.sxr');
  if(bp)bp.onclick=function(e){e.stopPropagation();sxShow(sx,(+sx.dataset.k||0)-1);};
  if(bn)bn.onclick=function(e){e.stopPropagation();sxShow(sx,(+sx.dataset.k||0)+1);};
  if(br)br.onclick=function(e){e.stopPropagation();sxShow(sx,0);};
});

/* ---------- тесты ---------- */
var score={ok:0,all:0};
qa(document,'.q[data-q]').forEach(function(box){
  var done=false;
  qa(box,'.opts button').forEach(function(b){
    b.onclick=function(){
      if(done)return; done=true;
      var good=b.dataset.ok==='1';
      b.classList.add(good?'good':'bad');
      if(!good)qa(box,'.opts button').forEach(function(x){if(x.dataset.ok==='1')x.classList.add('good');});
      var ex=q(box,'.ex'); if(ex)ex.classList.add('on');
      score.all++; if(good)score.ok++;
      var s=document.getElementById('score');
      if(s)s.textContent='Верно: '+score.ok+' из '+score.all;
    };
  });
});

/* ---------- задачи с полем ввода ---------- */
function norm(s){return (s||'').toLowerCase().replace(/\s+/g,'').replace(/,/g,'.');}
qa(document,'.q[data-task]').forEach(function(box){
  var inp=q(box,'input'), btn=q(box,'.chk'), vd=q(box,'.verdict'), ex=q(box,'.ex');
  var answers=box.dataset.task.split('||').map(norm);
  function check(){
    var ok=answers.indexOf(norm(inp.value))>=0;
    vd.textContent=ok?'Верно':'Не то — смотри подсказку';
    vd.className='verdict '+(ok?'ok':'no');
    if(ex)ex.classList.add('on');
  }
  btn.onclick=check;
  inp.addEventListener('keydown',function(e){if(e.key==='Enter')check();});
});

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
  var sx=slides[cur].querySelector('.sx');
  if(sx&&e.shiftKey&&(k==='ArrowRight'||k==='ArrowLeft')){
    sxShow(sx,(+sx.dataset.k||0)+(k==='ArrowRight'?1:-1)); e.preventDefault(); return;
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
  var now=Date.now(); if(now-lock<430)return; lock=now;
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

show(0);
})();
"""
