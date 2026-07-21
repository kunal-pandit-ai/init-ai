import tomllib
from pathlib import Path

def author():
    project_path = Path(__file__).resolve().parents[3] / "pyproject.toml"

    with open(project_path, "rb") as f:
        data = tomllib.load(f)

    print(f"Creayed by {data["project"]["creator"]}")

