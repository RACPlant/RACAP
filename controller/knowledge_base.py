from pyswip import Prolog
from datetime import datetime
from controller.sensor import Sensor
from controller import get_logger

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class KnowledgeBase:

    logger = get_logger("KnowledgeBase")

    def __init__(self,
                 rules_file=[],
                 metrics_fact_file="metrics.pl",
                 plants_fact_file="plants.pl",
                 prolog=Prolog()):
        self.__kb_metrics_dict = {}
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

    def update_metrics_file(self):
        text = ""
        for arduino in self.__kb_info_dict.keys():
            for sensor in self.__kb_info_dict[arduino].keys():
                text += "{}\n".format(
                    self.__kb_info_dict[arduino][sensor].get_fact())

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
        if not self.__kb_metrics_dict.get(arduino):
            self.__kb_metrics_dict[arduino] = {}

        if not self.__kb_metrics_dict[arduino].get(sensor):
            self.__kb_metrics_dict[arduino][sensor] = Sensor(arduino, sensor)

        self.__kb_metrics_dict[arduino][sensor].value = value

    def query(self, prolog_query, limit=-1):
        self._consult()
        return [result for result in self._prolog.query(prolog_query, limit)]
