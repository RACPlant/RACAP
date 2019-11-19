#!/usr/bin/env python3
# run every 6 hours
from controller import get_logger
from controller.config import DEVICES_ENDPOINT, SLOTS_ENDPOINT
from controller.plants import Plants
from social.arduino import Devices, Slots
from database.knowledge_base import KnowledgeBase

logger = get_logger("Requester")

arduinos = Devices(DEVICES_ENDPOINT)
kb = KnowledgeBase()
kb.update_arduino_fact(arduinos)

for arduino in arduinos.all:

    slots = Slots(SLOTS_ENDPOINT, arduino["id"])
    plants = Plants(slots)
    plants.set_info()

    kb.add_plants_fact(arduino["id"], plants)

kb.update_plants_fact()
