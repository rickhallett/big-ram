### 📑 Reflections on the *Agent-Driven Build-Plan* Experiment  
*(Big Ram project – 23 Apr 2025)*

---

## 1. What we set out to prove

| Goal | Metric of success |
|------|-------------------|
| **Agent can scaffold a full Python package** (typed code, tests, CI, weekly cron) *without* manual coding. | ✔ End-to-end pipeline passes locally & in GitHub Actions. |
| **Atomic commit log** per feature/gate. | ✔ 11 conventional commits, each green. |
| **Quality gates baked-in** (Black / isort / Ruff / MyPy / pytest). | ✔ Every step enforced gates before committing. |

---

## 2. Timeline of the day

| Time | Key event | Lesson |
|------|-----------|--------|
| **09:30 UTC** | Drafted initial `build_plan.yaml`; agent ran, **blocked by MyPy** (strict mismatch). | Static typing *while generating* causes churn. |
| 10:10 | Added MyPy ignore flags; progressed until **markdown type mismatch**; several patch steps. | Duplicate plan blocks → stale code. Prefer *single* source of truth. |
| 11:20 | CI failed: wrong action name `astral-sh/uv-action@v1`. | Spell-checking external IDs early saves cycles. |
| 12:05 | Fixed to `setup-uv`, but runner lacked venv; **`uv pip` failed**. | `setup-uv` ≠ `uv venv`. Always create + export `.venv`. |
| 13:00 | Added `$GITHUB_ENV` yet PATH still missing; **black not found**. | Must also write to `$GITHUB_PATH`. |
| 13:20 | Final push: tests, style, CI ✓. | Success criteria met. |

---

## 3. Key take-aways

### 3.1 Strengths of the build-plan agent

* **Reproducibility** – A single command rebuilds the repo exactly.
* **Auditability** – Each commit shows *what* and *why* and passed all gates.
* **On-rails quality** – Lint/format/test policy cannot be skipped.
* **Scalable template** – Can generate many cookie-cutter repos in minutes.

### 3.2 Pain points encountered

| Category | Pain | Mitigation next time |
|----------|------|----------------------|
| **Type churn** | MyPy aborted plan 5× for annotation mismatches. | ➊ Run MyPy only in CI until code stabilises. ➋ Or start with `Any`/`object`, refine later. |
| **Plan duplication** | Same file edited in 4 YAML blocks → drift. | Keep **one** canonical block; use `canmore` canvas if incremental edits needed. |
| **External action errors** | Miss-typed action name & missing venv repeated. | Validate workflow file locally with `act -j test` before committing. |
| **PATH handling** | `$GITHUB_ENV` ≠ `$GITHUB_PATH`. | Add a generic “ensure .venv/bin on PATH” snippet to scaffolding template. |

---

## 4. Optimised recipe for the next project

1. **Bootstrap skeleton via build-plan agent**  
   *Deps → pkg → minimal code + tests → CI (style + tests)*  
   *Skip MyPy gate here.*

2. **Switch to IDE-agentic loop (Cursor/Copilot)**  
   – rapid refactoring, richer context.

3. **Gradually tighten MyPy**  
   *Add after first feature set; fail only in CI.*

4. **Pre-flight GitHub Actions**  
   Run [`act`](https://github.com/nektos/act) locally or `gh actions run` to catch missing actions, env var mistakes.

5. **Shared snippets library**  
   Store proven YAML fragments (setup-uv, venv export) in a gist or repo for copy-paste.

---

## 5. Reusable building blocks harvested today

* `build_plan.yaml` format with eight lean steps.  
* **agent.py** that enforces Black → isort → Ruff → pytest before commit.  
* GitHub workflow template with `setup-uv`, `.venv`, PATH export.  
* Typed utility modules (`rss`, `scrape`, `diff`, `markdown`, `pipeline`).  

---

## 6. Open improvements

| Area | Idea |
|------|------|
| **HTTP politeness** | Cache retailer pages & respect `robots.txt`. |
| **Artifact storage** | Push `.md` & `.csv` to a dedicated branch or S3. |
| **Alerting** | Open PR or send mail when price diff ≥ 5 %. |
| **Multi-OEM support** | Parameterise OEM feed list from config file. |
| **Stub packages** | Add `types-requests`, `types-PyYAML` to enable MyPy strict mode in CI. |
| **Plan linter** | Small script to detect duplicate step IDs & stale file blocks. |

---

### 7. Verdict

*The agent-driven plan **excelled at deterministic scaffolding and policy
compliance**, but proved slower for iterative type-tuning than an IDE
assistant.* A **hybrid workflow**—bootstrapping with the agent, then
coding/refining in the IDE—offers the best of both worlds.