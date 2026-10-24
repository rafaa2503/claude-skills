# Sherka – komplette Chat-Zusammenfassung und Skill-Übersicht (Stand 24.10.2026)

Ergänzt `sherka-handoff.md` (Übergabe) und `sherka-context.md` (Fakten). Diese Datei ist die chronologische Fassung plus die Liste aller Skills, Agenten und Verbindungen, die in dieser Sitzung verfügbar sind.

## Teil A – Chat-Zusammenfassung (chronologisch)

### Phase 1: Analyse (Start)
- Rafaa (Gründer Sherka, Webdesign-Agentur Biel) liess mich **sherka.ch** und **@sherka.ch** (Instagram über Metricool) analysieren.
- Ergebnis: klares Versprechen, einfacher 3-Schritte-Ablauf, aber Schwächen bei Vertrauen (kein Name/Foto/Adresse/Kundenstimmen), keine Preise, nur 4 Referenzen, Instagram nur 1 Post, 22 Follower.
- Ziel: **ganze Schweiz**, nicht nur Biel. **Nische noch offen**, wird durch Tests gefunden (Vorschlag: 30 Tage, 10 Branchen, je 10 Betriebe).
- `sherka-context.md` mit allen Fakten für andere KIs erstellt.
- Rafaa zeigt sich noch nicht (kein Gesicht). Agentur immer in **"wir"**.

### Phase 2: Erste Videos und Skill-Aufbau
- Erste Videos komplett im Code gebaut (Bledi-Seite als echter Screenshot, mit Einverständnis von Bledi; Zahnarzt-Seite nicht bestätigt). Logo und Zip-Upload eingebunden, Texte auf "wir" korrigiert.
- Vorbild "Duolingo – The Path" (PDF), danach drei Quellen zu Video-Libraries (OpenMontage, Notion-Motion-Tips, Social-Post). Rafaa wollte **alle** Engines und entscheidet selbst.
- Gebaut: **sechs Varianten** desselben Reels (Python/PIL, HTML+Playwright mit Matter/Rough, Pixi/p5.brush/Orbs, Remotion, HyperFrames, OpenMontage) = V1–V6.
- **Skills:** `code-video` (Basis), je ein Skill pro Engine, `video-engine-picker` als Router.

### Phase 3: Stimme und Ton
- ElevenLabs-Connector verbunden. Piper (lokal) und Edge-TTS lehnte Rafaa ab ("Stimme ist scheisse").
- Stimmen: "Jan" (besser), später Turbo Tim. **Free-Tier wird zeitweise gesperrt**, fehlgeschlagene Generierungen nicht wiederholen.
- Rafaa postete einen **API-Key im Chat** (nicht benutzt, Connector stattdessen). Später ein 64-stelliger Hex-Code. Beide sollen gelöscht werden.
- V7: Sound-Konzept ("Klang einer guten Website"), von Rafaa als Skript "scheisse" bewertet. V8/V8b: Handy-Test mit Bledi (proof-based), ruhigerer Ton nach "Der Sound nervt". V9: viraler 3-Sekunden-Check (HyperFrames).
- Rafaa-Feedback prägt die Regeln: kein nerviger Sound, kein KI-Ton, echte Screenshots, keine erfundenen Behauptungen in Texten.

### Phase 4: Kunden-Texte
- Zwei Anfragen (Catia, Fatima) für ein 20-Minuten-Gespräch: Mails geschrieben, "sehr nach KI" → gekürzt. Signatur DE/EN/FR. Instagram-Bio/Caption-Texte mehrfach überarbeitet ("mehr Marketing, nicht alles wiederholen"). Gmail-Entwürfe wurden angeboten, nicht erstellt. Fatima-Mail noch nicht gekürzt.

### Phase 5: Marketing-Denken (der grosse Umschwung)
- V10 "Versteckte Kosten", V11 "Unsichtbar" gebaut. Rafaa: Auf Instagram muss nicht alles belegbar sein, Ziel sind Aufrufe. Meine Haltung (bleibt): Zahlen, Garantien und echte Firmen als Gegenbeispiel vermeiden (UWG). Rafaa akzeptiert das Risiko.
- Rafaa kritisierte V11 als **KI-Stil (erklärt alles, keine Spannung)** → Neustart mit Skript-Prinzipien (Szene statt Lehre, Pointe spät, Frage offen).
- **Recherche** zu Reels/TikTok (Blogs, Reddit-Spiegel, Medium; offizielle Quellen fehlen) → Skill **`reel-marketing`** (neu). Kernpunkte: Durchschauquote, **Sends**, Hook in 1–3 s, Ende zuerst schreiben, 3 Hook-Varianten testen, erst nach 3 Tagen urteilen.
- **Handwerker-Geschichte** ("Muss wohl am Wetter liegen."): V12 nur Text (Rafaa: fehlt Grafik) → V13 mit Handy-Grafiken. **V13b freigegeben ("passt")**.
- **Salon/Frauen/Gastro:** Rafaa wollte Wow, flüssig, verständnisvoll. Ich schlug dieselbe Struktur vor → Rafaa: gleiche Idee wie vorher, Gratis-Erstgespräch schon in 4 Posts verbraucht. Neue Richtung **"22:47"** (Nachrichten-Erschöpfung) als **Cartoon** gebaut (V14 stumm, V15 mit Leni-Stimme), Caption mit Website-Lösung.
- **Weitere Kundengruppen** (andere Botschaft je Gruppe): Handwerker-Galerie, Restaurant, Zahnarzt/Physio, Event, Coach. Noch nicht gebaut.
- **V16 "Verpasster Anruf"** (Storyboard von einem anderen Agenten): gebaut. Unabhängiger Review-Agent: nicht freigabefähig (Moral ausgesprochen, kein Send-Grund, Sherka nicht erkennbar).
- **Übergabe:** `sherka-handoff.md` erstellt.

