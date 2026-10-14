# -*- coding: utf-8 -*-
"""Движок деки OSPF: шаги, навигация, сценарии, тренажёры Дейкстры и стоимости, тест."""

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

/* ---------- сценарии ---------- */
var SCEN={}, T=[];
function later(fn,ms){var id=setTimeout(fn,ms/speed);T.push(id);return id;}
function clearScen(){T.forEach(function(t){clearTimeout(t);clearInterval(t);});T=[];}
function resetScen(s){
  qa(s,'.go').forEach(function(e){if(!e.dataset.keep)e.classList.remove('go');});
  qa(s,'.dim').forEach(function(e){e.classList.remove('dim');});
}
function runScen(){
  var s=slides[cur];
  clearScen(); resetScen(s);
  qa(s,'[data-at]').forEach(function(e){
    var ms=parseInt(e.dataset.at,10)||0;
    if(reduce){e.classList.add('go');return;}
    later(function(){e.classList.add('go');},ms);
  });
  var k=s.dataset.scen;
  if(k&&SCEN[k])SCEN[k](s,reduce);
}

function paint(){
  var st=stepsOf(cur);
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
  step=(openAll||reduce)?stepsOf(cur).length:0;
  paint(); runScen();
  if(!reduce&&!openAll) run();
}
function run(){
  stop();
  var total=stepsOf(cur).length;
  if(step>=total)return;
  timer=setInterval(function(){
    if(step>=total){stop();return;}
    step++;paint();
  },620/speed);
}
function stop(){if(timer){clearInterval(timer);timer=null;}}
function next(){stop();if(step<stepsOf(cur).length){step++;paint();}else if(cur<slides.length-1)show(cur+1);}
function prev(){stop();if(step>0){step--;paint();}else if(cur>0)show(cur-1,true);}
function replay(){stop();step=0;paint();runScen();if(!reduce)run();}

/* ---------- содержание ---------- */
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
});

