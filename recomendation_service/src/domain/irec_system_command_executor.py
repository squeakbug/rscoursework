"""

"""

from typing import Optional

from src.rec_system.recomendation_system import ClosenessStrategy
from src.domain.picture import Picture
from src.rec_system.filter import Filter
from src.domain.user import User


class IRecSystemCommandExecutor:
    def get_default_measure_func_name(
        self,
    ) -> str:
        pass

    def get_default_strategy_name(
        self,
    ) -> str:
        pass

    def get_strategies(
        self,
    ) -> list:
        pass

    def get_measures(
        self,
    ) -> list:
        pass

    def add_measure_dict(self, name, measure_matrix_dict):
        pass

    def set_closeness_strategy(self, closeness_strategy: ClosenessStrategy):
        pass

    def give_recomendation(self, user: User, limit: int):
        pass
