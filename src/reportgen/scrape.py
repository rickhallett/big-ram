"""Very naive £-price scraper for controlled product pages."""

from __future__ import annotations

import re

import bs4
import requests

_CURRENCY = re.compile(r"£\s?([0-9][0-9,]*\.?[0-9]{0,2})")


def fetch(url: str, timeout: int = 10) -> float | None:
    html = requests.get(
        url, headers={"User-Agent": "Mozilla/5.0"}, timeout=timeout
    ).text
    return parse_price(html)


def parse_price(html: str) -> float | None:
    text = bs4.BeautifulSoup(html, "lxml").text
    m = _CURRENCY.search(text)
    return float(m.group(1).replace(",", "")) if m else None
