# -*- coding: utf-8 -*-
"""Движок мятно-бирюзовой деки: шаги, навигация, сценарии, интерактив."""

JS = r"""
(function(){
'use strict';
var slides=[].slice.call(document.querySelectorAll('.slide'));
var cur=0, step=0, timer=null, speed=1;
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var elCount=document.getElementById('count'), elName=document.getElementById('sname'),
    elProg=document.getElementById('prog'), toc=document.getElementById('toc');

function steps(i){return [].slice.call(slides[i].querySelectorAll('.step'));}

/* ---------- сценарии слайдов ---------- */
var SCEN={}, scenTimers=[];
function later(fn,ms){scenTimers.push(setTimeout(fn,ms/speed));}
function clearScen(){scenTimers.forEach(clearTimeout);scenTimers=[];}
function runScen(){
  var s=slides[cur], k=s.dataset.scen;
  if(!k||!SCEN[k])return;
  clearScen(); SCEN[k](s, reduce);
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
  var box=slides[cur].querySelector('.sc'); if(box)box.scrollTop=0;
  step=(openAll||reduce)?steps(cur).length:0;
  paint(); runScen();
  if(!reduce&&!openAll) run();
}
function run(){
  stop();
  var total=steps(cur).length;
  if(step>=total){runScen();return;}
  timer=setInterval(function(){
    if(step>=total){stop();return;}
    step++;paint();
  },420/speed);
}
function stop(){if(timer){clearInterval(timer);timer=null;}}
function next(){stop();if(step<steps(cur).length){step++;paint();}else if(cur<slides.length-1)show(cur+1);}
function prev(){stop();if(step>0){step--;paint();}else if(cur>0)show(cur-1,true);}

/* ---------- содержание ---------- */
(function(){
  var g=document.getElementById('tocg');
  slides.forEach(function(s,i){
    var b=document.createElement('button');
    b.className='tocit';
    b.innerHTML='<i>'+(i+1)+'</i><span></span>';
    b.querySelector('span').textContent=s.dataset.label||'';
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
  else if(k===' '){if(timer){stop();}else{next();}e.preventDefault();}
  else if(k==='ArrowLeft'){prev();e.preventDefault();}
  else if(k==='ArrowDown'||k==='PageDown'){show(cur+1);e.preventDefault();}
  else if(k==='ArrowUp'||k==='PageUp'){show(cur-1);e.preventDefault();}
  else if(k==='Home'){show(0);}
  else if(k==='End'){show(slides.length-1);}
  else if(k==='r'||k==='R'||k==='к'||k==='К'){step=0;paint();clearScen();run();runScen();}
});

/* ---------- колесо и свайп ---------- */
var lock=0;
window.addEventListener('wheel',function(e){
  if(toc.classList.contains('on'))return;
  var box=e.target.closest('.sc,.tw,.q');
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
document.getElementById('brun').onclick=function(){step=0;paint();clearScen();run();runScen();};
document.getElementById('bspeed').onclick=function(){
  speed=speed===1?2:(speed===2?0.5:1);
  this.textContent=speed+'×';
  if(timer)run();
};

/* ================= СЦЕНАРИИ ================= */
function q(s,sel){return s.querySelector(sel);}
function qa(s,sel){return [].slice.call(s.querySelectorAll(sel));}

/* лесенка единиц */
SCEN.ladder=function(s,rm){
  var st=qa(s,'.ladder .stp'), mu=qa(s,'.ladder .mul');
  st.forEach(function(e){e.style.opacity=0;e.style.transform='translateY(14px)';});
  mu.forEach(function(e){e.style.opacity=0;});
  st.forEach(function(e,i){
    later(function(){e.style.transition='.45s cubic-bezier(.22,.7,.3,1)';e.style.opacity=1;e.style.transform='none';
      if(mu[i-1]){mu[i-1].style.transition='.3s';mu[i-1].style.opacity=1;}},rm?0:i*420);
  });
};

/* труба T = G + O */
function pipePaint(s,ov){
  var g=q(s,'#pipeG'), o=q(s,'#pipeO'), lg=q(s,'#labG'), lo=q(s,'#labO'),
      bg=q(s,'#brG'), bo=q(s,'#brO');
  var W=640, x0=120;
  var ow=W*ov/100, gw=W-ow;
  if(g){g.setAttribute('width',gw);}
  if(o){o.setAttribute('x',x0+gw);o.setAttribute('width',ow);}
  if(lg){lg.setAttribute('x',x0+gw/2);}
  if(lo){lo.setAttribute('x',x0+gw+ow/2);}
  if(bg){bg.setAttribute('d','M'+x0+' 250 v8 h'+gw+' v-8');}
  if(bo){bo.setAttribute('d','M'+(x0+gw)+' 250 v8 h'+ow+' v-8');}
}
SCEN.pipe=function(s,rm){
  var g=q(s,'#pipeG'), o=q(s,'#pipeO'), br=qa(s,'.brk');
  var ov=22;
  br.forEach(function(e){e.style.opacity=0;});
  if(rm){pipePaint(s,ov);br.forEach(function(e){e.style.opacity=1;});return;}
  g.setAttribute('width',0); o.setAttribute('width',0); o.setAttribute('x',120);
  var W=640, ow=W*ov/100, gw=W-ow, t0=null, D=900;
  function frame(ts){
    if(!t0)t0=ts;
    var k=Math.min(1,(ts-t0)/(D/speed));
    var e=1-Math.pow(1-k,3);
    g.setAttribute('width',gw*e);
    if(k>=1){
      var t1=null;
      function frame2(ts2){
        if(!t1)t1=ts2;
        var k2=Math.min(1,(ts2-t1)/(520/speed)), e2=1-Math.pow(1-k2,3);
        o.setAttribute('x',120+gw); o.setAttribute('width',ow*e2);
        if(k2<1)requestAnimationFrame(frame2);
        else{pipePaint(s,ov);br.forEach(function(el,i){later(function(){el.style.transition='.4s';el.style.opacity=1;},i*220);});}
      }
      requestAnimationFrame(frame2);
    } else requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
};

/* нагрузка: два индикатора */
SCEN.load=function(s,rm){
  var a=q(s,'#loadA>i'), b=q(s,'#loadB>i');
  var li=qa(s,'.loadlist li');
  if(a)a.style.width='0'; if(b)b.style.width='0';
  li.forEach(function(e){e.style.opacity=0;});
  later(function(){if(a)a.style.width='92%';if(b)b.style.width='31%';},rm?0:220);
  li.forEach(function(e,i){later(function(){e.style.transition='.35s';e.style.opacity=1;},rm?0:600+i*170);});
};

/* кадр Ethernet */
SCEN.frame=function(s,rm){
  var f=qa(s,'.fld'), ov=q(s,'#ovShare');
  f.forEach(function(e){e.style.opacity=0;e.style.transform='translateY(10px)';});
  if(ov)ov.style.opacity=0;
  f.forEach(function(e,i){
    later(function(){e.style.transition='.35s cubic-bezier(.22,.7,.3,1)';e.style.opacity=1;e.style.transform='none';},rm?0:i*230);
  });
  later(function(){
    f.forEach(function(e){if(e.dataset.k==='srv')e.style.opacity=.26;});
    if(ov){ov.style.transition='.5s';ov.style.opacity=1;}
  },rm?0:f.length*230+700);
};

/* повторы TCP */
SCEN.tcp=function(s,rm){
  var seg=q(s,'#tSeg'), ack=q(s,'#tAck'), re=q(s,'#tRe'), to=q(s,'#tTo'), cnt=q(s,'#tCnt');
  [seg,ack,re,to].forEach(function(e){if(e)e.style.opacity=0;});
  if(cnt)cnt.textContent='0';
  var o=[[seg,0],[ack,900],[to,1700],[re,2500]];
  o.forEach(function(p){later(function(){if(p[0]){p[0].style.transition='.45s';p[0].style.opacity=1;}},rm?0:p[1]);});
  later(function(){
    if(!cnt)return;
    var n=0, id=setInterval(function(){n+=4;cnt.textContent=n;if(n>=48)clearInterval(id);},40);
    scenTimers.push(id);
  },rm?0:2900);
};

/* доступность: подстановка значений */
SCEN.avail=function(s,rm){
  var st=qa(s,'.astep');
  st.forEach(function(e){e.style.opacity=0;e.style.transform='translateY(8px)';});
  st.forEach(function(e,i){later(function(){e.style.transition='.4s cubic-bezier(.22,.7,.3,1)';e.style.opacity=1;e.style.transform='none';},rm?0:i*600);});
};
SCEN.scales=function(s,rm){
  var b=qa(s,'.bar>i');
  b.forEach(function(e){e.style.width='0';});
  b.forEach(function(e,i){later(function(){e.style.width=e.dataset.w;},rm?0:200+i*300);});
};

/* SPOF */
SCEN.spof=function(s,rm){
  var dead=qa(s,'.dead'), dom=q(s,'#domain'), cas=qa(s,'.casc');
  dead.forEach(function(e){e.style.opacity=0;});
  cas.forEach(function(e){e.style.opacity=0;});
  if(dom)dom.style.opacity=0;
  later(function(){var e=q(s,'.dead[data-o="1"]');if(e){e.style.transition='.4s';e.style.opacity=1;}},rm?0:300);
  later(function(){dead.forEach(function(e){if(e.dataset.o!=='1'){e.style.transition='.4s';e.style.opacity=1;}});},rm?0:1100);
  later(function(){if(dom){dom.style.transition='.6s';dom.style.opacity=1;}},rm?0:1800);
  cas.forEach(function(e,i){later(function(){e.style.transition='.4s';e.style.opacity=1;},rm?0:2300+i*450);});
};

/* угрозы и затраты — простое накопление */
SCEN.sum=function(s,rm){
  var it=qa(s,'.sumit'), tot=qa(s,'.sumtot');
  it.forEach(function(e){e.style.opacity=0;e.style.transform='translateX(-8px)';});
  tot.forEach(function(e){e.style.opacity=0;});
  it.forEach(function(e,i){later(function(){e.style.transition='.35s cubic-bezier(.22,.7,.3,1)';e.style.opacity=1;e.style.transform='none';},rm?0:i*260);});
  tot.forEach(function(e,i){later(function(){e.style.transition='.45s';e.style.opacity=1;},rm?0:it.length*260+300+i*300);});
};

/* ================= ИНТЕРАКТИВ ================= */

/* калькулятор доступности */
(function(){
  var inp=document.getElementById('dt'), un=document.getElementById('dtu'),
      out=document.getElementById('aOut'), cls=document.getElementById('aCls'),
      note=document.getElementById('aNote');
  if(!inp)return;
  var K={min:1/60, h:1, d:24};
  var CLS=[
    [99.999,'Центры обработки данных — 99,999 % (≈5,3 минуты простоя в год)'],
    [99.995,'Финансовые организации, биржи — от 99,995 %'],
    [99.99 ,'Корпоративные сети — 99,99 % (≈53 минуты в год)'],
    [95    ,'Удалённая работа из дома — от 95 %'],
    [90    ,'Малый бизнес — от 90 %'],
    [80    ,'Домашняя сеть, развлечения — от 80 %'],
    [0     ,'Ниже 80 % — неприемлемо почти для любых задач']
  ];
  function calc(){
    var v=parseFloat(inp.value); if(isNaN(v)||v<0)v=0;
    var tot=24*365, dn=v*K[un.value];
    if(dn>tot)dn=tot;
    var a=(tot-dn)/tot*100;
    out.textContent=a.toFixed(a>=99.99?4:2).replace('.',',')+' %';
    var row=CLS.find(function(r){return a+0.0005>=r[0];});
    cls.textContent=row[1];
    note.textContent='Простой '+dn.toFixed(2).replace('.',',')+' ч из '+tot+' ч периода.';
  }
  inp.addEventListener('input',calc);
  un.addEventListener('change',calc);
  [inp,un].forEach(function(e){e.addEventListener('keydown',function(ev){ev.stopPropagation();});});
  calc();
})();

/* ползунок overhead */
(function(){
  var sl=document.getElementById('ovr'); if(!sl)return;
  var vO=document.getElementById('vO'), vG=document.getElementById('vG'), vP=document.getElementById('vP');
  var g=document.getElementById('mpG'), o=document.getElementById('mpO'),
      lg=document.getElementById('mlG'), lo=document.getElementById('mlO');
  function upd(){
    var p=+sl.value, T=1000, O=T*p/100, G=T-O;
    vP.textContent=p+' %';
    vO.textContent=O.toFixed(0)+' Мбит/с';
    vG.textContent=G.toFixed(0)+' Мбит/с';
    var W=560, x0=20, ow=W*p/100, gw=W-ow;
    if(g){g.setAttribute('width',gw);}
    if(o){o.setAttribute('x',x0+gw);o.setAttribute('width',ow);}
    if(lg){lg.setAttribute('x',x0+gw/2);lg.textContent='G — '+G.toFixed(0)+' Мбит/с';}
    if(lo){lo.setAttribute('x',x0+gw+ow/2);lo.setAttribute('opacity',p<6?0:1);
           lo.textContent='O — '+O.toFixed(0);}
  }
  sl.addEventListener('input',upd);
  sl.addEventListener('keydown',function(e){e.stopPropagation();});
  upd();
})();

/* проверь себя */
(function(){
  var done={}, sc=document.getElementById('score');
  var qs=[].slice.call(document.querySelectorAll('.q'));
  qs.forEach(function(qq,qi){
    var bs=[].slice.call(qq.querySelectorAll('.opts button'));
    bs.forEach(function(b){
      b.onclick=function(){
        if(done[qi]!==undefined)return;
        done[qi]=(b.dataset.a==='1');
        bs.forEach(function(x){
          if(x.dataset.a==='1')x.classList.add('good');
          else if(x===b)x.classList.add('bad');
        });
        var ex=qq.querySelector('.ex'); if(ex)ex.classList.add('on');
        if(sc){
          var ok=Object.keys(done).filter(function(k){return done[k];}).length;
          sc.textContent=ok+' / '+qs.length+'  (отвечено '+Object.keys(done).length+')';
        }
      };
    });
  });
  var rb=document.getElementById('qreset');
  if(rb)rb.onclick=function(){
    done={};
    qs.forEach(function(qq){
      qq.querySelectorAll('.opts button').forEach(function(x){x.classList.remove('good','bad');});
      var ex=qq.querySelector('.ex'); if(ex)ex.classList.remove('on');
    });
    if(sc)sc.textContent='0 / '+qs.length;
  };
  if(sc)sc.textContent='0 / '+qs.length;
})();

/* длины путей для stroke-dashoffset */
[].forEach.call(document.querySelectorAll('.dash'),function(p){
  try{var L=p.getTotalLength();p.style.setProperty('--L',Math.ceil(L));}catch(e){p.style.setProperty('--L','600');}
});

show(0);
})();
"""
