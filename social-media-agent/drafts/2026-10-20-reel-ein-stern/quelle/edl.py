# Baut Timeline aus echten Stimm-Clips: timings.js (fuer render) + mix.wav (Stimmen + SFX)
import numpy as np, wave, json
SR=44100
def load(f):
    w=wave.open(f'vo/{f}.wav'); a=np.frombuffer(w.readframes(w.getnframes()),np.int16).astype(np.float32)/32768; return a
SRC={k:load(k) for k in ['A','B','C','N','A2new','C2new']}
# (quelle, start, ende) in Sekunden, aus silencedetect + whisper
CL={
 'A1':('A2new',0.13,0.99),'A2':('A2new',1.47,2.32),'A3':('A2new',2.61,3.24),'F1':('A',4.62,5.27),
 'B1':('B',0.00,0.78),'B2':('B',1.32,2.16),'F2':('B',2.74,3.73),'F4':('B',4.42,5.08),
 'C1':('C2new',0.17,0.81),'C2':('C2new',1.29,1.85),'F3':('C',2.47,3.20),
 'N1':('N',0.20,1.93),'N2':('N',2.87,3.45),'N3':('N',4.45,5.27),'N4':('N',5.98,7.24),
 'N5':('N',8.02,9.11),'N6':('N',9.74,10.93),'N7a':('N',11.66,12.82),'N7b':('N',13.38,14.24),
}
def clip(k):
    s,a,b=CL[k]; x=SRC[s][int(a*SR):int(b*SR)].copy()
    if s!='N':  # Kundenstimmen auf -24 dBFS aktive Sprache
        r=np.sqrt(np.convolve(x**2,np.ones(441)/441,'same')); act=x[r>0.01]
        x*=10**((-24-20*np.log10(np.sqrt(np.mean(act**2))))/20)
    f=int(0.008*SR); x[:f]*=np.linspace(0,1,f); x[-f*3:]*=np.linspace(1,0,f*3); return x
def dur(k): return CL[k][2]-CL[k][1]
T={}; place=[]
def put(k,t,g=1.0,cust=False):
    place.append((k,t,g,cust)); T[k]=round(t,3); T[k+'_end']=round(t+dur(k),3)
# ---- Timeline ----
put('A1',0.03,cust=True)
put('A2',T['A1_end']+0.10,cust=True)
put('A3',T['A2_end']+0.08,cust=True)
T['card2']=round(T['A3_end']+0.08,3)
put('B1',T['card2']+0.03,cust=True)
put('B2',T['B1_end']+0.14,cust=True)
T['card3']=round(T['B2_end']+0.08,3)
put('C1',T['card3']+0.03,cust=True)
put('C2',T['C1_end']+0.08,cust=True)
f0=round(T['C2_end']+0.10,3)
T['flood']=[f0,f0+0.28,f0+0.56,f0+0.84]
put('F1',f0+0.02,cust=True); put('F2',f0+0.30,0.30,cust=True); put('F3',f0+0.58,0.30,cust=True); put('F4',f0+0.86,cust=True)
T['q']=round(T['F4_end']+0.06,3)
put('N1',T['q']+0.05)
c0=T['q']+0.30
T['cd']=[round(T['N1']+x,3) for x in (0.20,0.48,0.82,1.12,1.34,1.60,1.85)]  # 7..1, auf Wortgrenzen
T['zero']=round(max(T['cd'][-1]+0.55,T['N1_end']+0.25),3)
put('N2',T['zero']+0.06)
put('N3',T['N2_end']+0.12)
T['phone']=round(T['N3_end']+0.05,3)
put('N4',T['phone']+0.12)
t=T['N4_end']+0.06; T['cu']=[]
for k in ('A2','B2','C1'):  # Slot = Echo-Laenge, kein Ueberlappen
    T['cu'].append(round(t,3)); place.append((k,t+0.03,0.85,True)); T['echo'+k[0]]=round(t+0.03,3)
    t+=0.03+dur(k)+0.05
T['del']=round(t,3)
put('N5',T['del']+0.04)
T['call']=round(T['N5_end']+0.10,3)
put('N6',T['call']+0.02)
T['end1']=round(T['N6_end']+0.12,3)
put('N7a',T['end1']+0.03)
put('N7b',T['N7a_end']+0.10)
T['stars']=round(T['N7b']+0.36,3)
T['hes']=round(T['N7b_end']+0.08,3)
T['snap']=round(T['hes']+0.62,3)
T['loop']=round(T['snap']+0.45,3)
T['total']=round(round((T['loop']+0.20)*30)/30,4)
# Wort-Zeiten (relativ) fuer Einstempeln, aus whisper
T['w_A2']=[0.01,0.26,0.51]; T['w_A3']=[0.02,0.27,0.48]; T['w_B2']=[0.01,0.29]; T['w_C2']=[0.03,0.25]
N=int(T['total']*SR)+1
vo=np.zeros(N); 
from numpy.fft import rfft, irfft
def bandpass(x,lo,hi):
    X=rfft(x); f=np.fft.rfftfreq(len(x),1/SR); X[(f<lo)|(f>hi)]*=0.05; return irfft(X,len(x))
for k,t,g,cust in place:
    x=clip(k)*g
    if cust: x=bandpass(x,200,6000)*1.1
    i=int(t*SR); j=min(N,i+len(x)); vo[i:j]+=x[:j-i]
