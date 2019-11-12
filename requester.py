#!/usr/bin/env python3
import time
import sys
from controller import get_logger
from mape.analyzer import Analyzer
from mape.planner import Planner
from social.devices import Arduino
from social.serial_protocol import SerialProtocol

logger = get_logger("Requester")


analyzer = Analyzer()
planner = Planner()
arduinos = Arduino("api_endpoint")

while True:
    logger.info("Start loop...")
    for arduino in arduinos.all:
        protocol = SerialProtocol(arduino["port"])
        protocol.get_metrics()

        who_needs = analyzer.who_needs_water(arduino["id"])
        if who_needs:
            how_much = planner.how_much_water(arduino["id"], who_needs)
            
            for plant in how_much:
                protocol.water_in(plant["pump"], plant["time"])
                time.sleep(5)
    time.sleep(60*30) # 30 minutes
    logger.info("End loop.")
