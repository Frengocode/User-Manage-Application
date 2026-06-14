from typing import Optional

from pydantic import BaseModel


class SRefreshToken(BaseModel):
    refresh_token: str
    type: Optional[str] = "refresh"


class SAccessToken(BaseModel):
    access_token: str
    type: Optional[str] = "beaerer"


class SLogin(BaseModel):
    access_token: SAccessToken
    refresh_token: SRefreshToken
