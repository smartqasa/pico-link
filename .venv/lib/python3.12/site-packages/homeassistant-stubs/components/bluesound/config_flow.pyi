from .const import DOMAIN as DOMAIN
from .media_player import DEFAULT_PORT as DEFAULT_PORT
from .utils import format_unique_id as format_unique_id
from _typeshed import Incomplete
from homeassistant.components import zeroconf as zeroconf
from homeassistant.config_entries import ConfigFlow as ConfigFlow, ConfigFlowResult as ConfigFlowResult
from homeassistant.const import CONF_HOST as CONF_HOST, CONF_PORT as CONF_PORT
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from pyblu import SyncStatus as SyncStatus
from typing import Any

_LOGGER: Incomplete

class BluesoundConfigFlow(ConfigFlow, domain=DOMAIN):
    VERSION: int
    MINOR_VERSION: int
    _host: str | None
    _port: Incomplete
    _sync_status: SyncStatus | None
    def __init__(self) -> None: ...
    async def async_step_user(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
    async def async_step_import(self, import_data: dict[str, Any]) -> ConfigFlowResult: ...
    async def async_step_zeroconf(self, discovery_info: zeroconf.ZeroconfServiceInfo) -> ConfigFlowResult: ...
    async def async_step_confirm(self, user_input: dict[str, Any] | None = None) -> ConfigFlowResult: ...
