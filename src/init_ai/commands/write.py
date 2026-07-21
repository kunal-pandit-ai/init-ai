from pathlib import Path
import typer

def write(filename: str, text: str):
    try:
        path = Path(filename)

        if path.exists():
            print(f"⚠ File already exists: {filename}")
            return

        path.write_text(text)
        print(f"✅ Written to {filename}")

    except PermissionError:
        print(f"❌ Permission denied: {filename}")