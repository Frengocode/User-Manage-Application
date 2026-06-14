from typing import Optional

from pydantic import BaseModel


class SRefreshTOken(BaseModel):
    refresh_token: str
    type: Optional[str] = "refresh"


class SLogin(BaseModel):
    access_token: str
    type: Optional[str] = "bearer"
