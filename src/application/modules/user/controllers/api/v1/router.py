from typing import Annotated, Optional

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends, Path

from src.application.modules.user.controllers.api.dependcies import get_current_user
from src.application.modules.user.dto.request.request import SCreateUserRequest
from src.application.modules.user.dto.response.response import SUser
from src.application.modules.user.interfaces.use_cases.iget_user import IGetUserUseCase
from src.application.modules.user.use_cases.create_user import CreateUserUseCase

users_api_v1_router: APIRouter = APIRouter(
    prefix="/users/api/v1", tags=["Users api v1"]
)


@users_api_v1_router.post("/", response_model=SUser, summary="Create's user")
@inject
async def create_user(
    request: SCreateUserRequest, use_case: FromDishka[CreateUserUseCase]
) -> SUser:
    return await use_case.execute(request=request)


@users_api_v1_router.get(
    "/{user_id}", response_model=SUser, summary="Get's user by his id"
)
@inject
async def get_user(
    user_id: Annotated[str, Path(...)], use_case: FromDishka[IGetUserUseCase]
) -> Optional[SUser]:
    return await use_case.execute(user_id=user_id)


@users_api_v1_router.get("/me/get", response_model=SUser, summary="Get's current user")
@inject
async def get_user_me(
    current_user: Annotated[SUser, Depends(get_current_user)],
) -> Optional[SUser]:
    return current_user
