from src.domain.rec_system_command_base import RecSystemCommandBase
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.user_repo import UserRepositoryList
from src.rec_system.filter import Filter


class ResetHistoryCommandContructor(ICommandConstructor):
    user_repo: UserRepositoryList = None

    def __init__(self, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.user_repo = user_repo

    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ResetHistoryCommand(self.user_repo)


class ResetHistoryCommandResponse(ICommandResponse):
    def __init__(self):
        pass

    def form_message(self) -> str:
        return "История сброшена"


class ResetHistoryCommand(RecSystemCommandBase):
    user_repo: UserRepositoryList = None

    def __init__(self, user_repo: UserRepositoryList) -> None:
        super().__init__()
        self.user_repo = user_repo

    def execute(self) -> ICommandResponse:
        self.user.filter = Filter()
        self.user.dislikes = []
        self.user.likes = []
        self.user_repo.update_user(self.user.id, self.user)
        return ResetHistoryCommandResponse()
