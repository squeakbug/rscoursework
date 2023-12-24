from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class ShowDislikesCommandContructor(ICommandConstructor):
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowDislikesCommand()


class ShowDislikesCommandResponse(ICommandResponse):
    dislikes = []

    def __init__(self, dislikes: list) -> None:
        super().__init__()
        self.dislikes = dislikes

    def form_message(self) -> str:
        dislikes_str = "\n".join(self.dislikes)
        response = f"Вы не можете терпеть следующие картины:\n" f"{dislikes_str}"
        return response


class ShowDislikesCommand(RecSystemCommandBase):
    def execute(self) -> ICommandResponse:
        dislikes = self.user.dislikes
        return ShowDislikesCommandResponse(dislikes)
