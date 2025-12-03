from _typeshed import Incomplete
from aiohttp.web import Application as Application
from aiohttp.web_urldispatcher import AbstractResource as AbstractResource
from homeassistant.const import HTTP_HEADER_X_REQUESTED_WITH as HTTP_HEADER_X_REQUESTED_WITH
from homeassistant.core import callback as callback
from homeassistant.helpers.http import AllowCorsType as AllowCorsType, KEY_ALLOW_ALL_CORS as KEY_ALLOW_ALL_CORS, KEY_ALLOW_CONFIGURED_CORS as KEY_ALLOW_CONFIGURED_CORS
from typing import Final

ALLOWED_CORS_HEADERS: Final[list[str]]
VALID_CORS_TYPES: Final[Incomplete]

@callback
def setup_cors(app: Application, origins: list[str]) -> None: ...
