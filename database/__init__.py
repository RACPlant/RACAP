
from datetime import datetime
from os import path
from controller.config import DB_PATH, RASPBERRY_ID
from abc import ABC
from controller.sensor import Sensor
from controller import get_logger
from controller.plants import Plants
from social.arduino import Devices


class Database(ABC):
    _filename = None

    def __init__(self):
        self._memory_db = {}
        self._logger = get_logger(self.__class__.__name__)

    def get_file_path(self):
        return path.join(DB_PATH, self._filename)

    def _get_facts(self):
        raise NotImplementedError

    def update_database(self):
        facts = self._get_facts()  # Lista de string com os fatos
        facts_text = "\n".join(facts)
        text = "{}\n%%update database time: {}".format(
            facts_text, datetime.now())

        with open(self.get_file_path(), "+w") as pl_file:
            pl_file.write(text)


class DatabaseMetric(Database):
    _filename = "metrics.pl"

    def _get_facts(self):
        facts = []
        for arduino_id, sensors_dict in self._memory_db.items():
            for sensor_id, sensor in sensors_dict.items():
                fact = sensor.get_fact()
                if fact:
                    facts.append(sensor.get_fact())
        return sorted(facts)

    def add_metric_fact(self, arduino, sensor, value):
        if not self._memory_db.get(arduino):
            self._memory_db[arduino] = {}

        if not self._memory_db[arduino].get(sensor):
            self._memory_db[arduino][sensor] = Sensor(arduino, sensor)
        self._memory_db[arduino][sensor].value = value


class DatabasePlant(Database):
    _filename = "plants.pl"

    def add_plants_fact(self, arduino: str, plant: Plants):
        self._memory_db[arduino] = plant.get_all_facts()

    def _get_facts(self):
        facts = []
        for fact_list in self._memory_db.values():
            facts.extend(fact_list)
        return sorted(facts)


class DatabaseArduino(Database):
    _filename = "arduino.pl"

    def add_arduino_fact(self, arduinos: Devices):
        self._memory_db[RASPBERRY_ID] = arduinos.get_all_facts()

    def _get_facts(self):
        return sorted(self._memory_db[RASPBERRY_ID])


AllDatabases = [DatabaseArduino(), DatabaseMetric(), DatabasePlant()]
