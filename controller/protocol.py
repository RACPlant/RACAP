import serial

METRICS = "getMetrics"
WATER = "water"
END = "endMessage"

class Protocol:
    def __init__(self, serial_port, parser=None):
        self.parser = parser
        self.serial_port = serial_port
    
    def _connect(self):
        return serial.Serial(self.serial_port)

    def _send_message(self, message):
        with self._connect() as conn:
            conn.writelines(message)

    def _parse_water(self, data):

    def read_until(self):
        with self._connect() as conn:
            sensor_data = conn.read_until(b"{}".format(END))
        return sensor_data
    
    def parse(self, data):
        if data.startswith(METRICS):
            return self.parser(data).metrics()
        elif data.startswith(WATER):
            return self.parser(data).water()
        else:
            raise IOError("Data not recognized")

    def get_metrics(self):
        return self._send_message(b"{}".format(METRICS))
    
    def water_in(self, pump):
        return self._send_message(b"{}:{}".format(WATER, pump))