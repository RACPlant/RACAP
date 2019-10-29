import analizer
import planner
import time
from controller.protocol import Protocol

protocol = Protocol("/dev/ttyS3")

while True:
    protocol.get_metrics()
    for pump in plants.pumps:
        # if planner
        protocol.water_in(pump)
    time.sleep(1)