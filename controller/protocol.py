import serial

class Protocol:
    def __init__(self, serial_port):
        self.serial_port = serial_port
    
    def _connect(self):
        return serial.Serial(self.serial_port)

    def _read_until(self):
        with self._connect() as conn:
            sensor_data = conn.read_until(b"endMessage")
        return sensor_data

    def _send_message(self, message):
        with self._connect() as conn:
            conn.write(message)
            
    def get_metrics(self):
        self._send_message(b"getMetrics")
        return self._read_until()
    
    def water_in(self, pump):
        self._send_message(b"water:{}".format(pump))
        return self._read_until()
