from unittest.mock import MagicMock

from app.jobs.job_1 import Job1


def test_job_calls_processor():
    job = Job1()

    job.processor.process = MagicMock(return_value="ok")

    job.run()

    job.processor.process.assert_called_once()