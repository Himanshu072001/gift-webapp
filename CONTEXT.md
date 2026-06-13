# CONTEXT

## What this is

**The Memory Box** — a single-page, self-contained website built as a birthday gift for a partner. It's an interactive digital keepsake: photos, a heartfelt letter, things-I-love notes, wishes, inside jokes, a wall of framed photos, and a way for her to write back.

It is **one file**: `memory-box.html`. No build step, no dependencies to install, no server required. It runs by opening the file in a browser.

## Who it's for

- **The recipient:** the giver's girlfriend, on her birthday. The experience should feel warm, personal, and a little magical — like opening a real box of memories.
- **The editor (the giver):** non-developer friendly. All personalizable content lives in one clearly marked `/* EDIT THIS */` block near the bottom of the file. Editing is plain text — no code knowledge needed beyond replacing quoted strings.

## Current state

Fully working and populated with **sample content** (illustrated placeholder images generated inside the file, a complete sample letter, sample captions). It previews correctly with zero setup. The giver replaces the samples with real photos and words.

## Page flow (complete experience)

### **Pre-Memory Box Experience:**
1. **Countdown Timer** — shows days, hours, minutes, seconds until her birthday at midnight. Includes floating hearts animation and "skip countdown →" button for testing.
2. **Transition Page** — appears when countdown ends with "Happy Birthday!" message and "Let's reminisce ♡" button to start the quiz.
3. **Romantic Quiz** — 5 interactive memory-based questions with multiple choice answers. Each correct answer reveals a sweet memory note. Includes navigation between questions.

### **Main Memory Box (after quiz completion):**
4. **Hero** — "happy birthday" + her name + intro line.
5. **The desk** — draggable Polaroid photos scattered on a dark desk, connected by a red "thread of fate." Tap a photo to lift it and read the memory.
6. **Things I love about you** — sticky notes.
7. **This year, I hope we…** — wishes for the year ahead.
8. **Our inside jokes** — kraft-paper slips.
9. **Us, in pictures** — every photo shown as a framed print on a wall. Tap any photo to open a full-screen viewer with previous/next arrows (and keyboard ← / →) and a soft cross-fade between images. The arrangement defaults to a tidy grid; an optional heart layout is available via a switch.
10. **An open letter** — a longer written message on a taped sheet of paper.
11. **Write me back** — a reply box; her message opens a prefilled email or WhatsApp addressed to the giver.
12. **Finale** — a beating heart seal + closing line.

> Note: an earlier "Songs that remind me of you" playlist section and the gallery slideshow/auto-play "screensaver" have been removed. The gallery is now a simple framed wall with tap-to-enlarge.

## File layout when deployed

```
your-folder/
├── memory-box.html        ← the site
└── photos/                ← the giver's real images
    ├── first-date.jpg
    ├── goa.jpg
    └── ...
```

Sample images are generated in-code, so `photos/` is only needed once real photos are added.

## Hosting

Free options, no account complexity:
- **Netlify Drop** (`app.netlify.com/drop`) — drag the HTML file (plus `photos/` folder) to get an instant shareable link.
- **GitHub Pages** — commit the file and enable Pages.

## Non-goals

- No backend, database, accounts, or analytics.
- No persistent storage in the page itself (her reply is sent via email/WhatsApp, not stored).
- Not a template engine or CMS — it's a personal, hand-edited artifact.

## Related docs

- `CLAUDE.md` — guidance for Claude / Claude Code when editing this project.
- `AGENT.md` — conventions and tasks for any AI agent.
- `DESIGN.md` — the visual system, tokens, and animation inventory.
