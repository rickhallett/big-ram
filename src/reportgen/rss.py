import datetime as dt

import feedparser


def collect(feed_urls, models):
    for url in feed_urls:
        feed = feedparser.parse(url)
        for e in feed.entries:
            if any(m.lower() in e.title.lower() for m in models):
                yield {
                    "title": e.title,
                    "link": e.link,
                    "published": dt.datetime(*e.published_parsed[:6]),
                }
