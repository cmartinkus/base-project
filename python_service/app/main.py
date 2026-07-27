import logging

from common.config.settings import settings
from common.config.logging_config import configure_logging
from app.scheduler.scheduler import ServiceScheduler


def main():
    configure_logging(settings.LOG_LEVEL)

    logger = logging.getLogger(__name__)

    logger.info("Starting %s", settings.APP_NAME)

    scheduler = ServiceScheduler()
    scheduler.start()


if __name__ == "__main__":
    main()