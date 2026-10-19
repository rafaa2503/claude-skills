# Reel-Lehren (Stand 20.10.2026)

## Was beim Fehlschlag "Verpasster Anruf" falsch war
- Frame 0 war ein Standbild mit ruhigem Text. Im Feed entscheidet die erste Sekunde: Bewegung + Stimme + offene Frage gleichzeitig.
- Keine Stimme. Stumme Grafik-Reels wirken wie Werbung.
- Cartoon-Figuren aus einfachen Formen wirken leblos. Lieber Typografie, Oberflächen (Karten, Chats, Websites) und echte Stimmen.
- Kein Bild darf nach dem Hook länger als ca. 0.8 s stillstehen.

## Was beim Neubau funktioniert hat (Prozess)
1. Workflow: Recherche → 10 Konzepte aus 5 Winkeln → 4 Jury-Personas mit "an welcher Sekunde wische ich?" → Swipe-Test → finales Skript.
2. Stimmen über ElevenLabs (eleven_v4, englische Tags wie [tired]). Rate-Limit: Generierungen nur einzeln (generations_count 1), nacheinander.
3. Jede Stimme mit Whisper **medium** gegenhören. Small irrt, medium hat echte TTS-Fehler gefunden ("Wirkte" → "rückte", "Hat" → "Hab"). Bei Fehlern Text umformulieren, nicht nochmal dasselbe generieren.
4. Timeline aus den echten Clip-Längen bauen (edl.py), Animation liest die Zeiten (timings.js). Nie Timing raten.
5. Gerendertes Video von mehreren Prüfern zerlegen lassen (Hook, Sync, Marke, Motion). Die zweite Runde hat einen echten Bug gefunden (ein Wort wurde nie eingeblendet).
6. "Sherka" spricht die KI als "Schirka" aus: Markennamen nicht sprechen lassen.

## Offene Fragen, die nur echte Zahlen beantworten
- Hält "Ein Stern" wirklich besser als die Grafik-Reels? (H8)
- Sind 21 s zu lang? Wenn die Sehdauer unter 7 s bleibt: auf 15 s kürzen (Flut und Nahaufnahmen straffen).
