from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class ShowStrategyCommandContructor(ICommandConstructor):
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowStrategyCommand()


class ShowStrategyCommandResponse(ICommandResponse):
    def __init__(self, strategy_name: str):
        self.strategy_name = strategy_name

    def form_message(self) -> str:
        return f"Текущая стратегия рекомендаций - {self.strategy_name}"


class ShowStrategyCommand(RecSystemCommandBase):
    def __init__(self) -> None:
        super().__init__()

    def execute(self) -> ICommandResponse:
        current_strategy_name = self.user.strategy_name
        response = ShowStrategyCommandResponse(strategy_name=current_strategy_name)
        return response