### Offene Punkte
DM-Zuständigkeit, Zahnarzt-Einverständnis, Zielbranche, ob Rückruf-/Buchungs-Tool angeboten wird, ElevenLabs-Bezahlplan, beide Schlüssel löschen, Bio-Link prüfen, V16 Variante B (Send-Satz, sherka.ch klein sichtbar), nächste Reels (Handwerker-Galerie, Restaurant).

## Teil B – Skills, die in dieser Sitzung verfügbar sind

### B1. Repo-Skills (Ordner `/home/user/claude-skills/`)
**Sherka-spezifisch**
- `reel-marketing` – Ziel, Hook, Skript, Grenzen, Testplan. **Immer vor dem Bauen.**
- `video-engine-picker` – wählt die Engine, begründet in fünf Zeilen.
- `code-video` – Basis: Regeln, Phasen, Fallstricke für Videos im Code.
- `video-python`, `video-html-playwright`, `video-effects-libs`, `video-remotion`, `video-hyperframes`, `video-openmontage` – je eine Engine.

**Web-Design und Qualität**
- `anti-vibe-coded` (Verbotsliste gegen "KI-Look"), `design-taste-frontend` (+ `-v1`), `high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui`, `master-designer`, `redesign-existing-projects`, `stitch-design-taste`, `gpt-taste`, `pre-launch-website-audit`, `pick-ui-library`, `prototype`, `image-to-code`, `imagegen-frontend-web`, `imagegen-frontend-mobile`, `brandkit`.

**Animation**
- `animate`, `animate-expo`, `animation-vocabulary`, `apple-design`, `emil-design-eng`, `find-animation-opportunities`, `improve-animations`, `review-animations`.

**Sonstiges**
- `supabase`, `ask-sonner` (Toasts), `write-swift`, `find-skills`, `full-output-enforcement`.

### B2. Eingebaute Sitzungs-Skills
- **Code/Betrieb:** `code-review`, `simplify`, `security-review`, `init`, `run`, `loop`, `update-config`, `fewer-permission-prompts`, `keybindings-help`, `session-start-hook`, `plugin-authoring`, `claude-api`, `workflow-authoring` (Workflow-Tool aktuell nicht verfügbar).
- **Darstellung:** `dataviz`, `artifact-design`, `artifact-diagramming`, `artifact-capabilities`.

### B3. Anthropic-Skills (Dokumente, Browser, Alltag)
- `human-writer` (**für deutsche Texte ohne KI-Ton, sehr relevant für Rafaa**), `website` (Idee zu Website), `deep-research`, `docs`, `docx`, `pdf`, `pptx`, `xlsx`, `google-workspace`, `skill-creator`, `import-memory`, `morning`.
- Browser/Computer: `built-in-browser`, `chrome-browser`, `computer-use`.
- Rafaa privat: `ch-it-bewerbung-automation`, `ch-it-bewerbungs-tracker` (Jobsuche), nicht Teil von Sherka.

### B4. Neu: Apify-Skills
- `apify:apify-ultimate-scraper` – scrapt Instagram, TikTok, Google Maps, Google Search, Reddit, LinkedIn und mehr. **Neu hier nützlich:** Instagram-Scraping scheiterte vorher (HTTP 429), Reddit war gesperrt, Google-Maps-Betriebe als Lead-Liste wären möglich.
- `apify:apify-actor-development`, `-actorization`, `-generate-output-schema`, `-sdk-integration` – eigene Scraper bauen/einbinden.
- Vorsicht: kostet Apify-Guthaben, Scraping von Plattformen berührt Nutzungsbedingungen und (bei Personendaten) das Schweizer Datenschutzgesetz. Vor jedem Lauf Ziel und Kosten klären.

### B5. Agenten (für Delegieren)
- `general-purpose`, `Explore` (Suche), `Plan`, `claude-code-guide`, `statusline-setup`, `web-fetch`, `claude` (Auffangbecken), neu `apify:apify`. In dieser Sitzung genutzt: ein unabhängiger Review-Agent für V16.

