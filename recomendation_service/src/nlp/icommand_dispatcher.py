# Автор не работал с https://github.com/mrocklin/multipledispatch, но он это знает
from src.domain.rec_system_command_base import RecSystemCommandBase


class ICommandDispatcher:
    def registrate_cmd(self, rule_name: str, cmd: RecSystemCommandBase):
        pass

    def get_most_accurate_cmd(self, user_input: str) -> RecSystemCommandBase:
        pass
