from src.application.common.shared.exception.base import BaseHTTPException


class SystemCrashException(BaseHTTPException):
    """Exception for case, if system is currently unavailable."""

    def __init__(
        self, detail: str = "System is currently unavailable. Please try again later."
    ) -> None:
        super().__init__(status_code=503, detail=detail)
