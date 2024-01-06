import os

from dotenv import dotenv_values


def make_config():
    config = dotenv_values(".env")

    token = os.getenv("TOKEN")
    if token != None:
        config["TOKEN"] = token

    prolog_server_address = os.getenv("PROLOG_SERVER_ADDRESS")
    if prolog_server_address != None:
        config["PROLOG_SERVER_ADDRESS"] = prolog_server_address

    data_path_root = os.getenv("DATA_PATH_ROOT")
    if data_path_root != None:
        config["DATA_PATH_ROOT"] = data_path_root

    return config
