# Handwerker-Reel (Hook B / Hook C): ruhige Textszenen auf Stimme, Pausen = Schwarz. Erzeugt hf_b/ und hf_c/ samt Audio.
import os, shutil, subprocess, wave, numpy as np
Q='<q>Muss wohl<br>am Wetter<br>liegen.</q>'
V={
'b':dict(vo='sfx/vo_b.mp3',T=24.2,quote=20.16,end=23.1,P=[
 ['Du bist der<br><em>Beste</em>',0.14,1.02],['in deinem<br>Job.',1.04,1.85],['Genau das<br>ist dein<br><u>Problem.</u>',2.20,3.60],
 ['Letzte Woche<br>sagte mir<br>einer genau<br>das.',4.10,5.90],['Ich google<br>ihn.',6.02,6.85],['<u>Nichts.</u>',7.12,7.80],
 ['Kein<br>Eintrag.',7.86,8.75],['Keine<br>Fotos.',8.90,9.75],['Dann den<br>Zweiten.',10.18,11.15],['Mittel-<br>mässig.',11.42,12.25],
 ['Aber:',12.52,13.05],['Fotos.',13.20,13.62],['Bewertungen.',13.68,14.40],['Nummer<br>ganz oben.',14.62,15.55],
 ['Aber das war<br>nicht das<br>Schlimme.',16.00,16.92],['Das Schlimme<br>war,',16.94,17.96],['was der Beste<br>mir danach<br>schrieb:',17.98,19.90],
 [Q,20.16,21.80],['Schick das dem<br>Besten, den<br>du kennst.',21.90,24.2]]),
'c':dict(vo='sfx/vo_c.mp3',T=23.8,quote=19.42,end=22.7,P=[
 ['Das<br><em>Traurigste,</em>',0.08,0.82],['was mir ein<br>Handwerker<br>je geschrieben<br>hat,',0.84,2.50],['war ein Satz<br>übers Wetter.',2.88,4.00],
 ['Er sagte,<br>er sei der<br>Beste der<br>Stadt.',4.02,5.90],['Ich google<br>ihn.',6.24,7.05],['<u>Nichts.</u>',7.48,7.95],
 ['Kein<br>Eintrag.',8.00,8.70],['Keine<br>Fotos.',8.72,9.55],['Dann den<br>Zweiten:',10.02,10.95],['Mittel-<br>mässig.',11.06,11.95],
 ['Aber',12.20,12.80],['Fotos.',12.98,13.40],['Bewertungen.',13.46,14.08],['Nummer<br>ganz oben.',14.12,15.10],
 ['Aber das war<br>nicht das<br>Schlimme.',15.60,16.75],['Das Schlimme<br>war,',16.90,17.52],['was der Beste<br>mir danach<br>schrieb:',17.58,19.30],
 [Q,19.42,21.15],['Schick das dem<br>Besten, den<br>du kennst.',21.38,23.8]])}
