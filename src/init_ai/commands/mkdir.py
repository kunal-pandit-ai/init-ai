from pathlib import Path

def mkdir(name: str):
    path = Path(name)
    path.mkdir(exist_ok=True)

    if path.exists():
        print(f"✔ Directory '{name}' is ready")