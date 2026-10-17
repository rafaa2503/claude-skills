// Nutzung: node capture.js scene.html out.mp4 [fps=30] [dauer=4] [audio.wav]
// Playwright setzt die Zeit Bild für Bild (window.renderAt(t)), ffmpeg baut den H.264-MP4. Nur vorwärts rendern (Physik).
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const { spawn } = require('child_process');
const path = require('path');
const http = require('http'), fs = require('fs');
const MIME = { '.html':'text/html', '.js':'text/javascript', '.png':'image/png', '.jpg':'image/jpeg', '.wav':'audio/wav', '.json':'application/json' };
function serve(dir){ return new Promise(res => { const srv = http.createServer((q, r) => { const p = path.join(dir, decodeURIComponent(q.url.split('?')[0])); fs.readFile(p, (e, d) => { if (e) { r.writeHead(404); r.end(); } else { r.writeHead(200, { 'content-type': MIME[path.extname(p)] || 'application/octet-stream' }); r.end(d); } }); }).listen(0, () => res(srv)); }); }
const [,, scene, out, fpsA, durA, audio] = process.argv;
const fps = +(fpsA || 30), dur = +(durA || 4), n = Math.round(fps * dur);
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const pg = await (await b.newContext({ viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1 })).newPage();
  const srv = await serve(path.dirname(path.resolve(scene)));
  await pg.goto('http://127.0.0.1:' + srv.address().port + '/' + path.basename(scene));
  await pg.evaluate(() => document.fonts.ready);
  await pg.waitForFunction(() => window.READY === undefined || window.READY === true, null, { timeout: 60000 });
  const args = ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'png', '-i', '-'];
  if (audio) args.push('-i', audio);
  args.push('-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', '-preset', 'medium');
  if (audio) args.push('-c:a', 'aac', '-b:a', '192k', '-shortest');
  args.push('-movflags', '+faststart', out);
  const ff = spawn('ffmpeg', args, { stdio: ['pipe', 'inherit', 'inherit'] });
  for (let i = 0; i < n; i++) {
    await pg.evaluate(t => window.renderAt(t), i / fps);
    const png = await pg.screenshot({ type: 'png' });
    if (!ff.stdin.write(png)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 30 === 0) console.log(i, '/', n);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r)); await b.close(); srv.close(); console.log('fertig', out);
})();
