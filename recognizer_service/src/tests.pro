:-include('rules.pro').

:- rule(r_hello, _{}, [привет], _{}, []).

:- rule(r_change_strategy,
        _{strategy_name: driven}, 
        [заменить, стратегия, на, driven], 
        _{},
        []
    ).
:- rule(r_show_strategy,
        _{}, 
        [показать, стратегия], 
        _{},
        []
    ).
:- rule(r_change_measure,
        _{measure_name: driven},  
        [заменить, мера, на, driven], 
        _{},
        []
    ).
:- rule(r_show_measure,
        _{}, 
        [показать, мера], 
        _{},
        []
    ).

:- rule(r_add_filter_with_value,
        _{filter_name: 'ширина', filter_value: '10'}, 
        [добавить, фильтр, с, название, ширина, с, значение, равный, '10'], 
        _{},
        []
    ).

:- rule(r_add_filter_with_value,
        _{filter_name: 'ширина', filter_value: '10'}, 
        [добавить, фильтр, с, название, ширина, с, значение, '10'], 
        _{},
        []
    ).

:- rule(r_like_only,
        _{picture_name_list: [дюна, махди]}, 
        [я, нравиться, картины, 'дюна', и, 'махди'], 
        _{},
        []
    ).
:- rule(r_like_writer,
        _{writer_name:'Рембрандт'}, 
        [я, нравиться, картины, писатель, 'Рембрандт'], 
        _{},
        []
    ).
