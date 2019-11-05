from pyswip import Prolog
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class KnowledgeBase:

    def __init__(self,
                 rules_file=[],
                 metrics_fact_file="metrics.pl",
                 plants_fact_file="plants.pl",
                 prolog=Prolog()):
        """Prolog KnowledgeBase

        Args:
            file_path (list[str]): List of Prolog files
            prolog (Prolog, optional): Object to run querys on KnowledgeBase.
            Defaults to Prolog().
        """
        self._metrics_fact_file = metrics_fact_file
        self._plants_fact_file = plants_fact_file
        self._file_path = [metrics_fact_file, plants_fact_file] + rules_file
        self._prolog = prolog

    def __include_fact(self, kb_file, predicative, *terms):
        terms_string = ", ".join(terms)
        fact = "{}({}).".format(predicative, terms_string)
        register_time = datetime.now().strftime(DATE_FORMAT)

        with open(kb_file, "a") as kb:
            kb.write("{}%% registered:{}\n".format(fact, register_time))

    def _consult(self):
        for file_path in self._file_path:
            self._prolog.consult(file_path)

    def add_metric_fact(self, arduino, sensor, value):
        """Include a new fact in metrics knowledge base (Prolog file).

        Args:
            arduino (str): Arduino Id
            sensor (str): Sensor Id
            value (int): Value from sensor
        """
        self.__include_fact(self._metrics_fact_file,
                            "metrify",
                            arduino,
                            sensor,
                            value)

    def add_plant_fact(self, plant, arduino, humidity_sensor, pump):
        """Include a new plant register in plants knowledge base (Prolog file).

        Args:
            plant (str): Plant type
            arduino (str): Arduino id
            humidity_sensor (str): Humidity soil sensor id
            pump (str): Pump id
        """
        self.__include_fact(self._plants_fact_file,
                            "plant",
                            plant,
                            arduino,
                            humidity_sensor,
                            pump)

    def query(self, prolog_query, limit=-1):
        self._consult()
        return [result for result in self._prolog.query(prolog_query, limit)]
