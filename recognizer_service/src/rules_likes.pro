%rule(r_name_list, OM, A, IM, Z) :-
%    name_list(A, Names, Z),
%    OM = IM.put(name_list, Names).

%% Установка лайков

rule(r_like_writer, OM, A, IM, Z) :-
    me(A, B),
    like(B, C),
    picture(C, D),
    writer_name(D, Name, Z),
    OM = IM.put(writer_name, Name).

rule(r_like_only, OM, A, IM, Z) :-
    like(A, B),
    only(B, C),
    name_ws_list(C, Names, Z),
    OM = IM.put(picture_name_list, Names).

rule(r_like_only, OM, A, IM, Z) :-
    me(A, B),
    like(B, C),
    picture(C, D),
    name_ws_list(D, Names, Z),
    OM = IM.put(picture_name_list, Names).

%% Установка дизлайков

rule(r_hate_writer, OM, A, IM, Z) :-
    me(A, B),
    hate(B, C),
    picture(C, D),
    writer_name(D, Name, Z),
    OM = IM.put(writer_name, Name).

rule(r_hate_only, OM, A, IM, Z) :-
    hate(A, B),
    only(B, C),
    name_ws_list(C, Names, Z),
    OM = IM.put(picture_name_list, Names).

rule(r_hate_picturers, OM, A, IM, Z) :-
    me(A, B),
    hate(B, C),
    picture(C, D),
    name_ws_list(D, Names, Z),
    OM = IM.put(picture_name_list, Names).

%% Сброс лайков

rule(r_not_like_writer, OM, A, IM, Z) :-
    me(A, B),
    not_like(B, C),
    picture(C, D),
    writer_name(D, Name, Z),
    OM = IM.put(writer_name, Name).

rule(r_not_like_only, OM, A, IM, Z) :-
    not_like(A, B),
    only(B, C),
    name_ws_list(C, Names, Z),
    OM = IM.put(picture_name_list, Names).

rule(r_not_like_only, OM, A, IM, Z) :-
    me(A, B),
    not_like(B, C),
    picture(C, D),
    name_ws_list(D, Names, Z),
    OM = IM.put(picture_name_list, Names).

%% Сброс дизлайков

rule(r_not_hate_writer, OM, A, IM, Z) :-
    me(A, B),
    not_hate(B, C),
    picture(C, D),
    writer_name(D, Name, Z),
    OM = IM.put(writer_name, Name).

rule(r_not_hate_only, OM, A, IM, Z) :-
    not_hate(A, B),
    only(B, C),
    name_ws_list(C, Names, Z),
    OM = IM.put(picture_name_list, Names).

rule(r_not_hate_picturers, OM, A, IM, Z) :-
    me(A, B),
    not_hate(B, C),
    picture(C, D),
    name_ws_list(D, Names, Z),
    OM = IM.put(picture_name_list, Names).


%% Показать лайки

rule(r_show_likes, IM, A, IM, Z) :-
    show(A, B),
    me(B, C),
    likes(C, Z).

rule(r_show_likes, IM, A, IM, Z) :-
    show(A, B),
    likes(B, Z).

%% Показать дизлайки

rule(r_show_dislikes, IM, A, IM, Z) :-
    show(A, B),
    me(B, C),
    dislikes(C, Z).

rule(r_show_dislikes, IM, A, IM, Z) :-
    show(A, B),
    dislikes(B, Z).
