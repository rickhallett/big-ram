import csv
import datetime as dt
import pathlib

import yaml

from . import scrape as sc  # ← import the module, not the function
from .diff import price_changes
from .markdown import render
from .rss import collect

CONFIG = pathlib.Path("models.yaml")
PRICES_CSV = pathlib.Path("last_week_prices.csv")
REPORT = pathlib.Path("weekly_report.md")


def _load_models():
    return yaml.safe_load(CONFIG.read_text())


def _snapshot_prices(models):
    today = {}
    for m in models:
        today[m["model"]] = {}
        for vend, url in m["retailers"].items():
            today[m["model"]][vend] = sc.fetch(url)  # ← call via module alias
    return today


def _write_csv(data, path):
    fieldnames = ["Model"] + sorted({v for d in data.values() for v in d})
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for model, vendors in data.items():
            row = {"Model": model, **vendors}
            w.writerow(row)


def _read_csv(path):
    if not path.exists():
        return {}
    out = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            mod = row.pop("Model")
            out[mod] = {k: float(v) if v else None for k, v in row.items()}
    return out


def run():
    models = _load_models()
    feeds = {m["oem_feed"] for m in models}
    updates = list(collect(feeds, [m["model"] for m in models]))

    prev = _read_csv(PRICES_CSV)
    curr = _snapshot_prices(models)
    changes = list(price_changes(prev, curr))

    REPORT.write_text(render(updates, changes, dt.date.today()))
    _write_csv(curr, PRICES_CSV)
    return REPORT
