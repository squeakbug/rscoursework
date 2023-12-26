from typing import Optional

from src.rec_system.enums import ClosenessStrategy, RecomendationStrategy
from src.rec_system.filter import (
    Filter,
    calc_measure_main,
    calc_measure_money,
    calc_ranger,
    Ranger,
    filter_items,
)
from src.domain.picture import Picture
from src.repositories.pirtures_repo import PicturesRepositoryList


def find_self(lst, key):
    for elem in lst:
        if key(elem):
            return elem
    return None


class RecomendationSystem:
    picture_repo: PicturesRepositoryList = None
    measure_money_matrix_dict = None
    measure_base_matrix_dict = None
    min_values: Ranger = None
    closeness_strategy: ClosenessStrategy = None

    def __init__(self, picture_repo: PicturesRepositoryList) -> None:
        self.picture_repo = picture_repo

    def get_default_measure_func_name(
        self,
    ) -> str:
        return ""

    def get_default_strategy_name(
        self,
    ) -> str:
        return ""

    def get_strategies(
        self,
    ) -> list:
        return []

    def get_measures(
        self,
    ) -> list:
        return []

    def set_closeness_strategy(self, closeness_strategy: ClosenessStrategy):
        self.closeness_strategy = closeness_strategy

    def calc_measure_function(self, calc_func):
        self.min_values = calc_ranger(self.items)
        self.measure_matrix_dict = dict(
            [
                (
                    item1.name,
                    dict(
                        [
                            (item2.name, calc_func(item1, item2, self.min_values))
                            for item2 in self.items
                        ]
                    ),
                )
                for item1 in self.items
            ]
        )

    def do_recomendation(
        self,
        items: list[Picture],
        likes: list[Picture],
        dislikes: list[Picture],
        limit: Optional[int],
    ) -> list[Picture]:
        """
        В сортированном по близости к лайкам списке уменьшаем вес элементов на их вес в списке близких к дизлайкам элементов
        """
        names_like_likes = self.query_names_like_weighted(items, likes, None)
        names_like_dislikes = self.query_names_like_weighted(items, dislikes, None)

        names = []
        for liked_name in names_like_likes:
            dis_name = find_self(names_like_dislikes, lambda name: name[0] == liked_name[0])
            new_weight = liked_name[1]
            if not dis_name is None:
                new_weight -= dis_name[1]
            names.append((liked_name[0], new_weight))
        names = sorted(names, key=lambda x: x[1])

        result = []
        for name in names:
            item = find_self(items, lambda item: item.name == name[0])
            if not item is None:
                result.append(item)

        if not limit is None:
            result = result[:limit]
        return result

    def query_all(self, limit: Optional[int]) -> list[Picture]:
        items = self.picture_repo.select_all()
        if not limit is None:
            items = items[:limit]
        return items

    def query_with_filter(
        self,
        filter: Filter,
        limit: Optional[int],
    ) -> list[Picture]:
        items = self.picture_repo.select_all()
        items = filter_items(items, filter)
        if not limit is None:
            items = items[:limit]
        return items

    def query_names_like_weighted(
        self, items: list[Picture], likes: list[Picture], limit: Optional[int]
    ) -> list[tuple[Picture, float]]:
        for like in likes:
            row = self.measure_matrix_dict[like.name]
            if row == None:
                raise Exception("spam", "eggs")

        result = dict([(item.name, 0.0) for item in items])
        for like in likes:
            row = self.measure_matrix_dict[like.name]
            for name in row.keys():
                if not result[name] is None:
                    result[name] += row[name]

        result = sorted(result.items(), key=lambda x: x[1])
        if not limit is None:
            result = result[:limit]

        return result

    def query_like(self, likes: list[Picture], limit: Optional[int]) -> list[Picture]:
        for like in likes:
            row = self.measure_matrix_dict[like.name]
            if row == None:
                raise Exception("spam", "eggs")

        result = dict([(item, 0.0) for item in self.items])
        for like in likes:
            row = self.measure_matrix_dict[like.name]
            for name in row.keys():
                if not result[name] is None:
                    result[name] += row[name]

        result = sorted(result.items(), key=lambda x: x[1])
        result = [x[0] for x in result]
        if not limit is None:
            result = result[:limit]

        items = [x for x in self.items if x.name in result]
        return items

    def give_recomendation_filter_first_strategy(
        self,
        likes: list[Picture],
        dislikes: list[Picture],
        filter: Filter,
    ) -> list:
        """
        Получить отсортированный по "близости" список рекомендаций:
        Make selection based on provided filter
        Make recomendation based on selected items, dislikes and likes
        """
        items = self.picture_repo.select_all()
        filtered_items = filter_items(items, filter, None)
        filtered_item_names = [item.name for item in filtered_items]
        for like in likes:
            if not like.name in filtered_item_names:
                filtered_items.append(like)
        items = self.do_recomendation(items, filtered_items, dislikes, None)
        return items

    def give_recomendation_recomend_first_strategy(
        self,
        likes: list[Picture],
        dislikes: list[Picture],
        filter: Filter,
    ) -> list:
        """
        Получить отсортированный по "близости" список рекомендаций:
        Make recomendation based on likes and dislikes
        Make selection based on finded items and filters
        """
        items = self.picture_repo.select_all()
        items = self.do_recomendation(items, likes, dislikes, None)
        items = filter_items(items, filter, None)
        return items


"""
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_matrix(self):
    # Получить список кортежей (имя, расстояние до 1-го элемента)
    first_row = self.measure_matrix_dict[self.items[0].name].items()

    # Отсортировать список по увеличению расстояния до 1-го элемента
    sorted_first_row = sorted(first_row, key=lambda x: x[1])
    sorted_names = [x[0] for x in sorted_first_row]

    # Выборка значений по именам
    matrix = []
    for first_name in sorted_names:
        matrix.append(
            [self.measure_matrix_dict[first_name][second_name] for second_name in sorted_names]
        )
    sns.heatmap(matrix)
    plt.show()
"""
