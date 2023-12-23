import logging
from uuid import UUID, uuid1

from src.repositories.user import UserRepositoryList
from src.domain.user import User
from src.rec_system.recomendation_system import RecomendationSystem
from src.nlp.nlprocessor import NLProcessor


class RecomendationService:
    user_repo = UserRepositoryList()
    rec_system = RecomendationSystem()
    nlprocessor = None

    def __init__(self, nlprocessor: NLProcessor):
        self.nlprocessor = nlprocessor

    def create_user(self, user_id: UUID) -> User:
        user = User()
        user.id = user_id
        new_user = self.user_repo.create_user(user)
        logging.debug(f"user with id={user_id} created")
        return new_user

    def process_text(self, user_id: UUID, request_text: str) -> str:
        user = user_repo.get_user_by_id(user_id)
        if user is None:
            new_user = self.create_default_user()
            user = user_repo.create_user(new_user)

        command_to_rs = self.nlprocessor.form_command(user, request_text)
        command_to_rs.set_executor(self.rec_system)
        command_to_rs.set_user(user)
        command_res = self.rec_system.process_command(command_to_rs)
        response_text = self.nlprocessor.form_response_text(user, command_res)

        return response_text

    def create_default_user(self) -> User:
        user = User()
        return user


if __name__ == "__main__":
    user_repo = UserRepositoryList()
    gen_uuid = uuid1()
    new_user = User()
    new_user.id = gen_uuid
    created_user = user_repo.create_user(new_user)
    selected_user = user_repo.get_user_by_id(gen_uuid)
    assert selected_user == new_user
