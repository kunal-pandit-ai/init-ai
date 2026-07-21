from pathlib import Path

def ls():
    for item in Path.cwd().iterdir():
        if item.is_dir():
            print(f"[DIR] {item.name}")
        else:
            print(f"[FILE] {item.name}")
