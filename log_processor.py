from controller.knowledge_base import KnowledgeBase
import time
from json import loads


kb = KnowledgeBase()


def parser_line(line):
    start_index = line.find('{')
    end_index = line.rfind('}')
    json_line = line[start_index:end_index+1]
    json_line = json_line.replace("'", "\"")
    return loads(json_line)


with open('Consumer.log', 'r') as consumer_logfile:
    while True:
        line = consumer_logfile.readline()
        if line:
            metric_log = parser_line(line)
            kb.add_metric_fact(
                metric_log['arduino'],
                metric_log['sensor'],
                metric_log['value'])
            kb.update_metrics_file()
            print(consumer_logfile.tell())
        time.sleep(1)
