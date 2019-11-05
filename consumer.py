import sys
from controller.protocol import Protocol
from controller.parser import Parser
from controller.plants import Plants
from controller.knowledge_base import KnowledgeBase

plants = Plants()
# plants.set_info()
port = sys.argv[1] if (len(sys.argv) == 2) else "ACM0"

protocol = Protocol("/dev/tty{}".format(port))
parser = Parser()
kb = KnowledgeBase("kb.pl")

while True:
    data = protocol.read_until()
    parsed_data = parser.parse(data)
    # parsed_data = [{"arduino": "Dois", "sensor": "Maneiro", "value": 3}, {"arduino": "Dois", "sensor": "Biruta", "value": 4}]
    for metric in parsed_data:
        kb.metrify(**metric)
    # print(kb.query("dois", "X", "Y"))
