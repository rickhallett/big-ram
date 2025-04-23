from reportgen.rss import collect


def test_filter() -> None:
    items = list(collect(["tests/data/fake_feed.xml"], ["XPS 14"]))
    assert items and all("XPS 14" in i["title"] for i in items)
