import analizer
import planner
from controller.protocol import Protocol
from controller.parser import Parser
from controller.plants import Plants

plants = Plants()
plants.set_info()

protocol = Protocol("/dev/ttyS3", Parser())

while True:
    data = protocol.read_until()
    kind, parsed_data = protocol.parse(data)
    # to analyser