import tomli_w

from .paths import get_config_path
from .default import default_config
from .loader import load_config


def write_config(config=None):

    if config is None:
        config = default_config()

    path = get_config_path()

    with open(path, "wb") as file:
        tomli_w.dump(config, file)


def set_config(key, value):
    defaults = default_config()

    # Check if key exists
    if key not in defaults:
        raise ValueError("Unknown configuration key")

    config = load_config()
    config[key] = value

    write_config(config)