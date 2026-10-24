---
name: video-schnitt
description: Echte Aufnahmen schneiden (Handy-Take, Bildschirmaufnahme mit Stimme, fremder Clip mit Ton): Pausen raus, Stimme säubern, Wort-Untertitel, Pflicht-Check. Nur nutzen, wenn echtes Material mit Stimme existiert, nicht für reine Code-Animationen.
---

# Video-Schnitt (echtes Material)

Quelle: Starter-Kit @weblabai (Okt. 2026), auf Sherka zugeschnitten. Stil, Texte und Verbote: immer zuerst `reel-marketing` §9.

## 0. Brauchen wir das überhaupt? (zuerst prüfen, ehrlich sagen)
- **Stand 24.10.2026: meistens nein.** Raffa filmt sich nicht und zeigt kein Gesicht. Die Stimme kommt von ElevenLabs, deren Wort-Zeitstempel ersetzen Whisper. Tafeln und Animationen baut `video-engine-picker` / `code-video`.
- **Nutzen, wenn:** Raffa eine eigene Aufnahme schickt (Gesichts-Post „Wie ich angefangen habe“ ab Woche 2, Sprachmemo, Bildschirmaufnahme mit Stimme), oder ein fremder Clip mit Sprache untertitelt werden muss.
- Nicht nutzen für: stumme Tafel-Reels, Ei-Reel-Typ, reine Website-Clips. Dort ist nichts zu schneiden.
- Was Claude nicht kann: filmen, hören (nur messen) und beim ersten Mal Raffas Geschmack treffen. Jeder Schnitt wird von Raffa geprüft.

## 1. Werkzeuge
- `ffmpeg` (ist da). `pip install faster-whisper` nur bei Bedarf (Modell `small`, auf CPU `int8`, Sprache `de`).
- HyperFrames ist nicht nötig: Titel und Tafeln laufen über HTML/Playwright oder three.js (`code-video`).

## 2. Ablauf (jeden Schritt kurz zeigen, nicht alles auf einmal)
1. **Ansehen:** Contact Sheet (`fps=1,scale=180:-1,tile=6x4`) und `ffprobe` (Länge, Auflösung, fps, Ton).
2. **Transkript mit Wortzeiten:** faster-whisper `word_timestamps=True` → JSON. Versprecher und Neustarts im Text markieren und Raffa zeigen, welche Stellen rausfallen.
3. **Pausen schneiden:** jede Pause > 0,3 s raus, 0,1 s Luft vor und nach jedem Satz lassen, **nie mitten im Wort schneiden** (Schnitt nur an Wortgrenzen aus dem Transkript). Erkennen per `silencedetect=noise=-35dB:d=0.3`, gegen die Wortzeiten prüfen, dann `select/aselect` oder Segmente + `concat`.
4. **Stimme säubern** (Ziel: ruhig, nah, wie Podcast): `highpass=f=80, afftdn=nf=-25, equalizer=f=400:t=q:w=1.2:g=-3, acompressor=threshold=-18dB:ratio=3:attack=10:release=200, loudnorm=I=-14:TP=-1.5:LRA=11`. Vorher/Nachher als Waveform zeigen, Claude hört nicht.
5. **Untertitel:** 2–3 Wörter pro Einblendung aus den Wortzeiten, als ASS einbrennen. Sherka-Look: Bone #F0F1F3 auf Ink #14131C oder mit Schatten, Schlüsselwort orange #FFA51E, im unteren Drittel, aber über der Insta-Zone (unten ~400 px frei, oben ~250 px). Schweizer Rechtschreibung (kein ß), Mundart nur, wenn gesprochen.
6. **Grafik/Tafeln:** über `code-video` (1080x1920, echtes Logo), dann dazuschneiden.
7. **Pflicht-Check** (unten), dann liefern.

## 3. Tempo und Regeln
- Hook in den ersten 3 s, Totzeit und Wiederholungen raus. Lieber schneller als die Rohfassung, aber nicht hektisch: Raffa fand 16 Clips in 15 s zu schnell, ≈1 s pro Bild wie die Vorlage passte.
- Sound: Trend-Sound legt Raffa in der App drunter. Bei Stimme Musik nur leise darunter (Stimme −14 LUFS, Musik etwa −30).
- Gesicht echt lassen, keine KI-Verschönerung. Keine erfundenen Zitate, nur, was gesagt wurde.

## 4. Pflicht-Check vor dem Senden
1. Contact Sheet ansehen (abgeschnittener Text, Überlappungen, Safe Zones).
2. Handy-Encode: `-c:v libx264 -crf 24 -maxrate 8M -bufsize 16M -preset slow -pix_fmt yuv420p -movflags +faststart`, Ton AAC stereo.
3. `ffprobe`: Länge, 1080x1920, fps konstant, Ton vorhanden. Lautheit `ebur128` ≈ −14 LUFS.
4. `blackdetect=d=0.1:pix_th=0.05` und `freezedetect=n=-60dB:d=0.5`: gewollte Tafeln benennen, alles andere ist ein Fehler.
5. Kurze Liste „was falsch ist“ (oder „nichts gefunden“) mit dem Video schicken.

## 5. Stil-Datei wachsen lassen
Jede Korrektur von Raffa zum Schnitt sofort hier in §3 oder in `reel-marketing` §9 eintragen. Das ist der eigentliche Wert des Kits.
