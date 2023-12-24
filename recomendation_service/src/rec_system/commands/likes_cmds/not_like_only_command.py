from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class NotLikeOnlyCommandContructor(ICommandConstructor):
    def construct(self, matchings: CommandRecognizerResult) -> RecSystemCommandBase:
        picture_name_list = matchings["picture_name_list"]
        return NotLikeOnlyCommand(picture_name_list)


class NotLikeOnlyCommandResponse(ICommandResponse):
    output_pictures_list = []

    def __init__(self, output_pictures_list: list):
        super().__init__()
        self.output_pictures_list = output_pictures_list

    def form_message(self) -> str:
        pic_list_str = "\n".join(self.output_pictures_list)
        response = f"Из лайков убраны картины:\n{pic_list_str}"
        return response


class NotLikeOnlyCommand(RecSystemCommandBase):
    picture_name_list = None

    def __init__(self, picture_name_list: list) -> None:
        super().__init__()
        self.picture_name_list = picture_name_list

    def execute(self) -> ICommandResponse:
        # Найти картины с похожими именами
        # Добавить в пользователю к лайкам картины ... с id ...
        output_pictures_list = []
        return NotLikeOnlyCommandResponse(output_pictures_list)
