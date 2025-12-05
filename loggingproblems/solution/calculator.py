import logging
import support_functions.adder

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)
handler = logging.FileHandler("/tmp/calculator.log")

logger.debug("Adding 10 and 5")
adder = support_functions.adder.Adder(0)
adder.add(10, 5)
logger.warning(f"The result is {adder.result()}")