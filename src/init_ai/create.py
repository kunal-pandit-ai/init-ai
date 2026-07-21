import typer

app = typer.Typer()

@app.command()
def project(name:str):
    print(f"Creating {name}")