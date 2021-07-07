import logging
from logging.handlers import TimedRotatingFileHandler

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(pathname)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
file_handler = TimedRotatingFileHandler("./log/app.log", when="midnight", interval=1)

stream_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

stream_handler.setFormatter(CustomFormatter())
file_handler.setFormatter(CustomFormatter())

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
