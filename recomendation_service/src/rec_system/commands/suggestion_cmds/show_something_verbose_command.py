from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy, RecomendationSystem
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.user_repo import UserRepositoryList
from src.repositories.pirtures_repo import PicturesRepositoryList
from src.rec_system.commands.other_cmds.not_found_command import NotFoundCommand
from src.domain.picture import Picture

class ShowSomethingVerboseCommandContructor(ICommandConstructor):
    user_repo: UserRepositoryList
    picture_repo: PicturesRepositoryList

    def __init__(self, user_repo, picture_repo) -> None:
        super().__init__()
        self.user_repo = user_repo
        self.picture_repo = picture_repo

    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowSomethingVerboseCommand(self.user_repo, self.picture_repo)


class ShowSomethingVerboseCommandResponse(ICommandResponse):
    suggestion_list = None

    def __init__(self, suggestion_list: list[Picture]):
        self.suggestion_list = suggestion_list

    def form_message(self) -> str:
        suggestions_str = "\n".join([f"#{e}: {pic.name}, price = {pic.sale_price}" for e, pic in enumerate(self.suggestion_list)])
        response = f"Рекомендую вам посмотреть на след. экспонаты:\n{suggestions_str}"
        return response


class ShowSomethingVerboseCommand(RecSystemCommandBase):
    user_repo: UserRepositoryList
    picture_repo: PicturesRepositoryList

    def __init__(self, user_repo, picture_repo) -> None:
        super().__init__()
        self.user_repo = user_repo
        self.picture_repo = picture_repo

    def execute(self) -> ICommandResponse:
        rec_system = self.executor
        items = rec_system.give_recomendation(self.user, limit=10)
        response = ShowSomethingVerboseCommandResponse(suggestion_list=items)
        return response
