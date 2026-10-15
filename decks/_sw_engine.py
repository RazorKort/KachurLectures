# -*- coding: utf-8 -*-
"""Движок деки «Коммутаторы и коммутация»: шаги, сцены с кнопками вперёд/назад, тест, задачи."""

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
function stepsOf(i){return qa(slides[i],'.step');}

/* ===================== ПОКАЗ СЛАЙДА ===================== */
function paint(){
  var st=stepsOf(cur);
  st.forEach(function(e,k){e.classList.toggle('vis',k<step);});
  elCount.textContent=(cur+1)+' / '+slides.length+(st.length?'  ·  '+step+'/'+st.length:'');
  elName.textContent=slides[cur].dataset.label||'';
  elProg.style.width=((cur+1)/slides.length*100)+'%';
}
function show(i,openAll){
  stop();
  slides[cur].classList.remove('on');
  cur=Math.max(0,Math.min(slides.length-1,i));
  slides[cur].classList.add('on');
  var box=q(slides[cur],'.sc'); if(box)box.scrollTop=0;
  step=(openAll||reduce)?stepsOf(cur).length:0;
  paint();
  qa(slides[cur],'.scene').forEach(function(s){ SCN.reset(s); });
  if(!reduce&&!openAll) run();
}
function run(){
  stop();
  var total=stepsOf(cur).length;
  if(step>=total)return;
  timer=setInterval(function(){
    if(step>=total){stop();return;}
    step++;paint();
  },640/speed);
}
function stop(){if(timer){clearInterval(timer);timer=null;}}
function next(){stop();if(step<stepsOf(cur).length){step++;paint();}else if(cur<slides.length-1)show(cur+1);}
function prev(){stop();if(step>0){step--;paint();}else if(cur>0)show(cur-1,true);}
function replay(){
  stop();step=0;paint();
  qa(slides[cur],'.scene').forEach(function(s){SCN.reset(s);});
  if(!reduce)run();
}

/* ===================== СОДЕРЖАНИЕ ===================== */
(function(){
  var gg=document.getElementById('tocg');
  slides.forEach(function(s,i){
    var b=document.createElement('button');
    b.className='tocit';
    b.innerHTML='<i>'+(i+1)+'</i><span></span>';
    q(b,'span').textContent=s.dataset.label||'';
    b.onclick=function(){toc.classList.remove('on');show(i);};
    gg.appendChild(b);
  });
})();

