from simple_term_menu import TerminalMenu

from filter import *
from recomendation_system import *


options = [
    "Вывести все записи",
    "Визуализировать матрицу расстояний",
    "Поставить лайк 👍",
    "Сбросить лайк 👍",
    "Поставить дизлайк 👎",
    "Сбросить дизлайк 👎",
    "Установить фильтр",
    "Сбросить фильтр",
    "Вывести фильтр",
    "Установить функцию меры",
    "Установить стратегию рекомендации",
    "Получить рекомендацию",
    "Выход 😭",
]


def choose_measure_function(rec_system):
    choose_measure_options = ["General-driven", "Money-driven"]
    terminal_menu = TerminalMenu(choose_measure_options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        rec_system.calc_measure_function(calc_measure_main)
    elif menu_entry_index == 1:
        rec_system.calc_measure_function(calc_measure_money)
    else:
        print("❗Перестаньте ломать программу❗")

    return 0


def choose_set_filter(filter: Filter) -> Filter:
    choose_measure_options = [
        "Название картины",                  #  0
        "Полное имя писателя",               #  1
        "Ширина картины",                    #  2
        "Высота картины",                    #  3
        "Цена",                              #  4
        "Век написания картины",             #  5
        "Страна писателя",                   #  6
        "Стиль",                             #  7
        "Предмет картины",                   #  8
        "Жанр картины",                      #  9
        "Техника написания",                 # 10
        "Выставлена на обозрение (Да/Нет)",  # 11
        "Для продажи (Да/Нет)",              # 12
        "Реставрировалась (Да/Нет)",         # 13
    ]
    terminal_menu = TerminalMenu(choose_measure_options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        name = input("Название картины: ")
        filter.name = name
    elif menu_entry_index == 1:
        full_name = input("Полное имя автора")
        filter.full_name = full_name
    elif menu_entry_index == 2:
        choose_width_menu = TerminalMenu(["Нижняя граница", "Верхняя граница"])
        choose_entry_index = choose_width_menu.show()
        if choose_entry_index == 0:
            filter.width_min = int(input("Нижняя граница ширины: "))
        else:
            filter.width_max = int(input("Верхняя граница ширины: "))
    elif menu_entry_index == 3:
        choose_height_menu = TerminalMenu(["Нижняя граница", "Верхняя граница"])
        choose_entry_index = choose_height_menu.show()
        if choose_entry_index == 0:
            filter.height_min = int(input("Нижняя граница высоты: "))
        else:
            filter.height_max = int(input("Верхняя граница высоты: "))
    elif menu_entry_index == 4:
        choose_price_menu = TerminalMenu(["Нижняя граница", "Верхняя граница"])
        choose_entry_index = choose_price_menu.show()
        if choose_entry_index == 0:
            filter.sale_price_min = int(input("Нижняя граница цены: "))
        else:
            filter.sale_price_max = int(input("Верхняя граница цены: "))
    elif menu_entry_index == 5:
        choose_century_menu = TerminalMenu(["Нижняя граница", "Верхняя граница"])
        choose_entry_index = choose_century_menu.show()
        if choose_entry_index == 0:
            filter.century_min = int(input("Нижняя граница: "))
        else:
            filter.century_max = int(input("Верхняя граница: "))
    elif menu_entry_index == 6:
        country = input()
        filter.country = country
    elif menu_entry_index == 7:
        style = input()
        filter.style = style
    elif menu_entry_index == 8:
        subject = input()
        filter.subject = subject
    elif menu_entry_index == 9:
        genre = input()
        filter.genre = genre
    elif menu_entry_index == 10:
        medium = input()
        filter.medium = medium
    elif menu_entry_index == 11:
        for_sale = input()
        if for_sale == "Да":
            filter.for_sale = True
        elif restored == "Нет":
            filter.for_sale = False
        else:
            print("Повторите ввод: введите 'Да' или 'Нет'")
    elif menu_entry_index == 12:
        exhibition = input()
        if exhibition == "Да":
            filter.exhibition = True
        elif restored == "Нет":
            filter.exhibition = False
        else:
            print("Повторите ввод: введите 'Да' или 'Нет'")
    elif menu_entry_index == 13:
        restored = input()
        if restored == "Да":
            filter.restored = True
        elif restored == "Нет":
            filter.restored = False
        else:
            print("Повторите ввод: введите 'Да' или 'Нет'")
    else:
        print("❗Перестаньте ломать программу❗")

    return filter


strategy = RecomendationStrategy.FilterFirst


def choose_recomendation_strategy(rec_system):
    choose_recomendation_strategy = ["RecomendFirst", "FilterFirst"]
    terminal_menu = TerminalMenu(choose_recomendation_strategy)
    menu_entry_index = terminal_menu.show()

    global strategy
    if menu_entry_index == 0:
        strategy = RecomendationStrategy.RecomendFirst
    elif menu_entry_index == 1:
        strategy = RecomendationStrategy.FilterFirst
    else:
        print("❗Перестаньте ломать программу❗")

    return 0


main_filter = Filter()

"Название картины",  # 0
"Полное имя писателя",  # 1
"Ширина картины",  # 2
"Высота картины",  # 3
"Цена",  # 4
"Век написания картины",  # 5
"Страна писателя",  # 6
"Стиль",  # 7
"Предмет картины",  # 8
"Жанр картины",  # 9
"Техника написания",  # 10
"Выставлена на обозрение (Да/Нет)",  # 11
"Для продажи (Да/Нет)",  # 12
"Реставрировалась (Да/Нет)"  # 13


def print_filter(filter: Filter):
    print("\n========= Filter =========")
    print("Название картины:", filter.name)
    print("Полное имя писателя:", filter.full_name)
    print("Ширина картины (max):", filter.width_max)
    print("Ширина картины (min):", filter.width_min)
    print("Высота картины (max):", filter.height_max)
    print("Высота картины (min):", filter.height_min)
    print("Цена (max):", filter.sale_price_max)
    print("Цена (min):", filter.sale_price_min)
    print("Век написания картины (max):", filter.century_max)
    print("Век написания картины (min):", filter.century_min)
    print("Страна писателя:", filter.country)
    print("Стиль:", filter.style)
    print("Предмет картины:", filter.subject)
    print("Жанр картины:", filter.genre)
    print("Техника написания:", filter.medium)
    print("Выставлена на обозрение (Да/Нет):", filter.exhibition)
    print("Для продажи (Да/Нет):", filter.for_sale)
    print("Реставрировалась (Да/Нет):", filter.restored)


def main_loop(rec_system: RecomendationSystem, likes, dislikes) -> int:
    global main_filter
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0:
        # print numerated list of all entries
        items = rec_system.query_all(None)
        for i, item in enumerate(items):
            liked = "" if i not in likes else "👍"
            disliked = "" if i not in dislikes else "👎"
            print(
                f"{i:2}) {liked:1} {disliked:1} {item.name}: price={item.sale_price}; genre={item.genre}; style={item.style}; subject={item.subject}"
            )
        return 0
    elif menu_entry_index == 1:
        # output matrix
        rec_system.visualize_matrix()
        return 0
    elif menu_entry_index == 2:
        # add entry to likes
        item_index = 0
        item_index_str = input()
        try:
            item_index = int(item_index_str)
        except:
            print("❗ Ну ты чего... Посмотри что ты вводишь ❗")
            return -1
        if item_index in dislikes:
            print("❗ В списке дизлайков уже есть такой индекс ❗")
            return -1
        elif item_index < 0 or item_index > len(rec_system.query_all(None)):
            print("❗ Индекс выходит за границы массива ❗")
        else:
            likes.append(item_index)
            print("✅ Картина добавлена в список лайков ✅")
        return 0
    elif menu_entry_index == 3:
        # delete entry from likes
        item_index = 0
        item_index_str = input()
        try:
            item_index = int(item_index_str)
        except:
            print("❗ Ну ты чего... Посмотри что ты вводишь ❗")
            return -1
        if not item_index in likes:
            print("❗В списке лайков нет такого индекса❗")
            return -1
        else:
            del likes[likes.index(item_index)]
            print("✅ Картина удалена из списка лайков ✅")
        return 0
    elif menu_entry_index == 4:
        # add entry to dislikes
        item_index = 0
        item_index_str = input()
        try:
            item_index = int(item_index_str)
        except:
            print("❗ Ну ты чего... Посмотри что ты вводишь ❗")
            return -1
        if item_index in dislikes:
            print("❗В списке лайков уже есть такой индекс❗")
            return -1
        elif item_index < 0 or item_index > len(rec_system.query_all(None)):
            print("❗ Индекс выходит за границы массива ❗")
        else:
            dislikes.append(item_index)
            print("✅ Картина добавлена в список дизлайков ✅")
        return 0
    elif menu_entry_index == 5:
        # delete entry from dislikes
        item_index = 0
        item_index_str = input()
        try:
            print("❗ Ну ты чего... Посмотри что ты вводишь ❗")
            item_index = int(item_index_str)
        except:
            return -1
        if not item_index in dislikes:
            print("❗В списке дизлайков нет такого индекса❗")
            return -1
        else:
            del likes[likes.index(item_index)]
            print("✅ Картина удалена из списка дизлайков ✅")
        return 0
    elif menu_entry_index == 6:
        # set filter
        main_filter = choose_set_filter(main_filter)
        return 0
    elif menu_entry_index == 7:
        main_filter = Filter()
        return 0
    elif menu_entry_index == 8:
        # output filter
        print_filter(main_filter)
        return 0
    elif menu_entry_index == 9:
        # set measure function
        return choose_measure_function(rec_system)
    elif menu_entry_index == 10:
        # set recomendation strategy
        return choose_recomendation_strategy(rec_system)
    elif menu_entry_index == 11:
        # give recomendation
        global strategy
        all_items = rec_system.query_all(None)
        likes = [item for (i, item) in enumerate(all_items) if i in likes]
        dislikes = [item for (i, item) in enumerate(all_items) if i in dislikes]

        items = []
        if strategy == RecomendationStrategy.FilterFirst:
            items = give_recomendation_filter_first_strategy(
                rec_system, likes=likes, dislikes=dislikes, filter=main_filter
            )
        elif strategy == RecomendationStrategy.RecomendFirst:
            items = give_recomendation_recomend_first_strategy(
                rec_system, likes=likes, dislikes=dislikes, filter=main_filter
            )
        for i, item in enumerate(items):
            print(
                f"{i:2}) {item.name}: price={item.sale_price}; genre={item.genre}; style={item.style}; subject={item.subject}"
            )
        return 0
    elif menu_entry_index == 12:
        # exit
        print("Выходим из этого злополучного уголка")
        return 1
    else:
        print(f"❗Выбран несуществующий пункт меню.❗")

    return 0
