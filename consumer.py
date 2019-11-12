#!/usr/bin/env python3
import threading
import uuid
from controller import get_logger_to_file
from social.devices import Arduino
from social.serial_protocol import SerialProtocol
from social.parser import Parser

arduinos = Arduino("api_endpoint")

protocols = [SerialProtocol(arduino["port"]) for arduino in arduinos.all]


def consume_serial(protocol):
    logger = get_logger_to_file("Consumer{}".format(uuid.uuid4().hex))
    parser = Parser()
    while True:
        data = protocol.read_until()
        parsed_data = parser.parse(data)
        for metric in parsed_data:
            logger.info(metric)


for protocol in protocols:
    t = threading.Thread(target=consume_serial, args=(protocol,))
    t.start()
