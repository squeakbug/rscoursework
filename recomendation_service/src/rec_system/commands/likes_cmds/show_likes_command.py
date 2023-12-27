from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.pirtures_repo import PicturesRepositoryList


class ShowLikesCommandContructor(ICommandConstructor):
    picture_repo: PicturesRepositoryList = None
    
    def __init__(self, picture_repo: PicturesRepositoryList) -> None:
        super().__init__()
        self.picture_repo = picture_repo
    
    def construct(self, _: CommandRecognizerResult) -> RecSystemCommandBase:
        return ShowLikesCommand(self.picture_repo)


class ShowLikesCommandResponse(ICommandResponse):
    likes = []

    def __init__(self, likes: list) -> None:
        super().__init__()
        self.likes = likes

    def form_message(self) -> str:
        response = ""
        if len(self.likes) == 0:
            response = "Ваш список понравившихся картин пуст"
        else:
            likes_str = "\n".join([f"{pic.id}: {pic.name}" for e, pic in enumerate(self.likes)])
            response = f"Вам нравятся следующие картины:\n" f"{likes_str}"
        return response


class ShowLikesCommand(RecSystemCommandBase):
    picture_repo: PicturesRepositoryList = None
    
    def __init__(self, picture_repo: PicturesRepositoryList) -> None:
        super().__init__()
        self.picture_repo = picture_repo
    
    def execute(self) -> ICommandResponse:
        likes = [self.picture_repo.get_picture_by_id(id) for id in self.user.likes]
        return ShowLikesCommandResponse(likes)
