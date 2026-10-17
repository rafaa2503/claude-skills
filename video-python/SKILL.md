---
name: video-python
description: Build a short vertical brand video with the Python engine (PIL + numpy frames piped to ffmpeg). Use for continuous camera flights, a line of light through stations, glow, motion blur, sprite devices and pixel-level control. Slowest to edit, most control. Reference result - Sherka "Der Weg" (v1).
---

# Video – Python engine (PIL + numpy + ffmpeg)

Base skill with rules, gates and delivery: `code-video`. Template: `code-video/templates/path_video.py` (visuals) and `make_audio_path.py` (sound).

## Use when
- One continuous camera move through a world (stations on a path), glowing line, 3D-looking chunky shapes, parallax dust, grain.
- You want exact control of every pixel and no browser dependency.
## Do not use when
- You need physics, CSS/SVG text effects, shader filters or fast copy edits -> `video-html-playwright`, `video-effects-libs`, `video-hyperframes`.

## Setup
`python3` with PIL + numpy (present), `ffmpeg`, Inter fonts at `/usr/share/fonts/opentype/inter/`. Copy the template into a new folder with `assets/` (screenshots, logo).

## Workflow
1. Edit the constants at the top: colours, `A` (arrival times on the bar grid, 100 BPM = 0.6 s beat), `YS`, `STAT` titles, text strings.
2. Real screenshots into `assets/` (Playwright, see `code-video` §7); sprites are built in `phone_sprite`, `laptop_sprite`, `chat_sprite`, `approval_sprite`.
3. Test frames: `python3 path_video.py test 0.2 3.0 8.0 ...` -> `/tmp/pt_<t>.png`; build a contact sheet and look at it.
4. Audio: `python3 make_audio_path.py` then `loudnorm=I=-14:TP=-1.5:LRA=9`.
5. Render: `python3 path_video.py` (~4 min for 650 frames, 4 cores) -> master; phone encode `-crf 24 -maxrate 8M`.

## Pitfalls (hit before)
- Sub-frame time negative at t=0 -> complex numbers -> "incorrect coordinate type". Clamp `t=max(0,t)`; seeds `abs(...)`.
- `Image.alpha_composite` rejects negative offsets -> use `blit()`.
- Draw at 2x, downscale premultiplied (`convert("RGBa")`) or edges go dark.
- Big glows turn the accent flat yellow; scale glow with radius.
- Lines crossing titles: dark vertical band behind titles.

## Cost
Edit cycle slow (code + 4 min render). Render ~4 min. Good for one hero film, bad for ten client variants.
