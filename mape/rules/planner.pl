eto_calc(Vr,Vt,Eto):-
    round(0.0135*Vr*(Vt+17.8), Eto).

how_much_water(Arduino,Slot,Plant,Pump,Water):-
    plant(Arduino,Slot,Plant),
    slot(Arduino,Slot,_,Pump),
    is_radiation(Arduino, R),
    is_temperature(Arduino, T),
    sensor(Arduino,R,_,_,_,Vr),
    sensor(Arduino,T,_,_,_,Vt),
    eto_calc(Vr,Vt,Eto),
    eto_water(Plant,Eto,_,Water).