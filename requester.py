#!/usr/bin/env python3
import time
import os
from serial.serialutil import SerialException
from controller import get_logger
from controller.config import DEVICES_ENDPOINT
from social.arduino import Devices
from social.serial_protocol import SerialProtocol

SLEEP_SECONDS = os.environ.get("WAIT_TIME",15)

logger = get_logger("Requester")

arduinos = Devices(DEVICES_ENDPOINT)

while True:
    logger.info("Waiting {} seconds".format(SLEEP_SECONDS))
    time.sleep(SLEEP_SECONDS)
    logger.info("Start loop...")
    for arduino in arduinos.all:
        protocol = SerialProtocol(arduino["port"])
        try:
            protocol.get_metrics()
        except SerialException:
            logger.error("Error connecting to port {}, trying in next {} seconds".format(
                protocol.serial_port, SLEEP_SECONDS
            ))
    logger.info("End loop.")
