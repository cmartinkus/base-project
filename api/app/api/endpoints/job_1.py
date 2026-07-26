from fastapi import APIRouter

from common.messaging.rabbitmq import RabbitMQClient
from common.messaging.exchanges import COMMANDS_EXCHANGE
from common.messaging.exchanges import EVENTS_EXCHANGE

router = APIRouter()


@router.post("/job_1/run")
def submit_job():

    rabbit = RabbitMQClient()



    rabbit.publish(
        exchange=EVENTS_EXCHANGE,
        routing_key="job.completed",
        message={
            "job_name": "job_1",
            "status": "complete",
            "result": {
                "records_processed": 500
            }
        }
    )