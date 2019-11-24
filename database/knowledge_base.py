from pyswip import Prolog
from controller import get_logger
from typing import List
from database import Database

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

DB_PATH = "./database/db/"


class KnowledgeBase:

    logger = get_logger("KnowledgeBase")

    def __init__(self,
                 rules_files=[],
                 databases: List[Database] = [],
                 prolog=Prolog()):
        self._file_path = [db.get_file_path()
                           for db in databases] + rules_files
        self._prolog = prolog

    def _consult(self):
        for file_path in self._file_path:
            self._prolog.consult(file_path)

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
