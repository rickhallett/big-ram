from reportgen.rss import collect
def test_filter():
    feed = ["tests/data/fake_feed.xml"]
    models = ["XPS 14"]
    items = list(collect(feed, models))
    assert items and all("XPS 14" in i["title"] for i in items)
