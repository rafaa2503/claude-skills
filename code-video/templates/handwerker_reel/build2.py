# Handwerker-Reel v2: Handy-Grafiken statt Untertitel (Google-Suche, leere Treffer, Maps-Karte, Chat). Text nur: Hook, Zitat, Schlusssatz.
import os, shutil, subprocess, wave, numpy as np
V={
'b':dict(vo='sfx/vo_b.mp3',T=24.2,
 hook=[['Du bist der<br><em>Beste</em>',0.14,1.02],['in deinem<br>Job.',1.04,1.85],['Genau das<br>ist dein<br><u>Problem.</u>',2.20,3.60],['Letzte Woche<br>sagte mir<br>einer genau<br>das.',4.10,5.90]],
 g=6.02,gend=6.9,empty=7.12,photos_empty=8.90,card=10.18,fo=13.20,st=13.68,ca=14.62,chat=16.00,dots=17.98,quote=20.16,qend=21.80,fin=21.90),
'c':dict(vo='sfx/vo_c.mp3',T=23.8,
 hook=[['Das<br><em>Traurigste,</em>',0.08,0.82],['was mir ein<br>Handwerker<br>je geschrieben<br>hat,',0.84,2.50],['war ein Satz<br>übers Wetter.',2.88,4.00],['Er sagte,<br>er sei der<br>Beste der<br>Stadt.',4.02,5.90]],
 g=6.24,gend=7.1,empty=7.48,photos_empty=8.72,card=10.02,fo=12.98,st=13.46,ca=14.12,chat=15.60,dots=17.58,quote=19.42,qend=21.15,fin=21.38)}
