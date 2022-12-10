from enum import Enum

from typing import Any, Dict

from starlette.exceptions import HTTPException


class StatusCodes(int, Enum):
    """
    Subset of suitable HTTP status codes that are good fit to describe the scenario of the custom exceptions.
    """

    NO_CONTENT = 204
    BAD_REQUEST = 400
    NOT_AUTHORIZED = 401
    NOT_FOUND = 404
    NOT_ACCEPTABLE = 406
    REQUEST_TIMEOUT = 408
    EXPECTATION_FAILED = 412
    UNPROCESSABLE_ENTITY = 422
    INTERNAL_SERVER_ERROR = 500
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504


class BaseHttpException(HTTPException):
    status_code: int = None
    detail: str = None
    headers: Dict[str, Any] = None

    def __init__(self):
        super().__init__(status_code=self.status_code, detail=self.detail, headers=self.headers)


class CustomException(BaseHttpException):
    status_code = 400
    detail = 'Invalid Input'
