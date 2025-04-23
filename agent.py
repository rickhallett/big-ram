import subprocess, yaml, textwrap, os, sys, json, pathlib


def sh(cmd, **kw):
    print(f"$ {cmd}")
    subprocess.run(cmd, shell=True, check=True, text=True, **kw)


plan = yaml.safe_load(pathlib.Path("build_plan.yaml").read_text())["steps"]

for step in plan:
    # 1 . install deps with uv
    if "deps" in step:
        sh(f"uv pip install {' '.join(step['deps'])}")
        sh("uv pip sync")  # lock update

    # 2 . write files
    for file, content in (step.get("files") or {}).items():
        path = pathlib.Path(file)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content))
    for test, content in (step.get("tests") or {}).items():
        path = pathlib.Path(test)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(textwrap.dedent(content))

    # 3 . run tests until they pass
    while True:
        try:
            sh("pytest -q")
            break
        except subprocess.CalledProcessError:
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
