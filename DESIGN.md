# DESIGN.md

The visual and motion system for **The Memory Box**. The brief: a birthday gift that feels like a warm, candlelit keepsake box — intimate, handmade, a little magical — never a generic "website template."

## Concept

A dark desk at night under a pool of warm lamplight. Photos sit on it like real prints; a single **red thread of fate** ties the memories together. Handwriting, tape, and paper textures make it feel physical and personal rather than digital.

## Color tokens

Defined as CSS variables in `:root`. Use these — do not introduce ad-hoc hex values.

| Token | Value | Role |
|---|---|---|
| `--ink` | `#14151c` | Desk / page base (night) |
| `--ink-2` | `#1b1d27` | Secondary dark surface |
| `--lamp` | `#ffd79a` | Warm candlelight glow / highlights |
| `--paper` | `#f3ece0` | Polaroids, frames, letter, cards |
| `--paper-edge` | `#e3d9c7` | Paper edge tint |
| `--thread` | `#c5362b` | The red thread of fate (signature) |
| `--thread-glow` | `#e8584b` | Thread glow / warm accent |
| `--pencil` | `#3a342c` | Handwriting / ink on paper |
| `--muted` | `#9b94a3` | Dimmed secondary text |

**The signature element is the red thread.** Spend boldness there; keep everything else quiet. Warm accents (`--thread`, `--lamp`) are for emphasis only.

## Typography

Three roles, loaded from Google Fonts:

- **Display — Fraunces** (serif, optical sizing): headlines, her name, finale lines. Soft, characterful, romantic. Used with restraint.
- **Body — Karla** (humanist sans): paragraphs, UI labels, the letter body. Friendly and readable.
- **Handwriting — Caveat**: dates, captions, sticky notes, kraft slips, the reply box, small affectionate labels. Carries the "handmade" feeling.

Headlines often use a cream→lamp gradient clipped to text. Keep type sizes fluid (`clamp()`).

## Layout & structure

- Centered single-column reading width for written sections (`.written`, ~760px; gallery wrapper wider).
- The **desk** positions Polaroids absolutely from measured pixel widths, recomputed on `load`/`resize`. The **heart** gallery (optional) does the same via `heartLayout()`.
- Numbering/eyebrows are used as small handwritten "labels" (e.g., "every single one"), not as a rigid numbered system — order isn't the point, intimacy is.

## Signature components

### **Main Memory Box Components:**
- **Polaroid:** cream card, photo, a strip of translucent "tape," handwritten caption, slight rotation. Draggable (Pointer Events); tap lifts it into a reading card.
- **Red thread:** an SVG path that weaves between the Polaroids' tape points, with a slight droop like real string, and follows them when dragged.
- **Letter:** taped sheet of faintly ruled paper, handwritten "Dear …", body in Karla, handwritten sign-off.
- **Sticky notes / kraft slips:** small rotated paper scraps in warm note colors / kraft tones with a torn/perforated edge.
- **Photo gallery ("Us, in pictures"):** small framed prints. Default is a tidy framed **wall** (CSS-columns masonry); an optional **heart** arrangement places the same frames along a heart curve. Frames open a simple full-screen viewer.

### **Pre-Experience Components:**
- **Countdown Timer:** four glass-style units showing days/hours/minutes/seconds with gradient numbers. Includes floating heart decorations.
- **Transition Page:** birthday greeting with elegant button styling (red thread color, shadow, hover lift).
- **Quiz Container:** frosted glass card with backdrop blur, contains question text, multiple choice options, and memory note reveals.
- **Quiz Options:** interactive buttons with hover states, visual feedback for correct/wrong answers, smooth selection highlighting.

## Motion inventory

One orchestrated, romantic sequence rather than scattered effects. Everything below is disabled (shown static) under `prefers-reduced-motion`.

| Effect | Where | Feel |
|---|---|---|
| **Pre-Experience Animations:** | | |
| Countdown numbers | Timer units | Real-time updates with smooth number transitions, gradient text. |
| Floating hearts | Countdown/Transition | Gentle floating hearts around countdown display and transition page. |
| Countdown hearts pulse | Timer decorations | Soft pulsing hearts with offset timing for organic feel. |
| Page transitions | Between stages | Smooth opacity fades between countdown → transition → quiz → main box. |
| Quiz memory reveal | After answer selection | Memory note slides up with gentle fade-in after correct answer. |
| **Main Memory Box Animations:** | | |
| Develop-in | Polaroids on load | Photos fade up and brighten from dim, like a developing Polaroid, staggered. |
| Self-drawing thread | Red thread on load | Stroke draws itself across the memories once. |
| Breathing lamp | Background glow | Slow swell/fade of the candlelight pool. |
| Drifting hearts | Background | Sparse, low-opacity hearts float upward as ambience. |
| Scroll reveals | `.written` / `.finale` / grid frames | Sections and framed photos rise + fade in on entry. |
| Hover lift | Framed photos | Frame lifts and the photo zooms slightly on hover. |
| Beating seal | Finale heart | Gentle double-thump heartbeat. |
| Lightbox cross-fade | Viewer next/prev | Images fade between each other. |
| Heart beat + float | Gallery, **heart mode only** | The whole photo-heart pulses (`heartThrob`) while each photo gently floats out of sync (`floatPhoto`). Scoped to `.wall.heart`. |

> Removed: the lightbox slideshow auto-play, the idle full-screen "screensaver," and the constant Ken-Burns zoom on enlarged photos. The viewer is now a still, manual, framed enlargement.

### Motion principles

- **Subtlety over spectacle.** Low opacities, slow durations, easing that settles. Excess animation reads as AI-generated; restraint reads as intentional.
- **Serve the subject.** Each effect maps to the metaphor (developing photos, a thread being drawn, candlelight, a heartbeat).
- **Always provide a calm fallback.** Wire new motion into both the CSS `@media (prefers-reduced-motion:reduce)` block and the JS `reduce` flag.

## Accessibility floor

- Reduced motion respected throughout.
- Keyboard: Escape closes the lightbox; ← / → navigate.
- Touch: dragging and tapping via Pointer Events.
- Images carry `alt` text (caption or "us").
- Sufficient contrast: cream/lamp text on ink; ink text on paper.

## Copy voice

Warm, plain, specific. Lowercase handwritten labels; sentence-case headlines. Favor concrete, slightly imperfect lines ("the way you fall asleep halfway through every movie") over polished sentiment. No clichés, no exclamation pile-ups.

## Extending the design

When adding anything: reuse a token and one of the three fonts, lean on the paper/ink/thread material language, give it at most one small motion that fits the metaphor, and confirm it still feels like the same handmade box — not a new app bolted on.
