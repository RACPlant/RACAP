#!/usr/bin/env python3
# run every hour
from controller import get_logger
from controller.log_parser import LogParser
from controller.config import DEVICES_ENDPOINT
from mape.cycle import Cycle
from social.arduino import Devices
from social.serial_protocol import SerialProtocol
from database import DatabaseMetric


logger = get_logger("Main")

db_metrics = DatabaseMetric()

log_parser = LogParser(db_metrics)

if not log_parser.has_files():
    logger.info("Logfiles do not exist")
else:
    log_parser.parse_all_files()
    arduinos = Devices(DEVICES_ENDPOINT)

    for arduino in arduinos.all:
        protocol = SerialProtocol(arduino["port"])
        logger.info("Start MAPE cycle")
        Cycle(protocol, arduino["id"]).start()
