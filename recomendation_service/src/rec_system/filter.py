from typing import Optional
from dataclasses import dataclass

from .data import *
from .domain import *


@dataclass
class Filter:
    """
    Структура ограничений на поиск
    """

    name: Optional[str] = None
    full_name: Optional[str] = None
    width_min: Optional[int] = None
    width_max: Optional[int] = None
    height_min: Optional[int] = None
    height_max: Optional[int] = None
    sale_price_min: Optional[int] = None
    sale_price_max: Optional[int] = None
    century_min: Optional[int] = None
    century_max: Optional[int] = None
    country: Optional[str] = None
    style: Optional[str] = None
    subject: Optional[str] = None
    genre: Optional[str] = None
    medium: Optional[str] = None
    exhibition: Optional[bool] = None
    for_sale: Optional[bool] = None
    restored: Optional[bool] = None

    price_approx: Optional[PriceMeasure] = None

    limit: Optional[int] = None


# Вспомогательные функции API


def filter_min(items: list, get_value_lambda, min_value: Optional[int]) -> list:
    return filter(
        lambda item: True
        if (min_value is None) or (get_value_lambda(item) >= min_value)
        else False,
        items,
    )


def filter_max(items: list, get_value_lambda, max_value: Optional[int]) -> list:
    return filter(
        lambda item: True
        if (max_value is None) or (get_value_lambda(item) <= max_value)
        else False,
        items,
    )


def filter_eq(items: list, get_value_lambda, exact_value) -> list:
    return filter(
        lambda item: True
        if (exact_value is None) or (get_value_lambda(item) == exact_value)
        else False,
        items,
    )


def filter_items(
    items: list[DatasetItem], filter: Filter, limit: Optional[int]
) -> list[DatasetItem]:
    items = filter_min(items, lambda item: item.width, filter.width_min)
    items = filter_max(items, lambda item: item.width, filter.width_max)
    items = filter_min(items, lambda item: item.height, filter.height_min)
    items = filter_max(items, lambda item: item.height, filter.height_max)
    items = filter_min(items, lambda item: get_century_from_death(item.death), filter.century_min)
    items = filter_max(items, lambda item: get_century_from_death(item.death), filter.century_max)

    items = filter_eq(items, lambda item: item.name, filter.name)
    items = filter_eq(items, lambda item: item.full_name, filter.full_name)
    items = filter_eq(items, lambda item: item.country, filter.country)
    items = filter_eq(items, lambda item: item.style, filter.style)
    items = filter_eq(items, lambda item: item.subject, filter.subject)
    items = filter_eq(items, lambda item: item.genre, filter.genre)
    items = filter_eq(items, lambda item: item.medium, filter.medium)
    items = filter_eq(items, lambda item: item.exhibition, filter.exhibition)
    items = filter_eq(items, lambda item: item.for_sale, filter.for_sale)
    items = filter_eq(items, lambda item: item.restored, filter.restored)

    if filter.price_approx is None:
        items = filter_min(items, lambda item: item.sale_price, filter.sale_price_min)
        items = filter_max(items, lambda item: item.sale_price, filter.sale_price_max)
    else:
        items = filter_eq(
            items,
            lambda item: get_measure_for_price(item.sale_price),
            filter.price_approx,
        )

    if not filter.limit is None:
        items = items[:limit]
    return list(items)


# Test
def test_filter_min():
    filtered = filter_min([1, 2, 3, 4, 5, 6], lambda x: x, 4)
    assert list(filtered) == [4, 5, 6]
    filtered = filter_max([1, 2, 3, 4, 5, 6], lambda x: x, 4)
    assert list(filtered) == [1, 2, 3, 4]
