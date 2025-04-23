"""Detect price moves ≥ threshold percent."""

from __future__ import annotations

from collections.abc import Generator


def price_changes(
    prev: dict, curr: dict, thresh: float = 5.0
) -> Generator[tuple, None, None]:
    for model, vendors in curr.items():
        for vendor, new in vendors.items():
            old = prev.get(model, {}).get(vendor)
            if old and new and old != 0:
                pct = (new - old) / old * 100
                if abs(pct) >= thresh:
                    yield model, vendor, old, new, round(pct, 2)
