"""

"""
from .irec_system_command_executor import IRecSystemCommandExecutor
from .icommand_response import ICommandResponse


class ExecutableCommandBase:
    executor: IRecSystemCommandExecutor

    def set_executor(self, executor: IRecSystemCommandExecutor):
        self.executor = executor

    def execute(self) -> ICommandResponse:
        pass
