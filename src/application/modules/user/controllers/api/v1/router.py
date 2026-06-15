from typing import Annotated, List, Optional

from dishka import FromDishka
from dishka.integrations.fastapi import inject
from fastapi import APIRouter, Depends, Path, Query

from src.application.modules.user.controllers.api.dependcies import get_current_user
from src.application.modules.user.dto.request.request import (
    SCreateUserRequest,
    SGetUsersRequest,
    SUpdateUserRequest,
)
from src.application.modules.user.dto.response.response import SUser
from src.application.modules.user.interfaces.use_cases.iget_user import IGetUserUseCase
from src.application.modules.user.use_cases.create_user import CreateUserUseCase
from src.application.modules.user.use_cases.delete_user import DeleteUserUseCase
from src.application.modules.user.use_cases.get_users import GetUsersUseCase
from src.application.modules.user.use_cases.update_user import UpdateUserUseCase
from src.application.modules.user.use_cases.activate_user import ActivateUserUseCase

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


@users_api_v1_router.get(
    "/users/get",
    response_model=List[SUser],
    summary="Get's list of users (Allowed only for admins)",
)
@inject
async def get_users(
    current_user: Annotated[SUser, Depends(get_current_user)],
    request: Annotated[SGetUsersRequest, Query(...)],
    use_case: FromDishka[GetUsersUseCase],
) -> Optional[List[SUser]]:
    return await use_case.execute(current_user=current_user, request=request)


@users_api_v1_router.put(
    "/update/{user_id}",
    response_model=SUser,
    summary="Updates user (Opportunity to update for anyone to update for anyone)",
)
@inject
async def update_user_use_case(
    user_id: Annotated[str, Path(...)],
    request: SUpdateUserRequest,
    use_case: FromDishka[UpdateUserUseCase],
) -> Optional[SUser]:
    return await use_case.execute(user_id=user_id, request=request)


@users_api_v1_router.delete(
    "/delete/{user_id}", response_model=SUser, summary="Deletes user (Only for admins)"
)
@inject
async def delete_user(
    user_id: Annotated[str, Path(...)],
    current_user: Annotated[SUser, Depends(get_current_user)],
    use_case: FromDishka[DeleteUserUseCase],
) -> Optional[SUser]:
    return await use_case.execute(current_user=current_user, user_id=user_id)


@users_api_v1_router.post(
    "/activate/{token}", response_model=SUser, summary="Activates user"
)
@inject
async def activate_user(
    token: Annotated[str, Path(...)], use_case: FromDishka[ActivateUserUseCase]
) -> Optional[SUser]:
    return await use_case.execute(token=token)
