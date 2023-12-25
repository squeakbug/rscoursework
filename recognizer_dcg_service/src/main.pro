:- module(server,
      [ server/1            % ?Port
]).


:- use_module(library(http/thread_httpd)).
:- use_module(library(http/http_dispatch)).
:- use_module(library(http/http_error)).
:- use_module(library(http/http_json)).
:- use_module(library(http/http_parameters)).
:- use_module(library(http/http_path)).
:- use_module(library(http/http_files)).
:- use_module(library(http/http_unix_daemon)). % Если не подключить, то сервер после запуска будет сразу завершаться
:- use_module(library(http/http_log)).
:- use_module(library(http/http_server_files)).
:- use_module(library(http/http_dyn_workers)).

:-include('rules.pro').

% ===== Includes =====

%% select_rule_handler

:- http_handler(root(api/v1/rule_recognizer), select_rule_handler, []).

parse_rule_request(Body, Sentence) :-
    Body = json(
        [
            tokens = Sentence
        ]
    ).

select_rule_handler(Request):-
    http_parameters(Request, []),
    http_read_json(Request, Body, [json_object(term)]),
    parse_rule_request(Body, Sentence),
    format(user_output,"Sentence is: ~p~n", [Sentence]),
    main_rule(RuleName, OM, Sentence),
    reply_json(
        json{
            rule_name: RuleName,
            matchings: OM 
        }
    ).

select_rule_handler(_Request):-
    reply_json(json{status:'error'}).

%% healthcheck

:- http_handler(root(manage/healthcheck), healthcheck_handler, []).

healthcheck_handler(Request):-
    http_parameters(Request, []),
    reply_json(json{status:'ok'}).

healthcheck_handler(_Request):-
    reply_json(json{status:'error'}).

% ===== Main =====

server(Port) :-
    http_server(http_dispatch,
                [ port(Port),
                  workers(16)
                ]).
