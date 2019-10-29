import analizer
import planner
import sys
from controller.protocol import Protocol
from controller.parser import Parser
from controller.plants import Plants

plants = Plants()
#plants.set_info()
port = sys.argv[1] if (len(sys.argv) == 2) else "ACM0"

protocol = Protocol("/dev/tty{}".format(port), Parser())

while True:
    data = protocol.read_until()
    kind, parsed_data = protocol.parse(data)
    # to analyser