### B6. Verbindungen (Connectors)
- **ElevenLabs** (nur Stimme/Transkription; instabil wegen Free Tier), **Metricool** (Instagram-Daten, Planen), **Gmail**, **Google Drive**, **GitHub** (Repo), **Spotify**, **Claude Docs**, **Apify** (neu).

## Teil D – Ergänzungen aus einem parallelen Chat (im Repo gemerged, 24.10.2026)
Ein anderer Chat hat `reel-marketing` §9 **"Sherka-Stil (Raffas Korrekturen)"** und einen **Schluss-Check** in `code-video` §6 / `video-engine-picker` ergänzt. Das gilt ab jetzt vor jedem Reel. Kern:
- Ablauf: erst recherchieren, **Ideen + Hooks zeigen, Raffa wählt**, dann bauen. Struktur eines Reels übernehmen, das Raffa selbst gut findet. Selbst erfundene Website-Gags wurden abgelehnt.
- Hook verspricht genau das, was das Video liefert. Aufruf erst am Schluss. **Keine Serie, kein Kommentar-Aufruf, Wort "Wirt" nie, nie "für kleine Betriebe" und kein #kmu/#kleinunternehmen/#kleinbetrieb.** Nie im Video: Preise, Bauzeiten, "von Hand gebaut", Biel als Argument, Zweisprachigkeit. Marketing-Sätze dürfen zugespitzt sein, **erfundene Zahlen und Kundenzitate bleiben verboten.** Insta: du-Form.
- Look: **echtes Sherka-Logo** (Ink #14131C, Bone #F0F1F3, Punkt orange #FFA51E; Quelle Repo `rafaa2503/sherka` `/logo/`), keine alten A/B/C-Logos. Texttafeln ink/bone im Wechsel, orange Satzzeichen, Schluss mit Lockup.
- Zahlen (Metricool Okt. 2026): übliche Reels Ø 3,3–5,9 s Schauzeit, nur 15–30 % über 3 s. Bestes bisher: isometrisches Büro-Reel (31 s, Ø 10 s, 95 % Nicht-Follower, aber 0 neue Follower). Gewinner-Formate der Konkurrenz: POV-Making-of mit Geräuschen, Wissensfrage-Hook, Vorher/Nachher pro Branche.
- Tipps: Trend-Formate und -Sounds nutzen (Raffa schickt den Sound, Claude schneidet). Posten: 3–4 Reels pro Woche, Di–Fr 10:00, sonst 18:00.
- Schluss-Check vor jeder Auslieferung: Kontaktbogen ansehen, `ffprobe` (1080x1920, konstante fps, Stereo), Lautheit `ebur128` -14 LUFS, `blackdetect`/`freezedetect`, Liste "was falsch ist" mitschicken.

### Konflikte zwischen diesen Regeln und meinen Reels in diesem Chat
- **Kommentar-Aufruf:** V15 (Salon, "Zahl in die Kommentare") und V16 ("Zahl in die Kommentare") brechen die Regel. V11 ("Schreib: Sichtbar") ebenso.
- **Hashtag #kleinbetrieb** (V16-Caption des Fremdagenten) und "kleine Betriebe" sind verboten.
- **Logo:** Ich habe `icon-crop.png` aus dem hochgeladenen Logo-Zip genutzt. Ob das das **echte aktuelle Logo** ist, ist ungeprüft. Gegen `/logo/` im Repo `rafaa2503/sherka` abgleichen.
- **Erfundene Zitate:** "Muss wohl am Wetter liegen." (V13) und "Ich schäme mich fast…" sind erfundene Kundenzitate. Rafaa hat V13b freigegeben, die Regel nennt aber Kundenzitate als verboten. Klären, was gilt.
- **Preise in der Salon-Caption** ("Preise, Öffnungszeiten…") meint Inhalte der Kunden-Website, nicht Sherka-Preise. Trotzdem prüfen.
- **Ablauf:** In diesem Chat habe ich ab V12 Skript und Hooks gezeigt und Freigabe geholt. Bei V16 kam das Storyboard von einem anderen Agenten, das habe ich ohne zusätzliche Hook-Auswahl gebaut.
- **Offene Entscheidung:** Welche Fassung gilt, wenn zwei Regeln kollidieren? Vorschlag: die neuesten Korrekturen von Raffa in §9 gelten, V15/V16 ohne Kommentar-Aufruf neu fassen (Schluss: Send-Satz oder nichts).

## Teil C – Wo liegt was
- Videos: `sherka-variants/` (V1–V16, `voice-tests/`).
- Vorlagen: `code-video/templates/` (u. a. `viral_reel`, `kosten_reel`, `unsichtbar_reel`, `handwerker_reel`, `salon_reel`, `anruf_reel`).
- Dokumente: `sherka-context.md`, `sherka-handoff.md`, diese Datei.
- Repo/Branch: `claude/sherka-context` (alles gepusht).
