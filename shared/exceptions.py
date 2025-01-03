from typing import Any


class ExceptionMapper(Exception):
    pass


class ResponseMapperException(ExceptionMapper):
    def __init__(self, data: Any):
        self.data = data


class ValidationError(ExceptionMapper): ...


class TokenExpiredError(ExceptionMapper):
    pass


class InvalidTokenError(ExceptionMapper):
    pass
