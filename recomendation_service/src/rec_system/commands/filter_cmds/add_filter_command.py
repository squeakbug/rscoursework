from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class AddFilterCommandContructor(ICommandConstructor):
    def construct(self, cmd_reg_res: CommandRecognizerResult) -> RecSystemCommandBase:
        filter_name = cmd_reg_res.matchings["filter_name"]
        return AddFilterCommand(filter_name=filter_name)


class AddFilterCommandResponse(ICommandResponse):
    def __init__(self) -> None:
        super().__init__()

    def form_message(self) -> str:
        return "Введите значение фильтра"


class AddFilterCommand(RecSystemCommandBase):
    def __init__(self, filter_name: str) -> None:
        super().__init__()
        self.filter_name = filter_name

    def execute(self) -> ICommandResponse:
        response = AddFilterCommandResponse()
        return response
