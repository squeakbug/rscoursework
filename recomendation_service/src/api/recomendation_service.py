import logging
from uuid import UUID, uuid1

from src.repositories.user_repo import UserRepositoryList
from src.repositories.conversation_context_repo import (
    ConversationContextRepositoryList,
)
from src.domain.user import User
from src.domain.conversation_context import ConversationContext
from src.rec_system.recomendation_system import RecomendationSystem
from src.nlp.nlprocessor import NLProcessor
from src.rec_system.filter import Filter


class RecomendationService:
    user_repo = None
    ctx_repo = None
    rec_system = None
    nlprocessor = None

    def __init__(
        self,
        nlprocessor: NLProcessor,
        user_repo: UserRepositoryList,
        ctx_repo: ConversationContextRepositoryList,
        rec_system: RecomendationSystem,
    ):
        self.nlprocessor = nlprocessor
        self.user_repo = user_repo
        self.rec_system = rec_system
        self.ctx_repo = ctx_repo

    def create_user(self, user_id: UUID) -> User:
        user = User()
        user.id = user_id
        user.likes = []
        user.dislikes = []
        user.filter = Filter()
        user.measure_func_name = self.rec_system.get_default_measure_func_name()
        user.strategy_name = self.rec_system.get_default_strategy_name()
        conversation_ctx = ConversationContext()
        conversation_ctx.id = uuid1()
        new_conv_ctx = self.ctx_repo.create_context(conversation_ctx)
        user.conversation_context_id = new_conv_ctx.id
        new_user = self.user_repo.create_user(user)
        return new_user

    def process_text(self, user_id: UUID, request_text: str) -> str:
        user = self.user_repo.get_user_by_id(user_id)
        if user is None:
            return "Сначала необходимо зарегистрироваться (введите /start)"

        command_to_rs = self.nlprocessor.form_command(user, request_text)
        command_to_rs.set_executor(self.rec_system)
        command_to_rs.set_user(user)
        command_res = command_to_rs.execute()
        response_text = self.nlprocessor.form_response_text(user, command_res)

        ctx = self.ctx_repo.get_context_by_id(user.conversation_context_id)
        ctx.queries.append(command_to_rs)
        ctx.responses.append(command_res)
        self.ctx_repo.update_context(ctx.id, ctx)

        return response_text


if __name__ == "__main__":
    user_repo = UserRepositoryList()
    gen_uuid = uuid1()
    new_user = User()
    new_user.id = gen_uuid
    created_user = user_repo.create_user(new_user)
    selected_user = user_repo.get_user_by_id(gen_uuid)
    assert selected_user == new_user
