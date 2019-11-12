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
        logger.info("send getMetrics message")
        who_needs = analyzer.who_needs_water(arduino["id"])
        logger.info("who_needs_water return: {}".format(who_needs))
        if who_needs:
            how_much = planner.how_much_water(arduino["id"], who_needs)
            logger.info("how_much_water return: {}".format(how_much))

            for plant in how_much:
                protocol.water_in(plant["Pump"], plant["Water"])
                logger.info("Water in pump: {}, time: {}".format(
                    plant["Pump"], plant["Water"]))
                time.sleep(5)
    time.sleep(60*30)  # 30 minutes
    logger.info("End loop.")
