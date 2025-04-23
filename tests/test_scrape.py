from reportgen.scrape import parse_price
SAMPLE = "<html><p>Only £1,234.56 today!</p></html>"
def test_parse_price():
    assert parse_price(SAMPLE) == 1234.56
