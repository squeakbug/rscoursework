from src.domain.rec_system_command_base import RecSystemCommandBase
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.user_repo import UserRepositoryList


class ResetSessionCommandContructor(ICommandConstructor):
    user_repo: UserRepositoryList = None

    def __init__(self, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.user_repo = user_repo

    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ResetSessionCommand(self.user_repo)


class ResetSessionCommandResponse(ICommandResponse):
    def __init__(self):
        pass

    def form_message(self) -> str:
        return "Сессия сброшена"


class ResetSessionCommand(RecSystemCommandBase):
    user_repo: UserRepositoryList = None

    def __init__(self, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.user_repo = user_repo

    def execute(self) -> ICommandResponse:
        self.user_repo.update_user(self.user.id, self.user)
        return ResetSessionCommandResponse()
