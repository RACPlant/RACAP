import logging
import os

LOGLEVEL = os.environ.get('LOGLEVEL', 'INFO')
logging.basicConfig(
    level=LOGLEVEL,
    handlers=[])
_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
_stream_handler = logging.StreamHandler()
_stream_handler.setFormatter(_formatter)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.addHandler(_stream_handler)
    return logger


def get_logger_to_file(name):
    file_handler = logging.FileHandler('{}.log'.format(name))
    file_handler.setFormatter(_formatter)
    logger = logging.getLogger(name)
    logger.addHandler(file_handler)
    return logger
