from pathlib import Path

def rm(name:str):
    path = Path(name)
    path.unlink()
    print(f"Delete file {name}")