# "Unsichtbar" (13.6 s): Turbo-Tim-Stimme + dunkler 808-Puls (140 BPM) + Cowbell-Offbeats + NEIN-Einschlag + Whooshes.
import numpy as np, subprocess, wave, os
SR=44100; DUR=13.6; n=int(SR*DUR)
def load(f,t0=0.0,d=None,lp=None):
    af=[f"lowpass=f={lp}"] if lp else []
    cmd=["ffmpeg","-v","error","-ss",str(t0)]+(["-t",str(d)] if d else [])+["-i",f"sfx/{f}"]+(["-af",",".join(af)] if af else [])+["-ac","1","-ar",str(SR),"-f","f32le","-"]
    return np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,dtype=np.float32).astype(np.float64)
L=np.zeros(n); R=np.zeros(n)
def add(x,t,g=1.0,fade=0.004):
    s=int(t*SR)
    if s>=n or len(x)==0: return
    x=x[:n-s].copy(); k=min(len(x)//2,int(fade*SR))
    if k>1: x[:k]*=np.linspace(0,1,k); x[-k:]*=np.linspace(1,0,k)
    L[s:s+len(x)]+=x*g; R[s:s+len(x)]+=x*g
def kick(g):
    t=np.arange(int(0.45*SR))/SR; return np.sin(2*np.pi*(42+110*np.exp(-t*30))*t)*np.exp(-t*7)*g
def cow(g):
    t=np.arange(int(0.18*SR))/SR; x=(np.sign(np.sin(2*np.pi*587*t))+np.sign(np.sin(2*np.pi*845*t)))*np.exp(-t*24)*g
    return x
add(load("impact.mp3",0,0.9,lp=4000),0.10,0.5)
B=60/140
t=0.10+B
while t<12.7:
    add(kick(0.42),t,1.0)
    if int(round((t-0.10)/B))%2==0: add(kick(0.30),t+B*0.75,1.0)
    add(cow(0.05),t+B*0.5,1.0)
    t+=B
for tt in [1.82,3.30,4.76,5.76,7.76,10.02,12.22]: add(load("whoosh.mp3",0,0.6,lp=6000),tt-0.1,0.22,fade=0.08)
add(load("impact.mp3",0,1.0,lp=3500),7.14,0.9)         # NEIN
t0=np.arange(int(0.9*SR))/SR; add(np.sin(2*np.pi*(38+60*np.exp(-t0*9))*t0)*np.exp(-t0*3.5)*0.9,7.14)
add(load("chime.mp3",0,1.0,lp=6000),12.22,0.5)
vo=load("vo.mp3"); VL=np.zeros(n); VL[:len(vo)]=vo[:n]
env=np.convolve(np.abs(VL),np.ones(int(0.1*SR))/int(0.1*SR),mode="same"); duck=1-0.65*np.clip(env/0.06,0,1)
mix=np.stack([L*duck+VL*1.5,R*duck+VL*1.5],1); mix[-int(0.5*SR):]*=np.linspace(1,0,int(0.5*SR))[:,None]
mix=mix/np.max(np.abs(mix))*0.9
with wave.open("mix.wav","wb") as w: w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype("<i2").tobytes())
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","mix.wav","-af","loudnorm=I=-14:TP=-1.5:LRA=9","-ar","44100","-c:a","libmp3lame","-b:a","192k","hf/assets/audio.mp3"]); os.remove("mix.wav"); print("fertig")
