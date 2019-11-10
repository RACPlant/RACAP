#!/usr/bin/env python3
import time
import sys
from controller.protocol import Protocol
from controller import get_logger
from mape.analyzer import Analyzer
from mape.planner import Planner
logger = get_logger("Requester")


protocol = Protocol(sys.argv)
analyzer = Analyzer()
planner = Planner()

while True:
    logger.info("Start loop...")
    protocol.get_metrics()

    who_needs = analyzer.who_needs_water()
    if who_needs:
        how_much = planner.how_much_water(who_needs)
        
        for plant in how_much:
            protocol.water_in(plant["arduino"], plant["pump"], plant["time"])
            time.sleep(5)
    time.sleep(60*30) # 30 minutes
    logger.info("End loop.")
