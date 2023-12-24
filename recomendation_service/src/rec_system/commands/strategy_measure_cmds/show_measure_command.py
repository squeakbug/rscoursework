from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class ShowMeasureCommandContructor(ICommandConstructor):
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowMeasureCommand()


class ShowMeasureCommandResponse(ICommandResponse):
    def __init__(self, measure_name: str):
        self.measure_name = measure_name

    def form_message(self) -> str:
        return f"Текущая мера - {self.measure_name}"


class ShowMeasureCommand(RecSystemCommandBase):
    def __init__(self) -> None:
        super().__init__()

    def execute(self) -> ICommandResponse:
        current_measure_name = self.executor.get_current_measure()
        response = ShowMeasureCommandResponse(measure_name=current_measure_name)
        return response
