import logging
from dataclasses import dataclass
from typing import List, Optional

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects.role import RoleEnum
from src.application.modules.user.dto.request.request import SGetUsersRequest
from src.application.modules.user.dto.response.response import SUser
from src.application.modules.user.exceptions.exceptions import AccessDeniedExceptionHTTP
from src.application.modules.user.interfaces.services.iuser_service import IUserService
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class GetUsersUseCase:
    service: IUserService

    async def execute(
        self, current_user: SUser, request: SGetUsersRequest
    ) -> Optional[List[SUser]]:

        if current_user.role == RoleEnum.ADMIN:
            users: Optional[List[User]] = await self.service.get_users(
                pagination=request
            )
            return [SUser.cls(user) for user in users]

        log.info("Allowed only for admins not for users")
        raise AccessDeniedExceptionHTTP()
