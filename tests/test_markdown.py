from reportgen.markdown import render
def test_render_contains_header():
    md = render([], [])
    assert "Weekly BIOS Update" in md
