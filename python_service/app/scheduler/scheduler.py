import logging
from apscheduler.schedulers.blocking import BlockingScheduler
from common.config.settings import settings
from jobs.job_1 import Job1

logger = logging.getLogger(__name__)


class ServiceScheduler:

    def __init__(self):
        self.job1 = Job1()
        self.scheduler = BlockingScheduler()

    def register_jobs(self):

        if settings.JOB1_ENABLED:
            self.scheduler.add_job(
                self.job1.run,
                trigger="interval",
                seconds=settings.JOB1_INTERVAL_SECONDS,
                id="job_1",
                replace_existing=True,
            )

    def start(self):
        logger.info("Starting scheduler")
        self.register_jobs()
        self.scheduler.start()