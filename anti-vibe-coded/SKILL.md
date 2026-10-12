---
name: anti-vibe-coded
description: Hard ban list against the generic "AI-generated / vibe-coded" website look. Apply ALWAYS when building, styling, redesigning or reviewing any website, landing page, web app UI or component — even if another design skill is also active. Covers purple/blue gradients, Inter, pill buttons, glow, bento grids, glassmorphism, gradient text, floating 3D blobs, stock images, generic palettes.
---

# Anti-Vibe-Coded

A site looks AI-made when it stacks the defaults every model reaches for. One default alone is fine; three together is the tell. Every item below is **banned by default** and only allowed when there is a concrete, stated reason from the brand or the content — never "because it looks modern".

## The 15 tells → what to do instead

| # | Tell | Instead |
|---|------|---------|
| 1 | Purple → blue gradients (indigo/violet `#6366F1`, `#8B5CF6`, Tailwind `from-purple-500 to-blue-500`) | Flat color from the brand. If a gradient, then subtle and within one hue. |
| 2 | Uniform big rounded corners on everything (`rounded-2xl` everywhere) | Pick one radius system with intent: sharp (0–4px) or deliberate mix. Not the same blob radius on cards, inputs, images, buttons. |
| 3 | Inter (also Geist/system-ui as the only font) | A typeface with character that fits the brand (e.g. serif display + clean sans, grotesk, mono accent). Max 2 families. |
| 4 | Pill-shaped buttons (`rounded-full`) | Rectangular or lightly rounded buttons matching the radius system. |
| 5 | Glow effects, neon box-shadows, blurred color orbs behind content | None. Hierarchy through size, weight, contrast, space. |
| 6 | Bento grid feature sections | Layout derived from the content: lists, editorial columns, tables, asymmetric splits, real screenshots. |
| 7 | Frosted glass / `backdrop-blur` cards | Solid surfaces with clear borders or color blocks. |
| 8 | Oversized bold headline + small grey subline as the whole hero | Specific copy, real product/visual in the hero, measured scale. Headline says something concrete, not "Build the future of X". |
| 9 | Floating 3D shapes / abstract blobs | Real product, real photos, purposeful illustration, or nothing. |
| 10 | Thin outline icon set (Lucide/Heroicons) in tinted circles on every feature | Fewer icons. If needed: filled/custom/consistent with brand, never icon-in-circle-grid. |
| 11 | Gradient text (`bg-clip-text text-transparent`) | Solid text. Emphasis via weight, italic, color of the brand, or underline. |
| 12 | Generic stock images (smiling team at laptop) | Real photos of the actual business/product, or no image. Placeholder must be labeled as such. |
| 13 | Same section background repeated (white / grey-50 / white …) or every section same card pattern | Vary rhythm: full-bleed color blocks, dividers, density changes, different layouts per section. |
| 14 | Soft shadows on every card (`shadow-lg` everywhere) | Shadows only where elevation means something (menus, modals). Otherwise borders or contrast. |
| 15 | Generic palette: navy + indigo + lavender + off-white | Palette derived from the brand/industry, with one unexpected accent. Define tokens before writing components. |

## Also banned (same family)
- Emoji as feature icons, "✨" anywhere.
- Copy like "Unlock", "Elevate", "Seamless", "Supercharge", "Revolutionize", "Next-gen".
- Three-column feature row → testimonial carousel → pricing with "Most popular" pill → CTA band: the template page structure.
- Fake logos bar ("Trusted by…") and invented stats/testimonials.
- Hover = `scale-105` + bigger shadow on every card.

## Process
1. Before coding: write down palette, fonts, radius, shadow rule — derived from the brand, not defaults.
2. Build.
3. Self-check: walk the 15-item table against the result. Any hit without a written reason → remove it.
4. Final test: "Could this hero be swapped onto any other SaaS without anyone noticing?" If yes, it's not done.
