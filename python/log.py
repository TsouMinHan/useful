
from logging.handlers import TimedRotatingFileHandler

import logging

class StreamFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    debug_format = "%(asctime)s - %(name)s - %(levelname)s || %(message)s (%(pathname)s:%(lineno)d)"
    format = "%(asctime)s - %(levelname)s || %(message)s"

    FORMATS = {
        logging.DEBUG: grey + debug_format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + debug_format + reset,
        logging.ERROR: red + debug_format + reset,
        logging.CRITICAL: bold_red + debug_format + reset
    }

    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=self.DATE_FORMAT)
        
        return formatter.format(record)
    
class FileFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors
    """
    DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

    def format(self, record):
        if record.levelno == logging.INFO:
            log_fmt = "%(asctime)s - %(levelname)s || %(message)s"
        else:
            log_fmt = "%(asctime)s - %(name)s - %(levelname)s || %(message)s (%(pathname)s:%(lineno)d)"
        formatter = logging.Formatter(log_fmt, datefmt=self.DATE_FORMAT)
        
        return formatter.format(record)

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
file_handler = TimedRotatingFileHandler("./log/app.log", when="midnight", interval=1, encoding='utf-8')

stream_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)
logger.setLevel(logging.INFO)

stream_handler.setFormatter(StreamFormatter())
file_handler.setFormatter(FileFormatter())

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
