# The Memory Box 🎁

A magical, interactive birthday gift webapp designed to create an unforgettable romantic experience. Built as a single-file HTML application that requires no installation or setup.

## ✨ Features

### 🎭 **Multi-Stage Experience**
- **Countdown Timer** - Building anticipation with a beautiful countdown
- **Identity Verification** - Playful romantic questions to verify the birthday girl
- **Memory Quiz** - Interactive questions revealing sweet memories
- **Main Gift Experience** - The heart of the Memory Box

### 💝 **Interactive Sections**
- **📸 Photo Memories** - Draggable Polaroid photos connected by threads of fate (2-row layout)
- **🌟 Things I Love** - Sticky notes with thread connections in 4+4 grid
- **🖼️ Gallery Wall** - Photo collection with category filters and lightbox viewer
- **💌 Romantic Letter** - Animated letter with floating hearts on romantic phrases
- **🃏 Confession Flashcards** - Swipeable cards with playful admissions
- **🎯 Inside Jokes** - Personal humor on kraft paper slips
- **🌈 Year Ahead** - Wishes and dreams for the future together

### 🎨 **Romantic Animations**
- Floating hearts that travel across the full screen
- Gentle breathing effects on the letter
- Interactive highlights with hover effects
- Staggered fade-in animations
- Thread connections between elements
- Reduced motion support for accessibility

## 🚀 Quick Start

### Option 1: Download and Open
1. Download `index.html`
2. Open in any modern web browser
3. That's it! No installation required.

### Option 2: Clone Repository
```bash
git clone https://github.com/Himanshu072001/gift-webapp.git
cd gift-webapp
# Open index.html in your browser
```

### Option 3: Deploy Online
- **Vercel**: Import repository for automatic deployment
- **Netlify Drop**: Drag `index.html` to `app.netlify.com/drop`
- **GitHub Pages**: Enable Pages in repository settings

## ⚙️ Customization

All content can be personalized by editing the clearly marked section in `index.html`:

```javascript
/* ================= EDIT THIS ================= */

const BIRTHDAY_DATE = "2026-06-14"; // Target birthday
const HER_NAME = "Ankita"; // Recipient's name

const moments = [
  { date: "3rd May, 2025", title: "First Coffee", note: "...", img: "..." }
  // Add your own memories
];

const loves = [
  "🩷 Your laugh and I forget what I was even worried about.",
  // Add what you love about them
];

// ... and much more!
```

### 📂 File Structure
```
your-folder/
├── index.html             ← The complete webapp
├── optimize_photos.py     ← Optional photo optimization
├── photos_raw/            ← Your original photos
└── photos/                ← Optimized WebP images
    ├── 01.webp
    ├── 101.webp
    └── ...
```

## 🎨 Design System

- **Typography**: Fraunces (headings), Karla (body), Caveat (handwritten)
- **Colors**: Warm romantic palette with soft pinks and warm browns
- **Animation**: Smooth transitions with cubic-bezier easing
- **Accessibility**: Full support for `prefers-reduced-motion`

## 🛠️ Technical Details

### Built With
- **Pure HTML/CSS/JavaScript** - No frameworks or dependencies
- **CSS Grid & Flexbox** - Modern responsive layouts
- **Canvas API** - For thread connection drawings
- **Intersection Observer** - For scroll-based animations
- **CSS 3D Transforms** - For flashcard flip effects

### Browser Support
- Chrome/Edge 88+
- Firefox 86+
- Safari 14+
- Mobile browsers with modern JavaScript support

### Performance
- Single file under 500KB
- No external dependencies
- Optimized for mobile and desktop
- WebP image format for faster loading

## 📱 Mobile Experience

Fully responsive with touch-optimized interactions:
- Swipeable flashcards
- Touch-friendly gallery navigation
- Optimized text sizes and spacing
- Draggable photos work on touch devices

## 🔧 Development

### Testing Features
- **Skip Button**: Invisible skip button in top-right corner for countdown testing
- **Timer Configuration**: Currently set to 1-minute countdown for development
- **Sample Content**: Includes placeholder content and images

### Key Files
- `index.html` - Complete application
- `CONTEXT.md` - Project overview and page flow
- `CLAUDE.md` - Technical implementation guide
- `DESIGN.md` - Visual system documentation

## 🎯 Use Cases

Perfect for:
- 🎂 Birthday surprises
- 💝 Anniversary gifts
- 💕 Valentine's Day presents
- 🎓 Graduation celebrations
- 💒 Wedding memories
- 🎉 Any special occasion

## 🤝 Contributing

This is a personal gift project, but feel free to:
1. Fork for your own romantic projects
2. Submit bug reports
3. Suggest improvements
4. Share your own Memory Box stories!

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 💌 Acknowledgments

Created with love using [Claude Code](https://claude.ai/code) - where AI meets creativity to build something truly special.

---

**Made with 💖 for creating magical memories**

*"Every thread leads back to you."*