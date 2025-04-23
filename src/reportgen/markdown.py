from __future__ import annotations

import datetime as dt

TEMPLATE = """# Weekly BIOS Update & Price Change Report ({date})
## New BIOS/Firmware Updates
{updates}
## Price Changes (≥ 5%)
{prices}
"""


def _md_updates(items: list[dict]) -> str:
    if not items:
        return "*No new BIOS or firmware updates this week.*"
    return "\n".join(
        f"- **{i['title']}** – [{i['link']}]({i['link']}) " f"({i['published'].date()})"
        for i in items
    )


def _md_prices(changes: list[tuple]) -> str:
    if not changes:
        return "*No significant price changes this week.*"
    rows = ["| Model | Retailer | Old | New | % |", "|---|---|---|---|---|"]
    for m, v, o, n, p in changes:
        rows.append(
            f"| {m} | {v} | £{o:.2f} | £{n:.2f} | " f"{'+' if p>0 else ''}{p}% |"
        )
    return "\n".join(rows)


def render(
    updates: list[dict], changes: list[tuple], date: dt.date | None = None
) -> str:
    return TEMPLATE.format(
        date=(date or dt.date.today()),
        updates=_md_updates(updates),
        prices=_md_prices(changes),
    )
