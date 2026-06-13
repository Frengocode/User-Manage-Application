from dishka import FromDishka
from fastapi import APIRouter

from src.application.modules.user.dto.request.request import SCreateUserRequest
from src.application.modules.user.dto.response.response import SUser
from src.application.modules.user.use_cases.create_user import CreateUserUseCase

users_api_v1_router: APIRouter = APIRouter(
    prefix="/users/api/v1", tags=["Users api v1"]
)


@users_api_v1_router.post("/", response_model=SUser, summary="Create's user")
async def create_user(
    request: SCreateUserRequest, use_case: FromDishka[CreateUserUseCase]
) -> SUser:
    return await use_case.execute(request=request)
