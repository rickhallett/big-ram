from reportgen.diff import price_changes

prev = {"A": {"Shop": 100}}
curr = {"A": {"Shop": 108}}


def test_diff_detects_change():
    changes = list(price_changes(prev, curr, 5))
    assert changes and changes[0][-1] == 8.0
