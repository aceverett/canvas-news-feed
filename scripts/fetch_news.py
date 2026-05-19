import json
import time
from datetime import datetime, timezone

import feedparser

FEEDS = [
    {
        "name": "Music Business Worldwide",
        "url": "https://www.musicbusinessworldwide.com/feed/",
    },
    {
        "name": "Billboard",
        "url": "https://www.billboard.com/feed/",
    },
]

OUTPUT_FILE = "news.json"
MAX_ITEMS_PER_FEED = 10


def parse_date(entry):
    parsed = None
    for attr in ("published_parsed", "updated_parsed", "created_parsed"):
        parsed = entry.get(attr)
        if parsed:
            break

    if parsed:
        return datetime.fromtimestamp(time.mktime(parsed), tz=timezone.utc)

    date_str = entry.get("published") or entry.get("updated") or entry.get("date")
    if date_str:
        try:
            parsed = feedparser._parse_date(date_str)
            if parsed:
                return datetime.fromtimestamp(time.mktime(parsed), tz=timezone.utc)
        except Exception:
            pass

    return datetime.now(timezone.utc)


def normalize_entry(item, source):
    title = item.get("title", "")
    link = item.get("link", "")
    date = parse_date(item)
    return {
        "title": title,
        "link": link,
        "source": source,
        "date": date.isoformat().replace("+00:00", "Z"),
        "sort_date": date.isoformat(),
    }


def main():
    items = []

    for feed in FEEDS:
        parsed = feedparser.parse(feed["url"])
        entries = parsed.entries[:MAX_ITEMS_PER_FEED]

        for entry in entries:
            normalized = normalize_entry(entry, feed["name"])
            items.append(normalized)

    items.sort(key=lambda row: row["sort_date"], reverse=True)
    output = [
        {"title": item["title"], "link": item["link"], "source": item["source"], "date": item["date"]}
        for item in items
    ]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
        json.dump(output, out_file, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
