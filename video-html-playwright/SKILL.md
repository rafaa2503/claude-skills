---
name: video-html-playwright
description: Build a short vertical brand video as one HTML scene that renders any frame from a time value, captured by Playwright and stitched by ffmpeg. Use for DOM/CSS looks, Matter.js physics, Rough.js hand-drawn lines and fast copy edits. Reference result - Sherka best-of (v2).
---

# Video – HTML + Playwright engine

Base rules/gates/delivery: `code-video`. Templates: `code-video/templates/html_scene/` (`bestof.html`, `scene.html`, `capture.js`, `shots.js`, `make_audio_bestof.py`, `vendor/`, `assets/`).

## Use when
- Layouts that are easier in HTML/CSS than in pixels, physics (falling cards), SVG/Rough.js strokes, quick text changes.
## Do not use when
- WebGL filters (glitch/ASCII/crosshatch) -> `video-effects-libs`. Long multi-scene explainers -> `video-remotion` or `video-hyperframes`.

## The contract
`window.renderAt(t)` sets the full state for second `t`. Pure function of `t`; Matter.js is stepped at a fixed 1/60 s from the previous time, so capture runs **forward only**. No `Math.random`, `Date.now`, CSS transitions/animations, `requestAnimationFrame` loops.

## Workflow
1. Copy `html_scene/` to a project; edit the plan block (`A`, `TITLES`, texts) in `bestof.html`.
2. Test frames: `node shots.js bestof.html 0.2 5.4 11.4` -> `/tmp/shot_<t>.png` (use the exact number string as written, `1.0` becomes `shot_1.png`). Contact sheet, look.
3. Audio: `python3 make_audio_bestof.py` (writes `bestof-audio.wav`), loudnorm, or use the shipped `bestof-audio.mp3`.
4. Render: `node capture.js bestof.html out.mp4 30 24 bestof-audio.mp3` (about 0.4 s/frame, 6 min for 24 s). Re-encode for phones.

## Libraries (vendored, MIT)
Matter.js 0.19, Anime.js 3.2.2 (use `anime.timeline({autoplay:false})` + `tl.seek(ms)`), Rough.js 4.6.6 (seeded generator, `pathLength="1"` + dashoffset for reveal).

## Pitfalls
- Chromium path `/opt/pw-browsers/chromium`; Playwright from `/opt/node-tools/node_modules/playwright` (not pip).
- Screenshots ~0.3 s each; keep DOM light.
- Title text over a moving line needs a dark band behind it.
