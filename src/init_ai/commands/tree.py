from pathlib import Path

EXCLUDE_DIRS = {
    "__pycache__",
    ".git",
    ".mypy_cache",
    ".pytest_cache",
}

EXCLUDE_SUFFIXES = {
    ".pyc",
    ".pyo",
}


def tree():
    base = Path(".")

    print(base.resolve().name)

    for path in sorted(base.rglob("*")):
        # ❌ skip unwanted directories anywhere in path
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue

        # ❌ skip unwanted file types
        if path.suffix in EXCLUDE_SUFFIXES:
            continue

        depth = len(path.relative_to(base).parts)
        indent = "│   " * (depth - 1) + "├── "

        print(f"{indent}{path.name}")