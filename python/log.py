import logging
from datetime import datetime
from pathlib import Path
from bcolor import Bcolors as bc

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    GREY = "\x1b[38;21m"
    YELLOW = "\x1b[33;21m"
    RED = "\x1b[31;21m"
    BOLD_RED = "\x1b[31;1m"
    RESET = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: GREY + format + RESET,
        logging.INFO: GREY + format + RESET,
        logging.WARNING: YELLOW + format + RESET,
        logging.ERROR: RED + format + RESET,
        logging.CRITICAL: BOLD_RED + format + RESET
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
log_name = Path("log", f"{datetime.now().strftime('%Y-%m-%d')}.log")
file_handler = logging.FileHandler(log_name)

stream_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
)
stream_handler.setFormatter(CustomFormatter())
file_handler.setFormatter(file_formater)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
