import time
import sys
from controller.protocol import Protocol
import logging

FORMAT = '%(asctime)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger("Write")


port = sys.argv[1] if (len(sys.argv) == 2) else "ACM0"

protocol = Protocol("/dev/tty{}".format(port))

while True:
    logger.info("Start loop...")
    protocol.get_metrics()
    time.sleep(10)
    logger.info("End loop.")
