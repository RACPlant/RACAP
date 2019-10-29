import analizer
import planner
import time
from controller.protocol import Protocol

protocol = Protocol("/dev/ttyACM0")

while True:
    protocol.get_metrics()
#    for pump in plants.pumps:
        # if planner
    protocol.water_in(2)
    time.sleep(10)
