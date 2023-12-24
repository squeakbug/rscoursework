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
