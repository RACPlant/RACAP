import logging
import os


def get_logger(name, **kwargs):
    LOGLEVEL = os.environ.get('LOGLEVE', 'INFO')
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=LOGLEVEL,
        **kwargs)
    return logging.getLogger(name)
