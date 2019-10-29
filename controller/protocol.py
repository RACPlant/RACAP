import serial
import logging

METRICS = "getMetrics"
WATER = "water"
END = "endMessage"

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
        with self._connect() as conn:
            logger.debug("Sending message \"%s\"", message)
            conn.write(message)
            conn.flush()

    def read_until(self):
        with self._connect() as conn:
            logger.debug("Reading ... ")
            sensor_data = conn.read_until(str.encode("{}".format(END)))
            logger.debug("Readed message: \"%s\"", sensor_data)
        return sensor_data

    def parse(self, data):
        if data.startswith(METRICS):
            return self.parser(data).metrics()
        elif data.startswith(WATER):
            return self.parser(data).water()
        else:
            raise IOError("Data not recognized")

    def get_metrics(self):
        return self._send_message(str.encode("{}".format(METRICS)))

    def water_in(self, pump):
        return self._send_message(str.encode("{}:{}".format(WATER, pump)))
