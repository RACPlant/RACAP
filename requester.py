#!/usr/bin/env python3
import time
import sys
from controller import get_logger
from social.devices import Arduino
from social.serial_protocol import SerialProtocol

logger = get_logger("Requester")


arduinos = Arduino("api_endpoint")

while True:
    logger.info("Start loop...")
    for arduino in arduinos.all:
        protocol = SerialProtocol(arduino["port"])
        protocol.get_metrics()
    time.sleep(60*30)  # 30 minutes
    logger.info("End loop.")
