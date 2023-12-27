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
from src.domain.user import User
from src.repositories.pirtures_repo import PicturesRepositoryList


def find_self(lst, key):
    for elem in lst:
        if key(elem):
            return elem
    return None


class RecomendationSystem:
    picture_repo: PicturesRepositoryList = None
    measures = dict()

    def __init__(self, picture_repo: PicturesRepositoryList) -> None:
        self.picture_repo = picture_repo

    def get_default_measure_func_name(
        self,
    ) -> str:
        return "General-driven"

    def get_default_strategy_name(
        self,
    ) -> str:
        return "FilterFirst"

    def get_strategies(
        self,
    ) -> list:
        return ["RecomendFirst", "FilterFirst"]

    def get_measures(
        self,
    ) -> list:
        return ["General-driven", "Money-driven"]

    def add_measure_dict(self, name, measure_matrix_dict):
        self.measures[name] = measure_matrix_dict

    def do_recomendation(
        self,
        measure_name: str,
        items: list[Picture],
        likes: list[Picture],
        dislikes: list[Picture],
        limit: Optional[int],
    ) -> list[Picture]:
        """
        В сортированном по близости к лайкам списке уменьшаем вес элементов на их вес в списке близких к дизлайкам элементов
        """
        print("len(likes) = ", len(likes))
        names_like_likes = self.query_names_like_weighted(measure_name, items, likes, None)
        names_like_dislikes = self.query_names_like_weighted(measure_name, items, dislikes, None)

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
        self, measure_name: str, items: list[Picture], likes: list[Picture], limit: Optional[int]
    ) -> list[tuple[Picture, float]]:
        for like in likes:
            row = self.measures[measure_name][like.name]
            if row == None:
                raise Exception("spam", "eggs")

        result = dict([(item.name, 0.0) for item in items])
        for like in likes:
            row = self.measures[measure_name][like.name]
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
        measure_name: str,
        likes: list[Picture],
        dislikes: list[Picture],
        filter: Filter,
        limit: int
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
        items = self.do_recomendation(measure_name, items, filtered_items, dislikes, limit)
        return items

    def give_recomendation_recomend_first_strategy(
        self,
        measure_name: str,
        likes: list[Picture],
        dislikes: list[Picture],
        filter: Filter,
        limit: int
    ) -> list:
        """
        Получить отсортированный по "близости" список рекомендаций:
        Make recomendation based on likes and dislikes
        Make selection based on finded items and filters
        """
        items = self.picture_repo.select_all()
        items = self.do_recomendation(measure_name, items, likes, dislikes, limit)
        items = filter_items(items, filter, limit)
        return items

    def give_recomendation(self, user: User, limit: int):
        likes = [self.picture_repo.get_picture_by_id(id) for id in user.likes]
        dislikes = [self.picture_repo.get_picture_by_id(id) for id in user.dislikes]
        filter = user.filter
        measure_name = user.measure_func_name
        strategy = user.strategy_name

        if strategy == "RecomendFirst":
            return self.give_recomendation_recomend_first_strategy(
                measure_name, likes, dislikes, filter, limit
            )
        else:
            return self.give_recomendation_filter_first_strategy(
                measure_name, likes, dislikes, filter, limit
            )


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
