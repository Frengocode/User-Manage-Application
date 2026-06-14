import logging
from dataclasses import dataclass
from typing import Optional

from src.application.common.shared.auth.interfaces.hash.ihash import IHash
from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.domain.exceptions.exceptions import (
    InvalidPasswordException,
)
from src.application.modules.user.domain.value_objects.email import Email
from src.application.modules.user.domain.value_objects.password import Password
from src.application.modules.user.dto.request.request import SGetAuthUserRequest
from src.application.modules.user.exceptions.exceptions import InvalidDataExceptionHTTP
from src.application.modules.user.interfaces.services.iuser_service import IUserService
from src.application.modules.user.interfaces.use_cases.iget_auth_user import (
    IGetAuthUserUseCase,
)
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class GetAuthUserUseCase(IGetAuthUserUseCase):
    service: IUserService
    hasher: IHash

    async def execute(self, email: Email, password: Password) -> Optional[User]:
        user: Optional[User] = await self.service.get_user_by_email(email=email)
        if self.hasher.verify_hash(password.value, user.password.value):
            return user
        log.error("Invalid email or password %s ", email.value)
        raise InvalidDataExceptionHTTP()
