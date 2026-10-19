import sys,os
from playwright.sync_api import sync_playwright
out=sys.argv[1]; os.makedirs(out,exist_ok=True)
frames=[int(x) for x in sys.argv[2:]] if len(sys.argv)>2 else range(510)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome',args=['--no-sandbox'])
    pg=b.new_page(viewport={'width':1080,'height':1920})
    pg.goto('file://'+os.path.abspath('reel.html')); pg.wait_for_timeout(2500)
    print(pg.evaluate("document.fonts.check('800 20px Archivo')"))
    for i in frames:
        pg.evaluate(f"render({i/30})")
        pg.screenshot(path=f"{out}/f{i:04d}.jpg",type='jpeg',quality=92)
    b.close()
