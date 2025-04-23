import yaml
from reportgen.pipeline import CONFIG, run


def test_pipeline_runs(tmp_path, monkeypatch) -> None:
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
    assert run().exists()
