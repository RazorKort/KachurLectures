/* ================= практикум: проверка ответов ================= */
(function(){
  var tasks=[].slice.call(document.querySelectorAll('.tsk')); if(!tasks.length) return;
  function norm(s){ return String(s||'').toLowerCase().replace(/ё/g,'е').replace(/\s+/g,' ').replace(/\s*\/\s*/g,'/').trim(); }
  function okList(el){ return String(el.dataset.ok||'').split('|').map(norm); }
  tasks.forEach(function(box){
    var msg=box.querySelector('.tmsg'), sol=box.querySelector('.tsol');
    var ins=[].slice.call(box.querySelectorAll('input'));
    function mark(el,good){ var w=el.closest('.tfl')||el.closest('.tck'); if(!w) return; w.classList.remove('ok','no'); w.classList.add(good?'ok':'no'); }
    function clear(){ ins.forEach(function(el){ if(el.type==='checkbox') el.checked=false; else el.value='';
      var w=el.closest('.tfl')||el.closest('.tck'); if(w) w.classList.remove('ok','no'); });
      msg.innerHTML=''; msg.className='tmsg'; sol.hidden=true; }
    function check(){
      var good=0, total=0, empty=0;
      ins.forEach(function(el){
        if(el.type==='checkbox'){ total++; var want=el.dataset.ok==='1'; var hit=el.checked===want; if(hit) good++; mark(el,hit); return; }
        total++; if(!el.value.trim()) empty++;
        var hit=okList(el).indexOf(norm(el.value))>=0; if(hit) good++; mark(el,hit);
      });
      msg.className='tmsg on '+(good===total?'good':'bad');
      if(good===total) msg.innerHTML='<b>Верно — '+good+' из '+total+'.</b> Нажмите «Показать решение», чтобы увидеть разбор.';
      else if(empty===total) msg.innerHTML='<b>Сначала заполните поля.</b>';
      else msg.innerHTML='<b>Пока '+good+' из '+total+'.</b> Неверные поля подсвечены — попробуйте ещё раз или откройте решение.';
    }
    box.addEventListener('click',function(e){
      var b=e.target.closest('[data-a]'); if(!b) return;
      if(b.dataset.a==='check') check();
      else if(b.dataset.a==='sol'){ sol.hidden=!sol.hidden; b.classList.toggle('on',!sol.hidden); }
      else clear();
    });
    box.addEventListener('keydown',function(e){ if(e.key==='Enter'&&e.target.tagName==='INPUT'){ e.preventDefault(); check(); } });
    var sl=box.closest('.slide'); var prev=sl._init; sl._init=function(s){ if(prev) prev(s); clear(); };
  });
})();
