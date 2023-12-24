from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class HelloCommandContructor(ICommandConstructor):
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return HelloCommand()


class HelloCommandResponse(ICommandResponse):
    def __init__(self) -> None:
        super().__init__()

    def form_message(self) -> str:
        return "Привет, человек"


class HelloCommand(RecSystemCommandBase):
    def __init__(self) -> None:
        super().__init__()

    def get_measure(self, _: str):
        return 1

    def execute(self) -> ICommandResponse:
        return HelloCommandResponse()
