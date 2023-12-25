from enum import Enum


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
