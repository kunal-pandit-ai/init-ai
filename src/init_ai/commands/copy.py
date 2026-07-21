import shutil
import typer
from pathlib import Path

def copy(src: str, dest: str):
    try:
        if not Path(src).exists():
            print(f"❌ Source not found: {src}")
            return

        shutil.copy(src, dest)
        print(f"✅ Copied {src} → {dest}")
    except PermissionError:
        print("❌ Permission denied")