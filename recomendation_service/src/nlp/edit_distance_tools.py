from nltk.metrics.distance import jaro_winkler_similarity as edit_distance


def get_most_similar_base(user_input: str, patterns: list):
    dists = [(i, edit_distance(user_input, pattern)) for (i, pattern) in enumerate(patterns)]
    max_indx = max(dists, key=lambda x: x[1])
    return patterns[max_indx[0]]


def get_most_similar_country(user_country: str):
    countries = ["Америка", "Россия", "Великобритания", "Испания", "Франция"]
    return get_most_similar_base(user_country, countries)


def replace_country(user_input: str):
    countries_dict = {
        "Америка": "USA",
        "Россия": "Russia",
        "Великобритания": "United Kingdom",
        "Испания": "Spain",
        "Франция": "France",
    }
    return countries_dict[get_most_similar_country(user_input)]


def get_most_similar_genre(user_genre: str):
    genres = [
        "портрет",
        "пейзаж",
        "натюрморт",
        "автопортрет",
        "исторический портрет",
        "посмертный портрет",
        "религиозный портрет",
        "марин",
        "индустриальный пейзаж",
        "исторический пейзаж",
        "вымышленный пейзаж",
        "ландшафт",
        "цветочно-фруктовый",
        "кухонный натюрморт",
        "vanitas",
        "груповой портрет",
        "раздельный портрет",
        "исторические события",
        "исторические персонажи",
        "религиозные события",
        "религиозные персонажи",
        "открытое море",
        "побережье",
        "реки/озера",
        "мосты",
        "резиденции",
        "чудеса света",
        "часы",
        "человеческий череп",
        "доспехи",
        "настольные игры",
    ]
    return get_most_similar_base(user_genre, genres)


def replace_genre(user_input: str):
    genres_dict = {
        "портрет": "Portrait",
        "пейзаж": "Scenery",
        "натюрморт": "Still-life",
        "автопортрет": "Self-portrait",
        "исторический портрет": "Historical portrait",
        "посмертный портрет": "Posthumous portrait",
        "религиозный портрет": "Religious portrait",
        "марин": "Marinus",
        "индустриальный пейзаж": "Industrial",
        "исторический пейзаж": "Historical",
        "вымышленный пейзаж": "Fantasy",
        "ландшафт": "Landscape",
        "цветочно-фруктовый": "Floral-fruity",
        "кухонный натюрморт": "Kitchen",
        "vanitas": "Vanitas",
        "груповой портрет": "Group portrait",
        "раздельный портрет": "Separate",
        "исторические события": "Historical Events",
        "исторические персонажи": "Historical characters",
        "религиозные события": "Religious Events",
        "религиозные персонажи": "Religious characters",
        "открытое море": "Open sea",
        "побережье": "Coast",
        "реки/озера": "Rivers/Lakes",
        "мосты": "Bridges",
        "резиденции": "Residential buildings",
        "чудеса света": "Sights",
        "часы": "Clocks",
        "человеческий череп": "Human scull",
        "доспехи": "Steel arms",
        "настольные игры": "Table games",
    }
    return genres_dict[get_most_similar_genre(user_input)]


def get_most_similar_subject(user_subject: str):
    subjects = [
        "портреты",
        "натюрморты",
        "обнаженное",
        "абстрактное",
        "марин",
        "ландшафт",
        "реки/озера",
        "сады",
    ]
    return get_most_similar_base(user_subject, subjects)


def replace_subject(user_input: str):
    subjects_dict = {
        "портреты": "Portraits",
        "натюрморты": "Still-Life",
        "обнаженное": "Nude",
        "абстрактное": "Abstract/Modern Art",
        "марин": "Marine Art/Maritime",
        "ландшафт": "Landscape Art",
        "реки/озера": "Rivers/Lakes",
        "сады": "Gardens",
    }
    return subjects_dict[get_most_similar_subject(user_input)]


def get_most_similar_style(user_subject: str):
    styles = [
        "импрессионизм",
        "пост-импрессионизм",
        "барокко",
        "кубизм",
        "ренессанс",
        "рококо",
        "классицизм",
        "американский ландшафт",
        "экспрессионизм",
        "романтизм",
        "модерн",
        "реализм",
    ]
    return get_most_similar_base(user_subject, styles)


