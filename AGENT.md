# AGENT.md

Operating manual for any AI agent working in this repository. For Claude-specific notes see `CLAUDE.md`; for visual rules see `DESIGN.md`; for the big picture see `CONTEXT.md`.

## Project at a glance

- **Type:** static, single-file web page (`memory-box.html`).
- **Stack:** plain HTML + CSS + vanilla JS, Google Fonts via CDN link. No framework, no build, no package manager, no server.
- **Run:** open `memory-box.html` in any modern browser (works from `file://`).
- **Deploy:** drag to Netlify Drop, or push to GitHub Pages. Ship the HTML file plus the `photos/` folder.

## Repository conventions

- **Single source file.** Do not introduce additional source files, modules, or a bundler. CSS and JS stay inline.
- **No dependencies.** No `npm install`, no CDN scripts beyond the Google Fonts stylesheet. If a feature seems to need a library, implement it with platform APIs instead.
- **Content vs. code separation.** Everything a human personalizes lives in the `EDIT THIS` block as commented constants. Logic lives below it. Never mix hard-coded user content into the logic.
- **Comments are UX.** The comments in the edit block are the closest thing this project has to a UI for the editor. Keep them short, friendly, and show a concrete example for any non-obvious field.

## Current content constants

`HER_NAME`, `moments[]`, `LETTER`, `loves[]`, `wishes[]`, `jokes[]`, `gallery[]`, `GALLERY_SHAPE` (`"grid"` default / `"heart"`), `REPLY_TO`, plus the preview-only `sampleImg()` generator above the block.

> Previously present and since removed: `songs[]` (playlist) and `SCREENSAVER_SECONDS` (gallery slideshow/screensaver). The gallery is now a framed wall with a plain tap-to-enlarge viewer — no auto-play.

## Editing workflow

1. **Read first.** Open the file and locate: the `:root` token block, the `EDIT THIS` block, the render IIFE, the `layout()`/`heartLayout()` functions, the lightbox logic, and the two reduced-motion paths (CSS media query + JS `reduce` flag).
2. **Make the smallest change that satisfies the request.** Prefer extending an existing pattern over inventing a new one.
3. **Keep edits surgical.** Use exact-match string replacement; re-read the file region before editing it again, since prior edits invalidate earlier views.
4. **Verify** (see below).
5. **Update docs** if the page flow, a config constant, or a design pattern changed.

## Verification checklist

- Brackets and quotes in the edit block are balanced (one bad quote silently blanks the page).
- Any new animation has a `prefers-reduced-motion` fallback in **both** the CSS media query and the JS `reduce` branch.
- New colors/fonts come from existing tokens, or `DESIGN.md` is updated to add them.
- Absolutely-positioned layouts (`layout()`, and `heartLayout()` in heart mode) still run on `load` + `resize` and handle a not-yet-measured width.
- Lightbox keyboard controls (Esc, ←, →) and touch dragging on the desk still work.
- For anything involving geometry/math, validate with a quick `node -e` script (e.g., confirm computed positions stay within container bounds) since the page itself can't be unit-tested headlessly here.

## Task playbook

- **Add a content section:** new `<div class="written">` block → new commented constant in edit block → render from the IIFE → style from tokens → reduced-motion fallback → update `CONTEXT.md`.
- **Add an animation:** define `@keyframes` + class in CSS, gate it behind the `reduce` checks, prefer one orchestrated moment over many scattered effects (see `DESIGN.md`).
- **Change a layout shape (e.g., gallery):** add or use a switch constant in the edit block (like `GALLERY_SHAPE`) rather than hard-replacing, so the editor can revert.
- **Wire an external action (reply, links):** keep it stateless — build a `mailto:`/`https://wa.me/` URL or open a link; do not add storage or a backend.

## Guardrails

- Don't add tracking, analytics, or third-party scripts.
- Don't use browser storage APIs.
- Don't reintroduce the playlist or the slideshow/screensaver unless explicitly asked.
- Don't remove `sampleImg` until every reference to it is gone.
- Don't regress accessibility (focus visibility, reduced motion, keyboard nav, alt text).
- Keep the experience self-contained and offline-capable.
