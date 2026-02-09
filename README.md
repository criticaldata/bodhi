# Bodhi Research Group Website

A modern, responsive website for the Bodhi Research Group, built with clean HTML, CSS, and JavaScript. Designed in the style of the Applied Antifragility Group website.

## Features

* **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
* **Modern Aesthetics**: Clean layout with red accent colors and professional typography
* **Smooth Animations**: Fade in effects, hover states, and smooth scrolling
* **Mobile Navigation**: Collapsible menu for mobile devices
* **Modular Sections**: Easy to customize and expand
* **No Dependencies**: Pure HTML, CSS, and JavaScript (no frameworks required)

## Setup Instructions

### Option 1: GitHub Pages (Recommended)

1. Clone this repository or upload the files to your GitHub repository
2. Go to your repository settings
3. Scroll down to "GitHub Pages" section
4. Under "Source", select the branch you want to deploy (usually `main` or `master`)
5. Click "Save"
6. Your site will be available at `https://yourusername.github.io/repository-name`

### Option 2: Local Development

1. Download all files to a local directory
2. Open `index.html` in your web browser
3. Or use a local server:
   ```bash
   # Using Python 3
   python -m http.server 8000
   
   # Using Node.js (http-server)
   npx http-server
   ```
4. Navigate to `http://localhost:8000` in your browser

## File Structure

```
bodhi.github.io/
├── index.html          # Main HTML file
├── styles.css          # All styling and responsive design
├── script.js           # Interactive features and animations
└── README.md           # This file
```

## Customization Guide

### Changing Colors

Edit the CSS variables in `styles.css`:

```css
:root {
    --primary-red: #dc2626;      /* Main accent color */
    --dark-red: #991b1b;         /* Darker shade */
    --text-dark: #1f2937;        /* Primary text */
    --text-light: #6b7280;       /* Secondary text */
    --bg-light: #f9fafb;         /* Light background */
}
```

### Updating Content

Open `index.html` and modify:

* **Navigation**: Update links in the `<nav>` section
* **Hero Section**: Change title and subtitle text
* **About Section**: Edit the paragraphs describing your research
* **Paths Section**: Modify the four research path cards
* **Footer**: Update copyright and links

### Adding New Sections

1. Add a new `<section>` in `index.html`
2. Give it a unique `id` attribute
3. Add corresponding styles in `styles.css`
4. Update navigation links if needed

### Modifying Typography

The site uses Google Fonts:
* **Crimson Pro**: Headings and titles (serif)
* **Work Sans**: Body text (sans-serif)

To change fonts, update the Google Fonts link in the `<head>` section of `index.html` and modify the CSS font families.

## Browser Support

* Chrome (latest)
* Firefox (latest)
* Safari (latest)
* Edge (latest)
* Mobile browsers (iOS Safari, Chrome Mobile)

## Performance

* Minimal dependencies (only Google Fonts)
* Optimized CSS with efficient selectors
* Smooth animations using CSS transforms
* Lazy loading for scroll animations

## License

Feel free to use this template for your own research group or organization. Attribution is appreciated but not required.

## Credits

Design inspired by the Applied Antifragility Group website (antifragility.science)

## Support

For issues or questions, please open an issue on the GitHub repository.
