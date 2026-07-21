from pathlib import Path

def tree():
    base = Path(".")

    print(base.resolve().name)

    for path in sorted(base.rglob("*")):
        depth = len(path.relative_to(base).parts)
        indent = "│   " * (depth - 1) + "├── "
        print(f"{indent}{path.name}")