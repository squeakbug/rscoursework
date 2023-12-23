from src.nlp.icommand_dispatcher import ICommandDispatcher
from src.nlp.preprocessing import preprocessing
from src.domain.rec_system_command_base import RecSystemCommandBase
from .prolog_server_interface import PrologServer


class CommandDispatcherProlog(ICommandDispatcher):
    prolog_server = None

    def __init__(self, config):
        self.prolog_server = PrologServer(config)

    def registrate_cmd(self, rule_name: str, cmd_contructor):
        self.prolog_server.register_command(rule_name, cmd_contructor)

    def get_most_accurate_cmd(self, user_input: str) -> RecSystemCommandBase:
        normalized_user_input = preprocessing(user_input)
        tokenized_norm_user_input = normalized_user_input.split(" ")
        return self.prolog_server.recognize_command(tokenized_norm_user_input)
