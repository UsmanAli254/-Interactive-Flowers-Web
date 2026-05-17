p = r'C:\Users\Usman Ali\.kiro\New folder\Daizzyy\flowers\index.html'

JS = """<script>
// ============================================================
// PERFORMANCE: use canvas for falling petals (no DOM spam)
// ============================================================
const canvas = document.createElement('canvas');
canvas.style.cssText = 'position:fixed;top:0;left:0;width:100%;height:100%;pointer-events:none;z-index:8';
document.body.appendChild(canvas);
const ctx = canvas.getContext('2d');

function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
resize();
window.addEventListener('resize', resize);

// Petal colors matching the 4 flowers
const PETAL_COLORS = [
  '#ffe050','#f9b000','#fb8c00',   // sunflower
  '#f8f4ee','#ede8e0','#ffffff',   // rose
  '#e8f4f8','#c8dde8',             // daisy
  '#e8506a','#f4909a','#d84060',   // tulip
];

// Ambient falling petals - simple ellipses for performance
const petals = [];
for (let i = 0; i < 22; i++) {
  petals.push({
    x: Math.random() * window.innerWidth,
    y: -Math.random() * window.innerHeight,
    w: 8 + Math.random() * 14,
    h: 4 + Math.random() * 7,
    speed: 0.6 + Math.random() * 1.2,
    drift: (Math.random() - .5) * 0.8,
    rot: Math.random() * Math.PI * 2,
    rotSpeed: (Math.random() - .5) * 0.04,
    color: PETAL_COLORS[Math.floor(Math.random() * PETAL_COLORS.length)],
    alpha: 0.55 + Math.random() * 0.4,
  });
}

// Touch burst petals (temporary, drawn on canvas)
const burstPetals = [];

function addBurst(x, y, count) {
  for (let i = 0; i < count; i++) {
    const angle = (Math.random() * 280 - 140) * Math.PI / 180;
    const speed = 3 + Math.random() * 5;
    burstPetals.push({
      x, y,
      vx: Math.cos(angle) * speed,
      vy: Math.sin(angle) * speed - 4,
      w: 10 + Math.random() * 12,
      h: 5 + Math.random() * 6,
      rot: Math.random() * Math.PI * 2,
      rotSpeed: (Math.random() - .5) * 0.15,
      color: PETAL_COLORS[Math.floor(Math.random() * PETAL_COLORS.length)],
      alpha: 1,
      life: 1,
    });
  }
}

function drawPetal(x, y, w, h, rot, color, alpha) {
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.translate(x, y);
  ctx.rotate(rot);
  ctx.beginPath();
  ctx.ellipse(0, 0, w / 2, h / 2, 0, 0, Math.PI * 2);
  ctx.fillStyle = color;
  ctx.fill();
  ctx.restore();
}

function animate() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Ambient falling petals
  for (const p of petals) {
    p.y += p.speed;
    p.x += p.drift;
    p.rot += p.rotSpeed;
    if (p.y > canvas.height + 20) {
      p.y = -20;
      p.x = Math.random() * canvas.width;
    }
    drawPetal(p.x, p.y, p.w, p.h, p.rot, p.color, p.alpha);
  }

  // Burst petals
  for (let i = burstPetals.length - 1; i >= 0; i--) {
    const b = burstPetals[i];
    b.x += b.vx;
    b.y += b.vy;
    b.vy += 0.18; // gravity
    b.vx *= 0.97;
    b.rot += b.rotSpeed;
    b.life -= 0.022;
    b.alpha = b.life;
    if (b.life <= 0) { burstPetals.splice(i, 1); continue; }
    drawPetal(b.x, b.y, b.w, b.h, b.rot, b.color, b.alpha);
  }

  requestAnimationFrame(animate);
}
animate();

// ============================================================
// FIREFLIES - just 18, lightweight divs
// ============================================================
for (let i = 0; i < 18; i++) {
  const ff = document.createElement('div');
  const sz = 3 + Math.random() * 4;
  const flyDur = 6 + Math.random() * 9;
  const pulseDur = 1.2 + Math.random() * 1.6;
  const del = -(Math.random() * 10);
  const dx = (Math.random() - .5) * 350;
  const dy = (Math.random() - .5) * 250;
  ff.style.cssText = `position:fixed;border-radius:50%;pointer-events:none;z-index:9;
    width:${sz}px;height:${sz}px;
    left:${Math.random()*95}%;top:${5+Math.random()*80}%;
    background:radial-gradient(circle,#fffde7 0%,#ffe57f 45%,transparent 70%);
    box-shadow:0 0 6px 3px rgba(255,240,100,.7),0 0 16px 7px rgba(255,210,40,.25);
    --dx:${dx}px;--dy:${dy}px;
    animation:ffMove ${flyDur}s linear ${del}s infinite,ffPulse ${pulseDur}s ease-in-out ${-(Math.random()*2)}s infinite`;
  document.body.appendChild(ff);
}

// ============================================================
// RIPPLE
// ============================================================
function spawnRipple(x, y) {
  const d = document.createElement('div');
  d.className = 'rip';
  d.style.left = x + 'px';
  d.style.top = y + 'px';
  document.body.appendChild(d);
  setTimeout(() => d.remove(), 950);
}

// ============================================================
// REBLOOM
// ============================================================
function triggerRebloom(fg) {
  fg.querySelectorAll('.petal').forEach((p, i) => {
    p.style.animation = 'none';
    p.style.opacity = '0';
    void p.offsetWidth;
    p.style.animation = `bloom 1.3s cubic-bezier(.34,1.56,.64,1) ${i * .07}s forwards`;
  });
}

// ============================================================
// FLOWER INTERACTIONS
// ============================================================
document.querySelectorAll('.fg').forEach(fg => {
  fg.addEventListener('mouseenter', () =>
    fg.querySelectorAll('.petals-g').forEach(pg => pg.style.animation = 'shimmer .7s ease-in-out infinite'));
  fg.addEventListener('mouseleave', () =>
    fg.querySelectorAll('.petals-g').forEach(pg => pg.style.animation = 'shimmer 3.5s ease-in-out infinite'));

  const fire = (x, y) => {
    triggerRebloom(fg);
    addBurst(x, y, 18);
    spawnRipple(x, y);
  };
  fg.addEventListener('click', e => {
    e.stopPropagation();
    const r = fg.getBoundingClientRect();
    fire(r.left + r.width / 2, r.top + r.height * .25);
  });
  fg.addEventListener('touchstart', e => {
    e.preventDefault();
    const t = e.touches[0];
    fire(t.clientX, t.clientY);
  }, { passive: false });
});

// ============================================================
// TOUCH / CLICK ANYWHERE
// ============================================================
document.addEventListener('click', e => {
  if (e.target.closest('.fg')) return;
  addBurst(e.clientX, e.clientY, 14);
  spawnRipple(e.clientX, e.clientY);
});
document.addEventListener('touchstart', e => {
  if (e.target.closest('.fg')) return;
  const t = e.touches[0];
  addBurst(t.clientX, t.clientY, 14);
  spawnRipple(t.clientX, t.clientY);
}, { passive: true });
</script>
</body>
</html>
"""

with open(p, 'a', encoding='utf-8') as f:
    f.write(JS)

# Verify
with open(p, 'r', encoding='utf-8') as f:
    html = f.read()

print('Size:', len(html), 'bytes')
print('canvas:', 'canvas' in html)
print('addBurst:', 'addBurst' in html)
print('fireflies:', 'ffMove' in html)
print('ends correctly:', html.strip().endswith('</html>'))