CSS='''*{margin:0;padding:0;box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden;background:#000}
:root{--or:#ff9f1c;--red:#ff4a55;--g:#8d95a0}
#root{position:relative;width:1080px;height:1920px;font-family:Inter,ui-sans-serif,system-ui,sans-serif;color:#fff;background:#0a0b0f;overflow:hidden}
.abs{position:absolute}
#vig{position:absolute;left:0;top:0;width:1080px;height:1920px;background:radial-gradient(ellipse at 50% 46%,rgba(255,255,255,.05),rgba(0,0,0,0) 60%)}
#caps{position:absolute;left:0;top:0;width:1080px;height:1920px}
.cap{position:absolute;left:0;top:0;width:1080px;height:1920px;display:flex;align-items:center;justify-content:center;font-weight:700;line-height:1.06;letter-spacing:-1.5px;opacity:0}
.cap>div{max-width:960px;text-align:center}.cap em{font-style:normal;color:var(--or)}.cap u{text-decoration:none;color:var(--red)}
.cap q{quotes:"„" "“";color:var(--or);font-weight:800}
#logo{position:absolute;left:0;top:1560px;width:1080px;text-align:center;opacity:0}'''
for k,v in V.items():
    d=f'hf_{k}'; os.makedirs(d+'/assets',exist_ok=True)
    for f in ['hyperframes.json','meta.json','package.json']: shutil.copy('hf/'+f,d)
    shutil.copy('hf/assets/icon-crop.png',d+'/assets/')
    T=v['T']
    body=f'''<!doctype html><html lang="de" data-resolution="portrait"><head><meta charset="UTF-8"/><meta name="viewport" content="width=1080, height=1920"/>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script><style>{CSS}</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{T}" data-width="1080" data-height="1920">
<audio id="mus" src="assets/audio.mp3" data-start="0" data-duration="{T}" data-track-index="9" data-volume="1"></audio>
<div class="clip abs" data-start="0" data-duration="{T}" data-track-index="0" style="left:0;top:0;width:1080px;height:1920px">
<div id="vig"></div><div id="caps"></div>
<div id="logo"><img src="assets/icon-crop.png" style="height:110px"><div style="font-weight:800;font-size:52px;margin-top:4px">sherka<span style="color:var(--or)">.ch</span></div></div>
</div></div>
<script>
window.__timelines=window.__timelines||{{}};const tl=gsap.timeline({{paused:true}});const T={T};
const P={v['P']!r};
const caps=document.getElementById('caps');
P.forEach(([h,a,b],i)=>{{const d=document.createElement('div');d.className='cap';d.innerHTML='<div>'+h+'</div>';
 const longest=Math.max(...h.split('<br>').map(x=>x.replace(/<[^>]+>/g,'').length));const lines=h.split('<br>').length;
 d.style.fontSize=Math.min(150,Math.floor(900/(longest*0.56)),Math.floor(560/(lines*1.06)))+'px';caps.appendChild(d);
 tl.set(d,{{opacity:1}},a).fromTo(d,{{y:26,opacity:0}},{{y:0,opacity:1,duration:.18,ease:'power2.out'}},a);
 if(b<T)tl.set(d,{{opacity:0}},b);}});
tl.fromTo('#vig',{{opacity:.5}},{{opacity:1,duration:{T},ease:'none'}},0);
tl.to('#logo',{{opacity:1,duration:.6}},{v['end']});
window.__timelines["main"]=tl;tl.seek(0);
</script></body></html>'''
    open(d+'/index.html','w').write(body)
    # Ton: Stimme + leiser Bass-Teppich + weicher Schlag beim Zitat
    SR=44100;n=int(SR*T)
    cmd=["ffmpeg","-v","error","-i",v['vo'],"-ac","1","-ar",str(SR),"-f","f32le","-"]
    vo=np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,dtype=np.float32).astype(np.float64)
    VL=np.zeros(n);VL[:len(vo)]=vo[:n]
    t=np.arange(n)/SR
    pad=(np.sin(2*np.pi*55*t)*0.5+np.sin(2*np.pi*82.4*t+1)*0.3)*0.05*np.minimum(1,t/2)*np.minimum(1,(T-t)/1.0)
    s=int(v['quote']*SR);kt=np.arange(int(0.9*SR))/SR
    thud=np.sin(2*np.pi*(46+50*np.exp(-kt*14))*kt)*np.exp(-kt*4.5)*0.35
    th=np.zeros(n);th[s:s+len(thud)]=thud[:n-s]
    mix=VL*1.4+pad+th
    mix=np.stack([mix,mix],1);mix=mix/np.max(np.abs(mix))*0.9
    with wave.open('mix.wav','wb') as w: w.setnchannels(2);w.setsampwidth(2);w.setframerate(SR);w.writeframes((mix*32767).astype('<i2').tobytes())
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i","mix.wav","-af","loudnorm=I=-14:TP=-1.5:LRA=9","-ar","44100","-c:a","libmp3lame","-b:a","192k",d+"/assets/audio.mp3"]);os.remove('mix.wav')
print('fertig')
