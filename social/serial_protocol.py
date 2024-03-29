import serial
from controller import get_logger

METRICS = "getMetrics"
WATER = "water"
END = b"endMessage"


class SerialProtocol:

    logger = get_logger("Protocol")

    def __init__(self, serial_port):
        """Protocol class that handles message exchanges

        Args:
            serial_port (string):  serial_port is Arduino's serial port. Usually is /dev/ttyACM0.
        """
        self.serial_port = serial_port

    def connect(self):
        return serial.Serial(self.serial_port)

    def _send_message(self, message):
        encoded_message = str.encode(message)
        with self.connect() as conn:
            self.logger.debug("Sending message \"%s\"", encoded_message)
            conn.write(encoded_message)
            conn.flush()

    def read_until(self, conn):
        """Read the serial port until message is finish.

        Returns:
            str: Readed message.
        """
        self.logger.debug("Reading ... ")
        sensor_data = conn.read_until(END)
        self.logger.debug("Readed message: \"%s\"", sensor_data)
        return sensor_data.decode("utf-8")

    def get_metrics(self):
        """Send message `getMetrics`

        Returns:
            [None]: Nothing
        """
        self._send_message("{}".format(METRICS))

    def water_in(self, pump, time):
        """Send message to water a plant for some time

        Args:
            pump (str): Pump id
            time (int): Time in seconds to water the plant

        Returns:
            [None]: Nothing
        """
        self.logger.info(
            "Send message water_in: {}:{}:{}".format(
                WATER, pump, time))
        message_info = [WATER, pump, str(time)]
        self._send_message(":".join(message_info))
