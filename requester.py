#!/usr/bin/env python3
import time
import sys
from serial.serialutil import SerialException
from controller import get_logger
from social.devices import Arduino
from social.serial_protocol import SerialProtocol

SLEEP_MINUTES = 30

logger = get_logger("Requester")

arduinos = Arduino("api_endpoint")

while True:
    logger.info("Start loop...")
    for arduino in arduinos.all:
        protocol = SerialProtocol(arduino["port"])
        try:
            protocol.get_metrics()
        except SerialException:
            logger.error("Error connecting to port {}, trying in next {} minutes".format(
                protocol.serial_port, SLEEP_MINUTES
                ))
    time.sleep(60 * SLEEP_MINUTES)
    logger.info("End loop.")
