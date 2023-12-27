from src.domain.rec_system_command_base import RecSystemCommandBase
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.user_repo import UserRepositoryList
from src.nlp.edit_distance_tools import replace_measure_function_name, get_most_similar_measure_function_name


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
        return f"Установлена \"{self.measure_func_name}\" функция меры"


class ChangeMeasureCommand(RecSystemCommandBase):
    measure_func_name: str = None
    user_repo: UserRepositoryList = None

    def __init__(self, measure_func_name: str, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.measure_func_name = measure_func_name
        self.user_repo = user_repo

    def execute(self) -> ICommandResponse:
        domain_measure_func_name = replace_measure_function_name(self.measure_func_name)
        corrected_measure_func_name = get_most_similar_measure_function_name(self.measure_func_name)
        self.user.measure_func_name = domain_measure_func_name
        self.user_repo.update_user(self.user.id, self.user)
        return ChangeMeasureCommandResponse(corrected_measure_func_name)
