# === WATCHER HEADER START ===
# File: agent.py
# Managed by file watcher
# === WATCHER HEADER END ===
import subprocess, yaml, textwrap, os, sys, json, pathlib


def sh(cmd, **kw):
    print(f"$ {cmd}")
    subprocess.run(cmd, shell=True, check=True, text=True, **kw)


plan = yaml.safe_load(pathlib.Path("build_plan.yaml").read_text())["steps"]

for step in plan:
    # 1 . install deps with uv
    if "deps" in step:
        sh(f"uv pip install {' '.join(step['deps'])}")
        sh("uv pip sync requirements.txt")  # lock update

    # 2 . write files
    for file, content in (step.get("files") or {}).items():
        path = pathlib.Path(file)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content))
    for test, content in (step.get("tests") or {}).items():
        path = pathlib.Path(test)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content))

    # --- NEW: make package importable for tests --------------------------
    # If the project has a pyproject.toml, install/refresh it in editable mode
    if pathlib.Path("pyproject.toml").exists():
        sh("uv pip install -e .")

    # 3 . run tests until they pass
    while True:
        res = subprocess.run("pytest -q", shell=True)
        if res.returncode in (0, 5):  # 0 = all tests passed, 5 = none collected
            break
        else:
            print(f"❌ tests failed in step {step['id']} – aborting")
            sys.exit(1)

    # 4 . conventional commit
    msg = step["commit"]
    sh("git add -A")
    try:
        sh(f"git commit -m '{msg}'")
    except subprocess.CalledProcessError:
        print("ℹ️ nothing to commit (files unchanged)")

print("✅ build plan complete")
