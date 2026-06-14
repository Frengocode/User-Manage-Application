from typing import Optional, Protocol

from src.application.modules.user.dto.request.request import SGetAuthUserRequest
from src.application.modules.user.dto.response.response import SUser


class IGetAuthUserUseCase(Protocol):
    async def execute(self, request: SGetAuthUserRequest) -> Optional[SUser]:
        """Get auth User"""
