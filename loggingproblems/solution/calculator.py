import logging
logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("calculator")
handler = logging.FileHandler("/tmp/calculator.log")
handler.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
handler.setLevel(logging.WARNING)
logger.addHandler(handler)
import support_functions.adder

logger.debug("Adding 10 and 5")
adder = support_functions.adder.Adder(0)
adder.add(10, 5)
logger.warning(f"The result is {adder.result()}")