/* ---------- колесо и свайп ---------- */
var lock=0;
window.addEventListener('wheel',function(e){
  if(toc.classList.contains('on'))return;
  var box=e.target.closest?e.target.closest('.sc,.tw,.cli'):null;
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

/* последовательная подсветка элементов по классу .seq с шагом data-gap */
function seq(s,sel,gap,rm,cb){
  var el=qa(s,sel); el.forEach(function(e){e.classList.remove('go');});
  if(rm){el.forEach(function(e){e.classList.add('go');});if(cb)cb();return;}
  el.forEach(function(e,i){later(function(){e.classList.add('go');if(cb&&i===el.length-1)cb();},300+i*gap);});
}

/* 1. Состояния соседства: карточки слева направо + мини-сцена внутри */
SCEN.nbr=function(s,rm){ seq(s,'.nbrc',760,rm); };

/* 2. Стоимость: метки на линках, потом слагаемые суммы */
SCEN.cost=function(s,rm){
  var marks=qa(s,'.cmk'), terms=qa(s,'.cterm'), tot=q(s,'.ctot');
  marks.concat(terms).forEach(function(e){e.classList.remove('go');});
  if(tot)tot.classList.remove('go');
  if(rm){marks.concat(terms).forEach(function(e){e.classList.add('go');});if(tot)tot.classList.add('go');return;}
  marks.forEach(function(e,i){later(function(){e.classList.add('go');},300+i*480);});
  var base=300+marks.length*480+300;
  terms.forEach(function(e,i){later(function(){e.classList.add('go');},base+i*520);});
  later(function(){if(tot)tot.classList.add('go');},base+terms.length*520+260);
};

/* 3. Преимущества LS: рвётся канал, LSP расходятся по области 1 */
SCEN.lspros=function(s,rm){
  var cut=q(s,'.lcut'), waves=qa(s,'.lwave'), calm=q(s,'.lcalm');
  [cut,calm].forEach(function(e){if(e)e.classList.remove('go');});
  waves.forEach(function(e){e.classList.remove('go');});
  if(rm){if(cut)cut.classList.add('go');waves.forEach(function(e){e.classList.add('go');});
         if(calm)calm.classList.add('go');return;}
  later(function(){if(cut)cut.classList.add('go');},500);
  waves.forEach(function(e,i){later(function(){e.classList.add('go');},1100+i*420);});
  later(function(){if(calm)calm.classList.add('go');},1100+waves.length*420+500);
};

/* 4. LSA: 4 шага — формирование, LSU, LSDB, SPF */
SCEN.lsaflow=function(s,rm){ seq(s,'.lstep',900,rm); };

/* 5. Типы маршрутизаторов: роли по очереди */
SCEN.roles=function(s,rm){ seq(s,'.role',700,rm); };

/* 6. Области и LSA: переключатель типа области гасит непроходящие LSA */
SCEN.areasw=function(s,rm){
  var root=q(s,'.areasw'); if(!root)return;
  var btns=qa(root,'.ui button');
  var RULES={
    std:    {on:['l1','l2','l3','l4','l5'],  off:['l7','def'],
             note:'Обычная область получает всё: свою топологию (LSA-1/2), межобластные маршруты (LSA-3), путь к ASBR (LSA-4) и внешние маршруты (LSA-5).'},
    stub:   {on:['l1','l2','l3','def'],      off:['l4','l5','l7'],
             note:'Stub не принимает LSA-5 и LSA-4. Вместо внешних маршрутов ABR объявляет маршрут по умолчанию 0.0.0.0/0 через LSA-3.'},
    tstub:  {on:['l1','l2','def'],           off:['l3','l4','l5','l7'],
             note:'Totally Stubby отсекает ещё и подробные межобластные LSA-3. Внутри остаётся своя топология и один маршрут по умолчанию.'},
    nssa:   {on:['l1','l2','l3','l7','def'], off:['l4','l5'],
             note:'NSSA не принимает внешние LSA-5, но свой ASBR может вводить внешние маршруты через LSA-7. ABR может превратить подходящий LSA-7 в LSA-5.'},
    tnssa:  {on:['l1','l2','l7','def'],      off:['l3','l4','l5'],
             note:'Totally NSSA скрывает и подробные межобластные маршруты: остаются своя топология, локальные LSA-7 и маршрут по умолчанию.'}
  };
  function apply(k){
    var r=RULES[k]; if(!r)return;
    qa(root,'.lsabox').forEach(function(e){
      var on=r.on.indexOf(e.dataset.lsa)>=0;
      e.classList.toggle('dim',!on);
      var b=q(e,'.ban'); if(b)b.style.opacity=on?0:1;
    });
    var n=q(root,'.note'); if(n)n.textContent=r.note;
    btns.forEach(function(b){b.classList.toggle('pri',b.dataset.k===k);});
  }
  btns.forEach(function(b){b.onclick=function(){apply(b.dataset.k);};});
  apply(root.dataset.start||'std');
};

/* 7. Дейкстра: шаг по графу — текущая вершина, рёбра, пересчёт меток */
SCEN.dij=function(s,rm){
  var hal=q(s,'.dhalo'), edges=qa(s,'.dedge'), calcs=qa(s,'.dcalc'),
      lbls=qa(s,'.dlabel'), rows=qa(s,'.drow'), fin=q(s,'.dfin');
  [hal,fin].forEach(function(e){if(e)e.classList.remove('go');});
  edges.concat(calcs,lbls,rows).forEach(function(e){e.classList.remove('go');});
  if(rm){[hal,fin].forEach(function(e){if(e)e.classList.add('go');});
         edges.concat(calcs,lbls,rows).forEach(function(e){e.classList.add('go');});return;}
  later(function(){if(hal)hal.classList.add('go');},350);
  var t=900;
  edges.forEach(function(e,i){
    later(function(){e.classList.add('go');},t+i*760);
    if(calcs[i])later(function(){calcs[i].classList.add('go');},t+i*760+320);
    if(lbls[i])later(function(){lbls[i].classList.add('go');},t+i*760+560);
    if(rows[i])later(function(){rows[i].classList.add('go');},t+i*760+600);
  });
  later(function(){if(fin)fin.classList.add('go');},t+edges.length*760+420);
};

/* 8. Дерево SPF: прорастают рёбра, отброшенные бледнеют */
SCEN.spf=function(s,rm){
  var grow=qa(s,'.sgrow'), drop=qa(s,'.sdrop'), nodes=qa(s,'.snode');
  grow.concat(nodes).forEach(function(e){e.classList.remove('go');});
  drop.forEach(function(e){e.classList.remove('dim');});
  if(rm){grow.concat(nodes).forEach(function(e){e.classList.add('go');});
         drop.forEach(function(e){e.classList.add('dim');});return;}
  grow.forEach(function(e,i){later(function(){e.classList.add('go');},400+i*620);});
  nodes.forEach(function(e,i){later(function(){e.classList.add('go');},700+i*620);});
  later(function(){drop.forEach(function(e){e.classList.add('dim');});},400+grow.length*620+320);
};

/* 9. Печать команд */
SCEN.type=function(s,rm){
  var pre=q(s,'[data-type]');
  if(!pre)return;
  var full=pre.dataset.type;
  if(rm){pre.innerHTML=full;return;}
  var raw=full.replace(/<[^>]+>/g,'').replace(/&quot;/g,'"').replace(/&amp;/g,'&');
  pre.textContent='';
  var i=0;
  var iv=setInterval(function(){
    if(slides[cur]!==s){clearInterval(iv);return;}
    i+=2; pre.textContent=raw.slice(0,i);
    if(i>=raw.length){clearInterval(iv);pre.innerHTML=full+'<span class="cur"></span>';}
  },26/speed);
  T.push(iv);
};

/* 10. Поток пакетов: Hello → DBD → LSR → LSU → LSAck */
SCEN.pkt=function(s,rm){ seq(s,'.pstep',820,rm); };

/* 11. Выбор DR/BDR: сравнение приоритетов, затем Router ID */
SCEN.drbdr=function(s,rm){ seq(s,'.dstep',900,rm); };

/* ===================== ТРЕНАЖЁР ДЕЙКСТРЫ ===================== */
(function(){
  var root=document.getElementById('dijsim');
  if(!root)return;
  var N=['R1','R2','R3','R4','R5'];
  /* координаты вершин на схеме 1000x430 */
  var POS=[[150,110],[150,330],[500,215],[850,330],[850,110]];
  /* рёбра как в методичке: R1-R2 8, R1-R3 10, R1-R5 15, R2-R3 11, R2-R4 16, R3-R4 12, R3-R5 3, R4-R5 16 */
  var BASE=[[0,1,8],[0,2,10],[0,4,15],[1,2,11],[1,3,16],[2,3,12],[2,4,3],[3,4,16]];
  var E=BASE.map(function(e){return e.slice();});
  var INF=Infinity;
  var dist=[],vis=[],prev=[],picked=0,done=false;

  function rnd(){
    E=BASE.map(function(e){return [e[0],e[1],1+Math.floor(Math.random()*20)];});
    reset();
  }
  function reset(){
    dist=N.map(function(_,i){return i===0?0:INF;});
    vis=N.map(function(){return false;});
    prev=N.map(function(){return null;});
    picked=0; done=false;
    draw(); note('Стартуем из R1: его метка 0, у остальных ∞. Выберите вершину с наименьшей меткой среди непосещённых.');
  }
  function note(t){q(root,'#dnote').innerHTML=t;}
  function fmt(v){return v===INF?'∞':v;}
  function minUnvisited(){
    var best=-1;
    for(var i=0;i<N.length;i++){if(!vis[i]&&dist[i]<INF&&(best<0||dist[i]<dist[best]))best=i;}
    return best;
  }
  function neigh(i){
    var out=[];
    E.forEach(function(e){
      if(e[0]===i)out.push([e[1],e[2]]);
      else if(e[1]===i)out.push([e[0],e[2]]);
    });
    return out;
  }
  function pick(i){
    if(done)return;
    if(vis[i]){note('Вершина <b>'+N[i]+'</b> уже посещена. Её метка больше не меняется — выберите другую.');return;}
    if(dist[i]===INF){note('До <b>'+N[i]+'</b> пока нет известного пути: её метка ∞. Сначала нужно пройти вершину, из которой до неё есть ребро.');return;}
    var best=minUnvisited();
    if(i!==best){
      note('Нельзя: у <b>'+N[i]+'</b> метка '+fmt(dist[i])+', а у <b>'+N[best]+'</b> — '+fmt(dist[best])+
           '. Дейкстра всегда берёт <b>минимальную</b> метку среди непосещённых: только для неё путь уже гарантированно кратчайший.');
      return;
    }
    /* релаксация */
    var log=[];
    neigh(i).forEach(function(nb){
      var j=nb[0], w=nb[1];
      if(vis[j]){log.push(N[j]+' — посещена, пропускаем');return;}
      var cand=dist[i]+w;
      if(cand<dist[j]){
        log.push('<b>'+N[j]+'</b>: '+dist[i]+' + '+w+' = <b>'+cand+'</b> &lt; '+fmt(dist[j])+' → обновляем на '+cand);
        dist[j]=cand; prev[j]=i;
      }else{
        log.push('<b>'+N[j]+'</b>: '+dist[i]+' + '+w+' = '+cand+' ≥ '+fmt(dist[j])+' → оставляем '+fmt(dist[j]));
      }
    });
    vis[i]=true; picked++;
    draw();
    var left=N.some(function(_,k){return !vis[k]&&dist[k]<INF;});
    if(!left){
      done=true;
      note('Шаг '+picked+' — <b>'+N[i]+'</b> помечена посещённой.<br>'+log.join('<br>')+
           '<br><br>Все достижимые вершины посещены. Итог: '+
           N.map(function(n,k){return n+' = '+fmt(dist[k]);}).join(', ')+'.');
    }else{
      note('Шаг '+picked+' — <b>'+N[i]+'</b> помечена посещённой.<br>'+log.join('<br>'));
    }
  }
  function draw(){
    var svg=q(root,'#dsvg'), out=[];
    var best=done?-1:minUnvisited();
    E.forEach(function(e){
      var a=POS[e[0]], b=POS[e[1]];
      var tree=(prev[e[1]]===e[0]||prev[e[0]]===e[1]);
      out.push('<path d="M'+a[0]+' '+a[1]+'L'+b[0]+' '+b[1]+'" stroke="'+(tree?'#ffd93d':'#c7d6e4')+
               '" stroke-width="'+(tree?8:5)+'" stroke-linecap="round"/>');
      var mx=(a[0]+b[0])/2, my=(a[1]+b[1])/2;
      out.push('<circle cx="'+mx+'" cy="'+my+'" r="17" fill="#fff" stroke="#c7d6e4" stroke-width="2"/>');
      out.push('<text x="'+mx+'" y="'+(my+5)+'" text-anchor="middle" font-size="14" font-weight="800" fill="#121212">'+e[2]+'</text>');
    });
    POS.forEach(function(p,i){
      var st=vis[i]?'#3fc47c':(i===best?'#ffd93d':(dist[i]===INF?'#eef2f6':'#ffd3e4'));
      var ink=vis[i]?'#fff':'#121212';
      out.push('<g class="dvx" data-i="'+i+'" style="cursor:pointer">');
      out.push('<circle cx="'+p[0]+'" cy="'+p[1]+'" r="36" fill="'+st+'" stroke="#121212" stroke-width="3"/>');
      out.push('<text x="'+p[0]+'" y="'+(p[1]-4)+'" text-anchor="middle" font-size="17" font-weight="900" fill="'+ink+'">'+N[i]+'</text>');
      out.push('<text x="'+p[0]+'" y="'+(p[1]+16)+'" text-anchor="middle" font-size="15" font-weight="800" fill="'+ink+'">'+fmt(dist[i])+'</text>');
      out.push('</g>');
    });
    svg.innerHTML=out.join('');
    qa(svg,'.dvx').forEach(function(gel){
      gel.onclick=function(){pick(parseInt(gel.dataset.i,10));};
    });
    var tb=q(root,'#dtab'); tb.innerHTML='';
    N.forEach(function(n,i){
      var d=document.createElement('div');
      d.className='rw'+(vis[i]?' done':'')+((!done&&i===best)?' upd':'');
      d.innerHTML='<span><b>'+n+'</b></span><span>метка '+fmt(dist[i])+'</span><span>'+
                  (vis[i]?'посещена':(i===best?'следующая':'не посещена'))+
                  (prev[i]!==null?' · через '+N[prev[i]]:'')+'</span>';
      tb.appendChild(d);
    });
    q(root,'#dcnt').textContent=picked;
  }
  q(root,'#dreset').onclick=reset;
  q(root,'#drnd').onclick=rnd;
  q(root,'#dauto').onclick=function(){
    if(done)return;
    var b=minUnvisited(); if(b>=0)pick(b);
  };
  reset();
})();

/* ===================== ТРЕНАЖЁР СТОИМОСТИ ===================== */
(function(){
  var root=document.getElementById('costsim');
  if(!root)return;
  var REF=100; /* Мбит/с — эталон */
  var SPEEDS=[[10,'10 Мбит/с'],[100,'100 Мбит/с'],[1000,'1 Гбит/с'],[64/1000,'64 кбит/с'],
              [2,'2 Мбит/с'],[155,'155 Мбит/с'],[10000,'10 Гбит/с'],[1.544,'1,544 Мбит/с (T1)']];
  var task=null, score=0, total=0;

  function costOf(mbps){var c=Math.floor(REF/mbps);return c<1?1:c;}
  function gen(){
    var n=2+Math.floor(Math.random()*3);     /* 2..4 интерфейса на пути */
    var hops=[];
    for(var i=0;i<n;i++){hops.push(SPEEDS[Math.floor(Math.random()*SPEEDS.length)]);}
    task={hops:hops,sum:hops.reduce(function(a,h){return a+costOf(h[0]);},0)};
    render();
  }
  function render(){
    var box=q(root,'#cshop'); box.innerHTML='';
    task.hops.forEach(function(h,i){
      var d=document.createElement('div');
      d.className='rw';
      d.innerHTML='<span>Интерфейс '+(i+1)+'</span><span class="kv">'+h[1]+'</span>'+
                  '<span class="kv chv" data-i="'+i+'">cost = ?</span>';
      box.appendChild(d);
    });
    q(root,'#csin').value='';
    q(root,'#csnote').innerHTML='Посчитайте стоимость каждого интерфейса по формуле <b>cost = 100 Мбит/с ÷ пропускная способность</b> (дробь округляется вниз, минимум 1) и введите сумму по всему пути.';
    q(root,'#csin').focus();
  }
  function check(){
    var v=parseInt(q(root,'#csin').value,10);
    if(isNaN(v)){q(root,'#csnote').textContent='Введите число.';return;}
    total++;
    var parts=task.hops.map(function(h){return costOf(h[0]);});
    qa(root,'.chv').forEach(function(e,i){e.textContent='cost = '+parts[i];});
    if(v===task.sum){
      score++;
      q(root,'#csnote').innerHTML='<b style="color:#1d8a51">Верно.</b> '+parts.join(' + ')+' = <b>'+task.sum+'</b>.';
    }else{
      q(root,'#csnote').innerHTML='<b style="color:#d8276f">Не сходится.</b> Правильно: '+
        task.hops.map(function(h,i){return '100 ÷ '+h[1].replace(/ .*/,'')+' → '+parts[i];}).join(', ')+
        '. Сумма '+parts.join(' + ')+' = <b>'+task.sum+'</b>, а не '+v+'.';
    }
    q(root,'#csscore').textContent=score+' / '+total;
  }
  q(root,'#csnew').onclick=gen;
  q(root,'#cscheck').onclick=check;
  q(root,'#csin').addEventListener('keydown',function(e){if(e.key==='Enter'){check();e.preventDefault();}});
  gen();
})();

/* ===================== ТРЕНАЖЁР ТИПА ОБЛАСТИ ===================== */
(function(){
  var root=document.getElementById('areasim');
  if(!root)return;
  var CASES=[
    {t:'В филиале нет своих внешних маршрутов, нужны подробные маршруты из других областей, но внешние LSA-5 не нужны.',a:'stub'},
    {t:'В филиале нет своих внешних маршрутов, и ему достаточно одного маршрута по умолчанию вместо всех чужих маршрутов.',a:'tstub'},
    {t:'В филиале стоит свой ASBR с каналом к провайдеру, но внешние маршруты остальной сети туда пускать не хотят.',a:'nssa'},
    {t:'В филиале есть свой ASBR, и при этом подробные межобластные маршруты туда тоже решили не передавать.',a:'tnssa'},
    {t:'Центральная площадка, через которую идёт вся межобластная маршрутизация.',a:'backbone'},
    {t:'Область, которой нужны и межобластные, и внешние маршруты OSPF без ограничений.',a:'std'}
  ];
  var LAB={backbone:'Backbone (Area 0)',std:'Standard',stub:'Stub',tstub:'Totally Stubby',
           nssa:'NSSA',tnssa:'Totally NSSA'};
  var i=0,score=0,total=0,answered=false;
  function render(){
    answered=false;
    q(root,'#astask').textContent=CASES[i].t;
    qa(root,'.abtn').forEach(function(b){b.className='vbtn abtn';b.disabled=false;});
    q(root,'#asnote').textContent='';
    q(root,'#asnum').textContent=(i+1)+' / '+CASES.length;
  }
  qa(root,'.abtn').forEach(function(b){
    b.onclick=function(){
      if(answered)return; answered=true; total++;
      var ok=b.dataset.k===CASES[i].a;
      b.classList.add(ok?'good':'bad');
      if(!ok)qa(root,'.abtn').forEach(function(o){if(o.dataset.k===CASES[i].a)o.classList.add('good');});
      if(ok)score++;
      q(root,'#asnote').innerHTML=(ok?'<b style="color:#1d8a51">Верно.</b> ':'<b style="color:#d8276f">Нет.</b> ')+
        'Подходит <b>'+LAB[CASES[i].a]+'</b>.';
      q(root,'#asscore').textContent=score+' / '+total;
      qa(root,'.abtn').forEach(function(o){o.disabled=true;});
    };
  });
  q(root,'#asnext').onclick=function(){i=(i+1)%CASES.length;render();};
  render();
})();

/* ===================== ТЕСТ ===================== */
(function(){
  var all=qa(document,'.q');
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
        qa(document,'.score').forEach(function(sc){sc.textContent=right+' / '+total+'  (отвечено '+done+')';});
      };
    });
  });
})();

show(0);
})();
"""
