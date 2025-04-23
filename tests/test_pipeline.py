import yaml
from reportgen.pipeline import CONFIG, run


def test_pipeline_runs(tmp_path, monkeypatch):
    # minimal config + monkey-patched fetch to skip HTTP
    cfg = [
        {
            "model": "Foo",
            "retailers": {"Test": "http://example"},
            "oem_feed": "tests/data/fake_feed.xml",
        }
    ]
    CONFIG.write_text(yaml.safe_dump(cfg))
    import reportgen.scrape as sc

    monkeypatch.setattr(sc, "fetch", lambda *_: 100.0)
    report = run()
    assert report.exists()
