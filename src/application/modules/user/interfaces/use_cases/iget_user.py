from typing import Protocol, Optional
from src.application.modules.user.dto.response.response import SUser


class IGetUserUseCase(Protocol):

    async def execute(self, user_id: int) -> Optional[SUser]: ...
