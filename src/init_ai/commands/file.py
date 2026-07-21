from pathlib import Path

def touch(name: str):
    path = Path(name)
    path.touch(exist_ok=True)

    if path.exists():
        print(f"✔ file '{name}' is ready")