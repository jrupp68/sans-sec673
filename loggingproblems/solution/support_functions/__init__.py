import logging
import requests

logging.basicConfig(level=logging.WARNING, format=logging.BASIC_FORMAT)
logger = logging.getLogger(__name__)

#Confirm internet access:
try:
    resp = requests.get("http://sans.org")
except:
    logger.warning("No Internet")
else:
    if resp.status_code == 200:
        logger.warning("Internet Confirmed.")


logger.warning("Adder object exported!")
from support_functions.adder import Adder