import logging

from src.domain.rec_system_command_base import RecSystemCommandBase
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.user_repo import UserRepositoryList
from src.nlp.edit_distance_tools import replace_strategy_name, get_most_similar_strategy_name


class ChangeStrategyCommandContructor(ICommandConstructor):
    user_repo: UserRepositoryList = None

    def __init__(self, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.user_repo = user_repo

    def construct(self, cmd_reg_res: CommandRecognizerResult) -> RecSystemCommandBase:
        strategy_name = cmd_reg_res.matchings["strategy_name"]
        return ChangeStrategyCommand(strategy_name, self.user_repo)


class ChangeStrategyCommandResponse(ICommandResponse):
    strategy_name: str = None

    def __init__(self, strategy_name: str):
        self.strategy_name = strategy_name

    def form_message(self) -> str:
        return f"Установлена \"{self.strategy_name}\" стратегия рекомендации"


class ChangeStrategyCommand(RecSystemCommandBase):
    strategy_name: str = None
    user_repo: UserRepositoryList = None

    def __init__(self, strategy_name: str, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.strategy_name = strategy_name
        self.user_repo = user_repo

    def execute(self) -> ICommandResponse:
        domain_strategy_func_name = replace_strategy_name(self.strategy_name)
        corrected_strategy_func_name = get_most_similar_strategy_name(self.strategy_name)
        self.user.strategy_name = domain_strategy_func_name
        self.user_repo.update_user(self.user.id, self.user)
        return ChangeStrategyCommandResponse(corrected_strategy_func_name)
