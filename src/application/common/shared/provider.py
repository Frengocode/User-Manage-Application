import logging

import aioredis
from aio_pika import Connection
from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from src.application.common.shared.config.config import Settings
from src.application.common.shared.database.sqlalchemy.sqlalchemy_database import (
    engine, session_factory)
from src.application.common.shared.exception.system.system_exception import \
    SystemCrashException
from src.application.utils.utils import get_logger

logger: logging.Logger = get_logger(__name__, logging.INFO)


class SharedProvider(Provider):

    @provide(scope=Scope.APP)
    async def get_db_session(self, settings: Settings) -> AsyncSession:
        try:
            async with engine(settings) as conn:
                await conn.run_sync(lambda sync_conn: sync_conn.execute("SELECT 1"))
            session: AsyncSession = session_factory(settings)
            return session
        except Exception as e:
            logger.error(f"Can't reach to database : {e}")
            raise SystemCrashException()

    @provide(scope=Scope.APP)
    def get_settings(self) -> Settings:
        return Settings()

    @provide(scope=Scope.APP)
    async def get_redis_connection(self, settings: Settings):
        try:
            redis = await aioredis.from_url(
                settings.redis.REDIS_URL.get_secret_value(),
                encoding="utf-8",
                decode_responses=True,
            )
            return redis
        except Exception as e:
            logger.error(f"Can't reach to Redis %s ", e)
            raise SystemCrashException()

    @provide(scope=Scope.APP)
    async def get_rabbitmq_connection(self, settings: Settings) -> Connection:
        try:
            connection: None = await Connection.connect(
                settings.rabbitmq.RABBITMQ_URL.get_secret_value(),
                timeout=30,
            )
            return connection
        except Exception as e:
            logger.error(f"Can't reach to RabbitMQ %s ", e)
            raise SystemCrashException()
