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