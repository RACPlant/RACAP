import logging
import os

LOGLEVEL = os.environ.get('LOGLEVE', 'INFO')
logging.basicConfig(level=LOGLEVEL)


def get_logger(name):
    fomatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.StreamHandler()
    handler.setFormatter(fomatter)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    return logger


def get_logger_to_file(name):
    fomatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler('{}.log'.format(name))
    handler.setFormatter(fomatter)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    return logger
