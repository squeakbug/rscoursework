from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.user_repo import UserRepositoryList
from src.repositories.pirtures_repo import PicturesRepositoryList
from src.rec_system.commands.other_cmds.not_found_command import NotFoundCommandResponse
from src.domain.picture import Picture


class NotLikeOnlyCommandContructor(ICommandConstructor):
    user_repo = None
    pics_repo = None

    def __init__(self, user_repo: UserRepositoryList, pics_repo: PicturesRepositoryList) -> None:
        super().__init__()
        self.user_repo = user_repo
        self.pics_repo = pics_repo

    def construct(self, cmd_reg_res: CommandRecognizerResult) -> RecSystemCommandBase:
        picture_name_list = cmd_reg_res.matchings["picture_name_list"]
        picture_name = " ".join(picture_name_list)
        return NotLikeOnlyCommand(self.user_repo, self.pics_repo, picture_name)


class NotLikeOnlyCommandResponse(ICommandResponse):
    output_picture = None

    def __init__(self, output_picture: Picture):
        super().__init__()
        self.output_picture = output_picture

    def form_message(self) -> str:
        pic_str = f"#{self.output_picture.id}: {self.output_picture.name}"
        response = f"Из лайков убрана картина:\n{pic_str}"
        return response


class NotLikeOnlyCommand(RecSystemCommandBase):
    picture_name = None
    user_repo: UserRepositoryList = None
    pics_repo: PicturesRepositoryList = None

    def __init__(self, user_repo, pics_repo, picture_name: str) -> None:
        super().__init__()
        self.user_repo = user_repo
        self.pics_repo = pics_repo
        self.picture_name = picture_name

    def execute(self) -> ICommandResponse:
        selected_pic = self.pics_repo.select_by_name(self.picture_name)
        if selected_pic == None:
            return NotFoundCommandResponse()
        indx = next((e for e, did in enumerate(self.user.likes) if did == selected_pic.id), -1)
        if indx == -1:
            return NotFoundCommandResponse()
        del self.user.likes[indx]
        self.user_repo.update_user(self.user.id, self.user)
        return NotLikeOnlyCommandResponse(selected_pic)
