# Soundtrack für "Der Weg": Marimba, Sub, Beat ab dem Drop (4.8 s), SFX auf jedem Bildmoment. 100 BPM, D-Dur.
import numpy as np, wave
SR = 44100; DUR = 21.6
n = int(SR * DUR); rng = np.random.default_rng(4)
L = np.zeros(n); R = np.zeros(n)
BEAT = 0.6; BAR = 2.4
def mid(m): return 440.0 * 2 ** ((m - 69) / 12)
def add(sig, t0, pan=0.0, g=1.0):
    s0 = int(t0 * SR)
    if s0 >= n or s0 + len(sig) <= 0: return
    a = max(0, -s0); sig = sig[a:]; s0 = max(0, s0)
    sig = sig[: n - s0]
    L[s0:s0 + len(sig)] += sig * g * (1 - max(0, pan)); R[s0:s0 + len(sig)] += sig * g * (1 + min(0, pan))
def tt(d): return np.arange(int(d * SR)) / SR
def env(x, a, r):
    e = np.ones(len(x)); na = max(1, min(len(x) // 2, int(a * SR))); nr = max(1, min(len(x) // 2, int(r * SR)))
    e[:na] = np.linspace(0, 1, na); e[-nr:] = np.minimum(e[-nr:], np.linspace(1, 0, nr)); return x * e
def lp(x, k):
    for _ in range(2): x = np.convolve(x, np.ones(k) / k, mode="same")
    return x
def noise(d): return rng.standard_normal(int(d * SR))
def marimba(m, vel=1.0):
    t = tt(0.7); f = mid(m)
    return (np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * f * 4 * t) * np.exp(-t * 30) + 0.2 * np.sin(2 * np.pi * f * 2 * t)) * np.exp(-t * 7) * 0.2 * vel
def kick():
    t = tt(0.3); return np.sin(2 * np.pi * (48 + 110 * np.exp(-t * 30)) * t) * np.exp(-t * 11) * 0.55
def clap():
    t = tt(0.22); return lp(noise(0.22), 3) * np.exp(-t * 24) * 0.35
def shaker():
    t = tt(0.08); x = noise(0.08); x = x - lp(x, 12); return x * np.exp(-t * 55) * 0.1
def whoosh(d, g=1.0, up=True):
    x = noise(d)
    for _ in range(3): x = np.convolve(x, np.ones(18) / 18, mode="same")
    e = np.sin(np.linspace(0, np.pi, len(x))) ** 2 if up else np.linspace(1, 0, len(x)) ** 2
    return x * e * 4.0 * g
def riser(d, g=1.0):
    t = tt(d); x = noise(d)
    for _ in range(2): x = np.convolve(x, np.ones(10) / 10, mode="same")
    return x * (t / d) ** 2.2 * 5.0 * g + np.sin(2 * np.pi * (300 + 1500 * (t / d) ** 2) * t) * (t / d) ** 2 * 0.12 * g
def thump():
    t = tt(0.8); return np.sin(2 * np.pi * (150 * np.exp(-t * 6) + 34) * t) * np.exp(-t * 4.5) * 0.9 + lp(noise(0.8), 4) * np.exp(-t * 18) * 0.7
def pop(f=660, g=0.25):
    t = tt(0.25); return (np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * f * 2 * t)) * np.exp(-t * 18) * g
def click():
    t = tt(0.05); return noise(0.05) * np.exp(-t * 90) * 0.3
def chime(g=0.3):
    t = tt(1.2)
    a = np.sin(2 * np.pi * mid(81) * t) * np.exp(-t * 4)
    b = np.zeros_like(t); m = t > 0.11; tb = t[m] - 0.11; b[m] = np.sin(2 * np.pi * mid(88) * tb) * np.exp(-tb * 3.5)
    return (a + b + 0.2 * np.sin(2 * np.pi * mid(93) * t) * np.exp(-t * 6)) * g
def pad(notes, d, g=0.14):
    t = tt(d); x = sum(np.sin(2 * np.pi * mid(m) * t) + 0.3 * np.sin(2 * np.pi * mid(m) * 2 * t) for m in notes) / len(notes)
    return env(x, 0.35, 0.9) * g

