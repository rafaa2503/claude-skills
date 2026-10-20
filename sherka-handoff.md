# Sherka – Übergabe an einen neuen Chat (Stand 20.10.2026)

**Zweck:** Diese Datei fasst alles zusammen, was in diesem Chat besprochen und gebaut wurde. Ein neuer Chat soll damit sofort weiterarbeiten können, ohne Fragen zu wiederholen.
Ergänzende Fakten über Sherka stehen in `sherka-context.md` (gleiches Repo). Marketing-Regeln stehen in `reel-marketing/SKILL.md`.

## 0. Kurzanweisung für den neuen Chat (zuerst lesen)
- Nutzer: **Rafaa**, Gründer von **Sherka** (Webdesign-Agentur, Biel, Ziel: ganze Schweiz). Zeigt sein Gesicht noch nicht. Sprache: **Deutsch**.
- Rolle: **"Ruthless Mentor"**. Keine Schönfärberei, schwache Ideen klar als schwach benennen und begründen. **Kurze Antworten**, nur nötige Infos.
- Agentur immer als **"wir"**. Kein KI-Ton, keine Floskeln, Schweizer Rechtschreibung (kein ß).
- Rafaa mag keinen nervigen Sound. Er mag keine Texte, die alles erklären und nichts offen lassen.
- Ablauf bei Reels: **erst Skript** (Skill `reel-marketing`), Freigabe holen, dann Engine wählen (`video-engine-picker`), dann bauen.
- Repo: `/home/user/claude-skills`, Branch `claude/sherka-context` (alles gepusht, Stand `v16`).

## 1. Sherka in Kürze (Details: `sherka-context.md`)
- Kleine Webdesign-Agentur Biel/Bienne. Versprechen: "Mehr Kunden. Weniger Aufwand." Website bauen und betreuen, Domain gehört dem Kunden, Entwurf mit Kommentarmöglichkeit, online erst nach Freigabe, **Erstgespräch kostenlos**, Antwort innert eines Werktags. Keine Preise auf der Website.
- Referenzen: bledi-bienne.ch (Restaurant Biel, **Bledi hat der Darstellung zugestimmt**), bern-zahnarzt-team.ch (**Zustimmung nicht bestätigt**), takabul.ch, kamil-energy.ch.
- Instagram @sherka.ch (über Metricool verbunden): 22 Follower (17.10.2026), 1 Post vom 16.10. (Reichweite 829, 52 Interaktionen).
- **Nische offen.** Rafaa will starten und die Nische durch Tests finden (Vorschlag aus dem Chat: 30 Tage, 10 Branchen, je 10 Betriebe, messen).
- Formular auf der Website nennt auch "Tool statt Excel-Listen". Ob Sherka Buchungs- oder Rückruf-Tools anbietet, ist **ungeklärt**.

## 2. Wichtige Entscheidungen und Rafaas Haltung
- **Reels dürfen locker sein.** Rafaa sagt wörtlich: Auf Instagram muss nicht alles belegbar sein, Videos seien nicht verbindlich, Ziel sei Reichweite. Meine Gegenposition (bleibt bestehen, aber Rafaa hat das Risiko akzeptiert): Geschäftskonto-Reels sind Werbung (UWG gilt). Keine erfundenen Zahlen als Tatsache, keine Garantien, keine echten Firmen als Negativbeispiel.
- **"Gratis Erstgespräch" ist verbrannt:** Rafaa hat das in 4 Posts benutzt. Nicht wieder als Haken oder Schluss verwenden. Auch das Muster "Problem, Entwurf, gratis" nicht wiederholen.
- **Nicht "deine Website ist schlecht"** als Kernaussage. Gefühle statt Website-Kritik (Erschöpfung, Scham, Stolz, Angst).
- **Spannung statt Erklärung:** Eine Szene statt einer Lehre, Pointe spät, Frage offen lassen, Moral nicht aussprechen.
- **Grafik statt nur Text:** Rafaa wollte Bilder/Cartoon. Hinweise wie "nachgestellt" will er **nicht** im Bild. Text im Bild soll nicht wiederholen, was gesprochen wird.
- Für Frauen/Salons/Gastro wollte Rafaa: flüssige Animation, "Wow", Verständnis statt Urteil, Cartoon.
- Reichweite ist das Ziel der Reels (Views, Sends), Leads kommen über Kommentare/DM.

