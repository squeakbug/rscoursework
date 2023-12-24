"""

"""
import requests

from src.domain.rec_system_command_base import RecSystemCommandBase
from recomendation_service.src.rec_system.commands.other_cmds.hello_command import (
    CommandRecognizerResult,
)


class PrologServer:
    cmd_contructors = {}

    def __init__(self, config) -> None:
        self.prolog_server_address = config["PROLOG_SERVER_ADDRESS"]

    def register_command(self, rule_name: str, cmd_contructor):
        self.cmd_contructors[rule_name] = cmd_contructor

    def recognize_command(self, tokenized_norm_user_input: [str]) -> RecSystemCommandBase:
        url = f"{self.prolog_server_address}/api/v1/rule_recognizer"

        json = {"tokens": tokenized_norm_user_input}

        resp = requests.post(url=url, json=json)
        data = resp.json()
        print(data)
        rule_name = data["rule_name"]
        matchings = data["matchings"]
        result = CommandRecognizerResult(rule_name=rule_name, matchings=matchings)
        if rule_name not in self.cmd_contructors:
            return None
        return self.cmd_contructors[rule_name].construct(result)
