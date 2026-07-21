from pathlib import Path

def mv(src: str, dest: str):
    try:
        path = Path(src)

        if not path.exists():
            print(f"❌ File not found: {src}")
            return

        path.rename(dest)
        print(f"✅ Renamed {src} → {dest}")

    except PermissionError:
        print("❌ Permission denied")