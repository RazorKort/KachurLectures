# -*- coding: utf-8 -*-
"""Движок деки «Маршрутизаторы» (2.3): шаги, навигация, сценарии анимации, тренажёры, тест."""

JS = r"""
(function(){
'use strict';
var slides=[].slice.call(document.querySelectorAll('.slide'));
var cur=0, step=0, timer=null, speed=1;
var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
var elCount=document.getElementById('count'), elName=document.getElementById('sname'),
    elProg=document.getElementById('prog'), toc=document.getElementById('toc');

function qa(root,sel){return [].slice.call(root.querySelectorAll(sel));}

/* обёртка .wrap внутри каждого .sc — нужна для автоподгонки масштаба */
[].slice.call(document.querySelectorAll('.slide>.sc')).forEach(function(sc){
  var w=document.createElement('div'); w.className='wrap';
  while(sc.firstChild)w.appendChild(sc.firstChild);
  sc.appendChild(w);
});
/* автоподгонка: контент растягивается на всю высоту слайда (0.7…1.7) */
function fit(s){
  var sc=s.querySelector('.sc'), w=sc&&sc.querySelector('.wrap'); if(!w)return;
  w.style.zoom=''; w.style.width='';
  if(window.innerWidth<900||s.classList.contains('cover-slide'))return;
  var H=sc.clientHeight, z=1;
  function nat(){var m=w.style.minHeight;w.style.minHeight='0';w.style.flex='none';
    var C=w.scrollHeight;w.style.minHeight=m;w.style.flex='';return C;}
  function apply(v){z=v;w.style.zoom=v.toFixed(3);}
  for(var i=0;i<6;i++){
    var C=nat(); if(C<40)return;
    var z2=Math.max(.7,Math.min(1.7,H/C*.985));
    if(Math.abs(z2-z)<.01)break;
    apply(z2);
  }
  for(var j=0;j<3;j++){
    var C3=nat(); if(C3*z<=H+4||z<=.701)break;
    apply(Math.max(.7,z*(H/(C3*z))*.99));
  }
}
window.addEventListener('resize',function(){clearTimeout(window.__rz);
  window.__rz=setTimeout(function(){fit(slides[cur]);},120);});
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
  fit(slides[cur]);
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
  },640/speed);
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
  if(inField(e)&&e.key!=='Escape')return;
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

/* ---------- свайп (колесо слайды не листает — только прокрутка) ---------- */
var tx=0,ty=0;
window.addEventListener('touchstart',function(e){tx=e.touches[0].clientX;ty=e.touches[0].clientY;},{passive:true});
window.addEventListener('touchend',function(e){
  var dx=e.changedTouches[0].clientX-tx, dy=e.changedTouches[0].clientY-ty;
  if(Math.abs(dx)>60&&Math.abs(dx)>Math.abs(dy)){dx<0?next():prev();}
},{passive:true});

qa(document,'[data-go]').forEach(function(b){
  b.addEventListener('click',function(){
    var k=b.dataset.go;
    for(var i=0;i<slides.length;i++){if(slides[i].dataset.label===k){show(i);return;}}
  });
});
document.getElementById('bprev').onclick=prev;
document.getElementById('bnext').onclick=next;
document.getElementById('btoc').onclick=function(){toc.classList.toggle('on');};
document.getElementById('brun').onclick=replay;
document.getElementById('bspeed').onclick=function(){
  speed=speed===1?2:(speed===2?0.5:1);
  this.textContent=speed+'×';
};

/* ===================== СЦЕНАРИИ ===================== */
function seq(s,sel,gap,rm,cb){
  var el=qa(s,sel); el.forEach(function(e){e.classList.remove('go');});
  if(rm){el.forEach(function(e){e.classList.add('go');});if(cb)cb();return;}
  el.forEach(function(e,i){later(function(){e.classList.add('go');if(cb&&i===el.length-1)cb();},300+i*gap);});
}

/* универсальная последовательность по классу .sq с индивидуальным шагом */
SCEN.sq   =function(s,rm){ seq(s,'.sq',760,rm); };
SCEN.sqf  =function(s,rm){ seq(s,'.sq',480,rm); };
SCEN.sqs  =function(s,rm){ seq(s,'.sq',1050,rm); };

/* путь пакета: линии, затем пакет-метки, затем вывод */
SCEN.path=function(s,rm){
  var seg=qa(s,'.pseg'), pk=qa(s,'.ppk'), fin=q(s,'.pfin');
  seg.concat(pk).forEach(function(e){e.classList.remove('go');});
  if(fin)fin.classList.remove('go');
  if(rm){seg.concat(pk).forEach(function(e){e.classList.add('go');});if(fin)fin.classList.add('go');return;}
  var t=350;
  seg.forEach(function(e,i){
    later(function(){e.classList.add('go');},t+i*700);
    if(pk[i])later(function(){pk[i].classList.add('go');},t+i*700+340);
  });
  later(function(){if(fin)fin.classList.add('go');},t+seg.length*700+300);
};

/* печать команд в терминале */
SCEN.type=function(s,rm){
  var pre=q(s,'[data-type]');
  if(!pre)return;
  var full=pre.dataset.type;
  if(rm){pre.innerHTML=full;return;}
  var raw=full.replace(/<[^>]+>/g,'').replace(/&quot;/g,'"').replace(/&lt;/g,'<')
              .replace(/&gt;/g,'>').replace(/&amp;/g,'&');
  pre.textContent='';
  var i=0;
  var iv=setInterval(function(){
    if(slides[cur]!==s){clearInterval(iv);return;}
    i+=3; pre.textContent=raw.slice(0,i);
    if(i>=raw.length){clearInterval(iv);pre.innerHTML=full+'<span class="cur"></span>';}
  },24/speed);
  T.push(iv);
};

/* TTL-трассировка: hop за hop, TTL падает, приходит Time Exceeded */
SCEN.ttl=function(s,rm){
  var hops=qa(s,'.thop'), rows=qa(s,'.trow');
  hops.concat(rows).forEach(function(e){e.classList.remove('go');});
  if(rm){hops.concat(rows).forEach(function(e){e.classList.add('go');});return;}
  hops.forEach(function(e,i){
    later(function(){e.classList.add('go');},300+i*900);
    if(rows[i])later(function(){rows[i].classList.add('go');},300+i*900+500);
  });
};

/* ping: эхо-запрос туда, эхо-ответ обратно, затем статистика */
SCEN.ping=function(s,rm){ seq(s,'.sq',820,rm); };

/* переключаемая схема (кнопки .swbtn + блоки .swbox[data-k]) */
SCEN.sw=function(s,rm){
  var root=q(s,'.swroot'); if(!root)return;
  var btns=qa(root,'.swbtn');
  function apply(k){
    qa(root,'.swbox').forEach(function(e){e.style.display=(e.dataset.k===k)?'':'none';});
    btns.forEach(function(b){b.classList.toggle('pri',b.dataset.k===k);});
    var n=q(root,'.note');
    var src=q(root,'.swbox[data-k="'+k+'"]');
    if(n&&src&&src.dataset.note)n.innerHTML=src.dataset.note;
  }
  btns.forEach(function(b){b.onclick=function(){apply(b.dataset.k);};});
  apply(root.dataset.start||btns[0].dataset.k);
};

/* ===================== ТРЕНАЖЁР 1: ШЛЮЗ И ПОДСЕТЬ ===================== */
(function(){
  var root=document.getElementById('gwsim');
  if(!root)return;
  var task=null, score=0, total=0;
  function ip2n(s){var p=s.split('.').map(Number);return ((p[0]<<24)>>>0)+(p[1]<<16)+(p[2]<<8)+p[3];}
  function n2ip(n){return [(n>>>24)&255,(n>>>16)&255,(n>>>8)&255,n&255].join('.');}
  function rndInt(a,b){return a+Math.floor(Math.random()*(b-a+1));}
  function gen(){
    var m=[24,25,26,28][rndInt(0,3)];
    var size=Math.pow(2,32-m);
    var base=(ip2n('192.168.'+rndInt(0,30)+'.0')>>>0);
    base=base - (base%size);
    var net1=base, net2=(base+size*rndInt(2,5))>>>0;
    var gw1=n2ip(net1+1), gw2=n2ip(net2+1);
    var src=n2ip(net1+rndInt(10,Math.min(size-3,60)));
    var sameNet=Math.random()<0.45;
    var dst=sameNet?n2ip(net1+rndInt(61,Math.min(size-2,120))||net1+2):n2ip(net2+rndInt(10,Math.min(size-3,60)));
    if(sameNet&&dst===src)dst=n2ip(net1+2);
    task={m:m,src:src,dst:dst,gw1:gw1,gw2:gw2,net1:n2ip(net1),net2:n2ip(net2),same:sameNet};
    q(root,'#gwq').innerHTML=
      'ПК-источник <b class="kv">'+src+'/'+m+'</b> отправляет пакет на <b class="kv">'+dst+'</b>.<br>'+
      'Шлюз по умолчанию у ПК: <b class="kv">'+gw1+'</b> (интерфейс gi1/0/1 маршрутизатора R1).<br>'+
      'Вторая сеть R1: <b class="kv">'+task.net2+'/'+m+'</b>, её шлюз <b class="kv">'+gw2+'</b> (gi1/0/2).';
    qa(root,'.gwb').forEach(function(b){b.className='vbtn gwb';b.disabled=false;});
    q(root,'#gwnote').innerHTML='Сравните сеть источника и сеть получателя: совпадают ли их сетевые части при маске /'+m+'?';
  }
  qa(root,'.gwb').forEach(function(b){
    b.onclick=function(){
      if(b.disabled)return;
      total++;
      var ok=(b.dataset.k==='local')===task.same;
      b.classList.add(ok?'good':'bad');
      if(ok)score++;
      else qa(root,'.gwb').forEach(function(o){
        if((o.dataset.k==='local')===task.same)o.classList.add('good');});
      qa(root,'.gwb').forEach(function(o){o.disabled=true;});
      var net=function(ip){var n=ip2n(ip);var sz=Math.pow(2,32-task.m);return n2ip(n-(n%sz));};
      q(root,'#gwnote').innerHTML=(ok?'<b style="color:#0c7a49">Верно.</b> ':'<b style="color:#b11c3d">Нет.</b> ')+
        'Сеть источника <b class="kv">'+net(task.src)+'/'+task.m+'</b>, сеть получателя <b class="kv">'+
        net(task.dst)+'/'+task.m+'</b>. '+
        (task.same
          ? 'Сети совпадают — пакет уходит <b>напрямую</b> получателю, шлюз не нужен. ARP-запрос уйдёт на сам адрес получателя.'
          : 'Сети разные — ПК кадрирует пакет на MAC <b>шлюза '+task.gw1+'</b>, R1 смотрит таблицу маршрутизации и пересылает пакет через <b>gi1/0/2</b>.');
      q(root,'#gwscore').textContent=score+' / '+total;
    };
  });
  q(root,'#gwnew').onclick=gen;
  gen();
})();

/* ===================== ТРЕНАЖЁР 2: СТОИМОСТЬ ПУТИ ===================== */
(function(){
  var root=document.getElementById('costsim');
  if(!root)return;
  /* три пути из A в B, у каждого звена своя метрика — найти путь с минимальной суммой */
  var task=null, score=0, total=0;
  function rnd(a,b){return a+Math.floor(Math.random()*(b-a+1));}
  function gen(){
    var paths=[];
    for(var p=0;p<3;p++){
      var n=rnd(2,4), hops=[];
      for(var i=0;i<n;i++)hops.push(rnd(1,20));
      paths.push({hops:hops,sum:hops.reduce(function(a,b){return a+b;},0)});
    }
    /* гарантируем единственный минимум */
    var sums=paths.map(function(p){return p.sum;});
    var mn=Math.min.apply(null,sums);
    if(sums.filter(function(s){return s===mn;}).length>1){return gen();}
    task={paths:paths,best:sums.indexOf(mn)};
    var box=q(root,'#cspaths'); box.innerHTML='';
    var NAMES=['Путь A: R1 → R2 → … → R9','Путь Б: R1 → R3 → … → R9','Путь В: R1 → R4 → … → R9'];
    paths.forEach(function(p,i){
      var b=document.createElement('button');
      b.className='vbtn csb'; b.dataset.i=i;
      b.innerHTML='<b>'+NAMES[i]+'</b><br><span class="kv">метрики звеньев: '+p.hops.join(' + ')+'</span>';
      b.onclick=function(){pick(i);};
      box.appendChild(b);
    });
    q(root,'#csnote').innerHTML='Сложите метрики всех звеньев каждого пути и выберите путь с <b>наименьшей суммарной стоимостью</b> — именно его маршрутизатор запишет в таблицу маршрутизации.';
    q(root,'#csin').value='';
  }
  function pick(i){
    var bs=qa(root,'.csb');
    if(bs[0].disabled)return;
    total++;
    var ok=(i===task.best);
    if(ok)score++;
    bs[i].classList.add(ok?'good':'bad');
    bs[task.best].classList.add('good');
    bs.forEach(function(b,k){
      b.innerHTML=b.innerHTML+'<br><span class="kv">сумма = '+task.paths[k].sum+'</span>';
      b.disabled=true;
    });
    var v=parseInt(q(root,'#csin').value,10);
    var extra='';
    if(!isNaN(v)){
      extra=(v===task.paths[task.best].sum)
        ? ' Сумму вы посчитали верно: <b>'+v+'</b>.'
        : ' Введённая сумма <b>'+v+'</b> не сходится: правильная стоимость лучшего пути — <b>'+task.paths[task.best].sum+'</b>.';
    }
    q(root,'#csnote').innerHTML=(ok?'<b style="color:#0c7a49">Верно.</b> ':'<b style="color:#b11c3d">Нет.</b> ')+
      'Стоимости путей: '+task.paths.map(function(p,k){return String.fromCharCode(1040+(k===0?0:(k===1?1:2)))+' = '+p.sum;}).join(', ')+
      '. Лучший — с суммой <b>'+task.paths[task.best].sum+'</b>.'+extra;
    q(root,'#csscore').textContent=score+' / '+total;
  }
  q(root,'#csnew').onclick=gen;
  gen();
})();

/* ===================== ТРЕНАЖЁР 3: УРОВЕНЬ ПРИВИЛЕГИЙ ===================== */
(function(){
  var root=document.getElementById('privsim');
  if(!root)return;
  var CASES=[
    {c:'show interfaces status', need:1,  t:'Просмотр состояния интерфейсов — чистый мониторинг.'},
    {c:'show ip route',          need:5,  t:'Просмотр оперативного состояния маршрутизации.'},
    {c:'configure → interface gi1/0/1 → ip address …', need:10, t:'Настройка функционала: уровни 10–14.'},
    {c:'username user1 / privilege 9', need:15, t:'Создание пользователей доступно только с уровня 15.'},
    {c:'reload (перезагрузка устройства)', need:15, t:'Перезагрузка и загрузка ПО — только уровень 15.'},
    {c:'banner login Router-esr-200', need:10, t:'Изменение конфигурации устройства — уровни 10–14.'},
    {c:'show version', need:1, t:'Информация о версии ПО — базовый мониторинг.'},
    {c:'clock timezone gmt +7', need:10, t:'Настройка часового пояса меняет конфигурацию.'}
  ];
  var i=0,score=0,total=0,answered=false,lvl=9;
  function render(){
    answered=false;
    lvl=[1,5,9,14,15][Math.floor(Math.random()*5)];
    q(root,'#pvlvl').textContent=lvl;
    q(root,'#pvcmd').textContent=CASES[i].c;
    qa(root,'.pvb').forEach(function(b){b.className='vbtn pvb';b.disabled=false;});
    q(root,'#pvnote').textContent='';
    q(root,'#pvnum').textContent=(i+1)+' / '+CASES.length;
  }
  qa(root,'.pvb').forEach(function(b){
    b.onclick=function(){
      if(answered)return; answered=true; total++;
      var can=lvl>=CASES[i].need;
      var ok=(b.dataset.k==='yes')===can;
      b.classList.add(ok?'good':'bad');
      if(!ok)qa(root,'.pvb').forEach(function(o){if((o.dataset.k==='yes')===can)o.classList.add('good');});
      if(ok)score++;
      q(root,'#pvnote').innerHTML=(ok?'<b style="color:#0c7a49">Верно.</b> ':'<b style="color:#b11c3d">Нет.</b> ')+
        'Команде нужен уровень <b>'+CASES[i].need+'</b>, у пользователя — <b>'+lvl+'</b>. '+CASES[i].t+
        ' Правило: уровень пользователя должен быть <b>не ниже</b> требуемого уровня команды.';
      qa(root,'.pvb').forEach(function(o){o.disabled=true;});
      q(root,'#pvscore').textContent=score+' / '+total;
    };
  });
  q(root,'#pvnext').onclick=function(){i=(i+1)%CASES.length;render();};
  render();
})();

/* ===================== ТРЕНАЖЁР 4: ПОРЯДОК КОМАНД ===================== */
(function(){
  var root=document.getElementById('cfgsim');
  if(!root)return;
  var RIGHT=['configure',
             'interface gigabitethernet 1/0/1',
             'ip firewall disable',
             'ip address 192.168.25.25/24',
             'exit',
             'commit',
             'confirm'];
  var HINT={
    'configure':'Из привилегированного режима входим в режим глобального конфигурирования.',
    'interface gigabitethernet 1/0/1':'Выбираем конкретный физический интерфейс — попадаем в config-if-gi.',
    'ip firewall disable':'Снимаем межсетевой экран, иначе он заблокирует весь транзитный трафик.',
    'ip address 192.168.25.25/24':'Назначаем IP-адрес и маску интерфейсу.',
    'exit':'Выходим из режима конфигурирования в привилегированный режим.',
    'commit':'Применяем изменения и сохраняем конфигурацию во flash.',
    'confirm':'Подтверждаем: без confirm устройство откатит настройки по таймеру.'
  };
  var pool=[], placed=[];
  function shuffle(a){a=a.slice();for(var i=a.length-1;i>0;i--){var j=Math.floor(Math.random()*(i+1));var t=a[i];a[i]=a[j];a[j]=t;}return a;}
  function reset(){
    pool=shuffle(RIGHT); placed=[]; render();
    q(root,'#cfnote').innerHTML='Соберите последовательность настройки интерфейса: нажимайте команды в правильном порядке.';
  }
  function render(){
    var pb=q(root,'#cfpool'); pb.innerHTML='';
    pool.forEach(function(c){
      var b=document.createElement('button');
      b.className='vbtn'; b.innerHTML='<span class="kv">'+c+'</span>';
      b.onclick=function(){tryPut(c);};
      pb.appendChild(b);
    });
    var ob=q(root,'#cfout'); ob.innerHTML='';
    placed.forEach(function(c,i){
      var d=document.createElement('div');
      d.className='rw done';
      d.innerHTML='<span><b>'+(i+1)+'</b></span><span class="kv">'+c+'</span><span>'+HINT[c]+'</span>';
      ob.appendChild(d);
    });
    if(!placed.length){
      var d2=document.createElement('div');
      d2.className='rw';
      d2.innerHTML='<span>—</span><span class="kv">пусто</span><span>нажмите первую команду</span>';
      ob.appendChild(d2);
    }
    q(root,'#cfcnt').textContent=placed.length+' / '+RIGHT.length;
  }
  function tryPut(c){
    if(c===RIGHT[placed.length]){
      placed.push(c); pool.splice(pool.indexOf(c),1); render();
      q(root,'#cfnote').innerHTML='<b style="color:#0c7a49">Верно.</b> '+HINT[c];
      if(placed.length===RIGHT.length)
        q(root,'#cfnote').innerHTML='<b style="color:#0c7a49">Готово!</b> Интерфейс gi1/0/1 настроен, изменения применены и подтверждены. Проверить: <span class="kv">show interfaces status gigabitethernet 1/0/1</span>.';
    }else{
      q(root,'#cfnote').innerHTML='<b style="color:#b11c3d">Не сейчас.</b> Команда <span class="kv">'+c+
        '</span> здесь не подходит: '+HINT[c]+' Сейчас нужна команда, которая идёт раньше.';
    }
  }
  q(root,'#cfreset').onclick=reset;
  reset();
})();

/* ===================== ТРЕНАЖЁР 5: ДИАГНОСТИКА ===================== */
(function(){
  var root=document.getElementById('diagsim');
  if(!root)return;
  var CASES=[
    {t:'Ping до соседнего ПК в своей сети проходит, ping до шлюза — нет.',a:'fw',
     e:'На интерфейсе маршрутизатора не отключён межсетевой экран (ip firewall disable) либо интерфейс в down. Локальная сеть работает, значит проблема именно на шлюзе.'},
    {t:'Ping до шлюза проходит, ping до узла в удалённой сети — нет, ответа нет совсем.',a:'rt',
     e:'До шлюза дошли — локальная часть исправна. Дальше пакету нужен маршрут: либо в таблице маршрутизации нет пути к сети назначения, либо на обратном пути стоит фильтр ICMP.'},
    {t:'Ни один узел локальной сети не отвечает, хотя кабель подключён и линк горит.',a:'ip',
     e:'Скорее всего неверно задан IP-адрес или маска подсети узла: он считает соседей «чужой» сетью и шлёт всё на шлюз.'},
    {t:'Tracert доходит до 3-го перехода, дальше идут только звёздочки, но сайт открывается.',a:'icmp',
     e:'Промежуточные маршрутизаторы фильтруют ICMP и не отвечают на запросы трассировки. Передача данных при этом работает — это не авария.'},
    {t:'ssh admin@172.16.100.12 — соединение отклонено, хотя адрес пингуется.',a:'ssh',
     e:'IP-связность есть, значит дело в сервисе: на маршрутизаторе не включён ssh-сервер (ip ssh server) либо настройка не применена через commit/confirm.'},
    {t:'После ввода команд всё работало, а через 10 минут настройки пропали.',a:'commit',
     e:'Изменения применили командой commit, но не подтвердили командой confirm. По истечении таймера устройство откатило конфигурацию.'}
  ];
  var LAB={fw:'Межсетевой экран / интерфейс',rt:'Нет маршрута или фильтр на пути',
           ip:'Неверный IP-адрес или маска',icmp:'ICMP фильтруется',ssh:'Не поднят сервис SSH',
           commit:'Не выполнен confirm'};
  var i=0,score=0,total=0,answered=false;
  function render(){
    answered=false;
    q(root,'#dgt').textContent=CASES[i].t;
    qa(root,'.dgb').forEach(function(b){b.className='vbtn dgb';b.disabled=false;});
    q(root,'#dgnote').textContent='';
    q(root,'#dgnum').textContent=(i+1)+' / '+CASES.length;
  }
  qa(root,'.dgb').forEach(function(b){
    b.onclick=function(){
      if(answered)return; answered=true; total++;
      var ok=b.dataset.k===CASES[i].a;
      b.classList.add(ok?'good':'bad');
      if(!ok)qa(root,'.dgb').forEach(function(o){if(o.dataset.k===CASES[i].a)o.classList.add('good');});
      if(ok)score++;
      q(root,'#dgnote').innerHTML=(ok?'<b style="color:#0c7a49">Верно.</b> ':'<b style="color:#b11c3d">Нет.</b> ')+
        '<b>'+LAB[CASES[i].a]+'.</b> '+CASES[i].e;
      qa(root,'.dgb').forEach(function(o){o.disabled=true;});
      q(root,'#dgscore').textContent=score+' / '+total;
    };
  });
  q(root,'#dgnext').onclick=function(){i=(i+1)%CASES.length;render();};
  render();
})();

/* ===================== ТРЕНАЖЁР 6: ИНТЕРФЕЙСЫ И ИМЕНА ===================== */
(function(){
  var root=document.getElementById('ifsim');
  if(!root)return;
  var CASES=[
    {n:'gigabitethernet 1/0/3', a:'phys', e:'Физический порт: 1 — несъёмное шасси, 0 — материнская плата, 3 — порядковый номер порта.'},
    {n:'gigabitethernet 1/0/1.20', a:'sub', e:'Sub-интерфейс: после точки один VLAN-тег (20). Отдельный широковещательный домен на том же порту.'},
    {n:'gigabitethernet 1/0/1.20.420', a:'qinq', e:'QinQ-интерфейс: два тега — внешний 20 и внутренний 420. Создаётся только поверх существующего sub-интерфейса .20.'},
    {n:'loopback1', a:'loop', e:'Логический интерфейс loopback: до 8 IP-адресов, единственный интерфейс без широковещательного домена, всегда up.'},
    {n:'port-channel1', a:'log', e:'Логический агрегированный интерфейс: несколько физических портов объединены в один канал.'},
    {n:'bridge1', a:'log', e:'Логический интерфейс сетевого моста (bridge) — создаётся в системе, физического разъёма нет.'},
    {n:'usb-модем / SFP-модуль', a:'plug', e:'Подключаемый интерфейс: появляется, когда модуль физически вставлен в устройство.'},
    {n:'tengigabitethernet 1/0/2', a:'phys', e:'Физический порт на 10 Гбит/с. Для 10G режим дуплекса не выбирается — только full-duplex.'}
  ];
  var LAB={phys:'Физический',sub:'Sub-интерфейс',qinq:'QinQ',loop:'Loopback',log:'Логический',plug:'Подключаемый'};
  var i=0,score=0,total=0,answered=false;
  function render(){
    answered=false;
    q(root,'#ifn').textContent=CASES[i].n;
    qa(root,'.ifb').forEach(function(b){b.className='vbtn ifb';b.disabled=false;});
    q(root,'#ifnote').textContent='';
    q(root,'#ifnum').textContent=(i+1)+' / '+CASES.length;
  }
  qa(root,'.ifb').forEach(function(b){
    b.onclick=function(){
      if(answered)return; answered=true; total++;
      var ok=b.dataset.k===CASES[i].a;
      b.classList.add(ok?'good':'bad');
      if(!ok)qa(root,'.ifb').forEach(function(o){if(o.dataset.k===CASES[i].a)o.classList.add('good');});
      if(ok)score++;
      q(root,'#ifnote').innerHTML=(ok?'<b style="color:#0c7a49">Верно.</b> ':'<b style="color:#b11c3d">Нет.</b> ')+
        '<b>'+LAB[CASES[i].a]+'.</b> '+CASES[i].e;
      qa(root,'.ifb').forEach(function(o){o.disabled=true;});
      q(root,'#ifscore').textContent=score+' / '+total;
    };
  });
  q(root,'#ifnext').onclick=function(){i=(i+1)%CASES.length;render();};
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
