### Head-less `agent.py` workflow vs. IDE-embedded copilot

| Aspect | `agent.py + build_plan.yaml` (head-less) | IDE-embedded agent (Cursor, Copilot, etc.) |
|---|---|---|
| **Execution mode** | One unattended command drives install → code-gen → tests → conventional commits. | Interactive suggestions; you still run tests, accept changes, commit. |
| **Determinism / reproducibility** | Declarative YAML + lockfile ⇒ byte-for-byte commits anywhere. | Output varies with prompt history / randomness; needs manual tweaks. |
| **Audit trail** | Each green step auto-commits (atomic, Conventional Commits). | History depends on human staging; commits may mix unrelated changes. |
| **Human time required** | Near-zero until final review—perfect for boilerplate and CI scaffolding. | Continuous oversight; good for creative/exploratory coding. |
| **CI/CD friendliness** | Same script runs locally or in GitHub Actions/Docker. | IDE helper isn’t present in CI; extra scripting still required. |
| **Error handling** | Loop: generate → `pytest` → commit only on pass; repo never left red. | Developer must notice failures and prompt the assistant again. |
| **Environment locking** | `uv` guarantees a single, reproducible env (`uv.lock`). | Editor may use a different Python; CI env must be set up separately. |
| **Scalability / batch ops** | Can bootstrap or refactor dozens of repos head-lessly. | IDE workflow is limited to one session/repo. |
| **Cognitive load** | Focus on the *plan*, not keystrokes. | Continuous micro-decisions: accept, edit, test, stage. |

#### Complementary usage

1. Draft a high-level **build plan**.  
2. Let the head-less agent grind through boilerplate + CI wiring.  
3. Refine nuanced logic or UI interactively in the IDE copilot PR.