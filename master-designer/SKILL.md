---
name: master-designer
description: Reference-first frontend design workflow. Never generate a UI from a bare prompt — gather real references, extract technique (never brand identity), assemble a project DESIGN.md, then build and audit against it. Combines design-taste-frontend, redesign-existing-projects, stitch-design-taste, pick-ui-library, prototype, and the animation skills into one pipeline, plus external reference/asset tools (Refero Styles, Haikei, Pinterest/Dribbble sourcing).
---

# Master Designer

The core claim this skill encodes: **better inputs beat better prompts, every
time.** An LLM asked to "design a premium SaaS landing page" with no
references has one option — the statistical average of every SaaS landing
page it has seen, which is exactly the AI-slop look every other skill in this
repo exists to prevent. Feed it 2-3 real, specific references and a real
brief, and it has something to *match*, not something to *invent*.

This skill is the pipeline that sits above the individual taste/audit/build
skills already in this repo. It does not replace them — it tells you which
one to reach for, in what order, and where external reference tools plug in.

---

## 0. The hard gate: no generation without references

Before writing a single line of CSS or calling `design-taste-frontend`,
answer: **what real thing does this need to look like, or sit next to?**

Acceptable references, in priority order:

1. **User-provided screenshots or links.** Always ask for these first if the
   brief doesn't include them ("send me 2-3 sites/screens whose look you
   want, even rough ones").
2. **A real design-system export** for the *category* of product (see
   Section 1) — not to copy verbatim, but to see how a real team solved the
   same type problem, spacing rhythm, or component density.
3. **Pinterest / Dribbble search** on the vibe words from the brief (e.g.
   "glassmorphism UI", "editorial fintech dashboard"). Screenshot 2-3 that
   are actually close, not just aesthetically pleasing in isolation.

If none of these are available and the user has no strong opinion, state the
`design-taste-frontend` Section 0.B "Design Read" line, ask **one** question
if genuinely ambiguous, and proceed — but log that you're working from
inference, not reference, so the pre-flight audit (Section 6) gets applied
more strictly.

---

## 1. Reference sources — what each tool is actually for

Verified directly (August 2026), not taken on faith from marketing copy:

### `styles.refero.design` — real DESIGN.md exports
A database of 2,000+ AI-readable design systems extracted from real product
sites (Apple, Notion, Linear, etc.), each with an evocative descriptor
("midnight precision instrument" for Linear, "warm paper notebook" for
Notion) plus colors/type/spacing/components, exportable as `DESIGN.md`.

**How to actually use this — the non-negotiable caveat:** these exports
encode *specific brands' visual identities*. Shipping Linear's literal
palette + type system for an unrelated client is not "premium design," it is
wearing someone else's brand. Use these exports to:
- See how a *category* of product (analytics dashboard, marketing site,
  editorial blog) solves density, hierarchy, and spacing — the structural
  technique, not the hex codes.
- Calibrate a `DESIGN_VARIANCE` / `MOTION_INTENSITY` / `VISUAL_DENSITY`
  reading (Section 1 of `design-taste-frontend`) against a real, shipped
  example instead of guessing blind.
- Never as a source of the actual accent color, font pairing, or component
  radii for a *different* brand's project — those must come from *that*
  brand's brief (Section 11.C of `design-taste-frontend`: extract and lock
  the real brand's tokens, don't import someone else's).

### `haikei.app` — procedural decorative SVG
A generator (not hand-drawn, not AI-hallucinated) for abstract background
assets: Blob Scene, Layered Waves, Wave, Low Poly Grid, Circle Scatter, Blob
Scatter, Blurry Gradient, and more. Exports PNG or editable SVG. Colors and
canvas size are configurable; a randomize control gives quick variations.

