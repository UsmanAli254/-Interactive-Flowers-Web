p = r'C:\Users\Usman Ali\.kiro\New folder\Daizzyy\flowers\index.html'
with open(p, 'r', encoding='utf-8') as f:
    html = f.read()

old_anim = '@media(max-width:600px){'

new_anim = '''/* ── Daisy center pulse (breathing dome) ── */
#f4 .fhead ellipse{animation:daisyPulse 4s ease-in-out infinite}
@keyframes daisyPulse{0%,100%{transform:scale(1)}50%{transform:scale(1.06)}}
/* ── Rose petal unfurl (subtle continuous) ── */
#f3 .petals-g{animation:roseBreath 5s ease-in-out infinite}
@keyframes roseBreath{0%,100%{filter:brightness(1) drop-shadow(0 0 4px rgba(255,255,240,0.3))}50%{filter:brightness(1.08) drop-shadow(0 0 12px rgba(255,255,240,0.6))}}
/* ── Tulip gentle open-close ── */
#f2 .petals-g{animation:tulipSway 6s ease-in-out infinite}
@keyframes tulipSway{0%,100%{transform:scaleX(1)}50%{transform:scaleX(1.04)}}
/* ── Daisy petal shimmer (light catching) ── */
#f4 .petals-g{animation:daisyShimmer 3s ease-in-out infinite}
@keyframes daisyShimmer{0%,100%{filter:brightness(1) drop-shadow(0 0 3px rgba(200,230,255,0.2))}50%{filter:brightness(1.1) drop-shadow(0 0 10px rgba(200,230,255,0.5))}}
/* ── Hover: rose glows white-warm ── */
#f3:hover .fhead{filter:drop-shadow(0 0 20px rgba(255,255,240,0.95)) drop-shadow(0 0 45px rgba(240,240,200,0.5))}
@media(max-width:600px){'''

html = html.replace(old_anim, new_anim)
print('animations added:', 'daisyPulse' in html)
with open(p, 'w', encoding='utf-8') as f:
    f.write(html)
print('saved, size:', len(html))
