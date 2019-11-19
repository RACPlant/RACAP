
from datetime import datetime
from os import path
from controller.config import DB_PATH
from abc import ABC
from controller.sensor import Sensor


class Database(ABC):
    _filename = None

    def __init__(self):
        self._memory_db = {}

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
    # Utilizar modelos do tipo Metric para incluir/atualizar o arquivo arduino.pl

    def _get_facts(self):
        pass

    def add_metric(self, arduino, sensor, value):
        if not self._kb_metrics_dict.get(arduino):
            self._kb_metrics_dict[arduino] = {}

        if not self._kb_metrics_dict[arduino].get(sensor):
            self._kb_metrics_dict[arduino][sensor] = Sensor(arduino, sensor)

        self._kb_metrics_dict[arduino][sensor].value = value


class DatabasePlant:
    # Utilizar modelos do tipo Plant para incluir/atualizar o arquivo arduino.pl
    pass


class DatabaseArduino:
    # Utilizar modelos do tipo Arduino para incluir/atualizar o arquivo arduino.pl

    def _get_facts(self):
        pass

    def add_arduino(self):
        pass
