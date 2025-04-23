def price_changes(prev: dict, curr: dict, thresh=5.0):
    """
    Compare two nested dicts {model:{vendor:price}}.
    Yield tuples (model, vendor, old, new, pct).
    """
    for model, vendors in curr.items():
        for vendor, new in vendors.items():
            old = prev.get(model, {}).get(vendor)
            if old is None or new is None or old == 0:
                continue
            pct = (new - old) / old * 100
            if abs(pct) >= thresh:
                yield model, vendor, old, new, round(pct, 2)
