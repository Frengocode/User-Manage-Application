from src.application.modules.user.domain.entities.user import User
from src.application.modules.user.interfaces.services.iuser_service import IUserService
from src.application.modules.user.domain.value_objects.id import Id
from src.application.modules.user.dto.response.response import SUser
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class GetUserUseCase:
    service: IUserService

    async def execute(self, user_id: int) -> Optional[SUser]:
        user: Optional[User] = await self.service.get_user(id=Id(user_id))
        return SUser.model_validate(user)
