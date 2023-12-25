with([с | X], X).
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
change([изменить | X], X).

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
filters([фильтры | X], X).
similar([похожий | X], X).
measure([мера | X], X).
strategy([стратегия | X], X).
picture([картина | X], X).
pictures([картины | X], X).
writer([писатель | X], X).
writer([писатель, Name | X], Name, X).

only([только | X], X).
other([другой | X], X).
other([еще | X], X).
possible([возможный | X], X).
likes([понравившиеся | X], X).
dislikes([непонравившиеся | X], X).
eq([равный | X], X).
name([название | X], X).
name([название, Name | X], Name, X).

with_name(A, Name, Z) :-
    with(A, B),
    name(B, Name, Z).
filter_with_name(A, Name, Z) :-
    filter(A, B),
    with_name(B, Name, Z).
measure_to_name(A, Name, Z) :-
    measure(A, B),
    to(B, Name, Z).
strategy_to_name(A, Name, Z) :-
    strategy(A, B),
    to(B, Name, Z).

writer_name(A, Name, Z) :-
    writer(A, B),
    with(B, C),
    name(C, Name, Z).
writer_name(A, Name, Z) :-
    writer(A, Name, Z).

value([значение, Value | X], Value, X).
value_eq([значение, равный, Value | X], Value, X).

name_list([HNL, ',' | TA], [HNL | TNL], Z) :-
    name_list(TA, TNL, Z).
name_list([HNL1, и, HNL2 | Z], [HNL1, HNL2], Z).

%% Тесты

:- filter_with_name([фильтр, с, название, ширина], ширина, []).

:- value([значение, 10], 10, []).

name_list([привет, ',', привет, и, привет], [привет, привет, привет], []).
