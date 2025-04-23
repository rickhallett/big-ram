## Pre-flight Checklist (run this **before** `uv run python agent.py`)

| ✔︎ | Item | Why it matters | Quick check / fix |
|---|------|----------------|-------------------|
| ✔︎ **`uv` installed globally** | Agent invokes `uv pip …` & `uv run …`. | `uv --version` should print a version. If not: `pipx install uv` or `pip install uv`. |
| ✔︎ **PyYAML available *before* agent starts** | `agent.py` parses `build_plan.yaml` before installing deps. | `python -c "import yaml"` should succeed. If not, `pip install pyyaml` (outside env) or switch agent to `json`. |
| ✔︎ **Git repo initialised & clean** | Agent commits after each passing step. | `git status` ⇒ “nothing to commit”. If brand-new repo: `git commit --allow-empty -m "chore: init"`. |
| ✔︎ **`models.yaml` skeleton present** | The CLI needs it at runtime. | Example minimal file:  <br>`- model: "XPS 14"`<br>`  oem_feed: tests/data/fake_feed.xml`<br>`  retailers:`<br>`    Dummy: https://example.com` |
| ✔︎ **`tests/data/fake_feed.xml` populated** | `tests/test_rss.py` expects “XPS 14” title. | Minimal feed:  <br>```xml<br><rss version="2.0"><channel><title>dummy</title><item><title>XPS 14 BIOS 1.2</title><link>http://example</link><pubDate>Wed, 23 Apr 2025 10:00:00 GMT</pubDate></item></channel></rss>``` |
| ✔︎ **`lxml` included or parser switched** | `BeautifulSoup(html, "lxml")` needs `lxml`. | Add `lxml` to step-4 `deps:` *or* change code to `"html.parser"`. |
| ✔︎ **Workflow permissions** | `GITHUB_TOKEN` must push commits. | Ensure workflow YAML has:<br>`permissions: { contents: write }` |
| ✔︎ **Remote write access** | CI push-back step needs it. | For GitHub repo you own: nothing extra. For forks/orgs: enable “Allow GitHub Actions to write contents”. |

*Optional extras:* `.editorconfig`, pre-commit hooks, system build tools for `lxml` headers.

When every box is ticked, run:

```bash
uv run python agent.py
