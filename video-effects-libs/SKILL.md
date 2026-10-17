---
name: video-effects-libs
description: Build a short vertical brand video with shader and effect libraries in a deterministic HTML scene - PixiJS filters (glitch, bulge, crosshatch, ASCII, glow), Anime.js timelines, p5.brush hand-painted strokes, thinking-orbs dotted orbs, Matter.js. Use when the look must stand out. Reference result - Sherka v3.
---

# Video – effect libraries (PixiJS + Anime.js + p5.brush + thinking-orbs)

Base: `code-video`, engine contract from `video-html-playwright`. Template: `code-video/templates/html_effects/` (`effects.html`, `capture.js`, `shots.js`, `vendor/`, `assets/`, `bestof-audio.mp3`).

## Use when
- You want a distinctive, effect-led look: glitch hook, sketch-to-final reveal (CrossHatch -> clean), ASCII dissolve, glow, hand-painted underline/check, an "AI is working" orb.
## Do not use when
- Brand needs calm and corporate, or the effect would hide the message. Quick text-only edits -> `video-hyperframes`.

## Effect recipes
- **Hook glitch:** `new PIXI.filters.GlitchFilter({slices:14,offset,direction:0,fillMode:2})`, `offset = 70*exp(-(t-0.45)*2.2)`, `refresh()` each frame.
- **Impact bulge:** `BulgePinchFilter({center:[.5,.52],radius:800,strength})` on the root for 0.15-0.7 s.
- **Sketch -> final:** two sprites, one with `CrossHatchFilter` (capital H), crossfade over ~1.4 s.
- **ASCII dissolve:** `AsciiFilter(14)` sprite fades out as the clean one fades in.
- **Glow:** `GlowFilter({distance,outerStrength,color,quality:.3})` on a check or logo.
- **Orb:** bundle `thinking-orbs/engine` with esbuild (`orb_entry.js` -> `vendor/orb.js`), call `ORB.MODE_FRAMES[mode](size,t*speed,opts)` and `paintFrame(ctx,frame,true,{r:255,g:159,b:28})` onto a canvas texture; `resolvePreset('composing',64)` gives mode/opts.
- **p5.brush:** standalone `vendor/brush.js` (WebGL2, global `brush`). Coordinates are **centre-origin**. `brush.createCanvas(w,h)`; `brush.set('marker','#ff9f1c',1.7)`; draw; `brush.render()`; `canvas.toDataURL()` -> image -> `PIXI.Texture`. Render each stroke asset once before `window.READY=true`; reveal with a growing mask.
- **Anime.js:** one `anime.timeline({autoplay:false})` over plain objects, `tl.seek(t*1000)`, apply values to Pixi objects each frame.

## Rules
- Determinism: replace `Math.random` with a seeded generator and reseed per frame (`_s = floor(t*30)*7919+13`).
- WebGL textures from files need http: `capture.js`/`shots.js` serve the folder with a tiny node server; launch Chromium with `--use-gl=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`.
- Wait for `window.READY` (capture scripts do) before the first frame.
- Test frames first (`node shots.js effects.html 0.3 8.0 ...`), contact sheet, then `node capture.js effects.html out.mp4 30 24 bestof-audio.mp3` (about 7 min).

## Pitfalls
`F.CrosshatchFilter` does not exist (`CrossHatchFilter`). Container masks, not sprite masks, when the sprite has a filter (stencil leaks otherwise). `npm install --legacy-peer-deps pixi.js@7.4.2 pixi-filters@5.3.0` for rebuilding vendor files; all libs MIT (GSAP is not MIT, not vendored).
