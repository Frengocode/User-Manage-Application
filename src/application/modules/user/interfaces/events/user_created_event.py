from typing import Protocol

from src.application.modules.user.interfaces.events.payload.user_created_payload import (
    UserCreatedEventPayload,
)


class IUserCreatedEvent(Protocol):
    async def publish_event(self, payload: UserCreatedEventPayload) -> None: ...

    """ Publishes event into (Kafka, rabbitmq, and others) """
