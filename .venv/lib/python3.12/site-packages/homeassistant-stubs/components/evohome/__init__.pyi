import evohomeasync as ev1
import evohomeasync2 as evo
from .const import ACCESS_TOKEN as ACCESS_TOKEN, ACCESS_TOKEN_EXPIRES as ACCESS_TOKEN_EXPIRES, ATTR_DURATION_DAYS as ATTR_DURATION_DAYS, ATTR_DURATION_HOURS as ATTR_DURATION_HOURS, ATTR_DURATION_UNTIL as ATTR_DURATION_UNTIL, ATTR_SYSTEM_MODE as ATTR_SYSTEM_MODE, ATTR_ZONE_TEMP as ATTR_ZONE_TEMP, CONF_LOCATION_IDX as CONF_LOCATION_IDX, DOMAIN as DOMAIN, EvoService as EvoService, REFRESH_TOKEN as REFRESH_TOKEN, SCAN_INTERVAL_DEFAULT as SCAN_INTERVAL_DEFAULT, SCAN_INTERVAL_MINIMUM as SCAN_INTERVAL_MINIMUM, STORAGE_KEY as STORAGE_KEY, STORAGE_VER as STORAGE_VER, USER_DATA as USER_DATA
from .coordinator import EvoBroker as EvoBroker
from .helpers import dt_aware_to_naive as dt_aware_to_naive, dt_local_to_aware as dt_local_to_aware, handle_evo_exception as handle_evo_exception
from _typeshed import Incomplete
from homeassistant.const import ATTR_ENTITY_ID as ATTR_ENTITY_ID, CONF_PASSWORD as CONF_PASSWORD, CONF_SCAN_INTERVAL as CONF_SCAN_INTERVAL, CONF_USERNAME as CONF_USERNAME, Platform as Platform
from homeassistant.core import HomeAssistant as HomeAssistant, ServiceCall as ServiceCall, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.discovery import async_load_platform as async_load_platform
from homeassistant.helpers.dispatcher import async_dispatcher_send as async_dispatcher_send
from homeassistant.helpers.service import verify_domain_control as verify_domain_control
from homeassistant.helpers.storage import Store as Store
from homeassistant.helpers.typing import ConfigType as ConfigType
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator as DataUpdateCoordinator
from typing import Any, Final

_LOGGER: Incomplete
CONFIG_SCHEMA: Final[Incomplete]
RESET_ZONE_OVERRIDE_SCHEMA: Final[Incomplete]
SET_ZONE_OVERRIDE_SCHEMA: Final[Incomplete]

class EvoSession:
    hass: Incomplete
    _session: Incomplete
    _store: Incomplete
    client_v2: evo.EvohomeClient | None
    _tokens: dict[str, Any]
    client_v1: ev1.EvohomeClient | None
    session_id: str | None
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def authenticate(self, username: str, password: str) -> None: ...
    async def _load_auth_tokens(self, username: str) -> None: ...
    async def save_auth_tokens(self) -> None: ...

async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool: ...
@callback
def setup_service_functions(hass: HomeAssistant, broker: EvoBroker) -> None: ...
