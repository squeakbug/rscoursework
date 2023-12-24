"""

"""
from dataclasses import dataclass
from .rec_system_command_base import RecSystemCommandBase


@dataclass
class CommandRecognizerResult:
    rule_name: str
    matchings: list


class ICommandConstructor:
    def construct(self, recognize_result: CommandRecognizerResult) -> RecSystemCommandBase:
        pass
