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

:- rule(r_add_filter,
        _{filter_name: ['ширина', 'картины']}, 
        [добавить, фильтр, с, название, ширина, картины], 
        _{},
        []
    ).
:- rule(r_add_filter_with_value,
        _{filter_name: ['ширина'], filter_value: '10'}, 
        [добавить, фильтр, с, название, ширина, с, значение, равный, '10'], 
        _{},
        []
    ).
:- rule(r_add_filter_with_value,
        _{filter_name: ['ширина'], filter_value: '10'}, 
        [добавить, фильтр, с, название, ширина, с, значение, '10'], 
        _{},
        []
    ).
:- rule(r_add_filter_with_value,
        _{filter_name: ['ширина', 'картины'], filter_value: '10'}, 
        [добавить, фильтр, с, название, ширина, картины, с, значение, '10'], 
        _{},
        []
    ).
:- rule(r_filter_value_eq,
        _{filter_value: '10'},
        [значение, фильтр, равный, '10'],
        _{},
        []).

:- rule(r_hate_writer,
        _{writer_name:'Рембрандт'}, 
        [я, ненавидеть, картина, писатель, 'Рембрандт'], 
        _{},
        []
    ).
:- rule(r_hate_only,
        _{picture_name_list: [харконнен]},
        [ненавидеть, только, харконнен], 
        _{},
        []
    ).
:- rule(r_like_only,
        _{picture_name_list: [фримены]},
        [нравиться, только, фримены], 
        _{},
        []
    ).
:- rule(r_not_hate_only,
        _{picture_name_list: [фримены]},
        [перестать, ненавидеть, только, фримены], 
        _{},
        []
    ).
:- rule(r_not_like_only,
        _{picture_name_list: [фримены]},
        [перестать, нравиться, только, фримены], 
        _{},
        []
    ).
:- rule(r_hate_picturers, 
        _{picture_name_list: [тест]},
        [я, ненавидеть, картина, тест],
        _{},
        []
    ).
:- rule(r_hate_picturers, 
        _{picture_name_list: [изгой, из, ада]},
        [я, ненавидеть, картина, изгой, из, ада],
        _{},
        []
    ).
:- rule(r_like_only,
        _{picture_name_list: [дюна, махди]}, 
        [я, нравиться, картина, 'дюна', 'махди'], 
        _{},
        []
    ).
:- rule(r_like_writer,
        _{writer_name:'Рембрандт'}, 
        [я, нравиться, картина, писатель, 'Рембрандт'], 
        _{},
        []
    ).
:- rule(r_not_like_only,
        _{picture_name_list: [дюна, махди]}, 
        [я, перестать, нравиться, картина, 'дюна', 'махди'], 
        _{},
        []
    ).
:- rule(r_not_like_writer,
        _{writer_name:'Рембрандт'}, 
        [я, перестать, нравиться, картина, писатель, 'Рембрандт'], 
        _{},
        []
    ).
:- rule(r_not_hate_picturers,
        _{picture_name_list: [дюна, махди]},
        [я, перестать, ненавидеть, картина, 'дюна', 'махди'], 
        _{},
        []
    ).
:- rule(r_not_hate_writer,
        _{writer_name:'Рембрандт'}, 
        [я, перестать, ненавидеть, картина, писатель, 'Рембрандт'], 
        _{},
        []
    ).

:- rule(r_suggest_something,
        _{},
        [рекомендовать, 'что-нибудь'],
        _{},
        []
    ).
:- rule(r_show_something_verbose,
        _{},
        [показать, рекомендация, подробно],
        _{},
        []
    ).