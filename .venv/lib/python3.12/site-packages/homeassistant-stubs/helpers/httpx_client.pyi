import httpx
from .frame import warn_use as warn_use
from _typeshed import Incomplete
from collections.abc import Callable as Callable, Coroutine
from homeassistant.const import APPLICATION_NAME as APPLICATION_NAME, EVENT_HOMEASSISTANT_CLOSE as EVENT_HOMEASSISTANT_CLOSE, __version__ as __version__
from homeassistant.core import Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.loader import bind_hass as bind_hass
from homeassistant.util.hass_dict import HassKey as HassKey
from homeassistant.util.ssl import SSLCipherList as SSLCipherList, client_context as client_context, create_no_verify_ssl_context as create_no_verify_ssl_context
from typing import Any, Self

KEEP_ALIVE_TIMEOUT: int
DATA_ASYNC_CLIENT: HassKey[httpx.AsyncClient]
DATA_ASYNC_CLIENT_NOVERIFY: HassKey[httpx.AsyncClient]
DEFAULT_LIMITS: Incomplete
limits: Incomplete
SERVER_SOFTWARE: Incomplete
USER_AGENT: str

@callback
@bind_hass
def get_async_client(hass: HomeAssistant, verify_ssl: bool = True) -> httpx.AsyncClient: ...

class HassHttpXAsyncClient(httpx.AsyncClient):
    async def __aenter__(self) -> Self: ...
    async def __aexit__(self, *args: object) -> None: ...

@callback
def create_async_httpx_client(hass: HomeAssistant, verify_ssl: bool = True, auto_cleanup: bool = True, ssl_cipher_list: SSLCipherList = ..., **kwargs: Any) -> httpx.AsyncClient: ...
@callback
def _async_register_async_client_shutdown(hass: HomeAssistant, client: httpx.AsyncClient, original_aclose: Callable[[], Coroutine[Any, Any, None]]) -> None: ...
