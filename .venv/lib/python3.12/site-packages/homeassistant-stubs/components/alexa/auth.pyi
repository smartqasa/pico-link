from .const import STORAGE_ACCESS_TOKEN as STORAGE_ACCESS_TOKEN, STORAGE_REFRESH_TOKEN as STORAGE_REFRESH_TOKEN
from .diagnostics import async_redact_lwa_params as async_redact_lwa_params
from _typeshed import Incomplete
from homeassistant.const import CONF_CLIENT_ID as CONF_CLIENT_ID, CONF_CLIENT_SECRET as CONF_CLIENT_SECRET
from homeassistant.core import HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers import aiohttp_client as aiohttp_client
from homeassistant.helpers.storage import Store as Store
from typing import Any

_LOGGER: Incomplete
LWA_TOKEN_URI: str
LWA_HEADERS: Incomplete
PREEMPTIVE_REFRESH_TTL_IN_SECONDS: int
STORAGE_KEY: str
STORAGE_VERSION: int
STORAGE_EXPIRE_TIME: str

class Auth:
    hass: Incomplete
    client_id: Incomplete
    client_secret: Incomplete
    _prefs: dict[str, Any] | None
    _store: Store
    _get_token_lock: Incomplete
    def __init__(self, hass: HomeAssistant, client_id: str, client_secret: str) -> None: ...
    async def async_do_auth(self, accept_grant_code: str) -> str | None: ...
    @callback
    def async_invalidate_access_token(self) -> None: ...
    async def async_get_access_token(self) -> str | None: ...
    @callback
    def is_token_valid(self) -> bool: ...
    async def _async_request_new_token(self, lwa_params: dict[str, str]) -> str | None: ...
    async def async_load_preferences(self) -> None: ...
    async def _async_update_preferences(self, access_token: str, refresh_token: str, expire_time: str) -> None: ...
