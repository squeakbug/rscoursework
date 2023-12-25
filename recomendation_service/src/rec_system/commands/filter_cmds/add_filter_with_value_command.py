from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.user_repo import UserRepositoryList


class AddFilterWithValueCommandContructor(ICommandConstructor):
    user_repo: UserRepositoryList = None

    def __init__(self, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.user_repo = user_repo

    def construct(self, cmd_reg_res: CommandRecognizerResult) -> RecSystemCommandBase:
        filter_name = cmd_reg_res.matchings["filter_name"]
        filter_value = cmd_reg_res.matchings["filter_value"]
        return AddFilterWithValueCommand(filter_name, filter_value, self.user_repo)


class AddFilterWithValueCommandResponse(ICommandResponse):
    filter_name = None
    filter_value = None

    def __init__(self, filter_name, filter_value) -> None:
        super().__init__()
        self.filter_name = filter_name
        self.filter_value = filter_value

    def form_message(self) -> str:
        return f"Значение для фильтра {self.filter_name} установлено на {self.filter_value}"


class AddFilterWithValueCommand(RecSystemCommandBase):
    filter_name: str = None
    filter_value = None
    user_repo: UserRepositoryList = None

    def __init__(self, filter_name: str, filter_value, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.filter_name = filter_name
        self.filter_value = filter_value
        self.user_repo = user_repo

    def execute(self) -> ICommandResponse:
        filter = self.user.filter
        filter[self.filter_name] = self.filter_value
        self.user.filter = filter
        self.user_repo.update_user(self.user.id, self.user)
        return AddFilterWithValueCommandResponse(self.filter_name, self.filter_value)
