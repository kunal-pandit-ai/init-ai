import tomllib
from pathlib import Path

def who():
    project_path = Path(__file__).resolve().parents[3] / "pyproject.toml"

    with open (project_path, "rb") as f:
        data = tomllib.load(f)

    print(data["project"]["name"])