#!/usr/bin/env python3
# run every 6 hours
from controller import get_logger
from controller.config import DEVICES_ENDPOINT, SLOTS_ENDPOINT
from controller.plants import Plants
from social.arduino import Devices, Slots
from database import DatabasePlant, DatabaseArduino

logger = get_logger("Requester")

arduinos = Devices(DEVICES_ENDPOINT)
db_plants = DatabasePlant()

db_arduino = DatabaseArduino()
db_arduino.add_arduino_fact(arduinos)
db_arduino.update_database()

for arduino in arduinos.all:

    slots = Slots(SLOTS_ENDPOINT, arduino["id"])
    plants = Plants(slots)
    plants.set_info()

    db_plants.add_plants_fact(arduino["id"], plants)

db_plants.update_database()
