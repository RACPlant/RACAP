should_water(Arduino,Plant,Slot):-
    plant(Arduino,Slot,Plant),
    slot(Arduino,Slot,H,_),
    sensor(Arduino,H,V,_,_,_),
    V<400.