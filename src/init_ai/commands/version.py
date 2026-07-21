import tomllib  #👉 TOML file read karne ka built-in tool
from pathlib import Path


def version():
    project_path = Path(__file__).resolve().parents[3] / "pyproject.toml"

    with open(project_path, "rb") as f:
        data = tomllib.load(f)

    print(data["project"]['version'])