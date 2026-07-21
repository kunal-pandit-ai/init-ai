from pathlib import Path

def check(base: Path, name: str):
    path = base / name

    if path.exists():
        print(f"✔ {name}")
    else:
        print(f"✘ {name}")


def doctor(directory: str = "."):
    base = Path(directory)

    if not base.exists():
        print(f"❌ Directory not found: {directory}")
        return

    print(f"\n🔍 Checking project: {base.resolve()}\n")

    check(base, "README.md")
    check(base, "LICENSE")
    check(base, "pyproject.toml")
    check(base, "tests")
    check(base, ".git")
    check(base, ".venv")