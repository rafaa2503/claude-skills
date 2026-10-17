# Handy-Test-Reel (20 s): Stoppuhr-Ticken (echte ElevenLabs-SFX), Klacks pro Button, Stille-Moment, dann Musik zum CTA.
# Stimme optional: wenn sfx/vo.mp3 existiert, wird sie auf die Marken in VO_PLAN gelegt (sonst nur Sound-Design).
import numpy as np, subprocess, wave, os
SR=44100; DUR=20.0; n=int(SR*DUR); rng=np.random.default_rng(8)
def load(f,t0=0.0,d=None):
    cmd=["ffmpeg","-v","error","-ss",str(t0)]+(["-t",str(d)] if d else [])+["-i",f"sfx/{f}","-ac","1","-ar",str(SR),"-f","f32le","-"]
    return np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,dtype=np.float32).astype(np.float64)
L=np.zeros(n); R=np.zeros(n)
def add(x,t,g=1.0,pan=0.0,fade=0.005):
    s=int(t*SR)
    if s>=n or len(x)==0: return
    x=x[:n-s].copy(); k=min(len(x)//2,int(fade*SR))
    if k>1: x[:k]*=np.linspace(0,1,k); x[-k:]*=np.linspace(1,0,k)
    L[s:s+len(x)]+=x*g*(1-max(0,pan)); R[s:s+len(x)]+=x*g*(1+min(0,pan))
def mid(m): return 440*2**((m-69)/12)
def bell(f,d=0.9,g=0.5,dec=5.0):
    t=np.arange(int(d*SR))/SR; return (np.sin(2*np.pi*f*t)+0.4*np.sin(2*np.pi*f*2*t)+0.2*np.sin(2*np.pi*f*3*t))*np.exp(-t*dec)*g*0.5
tick=load("tick.mp3")
def tick_run(t0,t1,g0,g1):
    t=t0; 
    while t<t1-0.05:
        seg=tick[:min(len(tick),int((t1-t)*SR))]; g=g0+(g1-g0)*(t-t0)/(t1-t0)
        add(seg,t,g,fade=0.02); t+=len(tick)/SR-0.02
# 1) Uhr laeuft 0 - 9.55 (Spannung steigt), Phone-Slide-Whoosh
tick_run(0.0,9.55,0.45,0.8); add(load("whoosh.mp3",0,0.9),1.95,0.35,fade=0.2)
# 2) Button-Klacks + kleine Melodie (D-Dur-Pentatonik)
for i,(t,m) in enumerate(zip([5.6,6.6,7.6,8.6],[74,76,78,81])):
    add(load("click.mp3",0,0.5),t,0.9,pan=(-0.4+0.27*i)); add(bell(mid(m),0.9,0.55),t+0.02,1.0,pan=(-0.4+0.27*i))
# 3) Stopp + Erfolg
add(load("stop.mp3",0,1.2),9.6,1.0); add(load("chime.mp3"),9.72,0.55)
# 4) Suspense: zweite Uhr + Drohnen 10.9 - 14.25, dann harter Schnitt in Stille
tick_run(10.9,14.25,0.5,0.95)
t=np.arange(int(3.4*SR))/SR; drone=(np.sin(2*np.pi*55*t)+0.5*np.sin(2*np.pi*82.4*t))*np.linspace(0.02,0.16,len(t)); add(drone,10.9,1.0,fade=0.3)
# 5) CTA: Einschlag, Akkord, Marimba-Arpeggio
add(load("impact.mp3"),14.9,1.0); add(load("chime.mp3"),15.15,0.6)
for m,g in zip([50,57,62,66,69],[.2,.16,.16,.14,.12]):
    tt=np.arange(int(5.0*SR))/SR; add(np.sin(2*np.pi*mid(m)*tt)*np.exp(-tt*0.7)*g,14.9,1.0,fade=0.02)
arp=[62,66,69,74,69,66]; tcur=15.5
for k in range(14):
    add(bell(mid(arp[k%6]+12),0.8,0.4,6.0),tcur+k*0.3,1.0,pan=(-1)**k*0.3)
# 6) optionale Stimme
VO_PLAN=[]   # [(datei, start_in_datei, ende_in_datei, ziel_sekunde)] nach silencedetect fuellen
VL=np.zeros(n)
for f,a,b,t0 in VO_PLAN:
    x=load(f,a,b-a+0.15); s=int(t0*SR); k=int(0.02*SR); x[:k]*=np.linspace(0,1,k); x[-int(0.08*SR):]*=np.linspace(1,0,int(0.08*SR)); VL[s:s+len(x)]+=x[:n-s]
env=np.convolve(np.abs(VL),np.ones(int(0.12*SR))/int(0.12*SR),mode="same"); duck=1-0.6*np.clip(env/0.08,0,1)
mix=np.stack([L*duck+VL*1.4,R*duck+VL*1.4],1); mix[-int(0.6*SR):]*=np.linspace(1,0,int(0.6*SR))[:,None]
mix=mix/np.max(np.abs(mix))*0.9
with wave.open("mix.wav","wb") as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype("<i2").tobytes())
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","mix.wav","-af","loudnorm=I=-14:TP=-1.5:LRA=9","-ar","44100","-c:a","libmp3lame","-b:a","192k","hf/assets/audio.mp3"]); os.remove("mix.wav"); print("fertig")
