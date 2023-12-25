%% Separate the lexicon from the grammar.
%% In programming languages, these would be part of the lexer/scanner, and would be considered the
%% reserved keywords.
%% Since we are just parsing English, then this is the English dictionary!
lex(the, determiner).
lex(a, determiner).
lex(woman, noun).
lex(man, noun).
lex(shoots, verb).
lex(and, conjunction).
lex(or, conjunction).
lex(but, conjunction).
lex(he, pronoun(subject)).
lex(she, pronoun(subject)).
lex(him, pronoun(object)).
lex(her, pronoun(object)).

%% This shows induction and base case, left recursion elimination, recursive linked-list parse tree
%% The `statement` can take the form of: 
%% `statement(basic_statement, statement(...))` or 
%% `statement(conjunction, basic_statement, statement(...))` or 
%% `statement(epsilon)`
statement(statement(S, SS))         --> basic_statement(S), statement_rest(SS).
statement_rest(statement(E))        --> epsilon(E).
statement_rest(statement(C, S, SS)) --> conjunction(C), basic_statement(S), statement_rest(SS).

basic_statement(basic_statement(NP, VP)) --> noun_phrase(subject, NP), verb_phrase(VP).

%% `Position` is an inherited attribute.
noun_phrase(Position, noun_phrase(P))    --> pronoun(Position, P).
noun_phrase(_,        noun_phrase(D, N)) --> determiner(D), noun(N).

verb_phrase(verb_phrase(V, NP)) --> verb(V), noun_phrase(object, NP).
verb_phrase(verb_phrase(V))     --> verb(V).

conjunction(conjunction(Word)) --> [Word], { lex(Word, conjunction) }.

%% Differentiate subject pronouns from object pronouns using the `Position` inherited attribute
pronoun(Position, pronoun(Word)) --> [Word], { lex(Word, pronoun(Position)) }.

determiner(determiner(Word)) --> [Word], { lex(Word, determiner) }.

noun(noun(Word)) --> [Word], { lex(Word, noun) }.

verb(noun(Word)) --> [Word], { lex(Word, verb) }.

epsilon(epsilon) --> [].
