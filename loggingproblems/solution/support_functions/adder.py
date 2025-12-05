import logging

class Adder(object):
    def __init__(self, initial_value):
        self.value = initial_value
        self.logger = logging.getLogger(__name__)
        self.logger.warning(f"Set initial value to {initial_value}")

    def add(self, *addends):
        self.logger.info(f"Adding values {str(addends)}")
        for eachval in addends:
            self.value += eachval

    def result(self):
        self.logger.info(f"Sending the result!")
        return self.value

