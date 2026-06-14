# CLAUDE.md

Guidance for Claude (and Claude Code) when working on **The Memory Box** (`index.html`). Read `CONTEXT.md` and `DESIGN.md` alongside this.

## The golden rule

This is a **gift edited by a non-developer**. Optimize every change for that person's ability to personalize it safely. Keep all user-editable content in the single `/* ================= EDIT THIS ================= */` block, keep it plain-text, and keep the comments above each constant friendly and example-driven.

## Architecture in one breath

A single self-contained `.html` file: inline `<style>`, inline `<script>`, Google Fonts via `<link>`. No frameworks, no bundler, no external JS. Plain DOM APIs only. It must keep working when opened directly from disk (`file://`) and when hosted statically.

## The edit block (source of truth for content)

All personalization is driven by these constants near the top of the `<script>`:

| Constant | Purpose |
|---|---|
| `BIRTHDAY_DATE` | Target date for countdown timer (format: "YYYY-MM-DD"). Memory Box unlocks at midnight on this date. |
| `HER_NAME` | Shown in the hero and `<title>`; auto-substituted into the letter's `[Her Name]`. |
| `moments[]` | Desk Polaroids: `{ date, title, note, img, position }` (position optional: e.g., "top", "center", "bottom"). |
| `LETTER` | `{ dear, body:[paragraphs], sign }`. |
| `loves[]` | Sticky-note strings. |
| `confessions[]` | Flashcard objects: `{ front, back }` for swipeable confession cards. |
| `wishes[]` | Wishes-list strings. |
| `jokes[]` | Inside-joke objects: `{ text, img }` (img maps to a funniest 4-digit photo, which renders as a mini Polaroid taped to the joke). |
| `gallery[]` | Photos list: `{ img, category: "sweet"|"silly"|"chaotic", caption }` |
| `GALLERY_SHAPE` | `"grid"` (framed wall, default) or `"heart"`. |
| `quizQuestions[]` | Quiz questions: `{ question, options:[4 choices], correct:index, memory:"sweet note" }`. |
| `REPLY_TO` | `{ method:"email"|"whatsapp", to }`. |

`sampleImg(i)` (defined above the edit block) generates the inline placeholder images. It is preview-only — never depend on it for real output, and don't remove it unless the user has replaced every `sampleImg(...)` reference.

> Removed in a prior pass: the `songs[]` constant (playlist section) and the `SCREENSAVER_SECONDS` constant (gallery slideshow/screensaver). Don't reintroduce them unless explicitly asked.

## Rules of engagement

- **Never break the edit block contract.** If you add a feature, expose its content/config as a new clearly-commented constant in the edit block, not as inline magic numbers buried in logic.
- **One file.** Do not split into multiple files, add npm packages, or introduce a build step. Inline everything.
- **No browser storage.** `localStorage`/`sessionStorage` are not used and should not be added (they also fail in some sandboxes). State is in-memory only.
- **Respect `prefers-reduced-motion`.** Every animation must have a reduced-motion fallback that shows content statically. There is a `reduce` flag in JS and a `@media (prefers-reduced-motion:reduce)` block in CSS — wire new motion into both.
- **Use the design tokens.** Pull colors from the CSS variables in `:root` and the three fonts (Fraunces / Karla / Caveat). Don't hard-code new hex values or fonts without updating `DESIGN.md`.
- **Mobile + keyboard.** Drag uses Pointer Events (works on touch). Keep tap-targets reasonable, keyboard focus visible, and Escape/arrow keys working in the lightbox.
- **Tone of copy.** Warm, plain, specific, lowercase-leaning handwritten labels. Avoid clichés and purple prose. Sample copy should read like a real person, not a greeting card.

## The gallery ("Us, in pictures")

- `GALLERY_SHAPE = "grid"`: a CSS-columns masonry wall of framed photos with filter tabs ("show all", "sweet memories", "silly snaps", "absolute chaos") and a staggered entrance transition.
- **Heart layout currently disabled**: The optional heart layout (`GALLERY_SHAPE = "heart"`) is commented out due to visibility issues. The CSS and JavaScript for heart layout are preserved in comments and can be re-enabled after fixing the frame visibility problems.
- The lightbox is a **simple viewer**: tap a frame (or inside joke mini-polaroid) to enlarge, previous/next arrows + keyboard ← / →, cross-fade between images, Escape/backdrop to close. There is intentionally **no** slideshow auto-play, no idle screensaver, and no constant Ken-Burns zoom — keep it that way unless asked.

## The confessions flashcards

- **Swipeable carousel**: Flashcards are arranged in a horizontal container with navigation arrows and dot indicators.
- **3D flip effect**: Cards use CSS `transform-style: preserve-3d` with front and back faces. Click any visible card to flip it.
- **Navigation**: Arrow buttons and dot indicators allow moving between cards. Only one card is visible at a time.
- **Touch support**: Cards can be swiped on mobile devices using pointer events.
- **Accessibility**: Reduced motion users get instant flips without transition animations but preserve the flip functionality.

## Known sharp edges

- **Layout timing:** the desk (`layout()`) positions elements absolutely from measured widths in exactly 2 rows. Call it on `load` and `resize`, and guard against a zero/too-small width. After any change that affects element sizes, re-run layout.
- **Flashcard 3D transforms:** Flashcards use CSS `transform-style: preserve-3d` and `backface-visibility: hidden`. The reduced motion media query disables transitions but preserves flip functionality by not overriding transforms completely.
- **Sticky note threads:** Thread connections between sticky notes are drawn using Canvas API with quadratic bezier curves. Drawing is delayed with `setTimeout` to ensure DOM elements are rendered before calculating positions.
- **Heart layout disabled:** The heart layout feature is currently commented out due to frame visibility issues. The positioning calculations work correctly, but frames remain invisible despite having the `.show` class. This appears to be related to CSS specificity or browser security restrictions with fallback images.
- **`sampleImg` security:** When loading the HTML file directly (file://), browser security prevents data URI fallback images from loading, causing gallery frames to appear empty. This is resolved when the site is served via HTTP(S).
- **`sampleImg` IDs:** each SVG uses `id="g"` for its gradient. That's fine because each data-URI is its own isolated document; don't "fix" it by sharing one gradient.

## How to verify a change

There's no test suite. After editing:
1. `node --check` won't work on HTML; instead extract and sanity-check JS logic with `node -e` when math is involved (e.g. heart positions staying within bounds).
2. Confirm the edit block still parses (balanced brackets/quotes) — a stray quote breaks the whole page silently.
3. Spot-check that new motion has a reduced-motion fallback and uses tokens.
4. Re-present the file to the user.

## The countdown and quiz flow

The experience now includes a three-stage pre-Memory Box flow:
1. **Countdown Timer** - shows until `BIRTHDAY_DATE` at midnight. Includes skip button for testing.
2. **Transition Page** - birthday greeting with button to start quiz.
3. **Romantic Quiz** - interactive questions from `quizQuestions[]` with memory reveals.
4. **Main Memory Box** - original gift experience begins.

The countdown, transition, and quiz pages use fixed positioning (`z-index: 100, 90, 80`) and hide/show via opacity transitions. All respect `prefers-reduced-motion`.

## When adding a section

1. Add markup as a `<div class="written">…</div>` block (gets the scroll-reveal automatically).
2. Add its content as a new commented constant in the edit block.
3. Render it from the existing render IIFE.
4. Style it from the design tokens; add a reduced-motion fallback if it animates.
5. Update `CONTEXT.md` (page flow) and `DESIGN.md` (if it introduces a new pattern).
