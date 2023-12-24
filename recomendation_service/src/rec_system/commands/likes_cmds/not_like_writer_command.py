from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class NotLikeWriterCommandContructor(ICommandConstructor):
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return NotLikeWriterCommand()


class NotLikeWriterCommandResponse(ICommandResponse):
    def __init__(self):
        pass

    def form_message(self) -> str:
        return "Сессия сброшена"


class NotLikeWriterCommand(RecSystemCommandBase):
    def execute(self) -> ICommandResponse:
        return NotLikeWriterCommandResponse()