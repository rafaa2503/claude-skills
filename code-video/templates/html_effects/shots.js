// Nutzung: node shots.js scene.html t1 t2 ...  -> /tmp/shot_<t>.png (Physik läuft vorwärts bis zur letzten Zeit)
const { chromium } = require('/opt/node-tools/node_modules/playwright'); const path = require('path');
const http = require('http'), fs = require('fs');
const MIME = { '.html':'text/html', '.js':'text/javascript', '.png':'image/png', '.jpg':'image/jpeg', '.wav':'audio/wav', '.json':'application/json' };
function serve(dir){ return new Promise(res => { const srv = http.createServer((q, r) => { const p = path.join(dir, decodeURIComponent(q.url.split('?')[0])); fs.readFile(p, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': MIME[path.extname(p)] || 'application/octet-stream' }); r.end(d); } }); }).listen(0, () => res(srv)); }); }
const [,, scene, ...ts] = process.argv; const want = ts.map(Number).sort((a, b) => a - b);
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pg = await (await b.newContext({ viewport: { width: 1080, height: 1920 } })).newPage();
  pg.on('pageerror', e => console.log('PAGEERROR', e.message)); pg.on('console', m => m.type() === 'error' && console.log('CONSOLE', m.text()));
  const srv = await serve(path.dirname(path.resolve(scene)));
  await pg.goto('http://127.0.0.1:' + srv.address().port + '/' + path.basename(scene)); await pg.evaluate(() => document.fonts.ready);
  await pg.waitForFunction(() => window.READY === undefined || window.READY === true, null, { timeout: 60000 });
  const fps = 30, last = Math.max(...want); let wi = 0;
  for (let i = 0; i <= Math.round(last * fps) && wi < want.length; i++) {
    const t = i / fps; await pg.evaluate(t => window.renderAt(t), t);
    if (t >= want[wi] - 1e-6) { await pg.screenshot({ path: `/tmp/shot_${want[wi]}.png` }); wi++; }
  }
  await b.close(); srv.close();
})();
