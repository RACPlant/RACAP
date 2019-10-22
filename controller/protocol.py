import serial

class Protocol:
    def __init__(self, serial_port):
        self.serial_port = serial_port
    
    def _connect(action="read"):
        return serial.Serial(self.serial_port)

    def get_sensors(self):
        with self._connect() as conn:
            conn.writelines("start")
        with self._connect() as conn:
            sensor_data = conn.read_until("endian")
        with self._connect() as conn:
            conn.writelines("stop")