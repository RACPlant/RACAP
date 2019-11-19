import statistics

NOISE_ATTENUATOR = 10


class Sensor:

    def __init__(self, arduino_id, sensor_id):
        self.arduino_id = arduino_id
        self.sensor_id = sensor_id
        self._last_value = 0
        self._max = 0
        self._min = 1023
        self._sum = 0
        self._count_values = 0
        self._samples = []

    def get_fact(self):
        tuple_value = ",".join([self.arduino_id,
                                self.sensor_id,
                                str(self._last_value),
                                str(self._max),
                                str(self._min),
                                str(self.get_mean())])
        return "sensor({}).".format(tuple_value)

    @property
    def value(self):
        return self._last_value

    @value.setter
    def value(self, value):
        _last_value = float(value)
        if len(self._samples) <= NOISE_ATTENUATOR:
            self._samples.append(_last_value)
        else:
            self._samples.append(_last_value)
            self._last_value = statistics.median(self._samples)
            self._samples = []

            self._count_values += 1
            self._sum += self._last_value

            if self._last_value < self._min:
                self._min = self._last_value

            if self._last_value > self._max:
                self._max = self._last_value

    def get_max(self):
        return self._max

    def get_min(self):
        return self._min

    def get_mean(self):
        return self._sum/(self._count_values or 1)
