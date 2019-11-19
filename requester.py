#!/usr/bin/env python3
import time
import sys
from serial.serialutil import SerialException
from controller import get_logger
from controller.config import DEVICES_ENDPOINT
from social.arduino import Devices
from social.serial_protocol import SerialProtocol

SLEEP_MINUTES = 2

logger = get_logger("Requester")

arduinos = Devices(DEVICES_ENDPOINT

while True:
    logger.info("Waiting {} minutes".format(SLEEP_MINUTES))
    time.sleep(60 * SLEEP_MINUTES)
    logger.info("Start loop...")
    for arduino in arduinos.all:
        protocol=SerialProtocol(arduino["port"])
        try:
            protocol.get_metrics()
        except SerialException:
            logger.error("Error connecting to port {}, trying in next {} minutes".format(
                protocol.serial_port, SLEEP_MINUTES
            ))
    logger.info("End loop.")
