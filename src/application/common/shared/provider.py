import logging
from typing import AsyncIterable

from dishka import Provider, Scope, provide
from faststream.rabbit import RabbitBroker
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from src.application.common.shared.auth.infrastructure.hash.bcrypt_hash import \
    BcryptHash
from src.application.common.shared.auth.infrastructure.token.access_token_generator import \
    AccessTokenGenerator
from src.application.common.shared.auth.infrastructure.token.refresh_token_generator import \
    RefreshTokenGenerator
from src.application.common.shared.auth.interfaces.hash.ihash import IHash
from src.application.common.shared.auth.interfaces.token.refresh_token_generator import \
    IRefreshTokenGenerator
from src.application.common.shared.auth.interfaces.token.token_generator import \
    ITokenGenerator
from src.application.common.shared.config.config import Settings
from src.application.common.shared.database.sqlalchemy.sqlalchemy_database import (
    engine, session_factory)
from src.application.common.shared.exception.system.system_exception import \
    SystemCrashException
from src.application.utils.utils import get_logger

logger: logging.Logger = get_logger(__name__)


class SharedProvider(Provider):

    @provide(scope=Scope.REQUEST)
    async def get_session(
        self,
    ) -> AsyncIterable[AsyncSession]:
        async with session_factory() as session:
            yield session

    @provide(scope=Scope.APP)
    def get_settings(self) -> Settings:
        return Settings()

    @provide(scope=Scope.APP)
    async def get_redis_connection(self, settings: Settings) -> Redis:
        try:
            redis = await Redis.from_url(
                settings.redis.REDIS_URL.get_secret_value(),
            )
            return redis
        except Exception as e:
            logger.error(f"Can't reach to Redis %s ", e)
            raise SystemCrashException()

    @provide(scope=Scope.APP)
    async def get_rabbitmq_connection(self, settings: Settings) -> RabbitBroker:
        try:
            broker: RabbitBroker = RabbitBroker(
                settings.rabbitmq.RABBITMQ_URL.get_secret_value()
            )
            await broker.connect()
            return broker
        except Exception as e:
            logger.error(f"Can't reach to RabbitMQ %s ", e)
            raise SystemCrashException()

    @provide(scope=Scope.APP)
    def bcrypt_hash(self) -> IHash:
        return BcryptHash()

    @provide(scope=Scope.APP)
    def access_token_generator(self) -> ITokenGenerator:
        return AccessTokenGenerator()

    @provide(scope=Scope.APP)
    def refresh_token_generator(self) -> IRefreshTokenGenerator:
        return RefreshTokenGenerator()
