import numpy as np


# Центральный момент
def get_distance(v1, v2, nPow) -> float:
    res = 0.0
    for i in range(len(v1)):
        if v1[i] == None or v2[i] == None:
            continue
        res += pow(abs(v1[i] - v2[i]), nPow)
    return pow(res, 1.0 / nPow)


# Манхэттенское расстояние
def get_manhattan_distance(v1, v2) -> float:
    return get_distance(v1, v2, 1)


# Евклидово расстояние
def get_euclidean_distance(v1, v2) -> float:
    return get_distance(v1, v2, 2)


# Нормализация дипазона
def normalize(field: int, min_field: int, max_field: int) -> float:
    if max_field == min_field:
        return 0.0
    return (field - min_field) / (max_field - min_field)


# Обратная мера
def reverse_measure(field1: int, field2: int, min_field: int, max_field: int) -> float:
    if field1 == field2:
        return 0.0
    return 1.0 / (
        abs(normalize(field1, min_field, max_field) - normalize(field2, min_field, max_field))
    )


# Косинусная мера
def cos_measure(v1, v2) -> float:
    v1T, v2T = v1.copy(), v2.copy()
    n = len(v1)
    indArr = [
        i for i, (elem1, elem2) in enumerate(zip(v1T, v2T)) if np.isnan(elem1) or np.isnan(elem2)
    ]
    v1T[:] = [elem for i, elem in enumerate(v1T) if i not in indArr]
    v2T[:] = [elem for i, elem in enumerate(v2T) if i not in indArr]
    return 1.0 - np.dot(v1T, v2T) / (np.norm(v1T) * np.norm(v2T))


# Мера Жаккара
def get_jaccard(v1: list[bool], v2: list[bool]) -> float:
    a = v1.count(1)
    b = v2.count(1)
    c = 0.0
    if a == 0 and b == 0:
        return 0.0
    for i in range(len(v1)):
        if v1[i] and v2[i]:
            c += 1
    return 1.0 - c / (a + b - c)
