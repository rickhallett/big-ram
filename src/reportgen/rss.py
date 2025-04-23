"""Filter OEM RSS feeds for entries that mention our models."""

from __future__ import annotations

import datetime as dt
from typing import Any, Iterable, Iterator, Mapping

import feedparser


def collect(
    feed_urls: Iterable[str], models: Iterable[str]
) -> Iterator[Mapping[str, Any]]:
    wanted = [m.lower() for m in models]
    for url in feed_urls:
        feed = feedparser.parse(url)
        for e in feed.entries:
            if any(m in e.title.lower() for m in wanted):
                yield {
                    "title": str(e.title),
                    "link": str(e.link),
                    "published": dt.datetime(*e.published_parsed[:6]),
                }
