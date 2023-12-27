from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.rec_system.recomendation_system import RecomendationSystem


class ShowPossibleStrategiesCommandContructor(ICommandConstructor):
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowPossibleStrategiesCommand()


class ShowPossibleStrategiesCommandResponse(ICommandResponse):
    strategy_name_list: list = None

    def __init__(self, strategy_name_list: str):
        self.strategy_name_list = strategy_name_list

    def form_message(self) -> str:
        strategy_name_list = "\n".join(self.strategy_name_list)
        return f"Возможные рекомендательные стратегии:\n{strategy_name_list}"


class ShowPossibleStrategiesCommand(RecSystemCommandBase):
    def execute(self) -> ICommandResponse:
        strategy_name_list = self.executor.get_strategies()
        return ShowPossibleStrategiesCommandResponse(strategy_name_list)
