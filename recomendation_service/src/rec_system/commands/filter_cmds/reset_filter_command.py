from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.rec_system.filter import Filter


class ResetFilterCommandContructor(ICommandConstructor):
    def construct(self, cmd_reg_res: CommandRecognizerResult) -> RecSystemCommandBase:
        filter_name_list = cmd_reg_res.matchings["filter_name"]
        filter_name = " ".join(filter_name_list)
        return ResetFilterCommand(filter_name=filter_name)


class ResetFilterCommandResponse(ICommandResponse):
    filter_name = None

    def __init__(self, filter_name: str) -> None:
        super().__init__()
        self.filter_name = filter_name

    def form_message(self) -> str:
        return f"Значение фильтра \"{self.filter_name}\" было сброшено"


class ResetFilterCommand(RecSystemCommandBase):
    filter_name = None

    def __init__(self, filter_name: str) -> None:
        super().__init__()
        self.filter_name = filter_name

    def execute(self) -> ICommandResponse:
        self.user.filter = Filter()
        return ResetFilterCommandResponse(filter_name=self.filter_name)
