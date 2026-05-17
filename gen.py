p = r'C:\Users\Usman Ali\.kiro\New folder\Daizzyy\flowers\index.html'

JS = """<script>
const scene = document.getElementById('scene');
for(let i=0;i<20;i++){
  const ff=document.createElement('div');ff.className='ff';
  const sz=2+Math.random()*3,x=Math.random()*100,y=10+Math.random()*75;
  const dx=(Math.random()-.5)*320,dy=(Math.random()-.5)*220;
  const dur=5+Math.random()*9,del=Math.random()*10;
  ff.style.cssText=`left:${x}%;top:${y}%;width:${sz}px;height:${sz}px;--dx:${dx}px;--dy:${dy}px;animation-duration:${dur}s;animation-delay:-${del}s`;
  scene.appendChild(ff);
}
const fpColors=[['#f9a825','#fb8c00'],['#e91e8c','#f48fb1'],['#ede7f6','#ffffff'],['#eceff1','#ffffff']];
for(let i=0;i<14;i++){
  const fp=document.createElementNS('http://www.w3.org/2000/svg','svg');
  fp.setAttribute('width','18');fp.setAttribute('height','36');fp.setAttribute('viewBox','-12 -36 24 40');
  const path=document.createElementNS('http://www.w3.org/2000/svg','path');
  const shapes=['M0,0 Q-8,-14 -3,-28 Q0,-34 3,-28 Q8,-14 0,0','M0,0 Q-10,-10 -4,-22 Q0,-28 4,-22 Q10,-10 0,0','M0,0 Q-6,-16 -2,-30 Q0,-36 2,-30 Q6,-16 0,0'];
  path.setAttribute('d',shapes[i%3]);
  const c=fpColors[i%4];path.setAttribute('fill',c[Math.floor(Math.random()*2)]);path.setAttribute('opacity','0.8');
  fp.appendChild(path);fp.className='fp';
  const left=Math.random()*100,drift=(Math.random()-.5)*220,dur=7+Math.random()*11,del=Math.random()*14;
  fp.style.cssText=`left:${left}%;--drift:${drift}px;animation-duration:${dur}s;animation-delay:-${del}s`;
  scene.appendChild(fp);
}
document.querySelectorAll('.fg').forEach(fg=>{
  fg.addEventListener('mouseenter',()=>{fg.querySelectorAll('.petals-g').forEach(pg=>{pg.style.animation='shimmer .8s ease-in-out infinite'})});
  fg.addEventListener('mouseleave',()=>{fg.querySelectorAll('.petals-g').forEach(pg=>{pg.style.animation='shimmer 3.5s ease-in-out infinite'})});
  fg.addEventListener('touchstart',e=>{e.preventDefault();triggerRebloom(fg);const t=e.touches[0];spawnBurst(t.clientX,t.clientY,8)},{passive:false});
});
function triggerRebloom(fg){
  fg.querySelectorAll('.petal').forEach((p,i)=>{
    p.style.animation='none';p.style.opacity='0';void p.offsetWidth;
    const d=i*0.08;p.style.animation=`bloom 1.3s cubic-bezier(.34,1.56,.64,1) ${d}s forwards, shimmer 3.5s ease-in-out ${d}s infinite`;
  });
}
function spawnBurst(x,y,count){
  const cols=['#f9a825','#e91e8c','#ffffff','#eceff1','#fb8c00','#f48fb1'];
  for(let i=0;i<count;i++){
    const bp=document.createElementNS('http://www.w3.org/2000/svg','svg');
    bp.setAttribute('width','14');bp.setAttribute('height','28');bp.setAttribute('viewBox','-10 -30 20 34');
    const path=document.createElementNS('http://www.w3.org/2000/svg','path');
    path.setAttribute('d','M0,0 Q-6,-12 -2,-24 Q0,-30 2,-24 Q6,-12 0,0');
    path.setAttribute('fill',cols[i%cols.length]);bp.appendChild(path);bp.className='bp';
    const angle=(i/count)*Math.PI*2,dist=55+Math.random()*75;
    const bx=Math.cos(angle)*dist,by=Math.sin(angle)*dist-55;
    bp.style.cssText=`left:${x}px;top:${y}px;--bx:${bx}px;--by:${by}px;z-index:999`;
    document.body.appendChild(bp);setTimeout(()=>bp.remove(),1200);
  }
}
document.querySelectorAll('.fg').forEach(fg=>{
  fg.addEventListener('click',e=>{
    e.stopPropagation();triggerRebloom(fg);
    const r=fg.getBoundingClientRect();spawnBurst(r.left+r.width/2,r.top+r.height*.22,10);
  });
});
document.addEventListener('click',e=>{
  if(e.target.closest('.fg'))return;
  const rip=document.createElement('div');rip.className='ripple';
  rip.style.left=e.clientX+'px';rip.style.top=e.clientY+'px';
  document.body.appendChild(rip);setTimeout(()=>rip.remove(),950);
  spawnBurst(e.clientX,e.clientY,5);
});
</script>
</body>
</html>
"""

with open(p, 'a', encoding='utf-8') as f:
    f.write(JS)
print('JS written')
