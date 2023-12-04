""" SpaConnectionError covers error messages coming from the Arctic Spa web API. """
import email.message
from http import HTTPStatus
from urllib.error import HTTPError

from arcticspas.types import Response

from .const import _url


class SpaConnectionError(HTTPError):
    def __init__(self, response: Response):
        msg = email.message.Message()
        for k, v in response.headers.items():
            msg.set_raw(k, v)
        super().__init__(_url, response.status_code, HTTPStatus(response.status_code).phrase, msg, None)
