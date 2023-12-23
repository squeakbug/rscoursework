from typing import Optional

from src.rec_system.recomendation_system import ClosenessStrategy
from src.rec_system.data import DatasetItem
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
        items: list[DatasetItem],
        likes: list[DatasetItem],
        dislikes: list[DatasetItem],
        limit: Optional[int],
    ) -> list[DatasetItem]:
        pass

    def query_all(self, limit: Optional[int]) -> list[DatasetItem]:
        pass

    def query_with_filter(
        self,
        filter: Filter,
        limit: Optional[int],
    ) -> list[DatasetItem]:
        pass

    def query_names_like_weighted(
        self, items: list[DatasetItem], likes: list[DatasetItem], limit: Optional[int]
    ) -> list[tuple[DatasetItem, float]]:
        pass

    def query_like(self, likes: list[DatasetItem], limit: Optional[int]) -> list[DatasetItem]:
        pass
