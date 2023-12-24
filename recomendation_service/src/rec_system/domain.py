import networkx as nx

from enum import Enum
from dataclasses import dataclass

from .measure import *
from ..domain.picture import DatasetItem


class PriceMeasure(Enum):
    VeryHighPrice = 1
    HighPrice = 2
    OptimalPrice = 3
    LowPrice = 4
    TooLowPrice = 5


G = nx.Graph()

G.add_edge("ROOT", "Portrait", weight=0.0)
G.add_edge("ROOT", "Scenery", weight=0.0)
G.add_edge("ROOT", "Still-life", weight=0.0)

G.add_edge("Portrait", "Self-portrait", weight=1.0)
G.add_edge("Portrait", "Historical portrait", weight=1.0)
G.add_edge("Portrait", "Posthumous portrait", weight=1.0)
G.add_edge("Portrait", "Religious portrait", weight=1.0)

G.add_edge("Scenery", "Marinus", weight=1.0)
G.add_edge("Scenery", "Industrial", weight=1.0)
G.add_edge("Scenery", "Historical", weight=1.0)
G.add_edge("Scenery", "Fantasy", weight=1.0)
G.add_edge("Scenery", "Landscape", weight=1.0)

G.add_edge("Still-life", "Floral-fruity", weight=1.0)
G.add_edge("Still-life", "Kitchen", weight=1.0)
G.add_edge("Still-life", "Vanitas", weight=1.0)

G.add_edge("Self-portrait", "Insertable", weight=2.0)
G.add_edge("Self-portrait", "Executive", weight=2.0)
G.add_edge("Self-portrait", "Group portrait", weight=2.0)
G.add_edge("Self-portrait", "Separate", weight=2.0)

G.add_edge("Historical portrait", "Historical Events", weight=2.0)
G.add_edge("Historical portrait", "Historical characters", weight=2.0)

G.add_edge("Religious portrait", "Religious Events", weight=2.0)
G.add_edge("Religious portrait", "Religious characters", weight=2.0)

G.add_edge("Marinus", "Open sea", weight=2.0)
G.add_edge("Marinus", "Coast", weight=2.0)
G.add_edge("Marinus", "Rivers/Lakes", weight=2.0)

G.add_edge("Industrial", "Bridges", weight=2.0)
G.add_edge("Industrial", "Residential buildings", weight=2.0)
G.add_edge("Industrial", "Industrial building", weight=2.0)
G.add_edge("Industrial", "Sights", weight=2.0)

G.add_edge("Floral-fruity", "Floral predominate", weight=2.0)
G.add_edge("Floral-fruity", "Fruits predominate", weight=2.0)

G.add_edge("Vanitas", "Steel arms", weight=2.0)
G.add_edge("Vanitas", "Human scull", weight=2.0)
G.add_edge("Vanitas", "Clocks", weight=2.0)
G.add_edge("Vanitas", "Table games", weight=2.0)


def get_genre_distance(item1, item2) -> float:
    return nx.shortest_path_length(G, source=item1.genre, target=item2.genre)


country_dict = {"USA": 0, "Russia": 1, "United Kingdom": 2, "Spain": 3, "France": 4}

country_matr = [
    [0.0, 1.0, 0.5, 0.6, 0.6],
    [1.0, 0.0, 0.4, 0.4, 0.4],
    [0.5, 0.4, 0.0, 0.2, 0.2],
    [0.6, 0.4, 0.2, 0.0, 0.1],
    [0.6, 0.4, 0.2, 0.1, 0.0],
]


# Сравнение стран
def get_country_distance(item1, item2) -> float:
    if item1.country == "" or item2.country == "":
        return 1.0
    if (not item1.country in country_dict) or (not item2.country in country_dict):
        return 1.0
    return country_matr[country_dict[item1.country]][country_dict[item2.country]]


subject_dict = {
    "Portraits": 0,
    "Still-Life": 1,
    "Nude": 2,
    "Abstract/Modern Art": 3,
    "Marine Art/Maritime": 4,
    "Landscape Art": 5,
    "Rivers/Lakes": 6,
    "Gardens": 7,
}

