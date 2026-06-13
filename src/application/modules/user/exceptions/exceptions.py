from src.application.common.shared.exception.base import BaseHTTPException


class ExistUserExceptionHTTP(BaseHTTPException):
    status_code: int = 400
    detail: str = "User already exist by this email"
