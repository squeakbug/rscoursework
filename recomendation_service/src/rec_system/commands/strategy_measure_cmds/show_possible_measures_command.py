from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.rec_system.recomendation_system import RecomendationSystem


class ShowPossibleMeasuresCommandContructor(ICommandConstructor):
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowPossibleMeasuresCommand()


class ShowPossibleMeasuresCommandResponse(ICommandResponse):
    measure_name_list: list = None

    def __init__(self, measure_name_list: str):
        self.measure_name_list = measure_name_list

    def form_message(self) -> str:
        measure_list_str = "\n".join(self.measure_name_list)
        return f"Возможные рекомендательные меры:\n{measure_list_str}"


class ShowPossibleMeasuresCommand(RecSystemCommandBase):
    def __init__(self) -> None:
        super().__init__()

    def execute(self) -> ICommandResponse:
        measure_name_list = self.executor.get_measures()
        return ShowPossibleMeasuresCommandResponse(measure_name_list)
