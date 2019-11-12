should_water(Plant,Arduino,Pump):-
    plant(Plant,Arduino,H,Pump),
    sensor(Arduino,H,V,_,_,_),
    V<400.