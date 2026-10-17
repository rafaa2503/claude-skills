const { chromium } = require('/opt/node-tools/node_modules/playwright');
(async()=>{
  const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
  const ctx = await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,hasTouch:true,locale:'de-CH',extraHTTPHeaders:{'Accept-Language':'de-CH,de;q=0.9'}});
  const pg = await ctx.newPage();
  await pg.goto('https://bledi-bienne.ch',{waitUntil:'networkidle',timeout:45000}); await pg.waitForTimeout(2500);
  await pg.screenshot({path:'hf/assets/bledi-mobile.png'});
  const info = await pg.evaluate(()=>{
    const out=[];for(const e of document.querySelectorAll('a,button')){const r=e.getBoundingClientRect();const t=(e.innerText||e.getAttribute('aria-label')||'').trim();
      if(r.width>0&&r.top>=0&&r.bottom<=innerHeight&&t&&t.length<30)out.push({t,x:Math.round(r.x),y:Math.round(r.y),w:Math.round(r.width),h:Math.round(r.height)})}
    return {lang:document.documentElement.lang,title:document.title,btns:out}});
  console.log(JSON.stringify(info,null,1));
  await b.close();
})();
