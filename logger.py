__author__ = 'dk'
import logging
import datetime
from config import log_fname
logging.basicConfig(filename=log_fname, filemode='a',
                           format='%(asctime)s - %(levelname)s: %(message)s',
                           level=logging.NOTSET)
_WARNING = 10
_INFO = 100
_ERROR = 0
_EMPTY = -1
level = _INFO
def warning(msg):
    if level < _WARNING :
        return
    logging.warning(msg="Time:{0}, [WARN]: {1}".format(datetime.datetime.now(),msg))

def info(msg):
    if level < _INFO :
        return
    logging.warning(msg="Time:{0}, [INFO]: {1}".format(datetime.datetime.now(),msg))

def error(msg):
    if level < _ERROR :
        return
    logging.warning(msg="Time:{0}, [ERROR]: {1}".format(datetime.datetime.now(),msg))