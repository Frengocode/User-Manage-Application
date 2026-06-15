import logging
from dataclasses import dataclass
from typing import Optional

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.id import Id
from src.application.modules.user.dto.response.response import (
    SAccountConfirmation,
    SUser,
)
from src.application.modules.user.exceptions.exceptions import ExpiredTokenExceptionHTTP
from src.application.modules.user.interfaces.cache.iuser_cache import IUserCache
from src.application.modules.user.interfaces.services.iuser_service import IUserService
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class ActivateUserUseCase:
    service: IUserService
    cache: IUserCache

    async def execute(self, token: str) -> Optional[SUser]:
        cached_data: Optional[SAccountConfirmation] = (
            await self.cache.get_confirmation_data(token=token)
        )
        if cached_data:
            user: Optional[User] = await self.service.get_user(id=Id(cached_data.id))
            activated_user: User = await self.service.activate_user(user=user)
            log.info("User was activated %s", activated_user.id)
            return SUser.cls(activated_user)

        raise ExpiredTokenExceptionHTTP()
