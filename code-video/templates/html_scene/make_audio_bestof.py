# Soundtrack für bestof.html (24 s, 100 BPM, D-Dur). Zeiten passen zum Plan: Drop 4.2, Pullback 16.2, Wörter 18.6, Atempause 21.0, Hit 21.6.
import numpy as np, wave
SR=44100; DUR=24.0; n=int(SR*DUR); rng=np.random.default_rng(4)
L=np.zeros(n); R=np.zeros(n); BEAT=0.6; BAR=2.4
def mid(m): return 440.0*2**((m-69)/12)
def add(sig,t0,pan=0.0,g=1.0):
    s0=int(t0*SR)
    if s0>=n: return
    sig=sig[:n-s0]; L[s0:s0+len(sig)]+=sig*g*(1-max(0,pan)); R[s0:s0+len(sig)]+=sig*g*(1+min(0,pan))
def tt(d): return np.arange(int(d*SR))/SR
def env(x,a,r):
    e=np.ones(len(x)); na=max(1,min(len(x)//2,int(a*SR))); nr=max(1,min(len(x)//2,int(r*SR)))
    e[:na]=np.linspace(0,1,na); e[-nr:]=np.minimum(e[-nr:],np.linspace(1,0,nr)); return x*e
def lp(x,k):
    for _ in range(2): x=np.convolve(x,np.ones(k)/k,mode="same")
    return x
def noise(d): return rng.standard_normal(int(d*SR))
def marimba(m,v=1.0):
    t=tt(0.7); f=mid(m); return (np.sin(2*np.pi*f*t)+0.35*np.sin(2*np.pi*f*4*t)*np.exp(-t*30)+0.2*np.sin(2*np.pi*f*2*t))*np.exp(-t*7)*0.2*v
def kick():
    t=tt(0.3); return np.sin(2*np.pi*(48+110*np.exp(-t*30))*t)*np.exp(-t*11)*0.55
def clap():
    t=tt(0.22); return lp(noise(0.22),3)*np.exp(-t*24)*0.35
def shaker():
    t=tt(0.08); x=noise(0.08); x=x-lp(x,12); return x*np.exp(-t*55)*0.1
def whoosh(d,g=1.0):
    x=noise(d)
    for _ in range(3): x=np.convolve(x,np.ones(18)/18,mode="same")
    return x*np.sin(np.linspace(0,np.pi,len(x)))**2*4.0*g
def scribble(d=0.35,g=0.5):
    x=noise(d); x=x-lp(x,40); return x*np.sin(np.linspace(0,np.pi,len(x)))*0.5*g
def riser(d,g=1.0):
    t=tt(d); x=noise(d)
    for _ in range(2): x=np.convolve(x,np.ones(10)/10,mode="same")
    return x*(t/d)**2.2*5.0*g+np.sin(2*np.pi*(300+1500*(t/d)**2)*t)*(t/d)**2*0.12*g
def thump(g=1.0):
    t=tt(0.8); return (np.sin(2*np.pi*(150*np.exp(-t*6)+34)*t)*np.exp(-t*4.5)*0.9+lp(noise(0.8),4)*np.exp(-t*18)*0.7)*g
def knock(g=0.5):
    t=tt(0.25); return (np.sin(2*np.pi*(90*np.exp(-t*20)+55)*t)*np.exp(-t*16)*0.8+lp(noise(0.25),6)*np.exp(-t*40)*0.3)*g
def pop(f=660,g=0.25):
    t=tt(0.25); return (np.sin(2*np.pi*f*t)+0.4*np.sin(2*np.pi*f*2*t))*np.exp(-t*18)*g
def click():
    t=tt(0.05); return noise(0.05)*np.exp(-t*90)*0.3
def chime(g=0.3):
    t=tt(1.2); a=np.sin(2*np.pi*mid(81)*t)*np.exp(-t*4); b=np.zeros_like(t); m=t>0.11; tb=t[m]-0.11
    b[m]=np.sin(2*np.pi*mid(88)*tb)*np.exp(-tb*3.5); return (a+b+0.2*np.sin(2*np.pi*mid(93)*t)*np.exp(-t*6))*g
def pad(notes,d,g=0.14):
    t=tt(d); x=sum(np.sin(2*np.pi*mid(m)*t)+0.3*np.sin(2*np.pi*mid(m)*2*t) for m in notes)/len(notes); return env(x,0.35,0.9)*g
chords=[(38,[62,66,69]),(45,[61,64,69]),(47,[62,66,71]),(43,[62,67,71])]
A=[4.2,7.2,10.2,13.2]; DROP=4.2; BREATH=21.0; HIT=21.6
bar=0
while bar*BAR<BREATH:
    t0=bar*BAR; root,tri=chords[bar%4]
    add(env(np.sin(2*np.pi*mid(root)*tt(BAR))*0.3,0.02,0.2),t0)
    step=BEAT/2 if t0>=DROP else BEAT
    for k in range(int(BAR/step)):
        st=t0+k*step
        if st>=BREATH: break
        m=(tri+[tri[0]+12])[(k*3)%4]+(12 if k%2 else 0); add(marimba(m,0.7+0.3*(k%2)),st,pan=(-0.3 if k%2 else 0.3))
    if t0<BREATH-0.5: add(pad(tri,BAR+0.3,0.07),t0)
    bar+=1
t0=DROP
while t0<BREATH-0.01:
    b=round((t0-DROP)/BEAT); add(kick(),t0)
    if b%2==1: add(clap(),t0)
    add(shaker(),t0+BEAT/2,0.2); add(shaker(),t0,-0.2,0.7); t0+=BEAT
add(thump(0.7),DROP-0.02)
# Hook
add(riser(0.17,0.8),0.0); add(thump(1.2),0.17)
for i in range(7): add(pop(900+200*i,0.07),0.25+i*0.07,pan=(-1)**i*0.6)
add(whoosh(0.5,0.5),0.5); add(pop(520,0.2),1.38); add(whoosh(0.9,0.8),1.75); add(pop(700,0.12),2.15); add(pop(840,0.12),2.9)
# Stationen
for k,a in enumerate(A):
    add(pop(660+110*k,0.28),a-0.12); add(whoosh(0.5,0.55),a-0.05); add(pop(990,0.1),a+0.35)
    if k<3: add(whoosh(0.7,0.6),a+2.0)
for k in range(5): add(click(),A[0]+0.55+k*0.05)
add(pop(780,0.12),A[0]+0.5); add(pop(620,0.12),A[0]+1.35)
add(pop(700,0.18),A[1]+0.7); add(pop(930,0.18),A[1]+1.55)
add(click(),A[2]+0.9); add(chime(0.38),A[2]+1.1)
add(pop(800,0.14),A[3]+0.6); add(pop(1040,0.14),A[3]+1.1)
# Rückblick + Rough-Kreise
add(riser(2.4,0.8),16.2); add(whoosh(1.2,0.8),16.4)
for i in range(4): add(scribble(0.4,0.6),16.4+i*0.35,pan=(-1)**i*0.4)
# Wortkarten
for tw_ in [18.75,19.15,19.55,19.95]: add(whoosh(0.3,0.35),tw_-0.35)
for tl_ in [19.35,19.75,20.15,20.55]: add(knock(0.6),tl_)
add(riser(0.6,0.9),BREATH)
# Hit
add(thump(1.3),HIT)
for m,g in zip([50,57,62,66,69,74],[0.2,0.16,0.16,0.14,0.14,0.1]):
    t=tt(2.4); add(np.sin(2*np.pi*mid(m)*t)*np.exp(-t*0.9)*g*env(np.ones(len(t)),0.01,0.8),HIT)
add(marimba(74,1.2),HIT+0.05); add(marimba(81,1.0),HIT+0.12)
add(scribble(0.5,0.7),HIT+0.5); add(pop(660,0.2),HIT+0.8); add(chime(0.3),HIT+0.9); add(marimba(86,1.0),HIT+1.2)
for ch in (L,R):
    d=int(0.27*SR); ch[d:]+=ch[:-d]*0.22; d2=int(0.43*SR); ch[d2:]+=ch[:-d2]*0.12
mix=np.stack([L,R],1); mix[:int(0.02*SR)]*=np.linspace(0,1,int(0.02*SR))[:,None]; mix[-int(0.5*SR):]*=np.linspace(1,0,int(0.5*SR))[:,None]
mix=mix/np.max(np.abs(mix))*0.85
with wave.open("bestof-audio.wav","wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype("<i2").tobytes())
print("audio ok")
