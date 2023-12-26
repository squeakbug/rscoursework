from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.rec_system.recomendation_system import RecomendationSystem


class ShowPossibleMeasuresCommandContructor(ICommandConstructor):
    rec_system: RecomendationSystem = None

    def __init__(self, rec_system: RecomendationSystem) -> None:
        self.rec_system = rec_system

    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowPossibleMeasuresCommand(self.rec_system)


class ShowPossibleMeasuresCommandResponse(ICommandResponse):
    measure_name_list: list = None

    def __init__(self, measure_name_list: str):
        self.measure_name_list = measure_name_list

    def form_message(self) -> str:
        return f"Возможные рекомендательные стратегии: {self.measure_name_list}"


class ShowPossibleMeasuresCommand(RecSystemCommandBase):
    rec_system: RecomendationSystem = None

    def __init__(self, rec_system: RecomendationSystem) -> None:
        super().__init__()
        self.rec_system = rec_system

    def execute(self) -> ICommandResponse:
        measure_name_list = self.rec_system.get_measures()
        return ShowPossibleMeasuresCommandResponse(measure_name_list)
