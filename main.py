import analizer
import planner
from controller.protocol import Protocol
from controller.plants import Plants

plants = Plants()
plants.set_info()

protocol = Protocol("/dev/porta")
protocol.get_sensors()