/* ===================== КЛАВИАТУРА ===================== */
function inField(e){var t=e.target;return t&&(t.tagName==='INPUT'||t.tagName==='TEXTAREA'||t.isContentEditable);}
var digits='';
document.addEventListener('keydown',function(e){
  if(inField(e))return;
  var k=e.key;
  if(k==='Escape'){toc.classList.toggle('on');e.preventDefault();return;}
  if(toc.classList.contains('on')){if(k==='Enter')toc.classList.remove('on');return;}
  if(k>='0'&&k<='9'){
    digits+=k; clearTimeout(window.__dt);
    window.__dt=setTimeout(function(){var n=parseInt(digits,10);digits='';if(n>=1)show(n-1);},600);
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
  else if(k==='n'||k==='N'){ /* шаг сцены вперёд */ var s=q(slides[cur],'.scene'); if(s)SCN.go(s,1); }
  else if(k==='b'||k==='B'){ var s2=q(slides[cur],'.scene'); if(s2)SCN.go(s2,-1); }
});

/* свайпы (колесо намеренно НЕ листает слайды) */
var tx=0,ty=0;
document.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
document.addEventListener('touchend',function(e){
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

/* ===================== СЦЕНЫ С КНОПКАМИ ВПЕРЁД/НАЗАД ===================== */
var SCN=(function(){
  var state={}, timers={};

  function nOf(s){return parseInt(s.dataset.n,10)||1;}
  function apply(s){
    var k=s.dataset.scene, i=state[k]||0;
    qa(s,'[data-ph]').forEach(function(e){
      var at=parseInt(e.dataset.ph,10);
      var only=e.hasAttribute('data-ph-only');
      var upto=e.hasAttribute('data-ph-upto')?parseInt(e.dataset.phUpto,10):null;
      var on;
      if(only) on=(i===at);
      else if(upto!==null) on=(i>=at&&i<=upto);
      else on=(i>=at);
      e.classList.toggle('on',on);
    });
    qa(s,'[data-ghost]').forEach(function(e){
      var at=parseInt(e.dataset.ghost,10);
      e.classList.toggle('ghost',i>=at);
    });
    var pos=q(s,'.pos'); if(pos)pos.textContent=(i+1)+' / '+nOf(s);
    qa(s,'.dots i').forEach(function(d,j){d.classList.toggle('on',j<=i);});
    qa(s,'[data-cap]').forEach(function(c){c.style.display=(parseInt(c.dataset.cap,10)===i)?'':'none';});
    var bp=q(s,'[data-act="prev"]'), bn=q(s,'[data-act="next"]');
    if(bp)bp.disabled=(i<=0);
    if(bn)bn.disabled=(i>=nOf(s)-1);
  }
  function go(s,d){
    var k=s.dataset.scene, n=nOf(s);
    state[k]=Math.max(0,Math.min(n-1,(state[k]||0)+d));
    apply(s);
  }
  function set(s,i){state[s.dataset.scene]=i;apply(s);}
  function reset(s){stopPlay(s);set(s,0);}
  function stopPlay(s){
    var k=s.dataset.scene;
    if(timers[k]){clearInterval(timers[k]);timers[k]=null;}
    var b=q(s,'[data-act="play"]'); if(b)b.textContent='▷ Авто';
  }
  function play(s){
    var k=s.dataset.scene;
    if(timers[k]){stopPlay(s);return;}
    if((state[k]||0)>=nOf(s)-1)set(s,0);
    var b=q(s,'[data-act="play"]'); if(b)b.textContent='‖ Стоп';
    timers[k]=setInterval(function(){
      if((state[k]||0)>=nOf(s)-1){stopPlay(s);return;}
      go(s,1);
    },1500/speed);
  }

  qa(document,'.scene').forEach(function(s){
    state[s.dataset.scene]=0;
    qa(s,'.scbar button').forEach(function(b){
      b.onclick=function(){
        var a=b.dataset.act;
        if(a==='next'){stopPlay(s);go(s,1);}
        else if(a==='prev'){stopPlay(s);go(s,-1);}
        else if(a==='first'){stopPlay(s);set(s,0);}
        else if(a==='play'){play(s);}
      };
    });
    apply(s);
  });
  return {go:go,set:set,reset:reset,apply:apply};
})();

/* ===================== ТЕСТ ===================== */
(function(){
  var all=qa(document,'.q:not(.task)');
  var right=0, done=0, total=all.length;
  all.forEach(function(box){
    var ex=q(box,'.ex'), answered=false;
    qa(box,'.opts button').forEach(function(b){
      b.onclick=function(){
        if(answered)return; answered=true;
        var good=b.dataset.ok==='1';
        b.classList.add(good?'good':'bad');
        if(!good)qa(box,'.opts button').forEach(function(o){if(o.dataset.ok==='1')o.classList.add('good');});
        if(ex)ex.classList.add('on');
        done++; if(good)right++;
        qa(document,'.score').forEach(function(s){
          s.textContent=right+' / '+total+'  (отвечено '+done+')';
        });
      };
    });
  });
})();

/* ===================== ЗАДАЧИ СО СВОБОДНЫМ ОТВЕТОМ ===================== */
(function(){
  function norm(v){
    return String(v).toLowerCase().replace(/ё/g,'е')
      .replace(/[\s ]+/g,'').replace(/[.,;]+$/,'');
  }
  qa(document,'.task').forEach(function(box){
    var inp=q(box,'input'), note=q(box,'[data-note]'), ex=q(box,'[data-ex]');
    var answers=box.dataset.ans.split('|').map(norm);
    function check(){
      var v=inp.value.trim();
      if(!v){note.innerHTML='Введите ответ.';return;}
      if(answers.indexOf(norm(v))>=0){
        note.innerHTML='<b class="ok">Верно.</b>';
        if(ex)ex.classList.add('on');
      }else{
        note.innerHTML='<b class="no">Пока нет.</b> Проверьте рассуждение и попробуйте снова.';
      }
    }
    q(box,'[data-act="check"]').onclick=check;
    q(box,'[data-act="show"]').onclick=function(){
      note.innerHTML='Ответ: <b>'+box.dataset.ans.split('|')[0]+'</b>';
      if(ex)ex.classList.add('on');
    };
    inp.addEventListener('keydown',function(e){if(e.key==='Enter'){check();e.preventDefault();}});
  });
})();

show(0);
})();
"""
