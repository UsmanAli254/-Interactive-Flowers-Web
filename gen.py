p = r'C:\Users\Usman Ali\.kiro\New folder\Daizzyy\flowers\index.html'
with open(p, 'r', encoding='utf-8') as f:
    html = f.read()

old_js = """<script>
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
</script>"""

new_js = """<script>
const scene = document.getElementById('scene');

// ═══════════════════════════════════════════════
// FIREFLIES - glowing orbs with wandering paths
// ═══════════════════════════════════════════════
const FF_COUNT = 28;
const fireflies = [];

function createFirefly() {
  const ff = document.createElement('div');
  ff.className = 'ff';
  const sz = 3 + Math.random() * 4;
  ff.style.width = sz + 'px';
  ff.style.height = sz + 'px';
  ff.style.left = (Math.random() * 95) + '%';
  ff.style.top = (10 + Math.random() * 75) + '%';
  // Each firefly wanders independently via CSS vars
  const dx = (Math.random() - .5) * 380;
  const dy = (Math.random() - .5) * 260;
  const dur = 5 + Math.random() * 10;
  const del = -(Math.random() * 12);
  const pulseDur = 1.2 + Math.random() * 1.8;
  ff.style.cssText += `;--dx:${dx}px;--dy:${dy}px;animation-duration:${dur}s,${pulseDur}s;animation-delay:${del}s,${-(Math.random()*2)}s`;
  scene.appendChild(ff);
  fireflies.push(ff);
  // Respawn at new position when animation ends
  ff.addEventListener('animationiteration', () => {
    ff.style.left = (Math.random() * 95) + '%';
    ff.style.top = (10 + Math.random() * 75) + '%';
    const ndx = (Math.random() - .5) * 380;
    const ndy = (Math.random() - .5) * 260;
    ff.style.setProperty('--dx', ndx + 'px');
    ff.style.setProperty('--dy', ndy + 'px');
  });
}
for (let i = 0; i < FF_COUNT; i++) createFirefly();

// ═══════════════════════════════════════════════
// AMBIENT FALLING PETALS from top (always on)
// ═══════════════════════════════════════════════
const PETAL_SHAPES = [
  // sunflower petal
  'M0,0 Q-12,-8 -14,-32 Q-10,-54 0,-58 Q10,-54 14,-32 Q12,-8 0,0',
  // rose petal - wide cupped
  'M0,0 Q-16,-6 -16,-28 Q-12,-48 0,-52 Q12,-48 16,-28 Q16,-6 0,0',
  // daisy petal - thin elongated
  'M0,0 Q-7,-10 -5,-32 Q-2,-48 0,-52 Q2,-48 5,-32 Q7,-10 0,0',
  // tulip petal - egg
  'M0,0 Q-14,-5 -14,-30 Q-10,-52 0,-56 Q10,-52 14,-30 Q14,-5 0,0',
  // small round petal
  'M0,0 Q-10,-8 -10,-22 Q-6,-36 0,-38 Q6,-36 10,-22 Q10,-8 0,0',
];
const PETAL_COLORS = [
  '#ffe050','#f9b000','#fb8c00',   // sunflower yellow/orange
  '#f8f4ee','#ede8e0','#ffffff',   // rose white/cream
  '#e8f4f8','#c8dde8','#f0f8ff',   // daisy white-blue
  '#e8506a','#f4909a','#d84060',   // tulip pink-red
];

function spawnFallingPetal() {
  const svg = document.createElementNS('http://www.w3.org/2000/svg','svg');
  const size = 18 + Math.random() * 22;
  svg.setAttribute('width', size);
  svg.setAttribute('height', size * 2.2);
  svg.setAttribute('viewBox', '-18 -60 36 65');
  const path = document.createElementNS('http://www.w3.org/2000/svg','path');
  path.setAttribute('d', PETAL_SHAPES[Math.floor(Math.random() * PETAL_SHAPES.length)]);
  path.setAttribute('fill', PETAL_COLORS[Math.floor(Math.random() * PETAL_COLORS.length)]);
  path.setAttribute('opacity', (0.6 + Math.random() * 0.35).toFixed(2));
  svg.appendChild(path);
  svg.className = 'fp';
  svg.style.left = (Math.random() * 105 - 5) + '%';
  const drift = (Math.random() - .5) * 280;
  const dur = 8 + Math.random() * 14;
  const del = -(Math.random() * 20);
  svg.style.cssText += `;--drift:${drift}px;animation-duration:${dur}s;animation-delay:${del}s`;
  scene.appendChild(svg);
}
for (let i = 0; i < 22; i++) spawnFallingPetal();

// ═══════════════════════════════════════════════
// TOUCH / CLICK: petal rain shower at point
// ═══════════════════════════════════════════════
function spawnTouchPetalRain(x, y) {
  const count = 14;
  for (let i = 0; i < count; i++) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg','svg');
    const size = 12 + Math.random() * 18;
    svg.setAttribute('width', size);
    svg.setAttribute('height', size * 2);
    svg.setAttribute('viewBox', '-18 -60 36 65');
    const path = document.createElementNS('http://www.w3.org/2000/svg','path');
    path.setAttribute('d', PETAL_SHAPES[Math.floor(Math.random() * PETAL_SHAPES.length)]);
    path.setAttribute('fill', PETAL_COLORS[Math.floor(Math.random() * PETAL_COLORS.length)]);
    path.setAttribute('opacity', '0.9');
    svg.appendChild(path);
    svg.className = 'tp';
    // Fan out upward then fall
    const angle = (Math.random() * 260 - 130) * Math.PI / 180; // upward fan
    const dist = 60 + Math.random() * 140;
    const tx = Math.cos(angle) * dist;
    const ty = Math.sin(angle) * dist - 80; // bias upward
    const rot = (Math.random() - .5) * 540 + 'deg';
    const dur = 0.9 + Math.random() * 0.8;
    const del = i * 0.04;
    svg.style.cssText = `left:${x}px;top:${y}px;--tx:${tx}px;--ty:${ty}px;--tr:${rot};animation-duration:${dur}s;animation-delay:${del}s;z-index:9999`;
    document.body.appendChild(svg);
    setTimeout(() => svg.remove(), (dur + del + 0.2) * 1000);
  }
}

// ═══════════════════════════════════════════════
// RIPPLE effect
// ═══════════════════════════════════════════════
function spawnRipple(x, y) {
  const rip = document.createElement('div');
  rip.className = 'ripple';
  rip.style.left = x + 'px';
  rip.style.top = y + 'px';
  document.body.appendChild(rip);
  setTimeout(() => rip.remove(), 1100);
}

// ═══════════════════════════════════════════════
// BURST petals from flower center
// ═══════════════════════════════════════════════
function spawnBurst(x, y, count) {
  for (let i = 0; i < count; i++) {
    const svg = document.createElementNS('http://www.w3.org/2000/svg','svg');
    svg.setAttribute('width','16');svg.setAttribute('height','32');
    svg.setAttribute('viewBox','-12 -36 24 40');
    const path = document.createElementNS('http://www.w3.org/2000/svg','path');
    path.setAttribute('d', PETAL_SHAPES[i % PETAL_SHAPES.length]);
    path.setAttribute('fill', PETAL_COLORS[i % PETAL_COLORS.length]);
    svg.appendChild(path);
    svg.className = 'bp';
    const angle = (i / count) * Math.PI * 2;
    const dist = 50 + Math.random() * 90;
    const bx = Math.cos(angle) * dist;
    const by = Math.sin(angle) * dist - 60;
    svg.style.cssText = `left:${x}px;top:${y}px;--bx:${bx}px;--by:${by}px;z-index:9999`;
    document.body.appendChild(svg);
    setTimeout(() => svg.remove(), 1400);
  }
}

// ═══════════════════════════════════════════════
// REBLOOM on click/touch
// ═══════════════════════════════════════════════
function triggerRebloom(fg) {
  fg.querySelectorAll('.petal').forEach((p, i) => {
    p.style.animation = 'none';
    p.style.opacity = '0';
    void p.offsetWidth;
    const d = i * 0.07;
    p.style.animation = `bloom 1.3s cubic-bezier(.34,1.56,.64,1) ${d}s forwards, shimmer 3.5s ease-in-out ${d}s infinite`;
  });
}

// ═══════════════════════════════════════════════
// FLOWER hover shimmer boost
// ═══════════════════════════════════════════════
document.querySelectorAll('.fg').forEach(fg => {
  fg.addEventListener('mouseenter', () => {
    fg.querySelectorAll('.petals-g').forEach(pg => { pg.style.animation = 'shimmer .7s ease-in-out infinite'; });
  });
  fg.addEventListener('mouseleave', () => {
    fg.querySelectorAll('.petals-g').forEach(pg => { pg.style.animation = 'shimmer 3.5s ease-in-out infinite'; });
  });
  fg.addEventListener('click', e => {
    e.stopPropagation();
    triggerRebloom(fg);
    const r = fg.getBoundingClientRect();
    spawnBurst(r.left + r.width / 2, r.top + r.height * .2, 12);
  });
  fg.addEventListener('touchstart', e => {
    e.preventDefault();
    triggerRebloom(fg);
    const t = e.touches[0];
    spawnBurst(t.clientX, t.clientY, 12);
    spawnTouchPetalRain(t.clientX, t.clientY);
  }, { passive: false });
});

// ═══════════════════════════════════════════════
// TOUCH anywhere = petal rain + ripple
// ═══════════════════════════════════════════════
document.addEventListener('touchstart', e => {
  if (e.target.closest('.fg')) return;
  const t = e.touches[0];
  spawnRipple(t.clientX, t.clientY);
  spawnTouchPetalRain(t.clientX, t.clientY);
}, { passive: true });

// ═══════════════════════════════════════════════
// CLICK anywhere (desktop) = ripple + small shower
// ═══════════════════════════════════════════════
document.addEventListener('click', e => {
  if (e.target.closest('.fg')) return;
  spawnRipple(e.clientX, e.clientY);
  spawnTouchPetalRain(e.clientX, e.clientY);
});
</script>"""

html = html.replace(old_js, new_js)
print('JS replaced:', 'spawnTouchPetalRain' in html and 'FF_COUNT' in html)
with open(p, 'w', encoding='utf-8') as f:
    f.write(html)
print('saved, size:', len(html))
