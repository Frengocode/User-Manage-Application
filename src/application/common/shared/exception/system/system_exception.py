from src.application.common.shared.exception.base import BaseHTTPException


class SystemCrashException(BaseHTTPException):
    """Exception for case, if system is currently unavailable."""

    status_code: int = 503
    detail: str = "System is currently unavailable. Please try again later"
