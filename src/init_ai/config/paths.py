from pathlib import Path


def get_config_path() -> Path:
    config_dir = Path.home() / ".config" / "init-ai"

    config_dir.mkdir(
        parents=True,
        exist_ok=True
    )

    return config_dir / "config.toml"