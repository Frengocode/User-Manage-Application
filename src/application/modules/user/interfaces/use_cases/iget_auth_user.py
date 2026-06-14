from typing import Optional, Protocol

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects import email, password
from src.application.modules.user.dto.request.request import \
    SGetAuthUserRequest


class IGetAuthUserUseCase(Protocol):
    async def execute(
        self, email: email.Email, password: password.Password
    ) -> Optional[User]:
        """Get auth User"""
