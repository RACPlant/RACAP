import analizer
import planner
import time
from controller.protocol import Protocol
import logging

FORMAT = '%(asctime)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger("Write")


protocol = Protocol("/dev/ttyACM0")

while True:
    logger.info("Start loop...")
    protocol.get_metrics()
    protocol.water_in(2)
    time.sleep(10)
    logger.info("End loop.")
