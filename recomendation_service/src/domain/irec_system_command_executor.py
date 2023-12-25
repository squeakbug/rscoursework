"""

"""

from typing import Optional

from src.rec_system.recomendation_system import ClosenessStrategy
from src.domain.picture import Picture
from src.rec_system.filter import Filter


class IRecSystemCommandExecutor:
    def set_closeness_strategy(self, closeness_strategy: ClosenessStrategy):
        pass

    def calc_measure_function(self, calc_func):
        pass

    def select_all(self):
        pass

    def do_recomendation(
        self,
        items: list[Picture],
        likes: list[Picture],
        dislikes: list[Picture],
        limit: Optional[int],
    ) -> list[Picture]:
        pass

    def query_all(self, limit: Optional[int]) -> list[Picture]:
        pass

    def query_with_filter(
        self,
        filter: Filter,
        limit: Optional[int],
    ) -> list[Picture]:
        pass

    def query_names_like_weighted(
        self, items: list[Picture], likes: list[Picture], limit: Optional[int]
    ) -> list[tuple[Picture, float]]:
        pass

    def query_like(self, likes: list[Picture], limit: Optional[int]) -> list[Picture]:
        pass