# ---- SFX ----
sfx=np.zeros(N)
rng=np.random.default_rng(7)
def add(t,x,g=1.0):
    i=int(t*SR)
    if i<0: x=x[-i:]; i=0
    j=min(N,i+len(x)); sfx[i:j]+=g*x[:j-i]
def env(n,att=0.002,dec=0.1):
    t=np.arange(n)/SR; return np.minimum(1,t/att)*np.exp(-t/dec)
def thud(g=1.0,f0=90,f1=45,d=0.28):
    n=int(d*SR); t=np.arange(n)/SR; f=f0+(f1-f0)*t/d; ph=2*np.pi*np.cumsum(f)/SR
    body=np.sin(ph)*env(n,0.001,0.07)
    noise=rng.standard_normal(n)*env(n,0.0005,0.006)*0.5
    slap=bandpass(rng.standard_normal(int(0.02*SR)),1000,3000)*env(int(0.02*SR),0.0005,0.004)*0.8
    out=body+noise; out[:len(slap)]+=slap; return out*g
def tick(f=2000,d=0.01,g=0.2):
    n=int(d*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*f*t)*env(n,0.0005,d/3)*g
def whoosh(d=0.18,lo=300,hi=2500,g=0.25,rev=False,rise=False):
    n=int(d*SR); x=rng.standard_normal(n); out=np.zeros(n); seg=int(0.01*SR)
    for s in range(0,n,seg):
        p=s/n; p=1-p if rev else p; fc=lo+(hi-lo)*p
        out[s:s+seg]=bandpass(x[s:s+seg] if len(x[s:s+seg])>8 else np.zeros(seg)[:len(x[s:s+seg])],fc*0.6,fc*1.4) if len(x[s:s+seg])>8 else 0
    e=(np.arange(n)/n)**1.5 if rise else np.sin(np.pi*np.arange(n)/n)
    f=int(0.004*SR); e[-f:]*=np.linspace(1,0,f); return out*e*g
def bass(d=0.9,g=0.9):
    n=int(d*SR); t=np.arange(n)/SR; f=55-20*t/d; ph=2*np.pi*np.cumsum(f)/SR; return np.tanh(np.sin(ph)*2.5)*np.exp(-t/0.35)*g
# Karten
add(0,thud(1.0)); add(0,tick(2400,0.006,0.25))
for t in T['w_A3']: add(T['A3']+t,tick(1800,0.01,0.12))
for c in ('card2','card3'):
    add(T[c]-0.18,whoosh(rise=True)); add(T[c],thud(0.9)); add(T[c],tick(2400,0.006,0.22))
for k in ('A2','B2','C2'):
    for o in T['w_'+k]: add(T[k]+o,tick(1800,0.01,0.12))
add(T['A1']+0.42,tick(2400,0.006,0.15))
for k,t in enumerate(T['flood']): add(t,thud(0.75*(0.9**k),70,50,0.12)); add(t,tick(2400,0.006,0.2))
# Frage-Wusch, Countdown
add(T['q'],whoosh(0.25,2000,400,0.18))
for k,t in enumerate(T['cd']):
    add(t,tick(1400 if k>=5 else 2000,0.009,0.28))
add(T['cd'][-1]+0.22,tick(1300,0.01,0.22))
add(T['zero'],bass()); add(T['zero'],thud(0.6))
add(T['phone'],whoosh(0.45,2500,300,0.2))
for t in T['cu']: add(t,rng.standard_normal(int(0.008*SR))*0.25); add(t+0.2,tick(1600,0.012,0.15))
# Backspace
bs0=T['del']+0.28
for i in range(17):
    add(bs0+i/30,bandpass(rng.standard_normal(int(0.006*SR)),3000,5000)*env(int(0.006*SR),0.0003,0.002)*(0.35+0.1*rng.random()))
# Freizeichen CH 425 Hz
n=int(1.0*SR); tt=np.arange(n)/SR; tone=np.sin(2*np.pi*425*tt)*0.13; tone[:400]*=np.linspace(0,1,400); tone[-400:]*=np.linspace(1,0,400)
add(T['call'],bandpass(tone,300,3400))
add(T['end1'],thud(0.5,60,40,0.3))
for i in range(5): add(T['stars']+i*0.066,tick(1800,0.008,0.08))
for i,f in enumerate((900,1000,1120)): add(T['hes']+i*0.1,tick(f,0.03,0.15))
nb=int(0.06*SR); tb=np.arange(nb)/SR; fb=1120-520*tb/0.06; add(T['hes']+0.38,np.sin(2*np.pi*np.cumsum(fb)/SR)*np.exp(-tb/0.03)*0.15)
add(T['snap'],tick(3000,0.01,0.3)); add(T['snap'],thud(0.35,200,120,0.08))
add(T['loop'],whoosh(0.2,400,2500,0.25,rise=True))
# Raumrauschen
room=bandpass(rng.standard_normal(N),100,4000)*0.004
z0=int((T['zero']-0.07)*SR); room[z0:int(T['zero']*SR)]=0
mix=vo*1.0+sfx*0.8+room
mix=mix/np.max(np.abs(mix))*0.95
w=wave.open('mix_raw.wav','wb'); w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix*32767).astype(np.int16).tobytes()); w.close()
open('timings.js','w').write('window.T='+json.dumps(T)+';')
print(json.dumps(T))
