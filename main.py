import analizer
import planner
from controller.protocol import Protocol
from controller.plants import Plants

plants = Plants()
plants.set_info()

protocol = Protocol("/dev/tty4")
protocol.get_metrics()
for pump in plants.pumps:
    protocol.water_in(pump)