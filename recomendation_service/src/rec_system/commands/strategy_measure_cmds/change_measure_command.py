from src.domain.rec_system_command_base import RecSystemCommandBase
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.user_repo import UserRepositoryList


class ChangeMeasureCommandContructor(ICommandConstructor):
    user_repo: UserRepositoryList = None

    def __init__(self, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.user_repo = user_repo

    def construct(self, cmd_reg_res: CommandRecognizerResult) -> RecSystemCommandBase:
        measure_name = cmd_reg_res.matchings["measure_name"]
        return ChangeMeasureCommand(measure_name, self.user_repo)


class ChangeMeasureCommandResponse(ICommandResponse):
    measure_func_name: str = None

    def __init__(self, measure_func_name: str):
        self.measure_func_name = measure_func_name

    def form_message(self) -> str:
        return f"Установлена {self.measure_func_name} функция"


class ChangeMeasureCommand(RecSystemCommandBase):
    measure_func_name: str = None
    user_repo: UserRepositoryList = None

    def __init__(self, measure_func_name: str, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.measure_func_name = measure_func_name
        self.user_repo = user_repo

    def execute(self) -> ICommandResponse:
        self.user.measure_func_name = self.measure_func_name
        self.user_repo.update_user(self.user.id, self.user)
        return ChangeMeasureCommandResponse(self.measure_func_name)
