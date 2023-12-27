from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.pirtures_repo import PicturesRepositoryList


class ShowDislikesCommandContructor(ICommandConstructor):
    picture_repo: PicturesRepositoryList = None
    
    def __init__(self, picture_repo: PicturesRepositoryList) -> None:
        super().__init__()
        self.picture_repo = picture_repo
    
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowDislikesCommand(self.picture_repo)


class ShowDislikesCommandResponse(ICommandResponse):
    dislikes = []

    def __init__(self, dislikes: list) -> None:
        super().__init__()
        self.dislikes = dislikes

    def form_message(self) -> str:
        response = ""
        if len(self.dislikes) == 0:
            response = "Ваш черный список картин пуст"
        else:
            dislikes_str = "\n".join([f"{e}: {pic.name}" for e, pic in enumerate(self.dislikes)])
            response = f"Вы не можете терпеть следующие картины:\n" f"{dislikes_str}"
        return response


class ShowDislikesCommand(RecSystemCommandBase):
    picture_repo: PicturesRepositoryList = None
    
    def __init__(self, picture_repo: PicturesRepositoryList) -> None:
        super().__init__()
        self.picture_repo = picture_repo
    
    def execute(self) -> ICommandResponse:
        dislikes = [self.picture_repo.get_picture_by_id(id) for id in self.user.dislikes]
        return ShowDislikesCommandResponse(dislikes)