def replace_style(user_input: str):
    styles_dict = {
        "импрессионизм": "Impressionism",
        "пост-импрессионизм": "Post-Impressionism",
        "барокко": "Baroque",
        "кубизм": "Cubism",
        "ренессанс": "Renaissance",
        "рококо": "Rococo",
        "классицизм": "Classicism",
        "американский ландшафт": "American Landscape",
        "экспрессионизм": "Expressionism",
        "романтизм": "Romanticism",
        "модерн": "Art Nouveau",
        "реализм": "Realism",
    }
    return styles_dict[get_most_similar_style(user_input)]


def get_most_similar_medium(user_medium: str):
    mediums = ["масло", "карандаш", "акварель", "сухая кисть"]
    return get_most_similar_base(user_medium, mediums)


def replace_medium(user_input: str):
    mediums_dict = {
        "масло": "Oil on canvas",
        "карандаш": "Pencil",
        "акварель": "Watercolor",
        "сухая кисть": "Drybrush",
    }
    return mediums_dict[get_most_similar_medium(user_input)]


def get_most_similar_measure_function_name(user_input: str):
    measure_func_names = ["общаяя", "деньги прежде всего"]
    return get_most_similar_base(user_input, measure_func_names)


def replace_measure_function_name(user_input: str):
    measure_function_names_dict = {
        "общаяя": "General-driven",
        "деньги прежде всего": "Money-driven",
    }
    return measure_function_names_dict[get_most_similar_measure_function_name(user_input)]


def get_most_similar_strategy_name(user_input: str):
    strategies_names = ["рекомендация вначале", "фильтрация вначале"]
    return get_most_similar_base(user_input, strategies_names)


def replace_strategy_name(user_input: str):
    strategy_names_dict = {
        "рекомендация вначале": "RecomendFirst",
        "фильтрация вначале": "FilterFirst",
    }
    return strategy_names_dict[get_most_similar_strategy_name(user_input)]


def get_most_similar_filter_name(user_input: str):
    filter_names = [
        "название картины",
        "имя писателя",
        "минимальная ширина картины",
        "максимальная ширина картины",
        "минимальная высота картины",
        "максимальная высота картины",
        "минимальная цена",
        "максимальная цена",
        "минимальный век написания",
        "максимальный век написания",
        "страна",
        "стиль",
        "предмет",
        "жанр",
        "техника",
        "выставлена на обозрение",
        "для продажи",
        "реставрирована",
    ]
    return get_most_similar_base(user_input, filter_names)


def replace_filter_name(user_input: str):
    strategy_names_dict = {
        "название картины": "name",
        "имя писателя": "full_name",
        "минимальная ширина картины": "width_min",
        "максимальная ширина картины": "width_max",
        "минимальная высота картины": "height_min",
        "максимальная высота картины": "height_max",
        "минимальная цена": "sale_price_min",
        "максимальная цена": "sale_price_max",
        "минимальный век написания": "century_min",
        "максимальный век написания": "century_max",
        "страна": "country",
        "стиль": "style",
        "предмет": "subject",
        "жанр": "genre",
        "техника": "medium",
        "выставлена на обозрение": "exhibition",
        "для продажи": "for_sale",
        "реставрирована": "restored",
    }
    return strategy_names_dict[get_most_similar_filter_name(user_input)]


def get_most_similar_picture_name(user_input: str, picture_names: list):
    return get_most_similar_base(user_input, picture_names)


def replace_picture_name(user_input: str):
    return get_most_similar_picture_name(user_input)


if __name__ == "__main__":
    print(f"Start tests in {__file__}")
    assert replace_country("Расия") == "Russia"
    assert replace_country("Америка") == "USA"
    assert replace_genre("vanitas") == "Vanitas"
    assert replace_genre("побережье") == "Coast"
    assert replace_subject("реки/озера") == "Rivers/Lakes"
    assert replace_subject("обнаженка") == "Nude"
    assert replace_style("барока") == "Baroque"
    assert replace_style("мадер") == "Art Nouveau"
    assert replace_medium("макварель") == "Watercolor"
    assert replace_medium("корандашь") == "Pencil"
    print(f"[SUCC] End tests in {__file__}")
