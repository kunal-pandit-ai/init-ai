from pathlib import Path
import typer

def cat(file: str):
    try:
        content = Path(file).read_text()
        print(content)
    except FileNotFoundError:
        print(f"❌ File not found: {file}")
    except PermissionError:
        print(f"❌ Permission denied: {file}")