from typing import Optional, Protocol

from src.application.modules.user.dto.response.response import SAccountConfirmation


class IUserCache(Protocol):
    async def set_confirmation_data(
        self, data: SAccountConfirmation, token: str
    ) -> None: ...

    """ Set's AccountConfirmation data by generated token """

    async def get_confirmation_data(
        self, token: str
    ) -> Optional[SAccountConfirmation]: ...

    """ Get's AccountConfirmation data by generated token """
