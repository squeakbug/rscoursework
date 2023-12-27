from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse
from src.repositories.conversation_context_repo import ConversationContextRepositoryList
from src.repositories.user_repo import UserRepositoryList
from src.rec_system.commands.filter_cmds.add_filter_command import AddFilterCommand
from src.rec_system.commands.other_cmds.unknown_command import UnknownCommandResponse
from src.nlp.edit_distance_tools import replace_filter_name, get_most_similar_filter_name
from src.rec_system.filter import filter_value_cast


class FilterValueEqCommandContructor(ICommandConstructor):
    ctx_repo: ConversationContextRepositoryList = None
    user_repo: UserRepositoryList = None

    def __init__(
        self, user_repo: UserRepositoryList, ctx_repo: ConversationContextRepositoryList
    ) -> None:
        super().__init__()
        self.ctx_repo = ctx_repo
        self.user_repo = user_repo

    def construct(self, cmd_reg_res: CommandRecognizerResult) -> RecSystemCommandBase:
        filter_value = cmd_reg_res.matchings["filter_value"]
        return FilterValueEqCommand(self.user_repo, self.ctx_repo, filter_value)


class FilterValueEqCommandResponse(ICommandResponse):
    filter_name = None
    filter_value = None

    def __init__(self, filter_name, filter_value) -> None:
        super().__init__()
        self.filter_name = filter_name
        self.filter_value = filter_value

    def form_message(self) -> str:
        return f'Значение фильтра "{self.filter_name}" установлено на {self.filter_value}'


class FilterValueEqCommand(RecSystemCommandBase):
    filter_value = None
    ctx_repo: ConversationContextRepositoryList = None
    user_repo: UserRepositoryList = None

    def __init__(
        self,
        user_repo: UserRepositoryList,
        ctx_repo: ConversationContextRepositoryList,
        filter_value: str,
    ) -> None:
        super().__init__()
        self.filter_value = filter_value
        self.ctx_repo = ctx_repo
        self.user_repo = user_repo

    # TODO: Добавить проверку, что последняя команда - AddFilterCommand
    # TODO: Добавить проверку, что название фильтра существует (threashold value for coincidence)
    def execute(self) -> ICommandResponse:
        ctx = self.ctx_repo.get_context_by_id(self.user.conversation_context_id)
        last_request = ctx.queries[-1]
        print(last_request)
        user_filter_name = last_request.filter_name
        domain_filter_name = replace_filter_name(user_filter_name)
        user_filter_name = get_most_similar_filter_name(user_filter_name)
        casted_filter_value = filter_value_cast(domain_filter_name, self.filter_value)
        setattr(self.user.filter, domain_filter_name, casted_filter_value)
        self.user_repo.update_user(self.user.id, self.user)
        response = FilterValueEqCommandResponse(user_filter_name, casted_filter_value)
        return response
