from typing import Optional

from pydantic import BaseModel


class SAccessToken(BaseModel):
    access_token: str
    type: Optional[str] = "bearer"


class SLogin(BaseModel):

    access_token: str
    refresh_token: str
    type: Optional[str] = "bearer"
