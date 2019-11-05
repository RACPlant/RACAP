#!/usr/bin/env python3
import time
import sys
from controller.protocol import Protocol
from controller import get_logger
from controller.knowledge_base import KnowledgeBase
logger = get_logger("Write")


port = sys.argv[1] if (len(sys.argv) == 2) else "ACM0"

protocol = Protocol("/dev/tty{}".format(port))
kb_analyzer = KnowledgeBase(rules_file=["analyzer.pl"])
kb_planner = KnowledgeBase(rules_file=["planner.pl"])

while True:
    logger.info("Start loop...")
    protocol.get_metrics()
    time.sleep(10)
    logger.info("End loop.")
