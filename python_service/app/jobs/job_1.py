import logging
from processors.processor_1 import Processor1

logger = logging.getLogger(__name__)


class Job1:

    def __init__(self):
        self.processor = Processor1()

    def run(self):
        logger.info("Running Job 1",    
                    extra={
                        "job": "job_1",
                        "customer_id": 12345,
                    },
        )

        try:
            self.processor.process()

        except Exception:
            logger.exception("Job 1 failed")
            raise

        logger.info("Finished Job 1")