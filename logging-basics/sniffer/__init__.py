import logging
import sys

logger = logging.getLogger(__name__)
handler = logging.StreamHandler(stream=sys.stderr)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter(logging.BASIC_FORMAT)
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
logger.info("Sniffer __init__.py has run.")
protocols_logger = logging.getLogger("sniffer.protocols")
file_handler = logging.FileHandler("protocol_log.txt")
file_formatter = logging.Formatter("%(asctime)s:%(filename)s:%(name)s:%(levelname)s:%(message)s")
file_handler.setFormatter(file_formatter)
protocols_logger.addHandler(file_handler)