**Where this fits:** `design-taste-frontend` Section 4.8 bans hand-rolled
decorative SVG and div-based fake screenshots, and requires a real visual in
every hero — but not every project has a brief that calls for photography
(dashboards, dev tools, abstract/technical brands). Haikei output is the
correct middle ground for those: a real, intentional generated asset instead
of a flat AI-purple gradient blob or an amateur hand-drawn shape. Still
subject to the same rules: one accent family, no neon, tint to the page's
palette (regenerate with the project's actual hex values, don't ship the
tool's defaults).

### `motionsites.ai` — mostly a prompt library, not a code scraper
Checked directly: it's primarily a library of ready-made prompts for AI
website builders (Lovable/Bolt/Cursor/Claude), plus a separate browser
extension ("GetDesign") that can capture an existing site's design into those
tools. It does **not** hand you a real site's actual animation source the way
the "copy the code" framing implies.

**What to actually do for motion references:** if the user has captured a
real site's design/motion via GetDesign or their browser devtools, treat the
captured markup/CSS the same way as a Stitch export — a real reference to
adapt, not to ship verbatim. Otherwise, reach for this repo's own animation
skills (Section 3) rather than assuming an external tool will hand you
working code.

### Pinterest / Dribbble — component-level references
Best used narrow, not broad: search the *specific component* ("pricing card
hover state", "OTP input error state"), not "landing page design" in
general. Screenshot the 1-2 that are actually close and tell the design step
"match this," with the component's exact interaction (not just its static
look) described.

---

## 2. The pipeline

```
0. Gather references (Section 0) ──▶ never skip, even under time pressure
1. Read the brief (design-taste-frontend §0) ──▶ one-line Design Read
2. Existing project? ──▶ redesign-existing-projects audit + design-taste-frontend §11
   New project?      ──▶ design-taste-frontend §1-2 (dials + system pick)
3. Assemble DESIGN.md (stitch-design-taste format) ──▶ single source of truth,
   informed by step 0's references, never invented from the template defaults
4. Library decisions ──▶ pick-ui-library (explicit invoke, does not auto-trigger)
5. Uncertain component ──▶ prototype (explicit invoke) for 2-3 real variants
6. Decorative assets ──▶ Haikei (procedural) or real image-gen, never hand-SVG
7. Build against DESIGN.md
8. Motion pass ──▶ find-animation-opportunities → implement → review-animations
9. Pre-flight audit (Section 6 below) before calling it done
```

Steps 4, 5, and 8's review stage are **explicit-invoke skills**
(`disable-model-invocation: true` in this repo) — they do not fire on their
own. Name them in the prompt.

---

## 3. Tool map (which skill/tool, for which job)

| Need | Reach for |
|---|---|
| First aesthetic direction, dials, anti-slop rules | `design-taste-frontend` |
| Upgrading an existing site without breaking it | `redesign-existing-projects` |
| Portable design-system file for a coding agent | `stitch-design-taste` (this repo) or a `styles.refero.design` export, filtered per Section 1 above |
| "What library should I use for X" | `pick-ui-library` |
| Multiple real variants of one component | `prototype` |
| Decorative background, no photography brief | `haikei.app` (procedural SVG) |
| Real product photography | an image-gen tool if available, else `picsum.photos/seed/{description}` per `design-taste-frontend` §4.8 |
| Full-page hero/section reference images before coding | `image-to-code`, `imagegen-frontend-web`, `imagegen-frontend-mobile` |
| Missing motion | `find-animation-opportunities` |
| Planning a motion overhaul across a codebase | `improve-animations` |
| Reviewing motion against a craft bar | `review-animations` |
| Naming an effect you can't describe | `animation-vocabulary` |
| Apple-style physical/spring interaction | `apple-design` |
| General polish/invisible-detail judgment calls | `emil-design-eng` |

---

## 4. Extracting technique without stealing identity

This is the rule the Instagram-style "steal from the pros" framing skips,
and it's the difference between a designer and a brand-identity thief:

- **Never ship** another real company's literal palette + type pairing +
  wordmark treatment for a different, unrelated client. That is not
  "premium design," it's their brand on someone else's product.
- **Do extract and reuse:** spacing rhythm (how much air between sections),
  type-scale ratios, information hierarchy (what's bold vs. muted vs.
  hidden), component interaction patterns (how a card responds to hover),
  grid logic (how a bento grid resolves asymmetric content).
- **Always re-derive** the actual accent color, font choice, and component
  radii from the real brief in front of you (brand assets if they exist,
  `design-taste-frontend` §0.A signals if not).
- If a client explicitly asks to look "like Linear" or "like Notion" for
  legitimate competitive-positioning reasons, say so out loud in the Design
  Read and get their sign-off — don't silently import a competitor's exact
  identity as a default.

---

## 5. Worked example (from this project)

Teemar (a Muslim women's community/events/mail-subscription site in
Switzerland) went through this exact pipeline without any of the external
tools above being reachable in-session:
1. No user-supplied references existed yet, so references were derived from
   the brief itself — the product literally sells physical mail and event
   tickets, so "correspondence" became the reference concept instead of a
   generic "warm editorial" default.
2. `redesign-existing-projects` audit caught `Fraunces` (a named banned
   default) and a warm-cream ground sitting in the banned hex family.
3. First pass over-corrected into a moody, dark "letterpress invitation on a
   dusk table" — user feedback ("too serious, too dark") drove a second
   pass: same concept, lighter and warmer execution, softened shadows,
   wax-seal swapped for a friendlier washi-tape motif.
4. The final tokens, type system, and anti-pattern list were written up as
   `DESIGN.md` in the project root, in the `stitch-design-taste` format —
   ready to build every remaining screen against.

This is the pipeline working end-to-end without Stitch, Refero, or Haikei
being available — the point isn't that you need every external tool every
time, it's that you never skip Section 0 (real references, even
brief-derived ones) and you always converge on a written `DESIGN.md` before
building.

---

## 6. Pre-flight (before calling any screen done)

Run `design-taste-frontend` Section 14 in full. In addition, specific to this
pipeline:

- [ ] Every color, font, and spacing value in the built screen traces back to
      the project's own `DESIGN.md` — nothing invented ad hoc mid-build.
- [ ] If a `styles.refero.design` or similar export was consulted, confirm no
      literal brand-identity values (another company's exact accent hex,
      exact font, exact wordmark treatment) leaked into this project's
      tokens.
- [ ] If Haikei or similar procedural assets were used, confirm they were
      regenerated in the project's own palette, not shipped in the tool's
      default colors.
- [ ] Motion actually reviewed against `review-animations`, not just
      "implemented and assumed fine."
