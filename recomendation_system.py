import csv
import seaborn as sns
import matplotlib.pyplot as plt


from enum import Enum
from typing import Optional
from dataclass_csv import DataclassReader

from filter import *
from data import DatasetItem
from recomendation_system import *


class ClosenessStrategy(Enum):
    """
    Политика близости:
    NearDistinctSeeds - искать в окрестности полученных от пользователя записей
    NearGeneralCenter - искать в окрестности центра (по функции меры) полученных от пользователя записей
    """

    NearDistinctSeeds = 1
    NearGeneralCenter = 2


class RecomendationStrategy(Enum):
    RecomendFirst = 1
    FilterFirst = 2


@dataclass
class User:
    """
    Структура пользователя
    """

    history: list


def find_self(lst, key):
    for elem in lst:
        if key(elem):
            return elem
    return None


query_rk1_aicourse_items = []
with open("data/query-rk1-aicourse-10-14-2023-QueryResult.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    reader = DataclassReader(csv_file, DatasetItem, validate_header=False)

    for item in reader:
        query_rk1_aicourse_items.append(item)


class RecomendationSystem:
    items = query_rk1_aicourse_items
    measure_matrix_dict = None
    min_values: Ranger = None
    closeness_strategy: ClosenessStrategy = None

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
        items: list[DatasetItem],
        likes: list[DatasetItem],
        dislikes: list[DatasetItem],
        limit: Optional[int],
    ) -> list[DatasetItem]:
        """
        В сортированном по близости к лайкам списке уменьшаем вес элементов на их вес в списке близких к дизлайкам элементов
        """
        names_like_likes = self.query_names_like_weighted(items, likes, None)
        names_like_dislikes = self.query_names_like_weighted(items, dislikes, None)

        names = []
        for liked_name in names_like_likes:
            dis_name = find_self(
                names_like_dislikes, lambda name: name[0] == liked_name[0]
            )
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

    def query_all(self, limit: Optional[int]) -> list[DatasetItem]:
        items = [_ for _ in query_rk1_aicourse_items]
        if not limit is None:
            items = items[:limit]
        return items

    def query_with_filter(
        self,
        filter: Filter,
        limit: Optional[int],
    ) -> list[DatasetItem]:
        items = [_ for _ in query_rk1_aicourse_items]
        items = filter_items(items, filter)
        if not limit is None:
            items = items[:limit]
        return items

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
                [
                    self.measure_matrix_dict[first_name][second_name]
                    for second_name in sorted_names
                ]
            )
        sns.heatmap(matrix)
        plt.show()

    def query_names_like_weighted(
        self, items: list[DatasetItem], likes: list[DatasetItem], limit: Optional[int]
    ) -> list[tuple[DatasetItem, float]]:
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

    def query_like(
        self, likes: list[DatasetItem], limit: Optional[int]
    ) -> list[DatasetItem]:
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
    rec_system: RecomendationSystem,
    likes: list[DatasetItem],
    dislikes: list[DatasetItem],
    filter: Filter,
) -> list:
    """
    Получить отсортированный по "близости" список рекомендаций:
    Make selection based on provided filter
    Make recomendation based on selected items, dislikes and likes
    """
    items = query_rk1_aicourse_items
    filtered_items = filter_items(items, filter, None)
    filtered_item_names = [item.name for item in filtered_items]
    for like in likes:
        if not like.name in filtered_item_names:
            filtered_items.append(like)
    items = rec_system.do_recomendation(items, filtered_items, dislikes, None)
    return items


def give_recomendation_recomend_first_strategy(
    rec_system: RecomendationSystem,
    likes: list[DatasetItem],
    dislikes: list[DatasetItem],
    filter: Filter,
) -> list:
    """
    Получить отсортированный по "близости" список рекомендаций:
    Make recomendation based on likes and dislikes
    Make selection based on finded items and filters
    """
    items = query_rk1_aicourse_items
    items = rec_system.do_recomendation(items, likes, dislikes, None)
    items = filter_items(items, filter, None)
    return items
