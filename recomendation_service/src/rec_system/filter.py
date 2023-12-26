from typing import Optional
from dataclasses import dataclass

from src.domain.picture import *
from src.rec_system.domain import *


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


def filter_value_cast(filter_name: str, filter_value: str):
    string_filters = ["name", "full_name", "country", "style", "subject", "genre", "medium"]
    if filter_name in string_filters:
        return filter_value
    
    int_filters = ["width_min", "width_max", "height_min", "height_max",
                   "sale_price_min", "sale_price_max", "century_min", "century_max"]
    if filter_name in int_filters:
        return int(filter_value)
    
    bool_filters = ["exhibition", "for_sale", "restored"]
    if filter_name in bool_filters:
        if filter_value == "да":
            return True 
        if filter_value == "нет":
            return False

    return None


def filter_to_string(filter: Filter) -> str:
    result = (
        f"Название картины: {filter.name}\n"
        f"Полное имя писателя: {filter.full_name}\n"
        f"Ширина картины (max): {filter.width_max}\n"
        f"Ширина картины (min): {filter.width_min}\n"
        f"Высота картины (max): {filter.height_max}\n"
        f"Высота картины (min): {filter.height_min}\n"
        f"Цена (max): {filter.sale_price_max}\n"
        f"Цена (min): {filter.sale_price_min}\n"
        f"Век написания картины (max): {filter.century_max}\n"
        f"Век написания картины (min): {filter.century_min}\n"
        f"Страна писателя: {filter.country}\n"
        f"Стиль: {filter.style}\n"
        f"Предмет картины: {filter.subject}\n"
        f"Жанр картины: {filter.genre}\n"
        f"Техника написания: {filter.medium}\n"
        f"Выставлена на обозрение (Да/Нет): {filter.exhibition}\n"
        f"Для продажи (Да/Нет): {filter.for_sale}\n"
        f"Реставрировалась (Да/Нет): {filter.restored}\n"
    )
    return result


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


def filter_items(items: list[Picture], filter: Filter, limit: Optional[int]) -> list[Picture]:
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


if __name__ == "__main__":
    filter = Filter
    print(filter_to_string(filter))
