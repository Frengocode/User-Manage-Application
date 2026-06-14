from typing import Annotated, Optional

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Path

from src.application.modules.user.dto.request.request import SCreateUserRequest
from src.application.modules.user.dto.response.response import SUser
from src.application.modules.user.use_cases.create_user import CreateUserUseCase
from src.application.modules.user.use_cases.get_user import GetUserUseCase

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
    user_id: Annotated[str, Path(...)], use_case: FromDishka[GetUserUseCase]
) -> Optional[SUser]:
    return await use_case.execute(user_id=user_id)
