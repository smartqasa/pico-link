from .const import DOMAIN as DOMAIN
from .coordinator import ESPHomeDashboardCoordinator as ESPHomeDashboardCoordinator
from _typeshed import Incomplete
from homeassistant.config_entries import ConfigEntryState as ConfigEntryState, SOURCE_REAUTH as SOURCE_REAUTH
from homeassistant.const import EVENT_HOMEASSISTANT_STOP as EVENT_HOMEASSISTANT_STOP
from homeassistant.core import CALLBACK_TYPE as CALLBACK_TYPE, Event as Event, HomeAssistant as HomeAssistant, callback as callback
from homeassistant.helpers.aiohttp_client import async_get_clientsession as async_get_clientsession
from homeassistant.helpers.singleton import singleton as singleton
from homeassistant.helpers.storage import Store as Store
from typing import Any

_LOGGER: Incomplete
KEY_DASHBOARD_MANAGER: str
STORAGE_KEY: str
STORAGE_VERSION: int

async def async_setup(hass: HomeAssistant) -> None: ...
async def async_get_or_create_dashboard_manager(hass: HomeAssistant) -> ESPHomeDashboardManager: ...

class ESPHomeDashboardManager:
    _hass: Incomplete
    _store: Store[dict[str, Any]]
    _data: dict[str, Any] | None
    _current_dashboard: ESPHomeDashboardCoordinator | None
    _cancel_shutdown: CALLBACK_TYPE | None
    def __init__(self, hass: HomeAssistant) -> None: ...
    async def async_setup(self) -> None: ...
    @callback
    def async_get(self) -> ESPHomeDashboardCoordinator | None: ...
    async def async_set_dashboard_info(self, addon_slug: str, host: str, port: int) -> None: ...

@callback
def async_get_dashboard(hass: HomeAssistant) -> ESPHomeDashboardCoordinator | None: ...
async def async_set_dashboard_info(hass: HomeAssistant, addon_slug: str, host: str, port: int) -> None: ...
