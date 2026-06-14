import logging
from dataclasses import dataclass
from typing import Optional

from redis.asyncio import Redis

from src.application.modules.user.constants.constants import (
    ACCOUNT_CONFIRMATION_CACHE_KEY,
)
from src.application.modules.user.dto.response.response import SAccountConfirmation
from src.application.modules.user.interfaces.cache.iuser_cache import IUserCache
from src.application.utils.utils import get_logger

log: logging.Logger = get_logger(__name__)


@dataclass(frozen=True)
class UserCache(IUserCache):
    redis: Redis

    async def set_confirmation_data(
        self, data: SAccountConfirmation, token: str
    ) -> None:
        key: str = ACCOUNT_CONFIRMATION_CACHE_KEY.format(token=token)
        await self.redis.set(name=key, value=data.model_dump_json(), ex=300)
        log.info("Account confirmation was saved into cache %s", key)

    async def get_confirmation_data(self, token: str) -> Optional[SAccountConfirmation]:
        key: str = ACCOUNT_CONFIRMATION_CACHE_KEY.format(token=token)
        cached_data: Optional[SAccountConfirmation] = await self.redis.get(name=key)
        if cached_data:
            log.info("Getting AccountCorfimation data from cache by key %s", key)
            return cached_data
