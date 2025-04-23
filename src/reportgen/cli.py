import typer, sys
from .pipeline import run
app = typer.Typer()
@app.command()
def weekly():
    run()
if __name__ == "__main__":
    sys.exit(app())
