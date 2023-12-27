with([с | X], X).
with([с, Object | X], Object, X).
to([на, Object | X], Object, X).

name_list([HNL, ',' | TA], [HNL | TNL], Z) :-
    name_list(TA, TNL, Z).
name_list([HNL, 'и' | TA], [HNL | TNL], Z) :-
    name_list(TA, TNL, Z).
name_list([HNL1, и, HNL2 | Z], [HNL1, HNL2], Z).
name_list([HNL1 | Z], [HNL1], Z).
name_list(Z, [], Z).

name_ws_list([HNL | TA], [HNL | TNL], Z) :-
    name_ws_list(TA, TNL, Z).
name_ws_list([HNL | Z], [HNL], Z).
name_ws_list(Z, [], Z).

no([не | X], X).
yes([да | X], X).
not([нет | X], X).

show([показать | X], X).
suggest([рекомендовать | X], X).
suggest([порекомендовать | X], X).
add([добавить | X], X).
set([установить | X], X).
reset([сбросить | X], X).
change([заменить | X], X).
change([изменить | X], X).
verbose([подробно | X], X).
verbose([подробный | X], X).

me([я | X], X).
like([нравиться | X], X).
hate([ненавидеть | X], X).
not_like([перестать, нравиться | X], X).
not_hate([перестать, ненавидеть | X], X).

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
something(['что-нибудь' | X], X).
recomendation([рекомендация | X], X).

only([только | X], X).
other([другой | X], X).
other([еще | X], X).
possible([возможный | X], X).
likes([понравившийся | X], X).
likes([лайк | X], X).
dislikes([непонравившийся | X], X).
dislikes([дизлайк | X], X).
eq([равно | X], X).
eq([равный | X], X).
eq([равно, Value | X], Value, X).
eq([равный, Value | X], Value, X).
name([название | X], X).
name([название, Name | X], Name, X).
value([значение | X], X).

with_name(A, Name, Z) :-
    with(A, B),
    name(B, Name, Z).
filter_with_name(A, Name, Z) :-
    filter(A, B),
    with_name(B, Name, Z).
with_name_ws_list(A, NameList, Z) :-
    with(A, B),
    name(B, C),
    name_ws_list(C, NameList, Z).
filter_with_name_list(A, NameList, Z) :-
    filter(A, B),
    with_name_ws_list(B, NameList, Z).
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

%% Тесты

:- filter_with_name([фильтр, с, название, ширина], ширина, []).

:- value([значение, 10], 10, []).

:- name_list([привет, ',', привет, и, привет], [привет, привет, привет], []).
:- with_name_ws_list([с, название, муад, даби], [муад, даби], []).
:- filter_with_name_list([фильтр, с, название, муад, даби], [муад, даби], []).