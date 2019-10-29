import serial
import logging

METRICS = "getMetrics"
WATER = "water"
END = b"endMessage"
START = b"startMessage"

FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger("Protocol")


class Protocol:
    def __init__(self, serial_port, parser=None):
        self.parser = parser
        self.serial_port = serial_port

    def _connect(self):
        return serial.Serial(self.serial_port)

    def _send_message(self, message):
        encoded_message = str.encode(message)
        with self._connect() as conn:
            logger.debug("Sending message \"%s\"", encoded_message)
            conn.write(encoded_message)
            conn.flush()

    def read_until(self):
        with self._connect() as conn:
            logger.debug("Reading ... ")
            sensor_data = conn.read_until(END))
            logger.debug("Readed message: \"%s\"", sensor_data)
        return sensor_data

    def parse(self, data):
        logger.debug("Parsing data: \"%s\"", data)
        if data.startswith(START):
            return self.parser(data).metrics()
        else:
            raise IOError("Data not recognized")

    def get_metrics(self):
        return self._send_message("{}".format(METRICS))

    def water_in(self, pump):
        return self._send_message("{}:{}".format(WATER, pump))
