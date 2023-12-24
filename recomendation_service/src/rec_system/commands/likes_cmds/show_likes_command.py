from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class ShowLikesCommandContructor(ICommandConstructor):
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowLikesCommand()


class ShowLikesCommandResponse(ICommandResponse):
    likes = []

    def __init__(self, likes: list) -> None:
        super().__init__()
        self.likes = likes

    def form_message(self) -> str:
        likes_str = "\n".join(self.likes)
        response = f"Вам нравятся следующие картины:\n" f"{likes_str}"
        return response


class ShowLikesCommand(RecSystemCommandBase):
    def execute(self) -> ICommandResponse:
        likes = self.user.likes
        return ShowLikesCommandResponse(likes)
