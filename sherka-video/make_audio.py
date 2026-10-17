# Synthetischer Soundtrack: Pad + Arpeggio + Whoosh/Pop an den Schnitten
import numpy as np, wave
SR = 44100; DUR = 29.0
n = int(SR * DUR); t = np.arange(n) / SR
rng = np.random.default_rng(7)
def note(f): return 440.0 * 2 ** ((f - 69) / 12)
def env(length, a=0.01, r=0.3):
    e = np.ones(length); na = max(1, min(length // 2, int(a * SR))); nr = max(1, min(length // 2, int(r * SR)))
    e[:na] = np.linspace(0, 1, na); e[-nr:] = np.minimum(e[-nr:], np.linspace(1, 0, nr)); return e
mix = np.zeros(n)
# Akkorde Am - F - C - G, je 2 Takte bei 100 bpm (1 Beat = 0.6 s, Akkord = 4.8 s)
chords = [[57, 60, 64], [53, 57, 60], [48, 55, 64], [55, 59, 62]]
beat = 0.6; seg_len = beat * 8
i = 0
while i * seg_len < DUR:
    ch = chords[i % 4]; st = int(i * seg_len * SR); ln = int(min(seg_len + 0.4, DUR - i * seg_len) * SR)
    tt = np.arange(ln) / SR
    pad = sum(np.sin(2 * np.pi * note(m) * tt) + 0.4 * np.sin(2 * np.pi * note(m) * 2 * tt) for m in ch) / len(ch)
    pad *= env(ln, 0.6, 0.6) * 0.16
    mix[st:st + ln] += pad[: n - st]
    # Arpeggio (Achtel)
    for k in range(16):
        ts = i * seg_len + k * beat / 2
        if ts >= DUR: break
        m = ch[k % 3] + (12 if k % 6 >= 3 else 24)
        l = int(0.45 * SR); tt2 = np.arange(l) / SR
        pl = np.sin(2 * np.pi * note(m) * tt2) * np.exp(-tt2 * 6) * 0.10
        s0 = int(ts * SR); mix[s0:s0 + l] += pl[: n - s0]
    # Bass
    ls = int(seg_len * SR); tt3 = np.arange(ls) / SR
    bass = np.sin(2 * np.pi * note(ch[0] - 12) * tt3) * env(ls, 0.05, 0.3) * 0.22
    s1 = int(i * seg_len * SR); mix[s1:s1 + ls] += bass[: n - s1]
    i += 1
# Sanfter Beat ab 3.5 s
for k in range(int(DUR / beat)):
    ts = k * beat
    if ts < 3.5: continue
    l = int(0.25 * SR); tt4 = np.arange(l) / SR
    kick = np.sin(2 * np.pi * (50 + 90 * np.exp(-tt4 * 25)) * tt4) * np.exp(-tt4 * 12) * 0.35
    s0 = int(ts * SR); mix[s0:s0 + l] += kick[: n - s0]
# Whoosh an den Schnitten und Pop bei Punkten
def whoosh(ts, d=0.7):
    l = int(d * SR); x = rng.standard_normal(l)
    for _ in range(3): x = np.convolve(x, np.ones(24) / 24, mode="same")
    e = np.sin(np.linspace(0, np.pi, l)) ** 2
    s0 = int(ts * SR); mix[s0:s0 + l] += (x * e * 3.2)[: n - s0]
def pop(ts):
    l = int(0.2 * SR); tt5 = np.arange(l) / SR
    p = np.sin(2 * np.pi * 880 * tt5) * np.exp(-tt5 * 22) * 0.22
    s0 = int(ts * SR); mix[s0:s0 + l] += p[: n - s0]
for c in [3.3, 7.6, 11.6, 16.8, 23.0]: whoosh(c)
for p_ in [17.2, 19.0, 20.8, 24.8]: pop(p_ + 0.1)
# Ein- und Ausblenden, Normalisieren
mix *= np.minimum(1, t / 0.5) * np.minimum(1, (DUR - t) / 1.2)
mix = mix / np.max(np.abs(mix)) * 0.8
pcm = (mix * 32767).astype("<i2")
with wave.open("sherka-audio.wav", "wb") as w:
    w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
print("audio ok")
