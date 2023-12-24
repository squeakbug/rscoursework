from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class SosCommandContructor(ICommandConstructor):
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return SosCommand()


class SosCommandResponse(ICommandResponse):
    def __init__(self) -> None:
        super().__init__()

    def form_message(self) -> str:
        return "Вызываю полицию (и скорую)!"


class SosCommand(RecSystemCommandBase):
    def __init__(self) -> None:
        super().__init__()

    def get_measure(self, _: str):
        return 1

    def execute(self) -> ICommandResponse:
        return SosCommandResponse()
