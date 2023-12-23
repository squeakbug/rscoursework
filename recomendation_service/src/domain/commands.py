from dataclasses import dataclass

from .rec_system_command_base import RecSystemCommandBase


@dataclass
class CommandRecognizerResult:
    rule_name: str
    matchings: list


class HelloCommand(RecSystemCommandBase):
    def get_measure(self, user_input):
        return 1

    def execute(self):
        print("Привет, человек")


class HelloCommandContructor:
    def contruct(recognize_result: CommandRecognizerResult) -> RecSystemCommandBase:
        return HelloCommand()


"""
class SelectAllCommand(RecSystemCommandBase):
    def get_measure(self, user_input):
        return 0
    
    def execute(self):
        print("Hello world")


class SosCommand(RecSystemCommandBase):
    def execute(self):
        print("Вызываю полицию (и скорую)!")


class ResetSessionCommand(RecSystemCommandBase):
    def execute(self):
        main_filter = Filter()
        strategy = RecomendationStrategy.FilterFirst


class ResetHistoryCommand(RecSystemCommandBase):
    def execute(self):
        global main_filter
        global strategy
        main_filter = Filter()
        strategy = RecomendationStrategy.FilterFirst


class SuggestSomethingCommand(RecSystemCommandBase):
    def execute(self):
        global strategy
        global likes
        global dislikes
        global main_filter
        all_items = rec_system.query_all(None)
        likes = [item for (i, item) in enumerate(all_items) if i in likes]
        dislikes = [item for (i, item) in enumerate(all_items) if i in dislikes]

        items = []
        if strategy == RecomendationStrategy.FilterFirst:
            items = give_recomendation_filter_first_strategy(
                rec_system, likes=likes, dislikes=dislikes, filter=main_filter
            )
        elif strategy == RecomendationStrategy.RecomendFirst:
            items = give_recomendation_recomend_first_strategy(
                rec_system, likes=likes, dislikes=dislikes, filter=main_filter
            )
        for i, item in enumerate(items):
            print(
                f"{i:2}) {item.name}: price={item.sale_price}; genre={item.genre}; style={item.style}; subject={item.subject}"
            )
        return 0


class SuggestLikePicturesCommand(RecSystemCommandBase):
    def execute(self):
        print("Вызываю полицию!")


class SuggestDislikePicturesCommand(RecSystemCommandBase):
    def execute(self):
        print("Вызываю полицию!")


class ChangeStrategyCommand(RecSystemCommandBase):
    def set_strategy(self, strategy_name: str):
        self.strategy_name = strategy_name

    def execute(self):
        global strategy
        if self.strategy_name == "RecomendFirst":
            strategy = RecomendationStrategy.RecomendFirst
            print("Установлена RecomendFirst стратегия")
        elif self.strategy_name == "FilterFirst":
            strategy = RecomendationStrategy.FilterFirst
            print("Установлена FilterFirst стратегия")
        else:
            raise Exception("No such measure function")


class ChangeMeasureCommand(RecSystemCommandBase):
    def set_measure_function(self, measure_func_name: str):
        self.measure_func_name = measure_func_name

    def execute(self):
        if self.measure_func_name == "General-driven":
            rec_system.calc_measure_function(calc_measure_main)
            print("Установлена General-driven функция")
        elif self.measure_func_name == "Money-driven":
            rec_system.calc_measure_function(calc_measure_money)
            print("Установлена Money-driven функция")
        else:
            raise Exception("No such measure function")


class AddFilterCommand(RecSystemCommandBase):
    def execute(self):
        print("Вызываю полицию!")


class ShowFiltersCommand(RecSystemCommandBase):
    def execute(self):
        print("Вызываю полицию!")


class UnsetFilterCommand(RecSystemCommandBase):
    def execute(self):
        print("Вызываю полицию!")
"""
