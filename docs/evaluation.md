# Evaluation

## Build Plan

|Aspect | Strength
Determinism | Every file path, dep, and commit message is pre-declared.  The agent simply replays the plan → reproducible history with no “it works on my laptop” drift.
Atomic, audited commits | You now possess 11 tightly-scoped Conventional Commits that proved: style ✔︎, lint ✔︎, tests ✔︎ before each write.  No half-done features hiding in one giant “WIP” diff.
Toolchain boot-strap | In <100 mins we went from empty repo → typed package, tests, CI, and a cron-driven GitHub Action, without opening an editor even once.
Fail-fast gates | The workflow caught MyPy mis-matches, missing Actions, etc., during generation rather than reviewers discovering them later.
Scales to many similar repos | Plug a new build_plan.yaml into the agent and it can mint another project, guaranteeing policy compliance (naming, lint rules, CI skeleton) company-wide.

Aspect | Strength
Interactive refactoring | In an IDE, you see type errors and test failures inline, then fix them in seconds; here MyPy stalls meant patch-generate-rerun cycles.
Exploratory design | IDE agents let you sketch a rough module, run partial tests, prototype algorithms, then tidy later.  The build-plan approach forces up-front granularity guesses.
Lower ceremony for micro-changes | Editing a single annotation in the IDE is a ⌘S; with the agent we had to add a whole plan step (id, commit message) just to widen a type hint.
Real-time context | Side-panel agents “see” the whole tree at once—no need to duplicate code blocks in YAML.  Our plan duplicated markdown.py three times before convergence.
Fewer meta-files | IDE flow needs only code + tests; we added watcher headers, plan YAML, agent.py, GitHub-workflow yaml—all extra maintenance surface.

Where today’s experiment excelled
Reproducibility — the same uv run agent.py will build this repo tomorrow or on a fresh machine.

Commit hygiene — you already have a CI-green history; reviewers can scan diff-by-diff.

Where it cost time
Type-hint churn — several loops just to appease MyPy because the plan duplicated stale code.

Action name typo — a small mistake required multiple pushes because YAML lives in two files and the agent doesn’t lint workflows.

A pragmatic hybrid
Use the build-plan agent for project scaffolding & policy-critical repos.
Let it generate the skeleton, pre-commit hooks, CI, base tests.

Switch to IDE-agentic iteration once the code exists.
Let Cursor/Copilot handle tight feedback on types and runtime behaviour; commit via normal Git when a logical chunk stabilises.

This keeps deterministic bootstrap and audit-ready history without slowing day-to-day evolution.