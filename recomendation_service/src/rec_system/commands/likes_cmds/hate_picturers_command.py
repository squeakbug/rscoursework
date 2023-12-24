from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class HatePicturersCommandContructor(ICommandConstructor):
    def construct(self, matchings: CommandRecognizerResult) -> RecSystemCommandBase:
        picture_name_list = matchings["picture_name_list"]
        return HatePicturersCommand(picture_name_list)


class HatePicturersCommandResponse(ICommandResponse):
    output_pictures_list = []

    def __init__(self, output_pictures_list: list):
        super().__init__()
        self.output_pictures_list = output_pictures_list

    def form_message(self) -> str:
        pic_list_str = "\n".join(self.output_pictures_list)
        response = f"В дизлайки добавлены картины:\n{pic_list_str}"
        return response


class HatePicturersCommand(RecSystemCommandBase):
    picture_name_list = None

    def __init__(self, picture_name_list: list) -> None:
        super().__init__()
        self.picture_name_list = picture_name_list

    def execute(self) -> ICommandResponse:
        # Найти картины с похожими именами
        # Добавить в пользователю к лайкам картины ... с id ...
        output_pictures_list = []
        return HatePicturersCommandResponse(output_pictures_list)
