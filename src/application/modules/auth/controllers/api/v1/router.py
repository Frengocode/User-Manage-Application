from typing import Annotated, Optional

from dishka.integrations.fastapi import FromDishka, inject
from fastapi import APIRouter, Depends, Path, security

from src.application.modules.auth.dto.responses.response import SAccessToken, SLogin
from src.application.modules.auth.use_cases.login import LoginUseCase
from src.application.modules.auth.use_cases.refresh_token import RefreshTokenUseCase

auth_api_v1_router: APIRouter = APIRouter(prefix="/auth/api/v1", tags=["Auth Service"])


@auth_api_v1_router.post(
    "/login",
    response_model=SLogin,
    summary="Generates and returns access_token and refresh_token",
)
@inject
async def login(
    form: Annotated[security.OAuth2PasswordRequestForm, Depends()],
    use_case: FromDishka[LoginUseCase],
) -> Optional[SLogin]:
    return await use_case.execute(form=form)


@auth_api_v1_router.post(
    "/refresh-token/{token}",
    response_model=SAccessToken,
    summary="Generates new access_token using refresh_token",
)
@inject
async def refresh_token(
    token: Annotated[str, Path(...)], use_case: FromDishka[RefreshTokenUseCase]
) -> SAccessToken:
    return await use_case.execute(token=token)
