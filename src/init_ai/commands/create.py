from pathlib import Path
import subprocess
import sys


def create(type: str, name: str):
    if type != "project":
        print("❌ Only 'project' supported")
        return

    root = Path(name)

    if root.exists():
        print(f"❌ Directory already exists: {name}")
        return

    try:
        # create folders
        (root / "src" / name.replace("-", "_")).mkdir()
        (root / "src" / name.replace("-", "_") / "__init__.py").touch()
        (root / "tests").mkdir()

        # create files
        (root / "README.md").write_text(f"# {name}\n")
        (root / "LICENSE").write_text("MIT License\n")

        (root / ".gitignore").write_text(
            ".venv\n__pycache__/\n*.pyc\n.env\n"
        )

        (root / "pyproject.toml").write_text(f"""
[project]
name = "{name}"
version = "0.1.0"
description = ""
requires-python = ">=3.10"
""")

        # 🔥 create virtual environment properly
        subprocess.run([sys.executable, "-m", "venv", ".venv"], cwd=root)

        # 🔥 initialize git properly
        subprocess.run(["git", "add", "."], cwd=root)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=root)

        print(f"✅ Project '{name}' created successfully")

    except PermissionError:
        print("❌ Permission denied")