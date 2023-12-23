WANT = r"(?P<want>(хотеться|хотеть|нужно|нужный|надо|искать|есть))"

SHOW = r"(?P<show>(показать))"
CHANGE = r"(?P<change>(сменить|заменить|поменять|изменить|выбрать|установить))"
ADD = r"(?P<add>(установи|добавь))"
UNSET = r"(?P<set>(сбрось))"

SOME_PICTURE = r"(?P<some_picture>(картин(у)?|какую-нибудь картин(у)?))"
REC_STRATEGY = r"(?P<rec_strategy>(стратеги[юя]))"
REC_MEASURE = r"(?P<rec_measure>(мер[ау]))"
REC_FILTER = r"(?P<rec_filter>(фильтр))"

SIMILAR_TO = r"(?P<similar_to>(похожий|на подобие|аналог|тип))"
NOT_SIMILAT_TO = r"(?P<not_similar_to>(не похожий|отличный от))"

# ================== Main rules ==================

RULE_HELLO = r"(?P<rule_hello>([Пп]ривет))"

RULE_911 = r"(?P<rule_911>([Уу]бивать))"
RULE_PLAY_MUSIC = r"(?P<rule_music>([(теперь)] [Дд]ля души))"

RULE_RESET_SESSION = r"(?P<rule_reset_session>([Сс]брось (текущую)? сессию))"
RULE_RESET_HISTORY = r"(?P<rule_reset_history>([Сс]брось историю))"

RULE_SUGGEST_SOMETHING = r".*{}.*{}.*".format(SIMILAR_TO, SOME_PICTURE)
RULE_SUGGEST_LIKE_PICTURES = r".*{}(\s)*(?P<likes_list>(.*))".format(SIMILAR_TO)
RULE_SUGGEST_DISLIKE_PICTURES = r".*{}(\s)*(?P<dislikes_list>(.*)".format(NOT_SIMILAT_TO)

RULE_CHANGE_STRATEGY = r"(\s)*{}(\s)*{}(\s)*(?P<strategy_name>(.*))".format(CHANGE, REC_STRATEGY)
RULE_SHOW_STRATEGY = r".*{}.*{}.*".format(SHOW, REC_STRATEGY)
RULE_CHANGE_MEASURE = r"(\s)*{}(\s)*{}(\s)*(?P<measure_name>(.*))".format(CHANGE, REC_MEASURE)
RULE_SHOW_MEASURE = r".*{}.*{}.*".format(SHOW, REC_MEASURE)

RULE_ADD_FILTER = r"(\s)*{}(\s)*{}(\s)*(?P<filter_name>(.*))".format(ADD, REC_FILTER)
RULE_RESET_FILTER = r"(\s)*{}(\s)*{}(\s)*(?P<filter_name>(.*))".format(UNSET, REC_FILTER)
RULE_SHOW_FILTERS = r".*{}.*{}.*".format(SHOW, REC_FILTER)

# ================== Main rules ==================

RULES = [
    RULE_HELLO,
    RULE_911,
    RULE_PLAY_MUSIC,
    RULE_RESET_SESSION,
    RULE_RESET_HISTORY,
    RULE_SUGGEST_SOMETHING,
    RULE_SUGGEST_LIKE_PICTURES,
    RULE_SUGGEST_DISLIKE_PICTURES,
    RULE_CHANGE_STRATEGY,
    RULE_SHOW_STRATEGY,
    RULE_CHANGE_MEASURE,
    RULE_SHOW_MEASURE,
    RULE_ADD_FILTER,
    RULE_VALUE_FILTER,
    RULE_RESET_FILTER,
    RULE_SHOW_FILTERS,
]
