class CommandDispatcherNLTK(ICommandDispatcher):
    commands = []

    def registrate_cmd(self, cmd: RecSystemCommandBase):
        self.commands.push(cmd)

    def get_most_accurate_cmd(self, user_input: str) -> RecSystemCommandBase:
        pass
