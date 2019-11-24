import json
import glob
from database import DatabaseMetric

LOG_FILES = glob.glob("Consumer*.log")


class LogParser:
    def __init__(self, db: DatabaseMetric, log_files=LOG_FILES):
        self._db = db
        self._log_files = log_files

    def _parser_line(self, line):
        start_index = line.find('{')
        end_index = line.rfind('}')
        json_line = line[start_index:end_index + 1]
        json_line = json_line.replace("'", "\"")
        return json.loads(json_line)

    def _as_fact(self, metric_log):
        self._db.add_metric_fact(
            metric_log['arduino'],
            metric_log['sensor'],
            metric_log['value']
        )

    def _parse_file(self, log):
        with open(log, 'r') as consumer_logfile:
            line = consumer_logfile.readline()
            while line:
                metric_log = self._parser_line(line)
                self._as_fact(metric_log)
                line = consumer_logfile.readline()

    def _save_facts(self):
        self._db.update_database()

    def has_files(self):
        return bool(len(self._log_files))

    def parse_all_files(self):
        for log in self._log_files:
            self._parse_file(log)
        self._save_facts()
