---
name: video-remotion
description: Build a short or long vertical brand video as a Remotion (React) composition with spring animations and Sequences. Use for typed, reusable components, longer videos or team workflows. Reference result - Sherka v4.
---

# Video – Remotion (React)

Base: `code-video`. Template: `code-video/templates/remotion_reel/` (`src/Reel.tsx`, `Root.tsx`, `public/`, `package.json`).

## Use when
- Reusable components, props-driven variants (same layout, different client), videos longer than ~30 s, audio-synced sequences.
## Do not use when
- One-off pixel-art look -> `video-python`; shader effects -> `video-effects-libs`. Remember the licence: free for individuals and very small teams; companies need a licence (remotion.pro).

## Setup
`npm install` in the project (remotion, @remotion/cli, react 18). In this sandbox you can instead symlink `node_modules` from `OpenMontage/remotion-composer` if already installed.

## Render (sandbox-specific)
```
npx remotion render src/index.ts SherkaReel out/sherka-remotion.mp4 --width=1080 --height=1920 \
  --browser-executable=/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell \
  --chrome-mode=headless-shell --crf=22
npx remotion still src/index.ts SherkaReel out/f.png --frame=165   # single frame check
```
~2.5 min for 720 frames. The default browser download/launch fails here; always pass the headless shell.

## Pattern
`<Sequence from={sec*30} durationInFrames=...>` per scene; inside, `useCurrentFrame()/30` = scene-local seconds; `spring({frame,fps,config})` for pop/bounce; `interpolate` for linear moves; `<Audio src={staticFile(...)}/>` at the root. Put the plan constants (`A`, texts) at the top of `Reel.tsx`.

## Pitfalls
- Hand-placed "fallen" cards overlap: set landing positions with >=10 px gaps and rotation <=8 degrees; check a still at +1.0 s after the last card lands.
- Fonts: Inter is a system font here; for other machines load via `@remotion/google-fonts`.
- Check frames with `remotion still` before the full render.
