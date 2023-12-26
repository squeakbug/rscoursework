set_or_add(A, Z) :-
    set(A, Z);
    add(A, Z).

rule(r_add_filter, OM, A, IM, Z) :-
    set_or_add(A, B),
    filter_with_name_list(B, Name, Z),
    OM = IM.put(filter_name, Name).

rule(r_add_filter_with_value, OM, A, IM, Z) :-
    set_or_add(A, B),
    filter_with_name_list(B, Name, C),
    with(C, D),
    value_eq(D, Value, Z),
    OM1 = IM.put(filter_name, Name),
    OM = OM1.put(filter_value, Value).

rule(r_add_filter_with_value, OM, A, IM, Z) :-
    set_or_add(A, B),
    filter_with_name_list(B, Name, C),
    with(C, D),
    value(D, Value, Z),
    OM1 = IM.put(filter_name, Name),
    OM = OM1.put(filter_value, Value).

rule(r_reset_filter, OM, A, IM, Z) :-
    reset(A, B),
    filter_with_name_list(B, Name, Z),
    OM = IM.put(filter_name, Name).

rule(r_show_filters, IM, A, IM, Z) :-
    show(A, B),
    filters(B, Z).

rule(r_show_filters, IM, A, IM, Z) :-
    show(A, B),
    filter(B, Z).

rule(r_filter_value_eq, OM, A, IM, Z) :-
    value(A, B),
    filter(B, C),
    eq(C, Value, Z),
    OM = IM.put(filter_value, Value).
