# Quellen und was daraus übernommen wurde

Stand 17.10.2026. Alles aus Material, das der User geschickt hat. Nichts davon ist von mir erfunden.

## 1. "The Path" – Duolingo-Spec-Ad (PDF-Prompt, 2 Seiten)
Spec-Arbeit für ein Portfolio, nicht mit Duolingo verbunden. Marken, Logos, Figur und Sounds von Duolingo
werden nie verwendet; nur die Methode.
- **Aufbau des Prompts:** GOAL (Länge, fps, Formate, "eine durchgehende Kamerafahrt, null harte Schnitte",
  Hook in der ersten Sekunde) · IDEA (ein Lichtstrahl, der jede Aufgabe übernimmt) · LOOK (fast schwarze Bühne,
  ein gedimmtes Glow, chunky 3D-Formen mit dunklerer Lippe, Tiefenschärfe, Motion Blur, leichtes Korn) ·
  Beat-Sheet in Sekunden (S1 Hook 0-1.67 ... S10 End Card) · VOICE-OVER · MUSIC · SOUND · BRAND · PROCESS.
- **Prozess in Phasen, jede wird freigegeben:** Brief → Assets → Stimme → Engine → erste Vorschau → Fixes → 9:16 → Finals.
  Stimme zuerst, danach werden die Bildschläge auf die Wörter gelegt.
- **Was den Unterschied machte:** Hook, der gross landet · Marken-Sounds · ein einziger fliessender Sprechertext
  (kein Zerhacken) · passende Stimme (2-3 Kandidaten vergleichen) · Figur aus echten Teilen, Bild für Bild geprüft.
- **Musik/Mix-Zahlen:** 100 BPM, D-Dur; Stimme ca. -16 LUFS, Musik >= 12 dB unter jedem Wort, Master -14 LUFS / -1.25 dBTP;
  ca. 100 SFX-Cues, jede sichtbare Bewegung hat einen Ton.
- **Anker-Technik:** Zeitmarken im Beat-Sheet (0.50, 2.95, 4.60 ...) an Wörter der Stimme koppeln.
- **Nicht umsetzbar hier:** ElevenLabs-Stimme, Marken-Sounds, SF-Pro-Fonts, Duo-Vektorfigur, echte 3D-Kamera.

## 2. OpenMontage (calesthio/OpenMontage, openmontage.video) – geprüft, nicht installiert
- Agent-gesteuertes System, läuft *in* einem KI-Coding-Assistenten: research → proposal → script → scene_plan →
  assets → edit → compose. Renderer: Remotion, HyperFrames, FFmpeg. 12 Pipelines, 100+ Tools.
- Braucht: Python 3.10+, Node 18+ (evtl. 22 für HyperFrames), FFmpeg, einen KI-Assistenten (bezahlt/Cloud).
  API-Schlüssel sind optional (FAL, ElevenLabs, Suno, Pexels ...). Piper-TTS ist lokal und gratis.
- Lizenz AGPL-3.0, 69k Sterne, aktiv. Makefile ohne curl|bash. Quellcode nicht geprüft.
  README enthält einen Abschnitt, der "OpenClaw-Agenten" Befehle vorgibt: nicht blind ausführen.
- Studio-Desktop-App = Warteliste, kein Download.
- **Entscheidung:** nur installieren, wenn Stimme/Stockmaterial gebraucht wird; dann in getrenntem Ordner, `make demo` zuerst.
  Für kurze Reels reicht dieser Skill.

## 3. Notion "Claude Motion Tips" (withian.notion.site)
Open-Source-Effekte, die man Claude zum Studieren gibt (Projekt, Sterne, Nutzen):
- Matter.js (18k) – Schwerkraft, Kollisionen; Wortkarten fallen und stapeln sich.
- Rough.js (21k) – Skizzen-Umrisse, Schraffur.
- PixiJS-Filter (48k) – Glitch, Glow, ASCII, Bulge, Crosshatch auf Text/Bild.
- Anime.js (73k) – Choreografie für Text, Formen, SVG.
- p5.brush (972) – Stift-, Kohle-, Aquarell-Striche.
- thinking-orbs (44) – animierte Punktkugeln für "KI denkt".
- 400+ Claude-Videos als Vorlagen (Skillry-Galerie, GitHub-Sammlung).
Drei Workflow-Tipps: 1) lange Prompts mit XML-Tags gliedern (Stil, Referenzen, Timing, Ausgabe getrennt) ·
2) zuerst nur 1 Sekunde mit dem schwierigsten Effekt testen · 3) vor dem Render ein Kontaktblatt der Schlüsselbilder prüfen.
(Die "Copy prompt"-Texte sind Buttons und waren nicht lesbar.)

## 4. Social-Post "Claude can't generate video. It can still edit yours."
- Eine HTML-Szene, die zu jedem Zeitpunkt `t` ein Bild rendert + Playwright-Capture-Schleife über N Bilder + ffmpeg → H.264-MP4 mit Audio.
  Eine Änderung = eine Zeile, jeder Render identisch (nur ohne Zufall/Echtzeit-Animationen).
- Motion Graphics (Lower Thirds, Kinetic Titles) als HTML-Szenen; für längere Erklärvideos Remotion/HyperFrames.
- Voice-over: Skript schreiben, TTS per MCP-Connector, **Wort-Zeitstempel** anfordern, damit Bilder auf der Stimme landen.
- Rohschnitt: Rohmaterial zuerst transkribieren, nach Text schneiden, Render selbst prüfen lassen.
- Grenzen: Gesichter und Tiere als echtes Filmmaterial; physikalisch korrektes Licht explizit verlangen.
