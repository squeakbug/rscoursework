from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class HateWriterCommandContructor(ICommandConstructor):
    def construct(self, cmd_reg_res: CommandRecognizerResult) -> RecSystemCommandBase:
        writer_name = cmd_reg_res.matchings["writer_name"]
        return HateWriterCommand(writer_name)


class HateWriterCommandResponse(ICommandResponse):
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
            f"\nВы чувствуете отвращение ко всем этим картинам?"
        )
        return response


class HateWriterCommand(RecSystemCommandBase):
    writer_name = None

    def __init__(self, writer_name: str) -> None:
        super().__init__()
        self.writer_name = writer_name

    def execute(self) -> ICommandResponse:
        # query all pictures
        # filter pictures with author name ...
        pictures_list = []
        return HateWriterCommandResponse(self.writer_name, pictures_list)
