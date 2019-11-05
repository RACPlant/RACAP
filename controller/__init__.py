import logging
import os

LOGLEVEL = os.environ.get('LOGLEVE', 'INFO')
logging.basicConfig(level=LOGLEVEL)


def get_logger(name, **kwargs):
    fomatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler = logging.FileHandler('{}.log'.format(name))
    handler.setFormatter(fomatter)
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    return logger
