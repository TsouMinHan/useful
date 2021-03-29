import logging
from datetime import datetime
from pathlib import Path

class Log():
    def __init__(self):
        self.logger = logging.getLogger(__name__)

        stream_handler = logging.StreamHandler()
        log_name = Path("log", f"{datetime.now().strftime('%Y-%m-%d')}.txt")
        file_handler = logging.FileHandler(log_name)

        stream_handler.setLevel(logging.INFO)
        file_handler.setLevel(logging.INFO)

        formater = logging.Formatter("%(asctime)s | %(levelname)s | Line: %(lineno)d | %(message)s")
        file_formater = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

        stream_handler.setFormatter(formater)
        file_handler.setFormatter(file_formater)

        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)
    
    def debug(self, msg):
        self.logger.debug(msg)
        
    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
    
    
if __name__ == "__main__":
    log = Log()
    log.logger.warning("asdasds")
