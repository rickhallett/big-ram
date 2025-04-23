from reportgen.scrape import parse_price


def test_parse_price() -> None:
    assert parse_price("<p>Only £1,234.56!</p>") == 1234.56
