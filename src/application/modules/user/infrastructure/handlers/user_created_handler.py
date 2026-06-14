import logging
import uuid
from dataclasses import dataclass

from src.application.modules.user.constants.constants import ACCOUNT_CONFIRMATION_BODY
from src.application.modules.user.dto.response.response import SAccountConfirmation
from src.application.modules.user.interfaces.cache.iuser_cache import IUserCache
from src.application.modules.user.interfaces.confirmation.confirmation import (
    IAccountConfirmation,
)
from src.application.modules.user.interfaces.events.payload.user_created_payload import (
    UserCreatedEventPayload,
)
from src.application.modules.user.interfaces.handlers.iuser_created_handler import (
    IUserCreatedEventHandler,
)
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class UserCreatedEventHandler(IUserCreatedEventHandler):
    cache: IUserCache
    account_confirmation_sender: IAccountConfirmation

    async def handle(self, payload: UserCreatedEventPayload) -> None:
        token: str = str(uuid.uuid4())

        await self.account_confirmation_sender.send_confirmation(
            recipient=payload.email,
            subject="Account Confirmation",
            body=ACCOUNT_CONFIRMATION_BODY.format(token=token),
        )

        confirmation_data: SAccountConfirmation = SAccountConfirmation(id=payload.id)
        await self.cache.set_confirmation_data(confirmation_data)
        log.info("[UserCreatedEvent] was succesfully handled %s", payload)
