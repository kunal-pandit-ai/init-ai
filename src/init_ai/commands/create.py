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
        # ✅ create root first
        root.mkdir()

        pkg_name = name.replace("-", "_")
        pkg_path = root / "src" / pkg_name

        # ✅ create folders (FIXED)
        pkg_path.mkdir(parents=True, exist_ok=True)
        (pkg_path / "__init__.py").touch()
        (root / "tests").mkdir(exist_ok=True)

        # ✅ create files
        (root / "README.md").write_text(f"# {name}\n")
        (root / "LICENSE").write_text("MIT License\n")

        (root / ".gitignore").write_text(
            ".venv\n__pycache__/\n*.pyc\n.env\n"
        )

        (root / "pyproject.toml").write_text(f"""[project]
name = "{name}"
version = "0.1.0"
description = ""
requires-python = ">=3.10"
""")

        # ✅ create virtual environment
        subprocess.run([sys.executable, "-m", "venv", ".venv"], cwd=root)

        # ✅ initialize git properly (FIXED)
        subprocess.run(["git", "branch", "-m", "main"], cwd=root, check=True)
        subprocess.run(["git", "add", "."], cwd=root)
        subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=root)

        print(f"✅ Project '{name}' created successfully")

    except PermissionError:
        print("❌ Permission denied")