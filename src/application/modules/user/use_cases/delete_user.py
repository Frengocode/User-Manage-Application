import logging
from dataclasses import dataclass
from typing import Optional

from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.value_objects import id, role
from src.application.modules.user.dto.response.response import SUser
from src.application.modules.user.exceptions.exceptions import AccessDeniedExceptionHTTP
from src.application.modules.user.interfaces.services.iuser_service import IUserService
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class DeleteUserUseCase:
    service: IUserService

    async def execute(self, current_user: SUser, user_id: str) -> Optional[SUser]:

        # Verifies exist of user
        await self.service.get_user(id=id.Id(user_id))

        if current_user.role != role.RoleEnum.ADMIN:
            log.info("Only admin can delete user")
            raise AccessDeniedExceptionHTTP()

        deleted_user: User = await self.service.delete_user(user_id=id.Id(user_id))
        log.info("User was deleted successfully %s ", user_id)
        return SUser.cls(deleted_user)
