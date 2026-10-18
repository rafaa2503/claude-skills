<body>
<div id="root" data-composition-id="main" data-start="0" data-duration="13.6" data-width="1080" data-height="1920">
 <audio id="mus" src="assets/audio.mp3" data-start="0" data-duration="13.6" data-track-index="9" data-volume="1"></audio>
 <div class="clip abs" data-start="0" data-duration="13.6" data-track-index="0" style="left:0;top:0;width:1080px;height:1920px">
  <div id="glow" class="abs" style="left:0;top:0;width:1080px;height:1920px;background:radial-gradient(ellipse at 50% 50%,rgba(255,45,61,.22),rgba(0,0,0,0) 62%);opacity:.0"></div>
  <div id="logo" class="abs" style="left:0;top:1480px;width:1080px;text-align:center;opacity:0"><img src="assets/icon-crop.png" style="height:120px;filter:drop-shadow(0 0 18px rgba(255,159,28,.5))"><div style="font-weight:800;font-size:56px;margin-top:6px">sherka<span style="color:var(--or)">.ch</span></div></div>
  <div id="sub" class="abs" style="left:0;top:1230px;width:1080px;text-align:center;font-weight:700;font-size:54px;color:var(--g);opacity:0">in die Kommentare</div>
  <div id="caps"></div>
  <div id="red"></div><div id="flash"></div>
 </div>
</div>
<script>
window.__timelines = window.__timelines || {};
const tl = gsap.timeline({ paused: true });
const $=s=>document.querySelector(s);
const T=13.6;
const P=[
 ['Du bist<br>der <em>Beste</em>',0.10,0.88],['in deinem<br>Job',0.90,1.80],
 ['Und gehst<br>trotzdem',1.82,2.72],['<u>unter</u>',2.74,3.28],
 ['Weil der<br><em>Lauteste</em>',3.30,4.14],['gewinnt',4.16,4.74],
 ['Nicht der<br>Beste',4.76,5.74],['Qualität<br>spricht<br>sich rum?',5.76,7.12],
 ['<u>NEIN.</u>',7.14,7.74],
 ['Wer nicht<br>gefunden<br>wird',7.76,8.92],['existiert<br><u>nicht</u>',8.94,10.00],
 ['Wie viel<br>hat dich<br>das gekostet?',10.02,11.66],['Schreib',11.68,12.20],['<em>SICHTBAR</em>',12.22,T]];
const caps=$('#caps');tl.set(caps,{y:480},0);
P.forEach(([h,a,b],i)=>{
  const d=document.createElement('div');d.className='cap';d.innerHTML='<div>'+h+'</div>';
  const longest=Math.max(...h.split('<br>').map(x=>x.replace(/<[^>]+>/g,'').length));
  d.style.fontSize=Math.min(i==8?260:170,Math.floor(940/(longest*0.7)))+'px';
  caps.appendChild(d);
  tl.set(d,{opacity:1},a).fromTo(d,{scale:1.35,rotation:(i%2?-2:2)},{scale:1,rotation:0,duration:.14,ease:'power3.out'},a);
  if(b<T)tl.set(d,{opacity:0},b);
  tl.fromTo('#flash',{opacity:.16},{opacity:0,duration:.1},a);
});
// unter: Wort sinkt ab
tl.to(caps.children[3],{y:90,duration:.5,ease:'power2.in'},2.78);
// NEIN: roter Einschlag + Zittern
tl.set('#red',{opacity:.75},7.14).to('#red',{opacity:0,duration:.5},7.16);
tl.fromTo(caps.children[8],{x:-14},{x:14,duration:.05,yoyo:true,repeat:9,ease:'none'},7.16);
// Stimmung: Glow steigt, pulst
tl.to('#glow',{opacity:.9,duration:6,ease:'none'},0.1).to('#glow',{opacity:.35,duration:.4},7.14);
tl.to('#glow',{opacity:.7,duration:.43,yoyo:true,repeat:25,ease:'sine.inOut'},7.6);
// SICHTBAR + Logo
tl.to('#sub',{opacity:1,duration:.3},12.7);tl.to('#logo',{opacity:1,duration:.4},13.0);
tl.fromTo(caps.children[13],{textShadow:'0 6px 0 rgba(0,0,0,.55)'},{textShadow:'0 0 60px rgba(255,159,28,.8)',duration:.5,yoyo:true,repeat:2},12.3);
window.__timelines["main"] = tl;
tl.seek(0);
</script>
</body></html>
