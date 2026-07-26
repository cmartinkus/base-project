import json
import logging

from common.messaging.rabbitmq import RabbitMQClient


logger = logging.getLogger(__name__)

import json


def handle_job(
    channel,
    method,
    properties,
    body,
):

    message = json.loads(body)

    print(
        "Running:",
        message["job_name"]
    )

    # run job here

    channel.basic_ack(
        delivery_tag=method.delivery_tag
    )


rabbit.channel.basic_consume(
    queue="job.worker.queue",
    on_message_callback=handle_job,
)

rabbit.channel.start_consuming()
