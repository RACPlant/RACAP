import logging
import os

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO')
logging.basicConfig(level=LOGLEVEL)
fomatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(fomatter)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.addHandler(stream_handler)
    return logger


def get_logger_to_file(name):
    file_handler = logging.FileHandler('{}.log'.format(name))
    file_handler.setFormatter(fomatter)
    logger = logging.getLogger(name)
    logger.addHandler(file_handler)
    return logger