## 3. Marketing-Recherche (Zusammenfassung, Details in `reel-marketing/references/sources.md`)
Quellen sind fast nur Blogs/Einzelberichte, keine offizielle Plattform-Doku. Zahlen daraus sind Hypothesen.
- Signale: Schauzeit/Durchschauquote und Wiederholungen zuerst, dann **Sends (DM-Weiterleiten) pro Reichweite**, Saves; TikTok: ausführliche Kommentare, Untertext fliesst in Suche.
- Aufbau: Hook (0–3 s) → zweiter Haken (~5 s) → Auflösung → Grund zum Teilen. **Ende zuerst schreiben.** Hook muss nur einen Grund geben, jetzt weiterzuschauen.
- Praktiker (Reddit-Spiegel, Medium): Handy-Look schlägt Politur, Text mit dem Problem vor dem Gesicht, mehrere Hook-Varianten testen, dieselbe Struktur wiederholen, Trial Reels nur für Nicht-Follower (Einzelquelle, vorher prüfen).
- Für Betriebe belegt (schwach): Vorher-nachher, Kurztipps, hinter den Kulissen, Kundenreaktionen.
- Benchmarks (Metricool, 6,2 Mio. Videos): Reels Ø ~23'000 Views, aber verzerrt; Konten mit 2'000–10'000 Followern ~3'200. ~65 % der Reel-Views in den ersten 3 Tagen, also erst nach 3 Tagen urteilen.
- Lücken: nichts Spezifisches zu Schweiz/DACH, Handwerkern, Webdesign-Agenturen. Reddit direkt ist für die Suche gesperrt.
- Testplan: 3 Hook-Varianten pro Idee, Metriken: Sends/Reichweite, Halten nach 3 s, Durchschauquote, Saves, Profilbesuche, Kommentare/DMs; Entscheid nach 3 Tagen.

## 4. Skills im Repo
- `reel-marketing/` (neu): Ziel, Hook-Muster, Skript-Regeln, Grenzen, Testplan, Ausgabeformat. **Immer vor dem Bauen.**
- `video-engine-picker/` (Router): Empfehlung / Warum / Zweite Wahl / Aufwand / Risiko.
- Engine-Skills: `video-python`, `video-html-playwright`, `video-effects-libs`, `video-remotion`, `video-hyperframes`, `video-openmontage`.
- Basis: `code-video/SKILL.md` (Phasen, Pitfalls; §9 sound-first, §10 Handy-Test, §11 viraler ADHS-Schnitt). Quellen: `code-video/references/sources.md`.

## 5. Videos (alle in `sherka-variants/`, Vorlagen in `code-video/templates/`)
Frühere Runde (V1–V9): Engine-Vergleich desselben Reels (Python, HTML+Matter/Rough, Pixi/p5.brush, Remotion, HyperFrames, OpenMontage), V7 Sound-Konzept, V8/V8b Handy-Test mit Bledi, V9 viraler "3-Sekunden-Check".

| Datei | Idee | Status / Feedback |
|---|---|---|
| v10-versteckte-kosten | Text-Reel "Deine Website kostet Geld", Zeitmesser 2,5 s | Fertig, 14,4 s. Rafaa: Gratis-Erstgespräch-Schluss verbrannt |
| v11-unsichtbar | "Du bist der Beste… und gehst unter", Phonk-Bass, SICHTBAR | Rafaa: **KI-Stil, erklärt alles**, Spannung fehlt |
| v12b/v12c | Handwerker-Geschichte (Hook B/C), reiner Text, ruhige Stimme | Rafaa: **fehlt Bild/Grafik** |
| v13b / v13c | Gleiche Geschichte mit Handy-Grafiken (Google-Suche, leere Treffer, Maps-Karte, Chat "Muss wohl am Wetter liegen.") | **B: "passt".** C Alternative. Hook A (null Anrufe) nicht erzeugt |
| v14 | Salon "22:47", Cartoon, ohne Stimme | Ersatzfassung |
| v15 | Salon "22:47" mit Stimme (Leni) | Aktuelle Salon-Fassung. Caption siehe §7 |
| v16 | "Verpasster Anruf" (Maler auf Leiter, Rückruf-Knopf), 18,5 s, ohne Stimme | Neu. Siehe Review in §6 |

