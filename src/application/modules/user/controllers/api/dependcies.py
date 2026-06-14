from dishka.integrations.fastapi import inject, FromDishka
from typing import Annotated, Optional
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from src.application.common.shared.config.config import settings
from src.application.modules.user.interfaces.use_cases.iget_user import IGetUserUseCase
from src.application.modules.user.dto.response.response import SUser
from src.application.utils.utils import get_logger
from jose import jwt
import logging

log: logging.Logger = get_logger(__name__)

oauth2_bearer: OAuth2PasswordBearer = OAuth2PasswordBearer(settings.auth.AUTH_LOGIN_URL)


@inject
async def get_current_user(
    token: Annotated[str, Depends(oauth2_bearer)],
    get_user_use_case: FromDishka[IGetUserUseCase],
) -> Optional[SUser]:

    payload = jwt.decode(
        token=token,
        key=settings.auth.JWT_SECRET_KEY.get_secret_value(),
        algorithms=settings.auth.JWT_ALGORITHM,
    )
    user_id = payload["sub"]
    log.info("Current was successfully getted %s", user_id)

    return await get_user_use_case.execute(user_id)
