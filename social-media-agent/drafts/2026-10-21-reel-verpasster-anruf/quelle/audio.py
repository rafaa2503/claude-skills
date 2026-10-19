import numpy as np, wave
sr=44100; D=17.0
a=np.zeros(int(sr*D))
def add(t0,x,g=1.0):
    i=int(t0*sr); j=min(len(a),i+len(x)); a[i:j]+=g*x[:j-i]
def tone(f,dur,decay=None,harm=(1,)):
    t=np.arange(int(dur*sr))/sr
    x=sum(np.sin(2*np.pi*f*h*t)/h for h in harm)
    env=np.minimum(1,t/0.004)*(np.exp(-t/decay) if decay else np.minimum(1,(dur-t)/0.01))
    return x*env
def ring(t0,t1):
    # pulses 0.14 on / 0.11 off x2, gap to 0.9s cycle
    t=t0
    while t<t1:
        for k in range(2):
            s=t+k*0.25
            if s<t1: add(s,tone(1046,0.14,harm=(1,2)) * 0.22 + tone(1318,0.14)*0.12,1)
        t+=0.9
ring(0.0,4.0)
ring(16.7,17.0)
# thud at 4.0
t=np.arange(int(0.35*sr))/sr; add(4.0,np.sin(2*np.pi*(80-40*t)*t)*np.exp(-t/0.08)*0.9)
# typing ticks 5.6-8.0
rng=np.random.default_rng(3)
for s in np.arange(5.7,7.9,0.17)+rng.random(13)[:13].clip(0,1)*0.05:
    t=np.arange(int(0.03*sr))/sr; add(float(s),rng.standard_normal(len(t))*np.exp(-t/0.006)*0.25)
# tap click 8.85
t=np.arange(int(0.05*sr))/sr; add(8.85,np.sin(2*np.pi*700*t)*np.exp(-t/0.012)*0.4)
# pling 9.2
add(9.2,tone(1318,0.7,0.18)*0.35+tone(1760,0.7,0.12)*0.2)
# message pops
add(11.15,tone(660,0.15,0.04)*0.3); add(12.2,tone(880,0.2,0.06)*0.3)
# low tone at 13.5
add(13.5,tone(110,1.4,0.5,harm=(1,2))*0.45)
# soft pop for Nur erreichbar
add(14.9,tone(220,0.5,0.15)*0.2)
a=np.tanh(a*1.2)*0.9
pcm=(a*32767).astype(np.int16)
w=wave.open('audio.wav','wb');w.setnchannels(1);w.setsampwidth(2);w.setframerate(sr);w.writeframes(pcm.tobytes());w.close()
