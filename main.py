#!/usr/bin/env python3
# run every hour
from controller import get_logger
from controller.log_parser import LogParser
from mape.cycle import Cycle
from social.devices import Arduino
from social.serial_protocol import SerialProtocol
from database.knowledge_base import KnowledgeBase


logger = get_logger("Main")

kb = KnowledgeBase()

log_parser = LogParser(kb)

if log_parser.has_files():

    log_parser.parse_all_files()

    arduinos = Arduino("api_endpoint")

    for arduino in arduinos.all:
        protocol = SerialProtocol(arduino["port"])
        logger.info("send getMetrics message")
        Cycle(protocol, arduino["id"]).start()
