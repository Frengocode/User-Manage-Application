from dishka import Provider, Scope, provide
from faststream.rabbit import RabbitBroker
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.shared.auth.interfaces.hash.ihash import IHash
from src.application.modules.user.infrastructure.cache.user_cache import UserCache
from src.application.modules.user.infrastructure.confirmation.account.account_confirmation import (
    AccountConfirmation,
)
from src.application.modules.user.infrastructure.events.rabbitmq.user_created_event import (
    UserCreatedEventRabbitMQ,
)
from src.application.modules.user.infrastructure.handlers.user_created_handler import (
    UserCreatedEventHandler,
)
from src.application.modules.user.infrastructure.repository.sqlalchemy.user_repository import (
    SQLALchemyUserRepository,
)
from src.application.modules.user.infrastructure.service.user_service import UserService
from src.application.modules.user.interfaces.cache.iuser_cache import IUserCache
from src.application.modules.user.interfaces.confirmation.confirmation import (
    IAccountConfirmation,
)
from src.application.modules.user.interfaces.events.user_created_event import (
    IUserCreatedEvent,
)
from src.application.modules.user.interfaces.handlers.iuser_created_handler import (
    IUserCreatedEventHandler,
)
from src.application.modules.user.interfaces.repository.iuser_repository import (
    IUserRepository,
)
from src.application.modules.user.interfaces.services.iuser_service import IUserService
from src.application.modules.user.interfaces.use_cases.iget_auth_user import (
    IGetAuthUserUseCase,
)
from src.application.modules.user.interfaces.use_cases.iget_user import IGetUserUseCase
from src.application.modules.user.use_cases.activate_user import ActivateUserUseCase
from src.application.modules.user.use_cases.create_user import CreateUserUseCase
from src.application.modules.user.use_cases.delete_user import DeleteUserUseCase
from src.application.modules.user.use_cases.get_auth_user import GetAuthUserUseCase
from src.application.modules.user.use_cases.get_user import GetUserUseCase
from src.application.modules.user.use_cases.get_users import GetUsersUseCase
from src.application.modules.user.use_cases.update_user import UpdateUserUseCase


class UserProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def create_user_use_case(
        self, service: IUserService, event: IUserCreatedEvent
    ) -> CreateUserUseCase:
        return CreateUserUseCase(service=service, event=event)

    @provide(scope=Scope.REQUEST)
    def get_user_use_case(self, service: IUserService) -> IGetUserUseCase:
        return GetUserUseCase(service=service)

    @provide(scope=Scope.REQUEST)
    def get_user_repository(self, session: AsyncSession) -> IUserRepository:
        return SQLALchemyUserRepository(session=session)

    @provide(scope=Scope.REQUEST)
    def get_user_service(
        self, hasher: IHash, repository: IUserRepository
    ) -> IUserService:
        return UserService(hasher=hasher, repository=repository)

    @provide(scope=Scope.REQUEST)
    def get_user_created_event(self, broker: RabbitBroker) -> IUserCreatedEvent:
        return UserCreatedEventRabbitMQ(broker=broker)

    @provide(scope=Scope.REQUEST)
    def get_auth_user_use_case(
        self, hasher: IHash, service: IUserService
    ) -> IGetAuthUserUseCase:
        return GetAuthUserUseCase(service=service, hasher=hasher)

    @provide(scope=Scope.REQUEST)
    def get_users_use_case(self, service: IUserService) -> GetUsersUseCase:
        return GetUsersUseCase(service=service)

    @provide(scope=Scope.REQUEST)
    def update_user_use_case(self, service: IUserService) -> UpdateUserUseCase:
        return UpdateUserUseCase(service=service)

    @provide(scope=Scope.REQUEST)
    def delete_user_use_case(self, service: IUserService) -> DeleteUserUseCase:
        return DeleteUserUseCase(service=service)

    @provide(scope=Scope.REQUEST)
    def get_user_cache(self, redis: Redis) -> IUserCache:
        return UserCache(redis=redis)

    @provide(scope=Scope.REQUEST)
    def get_account_confirmation(self) -> IAccountConfirmation:
        return AccountConfirmation()

    @provide(scope=Scope.REQUEST)
    def get_user_created_event_handler(
        self, cache: IUserCache, account_confirmation_sender: IAccountConfirmation
    ) -> IUserCreatedEventHandler:
        return UserCreatedEventHandler(
            cache=cache, account_confirmation_sender=account_confirmation_sender
        )

    @provide(scope=Scope.REQUEST)
    def activate_account_use_case(
        self, service: IUserService, cache: IUserCache
    ) -> ActivateUserUseCase:
        return ActivateUserUseCase(service=service, cache=cache)
