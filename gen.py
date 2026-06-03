p = r'C:\Users\Usman Ali\.kiro\New folder\Daizzyy\flowers\index.html'
with open(p, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('src="flowers/sunflower.webp"', 'src="sunflower.webp"')
html = html.replace('src="flowers/tulip.webp"', 'src="tulip.webp"')
html = html.replace('src="flowers/white-rose.webp"', 'src="white-rose.webp"')
html = html.replace('src="flowers/daisy.webp"', 'src="daisy.webp"')

with open(p, 'w', encoding='utf-8') as f:
    f.write(html)
print('done')
