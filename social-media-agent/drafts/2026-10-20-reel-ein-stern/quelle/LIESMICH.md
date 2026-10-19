# Reel neu bauen

Voraussetzung: Python mit numpy, Pillow, playwright (Chromium unter /opt/pw-browsers), ffmpeg.

```bash
cd quelle
for f in vo/*.mp3; do ffmpeg -v error -y -i "$f" -ar 44100 -ac 1 "${f%.mp3}.wav"; done
python3 edl.py                         # Timeline aus Stimm-Clips -> timings.js + mix_raw.wav
ffmpeg -y -i mix_raw.wav -af "loudnorm=I=-14:TP=-1.5:LRA=11,alimiter=limit=0.85:level=false" -ar 44100 mix.wav
python3 shoot.py frames                # rendert render(t) Frame für Frame (30 fps)
ffmpeg -y -framerate 30 -i frames/f%04d.jpg -i mix.wav -c:v libx264 -crf 17 -pix_fmt yuv420p -map 0:v -map 1:a -frames:v 649 -c:a aac -b:a 192k out.mp4
```

Stimmen (ElevenLabs, eleven_v4): A = Irene UGC (Kundin), B = Jonas (brummig), C = Lenny (gelangweilt), N = Mary Kai (Erzählerin). A2new/C2new sind Neuaufnahmen, weil "Wirkte" und "Hat" undeutlich waren.
