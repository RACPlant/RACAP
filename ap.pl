loop :-
    read_serial(X),
    check(X),
    with_mutex(synch, (retractall(currentvalue(_)),
                       assertz(currentvalue(X)))),
    loop.
