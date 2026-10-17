---
name: code-video
description: Build a short brand/social video (Reel, Short, spec ad) entirely in code — PIL + numpy frames piped to ffmpeg, with synthesized music and SFX. Use when the user asks for a video, reel, ad or motion piece and no footage exists. Covers brief with frame-exact beats, real screenshots as proof, one continuous "path" motion idea, audio synth, frame checks, delivery and the sandbox pitfalls.
---

# Code Video

Make a 15-30 s vertical (1080x1920) video with no footage and no AI video model.
Every frame is drawn by code. Reference build: `templates/path_video.py` (visuals)
and `templates/make_audio_path.py` (sound) — the Sherka "Der Weg" reel. Copy them,
change the brand constants, stations and text; do not start from zero.

## 0. Gate: facts before pixels
- Ask or fetch: URL, logo (SVG/PNG), brand colours, real offer, 2-4 real references.
- Take real screenshots of the user's own client sites (Playwright, see §6) — proof beats mockups.
- **No invented claims.** No fake stats, prices, testimonials, "Telefon klingelt", "kein Risiko".
  Only promises the brand already makes on its own site. Illustrative UI (a chat, a comment) is
  allowed only when it is clearly a scene, never a "customer quote".
- Spec work for a third-party brand (e.g. a Duolingo-style ad): never use their logos or
  trademarks; build the idea with the user's own brand.

## 1. Brief (write it down in 10 lines before coding)
Idea in one sentence · length · aspect · one **continuous motion device** that does every job
(example: one line of light that reveals the logo, strings the steps, underlines the tagline) ·
beat sheet with seconds · what each beat proves · CTA. Put hit moments on a **bar grid**
(100 BPM = 0.6 s beat, 2.4 s bar) so picture and music lock.

Rules that made the reference work:
1. **Hook lands in the first second** (big, loud, one object). No logo-slow-fade.
2. Zero hard cuts. The camera moves; stations come to it.
3. Text holds long enough to read (>= 1.2 s a line, <= 7 words a line).
4. One accent colour from the logo; near-black stage; one dim glow, never neon.
5. Chunky "3D button" shapes: face + darker lip offset below + small highlight.
6. Instagram safe zones: keep key text out of top ~250 px and bottom ~400 px.
7. Honest about capability: no voice-over unless the user supplies/records one (no TTS in the
   sandbox, robotic German costs trust). Music is synthesized and plain; say so.

## 2. Renderer pattern (what `templates/path_video.py` does)
- Draw at 2x (`S = 2`) on RGBA layers, downscale with premultiplied alpha
  (`convert("RGBa").resize(...).convert("RGBA")`), then composite in numpy.
- Layers: `world` (path, nodes, devices, scrolls with a camera `(cy, zoom)` from keyframes) and `top`
  (HUD, titles, hero). Separate `L` glow layers, blurred and added in the accent colour.
- Camera and head position are keyframe lists with smootherstep; stations arrive on the bar grid.
- Devices (phone/laptop) are sprites built once from real screenshots, scaled with the camera.
- Motion blur = average of 3 sub-frames, only for fast sections. Light grain + vignette in numpy.
- Parallelise with `multiprocessing.Pool(4)` + `imap` (ordered) and pipe raw RGB to ffmpeg.
- 30 fps is enough for Reels; ~650 frames render in ~4 min on 4 cores.

## 3. Audio (`templates/make_audio_path.py`)
numpy synth, stereo, 44.1 kHz: sub + marimba arpeggio from frame 0, kick/clap/shaker from the
drop, riser into the fork, a breath (music stops) before the hero hit, full chord + low hit on the
hero beat. SFX on **every visible move** (whoosh, pop on node light, click on button, chime on
success). Then `loudnorm=I=-14:TP=-1.5:LRA=9`. Verify with `volumedetect`; you cannot listen, so
say "measured, not heard".

## 4. Check before sending (mandatory)
1. Render 5-8 test frames (`python3 path_video.py test 0.2 3 6 ...`), build a contact sheet,
   look at it. Check: text overlaps, clipped sprites, glow blowing out colour, title vs line collisions.
2. Full render, then re-encode for phone: `-crf 24 -maxrate 8M -preset slow -movflags +faststart`
   (a crf 17 master with grain was 125 MB; delivered file ~4 MB).
3. `ffprobe`: duration, 1080x1920, audio stream present, stereo.
4. Send with `SendUserFile`. Use `display: "attach"` if the user says they can't play it
   inline; also send the audio alone as MP3 when "I hear nothing" comes up (mono + quiet was the cause).

## 5. Pitfalls hit in this sandbox
- Tools available: ffmpeg, PIL, numpy, Playwright (Node, `/opt/node-tools/node_modules/playwright`,
  `executablePath: '/opt/pw-browsers/chromium'`), Inter fonts in `/usr/share/fonts/opentype/inter/`.
  NOT available: cairo, OpenCV, scipy, any TTS, `pip install playwright`.
- Sub-frame time can go negative at t=0 → `(t/x)**1.5` becomes complex → "incorrect coordinate type".
  Clamp `t = max(0, t)`. Same for numpy seeds (`abs(...)`).
- `Image.alpha_composite` rejects negative offsets: clip the sprite first (`blit()` in the template).
- Sprite canvases must be tall/wide enough for every animated overlay (a chip was cut off once).
- Big glows saturate the accent to flat yellow: scale glow intensity down for large radii.
- A scrolling line crossing a title is unreadable: darken a vertical band behind titles.
- Instagram blocks scraping (HTTP 429). Read account numbers through the connected Metricool tools.
- Stop hook wants untracked files committed: commit to a `claude/...` branch, never `main`,
  no PR unless asked. Check for personal data (email) in committed context files.

## 6. Screenshots (Playwright, Node)
```js
const { chromium } = require('/opt/node-tools/node_modules/playwright');
const b = await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const ctx = await b.newContext({viewport:{width:430,height:932},deviceScaleFactor:2,isMobile:true}); // phone
// desktop: viewport 1440x900, deviceScaleFactor 1  → laptop sprite
```

## 7. Hand-off checklist
Video file · template scripts · screenshots/logo under `assets/` · a note listing what is
missing vs. a studio ad (voice, licensed sounds, true 3D) · open questions (niche, prices, name/face).
