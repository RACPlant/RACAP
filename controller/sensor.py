
class Sensor:

    def __init__(self, arduino_id, sensor_id):
        self.arduino_id = arduino_id
        self.sensor_id = sensor_id
        self._value = 0
        self._max = 0
        self._min = 1023
        self._sum = 0
        self._count_values = 0

    def get_fact(self):
        tuple_value = ",".join([self.arduino_id,
                                self.sensor_id,
                                str(self._value),
                                str(self._max),
                                str(self._min),
                                str(self.get_mean())])
        return "sensor({}).".format(tuple_value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = float(value)
        self._count_values += 1
        self._sum += self._value

        if self._value < self._min:
            self._min = self._value

        if self._value > self._max:
            self._max = self._value

    def get_max(self):
        return self._max

    def get_min(self):
        return self._min

    def get_mean(self):
        return self._sum/self._count_values
