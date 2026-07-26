import logging

logger = logging.getLogger(__name__)


class Processor1:

    def function_1(self):

        logger.info("Beginning function_1")

        value = self.calculate()

        logger.info("Calculated value = %s", value)

    def calculate(self):
        return 42
    
    def process(self) -> str:
        self.function_1()
        return "processor completed"