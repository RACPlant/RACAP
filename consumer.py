import threading
import time
import os
from serial.serialutil import SerialException
from controller.config import DEVICES_ENDPOINT
from controller import get_logger_to_file, get_logger
from social.arduino import Devices
from social.serial_protocol import SerialProtocol
from social.parser import Parser

CONNECTION_BACKOFF_TIME = 60

arduinos = Devices(DEVICES_ENDPOINT)
protocols = [SerialProtocol(arduino["port"]) for arduino in arduinos.all]

main_thread_logger = get_logger("Consumer")


def consume_serial(protocol: SerialProtocol):
    port_id = os.path.basename(protocol.serial_port)
    logger = get_logger_to_file("Consumer_{}".format(port_id))
    parser = Parser()
    error_logger = get_logger("ConsumeErrorLog_{}".format(port_id))

    def loop_and_parse(conn):
        while True:
            data = protocol.read_until(conn)
            try:
                parsed_data = parser.parse(data)
                for metric in parsed_data:
                    logger.info(metric)
            except IOError:
                error_logger.info("Error to parse message:{}".format(data))

    def connect_and_parse():
        try:
            with protocol.connect() as conn:
                error_logger.info("Connected...")
                loop_and_parse(conn)

        except SerialException:
            error_logger.error(
                "Error connecting to port {}".format(protocol.serial_port))
            error_logger.error("Waiting {}s to retry".format(
                CONNECTION_BACKOFF_TIME))
            time.sleep(CONNECTION_BACKOFF_TIME)
            connect_and_parse()

    connect_and_parse()


for protocol in protocols:
    main_thread_logger.info(
        "Starting new thread to read port: {}".format(protocol.serial_port))
    t = threading.Thread(target=consume_serial, args=(protocol,))
    t.start()
