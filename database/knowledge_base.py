from os import path
from pyswip import Prolog
from datetime import datetime
from controller.sensor import Sensor
from controller import get_logger

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

DB_PATH = "./database/db/"


class KnowledgeBase:

    logger = get_logger("KnowledgeBase")

    def __init__(self,
                 rules_files=[],
                 metrics_fact_file="metrics.pl",
                 plants_fact_file="plants.pl",
                 arduino_fact_file="arduino.pl",
                 prolog=Prolog()):
        self._kb_metrics_dict = self._kb_plants_dict = {}
        self._metrics_fact_file = path.join(DB_PATH, metrics_fact_file)
        self._plants_fact_file = path.join(DB_PATH, plants_fact_file)
        self._arduino_fact_file = path.join(DB_PATH, arduino_fact_file)
        self._file_path = [
            self._metrics_fact_file,
            self._plants_fact_file,
            self._arduino_fact_file
        ] + rules_files
        self._prolog = prolog

    def _consult(self):
        for file_path in self._file_path:
            self._prolog.consult(file_path)

    def update_metrics_file(self):
        """This method generates the knowledge base for metrics (Prolog file).
        """
        text = ""
        for arduino in self._kb_metrics_dict.keys():
            for sensor in self._kb_metrics_dict[arduino].keys():
                text += "{}\n".format(
                    self._kb_metrics_dict[arduino][sensor].get_fact())
        text += "%% log processed at {}".format(
            datetime.now().strftime(DATE_FORMAT))

        self.logger.info("Writing the Metric Fact File")
        self.logger.debug("Matric Fact File Content: {}".format(text))
        with open(self._metrics_fact_file, "+w") as metrics_file:
            metrics_file.write(text)

    def add_metric_fact(self, arduino, sensor, value):
        """Include a new fact in metrics knowledge base (Prolog file).

        Args:
            arduino (str): Arduino Id
            sensor (str): Sensor Id
            value (int): Value from sensor
        """
        if not self._kb_metrics_dict.get(arduino):
            self._kb_metrics_dict[arduino] = {}

        if not self._kb_metrics_dict[arduino].get(sensor):
            self._kb_metrics_dict[arduino][sensor] = Sensor(arduino, sensor)

        self._kb_metrics_dict[arduino][sensor].value = value

    def add_plants_fact(self, arduino, plants):
        """Include a new fact in plants knowledge base (Prolog file).

        Args:
            arduino (str): Arduino Id
            plants (Plants): Plants object
        """
        self._kb_plants_dict[arduino] = plants.get_all_facts()

    def update_plants_fact(self):
        """This method generates the knowledge base for plants (Prolog file).
        """
        text = ""
        for facts in self._kb_plants_dict.values():
            text += facts
        text += "%% got plants at {}".format(
            datetime.now().strftime(DATE_FORMAT))

        self.logger.info("Writing the Plant Fact File")
        with open(self._plants_fact_file, "+w") as plants_file:
            plants_file.write(text)

    def update_arduino_fact(self, arduinos):
        """This method generates the knowledge base for arduino (Prolog file).
        Args:
            arduinos (Arduino): Arduino object
        """
        text = arduinos.get_all_facts()
        text += "%% got arduino at {}".format(
            datetime.now().strftime(DATE_FORMAT))

        self.logger.info("Writing the Arduino Fact File")
        with open(self._arduino_fact_file, "+w") as arduino_file:
            arduino_file.write(text)

    def query(self, prolog_query, limit=-1):
        """This method runs a Prolog query over rules_files,
        metrics_fact_file and plants_fact_file.

        Args:
            prolog_query (str): Prolog query
            limit (int, optional): limit for the result size.

        Returns:
            [list[dict]]: List of dicts with all query answers.
        """
        self._consult()
        return [result for result in self._prolog.query(prolog_query, limit)]
