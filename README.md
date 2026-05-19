# Canvas News Feed

A lightweight news marquee and dashboard tool designed for LMS embeds such as Canvas.

- **Demo page**: [index.html](./index.html)
- **Ticker embed**: `marquee.html`
- **Dashboard view**: `feed.html`
- **Data source**: `news.json`
- **Feed configuration**: `config.json`

## Overview

This repository contains a reusable news headline ticker that pulls RSS/Atom feed data, generates a static JSON payload, and renders an infinite marquee animation that is optimized for smaller iframe viewports.

The marquee is built to be embedded in Canvas or any other LMS using an `<iframe>` and includes pause-on-hover/focus accessibility support.

## Demo

Open the demo in your browser:

- [Live demo page](https://aceverett.github.io/canvas-news-feed/)


## Forking and Reusing

1. Fork this repository to your own GitHub account.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/<your-user>/canvas-news-feed.git
   cd canvas-news-feed
   ```
3. Install the Python dependency:
   ```bash
   python3 -m pip install -r requirements.txt
   ```
4. Update `config.json` with your own data sources and project metadata.
5. Run the feed generation script to build `news.json`:
   ```bash
   python3 scripts/fetch_news.py
   ```
6. Open `index.html` or `marquee.html` in a browser to verify the design.

## Customizing RSS Feeds / Sources

The feed sources are configured in `config.json`.

Example:

```json
{
  "project_title": "Live Headline Dashboard",
  "project_description": "Browse the latest headlines compiled from multiple sources in one clean, responsive grid.",
  "refresh_interval_hours": 4,
  "feeds": [
    { "name": "Music Business Worldwide", "url": "https://www.musicbusinessworldwide.com/feed/" },
    { "name": "Billboard", "url": "https://www.billboard.com/feed/" }
  ]
}
```

### Add or change feeds

- Edit the `feeds` array in `config.json`.
- Each item should include a `name` and a `url`.
- Use valid RSS/Atom feed URLs from the publications you want to surface.

### Regenerate the JSON payload

After updating `config.json`, run:

```bash
python3 scripts/fetch_news.py
```

This script reads the RSS feeds, normalizes each entry, sorts by date, and writes the result to `news.json`.

## What each file does

- `index.html` — demo page with links and descriptions for the project.
- `marquee.html` — the headline ticker that is intended for Canvas iframe embedding.
- `feed.html` — a full dashboard page that displays the news as cards with search/filter support.
- `news.json` — the static data file consumed by the pages.
- `config.json` — feed source configuration, title text, and refresh interval.
- `scripts/fetch_news.py` — the Python script that generates `news.json` from RSS/Atom feeds.
- `requirements.txt` — Python dependencies (`feedparser`).

## Embedding in Canvas or another LMS

Use the marquee page as the embedded iframe source:

```html
<iframe
  src="https://<your-host>/canvas-news-feed/marquee.html"
  width="100%"
  height="120"
  style="border:0;"
  scrolling="no"
  title="Live news ticker"
></iframe>
```

### Canvas-specific notes

- Create an external tool or HTML content item and paste the iframe markup.
- Use `width="100%"` so the ticker fills the Canvas content area.
- Adjust the `height` to fit your layout, typically `100px` to `140px` depending on font size.
- If Canvas blocks inline frames, host the repo on a trusted static site or GitHub Pages and use that public URL.

## Accessibility and behavior

- The ticker pauses when hovered or focused.
- The feed data is loaded from `news.json` to avoid browser CORS restrictions.
- The marquee animation is optimized for smaller embedded viewports when used inside an iframe.

## Extending the project

- Change the animation speed or spacing in `marquee.html`.
- Add additional metadata fields to the JSON output and display them in `feed.html`.
- Swap the feed generation script with a server-side API if you need dynamic updates.

## License

This repository is open for reuse and customization. Feel free to fork and adapt it for your own LMS or content pipeline.
