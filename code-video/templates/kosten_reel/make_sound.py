# "Die versteckten Kosten" (14.4 s): Stimme (ElevenLabs Turbo Tim) + Ticken des Zeitmessers + Whooshes + Alarm bei 2,5 s.
import numpy as np, subprocess, wave, os
SR=44100; DUR=14.4; n=int(SR*DUR)
def load(f,t0=0.0,d=None,lp=None):
    af=[f"lowpass=f={lp}"] if lp else []
    cmd=["ffmpeg","-v","error","-ss",str(t0)]+(["-t",str(d)] if d else [])+["-i",f"sfx/{f}"]+(["-af",",".join(af)] if af else [])+["-ac","1","-ar",str(SR),"-f","f32le","-"]
    return np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,dtype=np.float32).astype(np.float64)
L=np.zeros(n); R=np.zeros(n)
def add(x,t,g=1.0,fade=0.005):
    s=int(t*SR)
    if s>=n or len(x)==0: return
    x=x[:n-s].copy(); k=min(len(x)//2,int(fade*SR))
    if k>1: x[:k]*=np.linspace(0,1,k); x[-k:]*=np.linspace(1,0,k)
    L[s:s+len(x)]+=x*g; R[s:s+len(x)]+=x*g
def beep(f,d,g=0.4):
    t=np.arange(int(d*SR))/SR; return np.sin(2*np.pi*f*t)*np.exp(-t*8)*g
add(load("impact.mp3",0,0.8,lp=4000),0.18,0.5)
for t in [1.68,2.92,6.80,8.33,10.20,11.55]: add(load("whoosh.mp3",0,0.6,lp=6000),t-0.1,0.25,fade=0.08)
# Zeitmesser: Ticks im Takt, ab 2,5 s (t=6.80) tiefer
for k in range(int((6.80-4.45)/0.235)): add(load("click.mp3",0,0.4,lp=5000),4.45+k*0.235,0.45)
for k in range(int((8.33-6.80)/0.15)): add(beep(300,0.1,0.28),6.80+k*0.15)
add(beep(150,0.5,0.5),6.80)
add(load("impact.mp3",0,0.9,lp=4500),12.78,0.45); add(load("chime.mp3",0,1.0,lp=6000),13.4,0.5)
vo=load("vo.mp3"); VL=np.zeros(n); VL[:len(vo)]=vo[:n]
env=np.convolve(np.abs(VL),np.ones(int(0.1*SR))/int(0.1*SR),mode="same"); duck=1-0.7*np.clip(env/0.06,0,1)
mix=np.stack([L*duck+VL*1.5,R*duck+VL*1.5],1); mix[-int(0.4*SR):]*=np.linspace(1,0,int(0.4*SR))[:,None]
mix=mix/np.max(np.abs(mix))*0.9
with wave.open("mix.wav","wb") as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype("<i2").tobytes())
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","mix.wav","-af","loudnorm=I=-14:TP=-1.5:LRA=9","-ar","44100","-c:a","libmp3lame","-b:a","192k","hf/assets/audio.mp3"]); os.remove("mix.wav"); print("fertig")