Vorlagen: `kosten_reel/`, `unsichtbar_reel/`, `handwerker_reel/` (build.py = Textversion, build2.py = Grafikversion), `salon_reel/` (build.py, build_silent.py), `anruf_reel/`.

## 6. Offene Review-Punkte zu v16 (unabhängiger Agent, Gesamturteil: nicht freigabefähig in dieser Form)
- Moral wird ausgesprochen ("nicht besser… nur erreichbar"): bricht Regel "nicht erklären". Variante B: Schwarz-Teil streichen, mit "Danke, hat sich erledigt." enden.
- **Kein Grund zum Teilen.** Vorschlag: "Schick das dem Maler, der nie rangeht."
- **Sherka nicht erkennbar.** Vorschlag ohne Endkarte: "sherka.ch" klein in Browserleiste der Mock-Seite, Caption-Satz "Wir bauen Websites für Handwerker".
- Logik: "ohne zu telefonieren" vs. "erreichbar" leicht widersprüchlich. "Maler Brunner" evtl. echter Name, einen sicher erfundenen wählen.
- Rafaas Vorgabe ("kein Blau, keine Endkarte, kein BEISPIEL-Hinweis") wurde befolgt; die Skript-Datei des Fremdagenten (`social-media-agent/drafts/...`) existiert im Repo nicht, Kopie in `code-video/templates/anruf_reel/skript.md`.

## 7. Texte, die entstanden sind (Kern)
- **Handwerker-Geschichte (Skript, freigegeben):** Hook B "Du bist der Beste in deinem Job. Genau das ist dein Problem." → "Letzte Woche sagte mir einer genau das. Ich google ihn. Nichts. Kein Eintrag. Keine Fotos." → "Dann den Zweiten. Mittelmässig. Aber: Fotos, Bewertungen, Nummer ganz oben." → "Aber das war nicht das Schlimme. Das Schlimme war, was der Beste mir danach schrieb: «Muss wohl am Wetter liegen.»" → "Schick das dem Besten, den du kennst."
- **Salon "22:47":** "Es ist 22:47. Dein Laden ist zu. Dein Handy nicht." → drei Kundenfragen → "Du liebst deinen Laden. Nur nicht das hier." → "Das ist nicht dein Fehler." → "Schreib mir: Wie viele sind es heute?"
- **Salon-Caption (final, mit Lösung):** "Dein Laden ist zu. Dein Handy nicht. … Das meiste davon kann deine Website beantworten, bevor jemand fragt. Preise, Öffnungszeiten und ein Formular, das dir alles gesammelt schickt. … Wie viele Nachrichten sind es bei dir heute? Zahl in die Kommentare. Du willst das für deinen Laden? Schreib uns kurz, wir schauen, wie das bei dir aussehen könnte." Hashtags #coiffeur #beautysalon #salonbesitzerin #selbstständig #schweiz. Wirkung der Hashtags unbelegt. Prüfen: Beantwortet eine Website wirklich "Habt ihr morgen was frei?" Nur mit Terminkalender.
- **Weitere Ideen für andere Gruppen (noch nicht gebaut):** Restaurant ("Der Gast, der nie anrief", Öffnungszeiten vor verschlossener Tür), Handwerker-Galerie ("Dein bestes Werk liegt zwischen Katzenfotos"), Zahnarzt/Physio (Angst vor dem ersten Mal, Einverständnis nötig), Event (abgelaufene Links), Coach (Scham, nach dem Preis zu fragen; schwächste Idee).
- Früher im Chat entstanden (Details nicht in dieser Datei): Kunden-Mails (Catia gekürzt, Fatima noch zu kürzen), Signatur (DE/EN/FR), Instagram-Bio-/Video-Texte, `sherka-context.md`. Gmail-Entwürfe wurden angeboten, nicht erstellt.

