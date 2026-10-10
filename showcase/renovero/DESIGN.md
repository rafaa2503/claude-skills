# Design System: renovero Redesign (Konzept)

Redesign-Studie von https://www.renovero.ch/de. Modus: **Redesign, Marke erhalten.**
Inhalte, Kundenzitate, Bilder, Logo und Link-Ziele stammen 1:1 von der Originalseite.

Design Read: Überarbeitung einer Handwerker-Plattform für Schweizer Hauseigentümer,
vertrauensorientiert und konkret, abgeleitet aus dem eigenen Logo (Navy-Block + gelber Balken).

Dials: `DESIGN_VARIANCE 5` · `MOTION_INTENSITY 4` · `VISUAL_DENSITY 4`

## 1. Atmosphäre
"Baustellen-Signal". Das Logo ist ein navyblauer Block mit gelbem Balken darunter.
Dieser Aufbau (Fläche + gelber Balken) ist das einzige wiederkehrende Motiv:
Hervorhebung in der Headline, Umschalter unter dem Vorher/Nachher-Bild,
Abschluss der Navy-Panels. Keine weitere Deko.

## 2. Farben
| Token | Hell | Dunkel | Rolle |
|---|---|---|---|
| `--navy` | `#203768` | `#203768` | Markenflächen (Panels) |
| `--text` | `#162850` | `#E9EDF5` | Text |
| `--signal` | `#F9B415` | `#F9B415` | Einziger Akzent: Primär-CTA, Balken |
| `--bg` | `#F4F6F9` | `#0D1530` | Seitenhintergrund (kühl, kein Creme) |
| `--surface` | `#FFFFFF` | `#141F42` | Erhöhte Flächen |
| `--sunk` | `#E9EDF3` | `#1A2650` | Vertiefte Flächen |
| `--line` | `#DBDFE7` | `#26345F` | Linien |
| `--muted` | `#55627F` | `#A4AFC8` | Sekundärtext (AA auf `--bg`) |

Text auf Gelb ist immer `#162850`, nie Weiss.

## 3. Typografie
Eine Familie: **Encode Sans** (Markenschrift, variabel, `wdth 75-125`, `wght 100-900`).
- Display: `font-stretch: 118%`, `750`, `line-height 1.02`, `letter-spacing -0.025em`
- H2: `font-stretch: 114%`, `700`
- Body: `font-stretch: 100%`, `400`, `line-height 1.6`, max. `65ch`
- Zahlen: `font-variant-numeric: tabular-nums`

## 4. Komponenten
- Radius-System: **4px überall** (Buttons, Inputs, Bilder, Panels). Keine Pills.
- Primär-Button: Gelb, Text Navy, `inset` Schatten unten (Balken-Echo), `:active` 1px nach unten.
- Ein Label pro Absicht: "Projekt ausschreiben" (Anfrage starten), "Anmelden" (Login).
- Fokus: 3px Outline `--focus` (Navy hell / Gelb dunkel) mit 2px Offset.
- Formular: Label über dem Feld, Fehler darunter, kein Placeholder als Label.

## 5. Hero
Split links Text + Suchformular, rechts Vorher/Nachher-Schalter (Fassade Katharina Plüss).
Max. 3 Textelemente (H1, Subtext, Formular). Keine Chips, kein Trust-Strip im Hero.

## 6. Layout-Familien (je nur einmal)
Hero-Split · Trust-Leiste · Sticky-Titel + Liste (Ablauf) · Bento 3 Zellen (Warum) ·
Icon-Raster + Index-Disclosure (Kategorien) · Tabs + Bild (Kunden) · Definitionsliste (FAQ) ·
Überlappung Foto/Panel (Verzeichnis) · Abschluss-Band.

## 7. Motion
Genau ein orchestrierter Moment: Hero wischt einmal automatisch von "Vorher" auf "Nachher",
sobald er sichtbar ist. Alles andere nur als Antwort auf Interaktion.
`prefers-reduced-motion`: kein Autoplay, keine Transition.

## 8. Verboten
Inter, Creme/Messing-Palette, Lila-Gradients, Em-Dashes, Eyebrow-Labels,
drei gleiche Karten, Akkordeon-FAQ, Karussell mit Punkten, erfundene Zahlen.
