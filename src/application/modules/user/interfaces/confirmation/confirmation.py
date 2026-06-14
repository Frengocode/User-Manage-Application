from typing import Protocol

from src.application.modules.user.domain.value_objects import email


class IAccountConfirmation(Protocol):

    async def send_confirmation(
        self,
        recipient: str,
        subject: str,
        body: str,
    ) -> None: ...

    """ Send's confirmation into account """
