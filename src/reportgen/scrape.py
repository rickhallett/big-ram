import re, requests, bs4
_CURRENCY = re.compile(r"£\s?([0-9][0-9,]*\.?[0-9]{0,2})")
def fetch(url: str, timeout: int = 10) -> float | None:
    """
    Retrieve *url* and return the first £‐price as a float.
    Very naive but works for controlled test fixtures.
    """
    html = requests.get(url, headers={"User-Agent": "Mozilla/5.0"},
                        timeout=timeout).text
    return parse_price(html)
def parse_price(html: str) -> float | None:
    """Extract the first Sterling price from raw HTML."""
    m = _CURRENCY.search(bs4.BeautifulSoup(html, "lxml").text)
    return float(m.group(1).replace(",", "")) if m else None
