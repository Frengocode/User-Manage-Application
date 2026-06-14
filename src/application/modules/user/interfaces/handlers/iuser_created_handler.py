from typing import Protocol

from src.application.modules.user.interfaces.events.payload.user_created_payload import (
    UserCreatedEventPayload,
)
from src.application.modules.user.interfaces.events.user_created_event import (
    IUserCreatedEvent,
)


class IUserCreatedEventHandler(Protocol):
    async def handle(self, payload: UserCreatedEventPayload) -> None: ...
