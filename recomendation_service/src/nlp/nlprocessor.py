from src.domain.user import User
from src.domain.conversation_context import ConversationContext
from src.rec_system.commands.other_cmds.hello_command import (
    RecSystemCommandBase,
)
from src.repositories.conversation_context_repo import (
    ConversationContextRepositoryList,
)
from src.domain.icommand_response import ICommandResponse
from src.nlp.icommand_dispatcher import ICommandDispatcher


class NLProcessor:
    ctx_repo: ConversationContextRepositoryList = None
    cmd_recognizer: ICommandDispatcher = None

    def __init__(
        self, cmd_recognizer: ICommandDispatcher, ctx_repo: ConversationContextRepositoryList
    ):
        self.cmd_recognizer = cmd_recognizer
        self.ctx_repo = ctx_repo

    def form_command(self, user: User, request_text: str) -> RecSystemCommandBase:
        conversation_context = self.ctx_repo.get_context_by_id(user.conversation_context_id)
        return self.cmd_recognizer.get_most_accurate_cmd(user, request_text)

    def form_response_text(self, user: User, cmd_response: ICommandResponse) -> str:
        conversation_context = self.ctx_repo.get_context_by_id(user.conversation_context_id)
        return cmd_response.form_message()
