"""
if rule == RULE_HELLO:
    cmd = HelloCommand()

if rule == RULE_911:
    cmd = SosCommand()

if rule == RULE_CHANGE_MEASURE:
    cmd = ChangeMeasureCommand()
    most_similar_func_name = replace_measure_function_name(res_dict["measure_name"])
    cmd.set_measure_function(most_similar_func_name)

if rule == RULE_CHANGE_STRATEGY:
    cmd = ChangeStrategyCommand()
    most_similar_strategy_name = replace_strategy_name(res_dict["strategy_name"])
    cmd.set_strategy(most_similar_strategy_name)

if rule == RULE_ADD_FILTER:
    cmd = ChangeAddFilterCommand()
    most_similar_strategy_name = replace_filter_name(res_dict["filter_name"])
    cmd.set_strategy(most_similar_strategy_name)

if rule == RULE_RESET_FILTER:
    cmd = ChangeResetFilterCommand()
    most_similar_strategy_name = replace_strategy_name(res_dict["strategy_name"])
    cmd.set_strategy(most_similar_strategy_name)
"""


class CommandDispatcherRegex(ICommandDispatcher):
    commands = []

    def registrate_cmd(self, cmd: RecSystemCommandBase):
        self.commands.push(cmd)

    def get_most_accurate_cmd(self, user_input: str) -> RecSystemCommandBase:
        pass

    def form_command_regex(user: User, request_text: str) -> RecSystemCommandBase:
        pass
        """
        cmd_finded = 0
        cmd = None
        normalized_user_input = preprocessing(request_text)
        for rule in RULES:
            regexp = re.compile(rule)
            match = regexp.match(normalized_user_input)
            if match is not None:
                res_dict = match.groupdict()

                

                cmd_finded = True
                break

        if not cmd_finded:
            cmd = get_cmd_on_missing(normalized_user_input)

        return cmd
        matchings = 
        for rule in RULES:
            regexp = re.compile(rule)
            match = regexp.match(user_input)
            if 
        measures = get_measure(user_input, rule)
        return max(self, self.commands, key=lambda cmd: cmd.get_measure(user_input))
        """
