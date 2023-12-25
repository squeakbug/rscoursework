from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.rec_system.recomendation_system import RecomendationSystem


class ShowPossibleStrategiesCommandContructor(ICommandConstructor):
    rec_system: RecomendationSystem = None
    
    def __init__(self, rec_system: RecomendationSystem) -> None:
        self.rec_system = rec_system
    
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowPossibleStrategiesCommand(self.rec_system)


class ShowPossibleStrategiesCommandResponse(ICommandResponse):
    strategy_name_list: list = None
    
    def __init__(self, strategy_name_list: str):
        self.strategy_name_list = strategy_name_list

    def form_message(self) -> str:
        return f"Возможные рекомендательные стратегии: {self.strategy_name_list}"


class ShowPossibleStrategiesCommand(RecSystemCommandBase):
    rec_system: RecomendationSystem = None
    
    def __init__(self, rec_system: RecomendationSystem) -> None:
        super().__init__()
        self.rec_system = rec_system

    def execute(self) -> ICommandResponse:
        strategy_name_list =  self.rec_system.get_strategies()
        return ShowPossibleStrategiesCommandResponse(strategy_name_list)
