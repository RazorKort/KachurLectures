# -*- coding: utf-8 -*-
"""Движок практики по OSI: раскрытие при скролле, сцены-анимации, задания."""

JS = r"""
(function(){
'use strict';
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;

/* ======================= прогресс + навигация ======================= */
var prog=document.getElementById('prog');
var secs=[].slice.call(document.querySelectorAll('section.sc'));
var links=[].slice.call(document.querySelectorAll('#nav a'));
function onScroll(){
  var h=document.documentElement;
  var max=h.scrollHeight-h.clientHeight;
  prog.style.width=(max>0?(h.scrollTop||document.body.scrollTop)/max*100:0)+'%';
  var y=(h.scrollTop||document.body.scrollTop)+140, act=secs[0];
  secs.forEach(function(s){ if(s.offsetTop<=y) act=s; });
  links.forEach(function(a){ a.classList.toggle('on', a.getAttribute('href')==='#'+act.id); });
}
addEventListener('scroll',onScroll,{passive:true});
addEventListener('resize',onScroll);

/* ======================= раскрытие при скролле ======================= */
var rvs=[].slice.call(document.querySelectorAll('.rv'));
if(reduce||!('IntersectionObserver' in window)){
  rvs.forEach(function(e){e.classList.add('on');});
}else{
  var io=new IntersectionObserver(function(es){
    es.forEach(function(e){
      if(e.isIntersecting){ e.target.classList.add('on'); io.unobserve(e.target); }
    });
  },{rootMargin:'-6% 0px -12% 0px',threshold:0.06});
  rvs.forEach(function(e){io.observe(e);});
}

/* ======================= сцены ======================= */
function Scene(root){
  var self=this;
  this.root=root;
  this.els=[].slice.call(root.querySelectorAll('[data-s]'));
  this.caps=[].slice.call(root.querySelectorAll('.cap .t'));
  this.total=0;
  this.els.concat(this.caps).forEach(function(e){
    var a=(e.dataset.s||'1').split('-');
    e._f=parseInt(a[0],10)||0;
    e._t=a.length>1?(parseInt(a[1],10)||999):999;
    e._exact=(a.length===1);
    if(e._f>self.total) self.total=e._f;
    var p=e.dataset.path;
    if(p){
      e._keys=p.split('|').map(function(k){
        var q=k.split(':'), xy=q[1].split(',');
        return {s:parseInt(q[0],10),x:parseFloat(xy[0]),y:parseFloat(xy[1])};
      });
      e._keys.forEach(function(k){ if(k.s>self.total) self.total=k.s; });
    }
  });
  this.step=0; this.timer=null; this.played=false;
  this.n=root.querySelector('.stepn');
  var b=root.querySelector('[data-act="run"]');
  if(b) b.addEventListener('click',function(){ self.replay(); });
  var bp=root.querySelector('[data-act="prev"]');
  if(bp) bp.addEventListener('click',function(){ self.stop(); self.to(self.step-1); });
  var bn=root.querySelector('[data-act="next"]');
  if(bn) bn.addEventListener('click',function(){ self.stop(); self.to(self.step+1); });
  this.to(0);
}
Scene.prototype.paint=function(){
  var st=this.step;
  this.els.forEach(function(e){
    e.classList.toggle('on', st>=e._f && st<=e._t);
    if(e._keys){
      var k=null;
      for(var i=0;i<e._keys.length;i++) if(st>=e._keys[i].s) k=e._keys[i];
      if(k) e.setAttribute('transform','translate('+k.x+','+k.y+')');
    }
  });
  this.caps.forEach(function(e){
    e.classList.toggle('on', e._exact ? st===e._f : (st>=e._f && st<=e._t));
  });
  if(this.n) this.n.textContent=st+' / '+this.total;
};
Scene.prototype.to=function(s){
  this.step=Math.max(0,Math.min(this.total,s)); this.paint();
};
Scene.prototype.stop=function(){ if(this.timer){clearInterval(this.timer);this.timer=null;} };
Scene.prototype.play=function(){
  var self=this; this.stop();
  if(reduce){ this.to(this.total); return; }
  this.timer=setInterval(function(){
    if(self.step>=self.total){ self.stop(); return; }
    self.to(self.step+1);
  }, parseInt(self.root.dataset.pace||'1100',10));
};
Scene.prototype.replay=function(){ this.stop(); this.to(0); var s=this; setTimeout(function(){s.play();},180); };

var scenes=[].slice.call(document.querySelectorAll('.scene')).map(function(r){return new Scene(r);});
if(!reduce && 'IntersectionObserver' in window){
  var io2=new IntersectionObserver(function(es){
    es.forEach(function(e){
      var sc=e.target._sc;
      if(e.isIntersecting){ if(!sc.played){ sc.played=true; sc.play(); } }
      else sc.stop();
    });
  },{threshold:0.35});
  scenes.forEach(function(s){ s.root._sc=s; io2.observe(s.root); });
}else{
  scenes.forEach(function(s){ s.to(s.total); });
}

/* ======================= задания ======================= */
function norm(v){
  return String(v||'').trim().toLowerCase()
    .replace(/\s+/g,'').replace(/[«»"']/g,'').replace(/ё/g,'е');
}
[].slice.call(document.querySelectorAll('.task')).forEach(function(t){
  var ins=[].slice.call(t.querySelectorAll('input[data-a]'));
  var ver=t.querySelector('.ver'), ans=t.querySelector('.ans');
  var bc=t.querySelector('[data-act="check"]'), ba=t.querySelector('[data-act="show"]');
  if(bc) bc.addEventListener('click',function(){
    var ok=0;
    ins.forEach(function(i){
      var good=i.dataset.a.split('|').some(function(a){return norm(a)===norm(i.value);});
      i.classList.toggle('ok',good); i.classList.toggle('no',!good&&!!i.value.trim());
      if(good) ok++;
    });
    if(ver){ ver.textContent='Верно: '+ok+' из '+ins.length+(ok===ins.length?' — всё сошлось.':' — сравни с разбором.');
      ver.classList.add('on'); }
  });
  if(ba) ba.addEventListener('click',function(){
    if(!ans) return;
    var open=ans.classList.toggle('on');
    ba.textContent=open?'Скрыть разбор':'Показать разбор';
    if(open) ins.forEach(function(i){
      if(!i.value.trim()){ i.value=i.dataset.a.split('|')[0]; i.classList.add('ok'); }
    });
  });
});

/* ======================= подсказки по полям ======================= */
[].slice.call(document.querySelectorAll('.fld[data-tip]')).forEach(function(f){
  f.setAttribute('title', f.dataset.tip);
});

onScroll();
})();
"""
