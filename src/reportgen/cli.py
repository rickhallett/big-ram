import sys

import typer

from .pipeline import run

app = typer.Typer()


@app.command()
def weekly() -> None:
    """Entry-point used by GitHub Actions."""
    run()


if __name__ == "__main__":
    sys.exit(app())
