with([с, Object | X], Object, X).
to([на, Object | X], Object, X).

no([не | X], X).
yes([да | X], X).
not([нет | X], X).

show([показать | X], X).
suggest([рекомендовать | X], X).
add([добавить | X], X).
set([установить | X], X).
reset([сбросить | X], X).
change([заменить | X], X).

me([я | X], X).
like([нравиться | X], X).
hate([ненавижу | X], X).
not_like(A, Z) :-
    no(A, B),
    like(B, Z).
not_hate(A, Z) :-
    no(A, B),
    hate(B, Z).

session([сессия | X], X).
current([текущий | X], X).
history([история | X], X).
filter([фильтр | X], X).
similar([похожий | X], X).
measure([мера | X], X).
strategy([стратегия | X], X).
other([другой | X], X).
other([еще | X], X).

with_name(A, Name, Z) :-
    with(A, Name, Z).
filter_with_name(A, Name, Z) :-
    filter(A, B),
    with_name(B, Name, Z).
measure_to_name(A, Name, Z) :-
    measure(A, B),
    to(B, Name, Z).
strategy_to_name(A, Name, Z) :-
    strategy(A, B),
    to(B, Name, Z).

name_list([HNL, ',' | TA], [HNL | TNL], Z) :-
    name_list(TA, TNL, Z).
name_list([HNL, и | Z], [HNL | _], Z).

% =========================================
% А если только частичное совпадение фразы?
% А если фраза совпала посередине, а вокруг бред?
% =========================================

main_rule(RuleName, OM, Sentence) :-
    rule(RuleName, OM, Sentence, _{}, []).

% ================ Фильтры ================

rule(r_add_filter, OM, A, IM, Z) :-
    add(A, B),
    filter_with_name(B, Name, Z),
    OM = IM.put(filter_name, Name).

rule(r_reset_filter, OM, A, IM, Z) :-
    reset(A, B),
    filter_with_name(B, Name, Z),
    OM = IM.put(filter_name, Name).

rule(r_show_filters, IM, A, IM, Z) :-
    show(A, B),
    filters(B, Z).

% ======== Порекомендуй что-нибудь ========

rule(r_suggest_something, OM, A, IM, Z) :-
    suggest(A, B),
    similar(B, C),
    to(C, Suggestion, Z),
    OM = IM.put(suggestion, Suggestion).

rule(r_suggest_something, OM, A, IM, Z) :-
    show(A, B),
    similar(B, C),
    to(C, Suggestion, Z),
    OM = IM.put(suggestion, Suggestion).

rule(r_show_other, IM, A, IM, Z) :-
    show(A, B),
    other(B, Z).

rule(r_suggest_like_pictures, OM, A, IM, Z) :-
    similar(A, B),
    to(B, Name, Z),
    OM = IM.put(suggestion, Name).

rule(r_suggest_dislike_pictures, OM, A, IM, Z) :-
    similar(A, B),
    to(B, Name, Z),
    OM = IM.put(suggestion, Name).

% ======== Стратегия и мера ========

rule(r_change_strategy, OM, A, IM, Z) :-
    change(A, B),
    strategy_to_name(B, Name, Z),
    OM = IM.put(strategy_name, Name).

rule(r_show_strategy, IM, A, IM, Z) :-
    show(A, B),
    strategy(B, Z).

rule(r_change_measure, OM, A, IM, Z) :-
    change(A, B),
    measure_to_name(B, Name, Z),
    OM = IM.put(measure_name, Name).

rule(r_show_measure, IM, A, IM, Z) :-
    show(A, B),
    measure(B, Z).

% ======== Лайки/Дизлайки ========

rule(r_name_list, OM, A, IM, Z) :-
    name_list(A, Names, Z),
    OM = IM.put(name_list, Names).

%% Установка лайков

rule(r_like_writer, OM, A, IM, Z) :-
    me(A, B),
    like(B, C),
    picturers(C, D),
    writer_name(D, Name, Z),
    OM = IM.put(writer_name, Name).

rule(r_like_only, OM, A, IM, Z) :-
    like(A, B),
    only(B, C),
    name_list(C, Names, Z),
    OM = IM.put(picture_name_list, Names).

rule(r_like_only, OM, A, IM, Z) :-
    me(A, B),
    like(B, C),
    picturers(C, D),
    name_list(D, Names, Z),
    OM = IM.put(picture_name_list, Names).

%% Установка дизлайков

rule(r_hate_writer, OM, A, IM, Z) :-
    me(A, B),
    hate(B, C),
    picturers(C, D),
    writer_name(D, Name, Z),
    OM = IM.put(writer_name, Name).

rule(r_hate_only, OM, A, IM, Z) :-
    hate(A, B),
    only(B, C),
    name_list(C, Names, Z),
    OM = IM.put(picture_name_list, Names).

rule(r_hate_picturers, OM, A, IM, Z) :-
    me(A, B),
    hate(B, C),
    picturers(C, D),
    name_list(D, Names, Z),
    OM = IM.put(picture_name_list, Names).

%% Сброс лайков

rule(r_not_like_writer, OM, A, IM, Z) :-
    me(A, B),
    not_like(B, C),
    picturers(C, D),
    writer_name(D, Name, Z),
    OM = IM.put(writer_name, Name).

rule(r_not_like_only, OM, A, IM, Z) :-
    not_like(A, B),
    only(B, C),
    name_list(C, Names, Z),
    OM = IM.put(picture_name_list, Names).

rule(r_not_like_only, OM, A, IM, Z) :-
    me(A, B),
    not_like(B, C),
    picturers(C, D),
    name_list(D, Names, Z),
    OM = IM.put(picture_name_list, Names).

%% Сброс дизлайков

rule(r_like_writer, OM, A, IM, Z) :-
    me(A, B),
    not_hate(B, C),
    picturers(C, D),
    writer_name(D, Name, Z),
    OM = IM.put(picture_name_list, Name).

rule(r_like_only, OM, A, IM, Z) :-
    not_hate(A, B),
    only(B, C),
    name_list(C, Names, Z),
    OM = IM.put(picture_name_list, Names).

rule(r_like_only, OM, A, IM, Z) :-
    me(A, B),
    not_hate(B, C),
    picturers(C, D),
    name_list(D, Names, Z),
    OM = IM.put(picture_name_list, Names).

% ======== Другая мета ========

rule(r_reset_session, IM, A, IM, Z) :-
    reset(A, B),
    session(B, Z).
rule(r_reset_session, IM, A, IM, Z) :-
    reset(A, B),
    current(B, C),
    session(C, Z).

rule(r_reset_history, IM, A, IM, Z) :-
    reset(A, B),
    history(B, Z).

% ======== Вне домена ========

rule(r_hello, IM, [привет|X], IM, X). 
rule(r_hello, IM, [здравствуйте|X], IM, X).

rule(r_911, IM, [убивать|X], IM, X).

rule(r_for_pleasure, IM, [а,теперь,для,души|X], IM, X).
