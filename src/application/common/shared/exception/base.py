from dataclasses import dataclass

from fastapi.exceptions import HTTPException


class BaseHTTPException(HTTPException):
    status_code: int = 500
    detail: str = "Internal server error"

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail)
