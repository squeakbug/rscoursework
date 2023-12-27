from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.user_repo import UserRepositoryList
from src.repositories.pirtures_repo import PicturesRepositoryList
from src.rec_system.commands.other_cmds.not_found_command import NotFoundCommand


class LikeWriterCommandContructor(ICommandConstructor):
    user_repo = None
    pics_repo = None

    def __init__(self, user_repo: UserRepositoryList, pics_repo: PicturesRepositoryList) -> None:
        super().__init__()
        self.user_repo = user_repo
        self.pics_repo = pics_repo

    def construct(self, cmd_reg_res: CommandRecognizerResult) -> RecSystemCommandBase:
        writer_name_list = cmd_reg_res.matchings["writer_name_list"]
        writer_name = " ".join(writer_name_list)
        return LikeWriterCommand(self.user_repo, self.pics_repo, writer_name)


class LikeWriterCommandResponse(ICommandResponse):
    writer_name = None
    pictures_list = None

    def __init__(self, writer_name: str, pictures_list: list) -> None:
        super().__init__()
        self.writer_name = writer_name
        self.pictures_list = pictures_list

    def form_message(self) -> str:
        pictures_list_str = "\n".join(self.pictures_list)
        response = (
            f"Вот список картин {self.writer_name}:\n"
            f"{pictures_list_str}"
            f"\nВам все они понравились?"
        )
        return response


class LikeWriterCommand(RecSystemCommandBase):
    writer_name = None
    user_repo: UserRepositoryList = None
    pics_repo: PicturesRepositoryList = None

    def __init__(self, user_repo, pics_repo, writer_name: list) -> None:
        super().__init__()
        self.user_repo = user_repo
        self.pics_repo = pics_repo
        self.writer_name = writer_name

    def execute(self) -> ICommandResponse:
        pics = self.pics_repo.select_by_writer_name(self.writer_name)
        if len(pics) == None:
            return NotFoundCommand()
        return LikeWriterCommandResponse(self.writer_name, pics)