CSS='''*{margin:0;padding:0;box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#000}
:root{--or:#ff9f1c;--red:#ff4a55;--g:#8d95a0}
#root{position:relative;width:1080px;height:1920px;font-family:Inter,ui-sans-serif,system-ui,sans-serif;color:#fff;background:#0a0b0f;overflow:hidden}
.abs{position:absolute}.layer{position:absolute;left:0;top:0;width:1080px;height:1920px;display:none}
#vig{position:absolute;left:0;top:0;width:1080px;height:1920px;background:radial-gradient(ellipse at 50% 46%,rgba(255,255,255,.06),rgba(0,0,0,0) 60%)}
.cap{position:absolute;left:0;top:0;width:1080px;height:1920px;display:flex;align-items:center;justify-content:center;font-weight:700;line-height:1.06;letter-spacing:-1.5px;opacity:0}
.cap>div{max-width:960px;text-align:center}.cap em{font-style:normal;color:var(--or)}.cap u{text-decoration:none;color:var(--red)}
#ph{position:absolute;left:183px;top:210px;width:460px;height:968px;transform-origin:0 0;transform:scale(1.55);border-radius:62px;background:#101419;border:6px solid #2d343c;padding:6px;box-shadow:0 30px 120px rgba(0,0,0,.7)}
.scr{position:absolute;left:6px;top:6px;width:436px;height:944px;border-radius:52px;overflow:hidden;display:none}
#sG,#sM{background:#fff;color:#202124}#sC{background:#0d1418}
.gl{position:absolute;left:0;top:130px;width:100%;text-align:center;font-size:62px;font-weight:700;letter-spacing:-2px}
.sb{position:absolute;left:24px;top:230px;width:388px;height:64px;border-radius:32px;border:1.5px solid #dadce0;box-shadow:0 1px 6px rgba(32,33,36,.2);display:flex;align-items:center;padding-left:22px;font-size:23px;color:#202124}
.ph{background:#e8eaed;border-radius:14px;position:absolute;overflow:hidden}
.pc{position:absolute;left:0;top:0;width:100%;height:100%}
.ph.x:after{content:"";position:absolute;left:-10%;top:48%;width:120%;height:3px;background:#bdc1c6;transform:rotate(-24deg)}
.card{position:absolute;left:18px;top:120px;width:400px}
.ph2{position:absolute;border-radius:12px;overflow:hidden}
.btn{position:absolute;border-radius:28px;font-weight:700;font-size:21px;display:flex;align-items:center;justify-content:center}
#logo{position:absolute;left:0;top:1560px;width:1080px;text-align:center;opacity:0}
'''
def stars(): return '★★★★★'
for k,v in V.items():
    d=f'hf2_{k}'; os.makedirs(d+'/assets',exist_ok=True)
    for f in ['hyperframes.json','meta.json','package.json']: shutil.copy('hf/'+f,d)
    shutil.copy('hf/assets/icon-crop.png',d+'/assets/')
    T=v['T']
    cloud='<svg id="cloud" class="abs" style="left:390px;top:6px;opacity:0" width="300" height="192" viewBox="0 0 500 320"><g fill="#c9d1da"><ellipse cx="170" cy="150" rx="110" ry="80"/><ellipse cx="290" cy="120" rx="120" ry="95"/><ellipse cx="370" cy="170" rx="100" ry="70"/><rect x="100" y="150" width="360" height="70" rx="35"/></g><g stroke="#5aa9ff" stroke-width="9" stroke-linecap="round"><line class="rn" x1="170" y1="250" x2="150" y2="300"/><line class="rn" x1="250" y1="250" x2="230" y2="300"/><line class="rn" x1="330" y1="250" x2="310" y2="300"/><line class="rn" x1="410" y1="250" x2="390" y2="300"/></g></svg>'
    body=f'''<!doctype html><html lang="de" data-resolution="portrait"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<audio id="mus" src="assets/audio.mp3" data-start="0" data-duration="{T}" data-track-index="9" data-volume="1"></audio>
<div class="clip abs" data-start="0" data-duration="{T}" data-track-index="0" style="left:0;top:0;width:1080px;height:1920px">
<div id="vig"></div>
<div id="L_ph" class="layer">
 <div id="ph">
  <div id="sG" class="scr"><div class="gl"><span style="color:#4285f4">G</span><span style="color:#ea4335">o</span><span style="color:#fbbc05">o</span><span style="color:#4285f4">g</span><span style="color:#34a853">l</span><span style="color:#ea4335">e</span></div>
   <div class="sb"><span id="tp"></span><span id="caret" style="width:2px;height:28px;background:#4285f4;margin-left:2px"></span></div>
   <div id="emp" class="abs" style="left:0;top:380px;width:436px;text-align:center;opacity:0"><svg width="130" height="130" viewBox="0 0 24 24" fill="none" stroke="#bdc1c6" stroke-width="1.6" stroke-linecap="round"><circle cx="10" cy="10" r="6.5"/><line x1="15" y1="15" x2="21" y2="21"/><line x1="7" y1="7" x2="13" y2="13"/></svg><div style="font-size:24px;color:#80868b;margin-top:14px">Keine Ergebnisse</div></div>
   <div id="pe" class="abs" style="left:24px;top:640px;width:388px;height:120px;opacity:0"><div class="ph x" style="left:0;top:0;width:120px;height:120px"></div><div class="ph x" style="left:134px;top:0;width:120px;height:120px"></div><div class="ph x" style="left:268px;top:0;width:120px;height:120px"></div></div>
  </div>
  <div id="sM" class="scr"><div class="abs" style="left:0;top:0;width:436px;height:420px;background:#e8f0e6"></div>
   <svg class="abs" style="left:0;top:0" width="436" height="420"><g stroke="#fff" stroke-width="14" fill="none"><path d="M-10 120 L450 190"/><path d="M130 -10 L180 430"/><path d="M-10 320 L450 280"/></g><g stroke="#f5d98a" stroke-width="9" fill="none"><path d="M300 -10 L260 430"/></g></svg>
   <div class="abs" style="left:190px;top:170px;width:58px;height:58px;border-radius:50% 50% 50% 0;background:#ea4335;transform:rotate(-45deg);box-shadow:0 8px 20px rgba(0,0,0,.35)"></div><div class="abs" style="left:210px;top:190px;width:18px;height:18px;border-radius:50%;background:#fff"></div>
   <div id="cardW" class="abs" style="left:0;top:400px;width:436px;height:544px;background:#fff;border-radius:26px 26px 0 0;box-shadow:0 -6px 24px rgba(0,0,0,.18)">
    <div id="ph3" class="abs" style="left:18px;top:22px;width:400px;height:130px;opacity:0"><div class="ph2" style="left:0;top:0;width:128px;height:130px;background:linear-gradient(135deg,#f6b93b,#e58e26)"></div><div class="ph2" style="left:136px;top:0;width:128px;height:130px;background:linear-gradient(135deg,#78e08f,#38ada9)"></div><div class="ph2" style="left:272px;top:0;width:128px;height:130px;background:linear-gradient(135deg,#82ccdd,#4a69bd)"></div></div>
    <div id="nm" class="abs" style="left:20px;top:172px;font-size:31px;font-weight:700;color:#202124">Keller Elektro</div>
    <div id="rt" class="abs" style="left:20px;top:218px;font-size:23px;color:#202124;opacity:0"><b>4,7</b> <span style="color:#fbbc04;letter-spacing:1px">{stars()}</span> <span style="color:#70757a">(96)</span></div>
    <div class="abs" style="left:20px;top:258px;font-size:21px;color:#70757a">Elektriker · Bern</div>
    <div id="cb" class="btn" style="left:20px;top:318px;width:190px;height:58px;background:#188038;color:#fff;opacity:0">Anrufen</div>
    <div id="rb" class="btn" style="left:226px;top:318px;width:190px;height:58px;background:#e8f0fe;color:#1a73e8;opacity:0">Route</div>
   </div>
  </div>
  <div id="sC" class="scr"><div class="abs" style="left:0;top:0;width:436px;height:120px;background:#1f2c34"></div>
   <div class="abs" style="left:24px;top:46px;width:56px;height:56px;border-radius:50%;background:#53636d"></div><div class="abs" style="left:96px;top:50px;font-size:25px;font-weight:700">Müller Elektro</div><div class="abs" style="left:96px;top:82px;font-size:17px;color:#8ba0ad">online</div>
   <div id="dots" class="abs" style="left:20px;top:200px;width:110px;height:56px;border-radius:20px 20px 20px 4px;background:#1f2c34;display:flex;align-items:center;justify-content:center;gap:8px;opacity:0"><i class="dt" style="width:11px;height:11px;border-radius:50%;background:#8ba0ad"></i><i class="dt" style="width:11px;height:11px;border-radius:50%;background:#8ba0ad"></i><i class="dt" style="width:11px;height:11px;border-radius:50%;background:#8ba0ad"></i></div>
   <div id="msg" class="abs" style="left:20px;top:200px;width:360px;padding:20px 22px;border-radius:22px 22px 22px 4px;background:#1f2c34;font-size:34px;font-weight:600;line-height:1.25;opacity:0">Muss wohl am Wetter liegen.</div>
  </div>
 </div>
 {cloud}
</div>
<div id="caps"></div>
<div id="logo"><img src="assets/icon-crop.png" style="height:110px"><div style="font-weight:800;font-size:52px;margin-top:4px">sherka<span style="color:var(--or)">.ch</span></div></div>
</div></div>
<script>
window.__timelines=window.__timelines||{{}};const tl=gsap.timeline({{paused:true}});const T={T};const $=s=>document.querySelector(s);
const H={v['hook']!r};const caps=$('#caps');
function cap(h,a,b,fs,i){{const d=document.createElement('div');d.className='cap';d.innerHTML='<div>'+h+'</div>';d.style.fontSize=fs;caps.appendChild(d);
 tl.set(d,{{opacity:1}},a).fromTo(d,{{y:26,opacity:0}},{{y:0,opacity:1,duration:.18,ease:'power2.out'}},a);if(b<T)tl.set(d,{{opacity:0}},b);return d;}}
H.forEach(([h,a,b],i)=>{{const longest=Math.max(...h.split('<br>').map(x=>x.replace(/<[^>]+>/g,'').length));const lines=h.split('<br>').length;
 cap(h,a,b,Math.min(150,Math.floor(900/(longest*0.56)),Math.floor(560/(lines*1.06)))+'px',i);}});
const fin='Schick das dem<br>Besten, den<br>du kennst.';cap(fin,{v['fin']},T,'120px',9);
// Handy-Ebene
tl.set('#L_ph',{{display:'block'}},{v['g']-0.25}).set('#L_ph',{{display:'none'}},{v['fin']});
tl.fromTo('#ph',{{y:90,opacity:0}},{{y:0,opacity:1,duration:.3,ease:'power3.out'}},{v['g']-0.25});
tl.set('#sG',{{display:'block'}},{v['g']-0.25}).set('#sG',{{display:'none'}},{v['card']-0.05});
tl.set('#sM',{{display:'block'}},{v['card']-0.05}).set('#sM',{{display:'none'}},{v['chat']-0.05});
tl.set('#sC',{{display:'block'}},{v['chat']-0.05});
// Tippen
const q='Müller Elektro',o={{n:0}};tl.to(o,{{n:q.length,duration:{v['gend']-v['g']},ease:'none',onUpdate:()=>{{$('#tp').textContent=q.slice(0,Math.round(o.n))}}}},{v['g']});
tl.to('#caret',{{opacity:0,duration:.25,yoyo:true,repeat:30,ease:'steps(1)'}},{v['g']-0.25});
tl.fromTo('#emp',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.3}},{v['empty']});
tl.fromTo('#pe',{{opacity:0,y:20}},{{opacity:1,y:0,duration:.3}},{v['photos_empty']});
// Karte: erst nur Name, dann Fotos, Sterne, Anrufen
tl.fromTo('#cardW',{{y:300}},{{y:0,duration:.45,ease:'power3.out'}},{v['card']});
tl.fromTo('#ph3',{{opacity:0,scale:.9}},{{opacity:1,scale:1,duration:.25,ease:'back.out(2)',transformOrigin:'50% 50%'}},{v['fo']});
tl.fromTo('#rt',{{opacity:0,scale:.8}},{{opacity:1,scale:1,duration:.25,ease:'back.out(2)',transformOrigin:'0 50%'}},{v['st']});
tl.fromTo('#cb',{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.25,ease:'back.out(2)'}},{v['ca']}).fromTo('#rb',{{opacity:0,scale:.7}},{{opacity:1,scale:1,duration:.25,ease:'back.out(2)'}},{v['ca']+0.12});
// Chat
tl.fromTo('#dots',{{opacity:0,y:10}},{{opacity:1,y:0,duration:.2}},{v['dots']}).to('.dt',{{y:-8,duration:.28,yoyo:true,repeat:6,stagger:.12,ease:'sine.inOut'}},{v['dots']+0.1}).set('#dots',{{opacity:0}},{v['quote']});
tl.fromTo('#msg',{{opacity:0,y:14,scale:.96}},{{opacity:1,y:0,scale:1,duration:.22,ease:'power2.out',transformOrigin:'0 0'}},{v['quote']});
tl.fromTo('#cloud',{{opacity:0,y:-40}},{{opacity:1,y:0,duration:.6,ease:'power2.out'}},{v['quote']+0.1});
tl.fromTo('.rn',{{y:0,opacity:1}},{{y:46,opacity:0,duration:.55,repeat:12,stagger:.1,ease:'none'}},{v['quote']+0.3});
tl.fromTo('#vig',{{opacity:.5}},{{opacity:1,duration:T,ease:'none'}},0);
tl.to('#logo',{{opacity:1,duration:.6}},{v['fin']+1.0});
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
    open(d+'/index.html','w').write(body)
    # Ton: Stimme + leiser Bass + Tipp-Ticks + kleine Pops + weicher Schlag beim Zitat
    SR=44100;n=int(SR*T)
    def load(f,t0=0,dur=None,lp=None):
        af=["-af",f"lowpass=f={lp}"] if lp else []
        c=["ffmpeg","-v","error","-ss",str(t0)]+(["-t",str(dur)] if dur else [])+["-i",f]+af+["-ac","1","-ar",str(SR),"-f","f32le","-"]
        return np.frombuffer(subprocess.run(c,capture_output=True).stdout,dtype=np.float32).astype(np.float64)
    vo=load(v['vo']);VL=np.zeros(n);VL[:len(vo)]=vo[:n]
    t=np.arange(n)/SR
    pad=(np.sin(2*np.pi*55*t)*0.5+np.sin(2*np.pi*82.4*t+1)*0.3)*0.05*np.minimum(1,t/2)*np.minimum(1,(T-t)/1.0)
    X=np.zeros(n)
    def put(x,tt,g):
        s=int(tt*SR)
        if s<n: x=x[:n-s]*g; X[s:s+len(x)]+=x
    click=load('sfx/click.mp3',0,0.12,lp=4500)
    for i in range(14): put(click,v['g']+i*(v['gend']-v['g'])/14,0.3)
    pop=load('sfx/click.mp3',0,0.15,lp=2500)
    for tt in [v['empty'],v['photos_empty'],v['card'],v['fo'],v['st'],v['ca'],v['dots'],v['quote']]: put(pop,tt,0.5)
    put(load('sfx/chime.mp3',0,0.7,lp=4000),v['quote']+0.02,0.22)
    kt=np.arange(int(0.9*SR))/SR;thud=np.sin(2*np.pi*(46+50*np.exp(-kt*14))*kt)*np.exp(-kt*4.5)*0.35;put(thud,v['quote'],1.0)
    mix=VL*1.4+pad+X
    mix=np.stack([mix,mix],1);mix=mix/np.max(np.abs(mix))*0.9
    with wave.open('mix.wav','wb') as w: w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype('<i2').tobytes())
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i","mix.wav","-af","loudnorm=I=-14:TP=-1.5:LRA=9","-ar","44100","-c:a","libmp3lame","-b:a","192k",d+"/assets/audio.mp3"]);os.remove('mix.wav')
print('fertig')
