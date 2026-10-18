# Viraler 3-Sekunden-Check (22.4 s): Stimme (ElevenLabs "Turbo Tim", ein Zug, ohne Pausen) + Countdown-Beeps + Whooshes + Klacks.
import numpy as np, subprocess, wave, os
SR=44100; DUR=22.4; n=int(SR*DUR)
def load(f,t0=0.0,d=None,lp=None):
    af=[f"lowpass=f={lp}"] if lp else []
    cmd=["ffmpeg","-v","error","-ss",str(t0)]+(["-t",str(d)] if d else [])+["-i",f"sfx/{f}"]+(["-af",",".join(af)] if af else [])+["-ac","1","-ar",str(SR),"-f","f32le","-"]
    return np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,dtype=np.float32).astype(np.float64)
L=np.zeros(n); R=np.zeros(n)
def add(x,t,g=1.0,pan=0.0,fade=0.005):
    s=int(t*SR)
    if s>=n or len(x)==0: return
    x=x[:n-s].copy(); k=min(len(x)//2,int(fade*SR))
    if k>1: x[:k]*=np.linspace(0,1,k); x[-k:]*=np.linspace(1,0,k)
    L[s:s+len(x)]+=x*g*(1-max(0,pan)); R[s:s+len(x)]+=x*g*(1+min(0,pan))
def beep(f,d,g=0.4):
    t=np.arange(int(d*SR))/SR; return np.sin(2*np.pi*f*t)*np.exp(-t*8)*g
def mid(m): return 440*2**((m-69)/12)
# Hook: Einschlag + Countdown 3-2-1-Los
add(load("impact.mp3",0,0.8,lp=4000),0.0,0.5)
for t,f in [(1.76,523),(2.13,659),(2.50,784)]: add(beep(f,0.25,0.35),t)
add(beep(1046,0.5,0.45),2.66)
# Schnitte: Whoosh
for t in [3.32,6.68,12.58,16.70,18.48]: add(load("whoosh.mp3",0,0.7,lp=6000),t-0.12,0.28,fade=0.1)
add(beep(180,0.4,0.5),4.77); add(beep(130,0.5,0.5),4.78)     # NEIN-Bass
# Zahlen: Klacks und Treffer
add(load("click.mp3",0,0.45,lp=5000),7.80,0.7); add(load("click.mp3",0,0.45,lp=5000),8.62,0.7)
for t,m in zip([9.68,10.48,11.15,11.85],[74,76,78,81]): add(load("click.mp3",0,0.45,lp=5000),t,0.55); add(beep(mid(m),0.5,0.3),t+0.02)
add(load("stop.mp3",0,0.9,lp=5000),12.58,0.7)
for k in range(8): add(beep(900+k*70,0.08,0.18),14.0+k*0.18)   # Zaehlwerk 0..162
add(load("chime.mp3",0,1.0,lp=6000),15.92,0.5)
# CTA
add(load("impact.mp3",0,0.9,lp=4500),18.48,0.45); add(load("chime.mp3",0,1.0,lp=6000),19.9,0.4); add(load("chime.mp3",0,1.0,lp=6000),21.17,0.55)
# leises Pulsbett (Kick, 128 BPM) von 3.3 bis 18.4, tief gehalten
t=3.32
while t<18.4:
    ks=np.arange(int(0.25*SR))/SR; add(np.sin(2*np.pi*(48+90*np.exp(-ks*28))*ks)*np.exp(-ks*12)*0.22,t,1.0); t+=60/128
vo=load("vo.mp3"); VL=np.zeros(n); VL[:len(vo)]=vo[:n]
env=np.convolve(np.abs(VL),np.ones(int(0.1*SR))/int(0.1*SR),mode="same"); duck=1-0.7*np.clip(env/0.06,0,1)
mix=np.stack([L*duck+VL*1.5,R*duck+VL*1.5],1); mix[-int(0.4*SR):]*=np.linspace(1,0,int(0.4*SR))[:,None]
mix=mix/np.max(np.abs(mix))*0.9
with wave.open("mix.wav","wb") as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype("<i2").tobytes())
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","mix.wav","-af","loudnorm=I=-14:TP=-1.5:LRA=9","-ar","44100","-c:a","libmp3lame","-b:a","192k","hf/assets/audio.mp3"]); os.remove("mix.wav"); print("fertig")
