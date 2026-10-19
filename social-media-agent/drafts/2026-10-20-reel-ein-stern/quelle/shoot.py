import sys,os,json
from playwright.sync_api import sync_playwright
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
T=json.loads(open('timings.js').read()[len('window.T='):-1])
n=int(round(T['total']*30))
frames=[int(x) for x in sys.argv[2:]] if len(sys.argv)>2 else range(n)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1080,'height':1920})
    errs=[]; pg.on('pageerror',lambda e: errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
    pg.goto('file://'+os.path.abspath('reel.html')); pg.evaluate("document.fonts.ready"); pg.wait_for_timeout(2500)
    print('fonts', pg.evaluate("[document.fonts.check('900 40px Archivo'),document.fonts.check('400 20px Arimo')]"))
    for i in frames:
        pg.evaluate(f"render({i/30})")
        pg.screenshot(path=f"{out}/f{i:04d}.jpg",type='jpeg',quality=93)
    print('errors',errs[:5]); print('frames',n)
    b.close()
