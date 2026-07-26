from app.worker import run_worker


if __name__ == "__main__":

    run_worker()

    from common.messaging.rabbitmq import RabbitMQClient
from common.messaging.exchanges import COMMANDS_EXCHANGE


rabbit = RabbitMQClient()


rabbit.create_queue(
    "job.worker.queue"
)


rabbit.bind_queue(
    queue_name="job.worker.queue",
    exchange=COMMANDS_EXCHANGE,
    routing_key="job.*",
)