from fastapi import FastAPI

from api.router import router
from common.config.logging_config import configure_logging
from common.messaging.rabbitmq import RabbitMQClient
from common.messaging.exchanges import (
    COMMANDS_EXCHANGE,
    EVENTS_EXCHANGE,
)

configure_logging()

app = FastAPI()

app.include_router(router)
""" 
@app.on_event("startup")
def startup():

    rabbit = RabbitMQClient()

    rabbit.create_exchange(
        COMMANDS_EXCHANGE,
        exchange_type="topic",
    )

    rabbit.create_exchange(
        EVENTS_EXCHANGE,
        exchange_type="topic",
    ) """