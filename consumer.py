#!/usr/bin/env python3
import threading
import uuid
import time
from serial.serialutil import SerialException
from controller import get_logger_to_file, get_logger
from social.devices import Arduino
from social.serial_protocol import SerialProtocol
from social.parser import Parser

arduinos = Arduino("api_endpoint")

protocols = [SerialProtocol(arduino["port"]) for arduino in arduinos.all]


def consume_serial(protocol):
    logger = get_logger_to_file("Consumer{}".format(uuid.uuid4().hex))
    parser = Parser()
    error_logger = get_logger("Consume")

    def loop_and_parse(conn):
        while True:
            data = protocol.read_until(conn)
            try:
                parsed_data = parser.parse(data)
                for metric in parsed_data:
                    logger.info(metric)
            except IOError:
                logger.info("Error to parse message:{}".format(data))

    def connect_and_parse():
        try:
            with protocol.connect() as conn:
                logger.info("Connected...")
                loop_and_parse(conn)

        except SerialException:
            error_logger.error(
                "Error connecting to port {}".format(protocol.serial_port))
            time.sleep(60)
            error_logger.error("Retrying port {}".format(protocol.serial_port))
            connect_and_parse()

    connect_and_parse()


for protocol in protocols:
    t = threading.Thread(target=consume_serial, args=(protocol,))
    t.start()
