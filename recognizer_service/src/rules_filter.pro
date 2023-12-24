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
