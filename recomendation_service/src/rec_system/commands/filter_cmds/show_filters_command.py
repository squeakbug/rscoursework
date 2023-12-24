from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.rec_system.filter import Filter, filter_to_string


class ShowFiltersCommandContructor(ICommandConstructor):
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowFiltersCommand()


class ShowFiltersCommandResponse(ICommandResponse):
    filter = None

    def __init__(self, filter: Filter):
        self.filter = filter

    def form_message(self) -> str:
        filter_str = filter_to_string(self.filter)
        return f"Текущие значения фильтров: {filter_str}\n"


class ShowFiltersCommand(RecSystemCommandBase):
    def execute(self) -> ICommandResponse:
        filter = self.user.filter
        response = ShowFiltersCommandResponse(filter=filter)
        return response
