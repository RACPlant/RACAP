#!/usr/bin/env python3
# run every 6 hours
from controller import get_logger
from controller.plants import Plants
from controller.social import Social
from database.knowledge_base import KnowledgeBase

logger = get_logger("Requester")

social = Social("api_endpoint")

for arduino in social.arduinos:

    plants = Plants(arduino)
    plants.set_info()

    kb = KnowledgeBase()
    kb.add_plants_fact(arduino, plants)

kb.update_plants_fact()