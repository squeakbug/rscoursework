from uuid import UUID, uuid1

from src.domain.user import User


class UserRepositoryList:
    users = []

    def get_user_by_id(self, id: UUID) -> User:
        return next((user for user in self.users if user.id == id), None)

    def create_user(self, user: User) -> User:
        self.users.append(user)
        return user

    def update_user(self, id: UUID, user: User) -> User:
        pass

    def delete_user(self, id: UUID):
        pass
