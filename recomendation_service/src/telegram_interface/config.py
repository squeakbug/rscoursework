import os

from dotenv import dotenv_values


def make_config():
    config = dotenv_values(".env")

    if "TOKEN" not in config:
        config["TOKEN"] = os.getenv("TOKEN")

    return config
