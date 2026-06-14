import logging
from dataclasses import dataclass

from faststream.rabbit import RabbitBroker

from src.application.modules.user.interfaces.events.payload.user_created_payload import \
    UserCreatedEventPayload
from src.application.modules.user.interfaces.events.user_created_event import \
    IUserCreatedEvent
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class UserCreatedEventRabbitMQ(IUserCreatedEvent):
    broker: RabbitBroker

    async def publish_event(
        self,
        payload: UserCreatedEventPayload,
    ) -> None:
        log.info("Message pushed into rabbitmq %s", payload)
        await self.broker.publish(
            payload.model_dump(),
            routing_key="user.created",
        )
