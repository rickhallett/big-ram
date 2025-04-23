# === WATCHER HEADER START ===
# File: agent.py
# Managed by file watcher
# === WATCHER HEADER END ===
import subprocess, yaml, textwrap, sys, pathlib


def sh(cmd: str, **kw) -> None:
    """Run *cmd* in the shell or explode immediately."""
    print(f"$ {cmd}")
    subprocess.run(cmd, shell=True, check=True, text=True, **kw)


plan = yaml.safe_load(pathlib.Path("build_plan.yaml").read_text())["steps"]

for step in plan:
    # 1 — install/update deps  -------------------------------------------------
    if "deps" in step:
        sh(f"uv pip install {' '.join(step['deps'])}")
        sh("uv pip sync requirements.txt")  # keep env deterministic

    # 2 — materialise files  ---------------------------------------------------
    for file, content in (step.get("files") or {}).items():
        p = pathlib.Path(file)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(textwrap.dedent(content))
    for file, content in (step.get("tests") or {}).items():
        p = pathlib.Path(file)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(textwrap.dedent(content))

    # ensure editable install so tests can import `reportgen`
    if pathlib.Path("pyproject.toml").exists():
        sh("uv pip install -e .")

    # 3 — style / lint / type gate  -------------------------------------------
    sh("black --quiet src tests agent.py")
    sh("isort --quiet src tests")

    # Ruff: auto-fix simple issues, then require clean slate
    sh("ruff check --fix src tests")
    sh("ruff check src tests")

    # skip unknown stubs *and* silence "import-untyped" warnings
    sh("mypy src --ignore-missing-imports --disable-error-code import-untyped")

    sh("git add -A")  # stage any fixes

    # 4 — tests  ----------------------------------------------------------------
    while True:
        res = subprocess.run("pytest -q", shell=True)
        if res.returncode in (0, 5):  # 0 = pass, 5 = no tests
            break
        print(f"❌ tests failed in step {step['id']} – aborting")
        sys.exit(1)

    # 5 — conventional commit  --------------------------------------------------
    try:
        sh(f"git commit -m '{step['commit']}'")
    except subprocess.CalledProcessError:
        print("ℹ️ nothing to commit for this step")

print("✅ build plan complete")
