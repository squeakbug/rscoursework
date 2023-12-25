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
        indx = next((e for e, usr in enumerate(self.users) if usr.id == id), -1)
        if indx == -1:
            return None
        else:
            self.users[indx] = user
            return self.users[indx]

    def delete_user(self, id: UUID):
        indx = next((e for e, usr in enumerate(self.users) if usr.id == id), -1)
        if indx != -1:
            del self.users[indx]
