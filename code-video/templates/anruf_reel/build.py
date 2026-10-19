# "Verpasster Anruf" (18.5 s, ohne Stimme): Maler auf der Leiter verpasst Auftrag. Cartoon-SVG + GSAP (HyperFrames), Klingelton/Tipp-Sounds synthetisch.
import subprocess, wave, numpy as np, os
T=18.5
html='''<!doctype html><html lang="de" data-resolution="portrait"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script><style>
*{margin:0;padding:0;box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#000}
:root{--ink:#0f1115;--bone:#f2efe8;--amb:#ffb020;--dim:#8c8a84}
#root{position:relative;width:1080px;height:1920px;font-family:Inter,system-ui,sans-serif;color:var(--bone);background:var(--ink);overflow:hidden}
.abs{position:absolute}.L{position:absolute;left:0;top:0;width:1080px;height:1920px;display:none;overflow:hidden}
.cap{position:absolute;left:60px;width:960px;text-align:center;font-weight:800;line-height:1.06;letter-spacing:-1.5px}
.chip{position:absolute;left:0;width:1080px;text-align:center}.chip span{display:inline-block;background:#1a1d23;border:3px solid var(--amb);color:var(--amb);font-weight:800;font-size:52px;padding:14px 38px;border-radius:50px;font-variant-numeric:tabular-nums}
.btn{position:absolute;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:60px}
.bub{position:absolute;border-radius:30px;padding:24px 32px;font-size:40px;font-weight:600;line-height:1.2}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="18.5" data-width="1080" data-height="1920">
<audio id="mus" src="assets/audio.mp3" data-start="0" data-duration="18.5" data-track-index="9" data-volume="1"></audio>
<div class="clip abs" data-start="0" data-duration="18.5" data-track-index="0" style="left:0;top:0;width:1080px;height:1920px">

<!-- S1 Anruf -->
<div id="S1" class="L"><div id="cw" class="abs" style="left:0;top:0;width:1080px;height:1920px;background:linear-gradient(180deg,#171a20,#0f1115)">
 <div class="abs" style="left:0;top:210px;width:1080px;text-align:center;font-size:44px;color:var(--dim);font-weight:600">Eingehender Anruf</div>
 <div class="abs" id="rg1" style="left:340px;top:330px;width:400px;height:400px;border-radius:50%;border:4px solid #3a3d44"></div>
 <div class="abs" id="rg2" style="left:340px;top:330px;width:400px;height:400px;border-radius:50%;border:4px solid #3a3d44"></div>
 <div class="abs" style="left:390px;top:380px;width:300px;height:300px;border-radius:50%;background:#2a2d34;display:flex;align-items:center;justify-content:center;font-size:120px;font-weight:800;color:var(--dim)">FK</div>
 <div class="abs" style="left:0;top:790px;width:1080px;text-align:center;font-size:120px;font-weight:800;letter-spacing:-3px">Frau Keller</div>
 <div class="abs" style="left:0;top:940px;width:1080px;text-align:center;font-size:48px;color:var(--dim);font-weight:600">Küche und 3 Zimmer streichen</div>
 <div class="cap" id="c1" style="top:1130px;font-size:104px">Das ist ein<br>ganzer Auftrag.</div>
 <div class="btn" style="left:200px;top:1560px;width:200px;height:200px;background:#e5534b">✕</div>
 <div class="btn" style="left:680px;top:1560px;width:200px;height:200px;background:#3ac26f">✆</div>
</div></div>

<!-- S2 Leiter -->
<div id="S2" class="L">
 <svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">
  <rect width="1080" height="1920" fill="#cfc9bb"/><rect id="paint" x="640" y="360" width="440" height="0" fill="#f2efe8"/>
  <rect y="1560" width="1080" height="360" fill="#2a2824"/>
  <g fill="#9a7b4f"><rect x="330" y="400" width="30" height="1180" rx="8"/><rect x="560" y="400" width="30" height="1180" rx="8"/></g>
  <g fill="#b8956a"><rect x="360" y="540" width="200" height="22"/><rect x="360" y="700" width="200" height="22"/><rect x="360" y="860" width="200" height="22"/><rect x="360" y="1020" width="200" height="22"/><rect x="360" y="1180" width="200" height="22"/><rect x="360" y="1340" width="200" height="22"/></g>
  <g id="mal">
   <rect x="392" y="930" width="64" height="90" rx="14" fill="#8c8a84"/><rect x="466" y="930" width="64" height="90" rx="14" fill="#8c8a84"/>
   <rect x="380" y="700" width="160" height="260" rx="60" fill="#f2efe8"/>
   <rect x="400" y="760" width="120" height="14" fill="#d8d2c3"/>
   <circle id="mh" cx="460" cy="620" r="78" fill="#e8b99a"/><path d="M382 600 Q460 500 538 600 Z" fill="#0f1115"/><rect x="520" y="590" width="70" height="20" rx="8" fill="#0f1115"/>
   <ellipse cx="432" cy="630" rx="12" ry="16" fill="#fff"/><ellipse cx="488" cy="630" rx="12" ry="16" fill="#fff"/><circle id="pl" cx="434" cy="636" r="7" fill="#0f1115"/><circle id="pr" cx="490" cy="636" r="7" fill="#0f1115"/>
   <path d="M436 676 Q460 690 484 676" stroke="#8a4b3c" stroke-width="6" fill="none" stroke-linecap="round"/>
   <g id="arm"><path d="M530 760 L690 650" stroke="#f2efe8" stroke-width="54" stroke-linecap="round"/><circle cx="700" cy="644" r="30" fill="#e8b99a"/>
    <rect x="712" y="520" width="14" height="150" rx="6" fill="#8c8a84"/><rect x="680" y="400" width="80" height="150" rx="20" fill="#f2efe8" stroke="#bdb7a8" stroke-width="5"/></g>
   <path d="M380 780 Q330 840 360 900" stroke="#f2efe8" stroke-width="50" stroke-linecap="round" fill="none"/>
  </g>
  <g id="jk"><path d="M60 1560 Q40 1470 150 1450 Q300 1430 330 1560 Z" fill="#4a4f3c"/>
   <g id="ph2"><rect x="170" y="1400" width="86" height="150" rx="16" fill="#111" transform="rotate(-14 213 1475)"/><rect x="178" y="1412" width="70" height="120" rx="10" fill="#f2efe8" transform="rotate(-14 213 1475)"/></g>
   <g id="waves" fill="none" stroke="#f2efe8" stroke-width="6" stroke-linecap="round"><path d="M110 1420 Q90 1475 110 1530" opacity=".0"/></g></g>
 </svg>
 <div class="chip" style="top:150px"><span id="ct">Kundin wartet 0:00</span></div>
</div>

<!-- S3 Verpasst -->
<div id="S3" class="L" style="background:#0f1115"><div id="vp" class="abs" style="left:0;top:700px;width:1080px;text-align:center"><div style="font-size:150px;font-weight:800;letter-spacing:-4px">Verpasst.</div><div style="font-size:60px;color:#e5534b;margin-top:20px;font-weight:700">✆ Anruf von Frau Keller</div></div></div>

<!-- S4 Küche -->
<div id="S4" class="L" style="background:#2a2622">
 <svg class="abs" style="left:0;top:0" width="1080" height="1920" viewBox="0 0 1080 1920">
  <rect y="0" width="1080" height="420" fill="#3a342e"/><g fill="#4a433b"><rect x="40" y="80" width="300" height="260" rx="14"/><rect x="360" y="80" width="300" height="260" rx="14"/><rect x="680" y="80" width="360" height="260" rx="14"/></g>
  <rect y="1360" width="1080" height="560" fill="#1f1c19"/><rect y="1340" width="1080" height="40" fill="#5a5148"/>
  <g id="cup"><rect x="800" y="1250" width="110" height="90" rx="14" fill="#f2efe8"/><path id="steam" d="M830 1230 Q820 1190 840 1160" stroke="#8c8a84" stroke-width="6" fill="none" stroke-linecap="round"/></g>
  <g id="fk"><rect x="320" y="1000" width="440" height="400" rx="150" fill="#8c8a84"/><circle cx="540" cy="860" r="130" fill="#0f1115"/><circle cx="540" cy="875" r="105" fill="#e8b99a"/>
   <path d="M430 850 Q440 740 540 745 Q640 740 650 850 Q600 790 540 805 Q480 790 430 850Z" fill="#0f1115"/>
   <ellipse cx="500" cy="880" rx="14" ry="18" fill="#fff"/><ellipse cx="580" cy="880" rx="14" ry="18" fill="#fff"/><circle cx="500" cy="892" r="8" fill="#0f1115"/><circle cx="580" cy="892" r="8" fill="#0f1115"/>
   <path d="M480 840 Q500 826 522 838" stroke="#0f1115" stroke-width="7" fill="none" stroke-linecap="round"/><path d="M558 838 Q580 826 600 840" stroke="#0f1115" stroke-width="7" fill="none" stroke-linecap="round"/>
   <path d="M510 944 Q540 934 570 944" stroke="#8a4b3c" stroke-width="7" fill="none" stroke-linecap="round"/>
   <g id="kph"><rect x="470" y="1090" width="140" height="200" rx="22" fill="#111"/><rect x="480" y="1102" width="120" height="170" rx="14" fill="#f2efe8"/></g>
   <circle id="th1" cx="500" cy="1220" r="22" fill="#e8b99a"/><circle id="th2" cx="580" cy="1220" r="22" fill="#e8b99a"/></g>
 </svg>
 <div class="cap" id="c4" style="top:210px;font-size:120px">Sie wartet<br>nicht.</div>
 <div id="dts" class="abs" style="left:640px;top:1020px;background:#f2efe8;color:#0f1115;border-radius:34px 34px 34px 8px;padding:10px 34px;font-size:80px;font-weight:800;letter-spacing:6px;opacity:0">…</div>
</div>

<!-- S5 andere Seite -->
<div id="S5" class="L" style="background:#0f1115">
 <div class="cap" id="c5" style="top:90px;font-size:84px">2 Minuten 10.<br>Ohne zu telefonieren.</div>
 <div class="chip" style="top:300px"><span id="ct2">Kundin wartet 1:58</span></div>
 <div id="ph5" class="abs" style="left:225px;top:430px;width:460px;height:968px;transform-origin:0 0;transform:scale(1.35);border-radius:62px;background:#1b1e24;border:6px solid #2d343c;padding:6px">
  <div class="abs" style="left:6px;top:6px;width:436px;height:944px;border-radius:52px;overflow:hidden;background:#f2efe8;color:#0f1115">
   <div class="abs" style="left:0;top:0;width:436px;height:90px;background:#0f1115;color:#f2efe8;font-weight:800;font-size:26px;letter-spacing:3px;display:flex;align-items:center;padding-left:26px">MALER BRUNNER</div>
   <div class="abs" style="left:0;top:90px;width:436px;height:380px;background:linear-gradient(135deg,#cfc9bb,#a79f8c)"></div>
   <div class="abs" style="left:26px;top:230px;width:380px;font-weight:800;font-size:44px;line-height:1.05">Wände.<br>Fassaden.<br>Sauber.</div>
   <div class="abs" style="left:26px;top:520px;width:384px;font-size:21px;line-height:1.4;color:#5b5850">Innen- und Aussenarbeiten für Privat und Gewerbe. Wir melden uns, wenn wir auf der Leiter stehen.</div>
   <div id="rbtn" class="abs" style="left:26px;top:680px;width:384px;height:98px;border-radius:49px;background:#ffb020;font-weight:800;font-size:30px;display:flex;align-items:center;justify-content:center">Rückruf anfragen</div>
   <div id="tap" class="abs" style="left:190px;top:700px;width:60px;height:60px;border-radius:50%;border:5px solid #0f1115;opacity:0"></div>
  </div></div>
</div>

<!-- S6 Chat -->
<div id="S6" class="L" style="background:#0f1115">
 <div class="abs" style="left:0;top:0;width:1080px;height:230px;background:#171a20"></div>
 <div class="abs" style="left:60px;top:80px;width:100px;height:100px;border-radius:50%;background:#2a2d34;display:flex;align-items:center;justify-content:center;font-size:40px;font-weight:800;color:var(--dim)">FK</div>
 <div class="abs" style="left:190px;top:92px;font-size:46px;font-weight:700">Frau Keller</div>
 <div id="rc" class="bub" style="left:560px;top:380px;background:#2a2d34;font-size:36px;color:var(--dim);opacity:0">✆ Rückruf · Maler ruft an</div>
 <div id="dots6" class="bub" style="left:60px;top:560px;background:#23262c;opacity:0;font-size:60px;letter-spacing:6px;padding:14px 32px">···</div>
 <div id="in6" class="bub" style="left:60px;top:560px;background:#23262c;opacity:0;font-size:52px;max-width:760px">Danke, hat sich erledigt.</div>
</div>

<!-- S7 Schwarz -->
<div id="S7" class="L" style="background:#0f1115">
 <div class="cap" id="t1" style="top:720px;font-size:96px;opacity:0">Der andere Maler<br>war nicht besser.</div>
 <div class="cap" id="t2" style="top:700px;font-size:150px;color:var(--amb);opacity:0">Nur<br>erreichbar.</div>
</div>

<!-- S8 Frage -->
<div id="S8" class="L" style="background:#0f1115">
 <div class="cap" id="q" style="top:640px;font-size:104px">Wie viele Anrufe verpassen Sie diese Woche?</div>
 <div id="q2" class="abs" style="left:0;top:1190px;width:1080px;text-align:center;font-size:52px;color:var(--dim);font-weight:700">Zahl in die Kommentare</div>
</div>
<div id="flash" class="abs" style="left:0;top:0;width:1080px;height:1920px;background:#f2efe8;opacity:0;pointer-events:none"></div>
</div></div>
<script>
window.__timelines=window.__timelines||{};const tl=gsap.timeline({paused:true});const $=s=>document.querySelector(s);
const W=[['#S1',0,1.5],['#S2',1.5,4.0],['#S3',4.0,5.5],['#S4',5.5,8.0],['#S5',8.0,11.0],['#S6',11.0,13.5],['#S7',13.5,16.7],['#S8',16.7,18.2],['#S1',18.2,18.5]];
W.forEach(([s,a,b])=>{tl.set(s,{display:'block'},a);tl.set(s,{display:'none'},b)});
const pop=(s,a)=>tl.fromTo(s,{scale:.85,opacity:0},{scale:1,opacity:1,duration:.22,ease:'back.out(2)',transformOrigin:'50% 50%'},a);
// S1: vibriert, Ringe pulsieren
tl.fromTo('#cw',{x:-12},{x:12,duration:.055,yoyo:true,repeat:26,ease:'none'},0);
tl.fromTo('#cw',{x:-12},{x:12,duration:.055,yoyo:true,repeat:4,ease:'none'},18.2);
['#rg1','#rg2'].forEach((r,i)=>tl.fromTo(r,{scale:1,opacity:.9},{scale:1.5,opacity:0,duration:.9,repeat:3,ease:'power1.out',transformOrigin:'50% 50%'},0.05+i*.45));
// S2: Maler streicht, Handy bebt, Zaehler
tl.fromTo('#arm',{y:-50},{y:60,duration:.45,yoyo:true,repeat:6,ease:'sine.inOut'},1.5);
tl.fromTo('#paint',{height:0},{height:700,duration:2.5,ease:'none'},1.5);
tl.fromTo('#ph2',{x:-6},{x:6,duration:.05,yoyo:true,repeat:48,ease:'none'},1.5);
tl.to(['#pl','#pr'],{y:10,duration:.2},1.9).to(['#pl','#pr'],{y:0,duration:.2},2.6).to(['#pl','#pr'],{y:10,duration:.2},3.1);
const o1={v:0};tl.to(o1,{v:3.1,duration:2.5,ease:'none',onUpdate:()=>{$('#ct').textContent='Kundin wartet 0:0'+Math.floor(o1.v)}},1.5);
tl.fromTo('#ct',{scale:1},{scale:1.08,duration:.4,yoyo:true,repeat:5,transformOrigin:'50% 50%'},1.5);
// S3: Schlag
tl.fromTo('#vp',{scale:1.25,opacity:0},{scale:1,opacity:1,duration:.12,ease:'power4.out',transformOrigin:'50% 50%'},4.0);
tl.fromTo('#flash',{opacity:.35},{opacity:0,duration:.15,immediateRender:false},4.0);
// S4: Kueche, tippt
tl.fromTo('#th1',{y:0},{y:-10,duration:.12,yoyo:true,repeat:15},5.6).fromTo('#th2',{y:0},{y:-10,duration:.12,yoyo:true,repeat:15},5.66);
tl.fromTo('#steam',{y:0,opacity:.9},{y:-26,opacity:0,duration:1.2,repeat:2,ease:'none'},5.5);
tl.fromTo('#fk',{y:6},{y:-6,duration:1.2,yoyo:true,repeat:2,ease:'sine.inOut'},5.5);
tl.fromTo('#dts',{opacity:0,scale:.6},{opacity:1,scale:1,duration:.3,ease:'back.out(2)',transformOrigin:'0 100%'},6.4);
pop('#c4',5.55);
// S5: andere Seite
pop('#c5',8.0);tl.fromTo('#ph5',{y:140,opacity:0},{y:0,opacity:1,duration:.4,ease:'power3.out'},8.0);
const o2={v:118};tl.to(o2,{v:130,duration:1.4,ease:'none',onUpdate:()=>{const s=Math.round(o2.v);$('#ct2').textContent='Kundin wartet '+Math.floor(s/60)+':'+String(s%60).padStart(2,'0')}},8.2);
tl.fromTo('#tap',{opacity:1,scale:.4},{opacity:0,scale:1.6,duration:.45,ease:'power2.out',transformOrigin:'50% 50%'},9.5);
tl.fromTo('#rbtn',{scale:1},{scale:.94,duration:.1,yoyo:true,repeat:1,transformOrigin:'50% 50%'},9.5);
tl.call(()=>{$('#rbtn').textContent='Gesendet ✓';$('#rbtn').style.background='#0f1115';$('#rbtn').style.color='#f2efe8'},null,9.62);
tl.call(()=>{$('#rbtn').textContent='Rückruf anfragen';$('#rbtn').style.background='#ffb020';$('#rbtn').style.color='#0f1115'},null,0);
tl.fromTo('#ct2',{scale:1},{scale:1.2,duration:.2,yoyo:true,repeat:1,transformOrigin:'50% 50%'},9.6);
// S6: Rueckruf + Antwort
tl.fromTo('#rc',{opacity:0,y:20},{opacity:1,y:0,duration:.3},11.2);
tl.fromTo('#dots6',{opacity:0,y:20},{opacity:1,y:0,duration:.25},11.8).set('#dots6',{opacity:0},12.1);
tl.fromTo('#in6',{opacity:0,y:20,scale:.9},{opacity:1,y:0,scale:1,duration:.3,ease:'back.out(2)',transformOrigin:'0 100%'},12.1);
// S7: Satz, Pause, Amber
tl.fromTo('#t1',{opacity:0,y:30},{opacity:1,y:0,duration:.3},13.5).set('#t1',{opacity:0},14.8);
tl.fromTo('#t2',{opacity:0,scale:.8},{opacity:1,scale:1,duration:.3,ease:'back.out(2)',transformOrigin:'50% 50%'},15.5);
// S8
pop('#q',16.75);tl.fromTo('#q2',{opacity:0},{opacity:1,duration:.4},17.3);
tl.fromTo('#flash',{opacity:.5},{opacity:0,duration:.12,immediateRender:false},18.2);
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
open('hf/index.html','w').write(html)
# ---- Ton ----
SR=44100;n=int(SR*T);L=np.zeros(n)
def put(x,t,g=1.0):
    s=int(t*SR)
    if s<n and s>=0: x=x[:n-s]*g; L[s:s+len(x)]+=x
def tone(f,d,g,decay=6,fade=0.005):
    t=np.arange(int(d*SR))/SR;x=np.sin(2*np.pi*f*t)*np.exp(-t*decay)*g;k=int(fade*SR);x[:k]*=np.linspace(0,1,k);return x
def ring(d=0.4,g=0.3):
    t=np.arange(int(d*SR))/SR;x=(np.sin(2*np.pi*440*t)+np.sin(2*np.pi*480*t))*(0.5+0.5*np.sin(2*np.pi*25*t))*g;k=int(0.01*SR);x[:k]*=np.linspace(0,1,k);x[-k:]*=np.linspace(1,0,k);return x
def load(f,dur=None,lp=None):
    af=["-af",f"lowpass=f={lp}"] if lp else []
    c=["ffmpeg","-v","error","-i",f]+(["-t",str(dur)] if dur else [])+af+["-ac","1","-ar",str(SR),"-f","f32le","-"]
    return np.frombuffer(subprocess.run(c,capture_output=True).stdout,dtype=np.float32).astype(np.float64)
click=load('../viral_reel/sfx/click.mp3',0.1,5000);impact=load('../viral_reel/sfx/impact.mp3',0.8,2500);chime=load('../viral_reel/sfx/chime.mp3',0.9,6000)
# Klingeln ab Frame 1 bis 4.0 (zwei Stoesse, Pause)
tt=0.0
while tt<4.0-0.2:
    put(ring(0.4),tt);put(ring(0.4),tt+0.55);tt+=2.0
buz=np.sin(2*np.pi*95*np.arange(int(4.0*SR))/SR)*(0.5+0.5*np.sin(2*np.pi*18*np.arange(int(4.0*SR))/SR))*0.07;put(buz,0.0)
# Verpasst: Stille, dumpfer Schlag
th=np.arange(int(0.8*SR))/SR;put(np.sin(2*np.pi*(52+60*np.exp(-th*18))*th)*np.exp(-th*5)*0.8,4.02);put(impact,4.02,0.5)
# Tippen
rng=np.random.default_rng(3)
for i in range(18): put(click,5.7+i*0.125+rng.uniform(-.02,.02),0.45)
put(click,6.45,0.0)
put(click,9.5,0.9);put(tone(880,0.4,0.3),9.62);put(tone(1318,0.5,0.28),9.78)   # Tap + Gesendet
put(ring(0.4,0.12),11.0);put(ring(0.4,0.12),11.55)                              # Rueckruf
put(tone(1000,0.25,0.3,12),12.1)                                                 # Nachricht
put(tone(330,1.2,0.35,3),15.5);put(tone(660,1.0,0.12,3),15.5)                    # Amber: Nur erreichbar
put(ring(0.3,0.3),18.2)                                                          # Loop-Klingeln
mix=np.stack([L,L],1);mix[-int(0.05*SR):]*=np.linspace(1,0,int(0.05*SR))[:,None];mix=mix/np.max(np.abs(mix))*0.9
with wave.open('mix.wav','wb') as w: w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype('<i2').tobytes())
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","mix.wav","-af","loudnorm=I=-14:TP=-1.5:LRA=9","-ar","44100","-c:a","libmp3lame","-b:a","192k","hf/assets/audio.mp3"]);os.remove('mix.wav');print('fertig')
