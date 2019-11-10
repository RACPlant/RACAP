#!/usr/bin/env python3
import sys
from controller.protocol import Protocol
from controller.parser import Parser
from controller import get_logger_to_file

logger = get_logger_to_file("Consumer")

protocol = Protocol(sys.argv)
parser = Parser()

while True:
    data = protocol.read_until()
    parsed_data = parser.parse(data)
    for metric in parsed_data:
        logger.info(metric)