#!/usr/bin/env python3
# run every 6 hours
from controller import get_logger
from controller.plants import Plants
from social.devices import Arduino
from database.knowledge_base import KnowledgeBase

logger = get_logger("Requester")

arduinos = Arduino("api_endpoint")

for arduino in arduinos.all:

    plants = Plants(arduino["id"])
    plants.set_info()

    kb = KnowledgeBase()
    kb.add_plants_fact(arduino["id"], plants)

kb.update_plants_fact()
