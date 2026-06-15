from src.application.common.shared.exception.base import BaseHTTPException


class ExistUserExceptionHTTP(BaseHTTPException):
    status_code: int = 400
    detail: str = "User already exist by this email"


class InvalidNameExceptionHTTP(BaseHTTPException):
    status_code: int = 400
    detail: str = "Name can't be linger than 10 words"


class InvalidSurnameExceptionHTTP(BaseHTTPException):
    status_code: int = 400
    detail: str = "Surname can't be linger than 10 words"


class UserNotFoundExceptionHTTP(BaseHTTPException):
    status_code: int = 404
    detail: str = "User not found"


class AccessDeniedExceptionHTTP(BaseHTTPException):
    status_code: int = 403
    detail: str = "Access Denied"


class InvalidDataExceptionHTTP(BaseHTTPException):
    status_code: int = 400
    detail: str = "Invalid email or password"


class ExpiredTokenExceptionHTTP(BaseHTTPException):
    status_code: int = 400
    detail: str = "Expired token"
