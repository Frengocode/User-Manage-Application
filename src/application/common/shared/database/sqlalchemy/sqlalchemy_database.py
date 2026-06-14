from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import DeclarativeBase

from src.application.common.shared.config.config import settings

engine: AsyncEngine = create_async_engine(
    settings.postgresql.PG_URL.get_secret_value(),
)

session_factory: async_sessionmaker[AsyncSession] = async_sessionmaker(bind=engine)


class SQLAlchemyBase(DeclarativeBase):
    pass
