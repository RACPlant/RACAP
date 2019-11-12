#!/usr/bin/env python3
# run every hour
import time
import glob
from database.knowledge_base import KnowledgeBase
from json import loads


kb = KnowledgeBase()

log_files = glob.glob("Consumer*.log")

def parser_line(line):
    start_index = line.find('{')
    end_index = line.rfind('}')
    json_line = line[start_index:end_index+1]
    json_line = json_line.replace("'", "\"")
    return loads(json_line)


for log in log_files
    with open(log, 'r') as consumer_logfile:

        line = consumer_logfile.readline()
        while line:
            metric_log = parser_line(line)
            kb.add_metric_fact(
                metric_log['arduino'],
                metric_log['sensor'],
                metric_log['value'])

            line = consumer_logfile.readline()

kb.update_metrics_file()
