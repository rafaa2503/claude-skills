---
name: video-engine-picker
description: Router for code-built videos. Takes the user's video idea and picks the best of six engines (Python, HTML+Playwright, effect libraries, Remotion, HyperFrames, OpenMontage), says why in three lines, names the runner-up, then hands off to that engine's skill. Use at the start of any request for a reel, short, ad, kinetic title or explainer when no footage exists.
---

# Video engine picker

Vor dem Bauen eines Marketing-Reels: erst Skript und Hook mit `reel-marketing` klären.

One job: choose the engine, justify briefly, hand off. Do not build anything here. Shared rules and delivery: `code-video`.

## Step 1 – extract the brief (ask at most 3 questions, only for what is missing)
1. **Goal and length** (hook reel 15-30 s, kinetic title <10 s, explainer 30-90 s, series of variants?)
2. **Look** (calm brand film, effect-led/edgy, UI walkthrough, physics/playful, data/charts?)
3. **Reuse** (one-off, or the same layout again for many clients/texts?)
Also note: voice-over available (ElevenLabs/recording)? real footage? deadline? who edits later?

## Step 2 – score
| Engine skill | Pick when | Avoid when | Speed to first result | Edit later |
|---|---|---|---|---|
| `video-hyperframes` | many variants, text/asset swaps, <=60 s, need speed, lint gates, motion graphics, captions | needs physics or shader looks | fastest (46 s render) | easiest |
| `video-effects-libs` | the look must stand out (glitch, sketch->final, ASCII, glow, hand-painted, AI orb) | calm corporate tone | slow (~7 min) | medium |
| `video-html-playwright` | DOM/CSS layout, Matter physics, Rough.js, quick text edits, one-off | needs shaders or >60 s | medium (~6 min) | easy |
| `video-python` | one hero film with continuous camera/path, glow, motion blur, exact pixels | many edits or variants | slow edit cycle (~4 min render) | hard |
| `video-remotion` | reusable typed components, props-driven series, >60 s, React team | quick throwaway; company without licence | medium (~2.5 min) | good for devs |
| `video-openmontage` | JSON-only quick explainer, needs its voice/stock/localisation pipelines | exact brand look | medium | JSON edits |

Decision shortcuts:
- Voice-over + captions + long -> `video-remotion` or `video-hyperframes` (word timestamps drive scenes).
- "Make it look different from what agencies post" -> `video-effects-libs`.
- Same video for 5+ clients -> `video-hyperframes` (swap text/assets) or `video-remotion` (props).
- Cinematic path/camera move -> `video-python`.
- Data charts/stat cards -> `video-hyperframes` or `video-openmontage`.
- User has real footage to cut -> not this family: use `video-schnitt` (Pausen, Stimme, Wort-Untertitel), keep faces real.
- Fremder Vorlagen-Clip + Texttafeln (Ei-Reel-Typ) -> keine Engine nötig: ffmpeg + HTML-Tafeln, siehe `code-video` §12.
- Unsure -> `video-hyperframes` (cheapest to be wrong with).

## Step 3 – answer in this format (short)
```
Empfehlung: <engine skill>
Warum: <3 Zeilen, aus dem Brief>
Zweite Wahl: <engine skill> – nur wenn <Bedingung>
Aufwand: <Renderzeit / Anzahl Runden>
Kein Gegenargument gefunden / Risiko: <1 Zeile>
```
Then load the chosen skill and start at its Workflow. If the user asks to compare, build the same storyboard in two engines (templates exist for all six, see `sherka-variants/`).

## Rules
- Recommend one engine, not a menu. Defend it against the runner-up in one sentence.
- Never claim a voice exists before a TTS tool/connector is present; plan VO as a later step.
- No invented claims (stats, testimonials). Real screenshots over mockups.
- Third-party repos (OpenMontage) only on explicit request; licences: Remotion (company licence), OpenMontage AGPL-3.0, GSAP (own licence), others MIT/Apache.
- Before building a Sherka reel: read `reel-marketing` §9 (Sherka-Stil).
- Always end with the check before delivering (`code-video` §6): contact sheet ansehen · `ffprobe` Länge, 1080x1920, fps konstant, Ton stereo · Lautheit `ebur128` -14 LUFS · `blackdetect`/`freezedetect` (gewollte Tafeln benennen) · kurze Liste „was falsch ist“ mitschicken.
- Templates and engine skills live in repo `rafaa2503/claude-skills`, branch `claude/sherka-context` (clone it when a template is needed).
