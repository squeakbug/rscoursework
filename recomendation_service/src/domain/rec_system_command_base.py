"""

"""
from src.domain.user import User
from .measured_command import MeasuredCommandBase
from .executable_command import ExecutableCommandBase


class RecSystemCommandBase(ExecutableCommandBase, MeasuredCommandBase):
    user = None

    def set_user(self, user: User):
        self.user = user
