import serial
import time
from controller import get_logger
from controller.sensor import NOISE_ATTENUATOR

METRICS = "getMetrics"
WATER = "water"
END = b"endMessage"


class Protocol:

    logger = get_logger("Protocol")

    def __init__(self, argv):
        """Protocol class that handles message exchanges

        Args:
            argv (list):  argv[1] is Arduino's serial port. Usually is ACM0.
        """
        port = argv[1] if (len(argv) == 2) else "ACM0"
        self.serial_port = "/dev/tty{}".format(port)

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
            str: Readed message.
        """
        with self._connect() as conn:
            self.logger.debug("Reading ... ")
            sensor_data = conn.read_until(END)
            self.logger.debug("Readed message: \"%s\"", sensor_data)
        return sensor_data.decode("utf-8")

    def get_metrics(self):
        """Send message `getMetrics`

        Returns:
            [None]: Nothing
        """
        for i in range(NOISE_ATTENUATOR):
            self._send_message("{}".format(METRICS))
            time.sleep(10)

    def water_in(self, arduino, pump, time):
        """Send message to water a plant for some time

        Args:
            arduino (str): Arduino id
            pump (str): Pump id
            time (int): Time in seconds to water the plant

        Returns:
            [None]: Nothing
        """
        message_info = [WATER, arduino, pump, time]
        return self._send_message(":".join(message_info))
