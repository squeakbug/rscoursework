from src.domain.rec_system_command_base import RecSystemCommandBase
from src.rec_system.recomendation_system import RecomendationStrategy
from src.domain.icommand_constructor import ICommandConstructor, CommandRecognizerResult
from src.domain.icommand_response import ICommandResponse


class SuggestSomethingCommandContructor(ICommandConstructor):
    def construct(self, cmd_reg_res: CommandRecognizerResult) -> RecSystemCommandBase:
        suggestions = cmd_reg_res.matchings["suggestion"]
        return SuggestSomethingCommand()


class SuggestSomethingCommandResponse(ICommandResponse):
    suggestion_list = None

    def __init__(self, suggestion_list: list):
        self.suggestion_list = suggestion_list

    def form_message(self) -> str:
        suggestions_str = ", ".join(self.suggestion_list)
        response = f"Рекомендуя вам посмотреть на след. экспонаты: {suggestions_str}"
        return response


class SuggestSomethingCommand(RecSystemCommandBase):
    def __init__(self, suggestion) -> None:
        super().__init__()
        self.suggestion = suggestion

    def execute(self) -> ICommandResponse:
        rec_system = self.executor
        all_items = rec_system.query_all(None)
        likes = [item for (i, item) in enumerate(all_items) if i in likes]
        dislikes = [item for (i, item) in enumerate(all_items) if i in dislikes]

        items = []
        filter = rec_system.get_filter()
        strategy = rec_system.get_recomendation_strategy()
        if strategy == RecomendationStrategy.FilterFirst:
            items = rec_system.give_recomendation_filter_first_strategy(
                rec_system, likes=likes, dislikes=dislikes, filter=filter
            )
        elif strategy == RecomendationStrategy.RecomendFirst:
            items = rec_system.give_recomendation_recomend_first_strategy(
                rec_system, likes=likes, dislikes=dislikes, filter=filter
            )

        response = SuggestSomethingCommandResponse(suggestion_list=items)
        return response
