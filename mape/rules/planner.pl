how_much_water(Arduino,Slot,Plant,Pump,Water):-
    plant(Arduino,Slot,Plant),
    slot(Arduino,Slot,_,Pump),
    eto_water(Plant,,_,Water).