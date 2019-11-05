import logging
import os


def get_logger(name):
    LOGLEVEL = os.environ.get('LOGLEVE', 'INFO')
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=LOGLEVEL)
    return logging.getLogger(name)
