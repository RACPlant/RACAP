import serial
from controller import get_logger

METRICS = "getMetrics"
WATER = "water"
END = b"endMessage"


class Protocol:

    logger = get_logger("Protocol")

    def __init__(self, serial_port):
        """Protocol class that handles message exchanges

        Args:
            serial_port (int):  Arduino's serial port. Usually is /dev/ttyACM0.
        """

        self.serial_port = serial_port

    def _connect(self):
        return serial.Serial(self.serial_port)

    def _send_message(self, message):
        encoded_message = str.encode(message)
        with self._connect() as conn:
            self.logger.debug("Sending message \"%s\"", encoded_message)
            conn.write(encoded_message)
            conn.flush()

    def read_until(self):
        """Read the serial port until message is finish.

        Returns:
            str -- readed message with start and finish messages.
        """
        with self._connect() as conn:
            self.logger.debug("Reading ... ")
            sensor_data = conn.read_until(END)
            self.logger.debug("Readed message: \"%s\"", sensor_data)
        return sensor_data.decode("utf-8")

    def get_metrics(self):
        return self._send_message("{}".format(METRICS))

    def water_in(self, arduino, pump, time):
        message_info = [WATER, arduino, pump, time]
        return self._send_message(":{".join(message_info))