chords = [(38, [62, 66, 69]), (45, [61, 64, 69]), (47, [62, 66, 71]), (43, [62, 67, 71])]  # D, A, Bm, G
DROP, BREATH, HIT = 4.8, 16.2, 16.8
bar = 0
while bar * BAR < BREATH:
    t0 = bar * BAR; root, tri = chords[bar % 4]
    # Sub
    t = tt(BAR); sub = np.sin(2 * np.pi * mid(root) * t) * 0.3
    add(env(sub, 0.02, 0.2), t0, 0, 1.0 if t0 < BREATH - 0.2 else 0)
    # Marimba (8tel) - sparsamer vor dem Drop
    for k in range(8 if t0 >= DROP else 4):
        st = t0 + k * (BEAT / 2 if t0 >= DROP else BEAT)
        if st >= BREATH: break
        m = (tri + [tri[0] + 12])[(k * 3) % 4] + (12 if k % 2 else 0)
        add(marimba(m, 0.7 + 0.3 * (k % 2)), st, pan=(-0.3 if k % 2 else 0.3))
    # Pad
    if t0 < BREATH - 0.5: add(pad(tri, BAR + 0.3, 0.07), t0)
    bar += 1
# Beat ab Drop
t0 = DROP
while t0 < BREATH - 0.01:
    b = round((t0 - DROP) / BEAT)
    if b % 1 == 0: add(kick(), t0)
    if b % 2 == 1: add(clap(), t0)
    add(shaker(), t0 + BEAT / 2, 0.2); add(shaker(), t0, -0.2, 0.7)
    t0 += BEAT
add(thump(), DROP - 0.02, 0, 0.7)
# SFX
add(riser(0.17, 0.8), 0.0); add(thump(), 0.17, 0, 1.2)
for i in range(7): add(pop(900 + 200 * i, 0.07), 0.25 + i * 0.07, pan=(-1) ** i * 0.6)
add(whoosh(0.5, 0.5), 0.5); add(pop(520, 0.2), 1.38); add(whoosh(0.75, 0.9), 1.67)
for k, a in enumerate([2.4, 4.8, 7.2, 9.6]):
    add(pop(660 + 110 * k, 0.28), a - 0.12); add(whoosh(0.5, 0.55), a - 0.05); add(pop(990, 0.1), a + 0.35)
    add(whoosh(0.6, 0.6), a + 1.5)
for k in range(5): add(click(), 2.4 + 0.55 + k * 0.05); 
add(pop(780, 0.12), 2.4 + 0.5); add(pop(620, 0.12), 2.4 + 1.35); add(pop(700, 0.18), 4.8 + 0.7); add(pop(930, 0.18), 4.8 + 1.55)
add(click(), 7.2 + 0.9); add(chime(0.38), 7.2 + 1.1); add(pop(800, 0.14), 9.6 + 0.6); add(pop(1040, 0.14), 9.6 + 1.1)
add(riser(2.4, 0.8), 12.0); add(whoosh(1.2, 0.8), 12.2)
add(whoosh(0.6, 0.7), 14.65); add(whoosh(0.6, 0.7), 15.0); add(whoosh(0.7, 0.6), 15.5)
add(riser(0.6, 0.9), 16.2)   # Atempause: nur Reverse-Swell
add(whoosh(0.35, 0.6, True), 16.45)
# Hit
add(thump(), HIT, 0, 1.3)
for m, g in zip([50, 57, 62, 66, 69, 74], [0.2, 0.16, 0.16, 0.14, 0.14, 0.1]):
    t = tt(4.8); add(np.sin(2 * np.pi * mid(m) * t) * np.exp(-t * 0.9) * g * env(np.ones(len(t)), 0.01, 0.8), HIT)
add(marimba(74, 1.2), HIT + 0.05); add(marimba(81, 1.0), HIT + 0.12)
add(pop(660, 0.2), 17.55); add(pop(880, 0.18), 18.2); add(chime(0.3), 18.3)
add(pop(1100, 0.1), 19.3); add(marimba(86, 1.1), 19.35)
# Raum: einfaches Echo
for ch in (L, R):
    d = int(0.27 * SR); ch[d:] += ch[:-d] * 0.22; d2 = int(0.43 * SR); ch[d2:] += ch[:-d2] * 0.12
mix = np.stack([L, R], 1)
mix[:int(0.02 * SR)] *= np.linspace(0, 1, int(0.02 * SR))[:, None]
mix[-int(0.4 * SR):] *= np.linspace(1, 0, int(0.4 * SR))[:, None]
mix = mix / np.max(np.abs(mix)) * 0.85
pcm = (mix * 32767).astype("<i2")
with wave.open("sherka-path-audio.wav", "wb") as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print("audio ok")