subject_matr = [
    [0.0, 0.9, 0.2, 0.8, 1.0, 1.0, 1.0, 1.0],
    [0.9, 0.0, 0.9, 1.0, 1.0, 0.8, 0.8, 0.8],
    [0.2, 0.9, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [0.8, 1.4, 1.2, 0.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 0.0, 0.7, 0.2, 0.9],
    [1.0, 0.8, 1.0, 1.0, 0.7, 0.0, 0.6, 0.5],
    [1.0, 0.8, 1.0, 1.0, 0.2, 0.6, 0.0, 0.9],
    [1.0, 0.8, 1.0, 1.0, 0.9, 0.5, 0.9, 0.0],
]


# Сравнение стран
def get_subject_distance(item1, item2) -> float:
    if item1.subject == "" or item2.subject == "":
        return 1.0
    if (not item1.subject in subject_dict) or (not item2.subject in subject_dict):
        return 1.0
    return subject_matr[subject_dict[item1.subject]][subject_dict[item2.subject]]


style_dict = {
    "Impressionism": 0,
    "Post-Impressionism": 1,
    "Baroque": 2,
    "Cubism": 3,
    "Renaissance": 4,
    "Rococo": 5,
    "Classicism": 6,
    "American Landscape": 7,
    "Expressionism": 8,
    "Romanticism": 9,
    "Art Nouveau": 10,
    "Realism": 11,
}

style_matr = [
    [0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0],
    [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0],
]


# Сравнение стран
def get_style_distance(item1, item2) -> float:
    if item1.style == "" or item2.style == "":
        return 1.0
    if (not item1.style in style_dict) or (not item2.style in style_dict):
        return 1.0
    return style_matr[style_dict[item1.style]][style_dict[item2.style]]


medium_dict = {"Oil on canvas": 0, "Pencil": 1, "Watercolor": 2, "Drybrush": 3}

medium_matr = [
    [0.0, 0.9, 0.8, 1.0],
    [0.9, 0.0, 1.0, 0.3],
    [0.8, 1.0, 0.0, 1.0],
    [1.0, 0.4, 1.0, 0.0],
]


# Сравнение стран
def get_medium_distance(item1, item2) -> float:
    if item1.medium == "" or item2.medium == "":
        return 1.0
    if (not item1.medium in medium_dict) or (not item2.medium in medium_dict):
        return 1.0
    return medium_matr[medium_dict[item1.medium]][medium_dict[item2.medium]]


def items_get_jaccard(item1, item2) -> float:
    fields1 = [item1.exhibition, item1.for_sale, item1.restored]
    fields2 = [item2.exhibition, item2.for_sale, item2.restored]
    return get_jaccard(fields1, fields2)


def items_get_size_distance(item1, item2) -> float:
    fields1 = [item1.width, item1.height]
    fields2 = [item2.width, item2.height]
    return get_euclidean_distance(fields1, fields2)


def get_century_from_death(death: int):
    return death // 100


def items_get_century_distance(item1, item2) -> float:
    fields1 = [get_century_from_death(item1.death)]
    fields2 = [get_century_from_death(item2.death)]
    return get_euclidean_distance(fields1, fields2)


def items_get_price_distance(item1, item2) -> float:
    fields1 = [item1.sale_price]
    fields2 = [item2.sale_price]
    return get_euclidean_distance(fields1, fields2)


def get_measure_for_price(price: int) -> PriceMeasure:
    if price > 750:
        return PriceMeasure.VeryHighPrice
    elif price > 650:
        return PriceMeasure.HightPrice
    elif price > 550:
        return PriceMeasure.OptimalPrice
    elif price > 450:
        return PriceMeasure.LowPrice
    else:
        return PriceMeasure.TooLowPrice


# Основные функции расчета мер

# TODO: подумать, насколько разряженными могут быть матрицы значений мер. Да и в общем, как часто ее расчитывают.
# Могут ли ее расчитывать только для отдельных элементов?
# Могут ли ее расчитывать для всего набора данных?
# Тут и вылезают эффективные алгоритмы перемножения матриц, структуры для их хранения и т.д


@dataclass
class Ranger:
    """
    Структура ограничений на поиск
    """

    width_min: int = 0
    width_max: int = 0
    height_min: int = 0
    height_max: int = 0
    sale_price_min: int = 0
    sale_price_max: int = 0
    century_min: int = 0
    century_max: int = 0


def calc_ranger(items: list[DatasetItem]) -> Ranger:
    ranger = Ranger()
    if len(items) == 0:
        return ranger
    ranger.width_min = items[0].width
    ranger.width_max = items[0].width
    ranger.height_min = items[0].height
    ranger.height_max = items[0].width
    ranger.sale_price_min = items[0].sale_price
    ranger.sale_price_max = items[0].sale_price
    ranger.century_min = get_century_from_death(items[0].death)
    ranger.century_max = get_century_from_death(items[0].death)
    for item in items:
        ranger.width_min = min(item.width, ranger.width_min)
        ranger.width_max = max(item.width, ranger.width_max)
        ranger.height_min = min(item.height, ranger.height_min)
        ranger.height_max = max(item.height, ranger.height_max)
        ranger.sale_price_min = min(item.sale_price, ranger.sale_price_min)
        ranger.sale_price_max = max(item.sale_price, ranger.sale_price_max)
        ranger.century_min = min(get_century_from_death(item.death), ranger.century_min)
        ranger.century_max = max(get_century_from_death(item.death), ranger.century_max)
    return ranger


# Сделать работу с матрицами: это немного увеличит пиковое потребление памяти,
# но позволит быстрее вычислить произведение,
# "проще" получить min/max для нормализации значений
def calc_measure_main(item1, item2, min_values: Ranger):
    size_dist = items_get_size_distance(item1, item2) / 35
    century_dist = items_get_century_distance(item1, item2) / 4
    price_dist = items_get_price_distance(item1, item2) / 500

    country_dist = get_country_distance(item1, item2)
    style_dist = get_style_distance(item1, item2)
    subject_dist = get_subject_distance(item1, item2)
    medium_dist = get_medium_distance(item1, item2)

    genre_dist = get_genre_distance(item1, item2) / 8

    jaccard_dist = items_get_jaccard(item1, item2) / 3

    k_size, k_century, k_price = 0.1, 0.3, 0.5
    k_country, k_style, k_subject, k_medium = 0.2, 0.7, 0.8, 0.7
    k_genre = 0.8
    k_jaccard = 0.05

    return (
        k_size * size_dist
        + k_century * century_dist
        + k_price * price_dist
        + k_country * country_dist
        + k_style * style_dist
        + k_subject * subject_dist
        + k_medium * medium_dist
        + k_genre * genre_dist
        + k_jaccard * jaccard_dist
    )


def calc_measure_money(item1, item2, min_values: Ranger):
    size_dist = items_get_size_distance(item1, item2) / 35
    century_dist = items_get_century_distance(item1, item2) / 4
    price_dist = items_get_price_distance(item1, item2) / 500

    country_dist = get_country_distance(item1, item2)
    style_dist = get_style_distance(item1, item2)
    subject_dist = get_subject_distance(item1, item2)
    medium_dist = get_medium_distance(item1, item2)

    genre_dist = get_genre_distance(item1, item2) / 8

    jaccard_dist = items_get_jaccard(item1, item2) / 3

    k_size, k_century, k_price = 0.1, 0.1, 1.5
    k_country, k_style, k_subject, k_medium = 0.1, 0.1, 0.1, 0.1
    k_genre = 0.1
    k_jaccard = 0.1

    return (
        k_size * size_dist
        + k_century * century_dist
        + k_price * price_dist
        + k_country * country_dist
        + k_style * style_dist
        + k_subject * subject_dist
        + k_medium * medium_dist
        + k_genre * genre_dist
        + k_jaccard * jaccard_dist
    )
