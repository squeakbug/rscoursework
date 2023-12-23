from src.domain.user import User
from src.domain.conversation_context import ConversationContext
from src.domain.commands import RecSystemCommandBase
from src.repositories.conversation_context import ConversationContextRepositoryList
from src.nlp.prolog.prolog_server_interface import PrologServer
from .preprocessing import preprocessing
from .icommand_dispatcher import ICommandDispatcher


class RecSystemCommandResponseBase:
    pass


class NLProcessor:
    ctx_repo = ConversationContextRepositoryList()
    cmd_recognizer: ICommandDispatcher

    def __init__(self, cmd_recognizer: ICommandDispatcher):
        self.cmd_recognizer = cmd_recognizer

    def form_command(self, user: User, request_text: str) -> RecSystemCommandBase:
        conversation_context = self.ctx_repo.get_context_by_id(user.conversation_context_id)
        return self.cmd_recognizer.get_most_accurate_cmd(user, request_text)

    def form_response_text(self, user: User, cmd_response: RecSystemCommandResponseBase) -> str:
        pass
