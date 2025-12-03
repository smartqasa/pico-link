import httpx
from .const import XML_MIME_TYPES as XML_MIME_TYPES
from _typeshed import Incomplete
from homeassistant.core import HomeAssistant as HomeAssistant
from homeassistant.helpers import template as template
from homeassistant.helpers.httpx_client import create_async_httpx_client as create_async_httpx_client
from homeassistant.helpers.json import json_dumps as json_dumps
from homeassistant.util.ssl import SSLCipherList as SSLCipherList

DEFAULT_TIMEOUT: int
_LOGGER: Incomplete

class RestData:
    _hass: Incomplete
    _method: Incomplete
    _resource: Incomplete
    _encoding: Incomplete
    _auth: Incomplete
    _headers: Incomplete
    _params: Incomplete
    _request_data: Incomplete
    _timeout: Incomplete
    _verify_ssl: Incomplete
    _ssl_cipher_list: Incomplete
    _async_client: httpx.AsyncClient | None
    data: str | None
    last_exception: Exception | None
    headers: httpx.Headers | None
    def __init__(self, hass: HomeAssistant, method: str, resource: str, encoding: str, auth: httpx.DigestAuth | tuple[str, str] | None, headers: dict[str, str] | None, params: dict[str, str] | None, data: str | None, verify_ssl: bool, ssl_cipher_list: str, timeout: int = ...) -> None: ...
    def set_payload(self, payload: str) -> None: ...
    @property
    def url(self) -> str: ...
    def set_url(self, url: str) -> None: ...
    def data_without_xml(self) -> str | None: ...
    async def async_update(self, log_errors: bool = True) -> None: ...
