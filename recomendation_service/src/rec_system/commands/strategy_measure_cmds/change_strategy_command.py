from src.domain.rec_system_command_base import RecSystemCommandBase
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.user_repo import UserRepositoryList


class ChangeStrategyCommandContructor(ICommandConstructor):
    user_repo: UserRepositoryList = None

    def __init__(self, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.user_repo = user_repo

    def construct(self, matchings: CommandRecognizerResult) -> RecSystemCommandBase:
        strategy_name = matchings["strategy_name"]
        return ChangeStrategyCommand(strategy_name, self.user_repo)


class ChangeStrategyCommandResponse(ICommandResponse):
    strategy_name: str = None

    def __init__(self, strategy_name: str):
        self.strategy_name = strategy_name

    def form_message(self) -> str:
        return f"Установлена {self.strategy_name} стратегия рекомендации"


class ChangeStrategyCommand(RecSystemCommandBase):
    strategy_name: str = None
    user_repo: UserRepositoryList = None

    def __init__(self, strategy_name: str, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.strategy_name = strategy_name
        self.user_repo = user_repo

    def execute(self) -> ICommandResponse:
        self.user.strategy_name = self.strategy_name
        self.user_repo.update_user(self.user.id, self.user)
        return ChangeStrategyCommandResponse(self.strategy_name)
