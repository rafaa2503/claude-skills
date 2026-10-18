<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="14.4" data-width="1080" data-height="1920">
 <audio id="mus" src="assets/audio.mp3" data-start="0" data-duration="14.4" data-track-index="9" data-volume="1"></audio>
 <div class="clip abs" data-start="0" data-duration="14.4" data-track-index="0" style="left:0;top:0;width:1080px;height:1920px">

  <div id="L_g" class="layer">
   <div class="abs" id="tm" style="left:100px;top:760px;width:880px;text-align:center;font-weight:800;font-size:260px;line-height:1;font-variant-numeric:tabular-nums">0,0 s</div>
   <div class="abs" style="left:100px;top:1100px;width:880px;height:70px;border-radius:35px;background:#1b1f26"><div id="bar" style="width:0;height:70px;border-radius:35px;background:#2fd47a"></div></div>
   <div class="abs" style="left:@@M1@@px;top:1070px;width:6px;height:130px;background:#fff"></div>
   <div class="abs" style="left:@@M2@@px;top:1210px;width:260px;text-align:center;font-size:34px;font-weight:700;color:#fff">2,5 s</div>
   <div class="bx" style="top:1640px;font-size:30px">Google empfiehlt: unter 2,5 Sekunden · Zeitanzeige als Beispiel</div>
  </div>

  <div id="L_cta" class="layer">
   <img id="ic" src="assets/icon-crop.png" class="abs" style="left:449px;top:700px;height:230px;filter:drop-shadow(0 0 22px rgba(255,159,28,.5))">
   <div id="ur" class="abs" style="left:0;top:950px;width:1080px;text-align:center;font-weight:800;font-size:112px;line-height:1.1">sherka<span style="color:var(--or)">.ch</span></div>
   <div id="btn" class="abs" style="left:90px;top:1140px;width:900px;height:170px;border-radius:85px;background:#0a6fe0;box-shadow:0 14px 0 #064ea0;font-weight:800;font-size:56px;display:flex;align-items:center;justify-content:center;letter-spacing:1px">GRATIS ERSTGESPRÄCH</div>
   <div id="arr" class="abs" style="left:0;top:1350px;width:1080px;text-align:center;font-size:150px;font-weight:800;color:var(--or);line-height:1">↓</div>
   <div id="sub" class="abs" style="left:0;top:1540px;width:1080px;text-align:center;font-size:44px;font-weight:700;color:var(--g)">Antwort innert eines Werktags</div>
  </div>

  <div id="caps"></div>
  <div id="red"></div><div id="flash"></div>
 </div>
</div>
<script>
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
const $=s=>document.querySelector(s);
const T=14.4;
const WIN=[['#L_g',4.45,8.33],['#L_cta',12.78,T]];
WIN.forEach(([s,a,b])=>{tl.set(s,{display:'block'},a);if(b<T)tl.set(s,{display:'none'},b)});
const P=[
 ['Deine Website<br><u>kostet Geld</u>',0.18,1.66],
 ['Handy<br>geöffnet',1.68,2.9],['<u>Weggeklickt</u>',2.92,4.43],
 ['Google:',4.45,5.08],['<em>2,5</em> Sek.',5.10,6.78],
 ['Alles darüber:<br><u>zu langsam</u>',6.80,8.31],
 ['Wir bauen<br>Seiten die<br><em>arbeiten</em>',8.33,10.18],
 ['Ohne<br><em>Blabla</em>',10.20,11.53],
 ['<em>Erstgespräch</em><br>gratis',11.55,12.76],
 ['Link in<br>der <em>Bio</em>',12.78,T]];
const caps=$('#caps');tl.set(caps,{y:480},0).set(caps,{y:0},4.45).set(caps,{y:480},8.33).set(caps,{y:0},12.78);
P.forEach(([h,a,b],i)=>{
  const d=document.createElement('div');d.className='cap';d.innerHTML='<div>'+h+'</div>';
  const longest=Math.max(...h.split('<br>').map(x=>x.replace(/<[^>]+>/g,'').length));
  d.style.fontSize=Math.min(170,Math.floor(940/(longest*0.7)))+'px';
  caps.appendChild(d);
  tl.set(d,{opacity:1},a).fromTo(d,{scale:1.35,rotation:(i%2?-2:2)},{scale:1,rotation:0,duration:.14,ease:'power3.out'},a);
  if(b<T)tl.set(d,{opacity:0},b);
  tl.fromTo('#flash',{opacity:.2},{opacity:0,duration:.1},a);
});
tl.set('#red',{opacity:.5},0.18).to('#red',{opacity:0,duration:.25},0.2);
tl.to('#red',{opacity:.3,duration:.05},6.80).to('#red',{opacity:0,duration:.3},6.85);
const o={v:0};
tl.to(o,{v:4.1,duration:3.85,ease:'none',onUpdate:()=>{
  $('#tm').textContent=o.v.toFixed(1).replace('.',',')+' s';
  $('#bar').style.width=(o.v/4.2*880)+'px';
  const bad=o.v>2.5;$('#bar').style.background=bad?'#ff2d3d':'#2fd47a';$('#tm').style.color=bad?'#ff2d3d':'#fff';}},4.45);
tl.from('#ic',{scale:0,duration:.35,ease:'back.out(2)',transformOrigin:'50% 50%'},12.8).from('#ur',{clipPath:'inset(-20px 100% -20px 0)',duration:.3},13.0);
tl.from('#btn',{scale:0,duration:.3,ease:'back.out(2)'},13.1).to('#btn',{scale:1.05,duration:.2,yoyo:true,repeat:5,ease:'sine.inOut'},13.5);
tl.to('#arr',{y:26,duration:.22,yoyo:true,repeat:6,ease:'power1.inOut'},13.1).from('#sub',{opacity:0,duration:.3},13.3);
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body></html>
