import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

stream_handler = logging.StreamHandler()
log_name = Path("log", f"{datetime.now().strftime('%Y-%m-%d')}.log")
file_handler = logging.FileHandler(log_name)

stream_handler.setLevel(logging.INFO)
file_handler.setLevel(logging.INFO)

formater = logging.Formatter("%(asctime)s | %(levelname)s | Line: %(lineno)d | %(message)s")
file_formater = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

stream_handler.setFormatter(formater)
file_handler.setFormatter(file_formater)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)
