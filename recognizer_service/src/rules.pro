% =========================================
% А если только частичное совпадение фразы?
% А если фраза совпала посередине, а вокруг бред?
% =========================================

:-include('rules_common.pro').
:-include('rules_filter.pro').
:-include('rules_likes.pro').
:-include('rules_other.pro').
:-include('rules_reset.pro').
:-include('rules_strategy_measure.pro').
:-include('rules_suggestion.pro').

main_rule(RuleName, OM, Sentence) :-
    rule(RuleName, OM, Sentence, _{}, []).

main_rule(unknown, _{}, _).
