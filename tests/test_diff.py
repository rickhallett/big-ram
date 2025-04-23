from reportgen.diff import price_changes


def test_diff_detects_change() -> None:
    changes = list(price_changes({"A": {"Shop": 100}}, {"A": {"Shop": 108}}, 5))
    assert changes[0][-1] == 8.0
