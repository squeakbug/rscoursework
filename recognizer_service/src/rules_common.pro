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
likes([понравившиеся | X], X).
dislikes([непонравившиеся | X], X).

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
