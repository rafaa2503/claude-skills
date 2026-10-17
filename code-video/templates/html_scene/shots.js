// Nutzung: node shots.js scene.html t1 t2 ...  -> /tmp/shot_<t>.png (Physik läuft vorwärts bis zur letzten Zeit)
const { chromium } = require('/opt/node-tools/node_modules/playwright'); const path = require('path');
const [,, scene, ...ts] = process.argv; const want = ts.map(Number).sort((a, b) => a - b);
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const pg = await (await b.newContext({ viewport: { width: 1080, height: 1920 } })).newPage();
  pg.on('pageerror', e => console.log('PAGEERROR', e.message)); pg.on('console', m => m.type() === 'error' && console.log('CONSOLE', m.text()));
  await pg.goto('file://' + path.resolve(scene)); await pg.evaluate(() => document.fonts.ready);
  const fps = 30, last = Math.max(...want); let wi = 0;
  for (let i = 0; i <= Math.round(last * fps) && wi < want.length; i++) {
    const t = i / fps; await pg.evaluate(t => window.renderAt(t), t);
    if (t >= want[wi] - 1e-6) { await pg.screenshot({ path: `/tmp/shot_${want[wi]}.png` }); wi++; }
  }
  await b.close();
})();