## 8. Technik-Hinweise
- **Render:** HyperFrames (`npx hyperframes@0.8.169`, `DO_NOT_TRACK=1`, `HYPERFRAMES_SKIP_SKILLS=1`), HTML + GSAP, 1080x1920, `window.__timelines["main"]`. Befehl: im Ordner `hf*/` `npx --yes hyperframes@0.8.169 render -o <ziel.mp4>`.
- **Stolpersteine:** `gsap.fromTo` setzt Startwerte sofort (`immediateRender:false` für Blitz/Overlays); Fonts nur auflösbar wie `Inter` (kein "Arial Rounded"); nur `x/y/scale` animieren, nicht `left/top`; negative Zeit klemmen; Untertitel-Blöcke mit eigenem `<div>` und berechneter Schriftgrösse.
- **Ton:** synthetisch mit numpy (Pings, Plucks, Pads, Kick), Stimme mit Ducking, `loudnorm -14`, stereo. Rafaa hört Nerviges sofort: sparsam bleiben.
- **ElevenLabs-Connector** (nur Stimme): Free-Tier-Konto wird **zeitweise gesperrt** ("Unusual activity… Free Tier access disabled"). Fehlgeschlagene Generierungen **nicht wiederholen**. Verlässlich nur mit Bezahlplan (ab ca. 5 $/Monat). Wortzeiten: Audio per `creative_attach_reference_file` (URL) in denselben Flow, dann `creative_transcribe_audio` (Scribe), Zeiten aus `words`. Stimmen: Turbo Tim `2z1FNC3hpK58mQpkXz3h` (aggressiv), Jantosch Coffee Talk `29P4oL0t0q3euslXSCVo` (trocken), Leni `WzPl01KDMCPMOyx39EfF` (warm, weiblich), Jan Social Media Creator `keqaIOtp0ePlmN5jgQfy`. Piper/lokale Stimmen lehnt Rafaa ab.
- Sandbox: ffmpeg, PIL, numpy, Playwright/Chromium vorhanden; kein cairo/OpenCV/scipy/Whisper; Instagram-Scraping scheitert (429); WebSearch blockiert Reddit.
- Metricool-Konto ist über Connector erreichbar (Brand-ID 7459675); Posten/Planen wurde bisher nicht gemacht.

## 9. Offene Punkte / Entscheidungen von Rafaa
1. **Wer beantwortet DMs/Kommentare** (Versprechen "innert eines Werktags")?
2. **Zahnarzt-Einverständnis** (nur Bledi ist bestätigt).
3. **Zielbranche** und ob Salon/Gastro/Handwerk zuerst.
4. **Bietet Sherka einen Rückruf-Knopf / Buchungs-Tool an?** Sonst Reels nur als Reichweite nutzen.
5. **ElevenLabs-Bezahlplan** buchen; **alte API-Schlüssel löschen** (zwei wurden im Chat gepostet: der frühere `sk_…` und ein 64-stelliger Hex-Code). Nie Schlüssel in den Chat.
6. **Bio-Link** auf Instagram prüfen (Reels sagen teils "Link in der Bio").
7. Variante B von v16 bauen (Send-Satz + sherka.ch in der Browserleiste)?
8. Restaurant-Reel (mit Bledi-Bezug nur in der Caption) und Handwerker-Galerie-Reel sind die nächsten sinnvollen Tests.
9. Test-Setup: 3 Hook-Varianten pro Idee, nach 3 Tagen auswerten, max. 3 Reels pro Woche.

## 10. Wie weiterarbeiten
Neue Idee → `reel-marketing` anwenden (Ziel, Hook, Skript, Grund zum Teilen, Risiken, Testplan) → Freigabe → `video-engine-picker` → bauen (HyperFrames für Text/Cartoon-SVG, effects-libs für Flüssig/Shader) → Frames und Lautstärke prüfen → committen/pushen → Datei an Rafaa senden mit ehrlicher Kritik und offenen Punkten.
