rule(r_suggest_something, IM, A, IM, Z) :-
    suggest(A, B),
    something(B, Z).

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

rule(r_show_something_verbose, IM, A, IM, Z) :-
    show(A, B),
    recomendation(B, C),
    verbose(C, Z).
