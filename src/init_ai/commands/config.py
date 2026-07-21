import typer
import shutil

from pathlib import Path
import tomllib

from init_ai.config.paths import get_config_path
from init_ai.config.loader import load_config
from init_ai.config.writer import write_config, set_config
from init_ai.config.default import default_config

app = typer.Typer()


@app.command("init")
def init():
    write_config()
    typer.echo("Configuration initialized")


@app.command("get")
def get():
    typer.echo(load_config())


@app.command("path")
def path():
    typer.echo(get_config_path())

@app.command("set")
def set(
    key: str,
    value: str
):
    # Validate autosave
    if key == "autosave":
        if value.lower() not in ("true", "false"):
            typer.echo("Error: autosave must be true or false")
            raise typer.Exit(code=1)

        value = value.lower() == "true"

    try:
        set_config(key, value)
        typer.echo("Updated")

    except ValueError as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit(code=1)

@app.command("list")
def list_config():

    config = load_config()

    for key, value in config.items():
        typer.echo(f"{key:<10} {value}")

@app.command("doctor")
def doctor():

    path = get_config_path()

    if path.exists():
        typer.echo("✔ Config file")
    else:
        typer.echo("✘ Config file")
        return

    try:
        with open(path, "rb") as file:
            config = tomllib.load(file)

        typer.echo("✔ TOML valid")

    except Exception:
        typer.echo("✘ TOML invalid")
        return

    defaults = default_config()

    if all(key in config for key in defaults):
        typer.echo("✔ Required keys")
    else:
        typer.echo("✘ Missing keys")
        return

    valid = True

    for key, value in defaults.items():
        if not isinstance(config[key], type(value)):
            valid = False

    if valid:
        typer.echo("✔ Types valid")
    else:
        typer.echo("✘ Invalid types")

@app.command("backup")
def backup():

    path = get_config_path()

    shutil.copy(
        path,
        str(path) + ".bak"
    )

    typer.echo("Backup created")


@app.command("reset")
def reset():
    write_config()
    typer.echo("Reset complete")