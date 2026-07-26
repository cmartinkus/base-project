# common/messaging/rabbitmq.py

import json
import pika

from common.config.settings import settings


class RabbitMQClient:

    def __init__(self):

        credentials = pika.PlainCredentials(
            settings.RABBITMQ_USER,
            settings.RABBITMQ_PASSWORD,
        )

        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=settings.RABBITMQ_HOST,
                port=settings.RABBITMQ_PORT,
                credentials=credentials,
            )
        )

        self.channel = self.connection.channel()


    def create_exchange(
        self,
        exchange_name,
        exchange_type="topic",
    ):

        self.channel.exchange_declare(
            exchange=exchange_name,
            exchange_type=exchange_type,
            durable=True,
        )


    def publish(
        self,
        exchange,
        routing_key,
        message,
    ):

        self.channel.basic_publish(
            exchange=exchange,
            routing_key=routing_key,
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=2,
            ),
        )


    def create_queue(
        self,
        queue_name,
    ):

        self.channel.queue_declare(
            queue=queue_name,
            durable=True,
        )


    def bind_queue(
        self,
        queue_name,
        exchange,
        routing_key,
    ):

        self.channel.queue_bind(
            queue=queue_name,
            exchange=exchange,
            routing_key=routing_key,
        )