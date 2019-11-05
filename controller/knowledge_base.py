from pyswip import Prolog
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


class KnowledgeBase:

    def __init__(self, file_path, prolog=Prolog()):
        self._file_path = file_path
        self._prolog = prolog

    def metrify(self, arduino, sensor, value):
        self._persist("metrify({}, {}, {}).".format(
            arduino.lower(), sensor.lower(), value))

    def _persist(self, fact):
        with open(self._file_path, "a") as kb:
            kb.write("{}%% registered: {}\n".format(
                fact, datetime.now().strftime(DATE_FORMAT)))

    def _consult(self):
        self._prolog.consult(self._file_path)

    def query(self, arduino, sensor, value, limit=-1):
        self._consult()
        query = "metrify({}, {}, {})".format(arduino, sensor, value)
        return [result for result in self._prolog.query(query, limit)]
