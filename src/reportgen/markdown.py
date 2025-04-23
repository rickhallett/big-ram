import datetime as dt
TEMPLATE = """# Weekly BIOS Update & Price Change Report ({date})
## New BIOS/Firmware Updates
{updates}
## Price Changes (≥ 5%)
{prices}
"""
def md_updates(items):
    if not items:
        return "*No new BIOS or firmware updates this week.*"
    lines = [f"- **{i['title']}** – [{i['link']}]({i['link']}) "
             f"({i['published'].date()})" for i in items]
    return "\n".join(lines)
def md_prices(changes):
    if not changes:
        return "*No significant price changes this week.*"
    rows = "| Model | Retailer | Old | New | % |\n|---|---|---|---|---|"
    for m, v, o, n, p in changes:
        rows += f"\n| {m} | {v} | £{o:.2f} | £{n:.2f} | {'+' if p>0 else ''}{p}% |"
    return rows
def render(updates, changes, date=None):
    return TEMPLATE.format(
        date=(date or dt.date.today()),
        updates=md_updates(updates),
        prices=md_prices(changes),
    )
