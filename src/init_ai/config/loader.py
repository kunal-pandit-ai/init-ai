import os
import tomllib

from .paths import get_config_path


def load_config():

    with open(get_config_path(), "rb") as file:
        config = tomllib.load(file)

    editor = os.getenv("INIT_AI_EDITOR")

    if editor:
        config["editor"] = editor

    return config