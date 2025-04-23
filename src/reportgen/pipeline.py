from __future__ import annotations

import csv
import datetime as dt
import pathlib

import yaml

from . import scrape as sc  # module import, easy to patch
from .diff import price_changes
from .markdown import render
from .rss import collect

CONFIG = pathlib.Path("models.yaml")
PRICES_CSV = pathlib.Path("last_week_prices.csv")
REPORT = pathlib.Path("weekly_report.md")


def _load_models() -> list[dict]:
    return yaml.safe_load(CONFIG.read_text())


def _snapshot_prices(models: list[dict]) -> dict:
    today: dict = {}
    for m in models:
        today[m["model"]] = {v: sc.fetch(u) for v, u in m["retailers"].items()}
    return today


def _write_csv(data: dict, path: pathlib.Path) -> None:
    fieldnames = ["Model"] + sorted({v for d in data.values() for v in d})
    with path.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for model, vendors in data.items():
            w.writerow({"Model": model, **vendors})


def _read_csv(path: pathlib.Path) -> dict:
    if not path.exists():
        return {}
    out: dict = {}
    with path.open() as f:
        for row in csv.DictReader(f):
            mod = row.pop("Model")
            out[mod] = {k: float(v) if v else None for k, v in row.items()}
    return out


def run() -> pathlib.Path:
    models = _load_models()
    feeds = {m["oem_feed"] for m in models}
    updates = list(collect(feeds, [m["model"] for m in models]))
    prev = _read_csv(PRICES_CSV)
    curr = _snapshot_prices(models)
    changes = list(price_changes(prev, curr))
    REPORT.write_text(render(updates, changes, dt.date.today()))
    _write_csv(curr, PRICES_CSV)
    return REPORT
