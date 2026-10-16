# -*- coding: utf-8 -*-
"""Движок деки 2.6: движок 2.2 + варианты фона по слайдам + автоподгонка масштаба."""

from _sw_engine import JS as BASE

FIT = r"""
function fit(s){
  var sc=s.querySelector('.sc'), w=sc&&sc.querySelector('.wrap'); if(!w)return;
  w.style.zoom='';
  if(window.innerWidth<900||s.classList.contains('cover-slide')||s.querySelector('.scene,.figwrap,.pic'))return;
  var H=sc.clientHeight, z=1;
  function nat(){var m=w.style.minHeight;w.style.minHeight='0';w.style.flex='none';
    var C=w.scrollHeight;w.style.minHeight=m;w.style.flex='';return C;}
  for(var i=0;i<6;i++){
    var C=nat(); if(C<40)return;
    var z2=Math.max(.8,Math.min(1.45,H/C*.985));
    if(Math.abs(z2-z)<.01)break;
    z=z2; w.style.zoom=z.toFixed(3);
  }
}
window.addEventListener('resize',function(){clearTimeout(window.__rz);
  window.__rz=setTimeout(function(){fit(slides[cur]);},120);});
"""

JS = (BASE
      .replace("function qa(root,sel)", FIT + "\nfunction qa(root,sel)", 1)
      .replace("slides[cur].classList.add('on');",
               "slides[cur].classList.add('on');document.body.dataset.bg=slides[cur].dataset.bg||'a';"
               "fit(slides[cur]);", 1))
assert JS.count("function fit(") == 1 and "dataset.bg" in JS
