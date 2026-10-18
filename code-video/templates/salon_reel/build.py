# "22:47" Cartoon-Reel (16 s, ohne Stimme): Salonbesitzerin nachts mit Nachrichten-Blasen. SVG-Cartoon + GSAP (HyperFrames), weicher Pluck-Sound.
import subprocess, wave, numpy as np
T=16.0
html='''<!doctype html><html lang="de" data-resolution="portrait"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#000}
#root{position:relative;width:1080px;height:1920px;font-family:Inter,system-ui,sans-serif;color:#fff;overflow:hidden;background:#2a2150}
.abs{position:absolute}
#bgN{position:absolute;inset:0;background:linear-gradient(180deg,#1e1840 0%,#3d2f73 55%,#5a3f86 100%)}
#bgD{position:absolute;inset:0;background:linear-gradient(180deg,#ffd9e4 0%,#ffe9d6 55%,#fff3e6 100%);opacity:0}
.star{position:absolute;width:8px;height:8px;border-radius:50%;background:#fff;opacity:.7}
.cap{position:absolute;left:0;width:1080px;text-align:center;font-weight:900;line-height:1.05;letter-spacing:-1px;opacity:0;text-shadow:0 6px 0 rgba(0,0,0,.18)}
.cap em{font-style:normal;color:#ffd166}.cap u{text-decoration:none;color:#ff8fb1}
.bub{position:absolute;background:#fff;color:#3b2a3f;font-weight:800;border-radius:34px 34px 34px 8px;padding:22px 30px;box-shadow:0 10px 0 rgba(0,0,0,.14);opacity:0;transform-origin:20% 100%}
.mini{position:absolute;background:#fff;border-radius:30px 30px 30px 8px;opacity:0;box-shadow:0 8px 0 rgba(0,0,0,.14);display:flex;align-items:center;justify-content:center;font-weight:900;color:#ff6b9a}
#badge{position:absolute;left:560px;top:1170px;width:112px;height:112px;border-radius:50%;background:#ff4d6d;font-weight:900;font-size:60px;display:flex;align-items:center;justify-content:center;box-shadow:0 8px 0 rgba(0,0,0,.2);opacity:0}
#logo{position:absolute;left:0;top:1620px;width:1080px;text-align:center;opacity:0;color:#3b2a3f}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="16" data-width="1080" data-height="1920">
<audio id="mus" src="assets/audio.mp3" data-start="0" data-duration="16" data-track-index="9" data-volume="1"></audio>
<div class="clip abs" data-start="0" data-duration="16" data-track-index="0" style="left:0;top:0;width:1080px;height:1920px">
<div id="bgN"></div><div id="bgD"></div><div id="stars"></div>
<svg id="moon" class="abs" style="left:780px;top:140px" width="200" height="200" viewBox="0 0 200 200"><circle cx="100" cy="100" r="80" fill="#fff3cf"/><circle cx="130" cy="80" r="14" fill="#f4e0a8"/><circle cx="80" cy="125" r="18" fill="#f4e0a8"/><circle cx="118" cy="132" r="9" fill="#f4e0a8"/></svg>
<div id="clock" class="abs" style="left:0;top:660px;width:1080px;text-align:center;font-weight:900;font-size:330px;letter-spacing:-8px;opacity:0;text-shadow:0 12px 0 rgba(0,0,0,.25)">22<span id="cc">:</span>47</div>
<div id="sign" class="abs" style="left:340px;top:380px;width:400px;height:150px;opacity:0;transform-origin:50% 0"><div class="abs" style="left:198px;top:-300px;width:4px;height:300px;background:#cfc3f5"></div><div class="abs" style="left:0;top:0;width:400px;height:150px;border-radius:30px;background:#ffd166;color:#3b2a3f;font-weight:900;font-size:56px;display:flex;align-items:center;justify-content:center;box-shadow:0 10px 0 rgba(0,0,0,.2)">Geschlossen</div></div>
<div id="c1" class="cap" style="top:820px;font-size:150px">Dein Laden<br><u>ist zu.</u></div>
<div id="c2" class="cap" style="top:330px;font-size:150px">Dein Handy<br><em>nicht.</em></div>
<div id="c3" class="cap" style="top:330px;font-size:104px">Du liebst deinen<br>Laden.</div>
<div id="c4" class="cap" style="top:330px;font-size:120px">Nur nicht<br><u>das hier.</u></div>
<div id="c5" class="cap" style="top:330px;font-size:116px;color:#3b2a3f;text-shadow:none">Das ist nicht<br><span style="color:#ff6b9a">dein Fehler.</span></div>
<div id="c6" class="cap" style="top:290px;font-size:104px;color:#3b2a3f;text-shadow:none">Schreib mir:<br><span style="color:#ff6b9a">Wie viele sind<br>es heute?</span></div>
<!-- Figur -->
<svg id="girl" class="abs" style="left:240px;top:760px" width="600" height="700" viewBox="0 0 600 700">
 <rect x="10" y="400" width="580" height="290" rx="70" fill="#8b78c9"/><rect x="40" y="350" width="520" height="170" rx="80" fill="#a592dd"/>
 <g id="body"><rect x="170" y="330" width="260" height="300" rx="100" fill="#ff8fb1"/>
  <g id="head"><circle cx="300" cy="225" r="122" fill="#3b2a3f"/><circle cx="300" cy="92" r="56" fill="#3b2a3f"/>
   <circle cx="300" cy="238" r="102" fill="#f7c8a8"/>
   <path d="M196 222 Q205 118 300 120 Q395 118 404 222 Q350 160 300 176 Q250 160 196 222Z" fill="#3b2a3f"/>
   <g id="eyes"><ellipse cx="258" cy="246" rx="19" ry="25" fill="#fff"/><ellipse cx="342" cy="246" rx="19" ry="25" fill="#fff"/><circle id="p1" cx="258" cy="250" r="11" fill="#3b2a3f"/><circle id="p2" cx="342" cy="250" r="11" fill="#3b2a3f"/></g>
   <g id="lids" style="opacity:0"><path d="M236 240 Q258 214 280 240 Z" fill="#f7c8a8"/><path d="M320 240 Q342 214 364 240 Z" fill="#f7c8a8"/></g>
   <g id="bags" style="opacity:0" stroke="#c9a0d8" stroke-width="5" fill="none" stroke-linecap="round"><path d="M240 280 Q258 292 276 280"/><path d="M324 280 Q342 292 360 280"/></g>
   <g stroke="#3b2a3f" stroke-width="7" stroke-linecap="round" fill="none"><path id="b1" d="M236 205 Q258 192 280 205"/><path id="b2" d="M320 205 Q342 192 364 205"/></g>
   <circle cx="226" cy="290" r="16" fill="#ff9db8" opacity=".55"/><circle cx="374" cy="290" r="16" fill="#ff9db8" opacity=".55"/>
   <path id="m0" d="M278 306 Q300 316 322 306" stroke="#b5485f" stroke-width="7" fill="none" stroke-linecap="round"/>
   <path id="m1" d="M276 318 Q300 296 324 318" stroke="#b5485f" stroke-width="7" fill="none" stroke-linecap="round" style="opacity:0"/>
   <path id="m2" d="M270 300 Q300 340 330 300 Z" fill="#b5485f" style="opacity:0"/>
   <path id="sw" d="M398 180 Q412 206 398 220 Q384 206 398 180Z" fill="#8fd3ff" style="opacity:0"/>
  </g>
  <path d="M190 400 Q170 470 262 520" stroke="#ff8fb1" stroke-width="58" fill="none" stroke-linecap="round"/><path d="M410 400 Q430 470 338 520" stroke="#ff8fb1" stroke-width="58" fill="none" stroke-linecap="round"/>
  <g id="phone"><rect x="228" y="450" width="144" height="210" rx="26" fill="#2b2b3d"/><rect id="scr" x="238" y="462" width="124" height="186" rx="18" fill="#bfe3ff"/><circle cx="300" cy="545" r="46" fill="#fff" opacity=".35"/></g>
  <circle cx="246" cy="520" r="24" fill="#f7c8a8"/><circle cx="354" cy="520" r="24" fill="#f7c8a8"/>
 </g>
</svg>
<div id="glow" class="abs" style="left:240px;top:1130px;width:600px;height:500px;background:radial-gradient(circle,rgba(160,220,255,.45),rgba(0,0,0,0) 60%);opacity:0"></div>
<div id="bubs"></div>
<div id="badge">0</div>
<div id="hearts"></div>
<div id="logo"><div style="display:inline-block;background:#2a2150;border-radius:44px;padding:18px 46px 16px;color:#fff"><img src="assets/icon-crop.png" style="height:90px"><div style="font-weight:900;font-size:48px;margin-top:2px">sherka<span style="color:#ff9f1c">.ch</span></div></div></div>
</div></div>
<script>
window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});const $=s=>document.querySelector(s);
// Sterne
const st=$('#stars');for(let i=0;i<40;i++){const s=document.createElement('div');s.className='star';s.style.left=(Math.abs(Math.sin(i*12.9)*1080))+'px';s.style.top=(Math.abs(Math.sin(i*7.7)*900))+'px';s.style.opacity=.3+Math.abs(Math.sin(i*3.1))*.6;s.style.transform='scale('+(.5+Math.abs(Math.sin(i*5.3))*1.1)+')';st.appendChild(s);}
tl.to('#stars',{opacity:.25,duration:.8,yoyo:true,repeat:14,ease:'sine.inOut'},0);
// Uhr
tl.set('#clock',{opacity:1},0).fromTo('#clock',{scale:.4},{scale:1,duration:.5,ease:'elastic.out(1,.5)',transformOrigin:'50% 50%'},0);
tl.to('#cc',{opacity:0,duration:.01,repeat:4,yoyo:true,repeatDelay:.24},0.3);
tl.to('#clock',{y:-560,scale:.4,duration:.5,ease:'power3.inOut'},1.1).to('#clock',{opacity:0,duration:.3},2.2);
// Schild
tl.set('#sign',{opacity:1},1.2).fromTo('#sign',{y:-500,rotation:-18},{y:0,rotation:0,duration:.6,ease:'bounce.out'},1.2).to('#sign',{rotation:6,duration:.35,yoyo:true,repeat:3,ease:'sine.inOut'},1.8);
tl.set('#sign',{opacity:0},2.35);
function cap(id,a,b,y0){const e=$(id);tl.set(e,{opacity:1},a).fromTo(e,{scale:.6,y:30},{scale:1,y:0,duration:.45,ease:'elastic.out(1,.55)',transformOrigin:'50% 50%'},a).set(e,{opacity:0},b);}
cap('#c1',1.3,2.35);cap('#c2',2.4,3.3);cap('#c3',7.9,9.1);cap('#c4',9.2,10.7);cap('#c5',10.8,12.9);cap('#c6',13.0,16.0);
// Figur kommt rein
tl.fromTo('#girl',{y:700,opacity:0},{y:0,opacity:1,duration:.7,ease:'back.out(1.4)'},2.4);
tl.fromTo('#body',{scaleY:1},{scaleY:1.02,duration:1.4,yoyo:true,repeat:10,ease:'sine.inOut',transformOrigin:'50% 100%'},3);
tl.fromTo('#phone',{x:-5},{x:5,duration:.05,yoyo:true,repeat:11,ease:'none'},2.6);
tl.set('#glow',{opacity:1},2.6);tl.to('#glow',{opacity:.55,duration:.5,yoyo:true,repeat:12,ease:'sine.inOut'},2.8);
// Blinzeln
[3.1,6.2,9.6,12.4].forEach(t=>tl.to('#eyes',{scaleY:.08,duration:.07,yoyo:true,repeat:1,transformOrigin:'50% 50%'},t));
// Ausdruck: Stress -> müde -> Erleichterung
tl.set('#m0',{opacity:0},3.6).set('#m2',{opacity:1},3.6).set('#m2',{opacity:0},5.6).set('#m1',{opacity:1},5.6).set('#m1',{opacity:0},10.9).set('#m0',{opacity:1},5.6).set('#m0',{opacity:0},5.6);
tl.set('#sw',{opacity:1},4.4).to('#sw',{y:30,duration:.7,repeat:5},4.4).set('#sw',{opacity:0},8.6);
tl.set('#lids',{opacity:1},6.6).set('#bags',{opacity:1},6.6).set('#lids',{opacity:0},10.9).set('#bags',{opacity:0},10.9);
tl.to('#b1',{attr:{d:'M236 198 Q258 212 280 206'},duration:.3},6.6).to('#b2',{attr:{d:'M320 206 Q342 212 364 198'},duration:.3},6.6);
tl.to('#b1',{attr:{d:'M236 205 Q258 192 280 205'},duration:.3},10.9).to('#b2',{attr:{d:'M320 205 Q342 192 364 205'},duration:.3},10.9);
// Nachrichten-Blasen (Text) + Mini-Blasen
const B=[['Habt ihr morgen<br>noch was frei?',3.5,60,700,38],['Was kosten<br>Strähnen?',4.1,560,640,38],['Seid ihr<br>heute offen?',4.7,70,1000,38]];
const M=[['?',5.3,700,860,86,86],['…',5.6,430,660,120,76],['Hallo?',5.9,720,1050,200,84],['!!',6.2,70,1230,110,80],['…',6.5,780,760,120,76],['?',6.8,180,1150,86,86],['Preis?',7.1,50,1340,190,84],['…',7.4,780,1240,120,76]];
const bubs=$('#bubs');
B.forEach(([h,t,x,y,fs],i)=>{const d=document.createElement('div');d.className='bub';d.style.left=x+'px';d.style.top=y+'px';d.style.fontSize=fs+'px';d.innerHTML=h;bubs.appendChild(d);
 tl.fromTo(d,{opacity:0,scale:0,x:300-x,y:1250-y},{opacity:1,scale:1,x:0,y:0,duration:.55,ease:'elastic.out(1,.6)'},t).to(d,{y:-12,duration:1.1,yoyo:true,repeat:8,ease:'sine.inOut'},t+.6);});
const mb=[];M.forEach(([h,t,x,y,w,hh],i)=>{const d=document.createElement('div');d.className='mini';d.style.cssText+=`left:${x}px;top:${y}px;width:${w}px;height:${hh}px;font-size:44px`;d.textContent=h;bubs.appendChild(d);mb.push(d);
 tl.fromTo(d,{opacity:0,scale:0,x:300-x+120,y:1300-y},{opacity:1,scale:1,x:0,y:0,duration:.45,ease:'elastic.out(1,.6)'},t).to(d,{y:-10,duration:.9,yoyo:true,repeat:6,ease:'sine.inOut'},t+.5);});
const all=[...bubs.children];
// Abzeichen zählt hoch
const bg={n:0};tl.set('#badge',{opacity:1},3.4).fromTo('#badge',{scale:0},{scale:1,duration:.4,ease:'elastic.out(1,.5)'},3.4);
tl.to(bg,{n:27,duration:4.2,ease:'power1.in',onUpdate:()=>{$('#badge').textContent=Math.round(bg.n)}},3.5);
tl.to('#badge',{scale:1.18,duration:.25,yoyo:true,repeat:15,ease:'sine.inOut'},3.9);
// Gedränge: Blasen zittern bei "Nur nicht das hier"
tl.to(all,{rotation:3,duration:.07,yoyo:true,repeat:11,ease:'none',stagger:.01},9.2);
// Erleichterung: Blasen platzen / schweben weg, Hintergrund wird hell
tl.to(all,{y:-1200,opacity:0,scale:.4,duration:.9,ease:'power2.in',stagger:.07},10.8);
tl.to('#badge',{scale:0,duration:.35,ease:'back.in(2)'},10.9);
tl.to('#bgD',{opacity:1,duration:1.4},10.9).to(['#stars','#moon'],{opacity:0,duration:.8},10.9);
tl.to('#glow',{opacity:0,duration:.6},11.0);
// Herzchen
const hr=$('#hearts');for(let i=0;i<9;i++){const h=document.createElement('div');h.textContent='♥';h.style.cssText=`position:absolute;left:${300+ (i*53)%420}px;top:1250px;font-size:${50+(i%3)*22}px;color:#ff6b9a;opacity:0`;hr.appendChild(h);
 tl.fromTo(h,{y:0,opacity:0,scale:.3},{y:-420-(i%4)*70,opacity:1,scale:1,duration:1.4,ease:'power1.out'},11.4+i*.14).to(h,{opacity:0,duration:.4},12.6+i*.14);}
// Logo + CTA-Pfeil
tl.to('#logo',{opacity:1,duration:.6},14.2);
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(html)
# ---- Ton ----
SR=44100;n=int(SR*T);L=np.zeros(n)
def put(x,t,g=1.0):
    s=int(t*SR)
    if s<n: x=x[:n-s]*g; L[s:s+len(x)]+=x
def pluck(f,d=0.7,g=0.3):
    t=np.arange(int(d*SR))/SR;return (np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*2*f*t)+0.12*np.sin(2*np.pi*3*f*t))*np.exp(-t*6)*g
def load(f,dur=None,lp=None):
    af=["-af",f"lowpass=f={lp}"] if lp else []
    c=["ffmpeg","-v","error","-i",f]+(["-t",str(dur)] if dur else [])+af+["-ac","1","-ar",str(SR),"-f","f32le","-"]
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,dtype=np.float32).astype(np.float64)
click=load('sfx/click.mp3',0.12,4500);chime=load('sfx/chime.mp3',1.0,6000)
t=np.arange(n)/SR
def chord(fs,g): return sum(np.sin(2*np.pi*f*t) for f in fs)*g
dawn=np.clip((t-10.8)/1.5,0,1)
pad=(chord([130.8,196.0,246.9,329.6],0.012)*(1-dawn)+chord([130.8,164.8,196.0,261.6,329.6],0.014)*dawn)*np.minimum(1,t/1.5)*np.minimum(1,(T-t)/1.2)
L+=pad
for tt in [0.35,0.6,0.85,1.1]: put(click,tt,0.4)          # Uhr tickt
put(click,1.3,0.9);put(pluck(196,0.8,0.3),1.8,0.8)        # Schild fällt
put(load('sfx/click.mp3',0.5,3000),2.4,0.6)
buz=np.sin(2*np.pi*170*t[:int(0.8*SR)])*(0.5+0.5*np.sin(2*np.pi*22*t[:int(0.8*SR)]))*0.12;put(buz,2.6)
scale=[523,587,659,784,880,1047,880,784,659,587,523,659]
times=[3.5,4.1,4.7,5.3,5.6,5.9,6.2,6.5,6.8,7.1,7.4,7.7]
for i,tt in enumerate(times): put(pluck(scale[i],0.6,0.3),tt)
# Erleichterung: aufsteigende Funkel-Töne
for i,f in enumerate([523,659,784,1047,1319,1568,2093]): put(pluck(f,1.0,0.22),10.8+i*0.12)
put(chime,11.9,0.35);put(chime,13.0,0.4);put(pluck(1047,1.2,0.25),14.2)
mix=np.stack([L,L],1);mix[-int(0.5*SR):]*=np.linspace(1,0,int(0.5*SR))[:,None];mix=mix/np.max(np.abs(mix))*0.9
with wave.open('mix.wav','wb') as w: w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype('<i2').tobytes())
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","mix.wav","-af","loudnorm=I=-14:TP=-1.5:LRA=9","-ar","44100","-c:a","libmp3lame","-b:a","192k","hf/assets/audio.mp3"])
import os;os.remove('mix.wav');print('fertig')
