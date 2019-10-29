import analizer
import planner
import time
import sys
from controller.protocol import Protocol

port = sys.argv[1] if (len(sys.argv) == 2) else "ACM0"

protocol = Protocol("/dev/tty{}".format(port))

while True:
    protocol.get_metrics()
#    for pump in plants.pumps:
        # if planner
    protocol.water_in(2)
    time.sleep(10)
