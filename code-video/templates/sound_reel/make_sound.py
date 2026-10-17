# Soundgetriebenes Reel "Der Klang einer guten Website" (21.6 s): echte ElevenLabs-SFX + Jan-Voice + Ping-Melodie als Musik.
# Eingabe: sfx/*.mp3 (vo, wind, keys, click, whoosh, impact, riser, chime, launch, buzz). Ausgabe: sound-mix.mp3 + pings.json (Zeiten/Noten fürs Bild).
import numpy as np, json, subprocess, wave, os
SR=44100; DUR=21.6; n=int(SR*DUR); rng=np.random.default_rng(3)
def load(f,t0=0.0,d=None):
    cmd=["ffmpeg","-v","error","-ss",str(t0)]+(["-t",str(d)] if d else [])+["-i",f"sfx/{f}","-ac","1","-ar",str(SR),"-f","f32le","-"]
    return np.frombuffer(subprocess.run(cmd,capture_output=True).stdout,dtype=np.float32).astype(np.float64)
L=np.zeros(n); R=np.zeros(n)
def add(x,t,g=1.0,pan=0.0,fade=0.01):
    s=int(t*SR)
    if s>=n: return
    x=x[:n-s].copy(); k=min(len(x)//2,int(fade*SR))
    if k>1: x[:k]*=np.linspace(0,1,k); x[-k:]*=np.linspace(1,0,k)
    L[s:s+len(x)]+=x*g*(1-max(0,pan)); R[s:s+len(x)]+=x*g*(1+min(0,pan))
def mid(m): return 440*2**((m-69)/12)
def tone(f,d,g=1.0,dec=4.0,harm=(1,2.0,3.0),hg=(1,.4,.2)):
    t=np.arange(int(d*SR))/SR; return sum(a*np.sin(2*np.pi*f*h*t) for h,a in zip(harm,hg))*np.exp(-t*dec)*g*0.5
# ---- Ton-Plan (Sekunden) ----
VO=[("vo.mp3",0.0,2.76,0.5),("vo.mp3",4.18,6.26,3.6),("vo.mp3",7.41,10.67,7.7),("vo.mp3",12.08,14.27,12.6),("vo.mp3",16.01,18.68,17.0)]
# Stille: Windbett + Wind-SFX
bed=rng.standard_normal(int(3.6*SR))
for _ in range(3): bed=np.convolve(bed,np.ones(60)/60,mode="same")
bed*=np.linspace(0.5,0,len(bed))*0.9; add(bed,0.0,0.5,fade=0.2)
w=load("wind.mp3"); add(w,0.2,0.7,-0.3,0.2); add(w,1.6,0.5,0.3,0.2)
# Bauen
add(load("keys.mp3"),3.45,0.8); add(load("whoosh.mp3",0,1.0),3.3,0.35,fade=0.15)
add(load("click.mp3",0,0.6),5.0,0.9); add(load("chime.mp3"),5.28,0.6); add(load("launch.mp3"),6.3,0.9)
add(load("riser.mp3"),5.2,0.7,fade=0.05)
# Handy meldet sich
add(load("buzz.mp3",0,1.2),7.2,0.9,fade=0.05)
# Ping-Melodie (D-Dur-Pentatonik) = die Musik
PENT=[74,76,78,81,83,86]   # D5 E5 F#5 A5 B5 D6
free=[(7.45,0),(8.05,2),(8.65,3),(9.0,4),(9.3,2),(9.6,4),(9.8,5),(10.0,3),(10.2,5),(10.4,4),(10.6,5)]
pat=[0,2,4,2,3,5,4,2, 1,3,4,3,2,4,5,3]
pings=[]; t=10.8; i=0
while t<16.2-1e-6: pings.append((round(t,3),pat[i%len(pat)])); t+=0.3; i+=1
pings=free+pings
for tt,k in pings:
    add(tone(mid(PENT[k]),1.0,0.55,4.5),tt,1.0,pan=((k%3)-1)*0.4)
# Bett: Pad ab 7.2, Kick ab 9.6, Bass
chords=[(38,[62,66,69]),(43,[62,67,71]),(47,[62,66,71]),(45,[61,64,69])]
bar=0
while 7.2+bar*2.4<16.2:
    t0=7.2+bar*2.4; root,tri=chords[bar%4]
    tt=np.arange(int(2.6*SR))/SR
    pad=sum(np.sin(2*np.pi*mid(m-12)*tt) for m in tri)/3
    k=int(0.5*SR); e=np.ones(len(tt)); e[:k]=np.linspace(0,1,k); e[-k:]=np.linspace(1,0,k)
    add(pad*e*0.16,t0,1.0,fade=0.01)
    if t0>=9.6: add(np.sin(2*np.pi*mid(root)*tt[:int(2.4*SR)])*np.exp(-tt[:int(2.4*SR)]*0.8)*0.25,t0,1.0)
    bar+=1
t=9.6
while t<16.2-1e-6:
    ks=np.arange(int(0.3*SR))/SR; kick=np.sin(2*np.pi*(48+110*np.exp(-ks*30))*ks)*np.exp(-ks*11)*0.6; add(kick,t,1.0)
    hs=rng.standard_normal(int(0.07*SR)); hs=hs-np.convolve(hs,np.ones(10)/10,mode="same"); add(hs*np.exp(-np.arange(len(hs))/SR*60)*0.12,t+0.3,1.0)
    t+=0.6
# Atempause + Schlag + Abschluss
add(load("whoosh.mp3",0,0.9),15.9,0.5,fade=0.2)
add(load("impact.mp3"),16.8,1.1)
for m,g in zip([50,57,62,66,69,74],[.2,.16,.16,.14,.14,.1]):
    tt=np.arange(int(3.0*SR))/SR; add(np.sin(2*np.pi*mid(m)*tt)*np.exp(-tt*0.9)*g,16.8,1.0,fade=0.02)
add(load("chime.mp3"),19.95,0.7)
add(tone(mid(86),1.4,0.6,3.0),20.1,1.0)
# Stimme
vo=[]
for f,a,b,t0 in VO:
    x=load(f,a-0.03 if a>0 else 0,b-a+0.18); vo.append((x,t0))
VL=np.zeros(n)
for x,t0 in vo:
    s=int(t0*SR); k=int(0.02*SR); x=x.copy(); x[:k]*=np.linspace(0,1,k); x[-int(0.08*SR):]*=np.linspace(1,0,int(0.08*SR)); VL[s:s+len(x)]+=x[:n-s]
env=np.abs(VL); env=np.convolve(env,np.ones(int(0.12*SR))/int(0.12*SR),mode="same"); duck=1-0.65*np.clip(env/0.08,0,1)
duck=np.convolve(duck,np.ones(int(0.08*SR))/int(0.08*SR),mode="same")
music_L=L*duck; music_R=R*duck
mix=np.stack([music_L+VL*1.4, music_R+VL*1.4],1)
mix[-int(0.5*SR):]*=np.linspace(1,0,int(0.5*SR))[:,None]
mix=mix/np.max(np.abs(mix))*0.9
with wave.open("sound-mix.wav","wb") as wv:
    wv.setnchannels(2); wv.setsampwidth(2); wv.setframerate(SR); wv.writeframes((mix*32767).astype("<i2").tobytes())
subprocess.run(["ffmpeg","-y","-loglevel","error","-i","sound-mix.wav","-af","loudnorm=I=-14:TP=-1.5:LRA=9","-ar","44100","-c:a","libmp3lame","-b:a","192k","sound-mix.mp3"])
os.remove("sound-mix.wav")
json.dump({"pings":[[t,k] for t,k in pings]},open("pings.json","w"))
print("fertig",len(pings),"Pings")
