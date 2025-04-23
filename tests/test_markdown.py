from reportgen.markdown import render


def test_header() -> None:
    assert "Weekly BIOS Update" in render([], [])
